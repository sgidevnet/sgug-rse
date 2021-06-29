Name:           wafw00f
Version:        2.1.0
Release:        1%{?dist}
Summary:        A tool to identifies and fingerprints Web Application Firewall (WAF)

License:        BSD
URL:            https://github.com/sandrogauci/wafw00f
Source0:        https://github.com/sandrogauci/wafw00f/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
WAFW00F identifies and fingerprints Web Application Firewall (WAF) products.

%prep
%autosetup -n %{name}-%{version}
sed -i -e '/^#!\//, 1d' {wafw00f/*.py,wafw00f/*/*.py}

%build
%py3_build

%install
%py3_install

%files
%doc CREDITS.txt README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

%changelog
* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0
- Fix installation issue (rhbz#1770879)
- Remove patch

* Mon Oct 07 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-3
- Add patch to remove release pinning

* Wed Sep 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-2
- Remane BRs

* Sun May 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Fix files section and add tests
- Update to latest upstream release 1.0.0

* Thu Apr 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.6-1
- Update to latest upstream release 0.9.6

* Mon Nov 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Update to latest upstream release 0.9.4

* Sun Oct 12 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Initial package for Fedora
