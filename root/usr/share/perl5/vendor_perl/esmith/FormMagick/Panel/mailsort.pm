#----------------------------------------------------------------------
#  mailsorting.pm
#  support@dungog.net
#----------------------------------------------------------------------

package esmith::FormMagick::Panel::mailsort;

use strict;
use warnings;

use esmith::util;
use esmith::FormMagick;
use esmith::AccountsDB;
use esmith::ConfigDB;
use Unicode::IMAPUtf7;
use Unicode::String qw(utf8 latin1);

use Exporter;
use Carp qw(verbose);

use HTML::Tabulate;

our @ISA = qw(esmith::FormMagick Exporter);

our @EXPORT = qw();

our $db  = esmith::ConfigDB->open();
our $adb = esmith::AccountsDB->open();
our $pdb = esmith::ConfigDB->open('processmail') or die "Could not open processmail DB\n";

our $PanelUser = $ENV{'REMOTE_USER'} ||'';
$PanelUser = $1 if ($PanelUser =~ /^([a-z][\.\-a-z0-9]*)$/);

sub get_panel_user
{
    return $PanelUser;
}

sub get_full_name
{
    return  $adb->get_prop($PanelUser, "FirstName") . " " .
            $adb->get_prop($PanelUser, "LastName");
}

sub new {
    shift;
    my $self = esmith::FormMagick->new();
    $self->{calling_package} = (caller)[0];
    bless $self;
    return $self;
}

sub print_rules_table
{
    my $self = shift;
    my $q = $self->{cgi};

    my @rules = $pdb->get_all_by_prop(type => "$PanelUser");
    return $self->localise("NO_RULES") if (@rules == 0);

    my $rules_table =
    {
       title => $self->localise("CURRENT_RULES"),

       stripe => "#D4D0C8",

       fields => [ qw(b1 criterion b2 criterion2 deliver copy deliver2 Modify Remove) ],

       labels => 1,

       field_attr => {
                       b1            => {  label => $self->localise("BASIS")         },

                       criterion     => {  label => $self->localise("CRITERION")     },

                       b2            => {  label => $self->localise("2ND_BASIS")     },

                       criterion2    => {  label => $self->localise("2ND_CRITERION") },

                       deliver       => {  label => $self->localise("DESTINATION")   },

                       copy          => {  label => $self->localise("COPY")          },

                       deliver2      => {  label => $self->localise("DESTINATION")       },

                       Modify        => {
                                          label => $self->localise("MODIFY"),
                                          link  => \&modify_link
                                        },

                       Remove        => {
                                          label => $self->localise("REMOVE"),
                                          link  => \&remove_link
                                        },
                      }
    };

    my @data = ();
    my $a    = $self->localise('ACTION');
    my $b    = $self->localise('BASIS');
    my $c    = $self->localise('CRITERION');

    foreach my $rule (@rules)
    {
        my $key        = $rule->key;
        my $basis      = $rule->prop("basis")     || '';
        my $basis2     = $rule->prop("basis2")    || '';
        my $deliver    = $rule->prop("deliver")   || '';
        my $deliver2   = $rule->prop("deliver2")  || '';
        my $action     = $rule->prop("action")    || '';
        my $action2    = $rule->prop("action2")   || '';
        my $copy       = $rule->prop("copy")      || '';
        my $oldpmRule  = '';

        for ($basis, $basis2)
        {
         if ($_ eq '<')
         { $_ =  'sizelt'; }
         elsif ($_ eq '>')
         { $_ =  'sizegt'; }
        }

        my $b1    = $self->localise($basis);
        my $b2    = $self->localise($basis2);
        
        my $copyto     = $rule->prop("deliver2")  || '';
        if (($copy eq 'yes') && ($action2 eq 'inbox'))
        {  $copyto = 'inbox'; }

        $deliver = GetDisplayName($deliver);
        $deliver2 = GetDisplayName($deliver2);

        push @data,
            {
              key        => $rule->key,
              basis      => $basis,
              basis2     => $basis2,
              criterion  => $rule->prop("criterion")  || '',
              criterion2 => $rule->prop("criterion2") || '',
              deliver    => $deliver,
              deliver2   => $deliver2,
              action     => $action,
              action2    => $action2,
              copy       => $copy,
              Modify     => $self->localise('MODIFY'),
              Remove     => $self->localise('REMOVE'),
              b1         => $b1,
              b2         => $b2,
              a          => $a,
              b          => $b,
              c          => $c,
            }
    }

    my $t = HTML::Tabulate->new($rules_table);

    $t->render(\@data, $rules_table);
}

sub modify_or_create_description
{
    my $self = shift;
    my $q = $self->{cgi};

    my $key = $q->param('key');

    if ($key eq 'new')
    { return $self->localise('CREATE_RULE_DESCRIPTION'); }
    else
    { return $self->localise('MODIFY_RULE_DESCRIPTION'); }
}

sub priority
{
    my $self = shift;
    my $q = $self->{cgi};

    my $key = $q->param('key');

    if ($key eq 'new')
    { return ''; }
    else
    {
      my $start = ' <tr>
                     <td class="sme-noborders-label">' . $self->localise('PRIORITY') . '
                     <td class="sme-noborders-content"><INPUT VALUE="' . $key . '" NAME="key" TYPE="text" SIZE="40"></td>
                    </tr> ';
      return $start;
    }
}

sub filter_status
{
    my $self = shift;
    my $q = $self->{cgi};

    my $FilterType = $db->get_prop('qmail', "FilterType") || 'Disabled';

    if ($FilterType eq 'Disabled')
    {
      my $start = '<tr><td colspan="2"><p>' . 
                      $self->localise('FILTERTYPE_DISABLED') . 
                   '</p></td></tr> ';
    }
    else
    { return ''; }
}

sub user_status
{
    my $self = shift;
    my $q = $self->{cgi};

    my $MailFilter = $adb->get_prop($PanelUser, "MailFilter") || '';

    if ($MailFilter eq 'bypass')
    {
      my $start = '<tr><td colspan="2"><p>' .
                      $self->localise('USER_DISABLED') .
                  ' </p></td></tr> ';
    }
    else
    { return ''; }
}

sub modify_link  
{
    my ($data_item, $row, $field) = @_;

    return "userpanel-mailsort?" .
        join("&",
        "page=0",
        "page_stack=",
        "Next=Next",
        "key="        . $row->{key},
        "oldkey="     . $row->{key},
        "basis="      . $row->{basis},
        "basis2="     . $row->{basis2},
        "criterion="  . $row->{criterion},
        "criterion2=" . $row->{criterion2},
        "deliver="    . $row->{deliver},
        "deliver2="   . $row->{deliver2},
        "action="     . $row->{action},
        "action2="    . $row->{action2},
        "copy="       . $row->{copy},
        "wherenext=RULE_MODIFY");
}

sub remove_link
{
    my ($data_item, $row, $field) = @_;

    return "userpanel-mailsort?" .
        join("&",
        "page=0",
        "page_stack=",
        "Next=Next",
        "key="      . $row->{key},
        "desc="     . $row->{b} .' = '. $row->{basis}     . '<br>' .
                      $row->{c} .' = '. $row->{criterion} . '<br>' .
                      $row->{a} .' = '. $row->{action},
        "wherenext=RULE_REMOVE");
}

sub remove_rule
{
    my $self = shift;
    my $q = $self->{cgi};

    my $rule = $q->param('key');

    my $rec = $pdb->get($rule);
    $rec->delete;

    unless ( system ("/sbin/e-smith/signal-event mailsorting-conf $PanelUser") == 0 )
    { return $self->error('ERROR_UPDATING'); }

    return $self->success("SUCCESS");
}

sub save_rule
{
    my $self = shift;
    my $q = $self->{cgi};

    my $rule = $q->param ('key')  || '';
    if (($rule eq '') || ($rule eq 'new'))
    {
      my $random = int(rand(999999));
      $rule = $PanelUser.$random;
      $pdb->new_record($rule, { type => "$PanelUser" });
    }

    my $basis      = $q->param ('basis')     || '';
    my $basis2     = $q->param ('basis2')    || '';
    my $action     = $q->param ('action')     || '';
    my $action2    = $q->param ('action2')    || '';
    my $deliver    = $q->param ('deliver')    || '';
    my $deliver2   = $q->param ('deliver2')   || '';
    my $copy       = $q->param ('copy')       || '';
    my $oldkey     = $q->param ('oldkey')     || '';

    if ($basis eq 'sizelt')  { $basis  = '<'; }
    if ($basis eq 'sizegt')  { $basis  = '>'; }
    if ($basis2 eq 'sizelt') { $basis2 = '<'; }
    if ($basis2 eq 'sizegt') { $basis2 = '>'; }

    if ($copy eq 'no')       { $deliver2 = '';  $action2 = ''; }

    # keys are different but rule at least has part of users name so is likely changed
    if (($oldkey ne $rule) && ($oldkey =~ /$PanelUser/))
    {
        $pdb->new_record($rule, { type => "$PanelUser" });

        my $rec = $pdb->get($oldkey);
        $rec->delete;
    }

    foreach ("criterion","criterion2","action","action2","copy","basis","basis2","deliver","deliver2" )
    { $pdb->set_prop($rule, "$_", $q->param("$_")); }

    unless ( system ("/sbin/e-smith/signal-event mailsorting-conf $PanelUser") == 0 )
    { return $self->error('ERROR_UPDATING'); }

    return $self->success("SUCCESS");
}

sub GetDisplayName ($)
{
	my $s = shift;
	my $t = Unicode::IMAPUtf7->new();
	$s =~ s/(.*)//; # untaint it
	my $u = utf8($t->decode($1));
	return $u->latin1;
}

sub nonblankWithForward
{
    my $self = shift;
    my $q = $self->{cgi};

    my $action   = $q->param ('action')  || '';
    my $deliver  = $q->param ('deliver') || '';

    if ( $action ne 'delete')
    {
      if (not $deliver)
      { return "ERROR_FORWARD_NO_EMAIL"; }
      elsif (  $deliver =~ /^\s+$/ )
      { return "ERROR_FORWARD_NO_EMAIL"; }
      else
      { return "OK"; }
    }
    else { return "OK"; }
}

sub nonblankWithForward2
{
    my $self = shift;
    my $q = $self->{cgi};

    my $copy     = $q->param ('copy')     || '';
    my $action   = $q->param ('action2')  || '';
    my $deliver  = $q->param ('deliver2') || '';

    if (( $action ne 'delete') && ( $copy eq 'yes'))
    {
      if (not $deliver)
      { return "ERROR_FORWARD_NO_EMAIL"; }
      elsif (  $deliver =~ /^\s+$/ )
      { return "ERROR_FORWARD_NO_EMAIL"; }
      else
      { return "OK"; }
    }
    else { return "OK"; }
}

1;
