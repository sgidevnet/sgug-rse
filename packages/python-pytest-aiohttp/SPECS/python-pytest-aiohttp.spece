%global pypi_name pytest-aiohttp

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        9%{?dist}
Summary:        A pytest plugin for aiohttp support

License:        ASL 2.0
URL:            https://github.com/aio-libs/pytest-aiohttp/
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitelib}/pytest_aiohttp/
%{python3_sitelib}/pytest_aiohttp*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-9
- Add python3-setuptools as BR

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-8
- Add python3-setuptools as BR

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-2
- Change source (rhbz#1719010)

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora
