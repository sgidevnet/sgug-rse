%global pypi_name scramp

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Implementation of the SCRAM protocol

License:        MIT
URL:            https://github.com/tlocke/scramp
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Scramp is pure-Python implementation of the SCRAM authentication protocol.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Scramp is a pure-Python implementation of the SCRAM authentication protocol.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%doc README.adoc
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Update to latest upstream release 1.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to latest upstream release 1.1.1

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
