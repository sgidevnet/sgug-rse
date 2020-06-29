# what it's called on pypi
%global srcname daphne
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP,
developed to power Django Channels.  It supports automatic negotiation of
protocols; there’s no need for URL prefixing to determine WebSocket endpoints
versus HTTP endpoints.}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD
URL:            https://github.com/django/daphne
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools pytest-runner}
%if %{with tests}
BuildRequires:  %{py3_dist pytest pytest-asyncio hypothesis}
BuildRequires:  %{py3_dist twisted autobahn asgiref}
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
%pytest --verbose
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{_bindir}/daphne
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/twisted/plugins/*


%changelog
* Fri Jun 05 2020 Carl George <carl@george.computer> - 2.5.0-1
- Initial package
