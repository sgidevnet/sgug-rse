%global uuid    com.github.maoschanz.drawing

Name:           drawing
Version:        0.4.4
Release:        1%{?dist}
Summary:        Drawing application for the GNOME desktop

License:        GPLv3+
URL:            https://github.com/maoschanz/drawing
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       hicolor-icon-theme

%description
This application is a basic image editor, similar to Microsoft Paint,
but aiming at the GNOME desktop.

PNG, JPEG and BMP files are supported.

Besides GNOME, some more traditional design layouts are available too,
as well as an elementaryOS layout. It should also be compatible with
Purism's Librem 5 phone.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/%{uuid}.appdata.xml

%changelog
* Tue Sep 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.4-1
- Update to 0.4.4

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Tue Jul 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Sun Jul 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2-1
- Initial package.
