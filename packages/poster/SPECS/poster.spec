Summary:        Scales PostScript images to span multiple pages
Name:           poster
Version:        20060221
Release:        25%{?dist}
License:        GPLv2
Source:         ftp://ftp.kde.org/pub/kde/printing/%{name}.tar.bz2
URL:            http://printing.kde.org/downloads/

# Fixes a gs crash, see https://bugzilla.redhat.com/show_bug.cgi?id=436969
Patch0:         poster.fixes_gs_crash.patch

BuildRequires:  gcc
%description
Poster scales PostScript images to a larger size, and prints them on
larger media and/or tiles them to print on multiple sheets.


%prep
%setup -q
%patch0

%build
# The included Makefile is badly written
%{__cc} %{optflags} -lm -o poster poster.c %{?__global_ldflags}


%install
%{__install} -D -m755 -p poster   %{buildroot}%{_bindir}/poster
%{__install} -D -m644 -p poster.1 %{buildroot}%{_mandir}/man1/poster.1


%files
%{_mandir}/man1/poster.1*
%{_bindir}/poster
%doc COPYING ChangeLog README manual.ps


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20060221-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 30 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> - 20060221-17
- Added a patch reverting some "print_content_of_complete_page" 
  introduced in 20060221. It crashes gs on big files, fixes #436969

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 20060221-13
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060221-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20060221-5
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 20060221-4
- Multiple minor changes to clean up the SPEC to conform guidelines
- Fix the License tag

* Thu Sep 07 2006 W. Michael Petullo <mike[@]flyn.org> 20060221-3
- Rebuild for FC6.

* Sat Jul 08 2006 W. Michael Petullo <mike[@]flyn.org> 20060221-2
- Fixed installation of man page.

* Tue Jul 04 2006 W. Michael Petullo <mike[@]flyn.org> 20060221-1
- Initial RPM.
