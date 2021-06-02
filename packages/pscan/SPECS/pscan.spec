Name:           pscan
Version:        1.3
Release:        20%{?dist}
Summary:        Limited problem scanner for C source files

License:        GPLv2+
URL:            http://deployingradius.com/pscan/
Source0:        http://deployingradius.com/pscan/pscan.tar.gz
Patch0:         http://ftp.debian.org/debian/pool/main/p/pscan/pscan_1.2-9.diff.gz

BuildRequires:  gcc
BuildRequires:  flex

%description
PScan is a program which attempts to scan C source files for common
function abuses, which often lead to buffer overflows.


%prep
%setup -q -c
%patch0 -p1
patch -p1 -i debian/patches/20_pscan.patch
patch -p1 -i debian/patches/30_scanner.patch
patch -p0 -i debian/patches/40_max_stack.patch


%build
make %{?_smp_mflags} CC="%{__cc} -Wall $RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 pscan $RPM_BUILD_ROOT%{_bindir}/pscan
install -Dpm 644 debian/pscan.1 $RPM_BUILD_ROOT%{_mandir}/man1/pscan.1



%files
%doc COPYING README find_formats.sh stackguard.txt test.c wu-ftpd.pscan
%doc debian/changelog
%{_bindir}/pscan
%{_mandir}/man1/pscan.1*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.3-3
- Update Debian patchkit to 1.2-9 for support for larger source files
  (Debian bug 436794).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  9 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.3-1
- 1.3.

* Mon Aug  6 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.2-4
- License: GPLv2+

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.2-3
- Rebuild.

* Thu Feb 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.2-2
- Sync with Debian's 1.2-5.

* Sun Oct 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2-1
- First FE build.

* Wed Oct 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2-0.1
- First build, based on Debian's 1.2-4.
