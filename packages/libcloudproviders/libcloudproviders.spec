%global api_version 0.3

Name:           libcloudproviders
Summary:        Library for integration of cloud storage providers
Version:        0.3.1
Release:        1%{?dist}
License:        LGPLv3+

URL:            https://gitlab.gnome.org/World/libcloudproviders
Source0:        https://ftp.gnome.org/pub/GNOME/sources/libcloudproviders/%{api_version}/libcloudproviders-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Cross desktop library for desktop integration of cloud storage providers
and sync tools.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -Denable-gtk-doc=true
%meson_build


%install
%meson_install


%files
%doc CHANGELOG README.md
%license LICENSE

%{_libdir}/%{name}.so.0*
%{_libdir}/girepository-1.0/CloudProviders-%{api_version}.typelib

%files devel
%{_includedir}/cloudproviders/

%{_libdir}/pkgconfig/cloudproviders.pc
%{_libdir}/%{name}.so

%{_datadir}/gir-1.0/CloudProviders-%{api_version}.gir
%{_datadir}/gtk-doc/
%{_datadir}/vala/vapi/cloudproviders.*


%changelog
* Mon Jun 08 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.

* Mon Aug 19 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-1
- Update to version 0.3.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Carlos Soriano <csoriano@redhat.com> - 0.2.5-0.1
- Initial RPM release

