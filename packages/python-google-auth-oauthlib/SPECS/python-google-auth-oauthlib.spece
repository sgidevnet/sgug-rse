%global pypi_name google-auth-oauthlib

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Google oAuth Authentication Library

License:        ASL 2.0
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-click
BuildRequires:  python3-google-auth
BuildRequires:  python3-requests-oauthlib
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-mock

%description
This library provides oauthlib integration with google-auth.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides oauthlib integration with google-auth.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
pYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/google-oauthlib-tool
%{python3_sitelib}/google_auth_oauthlib/
%{python3_sitelib}/google_auth_oauthlib-%{version}-py%{python3_version}.egg-info

%changelog
* Sun May 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora
