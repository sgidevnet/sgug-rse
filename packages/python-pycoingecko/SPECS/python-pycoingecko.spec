%global pypi_name pycoingecko

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Python wrapper around the CoinGecko API

License:        MIT
URL:            https://github.com/man-c/pycoingecko
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python3 wrapper around the CoinGecko API (V3).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-responses
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python3 wrapper around the CoinGecko API (V3).

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.9

* Fri Mar 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Initial package for Fedora

