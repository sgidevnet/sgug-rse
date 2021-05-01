Summary: more, less, most
Name: most
Version: 5.1.0
Release: 2%{?dist}
License: GPLv2+
URL: http://www.jedsoft.org/releases/most/
Source: http://www.jedsoft.org/releases/most/most-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: slang-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1230278
Patch0: bz1230278.patch
Patch1: most-no-strip.patch

%description
most is a paging program that displays, one window-full at a time, the
contents of a file on a terminal. It pauses after each window-full and
prints on the window status line the screen the file name, current line
number, and the percentage of the file so far displayed.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure
# Parallel builds sometimes miss to create this directory before starting
# the compiler. In theory the Makefile would create this before running gcc.
mkdir -p src/objs
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYRIGHT
%doc README changes.txt most.txt most-fun.txt lesskeys.rc most.rc
%{_bindir}/most
%{_mandir}/man1/most.1*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Adrian Reber <adrian@lisas.de> - 5.1.0-1
- Updated to 5.1.0 (#1678098)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-20.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-19.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Adrian Reber <adrian@lisas.de> - 5.0.0-18.a.1
- Fix for parallel builds by creating the objs directory

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-17.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-16.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-15.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-14.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-13.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 03 2015 Adrian Reber <adrian@lisas.de> - 5.0.0-12.a.1
- Clean up spec file
- added patch to fix bz1230278
  "color overstrike and color underline in .mostrc have no effect"

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-11.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-10.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-9.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-8.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-7.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-6.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-5.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-4.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-3.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-2.a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0.0-1.a.1
- Autorebuild for GCC 4.3

* Fri Oct 12 2007 Adrian Reber <adrian@lisas.de> - 5.0.0-0.a.1
- updated to 5.0.0a
- removed BR gawk

* Sun Aug 26 2007 Adrian Reber <adrian@lisas.de> - 4.10.2-6
- rebuilt
- updated License
- added BR gawk

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 4.10.2-5
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Adrian Reber <adrian@lisas.de> - 4.10.2-4
- rebuilt

* Sun Mar 12 2006 Adrian Reber <adrian@lisas.de> - 4.10.2-3
- rebuilt

* Tue Nov 29 2005 Adrian Reber <adrian@lisas.de> - 4.10.2-2
- rebuilt for new slang

* Thu Jul 07 2005 Adrian Reber <adrian@lisas.de> - 4.10.2-1
- updated to 4.10.2 (fixes search aborting bug)

* Fri Jul 01 2005 Adrian Reber <adrian@lisas.de> - 4.10.1-1
- updated to 4.10.1

* Wed Mar 30 2005 Adrian Reber <adrian@lisas.de> - 4.9.5-4
- fix build on ppc/ppc64

* Sat Feb 12 2005 Thorsten Leemhuis <fedora at leemhuis dot info> - 4.9.5-3
- sed -i 's|/usr/lib|%%{_libdir}|g' configure fixes x86_64 build;

* Mon Jul 19 2004 Adrian Reber <adrian@lisas.de> - 0:4.9.5-0.fdr.2
- removed chrpath dependency

* Fri Jul 09 2004 Adrian Reber <adrian@lisas.de> - 0:4.9.5-0.fdr.1
- fedorafication

* Mon May 10 2004 Michael Scherer <misc@mandrake.org> 4.9.4-1mdk
- New release 4.9.4
- remove rpath

* Fri Jan  2 2004 Han Boetes <han@linux-mandrake.com> 4.9.2-3mdk
- rebuild

* Fri Dec 27 2002 Han Boetes <han@linux-mandrake.com> 4.9.2-2mdk
- rebuild because of new rpm macros and new glibc

* Wed Aug 21 2002 Han Boetes <han@linux-mandrake.com> 4.9.2-1mdk
- First spec for mandrake.
