%global pypi_name pytest-toolbox

Name:           python-%{pypi_name}
Version:        0.4
Release:        4%{?dist}
Summary:        Numerous useful plugins for pytest

License:        MIT
URL:            https://github.com/samuelcolvin/pytest-toolbox
Source0:        https://github.com/samuelcolvin/pytest-toolbox/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Numerous useful plugins for pytest.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-isort
BuildRequires:  python3-pydantic
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Numerous useful plugins for pytest.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
  -k "not test_any_int_false and not test_is_uuid_false"
rm -rf %{buildroot}%{python3_sitelib}/pytest_toolbox/__pycache__/*.cpython-%{python3_version_nodots}-PYTEST.pyc

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/pytest_toolbox/
%{python3_sitelib}/pytest_toolbox-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-2
- Update removal of test files (rhbz#1787450)

* Thu Jan 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Initial package for Fedora
