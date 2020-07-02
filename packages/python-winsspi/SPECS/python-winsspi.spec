%global pypi_name winsspi

Name:           python-%{pypi_name}
Version:        0.0.9
Release:        2%{?dist}
Summary:        Windows SSPI library in Python

License:        MIT
URL:            https://github.com/skelsec/winsspi
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Windows SSPI wrapper in pure Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Windows SSPI wrapper in pure Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' winsspi/common/defines.py
sed -i "s|\r||g" README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.9-2
- Rebuilt for Python 3.9

* Wed Apr 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.9-1
- Update to latest upstream release 0.0.9 (rhbz#1821092)

* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.8-1
- Update to latest upstream release 0.0.8 (rhbz#1821092)

* Mon Mar 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Use LICENSE file shipped in source tarball
- Update to latest upstream release 0.0.7 (rhbz#1814977)

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- Update to latest upstream release 0.0.5 (rhbz#1814977)

* Tue Jan 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-2
- Fix ownership

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-1
- Initial package for Fedora
