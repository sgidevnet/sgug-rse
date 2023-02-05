%global pypi_name xortool

Name:           %{pypi_name}
Version:        0.98
Release:        2%{?dist}
Summary:        A tool for XOR cipher analysis

License:        MIT
URL:            https://github.com/hellman/xortool
Source0:        https://github.com/hellman/xortool/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A tool to do some XOR analysis to guess the key length (based on count of
equal chars) and to guess the key (base on knowledge of most frequent char).

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' xortool/*.py

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-xor
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.98-1
- Initial package for Fedora
