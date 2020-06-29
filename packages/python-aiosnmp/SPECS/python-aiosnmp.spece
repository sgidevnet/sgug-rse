%global pypi_name aiosnmp

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        4%{?dist}
Summary:        Asyncio Python SNMP client

License:        MIT
URL:            https://github.com/hh-h/aiosnmp
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/hh-h/aiosnmp/master/LICENSE
BuildArch:      noarch

%description
aiosnmp is an asynchronous SNMP client for use with asyncio.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiosnmp is an asynchronous SNMP client for use with asyncio.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-2
- Add LICENSE file (rhbz#1790082)

* Wed Jan 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Initial package for Fedora
