%global common_description %{expand:
Granite is a companion library for GTK+ and GLib. Among other things, it
provides complex widgets and convenience functions designed for use in
apps built for elementary.}

Name:           granite
Summary:        elementary companion library for GTK+ and GLib
Version:        5.5.0
Release:        1%{?dist}
License:        LGPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.48.2
BuildRequires:  vala >= 0.40

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gobject-introspection-1.0)

# granite relies on org.gnome.desktop.interface for the clock-format setting
Requires:       gsettings-desktop-schemas

# granite provides and needs some generic icons
Requires:       hicolor-icon-theme

%description %{common_description}


%package        devel
Summary:        Granite Toolkit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

This package contains the development headers.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang granite


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/io.elementary.granite.demo.desktop

#appstream-util validate-relax --nonet \
#    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f granite.lang
%doc README.md
%license COPYING

%{_libdir}/libgranite.so.5
%{_libdir}/libgranite.so.5.*

%{_libdir}/girepository-1.0/Granite-1.0.typelib

%{_datadir}/icons/hicolor/*/actions/appointment.svg
%{_datadir}/icons/hicolor/*/actions/open-menu.svg
%{_datadir}/icons/hicolor/scalable/actions/open-menu-symbolic.svg

%{_datadir}/metainfo/%{name}.appdata.xml


%files devel
%doc README.md
%license COPYING

%{_bindir}/granite-demo

%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc

%{_includedir}/granite/

%{_datadir}/applications/io.elementary.granite.demo.desktop
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi


%changelog
* Fri Jul 03 2020 Fabio Valentini <decathorpe@gmail.com> - 5.5.0-1
- Update to version 5.5.0.

* Thu Apr 30 2020 Fabio Valentini <decathorpe@gmail.com> - 5.4.0-1
- Update to version 5.4.0.

* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 5.3.1-1
- Update to version 5.3.1.

* Thu Dec 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.0-1
- Update to version 5.3.0.

* Fri Sep 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.5-1
- Update to version 5.2.5.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.4-1
- Update to version 5.2.4.
- Drop obsolete datetime gsettings patch.

* Mon Feb 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3-2
- Fix typo in DateTime GSettings patch.

* Fri Feb 15 2019 Fabio Valentini <decathorpe@gmail.com> - 5.2.3-1
- Update to version 5.2.3.
- Remove obsolete patches (meson port, pkgconfig fixes).
- Rebase datetime gsettings patch.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.2-1
- Update to version 5.2.2.
- Add patch to fix a meson regression with the pkgconfig file.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.2.1-1
- Update to version 5.2.1.
- Port to meson.
- Resolve circular dependencies within Pantheon and fix third-party applications.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 5.1.0-1
- Update to version 5.1.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0-1
- Update to version 5.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5-2
- Remove icon cache scriptlets, replaced by file triggers.

* Fri Nov 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.5-1
- Update to version 0.5.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.1-1
- Update to version 0.4.1.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-8
- Make BR on /usr/bin/pkg-config explicit.

* Sun Nov 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-7
- Check granite-demo.desktop file explicitly.
- Correct license (s/LGPLv3/LGPLv3+).

* Sun Nov 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-6
- Add missing Requires to -devel.

* Thu Nov 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-5
- Spec file cosmetics.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-2
- Spec file cosmetics.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4.0.1-1
- Update to version 0.4.0.1.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.

