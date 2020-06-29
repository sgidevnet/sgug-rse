%global pypi_name cx_Oracle
%global local_name cx-oracle
# Tests requires the Oracle Client libraries
%bcond_with check

Name:           python-%{local_name}
Version:        7.3.0
Release:        3%{?dist}
Summary:        Python interface to Oracle

License:        BSD
URL:            https://oracle.github.io/python-cx_Oracle
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Python interface to Oracle Database conforming to the Python DB API 2.0
specification.

%package -n     python3-%{local_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{local_name}}

%description -n python3-%{local_name}
Python interface to Oracle Database conforming to the Python DB API 2.0
specification.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_prefix}/cx_Oracle-doc

%if %{with check}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{local_name}
%license LICENSE.txt
%doc README.txt
%{python3_sitearch}/cx_Oracle.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.3.0-3
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 7.3.0-2
- Update path
- Add missing BR (rhbz#1816279)

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 7.3.0-1
- Initial package for Fedora
