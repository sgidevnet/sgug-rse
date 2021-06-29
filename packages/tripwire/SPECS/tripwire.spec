%define		path_to_vi /bin/vi
%define		path_to_sendmail /usr/sbin/sendmail

Name:		tripwire
Version:	2.4.3.7
Release:	5%{?dist}
Summary:	IDS (Intrusion Detection System)

License:	GPLv2+
Source0:	https://github.com/Tripwire/%{name}-open-source/releases/download/%{version}/%{name}-open-source-%{version}.tar.gz
Source1:	tripwire.cron.in
Source3:	tripwire.gif
Source4:	twcfg.txt.in
Source5:	tripwire-setup-keyfiles.in
Source6:	twpol.txt.in
Source7:	README.Fedora.in
Source9:	License-Issues
URL:		https://github.com/Tripwire/%{name}-open-source/

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	openssl-devel
Requires(post):	sed


%description
Tripwire is a very valuable security tool for Linux systems, if  it  is
installed to a clean system. Tripwire should be installed  right  after
the OS installation, and before you have connected  your  system  to  a
network (i.e., before any possibility exists that someone  could  alter
files on your system).

When Tripwire is initially set up, it creates a database  that  records
certain file information. Then when it is run, it compares a designated
set of files and directories to the information stored in the database.
Added or deleted files are flagged and reported, as are any files  that
have changed from their previously recorded state in the database. When
Tripwire is run against system files  on  a  regular  basis,  any  file
changes will be spotted when Tripwire is run. Tripwire will report  the
changes, which will give system administrators a clue that they need to
enact damage control measures immediately if certain  files  have  been
altered.

%prep
%setup -q -n %{name}-open-source-%{version}
%{__cp} -p %{SOURCE3} .

%build
%configure --sysconfdir=%{_sysconfdir}/tripwire \
           path_to_vi=%{path_to_vi} \
           path_to_sendmail=%{path_to_sendmail}

%{__make} %{?_smp_mflags}

%install
%{__rm} -fr %{buildroot}

# Install the binaries.
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/siggen %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/tripwire %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/twadmin %{buildroot}%{_sbindir}
%{__install} -p -m755 bin/twprint %{buildroot}%{_sbindir}

# Install the man pages.
%{__mkdir_p} %{buildroot}%{_mandir}/{man4,man5,man8}
%{__install} -p -m644 man/man4/*.4 %{buildroot}%{_mandir}/man4/
%{__install} -p -m644 man/man5/*.5 %{buildroot}%{_mandir}/man5/
%{__install} -p -m644 man/man8/*.8 %{buildroot}%{_mandir}/man8/

# Create configuration files from templates.
%{__rm} -fr _tmpcfg
%{__mkdir} _tmpcfg
for infile in %{SOURCE1} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} ; do
	outfile=${infile##/*/}
	outfile=${outfile%.*n}
	cat ${infile} |\
	%{__sed} -e 's|@path_to_vi@|%{path_to_vi}|g' |\
	%{__sed} -e 's|@path_to_sendmail@|%{path_to_sendmail}|g' |\
	%{__sed} -e 's|@sysconfdir@|%{_sysconfdir}|g' |\
	%{__sed} -e 's|@sbindir@|%{_sbindir}|g' |\
	%{__sed} -e 's|@vardir@|%{_var}|g' >\
	_tmpcfg/${outfile}
done
%{__mv} _tmpcfg/{tripwire-setup-keyfiles,README.Fedora} .

# Create the reports directory.
%{__install} -d -m700 %{buildroot}%{_var}/lib/tripwire/report

# Install the cron job.
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/cron.daily
%{__install} -p -m755 _tmpcfg/tripwire.cron \
	%{buildroot}%{_sysconfdir}/cron.daily/tripwire-check
%{__rm} _tmpcfg/tripwire.cron

# Install configuration files.
%{__mkdir_p} %{buildroot}%{_sysconfdir}/tripwire
for file in _tmpcfg/* ; do
	%{__install} -p -m644 ${file} %{buildroot}%{_sysconfdir}/tripwire
done

# Install the keyfile setup script
%{__install} -p -m755 tripwire-setup-keyfiles %{buildroot}%{_sbindir}

# Fix permissions on documentation files.
%{__cp} -p %{SOURCE9} .
%{__chmod} 644 \
	ChangeLog COMMERCIAL COPYING TRADEMARK tripwire.gif \
	README.Fedora policy/policyguide.txt License-Issues


%post
# Set the real hostname in twpol.txt
%{__sed} -i -e "s|localhost|$HOSTNAME|g" %{_sysconfdir}/tripwire/twpol.txt


%files
%doc ChangeLog COMMERCIAL COPYING TRADEMARK tripwire.gif
%doc README.Fedora policy/policyguide.txt License-Issues
%attr(0700,root,root) %dir %{_sysconfdir}/tripwire
%config(noreplace) %{_sysconfdir}/tripwire/twcfg.txt
%config(noreplace) %{_sysconfdir}/tripwire/twpol.txt
%attr(0755,root,root) %{_sysconfdir}/cron.daily/tripwire-check
%attr(0700,root,root) %dir %{_var}/lib/tripwire
%attr(0700,root,root) %dir %{_var}/lib/tripwire/report
%{_mandir}/*/*
%attr(0755,root,root) %{_sbindir}/*


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.7-3
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1606572

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.7-1
- update to 2.4.3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.6-1
- update to 2.4.3.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.5-1
- update to 2.4.3.5

* Fri Mar 10 2017 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.4-1
- update to 2.4.3.4
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1429542
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1435181

* Sat Mar 04 2017 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.3-1
- update to 2.4.3.3

* Tue Feb 14 2017 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.2-3
- Fix #1421468 by removing defattr macro in files section
- Remove executable permission on 2 cpp files.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.2-1
- update to 2.4.3.2
- Remove personal config.guess
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=830999 

* Sat Apr 23 2016 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.1-1
- update to 2.4.3.1

* Sat Apr 16 2016 Didier Fabert <didier.fabert@gmail.com> - 2.4.3.0-1
- update to 2.4.3.0
- switch upstream from sourceforge to github (official sources)
- Patch to avoid narrowing errors

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.2.2-8
- Rebuilt for GCC 5 C++11 ABI change

* Tue Sep 16 2014 Moez Roy <moez.roy@gmail.com> - 2.4.2.2-7
- F21 build patch as suggested by Michael Schwendt on devel mailing list


* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar  5 2012 Tom Callaway <spot@fedoraproject.org> - 2.4.2.2-1
- update to 2.4.2.2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1.2-14
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.4.1.2-11
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 7 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 2.4.1.2-9
- Added support for /usr/lib64 & /usr/local/lib64

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 2.4.1.2-7
- rebuild with new openssl

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.1.2-6
- fix license tag

* Mon Feb 11 2008 Brandon Holbrook <fedora at theholbrooks.org> 2.4.1.2-5
- Rebuild for gcc-4.3

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.4.1.2-4
- Rebuild for deps

* Wed Aug 29 2007 Brandon Holbrook <fedora at theholbrooks.org> 2.4.1.2-3
- Pull in a new config.guess to properly detect ppc64 archs

* Wed Aug 29 2007 Brandon Holbrook <fedora at theholbrooks.org> 2.4.1.2-2
- Upgrade to 2.4.1.2

* Wed Feb 28 2007 Brandon Holbrook <fedora at theholbrooks.org> 2.4.1.1-1
- Upgrade to upstream 2.4.1.1 (obsoletes gcc4 patch)
- Merge quickstart.txt into README.Fedora and fix doc bug (#161764)

* Thu Dec 21 2006 Brandon Holbrook <fedora at theholbrooks.org> 2.4.0.1-4
- Don't print anything at install time

* Tue Dec 19 2006 Brandon Holbrook <fedora at theholbrooks.org> 2.4.0.1-3
- Changed defattr to 644,755
- removed BR: autoconf
- Inform users about README.Fedora instead of spamming the install
  with catting the whole file

* Wed Nov 15 2006 Brandon Holbrook <fedora at theholbrooks.org> 2.4.0.1-2
- chmod'ed /etc/tripwire to 0700
- Added sed to Requires(post)

* Tue Aug 22 2006 Brandon Holbrook <fedora at theholbrooks.org> 2.4.0.1-1.4
- Include COMMERCIAL file from upstream
- Print README.RPM on initial install
- Added _smp_mflags to make
- Removed ExclusiveArch: ix86
- Replaced 2.3 with 2.4 in tripwire.txt

* Tue Aug 22 2006 Brandon Holbrook <fedora at theholbrooks.org> 2.4.0.1-1.2
- Updated to 2.4.0.1

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jun 15 2004 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-20.fdr.1
- Revision bump to supersede Fedora Legacy
- Fixed a bogus entry in twpol.txt.in (modeprobe.conf -> modprobe.conf)

* Thu Jun 10 2004 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.9
- Applied Paul Herman's patch to fix a format string vulnerability in
 pipedmailmessage.cpp

* Sun Feb 29 2004 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.8
- Default policy overhaul
- Spec cleanup

* Sun Feb 22 2004 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.7
- Moved documentation data out of package description

* Sat Feb 21 2004 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.6
- Removed explicit Buildrequires gcc-c++

* Fri Feb 20 2004 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.5
- Finally moved twinstall.sh from the sysconfdir to the sbindir, since
  it is not a configuration file. Fixes Red Hat bug #61855
- Renamed twinstall.sh to tripwire-setup-keyfiles, since  the  name  is
  misleading. It is setting up keyfiles, not installing an  application
- Minor correction to twinstall.sh (now tripwire-setup-keyfiles), which
  made an incorrect reference to the site key rather than the local key
- Long overdue default policy update
- Added explicit Buildrequires gcc-c++, to satisfy mach

* Thu Feb 19 2004 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.4
- Fixed siggen.8 man page, broken command synopsis syntax. Submitted by
  doclifter
- Set real hostname in post, so  Tripwire  works  first  time,  without
  editing twpol.txt
- More accurate package summary
- Spec cleanup

* Fri Nov 28 2003 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.3
- Thanks to Michael Schwendt for really cleaning up the Spec file
- The remaining parts of the  original  tripwire-2.3.1-gcc3.patch  have
  now been implemented
- Debuginfo fully builds now

* Thu Nov 27 2003 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.2
- Removed version specific grep dependency, since grep >= 2.3 is common
- Added openssl-devel and autoconf to build dependencies
- The tripwire-jbj.patch is now confirmed merged with tw-20030919.patch
- Added RPM optimisation flags option, disabled  by  default  since  it
  breaks the code
- Fixed file permissions of packaged files

* Wed Nov 26 2003 Keith G. Robertson-Turner <tripwire-devel[AT]genesis-x.nildram.co.uk> 0:2.3.1-18.fdr.1
- Implemented Paul Herman's tw-20030919.patch
- Removed the fhs gcc3 and jbj patches, which are now  broken/obsoleted
  by the above
- Both the mkstemp and rfc822 patches are still implemented
- Build uses autoconf for now
- Spec file given complete overhaul for stricter compliance. More to do

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sat Nov 16 2002 Jeff Johnson <jbj@redhat.com> 2.3.1-16
- rebuild from cvs.
- comment out debug messages to achieve compilation.
- include policyguide.txt (#72259).
- use mkstemp, not mktemp.

* Fri Aug 02 2002 Mike A. Harris <mharris@redhat.com> 2.3.1-14
- Modified default sample twpol file to remove bogus warnings (#70502)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 2.3.1-13
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com> 2.3.1-12
- automated rebuild

* Wed May 22 2002 Mike A. Harris <mharris@redhat.com> 2.3.1-11
- Rebuilt in new build environment with gcc 3.1

* Tue Feb 26 2002 Mike A. Harris <mharris@redhat.com> 2.3.1-9
- Conditionalized gcc3 patch
- Added back the ExclusiveArch that is required but disappeared somewhere along
  the line.
- Rebuild in new build environment

* Thu Jan 31 2002 Mike A. Harris <mharris@redhat.com> 2.3.1-7
- Bump release and rebuild in new environment.
- (Elliot Lee) Add patch to make it build with gcc3.

* Thu Aug  9 2001 Nalin Dahyabhai <nalin@redhat.com> 2.3.1-5
- define USE_FHS when USES_FHS is defined, so that the database winds up
  in the right directory (#51332)
- update default twpol file to include files recently-added to the full
  installation tree

* Tue Jul 17 2001 Mike A. Harris <mharris@redhat.com> 2.3.1-4
- Applied bugfix for (#47276) to make tripwire email RFC822 compliant, using
  patch in bugreport from Michael Schwendt <mschwendt@yahoo.com>

* Tue Jul 10 2001 Mike A. Harris <mharris@redhat.com> 2.3.1-3
- Made package own dir /var/lib/tripwire

* Mon Jun 25 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.3.1-2

* Thu Mar  1 2001 Bill Nottingham <notting@redhat.com>
- rebuild, fix defattr. Weird.

* Tue Feb 27 2001 Nalin Dahyabhai <nalin@redhat.com>
- refresh from upstream
- modify the default policy to match the current tree more closely (#28744)
- make the text files 0644, not 0755
- defattr for the sake of the docs

* Wed Sep 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- change exclusivearch: i386 to exclusivearch: %%{ix86} (#17759)

* Wed Aug 23 2000 Than Ngo <than@redhat.com>
- remove copyleft information in specfile (Bug #16765)

* Tue Aug 22 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove duplicate source files
- sync up description with specspo

* Fri Aug 4 2000 Than Ngo <than@redhat.de>
- remove Vendor and Distribution from specfile (Bug #15246)

* Fri Aug 4 2000 Than Ngo <than@redhat.de>
- starts tripwire --check if it was configured before. (Bug #15384)

* Fri Aug 4 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix sense of checking for the database's existence in the cron job
- actually include twinstall.sh, twcfg.txt, twpol.txt

* Thu Aug 3 2000 Than Ngo <than@redhat.de>
- permission fix (bug #15246)

* Mon Jul 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- add quickstart docs (Ed)
- tweak description text (Ed)

* Thu Jul 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- update .spec file to follow RPM conventions
- add tripwire --check to cron.daily

