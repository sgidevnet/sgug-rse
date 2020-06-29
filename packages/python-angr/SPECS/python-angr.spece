%global srcname angr

# Have arch-specific dependencies, so cannot build as noarch.
# No ppc64le python-pyvex.
ExcludeArch: ppc64le
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        8.20.6.8
Release:        4%{?dist}
Summary:        A multi-architecture binary analysis toolkit

License:        BSD and ASL 2.0
URL:            https://angr.io/
Source0:        %{pypi_source}
Source1:        PACKAGE-LICENSING
Source2:        LICENSE-ASL-2.0

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  unicorn-devel
BuildRequires:  python3-pyvex
BuildRequires:  python3-unicorn

%description
angr is a platform-agnostic binary analysis framework with the ability
to perform dynamic symbolic execution and various static analyses on
binaries.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
angr is a platform-agnostic binary analysis framework with the ability
to perform dynamic symbolic execution and various static analyses on
binaries.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install
cp %{SOURCE1} .
cp %{SOURCE2} .

%files -n python3-%{srcname}
%doc README.md
%license PACKAGE-LICENSING
%license LICENSE
%license LICENSE-ASL-2.0
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/angr/

%changelog
* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-4
- Exclude ppc64le, because python-pyvex not available on ppc64le

* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-3
- Add note about dual license 

* Mon Jun 22 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-2
- Add some BuildRequires

* Sat Jun 20 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-1
- New upstream version
- BuildRequires gcc-c++
- Use pypi_source macro

* Mon May 25 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-1
- Initial package
