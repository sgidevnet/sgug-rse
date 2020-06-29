%global pypi_name pytest-ordering

Name:           python-%{pypi_name}
Version:        0.6
Release:        3%{?dist}
Summary:        Plugin to run your pytest tests in a specific order

License:        MIT
URL:            https://github.com/ftobia/pytest-ordering
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pytest-ordering is a pytest plugin to run your tests in any order that you
specify. It provides custom markers that say when your tests should run in
relation to each other. They can be absolute (i.e. first, or second-to-last)
or relative (i.e. run this test before this other test).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pytest-ordering is a pytest plugin to run your tests in any order that you
specify. It provides custom markers that say when your tests should run in
relation to each other. They can be absolute (i.e. first, or second-to-last)
or relative (i.e. run this test before this other test).

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-alabaster

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs/source/ html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=%{buildroot}%{python3_sitelib} \
  pytest-%{python3_version} -v tests -k "not test_run_marker_registered"

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/pytest_ordering/
%{python3_sitelib}/pytest_ordering-%{version}-py*.egg-info/

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-2
- Add missing BR
- Don't write byte code during tests (rhbz#1809537)

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- Initial package for Fedora
