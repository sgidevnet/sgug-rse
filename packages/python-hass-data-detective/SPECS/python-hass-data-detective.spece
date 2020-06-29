%global pypi_name HASS-data-detective
%global pkg_name hass-data-detective

Name:           python-%{pkg_name}
Version:        2.3
Release:        1%{?dist}
Summary:        Tools for studying Home Assistant data

License:        MIT
URL:            https://github.com/robmarkcole/HASS-data-detective
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides a set of convenience functions and classes to analyze the
data in your Home Assistant database.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pandas
BuildRequires:  python3-pytz
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
This package provides a set of convenience functions and classes to analyze the
data in your Home Assistant database.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/detective/
%{python3_sitelib}/HASS_data_detective-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-1
- Update to new upstream release 2.3

* Tue Jun 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1-1
- Initial package for Fedora
