%global pypi_name opendata-transport

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        4%{?dist}
Summary:        Python client for interacting with transport.opendata.ch

License:        MIT
URL:            https://github.com/fabaff/python-opendata-transport
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python client for interacting with transport.opendata.ch. This module is
simply retrieving the details about a given connection between two stations.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python client for interacting with transport.opendata.ch. This module is
simply retrieving the details about a given connection between two stations.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc CHANGES.rst README.rst example.py
%license LICENSE
%{python3_sitelib}/opendata_transport/
%{python3_sitelib}/python_opendata_transport*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Update to latest upstream release 0.2.1

* Tue Dec 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Update to latest upstream release 0.2.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-2
- Change source (rhbz#1718903)

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-1
- Initial package for Fedora
