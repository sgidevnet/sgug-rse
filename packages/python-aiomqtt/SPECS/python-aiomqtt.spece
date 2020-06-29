%global pypi_name aiomqtt

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        4%{?dist}
Summary:        AsyncIO asynchronous wrapper around paho-mqtt

License:        EPL-1.0
URL:            https://github.com/mossblaser/aiomqtt
Source0:        https://github.com/mossblaser/aiomqtt/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  mosquitto

%description
This library implements a minimal Python 3 asyncio wrapper around the MQTT
client in paho-mqtt.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-paho-mqtt
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-mock
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library implements a minimal Python 3 asyncio wrapper around the MQTT
client in paho-mqtt.

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-2
- Better use of wildcards (rhbz#1786958)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
