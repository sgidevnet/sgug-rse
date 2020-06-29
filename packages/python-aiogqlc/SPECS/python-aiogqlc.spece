%global pypi_name aiogqlc

Name:           python-%{pypi_name}
Version:        1.0.4
Release:        1%{?dist}
Summary:        GraphQL client with file upload support

License:        MIT
URL:            https://github.com/DoctorJohn/aiogqlc
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python asynchronous/IO GraphQL client based on aiohttp that supports the
GraphQL multipart form requests spec for file uploads.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-aiohttp
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python asynchronous/IO GraphQL client based on aiohttp that supports the
GraphQL multipart form requests spec for file uploads.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat May 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.4-1
- Update to latest upstream release 1.0.4

* Thu May 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.3-1
- Initial package for Fedora
