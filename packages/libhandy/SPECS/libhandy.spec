Name:           libhandy
Version:        0.0.13
Release:        1%{?dist}
Summary:        Library with GTK+ widgets for mobile phones

License:        LGPLv2+
URL:            https://source.puri.sm/Librem5/libhandy/
Source0:        https://source.puri.sm/Librem5/libhandy/-/archive/v%{version}/libhandy-v%{version}.tar.bz2
Patch100:       libhandy.sgifixes.patch

BuildRequires:  gcc
#BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vala

%description
libhandy provides GTK+ widgets and GObjects to ease developing
applications for mobile phones.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libhandy-v%{version} -p1

%build
%meson -Dgtk_doc=false -Dexamples=false
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_libdir}/girepository-1.0/
%{_libdir}/libhandy-0.0.so.0*

%files devel
%{_includedir}/libhandy-0.0/
%{_libdir}/glade/
%{_libdir}/libhandy-0.0.so
%{_libdir}/pkgconfig/libhandy-0.0.pc
%{_datadir}/gir-1.0/
%{_datadir}/glade/
#%%{_datadir}/gtk-doc/
%{_datadir}/vala/

%changelog
* Mon Dec 21 2020  HAL <notes2@gmx.de> - 0.0.13-1
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 0.0.13-1
- Update to 0.0.13

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 0.0.11-1
- Update to 0.0.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 0.0.10-2
- Add patch to fix installation of glade resources for flatpak builds

* Thu Jun 13 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.10-1
- Update to 0.0.10

* Thu Mar 07 2019 Kalev Lember <klember@redhat.com> - 0.0.9-1
- Update to 0.0.9

* Fri Mar 1 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.8-2
- Pull an upstream fix to prevent broken translations in
  libhandy using apps

* Sat Feb 16 2019 Kalev Lember <klember@redhat.com> - 0.0.8-1
- Update to 0.0.8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Kalev Lember <klember@redhat.com> - 0.0.7-1
- Update to 0.0.7

* Fri Jan 11 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.6-2
- Swap some runtime vs devel bits

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 0.0.6-1
- Initial Fedora packaging
