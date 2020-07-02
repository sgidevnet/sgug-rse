%global srcname python-masscan

Name:           %{srcname}
Version:        0.1.6
Release:        1%{?dist}
Summary:        Python module to interact with masscan

License:        GPLv3+
URL:            https://github.com/MyKings/python-masscan
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

Requires:       masscan

%description
python-masscan is a python library which helps in using masscan port scanner.

%package -n python3-masscan
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-masscan}

%description -n python3-masscan
python-masscan is a python library which helps in using masscan port scanner.

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' masscan/*.py

%build
%py3_build

%install
%py3_install

%files -n python3-masscan
%doc CHANGELOG.md README.rst
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/masscan/

%changelog
* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.6-1
- Update to latest upstream release 0.1.6

* Sun Apr 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora
