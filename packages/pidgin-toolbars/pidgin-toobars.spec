# This is a plugin, so we don't need strict symbol linkage.
%undefine _strict_symbol_defs_build

Name: pidgin-toobars
Version: 1.14
Release: 12%{?dist}
Summary: Toolbar and status bar for Pidgin

License: GPLv2+
Source0: http://vayurik.ru/wordpress/wp-content/uploads/toobars/%{version}/%{name}-%{version}.tar.gz
Patch0: 0001-Fix-incorrect-FSF-address.patch
URL: http://vayurik.ru/en/toobars

BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(pidgin)
BuildRequires: intltool
BuildRequires: gcc
#Requires: pidgin%{?_isa}

%description
This plugin adds toolbar and status bar to Pidgin buddy list.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%find_lang toobars
rm -f %{buildroot}%{_libdir}/pidgin/toobars.la

%files -f toobars.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/pidgin/toobars.so
%{_datadir}/pixmaps/pidgin/buttons/*.png

%changelog
* Sat Sep 05 2020  HAL <notes2@gmx.de> - 
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-8
- Fixed build under Fedora Rawhide.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-5
- Some SPEC fixes.

* Mon Mar 27 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-4
- Added missing BR: gcc.

* Thu Nov 24 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-3
- Build against new Pidgin releases.

* Sat Jan 30 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-2
- Fixed SPEC. Added support of Fedora 22+.

* Mon Jul 29 2013 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-1
- Updated to v. 1.14. Fixed build under Fedora 19+.

