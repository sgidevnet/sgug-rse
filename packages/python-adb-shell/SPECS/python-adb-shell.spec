%global pypi_name adb-shell

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        2%{?dist}
Summary:        Python implementation for ADB shell and file sync

License:        ASL 2.0
URL:            https://github.com/JeffLIrion/adb_shell
Source0:        %{pypi_source adb_shell}
BuildArch:      noarch

%description
Python package implements ADB shell and FileSync functionality.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python package implements ADB shell and FileSync functionality.

%prep
%autosetup -n adb_shell-%{version}
rm -rf %{pypi_name}.egg-info
# Conflict with crypto
sed -i -e 's/pycryptodome/pycryptodomex/g' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
# License file missing: https://github.com/JeffLIrion/adb_shell/issues/84
%{python3_sitelib}/adb_shell/
%{python3_sitelib}/adb_shell-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-1
- Update to latest upstream release 0.1.4

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Initial package for Fedora
