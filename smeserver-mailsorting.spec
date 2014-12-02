# $Id: smeserver-mailsorting.spec,v 1.7 2013/12/11 21:01:28 unnilennium Exp $
# Authority: dungog
# Name: Stephen Noble

Summary: Lets users configure procmail or maildrop rules.
%define name smeserver-mailsorting
Name: %{name}
%define version 1.4
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: GPL
URL: http://www.dungog.net/sme
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}
Requires:  e-smith-release >= 9.0,
Requires: perl-Unicode-IMAPUtf7
Requires: e-smith-formmagick >= 1.4.0-12
#Requires:  smeserver-userpanel, userpanel causes endless problems
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no

%description
SME Server enhancement to enable procmail or maildrop filtering for users.
Optionally provides user panels where users can create mail rules for themselves

%changelog
* Tue Dec 2 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.4-2.sme
- allow the possibility to use sieve script if no rules has matched.
- Code developed by <m.schuh@neckargeo.net> Mats Schuh

* Mon Jun 23 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.4-1.sme
- Initial release to sme9

* Wed Dec 11 2013 JP Pialasse <tests@pialasse.com> 1.2-45.sme
- fix bug as admin .procmail was not created [SME: 8023]

* Fri Nov 29 2013 JP Pialasse <tests@pialasse.com> 1.2-44.sme
- fix admin patch 

* Wed Nov 28 2013 Steph DL <stephdl@de-labrusse.fr> 1.2-43.sme
- fix  [SME: 8023] [SME: 8024]

* Thu Oct 09 2013 John Crisp <jcrisp@safeandsoundit.co.uk> 1.2-42.sme
- remove space from TO_ [SME: 6061] [SME: 2264]

* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.2-41.sme
- apply locale 2013-07-14 patch
- documentation fix [SME: 7586]
- copy keeped even if forward [SME: 6847]


* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 1.2-40.sme
- apply locale 2011-03-06 patch

* Sun May 23 2010 SME Translation Server <translations@contribs.org> 1.2-39.sme
- apply locale 2010-05-23 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 1.2-38.sme
- apply locale 2010-03-02 patch

* Tue Oct 27 2009 SME Translation Server <translations@contribs.org> 1.2-37.sme
- apply locale 2009-10-27 patch

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 1.2-36.sme
- apply locale 2009-08-24 patch

* Fri Jun 12 2009 Stephen Noble <support@dungog.net> 1.2-35
- don't escape spaces in folder names with zarafa enabled [SME: 5164]

* Wed May 20 2009 SME Translation Server <translations@contribs.org> 1.2-34.sme
- apply locale 2009-05-20 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 1.2-33.sme
- apply locale 2009-04-27 patch

* Sun Mar 22 2009 Stephen Noble <support@dungog.net> 1.2-32
-  qmail FilterOrder enabled lets maildrop filter before forwarding [SME: 5044]

* Tue Mar 03 2009 SME Translation Server  xyz   1.2-31
- apply locale 2009-03-03 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-30
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Sat Feb 21 2009 Stephen Noble <support@dungog.net> 1.2-29
- remove drop down to select folders [SME: 5016]

* Sat Feb 21 2009 Stephen Noble <support@dungog.net> 1.2-28
- procmail sort to zarafa folders if enabled [SME: 5016]

* Thu Jan  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-27
- Apply  1 Jan 2009 locale patch [SME: 4900]

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-26
- Apply 14 Oct 2008 locale patch

* Mon Sep 29 2008 Stephen Noble <support@dungog.net> - 1.2-25
- remove internal forwarding [SME: 4605]

* Sat Sep 27 2008 Stephen Noble <support@dungog.net> - 1.2-24
- move .qmail fragment after SME forwarding [SME: 4602]

* Sat Sep 27 2008 Stephen Noble <support@dungog.net> - 1.2-23
- Apply 27 Sep 2008 locale patch

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-22
- Apply 1 July 2008 locale patch

* Thu May 21 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-21
- Apply 21 May 2008 locale patch
- Updating the release number (it was lagging behind about 10)

* Mon May 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-20
- Apply 5 May 2008 locale patch

* Sun Apr 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-19
- Add common <base> tags to e-smith-formmagick's general

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-18
- Added 22 April 2008 locale patch

* Tue Apr 1 2008 Shad L. Lords <slords@mail.com> 1.2-17
- Update to UTF-8 translations

* Fri Mar 14 2008 Stephen Noble <support@dungog.net> - 1.2-16
- block generation of procmail/maildrop rules [SME: 4051]

* Fri Mar 14 2008 Stephen Noble <support@dungog.net> - 1.2-15
- update locale 2008-03-14

* Wed Mar 12 2008 Shad L. Lords <slords@mail.com> - 1.2-14
- Add requires for e-smith-formmagick for UTF-8 support [SME: 3858]

* Tue Mar 11 2008 Stephen Noble <support@dungog.net> - 1.2-13
- Add 2008-03-11 locale patch

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> - 1.2-12
- prepare en lexicons for pootle translations

* Tue Dec 25 2007 Stephen Noble <support@dungog.net> 1.2-11
- french translation fix

* Tue Dec 25 2007 Stephen Noble <support@dungog.net> 1.2-10
- add french translation, thanks Sylvain Gomez

* Mon Oct 29 2007 Stephen Noble <support@dungog.net> 1.2-9
- add spanish translation, thanks Normando Hall [SME 3503]

* Sun Jul 29 2007 Stephen Noble <support@dungog.net> 1.2-8
- Add Requires perl-Unicode-IMAPUtf7 [SME: 3218]

* Thu Jul 05 2007 Stephen Noble <support@dungog.net> 1.2-7
- touch processmail db, thanks dclarke

* Wed Jun 13 2007 Stephen Noble <stephen@dungog.net> 1.2-6
- add global maildrop delete duplicate db value

* Wed Jun 13 2007 Stephen Noble <stephen@dungog.net>
- update .tar.gz to current version

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sat Mar 17 2007 Stephen Noble <stephen@dungog.net>
- retry mail in .qmail [sme 2733]
- [1.2-5]

* Wed Feb 28 2007 Stephen Noble <stephen@dungog.net>
- remove Requires: smeserver-userpanel
- [1.2-4]

* Tue Jan 9 2007 Stephen Noble <support@dungog.net>
- remove .* after TO_ macro [sme 2264]
- Existing mail folders search improved [sme 2265]
- [1.2-3]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Mon Oct 30 2006  Stephen Noble <support@dungog.net>
- improved german support, thanks Dietmar
- Unicode-IMAPUtf7 support [sme 1446]
- [1.2-2]

* Sat Oct 21 2006 Stephen Noble <support@dungog.net>
- FormMagick version
- [1.2-1]

* Thu Aug 24 2006 Stephen Noble <support@dungog.net>
- remove strict check on mailrule criterion [sme 1643]
- fix log rotation
- maildrop matching improved, [sme 1642]
- allow for spaces in folder names for maildrop [sme 1640]
- [0.9-6]

* Sat May 6 2006 Stephen Noble <support@dungog.net>
- default shell for maildrop set to /bin/bash 
-  [contribs 1378] thanks mweinber neddix.de
- [0.9-5]

* Wed Apr 6 2006 Stephen Noble <support@dungog.net>
- delete duplicates 
-  globally enabled for procmail, works ok
-  per user for maildrop, worked ok for user A, but started deleting mail for user B
- [0.9-4]

* Thu Mar 9 2006 Stephen Noble <support@dungog.net>
- remove preun actions
- [0.9-3]

* Thu Mar 9 2006 Stephen Noble <support@dungog.net>
- Requires:  smeserver-userpanel
- bypass admin's .qmail
- [0.9-2]

* Sun Sep 25 2005  Stephen Noble <support@dungog.net>
- initial release
- [0.9-1]

%prep
%setup

%build
perl createlinks

LEXICONS=$(find root/etc/e-smith/{locale/,web/functions/} -type f )
for lexicon in $LEXICONS
do
    /sbin/e-smith/validate-lexicon $lexicon
done

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean

%pre
%preun

%post
#new installs
if [ $1 = 1 ] ; then
 echo ''
 echo '#############################################################'
 echo '  Please visit the url below to apprehend all the db commands'
 echo '  http://wiki.contribs.org/Mailsorting#Configuration         '
 echo '#############################################################'
 echo ''
fi

#upgrades (and new installs)
/bin/touch /home/e-smith/db/processmail
# this one is essential to avoid to lose mails !!!!
/sbin/e-smith/signal-event mailsorting-conf
if [ -d /etc/e-smith/events/conf-userpanel ] ; then
   /sbin/e-smith/signal-event conf-userpanel
fi

%postun
#uninstall
if [ $1 = 0 ] ; then

echo ''
echo '##################################'
echo 'to disable procmail or maildrop'
echo 'config delprop qmail FilterType'
echo 'signal-event email-update'
echo '##################################'
echo ''

 DBS=`find /home/e-smith/db/navigation -type f -name "navigation.*"`
 for db in $DBS ; do
          /sbin/e-smith/db $db delete userpanel-mailsort 2>/dev/null
	done
fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
