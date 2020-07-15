
# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name: gamin
Version: 0.1.10
Release: 35%{?dist}
Summary: Library providing the FAM File Alteration Monitor API
License: LGPLv2
URL: http://www.gnome.org/~veillard/gamin/
#some of the files (server/inotify-kernel.c) are GPLv2
#so https://fedoraproject.org/wiki/Licensing#GPL_Compatibility_Matrix
#says the whole is GPLv2
#License: GPLv2
Source0: http://ftp.gnome.org/pub/GNOME/sources/gamin/0.1/gamin-%{version}.tar.bz2
# sample config file
Source1: gaminrc

BuildRequires: glib2-devel
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool

# This fix addresses an issue with ARM, where the configuration triplet
# happens to be armv5tel-redhat-linux-gnueabi instead of armv5tel-redhat-linux-gnu.
# The patch declares HAVE_LINUX in case of linux-gnueabi as well.
# Patch by Kedar Sovani <kedars@marvell.com>
Patch1: gamin-0.1.10-gnueabi.patch

# Don't try to build with -DG_DISABLE_DEPRECATED - glib has moved on
Patch2: gamin-manape.patch

# upstream fixes
Patch4: 0001-Poll-files-on-nfs4.patch
Patch5: 0002-Fix-compilation-of-recent-glib-removing-G_CONST_RETU.patch
# gam_server deadlocks, leading to all KDE applications hanging at start
# https://bugzilla.redhat.com/show_bug.cgi?id=786170
# https://bugzilla.gnome.org/show_bug.cgi?id=667120
Patch7: 0004-fix-possible-server-deadlock-in-ih_sub_cancel.patch

%description
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%package devel
Summary: Libraries, includes, etc. to embed the Gamin library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%prep
%setup -q
%patch1 -p1 -b .gnueabi
%patch2 -p1 -b .manape
%patch4 -p1 -b .nfs4
%patch5 -p1 -b .const
%patch7 -p1 -b .double-lock

# recode docs into UTF-8
for i in ChangeLog NEWS ; do 
   iconv -f iso-8859-1 -t utf-8 < $i > XXX
   touch -r $i XXX
   mv XXX $i
done

# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
# replace "/usr/bin/env python" with "/usr/bin/python2"
for i in `find -name '*.py'`; do
   sed -i.bak "s|^#!/usr/bin/env python|#!%{__python2}|g" $i
   touch -r ${i}.bak $i
   rm ${i}.bak
done

%build
autoreconf -vif
%configure \
  --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

install -D -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gamin/gaminrc
touch %{buildroot}%{_sysconfdir}/gamin/mandatory_gaminrc

rm -fv %{buildroot}%{_libdir}/lib*.la
# gamin server links this, it gets installed even in --disable-static mode,
# but continue to omit from packaging as has been done for a long time -- rex
rm -fv %{buildroot}%{_libdir}/libgamin_shared.a

%check
## 'make check' isn't working well at all in mock yet, needs work.
#make check ||:

#%%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/*.html
%doc doc/*.gif
%doc doc/*.txt
%dir %{_sysconfdir}/gamin/
%config(noreplace) %{_sysconfdir}/gamin/gaminrc
%config(noreplace) %{_sysconfdir}/gamin/mandatory_gaminrc
%{_libdir}/libfam.so.0*
%{_libdir}/libgamin-1.so.0*
%{_libexecdir}/gam_server

%files devel
%{_libdir}/libfam.so
%{_libdir}/libgamin-1.so
%{_includedir}/fam.h
%{_libdir}/pkgconfig/gamin.pc

%changelog
* Thu Jul 09 2020  HAL <notes2@gmx.de> - 0.1.10-35
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-34
- Subpackage python2-gamin has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.10-32
- Fix FTBFS, minor spec cleanups

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.10-29
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.10-28
- Python 2 binary package renamed to python2-gamin
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.1.10-24
- ship sample /etc/gamin/gaminrc, /etc/gamin/mandatory_gaminrc
- s|/usr/bin/python|/usr/bin/python2|

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-23
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.1.10-22
- %%check: disable 'make check', needs work
- %%build: --disable-static, drop rpath hacks
- %%install: cleaner .la/.a omission

* Mon Feb 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.1.10-21
- pull in slightly different upstream fix for deadlocks (gnome#667230)
- cosmetics: use %%license, tighten subpkg deps
- -python: cleanup, Provides: python(2)-gamin
- %%check: make check (non-fatal for now)
- %%files: track sonames explicitly

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.10-19
- Minor cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb  1 2013 Matthias Clasen <mclasen@redhat.com> - 0.1.10-14
- Make it work on nfs4
- Fix the build
- Minor spec file cleanups

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Tomas Bzatek <tbzatek@redhat.com> - 0.1.10-12
- Prevent deadlock when cancelling a watch (#786170)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.1.10-10
- Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Mar  3 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.1.10-7
- Further cleanup for package review (#225776)
- Fix source URL

* Mon Dec 21 2009 Tomas Bzatek <tbzatek@redhat.com> - 0.1.10-6
- Cleanup for package review (#225776)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan  5 2009 Tomas Bzatek <tbzatek@redhat.com> - 0.1.10-3
- Fix build on gnueabi (patch by Kedar Sovani)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.10-2
- Rebuild for Python 2.6

* Mon Nov 24 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.1.10-1
- Update to 0.1.10
- Drop upstreamed patches

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.9-6
- fix license tag

* Wed Feb 14 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.1.9-5
- workaround for missing struct ucred in glibc headers (fixed x86_64 compilation)

* Fri Sep 14 2007 Matthias Clasen <mclasen@redhat.com> - 0.1.9-4
- Fix a memory leak

* Fri Sep 14 2007 Ray Strode <rstrode@redhat.com> - 0.1.9-3
- don't poll for non-existant watched files (bug 240385)

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.1.9-2
- Rebuild for selinux ppc32 issue.

* Fri Jul 27 2007 Daniel Veillard <veillard@redhat.com> - 0.1.9-1.fc8
- made new upstream release, that includes all the existing patches

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> - 0.1.8-6
- Don't ship static libraries

* Wed Apr 11 2007 Alexander Larsson <alexl@redhat.com> - 0.1.8-5
- Add patch that handles inotify failing fallback (#233316)

* Wed Mar  7 2007 Alexander Larsson <alexl@redhat.com> - 0.1.8-4
- Add patch to fix #204906

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.1.8-3
- rebuild for python 2.5

* Mon Nov 20 2006 Alexander Larsson <alexl@redhat.com> - 0.1.8-2.fc7
- Fix polling backend, making NFS work again
- Resolves: #212551

* Tue Oct 31 2006 Daniel Veillard <veillard@redhat.com> - 0.1.8-1
- made new upstream release, that should include all the existing patches

* Fri Sep  8 2006 Alexander Larsson <alexl@redhat.com> - 0.1.7-7
- Fix problems in new inotify backend (#205731)

* Tue Sep  5 2006 Alexander Larsson <alexl@redhat.com> - 0.1.7-6
- Remove last regular timers from gamin

* Tue Sep  5 2006 Alexander Larsson <alexl@redhat.com> - 0.1.7-5
- Use sigaction to reset old signal handler (from cvs)
- New inotify backend from cvs (based on gnome-vfs code)
- Only create timer on demand
- This should fix #204906

* Mon Aug 28 2006 Alexander Larsson <alexl@redhat.com> - 0.1.7-4
- Flush in-buffer on connection reset (#196444)
- Patch from Ariel T. Glenn

* Tue Aug 22 2006 Alexander Larsson <alexl@redhat.com> - 0.1.7-3
- Use /dev/null as stdin/out/err when spawning gam_server
- This could help if there is stdout output somewhere.

* Wed Aug 16 2006 Alexander Larsson <alexl@redhat.com> - 0.1.7-2
- Add patch that avoids closing the fd after FAMOpen, fixes some 100% cpu bugs

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.7-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.1.7-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.1.7-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Oct 27 2005 Daniel Veillard <veillard@redhat.com> 0.1.7-1
- hopefully fixes gam_server crashes
- some portability fixes
- removed a minor leak
* Thu Sep  8 2005 Daniel Veillard <veillard@redhat.com> 0.1.6-1
- revamp of the inotify back-end
- memory leak fix
- various fixes and cleanups
* Tue Aug  9 2005 Daniel Veillard <veillard@redhat.com> 0.1.5-1
- Improvement of configuration, system wide configuration files and
  per filesystem type default
- Rewrite of the inotify back-end, reduce resources usage, tuning in
  case of busy resources
- Documentation updates
- Changes to compile inotify back-end on various architectures
- Debugging output improvements
* Tue Aug  2 2005 Daniel Veillard <veillard@redhat.com> 0.1.3-1
- Fix to compile on older gcc versions
- Inotify back-end changes and optimizations
- Debug ouput cleanup, pid and process name reports
- Dropped kernel monitor bugfix
- Removed the old glist copy used for debugging
- Maintain mounted filesystems knowledge, and per fstype preferences
* Wed Jul 13 2005 Daniel Veillard <veillard@redhat.com> 0.1.2-1
- inotify back end patches, ready for the new inotify support in kernel
- lot of server code cleanup patches
- fixed an authentication problem
* Fri Jun 10 2005 Daniel Veillard <veillard@redhat.com> 0.1.1-1
- gamin_data_conn_event fix
- crash from bug gnome #303932
- Inotify and mounted media #171201
- mounted media did not show up on Desktop #159748
- write may not be atomic
- Monitoring a directory when it is a file
- Portability to Hurd/Mach and various code cleanups
- Added support for ~ as user home alias in .gaminrc
* Thu May 12 2005 Daniel Veillard <veillard@redhat.com> 0.1.0-1
- Close inherited file descriptors on exec of gam_server
- Cancelling a monitor send back a FAMAcknowledge
- Fixed for big files > 2GB
- Bug when monitoring a non existing directory
- Make client side thread safe
- Unreadable directory fixes
- Better flow control handling
- Updated to latest inotify version: 0.23-6
* Tue Mar 15 2005 Daniel Veillard <veillard@redhat.com> 0.0.26-1
- Fix an include problem showing up with gcc4</li>
- Fix the crash on failed tree assert bug #150471 based on patch from Dean Brettle
- removed an incompatibility with SGI FAM #149822
* Tue Mar  1 2005 Daniel Veillard <veillard@redhat.com> 0.0.25-1
- Fix a configure problem reported by Martin Schlemmer
- Fix the /media/* and /mnt/* mount blocking problems from 0.0.24 e.g. #142637
- Fix the monitoring of directory using poll and not kernel
* Fri Feb 18 2005 Daniel Veillard <veillard@redhat.com> 0.0.24-1
- more documentation
- lot of serious bug fixes including Gnome Desktop refresh bug
- extending the framework for more debug (configure --enable-debug-api)
- extending the python bindings for watching the same resource multiple times
  and adding debug framework support
- growing the regression tests a lot based on python bindings
- inotify-0.19 patch from John McCutchan
- renamed python private module to _gamin to follow Python PEP 8

* Tue Feb  8 2005 Daniel Veillard <veillard@redhat.com> 0.0.23-1
- memory corruption fix from Mark on the client side
- extending the protocol and API to allow skipping Exists and EndExists
  events to avoid deadlock on reconnect or when they are not used.

* Mon Jan 31 2005 Daniel Veillard <veillard@redhat.com> 0.0.22-1
- bit of python bindings improvements, added test
- fixed 3 bugs

* Wed Jan 26 2005 Daniel Veillard <veillard@redhat.com> 0.0.21-1
- Added Python support
- Updated for inotify-0.18 

* Thu Jan  6 2005 Daniel Veillard <veillard@redhat.com> 0.0.20-1
- Frederic Crozat seems to have found the GList corruption which may fix
  #132354 and related problems
- Frederic Crozat also fixed poll only mode

* Fri Dec  3 2004 Daniel Veillard <veillard@redhat.com> 0.0.19-1
- still chasing the loop bug, made another pass at checking GList,
  added own copy with memory poisonning of GList implementation.
- fixed a compile issue when compiling without debug

* Fri Nov 26 2004 Daniel Veillard <veillard@redhat.com> 0.0.18-1
- still chasing the loop bug, checked and cleaned up all GList use
- patch from markmc to minimize load on busy apps

* Wed Oct 20 2004 Daniel Veillard <veillard@redhat.com> 0.0.16-1
- chasing #132354, lot of debugging, checking and testing and a bit
  of refactoring

* Sat Oct 16 2004 Daniel Veillard <veillard@redhat.com> 0.0.15-1
- workaround to detect loops and avoid the nasty effects, see RedHat bug #132354

* Sun Oct  3 2004 Daniel Veillard <veillard@redhat.com> 0.0.14-1
- Found and fixed the annoying bug where update were not received
  should fix bugs ##132429, #133665 and #134413
- new mechanism to debug on-the-fly by sending SIGUSR2 to client or server
- Added documentation about internals

* Fri Oct  1 2004 Daniel Veillard <veillard@redhat.com> 0.0.13-1
- applied portability fixes
- hardened the code while chasing a segfault

* Thu Sep 30 2004 Daniel Veillard <veillard@redhat.com> 0.0.12-1
- potential fix for a hard to reproduce looping problem.

* Mon Sep 27 2004 Daniel Veillard <veillard@redhat.com> 0.0.11-1
- update to the latest version of inotify
- inotify support compiled in by default
- fix ABI FAM compatibility problems #133162 

* Tue Sep 21 2004 Daniel Veillard <veillard@redhat.com> 0.0.10-1
- more documentation
- Added support for a configuration file $HOME/.gaminrc
- fixes FAM compatibility issues with FAMErrno and FamErrlist #132944

* Wed Sep  1 2004 Daniel Veillard <veillard@redhat.com> 0.0.9-1
- fix crash with konqueror #130967
- exclude kernel (dnotify) monitoring for /mnt//* /media//*

* Thu Aug 26 2004 Daniel Veillard <veillard@redhat.com> 0.0.8-1
- Fixes crashes of the gam_server
- try to correct the kernel/poll switching mode

* Tue Aug 24 2004 Daniel Veillard <veillard@redhat.com> 0.0.7-1
- add support for both polling and dnotify simultaneously
- fixes monitoring of initially missing files
- load control on very busy resources #124361, desactivating
  dnotify and falling back to polling for CPU drain

* Thu Aug 19 2004 Daniel Veillard <veillard@redhat.com> 0.0.6-1
- fixes simple file monitoring should close RH #129974
- relocate gam_server in $(libexec)

* Thu Aug  5 2004 Daniel Veillard <veillard@redhat.com> 0.0.5-1
- Fix a crash when the client binary forks the gam_server and an
  atexit handler is run.

* Wed Aug  4 2004 Daniel Veillard <veillard@redhat.com> 0.0.4-1
- should fix KDE build problems
