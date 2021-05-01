Name:           pangox-compat
Version:        0.0.2
Release:        15%{?dist}
Summary:        Compatibility library for pangox

License:        LGPLv2+
URL:            http://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/%{name}-%{version}.tar.xz

BuildRequires:  pango-devel
BuildRequires:  gcc

%description
This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.  

%package devel
Summary: Development files for pangox-compat
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup


%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

#%%ldconfig_scriptlets


%files
%doc README NEWS AUTHORS
%license COPYING
%{_libdir}/libpango*-*.so.*
%dir %{_sysconfdir}/pango
%config %{_sysconfdir}/pango/pangox.aliases

%files devel
%{_libdir}/libpango*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Fri Sep 18 2020  HAL <notes2@gmx.de> - 0.0.2-15
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.0.2-12
- Add BuildRequires: gcc as per packaging guidelines
- Added %%license
- Removed group tag
- Used %%autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 05 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.0.2-2
- Resolves:rh#907552 - unowned directory /etc/pango after pangox-compat installation

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 0.0.2-1
- Update to 0.0.2

* Tue Aug 28 2012 Parag Nemade <pnemade AT redhat DOT com> - 0.0.1-1
- Initial package
