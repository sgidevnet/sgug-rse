%global pypi_name textparser

Name:           python-%{pypi_name}
Version:        0.23.0
Release:        3%{?dist}
Summary:        Python text parser

License:        MIT
URL:            https://github.com/eerimoq/textparser
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A text parser written in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A text parser written in Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.23.0-2
- Update source URL
- Fix ownership and style (rhbz#1795071)

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.23.0-1
- Initial package for Fedora
