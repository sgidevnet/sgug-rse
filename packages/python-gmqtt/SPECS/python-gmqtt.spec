%global pypi_name gmqtt
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.6.5
Release:        1%{?dist}
Summary:        Client for the MQTT protocol

License:        MIT
URL:            https://github.com/wialon/gmqtt
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Asynchronous Python MQTT client implementation.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with network}
BuildRequires:  python3-pytest
%endif

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Asynchronous Python MQTT client implementation.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/examples

# Requires access to a third-party MQTT Broker
%if %{with network}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md examples
%{python3_sitelib}/%{pypi_name}/
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.5-1
- Update to latest upstream release 0.6.5

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-2
- Rebuilt for Python 3.9

* Sat Mar 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.3-1
- Update to latest upstream release 0.6.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.4-1
- Update to latest upstream release 0.5.4

* Mon Dec 30 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.3-1
- Initial package for Fedora

