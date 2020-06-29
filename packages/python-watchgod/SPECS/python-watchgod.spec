# what it's called on pypi
%global srcname watchgod
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Simple, modern file watching and code reload in python.  watchgod is inspired
by watchdog, hence the name, but tries to fix some of the frustrations found
with watchdog.}


%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.6
Release:        1%{?dist}
Summary:        Simple, modern file watching and code reload
License:        MIT
URL:            https://github.com/samuelcolvin/watchgod
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist pytest pytest-mock pytest-toolbox}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%pytest -v
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{_bindir}/watchgod
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jun 05 2020 Carl George <carl@george.computer> - 0.6-1
- Initial package
