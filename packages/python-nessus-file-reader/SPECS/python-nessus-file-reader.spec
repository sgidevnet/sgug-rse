%global pypi_name nessus-file-reader

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Python file reader for nessus files

License:        GPLv3+
URL:            https://github.com/LimberDuck/nessus-file-reader
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
nessus file reader is a python module created to quickly parse nessus files
containing the results of scans performed by using Nessus by (C) Tenable, Inc.
This module will let you get data through functions grouped into categories
like file, scan, host and plugin to get specific information.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
nessus file reader is a python module created to quickly parse nessus files
containing the results of scans performed by using Nessus by (C) Tenable, Inc.
This module will let you get data through functions grouped into categories
like file, scan, host and plugin to get specific information.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/nessus_file_reader/
%{python3_sitelib}/nessus_file_reader-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
