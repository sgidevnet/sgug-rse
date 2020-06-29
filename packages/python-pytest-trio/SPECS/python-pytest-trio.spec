%global pypi_name pytest-trio

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Pytest plugin for trio

License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/pytest-trio
Source0:        https://github.com/python-trio/pytest-trio/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a pytest plugin to help you test projects that use Trio, a friendly
library for concurrency and async I/O in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-async-generator
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-setuptools
BuildRequires:  python3-trio
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a pytest plugin to help you test projects that use Trio, a friendly
library for concurrency and async I/O in Python.

%package -n python-%{pypi_name}-doc
Summary:        pytest-trio documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-trio
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i /RemovedInPytest4Warning/d pytest_trio/_tests/conftest.py

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# https://github.com/python-trio/pytest-trio/issues/84
#%check
#PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v pytest_trio

%files -n python3-%{pypi_name}
%license LICENSE.MIT LICENSE LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/pytest_trio/
%{python3_sitelib}/pytest_trio-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.MIT LICENSE LICENSE.APACHE2

%changelog
* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Update to latest upstream release 0.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Initial package for Fedora
