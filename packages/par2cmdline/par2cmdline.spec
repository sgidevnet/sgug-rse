Name: par2cmdline
Version: 0.8.0
Release: 3%{?dist}
Summary: PAR 2.0 compatible file verification and repair tool

License: GPLv2+
URL: https://github.com/Parchive/par2cmdline/
Source0: https://github.com/Parchive/par2cmdline/releases/download/v%{version}/par2cmdline-%{version}.tar.bz2

BuildRequires: gcc-c++


%description
par2cmdline is a program for creating and using PAR2 files to detect damage
in data files and repair them if necessary. PAR2 files are usually
published in binary newsgroups on Usenet; they apply the data-recovery
capability concepts of RAID-like systems to the posting and recovery of
multi-part archives.


%prep
%autosetup
# Remove executable permission from text files
chmod -x ChangeLog configure.ac INSTALL Makefile.am NEWS stamp-h.in


%build
%configure
%make_build


%install
%make_install


%check
make check-TESTS


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify
%{_mandir}/man1/par2.1*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Tadej Janež <tadej.j@nez.si> - 0.8.0-1
- Update to 0.8.0 release
- Add gcc-c++ to BuildRequires to account for
  https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Use make command instead of %%{__make} as mandated in
  https://fedoraproject.org/wiki/Packaging:Guidelines#Macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Tadej Janež <tadej.j@nez.si> - 0.7.4-1
- Update to 0.7.4 release.
- Drop OpenMP support patch which has been merged upstream.
- Drop patch that uses /dev/urandom in tests since it has been merged upstream.
- Modernize and clean-up SPEC file.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.6.14-1
- Switch to the more actively maintained fork https://github.com/Parchive/par2cmdline
- Backport the OpenMP support pieces from https://github.com/jkansanen/par2cmdline-mt
- This version is more reliable than the previous par2-tbb fork, but has slightly worse performance
- Resolves RHBZ #1239757 #1221165 #1198492 #1197560 #1187833 #1105926

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20100203-16
- Enable NX in order to prevent having an executable stack
  Patch contributed by Dhiru Kholia (RHBZ #973499)

* Mon May 27 2013 Petr Machata <pmachata@redhat.com> - 0.4.tbb.20100203-15
- Bump to preserve upgrade path

* Fri May 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20100203-14
- Rewritten the patches so that autoreconf isn't needed any more
  Fixes a regression in the testsuite caused by changed behavior in modern automake
- Re-enabled the testsuite for all targets
- Don't use the %%makeinstall macro any more

* Fri May 24 2013 Petr Machata <pmachata@redhat.com> - 0.4.tbb.20100203-13
- Rebuild for TBB memory barrier bug

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20100203-10
- Removed the /usr/bin/par symlink as it conflicts with par (paragraph reformatter)

* Mon May 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.tbb.20100203-9
- Clean up spec to fix FTBFS on ARM

* Wed Apr 11 2012 Karsten Hopp <karsten@redhat.com> 0.4.tbb.20100203-8
- sed script to change from tbb to rt on non-x86 archs needs to fix Makefile.am
  as autoreconf runs afterwards

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-7
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20100203-6
- Fix FTBFS (RHBZ #564834)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.tbb.20100203-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 21 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20100203-3
- Added support for EL6

* Sat Jun 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20100203-2
- Fix DSO linking failure (BZ #564834)

* Fri Feb  5 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20100203-1
- Update to par2_tbb 20100203 (Fixes BZ #545859 and #549007)

* Sun Dec 27 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20090203-4
- Fixed PPC build failure (BZ #550818)

* Sat Dec 12 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20090203-3
- Rebuild for new tbb

* Sun Nov 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20090203-2
- FTBFS fix, BZ #539005

* Mon Aug  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.tbb.20090203-1
- Updated to the par2_tbb fork of par2cmdline (revision 20090203)
  This fork is maintained at http://www.chuchusoft.com/par2_tbb/
- This adds support for PAR2 verifications and repairs using multiple CPU cores
- As Intel Threading Building Blocks (TBB) only works on x86 hardware, fall
  back to the old behaviour on other platforms (like PPC/PPC64)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4-14
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 0.4-13
- Rebuild.

* Fri Aug 24 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 0.4-12
- New License: tag.
- rpmlint cleaning:
    - clean the build root at the beginning of %%install
    - use -q in %%setup

* Mon Aug 28 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 0.4-11
- Rebuild for FC-6.
- Change my email address in the %%changelog.

* Fri May 12 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 0.4-10
- New %%changelog. Quote percent signs.

* Wed May 10 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 0.4-9
- Remove PORTING and ROADMAP from doc files.
- Patch2: Remove explicit linking with -lstdc++ in Makefile.am, what required to call aclocal-1.9 and automake-1.9

* Tue May  9 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 0.4-8
- Added a new patch, to kill warnings, and try to fix ppc compilation error.

* Fri Apr 28 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 0.4-7
- Change the description. Thanks to Jason Tibbitts (tibbs@math.uh.edu) for his help.
- Add %%check section

* Thu Apr 27 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 0.4-6
- chmod 644 several files, in %%build
- fix the Source: tag.
- new %%description
- changed the buildroot to the one recommanded for Fedora Extras

* Wed Apr 12 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 0.4-5
- Added the dist tag.
- Recode several file with sed, to remove DOS end-of-lines.
- Changed the URL: tag.
- Cleanup after a rpmlint pass.

* Tue Apr 11 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> -  0.4-3
- updated for Fedora Core 4
- obsolete parchive 1.1.4
- provides parchive = 1.1.4.0.par2.%%{version}

* Tue May 11 2004 - Thibaut Cousin <linux@thibaut-cousin.net>
- updated to version 0.4 for SUSE 9.1

* Tue Oct 21 2003 - Thibaut Cousin <linux@thibaut-cousin.net>
- first release of this package for SuSE 9.0
