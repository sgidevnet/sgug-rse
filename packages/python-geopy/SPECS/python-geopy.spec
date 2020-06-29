%global pypi_name geopy

Name:           python-%{pypi_name}
Version:        1.21.0
Release:        2%{?dist}
Summary:        Python client for several popular geocoding web services

License:        MIT
URL:            https://geopy.readthedocs.io
Source0:        https://github.com/geopy/geopy/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using third-
party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, Google
Geocoding API (V3), and many other geocoding services.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-GeographicLib
BuildRequires:  python3-pytz
BuildRequires:  python3-mock
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using third-
party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, Google
Geocoding API (V3), and many other geocoding services.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}/%{python3_sitelib}/ pytest-%{python3_version} -v test -k "not proxy and not yandex and not what3words and not banfrance and not arcgist and not databc and not geocodefarm and not geonames and not nominatim and not photon and not arcgis"

%files -n python3-%{pypi_name}
%doc AUTHORS CONTRIBUTING.md README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.21.0-2
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.0-1
- Update to latest upstream release 1.21.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.20.0-2
- Address issues (rhbz#1723052)

* Thu Jun 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.20.0-1
- Initial package for Fedora
