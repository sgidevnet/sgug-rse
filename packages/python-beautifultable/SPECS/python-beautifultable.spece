%global pypi_name beautifultable

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        2%{?dist}
Summary:        Print ASCII tables for terminals

License:        MIT
URL:            https://github.com/pri22296/beautifultable
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides the BeautifulTable class for easily printing tabular data
in a visually appealing ASCII format to a terminal.

Features included but not limited to:

- Full customization of the look and feel of the table
- Build the Table as you wish, By adding rows, or by columns or even mixing both
  these approaches
- Full support for colors using ANSI sequences or any library of your choice
- Plenty of predefined styles for multiple use cases and option to create
  custom ones
- Support for Unicode characters

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wcwidth
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
This package provides the BeautifulTable class for easily printing tabular data
in a visually appealing ASCII format to a terminal.

Features included but not limited to:

- Full customization of the look and feel of the table
- Build the Table as you wish, By adding rows, or by columns or even mixing both
  these approaches
- Full support for colors using ANSI sequences or any library of your choice
- Plenty of predefined styles for multiple use cases and option to create
  custom ones
- Support for Unicode characters

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} test.py

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%files -n %{name}-doc
%doc html
%license LICENSE.txt

%changelog
* Thu Apr 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-2
- Add missing BR for tests (rhbz#1812435)

* Wed Mar 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Initial package for Fedora
