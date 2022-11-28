%global pypi_name asteval

Name:           python-%{pypi_name}
Version:        0.9.18
Release:        1%{?dist}
Summary:        Evaluator of Python expression using ast module

License:        MIT
URL:            http://github.com/newville/asteval
Source0:        %{pypi_source}
BuildArch:      noarch

%description
ASTEVAL is a safe(ish) evaluator of Python expressions and statements,
using Python's ast module. The idea is to provide a simple, safe, and robust
miniature mathematical language that can handle user-input. The emphasis here
is on mathematical expressions, and so many functions from numpy are imported
and used if available.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
ASTEVAL is a safe(ish) evaluator of Python expressions and statements,
using Python's ast module. The idea is to provide a simple, safe, and robust
miniature mathematical language that can handle user-input. The emphasis here
is on mathematical expressions, and so many functions from numpy are imported
and used if available.

%package -n python-%{pypi_name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' asteval/asteval.py

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo} html/_static/empty

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Dec 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.18-1
- Initial package for Fedora
