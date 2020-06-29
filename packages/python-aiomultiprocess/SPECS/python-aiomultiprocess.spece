%global pypi_name aiomultiprocess

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Asyncio version of the standard multiprocessing module

License:        MIT
URL:            https://github.com/jreese/aiomultiprocess
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
aiomultiprocess presents a simple interface, while running a full AsyncIO
event loop on each child process, enabling levels of concurrency never
before seen in a Python application. Each child process can execute multiple
coroutines at once, limited only by the workload and number of cores available.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiomultiprocess presents a simple interface, while running a full AsyncIO
event loop on each child process, enabling levels of concurrency never
before seen in a Python application. Each child process can execute multiple
coroutines at once, limited only by the workload and number of cores available.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Initial package for Fedora
