Name:           deepin-gtk-theme
Version:        17.10.11
Release:        1%{?dist}
Summary:        Deepin GTK Theme
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-gtk-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{summary}.

%prep
%setup -q

%build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_datadir}/themes/deepin/
%{_datadir}/themes/deepin-dark/

%changelog
* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 17.10.11-1
- Release 17.10.11

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 17.10.10-1
- Update to 17.10.10

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 17.10.8-1
- Update to 17.10.8

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 17.10.7-1
- Update to 17.10.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 17.10.5-1
- Update to 17.10.5

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 17.10.4-1
- Update to 17.10.4

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 17.10.3-1.git6140502
- Update to 17.10.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 17.10.2-1.giteba2cf4
- Update to 17.10.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 15.12.8-1.git9fd5f70
- Update to 15.12.8

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build
