%global pypi_name pytenable

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Python library to interface with Tenable's products and applications

License:        MIT
URL:            https://github.com/tenable/pytenable
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pyTenable is intended to be a pythonic interface into the Tenable application
APIs. Further by providing a common interface and a common structure between
all of the various applications, we can ease the transition from the vastly
different APIs between some of the products.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-requests
BuildRequires:  python3-restfly
BuildRequires:  python3-dateutil
BuildRequires:  python3-defusedxml
BuildRequires:  python3-requests-pkcs12
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-vcr
BuildRequires:  python3-pytest-datafiles
BuildRequires:  python3-semver
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
pyTenable is intended to be a pythonic interface into the Tenable application
APIs. Further by providing a common interface and a common structure between
all of the various applications, we can ease the transition from the vastly
different APIs between some of the products.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n pyTenable-%{version}
rm -rf %{pypi_name}.egg-info
# Remove standard lib
sed -i -e '43d' setup.py

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo,nojekyll}

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests -k "not docker"

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/tenable/
%{python3_sitelib}/pyTenable-%{version}-py*.egg-info
%exclude %{python3_sitelib}/tests

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Remove configuration file for publishing
- Remove standard library (rhbz#1815272)
- Update to latest upstream release 1.1.1

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
