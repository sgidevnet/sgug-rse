%global pypi_name aiopg
%bcond_with docker

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        3%{?dist}
Summary:        Postgres integration with asyncio

License:        BSD
URL:            https://aiopg.readthedocs.io
Source0:        https://github.com/aio-libs/aiopg/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the Psycopg
database driver.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with docker}
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-sugar
BuildRequires:  python3-pytest-timeout
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the Psycopg
database driver.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Use a different module
sed -i -e "s/'psycopg2-binary>=2.7.0'/'psycopg2'/g" setup.py

%build
%py3_build

%install
%py3_install

%if %{with docker}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-2
- Make tests optional
- Don't use psycopg2-binary (rhbz#1787218)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package for Fedora
