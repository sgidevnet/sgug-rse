%global pypi_name play-scraper

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        5%{?dist}
Summary:        Scrapes and parses application data from Google Play Store

License:        MIT
URL:            https://github.com/danieliu/play-scraper
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Scrapes and parses application data from Google Play Store.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Scrapes and parses application data from Google Play Store.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# https://github.com/danieliu/play-scraper/issues/64
#%check
#%{__python3} setup.py test

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{python3_sitelib}/play_scraper/
%{python3_sitelib}/play_scraper-%{version}-py*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-5
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-2
- Disable tests till upstream fix is available
- Better use of wildcards (rhbz#1786656)

* Sat Dec 14 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Initial package for Fedora
