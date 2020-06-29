%global pypi_name mysqlclient
%bcond_with mysqldb

Name:           python-%{pypi_name}
Version:        1.4.6
Release:        2%{?dist}
Summary:        MySQL/mariaDB database connector for Python

License:        GPLv2
URL:            https://github.com/PyMySQL/mysqlclient-python
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  mysql-devel

%description
MySQLdb is an interface to the popular MySQL database server that provides
the Python database API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with mysqldb}
%check
BuildRequires:  python3-pytest
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MySQLdb is an interface to the popular MySQL database server that provides
the Python database API.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  python3-sphinx
%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-python-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%if %{with mysqldb}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests
%endif

%files -n python3-%{pypi_name}
%doc README.md HISTORY.rst
%license LICENSE
%{python3_sitearch}/MySQLdb/
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.6-2
- Add tests and missing BR
- Fix license (rhbz#1816295)

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.6-1
- Initial package for Fedora
