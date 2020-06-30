%global pypi_name pyi2cflash

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        2%{?dist}
Summary:        Python I2C eeprom device drivers

License:        MIT
URL:            https://github.com/eblot/pyi2cflash
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
I2C flash devices, also known as DataFlash are commonly found in embedded
products, to store firmware, microcode or configuration parameters.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#BuildRequires:  python3-pyftdi
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
I2C flash devices, also known as DataFlash are commonly found in embedded
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
%doc README.rst AUTHORS
%license LICENSE
%{python3_sitelib}/i2cflash/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to latest upstream release 0.2.2 (rhbz#1833299)
- Fix FTI (rhbz#1830681)

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Update to latest upstream release 0.2.1 (rhbz#1814986)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
