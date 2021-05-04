Name:           arandr
Version:        0.1.10
Release:        1%{?dist}
Summary:        Simple GTK+ XRandR GUI

License:        GPLv3
URL:            http://christian.amsuess.com/tools/arandr/
Source0:        http://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz
Patch0:         0001-Make-ARandR-appear-in-XFCE-Settings-Manager.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  gettext
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils
Requires:       python3
Requires:       python3-gobject
Requires:       xorg-x11-server-utils

%description
ARandR is designed to provide a simple visual front end for XRandR 1.2/1.3.
Relative monitor positions are shown graphically and can be changed in a
drag-and-drop way.

%prep
%setup -q
%patch0 -p1


%build
%py3_build

%install
%py3_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/arandr.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc README TODO ChangeLog NEWS
%license COPYING
%{_bindir}/arandr
%{_bindir}/unxrandr
%{python3_sitelib}/screenlayout/
%{python3_sitelib}/arandr-%{version}-py*.egg-info
%{_mandir}/man1/arandr.1.*
%{_mandir}/man1/unxrandr.1.*
%{_datadir}/applications/arandr.desktop


%changelog
* Mon Aug 26 2019 Frantisek Sumsal <frantisek@sumsal.cz> - 0.1.10-1
- New version (0.1.10)
- arandr now uses python3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.9-2
- Update spec file
- Add build requires python2-devel

* Thu Aug 04 2016 Maros Zatko <mzatko@fedoraproject.org> - 0.1.9-1
- new version (0.1.9)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 14 2013 Maros Zatko <mzatko@fedoraproject.org> - 0.1.7.1-3
- Add patch for ARandR to be in XFCE Settings Manager

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Maros Zatko <mzatko@fedoraproject.org> - 0.1.7-1
- new version (1.7.1)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Maros Zatko <mzatko@fedoraproject.org> - 0.1.6-1
- new version (1.6)

* Mon Oct 03 2011 Maros Zatko <mzatko@fedoraproject.org> - 0.1.4-4
- fixed tab indentation
- changed py2.7 -> py*

* Mon Sep 19 2011 Maros Zatko <mzatko@fedoraproject.org> - 0.1.4-3
- RPM_BUILD_ROOT replaced by macro
- doc files are handled completely by doc macro

* Sat Sep 17 2011 Maros Zatko <mzatko@fedoraproject.org> - 0.1.4-2
- tabs replaced by spaces
- COPYING, README, ChangeLog, NEWS and TODO doc entry
- fixed date in previous changelog entry
- desktop files installed according to guidelines

* Thu Sep 15 2011 Maros Zatko <mzatko@fedoraproject.org> - 0.1.4-1
- Initial package
