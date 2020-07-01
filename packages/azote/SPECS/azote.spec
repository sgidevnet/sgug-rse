# -*-Mode: rpm-spec -*-

Name:      azote
Version:   1.7.12
Release:   1%{?dist}
BuildArch: noarch
Summary:   Wallpaper and colour manager for Sway, i3 and some other WMs

# GPLv3: main program
# BSD: colorthief.py
License:   GPLv3 and BSD

URL:       https://github.com/nwg-piotr/azote
Source0:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-devel

Requires: python3-send2trash
Requires: python3-pillow
Requires: python3-gobject

Provides: bundled(python3-colorthief) = 0.2.1

%description
Azote is a GTK+3 - based picture browser and background setter, as the
frontend to the swaybg (sway/Wayland) and feh (X windows) commands. It
also includes several colour management tools.

The program is confirmed to work on sway, i3, Openbox, Fluxbox and dwm
window managers, on Arch Linux, Void Linux, Debian and Fedora.

%prep
%autosetup

%build
%py3_build

%install
%py3_install
# not sure why setup.py doesn't do this, but:
install -p -D dist/%{name} %{buildroot}/%{_bindir}/%{name}
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/applications dist/%{name}.desktop
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/%{name} dist/*.png dist/*.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*

%doc README.md

%license LICENSE LICENSE-COLORTHIEF

%changelog
* Wed Jun 24 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.12-1
- new release

* Mon Jun 01 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-7
- rebuilt to fix runpath error in f32

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.10-6
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-5
- update per RHBZ#1813737

* Tue Mar 17 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-4
- update per RHBZ#1813737

* Tue Mar 17 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-3
- update per RHBZ#1813737

* Mon Mar 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-2
- update per RHBZ#1813737

* Mon Mar 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-1
- new release

* Mon Feb 24 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.9-2.fc31.wef
- fix location of icons to what the .desktop expects

* Mon Feb 24 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.9-1.fc31.wef
- Initial version of the package
