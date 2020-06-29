%global pypi_name ansiwrap

Name:           python-%{pypi_name}
Version:        0.8.4
Release:        1%{?dist}
Summary:        Text wrapper with ANSI colors and styles support

License:        ASL 2.0
URL:            https://github.com/jonathaneunice/ansiwrap
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

%description
ansiwrap wraps text, like the standard textwrap module. But it also correctly
wraps text that contains ANSI control sequences that colorize or style text.
Where textwrap is fooled by the raw string length of those control codes,
ansiwrap is not; it understands that however much those codes affect color
and display style, they have no logical length.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-ansicolors
BuildRequires:  python3-coverage
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
BuildRequires:  python3-textwrap3
BuildRequires:  python3-tox
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
ansiwrap wraps text, like the standard textwrap module. But it also correctly
wraps text that contains ANSI control sequences that colorize or style text.
Where textwrap is fooled by the raw string length of those control codes,
ansiwrap is not; it understands that however much those codes affect color
and display style, they have no logical length.

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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.4-1
- Initial package for Fedora
