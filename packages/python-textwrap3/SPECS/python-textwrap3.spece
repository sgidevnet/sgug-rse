# Created by pyp2rpm-3.3.4
%global pypi_name textwrap3

Name:           python-%{pypi_name}
Version:        0.9.2
Release:        1%{?dist}
Summary:        Text wrap backport

License:        Python
URL:            https://github.com/jonathaneunice/textwrap3
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

%description
textwrap3 is a compatibility back-port of Python 3.6’s textwrap module. This
makes a few new APIs such as shorten and the max_lines parameter available
in a compatible way to all Python versions typically in current use.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-coverage
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
BuildRequires:  python3-tox
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
textwrap3 is a compatibility back-port of Python 3.6’s textwrap module. This
makes a few new APIs such as shorten and the max_lines parameter available
in a compatible way to all Python versions typically in current use.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v test

%files -n python3-%{pypi_name}
%doc README.rst
# Missing license file: https://github.com/jonathaneunice/textwrap3/issues/1
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.2-1
- Initial package for Fedora
