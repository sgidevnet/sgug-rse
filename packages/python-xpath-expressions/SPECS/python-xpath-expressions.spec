%global pypi_name xpath-expressions

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        2%{?dist}
Summary:        Treat XPath expressions as Python objects

License:        MIT
URL:            https://github.com/orf/xpath-expressions
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This is a small, lightweight Python library to aide in the manipulations of
xpath expressions. It allows you to manipulate them as Python objects with
Python expressions and operators.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a small, lightweight Python library to aide in the manipulations of
xpath expressions. It allows you to manipulate them as Python objects with
Python expressions and operators.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/xpath/
%{python3_sitelib}/xpath_expressions-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.2-1
- Add LICENSE file (rhbz#1816759)

* Tue Mar 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora
