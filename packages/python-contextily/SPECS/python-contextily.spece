%global srcname contextily

# Some tests require the network.
%bcond_with network

Name:           python-%{srcname}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Context geo-tiles in Python

License:        BSD
URL:            https://github.com/geopandas/contextily
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/geopandas/contextily/pull/124
Patch0001:      0001-Mark-tests-that-require-the-network.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(geopy)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(mercantile)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(rasterio)
BuildRequires:  python3dist(requests)

%description
contextily is a small Python 3 package to retrieve and write to disk tile maps
from the internet into geospatial raster files. Bounding boxes can be passed in
both WGS84 (EPSG:4326) and Spheric Mercator (EPSG:3857).


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
contextily is a small Python 3 package to retrieve and write to disk tile maps
from the internet into geospatial raster files. Bounding boxes can be passed in
both WGS84 (EPSG:4326) and Spheric Mercator (EPSG:3857).


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with network}
pytest-3
%else
pytest-3 -m 'not network'
%endif

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.9

* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0~rc2-1
- Update to latest release candidate

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.99.0-1
- Initial package.
