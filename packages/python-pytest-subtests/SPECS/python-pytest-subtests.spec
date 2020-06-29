%global pypi_name pytest-subtests

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        2%{?dist}
Summary:        Support for unittest subTest() and subtests fixture

License:        MIT
URL:            https://github.com/pytest-dev/pytest-subtests
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pytest-subtests unittest subTest() support and subtests fixture.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
pytest-subtests unittest subTest() support and subtests fixture.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# https://github.com/pytest-dev/pytest-subtests/issues/21
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=%{buildroot}%{python3_sitelib} \
  pytest-%{python3_version} -v tests \
  -k "not TestFixture and not TestCapture and not test_simple_terminal"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_subtests.py
%{python3_sitelib}/pytest_subtests-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora
