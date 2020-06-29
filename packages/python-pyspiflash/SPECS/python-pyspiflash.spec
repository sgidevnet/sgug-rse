%global pypi_name pyspiflash

Name:           python-%{pypi_name}
Version:        0.6.3
Release:        2%{?dist}
Summary:        Python SPI data flash device drivers

License:        MIT
URL:            https://github.com/eblot/pyspiflash
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
SPI flash devices, also known as DataFlash are commonly found in embedded
products, to store firmware, microcode or configuration parameters.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#BuildRequires:  python3-pyftdi
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
SPI flash devices, also known as DataFlash are commonly found in embedded
products, to store firmware, microcode or configuration parameters.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# Not running tests as they try to create a device
#%check
#PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} i2cflash/tests/serialeeprom.py

%files -n python3-%{pypi_name}
%doc README.rst spiflash/AUTHORS
%license LICENSE
%{python3_sitelib}/spiflash/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.3-1
- Update to latest upstream release 0.2.2 (rhbz#1833300)

* Fri Apr 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Update to latest upstream release 0.6.2 (rhbz#1822562)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Update to latest upstream release 0.6.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Initial package for Fedora
