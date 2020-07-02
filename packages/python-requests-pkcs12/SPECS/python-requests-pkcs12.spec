%global pypi_name requests-pkcs12

Name:           python-%{pypi_name}
Version:        1.7
Release:        2%{?dist}
Summary:        Add PKCS12 support to the requests library

License:        ISC
URL:            https://github.com/m-click/requests_pkcs12
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library adds PKCS12 support to the Python requests library. It is
integrated into requests as recommended by its authors: creating a custom
TransportAdapter, which provides a custom SSLContext.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library adds PKCS12 support to the Python requests library. It is
integrated into requests as recommended by its authors: creating a custom
TransportAdapter, which provides a custom SSLContext.

%prep
%autosetup -n requests_pkcs12-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/requests_pkcs12.py
%{python3_sitelib}/requests_pkcs12-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-1
- Initial package for Fedora
