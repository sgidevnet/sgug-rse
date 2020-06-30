%global pypi_name webthing-ws

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        4%{?dist}
Summary:        WebThing WebSocket consumer and API client

License:        MIT
URL:            https://github.com/fabaff/webthing-ws
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A WebThing WebSocket consumer and API client.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A WebThing WebSocket consumer and API client.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst example.py
%license LICENSE
%{python3_sitelib}/webthing_ws/
%{python3_sitelib}/webthing_ws*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Initial package for Fedora
