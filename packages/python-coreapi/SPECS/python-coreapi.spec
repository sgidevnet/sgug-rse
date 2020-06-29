%global srcname coreapi

Name:           python-%{srcname}
Version:        2.3.3
Release:        2%{?dist}
Summary:        Python client library for Core API

License:        BSD
URL:            https://github.com/core-api/python-client
Source0:        %{pypi_source}
Source1:        %{url}/raw/master/LICENSE.md

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info
cp -a %{S:1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.md
%{python3_sitelib}/coreapi/
%{python3_sitelib}/coreapi-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.3-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.3-1
- Initial package
