# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary:       An X Window System utility for monitoring system resources
Name:          xosview
Version:       1.21
Release:       2%{?dist}
# The netbsd/swapinternal.{cc,h} source files are BSD only (with 
# advertising), but neither file is used in the linux version of 
# xosview.  Instead, the source files used are linux/swapmeter.{cc,h}, 
# both of which fall under the GPL. All other files are either GPL 
# based, or can fall under either the BSD or GPL copyright.
License:       GPL+
URL:           http://www.pogo.org.uk/~mark/xosview/
Source0:       http://www.pogo.org.uk/~mark/xosview/releases/xosview-%{version}.tar.gz
Patch0:        xosview-1.11-app-def.patch
Patch1:        xosview-1.20-arm.patch
Patch50:       xosview.sgifixes.patch
#BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libXpm-devel
#BuildRequires: libX11-devel 
#Requires:      xorg-x11-fonts-misc
%description
The xosview utility displays a set of bar graphs which show the
current system state, including memory usage, CPU usage, system load,
etc. Xosview runs under the X Window System.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch50 -p1

%build
make PLATFORM=irix65 %{?_smp_mflags} OPTFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
make PLATFORM=irix65 install PREFIX=%{buildroot}%{_prefix} INSTALL="install -p"
install -p -m 0644 -D Xdefaults %{buildroot}%{_datadir}/X11/app-defaults/XOsview
#desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
#mv $RPM_BUILD_ROOT%{_datadir}/man $RPM_BUILD_ROOT%{_mandir}/

%files
%license COPYING COPYING.GPL
%doc CHANGES README README.linux TODO Xdefaults
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/32x32/apps/xosview.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/X11/app-defaults/XOsview

%changelog
* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 1.21-2
- Manpath correction

* Mon Aug 12 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.21-1
- 1.21

* Mon Aug 12 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20-7
- Fix FTBFS

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.20-4
- Add C++ compiler

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.20-1
- 1.20

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.19-1
- Rebuilt for new upstream release 1.19, fixes rhbz #1401149
- Do not use upstreamed patches (already in latest release)

* Sat Feb 06 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.17-3
- Add patch to fix FTBFS with gcc 6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 04 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.17-1
- 1.17

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.16-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.16-3
- handle AArch64 as well

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 05 2014 Terje Rosten <terje.rosten@ntnu.no> - 1.16-1
- 1.16

* Tue Oct 22 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.15-1
- 1.15

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.14-1
- 1.14

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.12-1
- 1.12
- Add patch to install and read X resources

* Mon Dec 03 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.11-1
- 1.11

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 09 2012 Karsten Hopp <karsten@redhat.com> 1.9.2-3
- replace ancient config.* files with newer ones so that PPC is supported

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for c++ ABI breakage

* Sun Feb 19 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.9.2-1
- 1.9.2
- New upstream location

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-19.20080301cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-18.20080301cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-17.20080301cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.8.3-16.20080301cvs
- Add patch to build with gcc 4.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-15.20080301cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.8.3-14.20080301cvs
- Add xorg-x11-fonts-misc to req, fixing #479456.

* Mon Sep  8 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.8.3-13.20080301cvs
- Fix license and desktop file

* Mon Sep  8 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.8.3-12.20080301cvs
- Drop fedora as vendor
- Use date in cvs checkout

* Tue May 20 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 1.8.3-11.20080520cvs
- Pulling icon directly from website

* Tue May 20 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 1.8.3-10.20080520cvs
- Added Source1 URL
- Fixed ppc64 config error
- Added -q to %%setup again (deleted by accident in release 9)
- Fixed macros conventions
- Only including README and README.linux files

* Mon May 19 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 1.8.3-9.20080519cvs
- Fixed naming guidelines (again)
- Removed CXXFLAGS (redundant)

* Fri Apr 25 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 1.8.3.20080425cvs-8
- Clarified BSD vs. GPL License Issue
- Pulling source dirctly from CVS
- Removed CVS patch generation file since current CVS snapshot is used
- Removed COPYING.BSD file (see License Section above for explanation)
- Fixed Post-Release Naming Guidelines
- Fixed Categories section in Desktop file

* Thu Apr 17 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.8.3-7
- Add cvs patch generation info

* Mon Apr  7 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.8.3-6
- Remove extra build flags

* Thu Apr  3 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.8.3-5
- Patches from cvs, remove private patches
- Add app-defaults patch
- Fix license, summary, src url, buildroot and desktop file
- Random clean up

* Wed Feb 20 2008 Chelban Vasile <vchelban@fedoramd.org> 1.8.3-4.prof_k
- BuildRequires: libXpm-devel, libX11-devel
- Removed i386 build restriction

* Sun Dec 16 2007 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> xosview-1.8.3-3.fc8.prof_k
- Fixed man location

* Wed Dec 12 2007 Gregory Kriehn <gkriehn@csufresno.edu> xosview-1.8.3-2.fc8.prof_k
- Cleaned up spec file
- Now includes doc files

* Mon Dec 3 2007 Gregory Kriehn <gkriehn@csufresno.edu> xosview-1.8.3-1.fc8.prof_k
- Recompiled for Fedora 8

* Sun Mar 26 2006 Ron Yorston <rmy@tigress.co.uk> 1.8.3-1.tig1.fc5
- fixes to compile with modular X on FC5

* Sun Jan  2 2005 Ron Yorston <rmy@tigress.co.uk> 1.8.2-1.tig1
- backport from FC3 to RHEL3
- change default reosurce for CPU to 'cpuGraph: False'

* Mon Jul 19 2004 Than Ngo <than@redhat.com> 1.8.2-1
- update to 1.8.2
- remove all patches, which are included in new upstream
- bug #126432, #124156, #124569, #124896

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 19 2004 Than Ngo <than@redhat.com> 1.8.0-21
- fix PAGE/DISK lines with kernel > 2.5, they work again.

* Wed May 19 2004 Than Ngo <than@redhat.com> 1.8.0-20
- fixed build problem with gcc34

* Wed Mar 10 2004 Than Ngo <than@redhat.com> 1.8.0-19
- added nfs traffic

* Tue Feb 24 2004 Than Ngo <than@redhat.com> 1.8.0-18 
- get rid of rpath

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 20 2004 Than Ngo <than@redhat.com> 1.8.0-16
- add patch to get xosview working on 2.6 kernel

* Tue Jul 08 2003 Than Ngo <than@redhat.com> 1.8.0-15
- cleanup

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Than Ngo <than@redhat.com> 1.8.0-13
- fix build with gcc 3.3

* Wed Apr 30 2003 Elliot Lee <sopwith@redhat.com> 1.8.0-12
- Fix powerpc64 & ia64 according to the pattern of other non-i386 archs

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.8.0-10
- rebuild on all arches

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com>
- rebuilt with gcc-3.2 (we hope)

* Wed Jul 24 2002 Than Ngo <than@redhat.com> 1.8.0-7
- desktop file issue (bug #69551)

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 1.8.0-6
- build using gcc-3.2-0.1

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.8.0-5
- automated rebuild

* Thu Jun 20 2002 Than Ngo <than@redhat.com> 1.8.0-4
- Don't forcibly strip binaries

* Sun Jun 2 2002 Than Ngo <than@redhat.com> 1.8.0-3
- fix a bug in cpumeter (bug #64798)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr 24 2002 Karsten Hopp <karsten@redhat.de> 1.8.0-1
- update to current version
- redo .proc patch
- change URLs

* Fri Feb 22 2002 Than Ngo <than@redhat.com> 1.7.3-10
- rebuild in new environment.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec 18 2001 Than Ngo <than@redhat.com> 1.7.3-8
- xosview +net goes into hard loop (bug #57150)
- add patch for building against g++ 3
- use RPM_OPT_FLAG

* Wed Nov 14 2001 Than Ngo <than@redhat.com> 1.7.3-7
- added missing Icon in desktop file
- fixed Url

* Wed Sep 12 2001 Tim Powers <timp@redhat.com>
- rebuild with new gcc and binutils

* Tue Apr 10 2001 Phil Knirsch <pknirsch@redhat.de>
- Fix for s390 patch to actually work

* Tue Mar 20 2001 Preston Brown <pbrown@redhat.com>
- fix up .desktop entry

* Sun Feb 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix typo

* Sun Feb 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- adjusted s390 patches

* Wed Jan 31 2001 Preston Brown <pbrown@redhat.com>
- upgrade to 1.7.3, fixes (#11380)

* Mon Jan 15 2001 Than Ngo <than@redhat.com>
- ported to ibm s/390

* Tue Jul 25 2000 Jeff Johnson <jbj@redhat.com>
- migrate wmconfig to applnk.

* Fri Jul 14 2000 Jeff Johnson <jbj@redhat.com>
- rebuild the auto-rebuild.
- exclude alpha and i164 for now.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul  2 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Fri Jun  2 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for 7.0

* Mon Feb 14 2000 Matt Wilson <msw@redhat.com>
- rebuild on i386

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- updated to 1.7.1.

* Wed Mar  3 1999 Matt Wilson <msw@redhat.com>
- updated to 1.7.0

* Fri Feb  5 1999 Bill Nottingham <notting@redhat.com>
- build against new libstdc++, build on arm

* Tue Dec 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.6.2.a.

* Tue Jun 16 1998 Jeff Johnson <jbj@redhat.com>
- add sparc/alpha functionality.
- add %%clean

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- how the hell did this get setuid root?

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.1 (so that it compiles with egcs)
- buildroot

* Tue Nov  4 1997 Erik Troan <ewt@redhat.com>
- commented out line causing core dumps when exiting

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
