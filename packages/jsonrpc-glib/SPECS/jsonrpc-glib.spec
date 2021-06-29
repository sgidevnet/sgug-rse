Name:           jsonrpc-glib
Version:        3.34.0
Release:        1%{?dist}
Summary:        A JSON-RPC library for GLib

License:        LGPLv2+
URL:            https://git.gnome.org/browse/jsonrpc-glib/
Source0:        https://download.gnome.org/sources/%{name}/3.34/%{name}-%{version}.tar.xz

# https://github.com/chergert/jsonrpc-glib/issues/3
Patch1: jsonrpc-glib-skip-test-stress.patch

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)

%description
Jsonrpc-GLib is a JSON-RPC library for GLib. It includes support for
communicating as both a JSON-RPC client and server. Additionally,
supports upgrading connections to use GVariant for less runtime overhead.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -D enable_gtk_doc=true
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING
%doc AUTHORS
%{_libdir}/libjsonrpc-glib-1.0.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Jsonrpc-1.0.typelib

%files devel
%doc CONTRIBUTING.md
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Jsonrpc-1.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/jsonrpc-glib
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/jsonrpc-glib-1.0.pc


%changelog
* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Wed Mar 13 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-2
- Rebuilt against fixed atk (#1626575)

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Sat Mar 03 2018 Kalev Lember <klember@redhat.com> - 3.27.91-1
- Update to 3.27.91

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90

* Fri Feb  2 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.4-2
- test-stress still failing randomly. Skip

* Tue Jan 30 2018 Kalev Lember <klember@redhat.com> - 3.27.4-1
- Update to 3.27.4
- Drop ldconfig scriptlets

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 3.27.1-1
- Update to 3.27.1

* Tue Oct  3 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.1-1
- Update to 3.26.1
- Drop most patches

* Wed Sep 13 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.0-2
- Some upstream fixes for different platforms
- Run tests, except test-stress

* Tue Sep 12 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.0-1
- Update to 3.26.0

* Tue Sep  5 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.92-1
- Update to 3.25.92

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.3-1
- Update to 3.25.3

* Fri Jun  9 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.2-2
- Address some issues from the other review - -2
- Initial spec
