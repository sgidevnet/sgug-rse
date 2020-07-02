%global pypi_name socks5line

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        2%{?dist}
Summary:        Helper for socks5-unaware clients

License:        MIT
URL:            https://github.com/skelsec/socks5line
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Helping tunneling for proxy-unaware scripts.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Helping tunneling for proxy-unaware scripts.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-2
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Use LICENSE file shipped in source tarball
- Update to latest upstream release 0.0.4 (rhbz#1818642)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-2
- Fix BR

* Mon Jan 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-1
- Initial package for Fedora
