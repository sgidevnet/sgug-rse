%global srcname pytest-astropy-header

Name: python-%{srcname}
Version: 0.1.2
Release: 3%{?dist}
Summary: pytest plugin to add diagnostic info to the header of output

License: BSD
URL: https://www.astropy.org/
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
This plugin package provides a way to include information about the system, 
Python installation, and select dependencies in the header of the output 
when running pytest. It can be used with packages that are not affiliated 
with the Astropy project, but is optimized for use with 
astropy-related projects.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/pytest_astropy_header
%{python3_sitelib}/pytest_astropy_header-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Rebuilt for Python 3.9

* Mon Feb 17 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.1.2-2
- Do not include all files in python sitelib with wildcard

* Sat Jan 11 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.1.2-1
- initial packaging effort

