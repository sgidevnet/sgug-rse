Name: jhead
Version: 3.04
Release: 1%{?dist}
Summary: Tool for displaying EXIF data embedded in JPEG images
License: Public Domain
URL: http://www.sentex.net/~mwandel/jhead/
Source0: http://www.sentex.net/~mwandel/jhead/jhead-%{version}.tar.gz
%if 0%{?rhel} == 6
Requires: libjpeg-turbo
%else
Requires: libjpeg-turbo-utils
%endif
Patch0: 35_compiler_warning_truncate
BuildRequires: gcc

%description
Jhead displays and manipulates the non-image portions of EXIF formatted
JPEG images, such as the images produced by most digital cameras.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_bindir}
cp -p jhead ${RPM_BUILD_ROOT}/%{_bindir}
%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cp -p jhead.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/

%files
%doc readme.txt usage.html changes.txt
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%changelog
* Fri Nov 22 2019 Adrian Reber <adrian@lisas.de> - 3.04-1
- updated to 3.04 (CVE-2019-19035)

* Mon Aug 05 2019 Adrian Reber <adrian@lisas.de> - 3.03-4
- added patches to fix CVE-2019-1010301 and CVE-2019-1010302 from Debian

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Adrian Reber <adrian@lisas.de> - 3.03-1
- updated to 3.03 (#1667491)

* Sat Dec 29 2018 Adrian Reber <adrian@lisas.de> - 3.02-1
- updated to 3.02 (#1661744)
- dropped upstreamed patches

* Wed Sep 19 2018 Adrian Reber <adrian@lisas.de> - 3.00-12
- Added more buffer overflow Debian patches (should also fix CVE-2018-16554, CVE-2016-3822)

* Sat Jul 14 2018 Adrian Reber <adrian@lisas.de> - 3.00-11
- added BR gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Adrian Reber <adrian@lisas.de> - 3.00-9
- Correctly handle jpegtran dependency on el6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Adrian Reber <adrian@lisas.de> - 3.00-7
- Added Debian patch to fix CVE-2018-6612 (#1542049)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Adrian Reber <adrian@lisas.de> - 3.00-1
- updated to 3.00

* Sat Aug 30 2014 Adrian Reber <adrian@lisas.de> - 2.97-1
- updated to 2.97

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.96-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Adrian Reber <adrian@lisas.de> - 2.96-1
- updated to 2.96

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Oliver Falk <oliver@linux-kernel.at> - 2.95-1
- Update

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 15 2011 Adrian Reber <adrian@lisas.de> - 2.90-4
- added "Requires: libjpeg-turbo-utils" to fix
  "jhead should depend on libjpeg-turbo-utils" (#673808)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Adrian Reber <adrian@lisas.de> - 2.90-2
- added patch to fix "[abrt] jhead-2.90-1.fc14: ClearOrientation" (#655727)

* Wed Aug 04 2010 Adrian Reber <adrian@lisas.de> - 2.90-1
- updated to 2.90

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Adrian Reber <adrian@lisas.de> - 2.87-1
- updated to 2.87

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Adrian Reber <adrian@lisas.de> - 2.86-1
- updated to 2.86
- fixes "CVE-2008-4640 jhead: arbitrary file deletion" (#468056)
- fixes "CVE-2008-4641 jhead: command exection caused by
  incorrect handling of the shell escapes" (#468057)
- fixes "build ignores optflags" (#485697)

* Thu Oct 16 2008 Adrian Reber <adrian@lisas.de> - 2.84-1
- updated to 2.84
- fixes "CVE-2008-4575 jhead buffer overflow" (#467262)
- removed upstreamed makefile patch

* Wed Sep 24 2008 Adrian Reber <adrian@lisas.de> - 2.82-2
- rebased makefile patch

* Sat Apr 05 2008 Adrian Reber <adrian@lisas.de> - 2.82-1
- updated to 2.82

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.7-3
- Autorebuild for GCC 4.3

* Sat Oct 13 2007 Adrian Reber <adrian@lisas.de> - 2.7-2
- rebuilt for BuildID

* Sun Mar 18 2007 Adrian Reber <adrian@lisas.de> - 2.7-1
- updated to 2.7

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.6-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Adrian Reber <adrian@lisas.de> - 2.6-2
- rebuilt

* Mon May 01 2006 Adrian Reber <adrian@lisas.de> - 2.6-1
- updated to 2.6
- removed gcc4 patch

* Sat Feb 18 2006 Adrian Reber <adrian@lisas.de> - 2.5-1
- updated to 2.5
- removed compiler warnings patch and added gcc4 patch

* Fri Jul 08 2005 Adrian Reber <adrian@lisas.de> - 2.4-3
- undo parts of the compiler warning patch because it
  disabled the correct optflags

* Fri Jul 08 2005 Adrian Reber <adrian@lisas.de> - 2.4-2
- added patch to make compiler happy

* Fri Jul 08 2005 Adrian Reber <adrian@lisas.de> - 2.4-1
- updated to 2.4

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Feb 12 2005 Adrian Reber <adrian@lisas.de> 2.3-1
- updated to 2.3

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 2.2-2
- Bump release to provide Extras upgrade path.

* Wed Oct 13 2004 Adrian Reber <adrian@lisas.de> 0:2.2-0.fdr.1
- updated to 2.2
- use full URL for source
- now honouring RPM_OPT_FLAGS

* Sat Jul 26 2003 Chris Ricker <kaboom@gatech.edu> 0:2.0-0.fdr.2
- Optimize compile (#502)
- Include changes.txt (#502)

* Tue Jul 22 2003 Chris Ricker <kaboom@gatech.edu> 0:2.0-0.fdr.1
- Initial package
