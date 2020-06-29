%global pypi_name ssdp

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Python library for Simple Service Discovery Protocol (SSDP)

License:        MIT
URL:            https://github.com/codingjoe/ssdp
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python asyncio library for Simple Service Discovery Protocol (SSDP). SSDP is
a UPnP sub standard.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python asyncio library for Simple Service Discovery Protocol (SSDP). SSDP is
a UPnP sub standard.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora
