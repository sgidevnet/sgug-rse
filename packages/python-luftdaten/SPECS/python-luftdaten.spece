%global pypi_name luftdaten

Name:           python-%{pypi_name}
Version:        0.6.4
Release:        3%{?dist}
Summary:        Python API wrapper for interacting with luftdaten.info

License:        MIT
URL:            https://github.com/fabaff/python-luftdaten
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python API wrapper for interacting with luftdaten.info

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python API wrapper for interacting with luftdaten.info.

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
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.4-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.4.-1
- Update to latest upstream release 0.6.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.3-1
- Update to new upstream release 0.6.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Update to new upstream release 0.6.2

* Wed Jun 26 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Update to new upstream release 0.6.1

* Tue Jun 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Update to new upstream release 0.6.0

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Initial package for Fedora
