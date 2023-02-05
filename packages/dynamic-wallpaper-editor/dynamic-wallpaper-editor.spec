%global uuid    com.github.maoschanz.DynamicWallpaperEditor

Name:           dynamic-wallpaper-editor
Version:        2.2.1
Release:        2%{?dist}
Summary:        Utility for creation or edition GNOME desktop's XML wallpapers

License:        GPLv3+
URL:            https://github.com/maoschanz/dynamic-wallpaper-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       hicolor-icon-theme

%description
The GNOME desktop allows the wallpaper to change with time.

These dynamic wallpapers are XML files, and you don't want to write these
files yourself: Dynamic Wallpaper Editor is a little utility for the creation
or the edition of these XML wallpapers.


%prep
%autosetup


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
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.xml


%changelog
* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.1-2
- Tiny fix

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0-2
- Update to 2.1.0

* Mon Jul 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-2
- Initial package
