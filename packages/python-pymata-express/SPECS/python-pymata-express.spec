%global pypi_name pymata-express

Name:           python-%{pypi_name}
Version:        1.17
Release:        1%{?dist}
Summary:        Python Protocol Abstraction Library For Arduino Firmata

License:        AGPLv3
URL:            https://github.com/MrYsLab/pymata-express
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Pymata-Express is a Firmata client that allows you to control an Arduino using
the high-performance FirmataExpress sketch. It uses a conventional Python API
for those that do not need or wish to use the asyncio programming paradigm of
pymata-express.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pymata-Express is a Firmata client that allows you to control an Arduino using
the high-performance FirmataExpress sketch. It uses a conventional Python API
for those that do not need or wish to use the asyncio programming paradigm of
pymata-express.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license license.txt
%{python3_sitelib}/pymata_express/
%{python3_sitelib}/pymata_express-%{version}-py*.egg-info/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.17-1
- Update to latest upstream release 1.17

* Wed May 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.15-1
- Update to latest upstream release 1.15

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.13-1
- Update to latest upstream release 1.13

* Wed Apr 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-1
- Initial package for Fedora
