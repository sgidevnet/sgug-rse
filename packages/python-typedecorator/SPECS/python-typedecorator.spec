%global pypi_name typedecorator

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        1%{?dist}
Summary:        Decorator-based type checking library

License:        MIT
URL:            https://github.com/dobarkod/typedecorator/
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A decorator-based implementation of type checks for Python. Provides
@params, @returns and @void decorators for describing the type of the
function arguments and return values. If the types mismatch, an exception
can be thrown, the mismatch can be logged, or it can be ignored.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A decorator-based implementation of type checks for Python. Provides
@params, @returns and @void decorators for describing the type of the
function arguments and return values. If the types mismatch, an exception
can be thrown, the mismatch can be logged, or it can be ignored.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Shebang: https://github.com/dobarkod/typedecorator/pull/14
sed -i -e '/^#!\//, 1d' typedecorator/__init__.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} tests3.py

%files -n python3-%{pypi_name}
%doc README.md
# Missing license: https://github.com/dobarkod/typedecorator/pull/15
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun May 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- Initial package for Fedora
