%global srcname         sound-theme

Name:           elementary-sound-theme
Summary:        Set of system sounds for elementary
Version:        1.0
Release:        4%{?dist}
License:        Unlicense

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson

BuildArch:      noarch


%description
A set of system sounds for elementary OS. Designed to be light, natural/
physical, and pleasant.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install


%files
%doc README.md
%license LICENSE

%{_datadir}/sounds/elementary/


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0-1
- Initial package for fedora.


