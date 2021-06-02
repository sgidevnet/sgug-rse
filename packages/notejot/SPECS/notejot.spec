%global appname com.github.lainsce.notejot

Name:           notejot
Summary:        Stupidly-simple sticky notes applet
Version:        1.5.8
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/lainsce/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)

Requires:       hicolor-icon-theme


%description
Stupidly simple sticky notes applet.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Fri Aug 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.8-1
- Update to version 1.5.8.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.5-1
- Update to version 1.5.5.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.4-1
- Update to version 1.5.4.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.3-1
- Update to version 1.5.3.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1-1
- Update to version 1.5.1.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-1
- Update to version 1.5.0.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.5-1
- Update to version 1.4.5.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.3-1
- Update to version 1.4.3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.2-1
- Update to version 1.4.2.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.0-2
- Rebuild for granite5 soname bump.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.4.0-1
- Update to version 1.4.0.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.8-1
- Update to version 1.3.8.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.7-1
- Initial package.

