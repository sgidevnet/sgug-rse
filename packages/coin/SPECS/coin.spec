# Enable LTO
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

%global uuid    com.github.lainsce.%{name}

Name:           coin
Version:        1.3.0
Release:        1%{?dist}
Summary:        Track the virtual currencies in real world currency value

License:        GPLv3+
URL:            https://github.com/lainsce/coin
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  vala
Requires:       hicolor-icon-theme

%description
Track the virtual currencies in real world currency value with this handy
applet.

- Choose which currency and virtual currency to use for tracking
- Quit anytime with the shortcut Ctrl + Q
- Move the applet by dragging it from anywhere in the window
- Stays out of your way in the desktop


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
# Disable temporary
# * timestamp is in the future
#appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.appdata.xml


%changelog
* Sat Feb 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.7-1
- Update to 1.2.7

* Mon Aug 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.6-2
- Initial package
