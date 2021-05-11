Name:    dnf-plugin-ovl
Version: 0.0.3
Release: 1%{?dist}
Summary: DNF plugin to work around overlayfs issues
URL:     https://github.com/FlorianLudwig/dnf-plugin-ovl
License: GPLv2+

Source0: https://github.com/FlorianLudwig/dnf-plugin-ovl/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

Requires: python3-dnf

%description
Workaround to run dnf on overlayfs. A port of yum-plugin-ovl to dnf.

%prep
%autosetup -n %{name}-%{version}

%build


%install
install -D -p ovl.py %{buildroot}/%{python3_sitelib}/dnf-plugins/ovl.py

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/dnf-plugins/ovl.py
%{python3_sitelib}/dnf-plugins/__pycache__/ovl.*

%changelog
* Thu Feb 20 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.0.3-1
- Update to 0.0.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3.20181107gitfd1a5a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2.20181107gitfd1a5a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.0.2-1.20181107gitfd1a5a5d
- Update to 0.0.2
- Use git snapshot to include latest upstream fixes
- Install license file

* Mon Nov 05 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.0.1-2
- Add missing Requires and BuildRequires
- Make package noarch

* Sun Feb 25 2018 Florian Ludwig <vierzigundzwei@gmail.com> - 0.0.1-1
- Initial package
