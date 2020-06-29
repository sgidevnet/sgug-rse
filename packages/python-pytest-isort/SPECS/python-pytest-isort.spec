%global pypi_name pytest-isort

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        4%{?dist}
Summary:        Pytest plugin to check import ordering using isort

License:        BSD
URL:            http://github.com/moccu/pytest-isort/
Source0:        http://github.com/moccu/pytest-isort/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
py.test plugin to check import ordering using isort.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-isort
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
py.test plugin to check import ordering using isort.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v test_isort.py \
  -k "not test_file_no_ignored and not test_file_ignored and not \
  test_correctly_sorted and not test_incorrectly_sorted"
rm -rf %{buildroot}%{python3_sitelib}/__pycache__/pytest_isort.cpython-%{python3_version_nodots}-PYTEST.pyc

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_isort.py
%{python3_sitelib}/pytest_isort-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-2
- Update removal of test files (rhbz#1787443)

* Thu Jan 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Initial package for Fedora
