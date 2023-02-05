Name: fedora-workstation-backgrounds
Version: 1.1
Release: 6%{?dist}
Summary: Desktop backgrounds for Fedora Workstation

License: CC-BY-SA and CC-BY and CC0
URL: https://pagure.io/fedora-design/fedora-workstation-backgrounds
Source0: https://releases.pagure.org/fedora-design/%{name}/%{name}-%{version}.tar.gz

BuildArch: noarch

%description
The fedora-workstation-backgrounds packages contains the additional standard
wallpapers for Fedora Workstation.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README AUTHORS
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Ryan Lerch <rlerch@redhat.com> - 1.1-1
- Initial Release
