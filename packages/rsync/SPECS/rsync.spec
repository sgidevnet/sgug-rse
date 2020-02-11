# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

%global _hardened_build 1

%define isprerelease 0

%if %isprerelease
%define prerelease pre1
%endif

Summary: A program for synchronizing files over a network
Name: rsync
Version: 3.1.3
Release: 9%{?dist}
URL: http://rsync.samba.org/

Source0: https://download.samba.org/pub/rsync/src/rsync-%{version}%{?prerelease}.tar.gz
Source1: https://download.samba.org/pub/rsync/src/rsync-patches-%{version}%{?prerelease}.tar.gz
Source2: rsyncd.socket
Source3: rsyncd.service
Source4: rsyncd.conf
Source5: rsyncd.sysconfig
Source6: rsyncd@.service

BuildRequires:  gcc
#BuildRequires: libacl-devel, libattr-devel, autoconf, popt-devel, systemd
BuildRequires: autoconf, popt-devel
Requires: zlib
#Added virtual provide for zlib due to https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries
Provides: bundled(zlib) = 1.2.8
License: GPLv3+

Patch0: rsync-man.patch
Patch1: rsync-noatime.patch
Patch2: rsync-3.0.6-iconv-logging.patch

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.

%package daemon
Summary: Service for anonymous access to rsync
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%{?systemd_requires}
%description daemon
Rsync can be used to offer read only access to anonymous clients. This
package provides the anonymous rsync service.

%prep
# TAG: for pre versions use

%if %isprerelease
%setup -q -n rsync-%{version}%{?prerelease}
%setup -q -b 1 -n rsync-%{version}%{?prerelease}
%else
%setup -q
%setup -q -b 1
%endif

chmod -x support/*

#Needed for compatibility with previous patched rsync versions
patch -p1 -i patches/acls.diff
patch -p1 -i patches/xattrs.diff

#Enable --copy-devices parameter
patch -p1 -i patches/copy-devices.diff

%patch0 -p1 -b .man
%patch1 -p1 -b .noatime
%patch2 -p1 -b .iconv

%build

%configure --with-included-popt
# --with-included-zlib=no temporary disabled because of #1043965

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall INSTALLCMD='install -p' INSTALLMAN='install -p'

#install -D -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_unitdir}/rsyncd.service
#install -D -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_unitdir}/rsyncd.socket
install -D -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/rsyncd.conf
#install -D -m644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/rsyncd
#install -D -m644 %{SOURCE6} $RPM_BUILD_ROOT/%{_unitdir}/rsyncd@.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc NEWS OLDNEWS README support/ tech_report.tex
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/rsyncd.conf.5*
%config(noreplace) %{_sysconfdir}/rsyncd.conf

#%files daemon
#%config(noreplace) %{_sysconfdir}/sysconfig/rsyncd
#%{_unitdir}/rsyncd.socket
#%{_unitdir}/rsyncd.service
#%{_unitdir}/rsyncd@.service

#%post daemon
#%systemd_post rsyncd.service

#%preun daemon
#%systemd_preun rsyncd.service

#%postun daemon
#%systemd_postun_with_restart rsyncd.service

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Michal Ruprich <mruprich@redhat.com> - 3.1.3-8
- Resolves: #1452187 - move man page rsyncd.conf(5) from rsync-daemon to rsync package
- Moving the config file as well

* Tue Mar 19 2019 Michal Ruprich <mruprich@redhat.com> - 3.1.3-7
- Resolves: #1683737 - [abrt] rsync: utf8_internal_loop(): rsync killed by SIGSEGV

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Michal Ruprich <mruprich@redhat.com> - 3.1.3-5
- Fix for rhbz#1586346 - rsyncd.service fails to start at boot if address is configured

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.3-3
- Escape macros in %%changelog

* Tue Jan 30 2018 Michal Ruprich <mruprich@redhat.com> - 3.1.3-2
- removed dependencies on systemd-units

* Mon Jan 29 2018 Michal Ruprich <mruprich@redhat.com> - 3.1.3-1
- new version 3.1.3
- Resolves CVE-2018-5764

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Michal Ruprich <mruprich@redhat.com> - 3.1.2-5
- Resolves: #1459681 - rpmscripts for rsyncd.service are in the wrong package

* Wed May 03 2017 Michal Ruprich <mruprich@redhat.com> - 3.1.2-4
- Added virtual provide for zlib library

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Luboš Uhliarik <luhliari@redhat.com> - 3.1.2-1
- new version 3.1.2

* Mon Nov 09 2015 Luboš Uhliarik <luhliari@redhat.com> - 3.1.1-8
- Resolves: #1233893 - added noatime patch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Pavel Šimerda <psimerda@redhat.com> - 3.1.1-5
- Related: #1123813 - fix rsync-daemon subpackage dependencywq

* Wed Aug 13 2014 Pavel Šimerda <psimerda@redhat.com> - 3.1.1-4
- Related: #1123813 - build rsync-daemon as noarch

* Tue Aug 12 2014 Pavel Šimerda <psimerda@redhat.com> - 3.1.1-3
- Resolves: #1123813 - Reduce dependencies

* Mon Aug  4 2014 Tom Callaway <spot@fedoraproject.org> - 3.1.1-2
- fix license handling

* Wed Jun 25 2014 Michal Luscon <mluscon@redhat.com> - 3.1.1-1
- Update to latest upstream version 3.1.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Michal Luscon <mluscon@redhat.com> - 3.1.0-5
- Reverted: #1050081 - breaks rawhide live installation

* Mon May 26 2014 Michal Luscon <mluscon@redhat.com> - 3.1.0-4
- Fixed: #1050081 undo the hard-link xattr optimization

* Wed Apr 16 2014 Michal Luscon <mluscon@redhat.com> - 3.1.0-3
- Fixed: CVE-2014-2855 - denial of service
- Reverted: compilation with system provided zlib (#1043965)

* Sun Oct 20 2013 Michal Lusocn <mluscon@redhat.com> - 3.1.0-2
- Update to latest upstream 3.1.0
- Fixed #1018520 - missing rsyncd@.service

* Wed Aug 07 2013 Michal Luscon <mluscon@redhat.com> - 3.1.0-1pre1
- Upstream 3.1.0 pre release
- Fixed: #495310 - rsync contains forked copy of zlib
- Fixed: #926459 - building aarch64
- Fixed: bogus dates in changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Michal Luscon <mluscon@redhat.com> - 3.0.9-11
- Add BuildRequires: systemd-units

* Mon Jun 17 2013 Michal Luscon <mluscon@redhat.com> - 3.0.9-10
- Fixed: #947765 - rsync daemon chooses wrong destination place

* Fri May 17 2013 Michal Luscon <mluscon@redhat.com> - 3.0.9-9
- Fix missing man page and help options

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Michal Luscon <mluscon@redhat.com> 3.0.9-6
- Systemd units for rsync

* Tue Oct 23 2012 Michal Luscon <mluscon@redhat.com> 3.0.9-5
- Reverted: #495310 - rsync contains forked copy of zlib

* Tue Oct 16 2012 Michal Luscon <mluscon@redhat.com> 3.0.9-4
- Fixed: #823088 - rsync loses track of files with different directory prefixes
- Fixed: #495310 - rsync contains forked copy of zlib

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 14 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 3.0.9-1
- Rebase to 3.0.9 (#741004)

* Wed Sep 14 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 3.0.8-2
- Fix security context of symbolic links (#709779)

* Tue Mar 29 2011 Vojtech Vitek <vvitek@redhat.com> - 3.0.8-1
- Rebase to 3.0.8, remove buffer overflow patch (#691362, #675036)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 29 2010 Jan Zeleny <jzeleny@redhat.com> - 3.0.7-3
- buffer overflow patch replaced by upstream version

* Fri Jan 22 2010 Jan Zeleny <jzeleny@redhat.com> - 3.0.7-2
- fixed issue with buffer overflow when using long filenames (#557916)

* Tue Jan 19 2010 Jan Zeleny <jzeleny@redhat.com> - 3.0.7-1
- rebased to 3.0.7

* Mon Dec 07 2009 Jan Zeleny <jzeleny@redhat.com> - 3.0.6-4
- applied patch to avoid retouching dir permissions (#542679)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009 Simo Sorce <ssorce@redhat.com> 3.0.6-2
- Final 3.0.6 release

* Thu May 21 2009 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.0.6-1pre1
- Enabled patches/copy-devices.diff patch (bz#494313)

* Wed Apr 15 2009 Simo Sorce <ssorce@redhat.com> 3.0.6-0pre1
- First 3.0.6 pre release
- Also change the spec to simplify releasing pre-releases

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan  1 2009 Simo Sorce <ssorce@redhat.com> 3.0.5-0.fc11
- New upstream bugfix release

* Mon Sep  8 2008 Simo Sorce <ssorce@redhat.com> 3.0.4-0.fc10
- New upstream bugfix release

* Mon Jun 30 2008 Simo Sorce <ssorce@redhat.com> 3.0.3-0.fc10
- New upstream release

* Tue Apr  8 2008 Simo Sorce <ssorce@redhat.com> 3.0.2-0.fc9
- Security release: http://rsync.samba.org/security.html#s3_0_2

* Fri Apr  4 2008 Simo Sorce <ssorce@redhat.com> 3.0.1-2.fc9
- Make sure support scripts are not executable so that no bad perl dependecies
  are created

* Fri Apr  4 2008 Simo Sorce <ssorce@redhat.com> 3.0.1-1.fc9
- Add NEWS and support/ scripts in the docs section
- 3.0.1 final

* Mon Mar 31 2008 Simo Sorce <ssorce@redhat.com> 3.0.1-0.3.pre3.fc9
- 3.0.1 pre release #3
- Fixes some annoying minor bugs (see release notes)

* Thu Mar 27 2008 Simo Sorce <ssorce@redhat.com> 3.0.1-0.2.pre2.fc9
- 3.0.1 pre release #2
- Fixes #439074

* Tue Mar 25 2008 Simo Sorce <ssorce@redhat.com> 3.0.1-0.1.pre1.fc9
- 3.0.1 pre release #1
- Fixes #438694

* Sun Mar  2 2008 Simo Sorce <ssorce@redhat.com> 3.0.0-1.fc9
- Final 3.0.0 release

* Sat Feb 23 2008 Simo Sorce <ssorce@redhat.com> 3.0.0-0.pre10.fc9
- Tenth preprelease of the 3.0.0 series

* Sat Feb 16 2008 Simo Sorce <ssorce@redhat.com> 3.0.0-0.pre9.fc9
- Ninth preprelease of the 3.0.0 series

* Sat Feb  2 2008 Simo Sorce <ssorce@redhat.com> 3.0.0-0.pre8.fc9
- Eight prerelease
- Add second source, now patches are in a separate file
- Add temporary fix to the xattrs.diff patch line as, in this version
  the patch contains one extra humk already contained in acls.diff

* Sat Oct 27 2007 Simo Sorce <ssorce@redhat.com> 3.0.0-0.pre4.fc9
- Fourth prerelease

* Mon Oct 15 2007 Simo Sorce <ssorce@redhat.com> 3.0.0-0.pre2.1.fc9
- Add support for IPv6 by default with xinetd

* Fri Oct 12 2007 Simo Sorce <ssorce@redhat.com> 3.0.0-0.pre2.fc9
- Second prerelease

* Wed Oct 10 2007 Simo Sorce <ssorce@redhat.com> 3.0.0-0.pre1.fc9
- New Major version prerelease

* Wed Sep 5 2007 Simo Sorce <ssorce@redhat.com> 2.6.9-3.fc8
- Add patch to fix crash bug with hardlinks and ACLs patches

* Mon Feb 19 2007 Adam Jackson <ajax@redhat.com> 2.6.9-2
- Add dist tag to Release to fix upgrades from FC5 or FC6.

* Mon Feb 19 2007 Simo Sorce <ssorce@redhat.com> - 2.6.9-2
- fix acl/xattr bug with --delete: (bz#229145)

* Wed Nov 22 2006 Florian La Roche <laroche@redhat.com> - 2.6.9-1
- update to 2.6.9

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.6.8-3.1
- rebuild

* Fri Jun 9 2006 Jay Fenlason <fenlason@redhat.com> 2.6.8-3
- Add my xattrs_bug patch to fix a bug where xattrs don't get sent correctly.
- Add BuildRequires to make sure libattr-devel and libacl-devel are avaliable
- replace --with... with --enable... so they actually work
- Add make, autoconf and gcc to BuildRequires

* Mon May 8 2006 Jay Fenlason <fenlason@redhat.com> 2.6.8-2
- New upstream release
- Use the upstream xattr patch instead of mine.  This closes
  bz#190208 CVE-2006-2083 rsync buffer overflow issue

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.6.6-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.6.6-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Jul 28 2005 Jay Fenlason <fenlason@redhat.com> 2.6.6-2
- New upstream release.  See the NEWS file for details.

* Thu Jun 2 2005 Jay Fenlason <fenlason@redhat.com> 2.6.5-2
- New upstream release

* Tue May 17 2005 Jay Fenlason <fenlason@redhat.com> 2.6.5-0.pre1.0
- new upstream pre-release

* Tue May 17 2005 Jay Fenlason <fenlason@redhat.com> 2.6.4-3
- Include the -address patch from upstream, to close
  bz#154752 Unable to use --address in client mode

* Thu Mar 31 2005 Jay Fenlason <fenlason@redhat.com> 2.6.4-2
- New upstream version

* Wed Mar 2 2005 Jay Fenlason <fenlason@redhat.com> 2.6.3-3
- bump release, rebuild with gcc4
- pass RPM_OPT_FLAGS to make

* Thu Feb 10 2005 Jay Fenlason <fenlason@redhat.com> 2.6.3-2
- Added my -xattr patch, which is based on the -acl patch.

* Thu Sep 30 2004 Jay Fenlason <fenlason@redhat.com> 2.6.3-1
- New upstream release.

* Tue Sep 21 2004 Jay Fenlason <fenlason@redhat.com> 2.6.3-0.pre2
- new upstream version.

* Tue Aug 17 2004 Jay Fenlason <fenlason@redhat.com> 2.6.3-0.pre1
- New upstream version with security fix for CAN-2004-0792
- This obsoletes the -lastdir-corruption patch.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 25 2004 Mark McLoughlin <markmc@redhat.com> - 2.6.2-1
- Backport fix for crasher when passing multiple directories of the same
  length (bug #123708)

* Fri Apr 30 2004 Jay Fenlason <fenlason@redhat.com> 2.6.2-0
- New upstream version to correct the problems with 2.6.1.
  This obsoletes all the patches to 2.6.1

* Thu Apr 29 2004 Jay Fenlason <fenlason@redhat.com> 2.6.1-1
- Rsync 2.6.1 final.
- Add a patch from Wayne Davison <wayned@samba.org> that fixes a
  use of uninitilized memory in the map_uid and map_gid functions.
- Add another patch from Wayne Davidson that fixes the -R option.
- Add a patch (extracted from a patch by Sami Farin
  <safari-rsync@safari.iki.fi>) to not ignore the return value
  of close().

* Thu Mar 25 2004 Jay Fenlason <fenlason@redhat.com> 2.6.1-0.pre1
- New upstream version

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan  5 2004 Jay Fenlason <fenlason@redhat.com> 2.6.0-0
- New upstream version, obsoletes the rsync-2.5.6-signal.patch

* Wed Dec  3 2003 Bill Nottingham <notting@redhat.com> 2.5.7-2
- rebuild

* Wed Dec  3 2003 Bill Nottingham <notting@redhat.com> 2.5.7-1
- update to 2.5.7

* Tue Aug 05 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-20
- rebuild in new build env

* Tue Aug 05 2003 Lon Hohberger <lhh@redhat.com> 2.5.6-19
- spec file fix

* Tue Aug 05 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-18
- rebuild in new build env

* Tue Aug 05 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-17
- fixed spec - added patch0 to prep.

* Tue Aug 05 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-16
- rebuild in new build env

* Mon Aug 04 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-15
- add rsync-2.5.6-signal.patch to fix kernel warnings that
  appear because socket.c sets SIGCHLD to SIG_IGN and then
  calls wait.  This is in response to bug#98740.  This patch
  *has* been committed to CVS upstream and will be in
  upstream rsync-2.5.7.

* Fri Jun 13 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-14
- build scratch - for compile warnings

* Fri Jun 13 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-13
- build scratch - for compile warnings

* Thu Jun 12 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-12
- rebuild in new build env

* Thu Jun 12 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-11
- removed rsync-2.5.6-sign.patch.  Upstream code
  incorporates signed vs unsigned changes.

* Wed Jun 11 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-10_CVSHEAD_signpatch
- build scratch - added rsync-2.5.6-sign.patch.

* Wed Jun 11 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-9_CVSHEAD_nopatches
- build scratch.

* Wed Jun 11 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-8
- build scratch - deleted rsync-2.5.6-sign.patch.

* Mon Jun 09 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-7
- rebuild in new build env

* Thu Jun 05 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-6
- removed patch rsync-2.5.4-maxdel.patch
- removed patch rsync-2.4.6-segv.patch
   - current 2.5.6 properly handles (no segfault) the situation
     (rsync '[a]') that caused a need for this patch.
- added patch rsync-2.5.6-sign.patch, which is a working
  subset of patches (that still apply) included in the original
  rsync-2.5.4-moresignage.patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 11 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-4
- rebuild in new build env

* Tue Mar 11 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-3
- fixed changelog comments

* Mon Mar 10 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-2
- rebuild in new build env

* Mon Mar 10 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.6-1
- update to 2.5.6 from upstream

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 17 2003 Hardy Merrill <hmerrill@redhat.com> 2.5.5-3
- fix spelling mistake in rsync.xinetd.  #66036 & dup #75006

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 2.5.5-2
- rebuild on all arches

* Mon Jun 24 2002 Bill Nottingham <notting@redhat.com> 2.5.5-1
- update to 2.5.5

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr 10 2002 Bill Nottingham <notting@redhat.com> 2.5.4-2
- upstream patches: fix accidental use of --whole-file, fix
  minor memory leak, and bad worst-case child kill behavior
- make passing -e to rsync:// URLs not cause an error exit (#62489)

* Wed Mar 13 2002 Bill Nottingham <notting@redhat.com> 2.5.4-1
- update to 2.5.4, do assorted patchmerging

* Wed Feb 20 2002 Bill Nottingham <notting@redhat.com>
- fix --address (#60127)
- call setgroups before dropping privs (<mkp@samba.org>)

* Mon Jan 28 2002 Bill Nottingham <notting@redhat.com>
- fix some errors in the unsigned patch

* Sun Jan 27 2002 Bill Nottingham <notting@redhat.com>
- rebuild to get proper LFS_CFLAGS

* Wed Jan 23 2002 Bill Nottingham <notting@redhat.com>
- fix some signed/unsigned issues (<krahmer@suse.de>)
- tweak ipv6 patch (#55337, <john.l.villalovos@intel.com>)
- make xinetd file %%config(noreplace)

* Fri Aug 17 2001 Bill Nottingham <notting@redhat.com>
- fix segfault on weird arguments (#51801)

* Tue Jul 24 2001 Bill Nottingham <notting@redhat.com>
- IPv6 patch (<pekkas@netcore.fi>) (#47780)

* Tue Jun 19 2001 Bill Nottingham <notting@redhat.com>
- add patch to fix hangs at end of sync, and other odd behaviors (#42111)

* Sat Sep 30 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add xinetd configuration

* Tue Sep 26 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.4.6

* Mon Jul 31 2000 Bill Nottingham <notting@redhat.com>
- update to 2.4.4 - fixes yet another problem with rsh transport

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- rebuild in new build env.

* Mon Apr 10 2000 Bill Nottingham <notting@redhat.com>
- update to 2.4.3

* Tue Apr  4 2000 Bill Nottingham <notting@redhat.com>
- update to 2.4.2

* Tue Mar  7 2000 Bill Nottingham <notting@redhat.com>
- fix maxdelete behavior so it isn't sent to older servers.

* Mon Jan 31 2000 Jeff Johnson <jbj@redhat.com>
- update to 2.4.1.

* Fri Dec 17 1999 Bill Nottingham <notting@redhat.com>
- update to 2.3.2

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- add "max. delete" patch to limit damage when server is hosed.

* Wed Apr 07 1999 Bill Nottingham <notting@redhat.com>
- update to 2.3.1.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Mar 16 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.3.0.

* Sat Mar 13 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.3.0 beta.

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- update to 2.2.1

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.1.1

* Mon Aug 17 1998 Erik Troan <ewt@redhat.com>
- updated to 2.1.0

* Thu Aug 06 1998 Erik Troan <ewt@redhat.com>
- buildrooted and attr-rophied
- removed tech-report.ps; the .tex should be good enough

* Mon Aug 25 1997 John A. Martin <jam@jamux.com>
- Built 1.6.3-2 after finding no rsync-1.6.3-1.src.rpm although there
  was an ftp://ftp.redhat.com/pub/contrib/alpha/rsync-1.6.3-1.alpha.rpm
  showing no packager nor signature but giving 
  "Source RPM: rsync-1.6.3-1.src.rpm".
- Changes from 1.6.2-1 packaging: added '$RPM_OPT_FLAGS' to make, strip
  to '%%build', removed '%%prefix'.

* Thu Apr 10 1997 Michael De La Rue <miked@ed.ac.uk>
- rsync-1.6.2-1 packaged.  (This entry by jam to credit Michael for the
  previous package(s).)
