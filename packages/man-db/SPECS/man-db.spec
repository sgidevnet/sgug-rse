# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

%global cache %{_prefix}/var/cache/man
%global gnulib_ver 20140202

Summary: Tools for searching and reading man pages
Name: man-db
Version: 2.8.5
Release: 6%{?dist}
# GPLv2+ .. man-db
# GPLv3+ .. gnulib
License: GPLv2+ and GPLv3+
URL: http://www.nongnu.org/man-db/

Source0: http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1: man-db.crondaily
Source2: man-db.sysconfig
Source3: man-db-cache-update.service
Patch0: man-db-2.8.3-change-owner-of-man-cache.patch

# http://lists.nongnu.org/archive/html/man-db-devel/2017-01/msg00013.html
Patch1: man-db-2.7.6.1-fix-override-dir-handling.patch

Patch100: man-db.sgifixes.patch

Obsoletes: man < 2.0
Provides: man = %{version}
Provides: man-pages-reader = %{version}
# FPC exception for gnulib - copylib - https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = %{gnulib_ver}

Requires: coreutils, grep, groff-base, gzip, less
BuildRequires: gcc
#BuildRequires: systemd
BuildRequires: gdbm-devel, gettext, groff, less, libpipeline-devel, zlib-devel
#BuildRequires: po4a, perl-interpreter, perl-version
BuildRequires: perl-interpreter, perl-version

%description
The man-db package includes five tools for browsing man-pages:
man, whatis, apropos, manpath and lexgrog. man formats and displays
manual pages. whatis searches the manual page names. apropos searches the
manual page names and descriptions. manpath determines search path
for manual pages. lexgrog directly reads header information in
manual pages.

#%package cron
#Summary: Periodic update of man-db cache

#Requires: %{name} = %{version}-%{release}
#Requires: crontabs

#BuildArch: noarch

#%description cron
#This package provides periodic update of man-db cache.

%prep
%autosetup -p1

%build
%configure \
    --with-sections="1 1p 8 2 3 3p 3pm 4 5 6 7 9 0p n l p o 1x 2x 3x 4x 5x 6x 7x 8x" \
    --disable-setuid --disable-cache-owner \
    --with-browser=elinks --with-lzip=lzip \
    --with-override-dir=overrides
make CC="%{__cc} %{optflags}" %{?_smp_mflags} V=1

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

# move the documentation to the relevant place
mv $RPM_BUILD_ROOT%{_datadir}/doc/man-db/* ./

# remove zsoelim man page - part of groff package
#rm $RPM_BUILD_ROOT%{_datadir}/man/man1/zsoelim.1

# remove libtool archives
rm $RPM_BUILD_ROOT%{_libdir}/man-db/*.la

# install cache directory
install -d -m 0755  $RPM_BUILD_ROOT%{cache}

# install cron script for man-db creation/update
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
#install -D -p -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/man-db.cron

# config for cron script
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
#install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/man-db

# config for tmpfiles.d
#install -D -p -m 0644 init/systemd/man-db.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/.

# man-db-cache-update.service
#install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/man-db-cache-update.service

# Remove unused tmpfiles.d directory
rm -rf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d

# Remove wierd italian man pages at wrong level...
rm -rf $RPM_BUILD_ROOT%{_prefix}/man/it

# Remove zsoelim man pages handled by groff
rm $RPM_BUILD_ROOT%{_prefix}/man/man1/zsoelim.1

# Remove systemd things we don't want
rm -rf $RPM_BUILD_ROOT/lib

# Rewrite a hardcoded bash path
#perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" $RPM_BUILD_ROOT%{_prefix}/etc/cron.daily/man-db.cron

%find_lang %{name}
%find_lang %{name}-gnulib

# stop and disable timer from previous builds
#pre
#if [ -e /usr/lib/systemd/system/mandb.timer ]; then
#  if test -d /run/systemd; then
#	systemctl stop man-db.timer
#	systemctl -q disable man-db.timer
#  fi
#fi

# clear the old cache
%post
%{__rm} -rf %{cache}/*

# update cache
#transfiletriggerin -- %{_mandir}
#if [ -x /usr/bin/systemd-run -a -x /usr/bin/systemctl ]; then
#    /usr/bin/systemd-run /usr/bin/systemctl start man-db-cache-update >/dev/null 2>&1 || :
#fi

# update cache
#transfiletriggerpostun -- %{_mandir}
#if [ -x /usr/bin/systemd-run -a -x /usr/bin/systemctl ]; then
#    /usr/bin/systemd-run /usr/bin/systemctl start man-db-cache-update >/dev/null 2>&1 || :
#fi


%files -f %{name}.lang -f %{name}-gnulib.lang
%{!?_licensedir:%global license %%doc}
%license docs/COPYING
%doc README man-db-manual.txt man-db-manual.ps ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/man_db.conf
#%config(noreplace) %{_sysconfdir}/sysconfig/man-db
#%config(noreplace) %{_tmpfilesdir}/man-db.conf
#%{_unitdir}/man-db-cache-update.service
%{_sbindir}/accessdb
%{_bindir}/man
%{_bindir}/whatis
%{_bindir}/apropos
%{_bindir}/manpath
%{_bindir}/lexgrog
%{_bindir}/catman
%{_bindir}/mandb
%dir %{_libdir}/man-db
%{_libdir}/man-db/*.so
%dir %{_libexecdir}/man-db
%{_libexecdir}/man-db/globbing
%{_libexecdir}/man-db/manconv
%{_libexecdir}/man-db/zsoelim
%verify(not mtime) %dir %{cache}
# documentation and translation
%{_mandir}/man1/apropos.1*
%{_mandir}/man1/lexgrog.1*
%{_mandir}/man1/man.1*
%{_mandir}/man1/manconv.1*
%{_mandir}/man1/manpath.1*
%{_mandir}/man1/whatis.1*
%{_mandir}/man5/manpath.5*
%{_mandir}/man8/accessdb.8*
%{_mandir}/man8/catman.8*
%{_mandir}/man8/mandb.8*
#%lang(da)       %{_datadir}/man/da/man*/*
#%lang(de)       %{_datadir}/man/de/man*/*
#%lang(es)       %{_datadir}/man/es/man*/*
#%lang(fr)       %{_datadir}/man/fr/man*/*
#%lang(id)       %{_datadir}/man/id/man*/*
#%lang(it)       %{_datadir}/man/it/man*/*
#%lang(ja)       %{_datadir}/man/ja/man*/*
#%lang(nl)       %{_datadir}/man/nl/man*/*
#%lang(pl)       %{_datadir}/man/pl/man*/*
#%lang(pt_BR)    %{_datadir}/man/pt_BR/man*/*
#%lang(ru)       %{_datadir}/man/ru/man*/*
#%lang(sr)       %{_datadir}/man/sr/man*/*
#%lang(sv)       %{_datadir}/man/sv/man*/*
#%lang(tr)       %{_datadir}/man/tr/man*/*
#%lang(zh_CN)    %{_datadir}/man/zh_CN/man*/*

#%files cron
#%config(noreplace) %{_sysconfdir}/cron.daily/man-db.cron

%changelog
* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 2.8.5-6
- Remove hard coded shell paths, disable cron package

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Nikola Forró <nforro@redhat.com> - 2.8.4-3
- prioritize POSIX man pages over perl manuals
  resolves #1663919

* Wed Nov 07 2018 Nikola Forró <nforro@redhat.com> - 2.8.4-2
- get rid of hardcoded path

* Mon Jul 30 2018 Nikola Forró <nforro@redhat.com> - 2.8.4-1
- update to 2.8.4
  resolves #1609438

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.3-3
- Rebuild for new gdbm

* Fri Apr 06 2018 Nikola Forró <nforro@redhat.com> - 2.8.3-2
- fix version in the name of change-owner-of-man-cache patch

* Fri Apr 06 2018 Nikola Forró <nforro@redhat.com> - 2.8.3-1
- update to 2.8.3
  resolves #1564220

* Tue Feb 20 2018 Nikola Forró <nforro@redhat.com> - 2.7.6.1-15
- add missing gcc build dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Todd Zullinger <tmz@pobox.com> - 2.7.6.1-13
- Avoid noisy output from man-db-cache-update triggers

* Tue Jan 16 2018 Jiri Kucera <jkucera@redhat.com> - 2.7.6.1-12
- fix segmentation fault caused by 'man -D?'
  resolves: #1495507

* Tue Jan 16 2018 Nikola Forró <nforro@redhat.com> - 2.7.6.1-11
- rebuild with gdbm-1.14

* Tue Dec 19 2017 Nikola Forró <nforro@redhat.com> - 2.7.6.1-10
- fix failure of man-db-cache-update service when configured not to run
  resolves: #1526715

* Tue Nov 21 2017 Nikola Forró <nforro@redhat.com> - 2.7.6.1-9
- allow configuration of man-db-cache-update service through sysconfig
  resolves: #1514909

* Tue Nov 21 2017 Nikola Forró <nforro@redhat.com> - 2.7.6.1-8
- set group of /var/cache/man to root and drop setgid bit
  resolves: #1515823

* Thu Nov 16 2017 Nikola Forró <nforro@redhat.com> - 2.7.6.1-7
- make file trigger scriptlets not to fail in case systemd is unavailable
- drop systemd dependency

* Wed Nov 08 2017 Nikola Forró <nforro@redhat.com> - 2.7.6.1-6
- run cache update in a transient service using systemd-run
  resolves #1318058

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Nikola Forró <nforro@redhat.com> - 2.7.6.1-2
- set owner of man cache to root instead of man

* Thu Jan 19 2017 Nikola Forró <nforro@redhat.com> - 2.7.6.1-1
- update to 2.7.6.1
  resolves #1403618

* Mon Mar 14 2016 Nikola Forró <nforro@redhat.com> - 2.7.5-3
- suppress potential locale warning when installing with glibc-minimal-langpack
  resolves #1314633

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Nikola Forró <nforro@redhat.com> - 2.7.5-1
- update to 2.7.5
  resolves #1279867

* Tue Oct 13 2015 Nikola Forró <nforro@redhat.com> - 2.7.4-2
- add cron subpackage

* Tue Oct 13 2015 Nikola Forró <nforro@redhat.com> - 2.7.4-1
- update to 2.7.4
  resolves #1270078

* Mon Sep 21 2015 Nikola Forró <nforro@redhat.com> - 2.7.3-3
- fix replace.sed prerequisite syntax
  resolves #1263930

* Thu Sep 10 2015 Nikola Forró <nforro@redhat.com> - 2.7.3-2
- use file triggers instead of crontabs for updating cache

* Thu Sep 10 2015 Nikola Forró <nforro@redhat.com> - 2.7.3-1
- update to 2.7.3
  resolves #1261678

* Mon Aug 24 2015 Nikola Forró <nforro@redhat.com> - 2.7.2-3
- try to get terminal width from /dev/tty
  resolves #1255930

* Mon Aug 24 2015 Nikola Forró <nforro@redhat.com> - 2.7.2-2
- rebuilt with latest libpipeline

* Mon Aug 24 2015 Nikola Forró <nforro@redhat.com> - 2.7.2-1
- update to 2.7.2
  resolves #1256177

* Tue Aug 04 2015 Nikola Forró <nforro@redhat.com> - 2.7.1-8
- fix inaccurate description of "man -f"
  resolves #1249377

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 jchaloup <jchaloup@redhat.com> - 2.7.1-6
- Test for /run/systemd only if mandb.timer is actually installed
  resolves: #1223244

* Tue May 12 2015 Colin Walters <walters@redhat.com> - 2.7.1-5
- Test for /run/systemd to detect systemd state rather than invoking
  rpm in % pre - it is not really supported by rpm.

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.7.1-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Jan 02 2015 jchaloup <jchaloup@redhat.com> - 2.7.1-3
- switching back to crontabs
  resolves: #1177993
  resolves: #1171450
- rpm verify reports for /var/cache/man
  resolves: #1173496

* Thu Nov 13 2014 jchaloup <jchaloup@redhat.com> - 2.7.1-2
- src/man.c (do_extern): Pass the -l option through
  resolves: #1161747

* Wed Nov 12 2014 jchaloup <jchaloup@redhat.com> - 2.7.1-1
- update to 2.7.1
  resolves: #1163167

* Wed Oct 15 2014 jchaloup <jchaloup@redhat.com> - 2.7.0.2-5
- switch man and root in init/systemd/man-db.conf
  related: #1151558

* Mon Oct 13 2014 jchaloup <jchaloup@redhat.com> - 2.7.0.2-4
- preun missing condition on number of man-db packages installed
  related: #1151558

* Sun Oct 12 2014 jchaloup <jchaloup@redhat.com> - 2.7.0.2-3
- remove executable flag for *.service and *.timer file
  resolves: #1151558

* Wed Oct 08 2014 jchaloup <jchaloup@redhat.com> - 2.7.0.2-2
- replacing cron with systemd.timer
  resolves: #1148559
- adding zsoelim to {_libexecdir}/man-db/zsoelim
  related: #1145493

* Wed Oct 08 2014 jchaloup <jchaloup@redhat.com> - 2.7.0.2-1
- Update to 2.7.0.2
  resolves: #1145493

* Thu Sep 18 2014 jchaloup <jchaloup@redhat.com> - 2.6.7.1-7
- resolves: #1043401
  Don't store canonicalised versions of manpath elements

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 2.6.7.1-5
- fix license handling

* Tue Jul 01 2014 jchaloup <jchaloup@redhat.com> - 2.6.7.1-4
- related: #1110274
  swapping root for man in man-db.conf

* Wed Jun 25 2014 jchaloup <jchaloup@redhat.com> - 2.6.7.1-3
- resolves: #1110274
  Add systemd tmpfiles snippet to clean up old cat files after (upstream patch)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Peter Schiffer <pschiffe@redhat.com> - 2.6.7.1-1
- resolves: #1087279
  updated to 2.6.7.1

* Wed Feb 19 2014 Peter Schiffer <pschiffe@redhat.com> - 2.6.6-1
- resolves: #1057495
  updated to 2.6.6

* Wed Aug 07 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.6.5-3
- Add a missing requirement on crontabs to spec file
- Mark the cron job as config(noreplace)
- Fix RHBZ#989077

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Peter Schiffer <pschiffe@redhat.com> - 2.6.5-1
- updated to 2.6.5

* Tue Jun 25 2013 Peter Schiffer <pschiffe@redhat.com> - 2.6.4-1
- resolves: #977255
  updated to 2.6.4

* Mon Apr  8 2013 Peter Schiffer <pschiffe@redhat.com> - 2.6.3-6
- resolves: #948695
  fixed double free
- fixed certain man pages to match options with --help and --usage

* Thu Mar 21 2013 Peter Schiffer <pschiffe@redhat.com> - 2.6.3-5
- temporarily disabled one unstable unit test

* Thu Mar 21 2013 Peter Schiffer <pschiffe@redhat.com> - 2.6.3-4
- fixed some compiler warnings and memory leaks

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.3-2
- resolves: #870680
  use less as the default pager

* Wed Oct 24 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.3-1
- resolves: #858577
  updated to 2.6.3
- cleaned .spec file
- resolves: #855632
  fixed SIGABRT crash
- adds support for man-pages-overrides

* Tue Jul 31 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.2-5
- resolves: #841431
  ignore cached man pages if they don't exist anymore

* Fri Jul 20 2012 Dan Horák <dan[at]danny.cz> - 2.6.2-4
- fully patch the autotools files, fixes FTBFS due updated automake

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.2-2
- resolves: #829553
  clear the old man cache on install or update

* Tue Jul 10 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.2-1
- resolves: #833312
  update to 2.6.2
- resolves: #657409
  fixed warning when invoking col by the mandb program in cron
- resolves: #829935
  enabled support for man pages compressed with lzip
- resolves: #821778
  added virtual provides for bundled gnulib library
- resolves: #824825
  apropos returns correct exit code for invalid man page

* Tue Apr 24 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.1-4
- related: #693458
  updated patch for .so links because previous one wasn't working very well

* Tue Apr 24 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.1-3
- added autoconf, automake, libtool and gettext-devel to the build requires

* Tue Apr 24 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.1-2
- resolves: #677669
  added support for wildcards in path
- resolves: #693458
  fixed error with .so links

* Thu Apr 05 2012 Peter Schiffer <pschiffe@redhat.com> - 2.6.1-1
- resolves: #790771
  update to 2.6.1
- resolves: #806086
  removed hard-dependency on cron, update man db after install or update

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 05 2011 Peter Schiffer <pschiffe@redhat.com> - 2.6.0.2-3
- resolves: #702904
  fixed double free or corruption issue
- resolves: #739207
  require groff-base instead of groff
- rebuilt for gdbm-1.9.1-1

* Sun May 29 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.6.0.2-2
- Own the %%{_libdir}/man-db dir.

* Thu Apr 21 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.6.0.2-1
- update to 2.6.0.2
- remove obsolete patches
- add libpipe dependency

* Wed Mar 23 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-6
- Build with zlib support.
- Use elinks as default HTML browser.
   thanks Ville Skyttä

* Wed Mar 23 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-5
* Resolves: #684977
  backport upstream patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-3
- Resolves: #659292
  use ionice in man cron job

* Wed Nov 24 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-2
- Resolves: #655385 - use old format of nroff output

* Mon Nov 22 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.9-1
- update to 2.5.9

* Fri Oct  1 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-8
- add less buildrequire

* Wed Sep 29 2010 jkeating - 2.5.7-7
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-6
- Resolves: #630506 (change the description)
- minor spec file changes

* Mon Aug 30 2010 Dennis Gilmore <dennis@ausil.us> - 2.5.7-5
- Provide Versioned man

* Mon Aug 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-4
- remove obsolete conflict flag

* Mon Aug 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-3
- provides man tag
- resolves: #621688
  remove problematic man-pages (now in man-pages-de package)

* Fri Apr 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-2
- add conflicts tag

* Wed Feb 17 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.5.7-1
- initial build
