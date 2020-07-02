%global pypi_name volkszaehler

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        8%{?dist}
Summary:        Python Client for interacting with the Volkszahler API

License:        MIT
URL:            https://github.com/home-assistant-ecosystem/python-volkszaehler
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python client for interacting with the Volkszahler API.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python client for interacting with the Volkszahler API.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc CHANGES.rst README.rst example.py
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-8
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-2
- Change source (rhbz#1718886)

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora
