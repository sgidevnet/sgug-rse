%global pypi_name py-gql

Name:           python-%{pypi_name}
Version:        0.6.1
Release:        2%{?dist}
Summary:        Comprehensive GraphQL implementation for Python

License:        MIT
URL:            https://github.com/lirsacc/py-gql
Source0:        %{url}/releases/download/v%{version}/py_gql-%{version}.tar.gz
BuildArch:      noarch

%description
py-gql is a pure Python GraphQL implementation aimed at creating GraphQL
servers and providing common tooling.

It supports:

- Parsing the GraphQL query language and schema definition language.
- Building a GraphQL type schema programmatically and from Schema Definition
  files (including support for schema directives).
- Validating and Executing a GraphQL request against a type schema.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-coverage
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
py-gql is a pure Python GraphQL implementation aimed at creating GraphQL
servers and providing common tooling.

It supports:

- Parsing the GraphQL query language and schema definition language.
- Building a GraphQL type schema programmatically and from Schema Definition
  files (including support for schema directives).
- Validating and Executing a GraphQL request against a type schema.

%prep
%autosetup -n py_gql-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/py_gql/
%{python3_sitelib}/py_gql-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-2
- Run tests as pytest is now available (rhbz#1837139)

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Initial package for Fedora
