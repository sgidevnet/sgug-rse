%global pypi_name graphql-core

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        GraphQL implementation for Python

License:        MIT
URL:            https://github.com/graphql-python/graphql-core
Source0:        %{pypi_source}
BuildArch:      noarch

%description
GraphQL-core-3 is a Python port of GraphQL.js, the JavaScript reference
implementation for GraphQL, a query language for APIs.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-benchmark
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
GraphQL-core-3 is a Python port of GraphQL.js, the JavaScript reference
implementation for GraphQL, a query language for APIs.

%package -n python-%{pypi_name}-doc
Summary:       Documentation for %{name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for graphql-core.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/graphql/
%{python3_sitelib}/graphql_core-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.1-1
- Generate docs in install (rhbz#1836567)
- Update BR name
- Update to latest upstream release 3.1.1

* Thu May 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Initial package for Fedora
