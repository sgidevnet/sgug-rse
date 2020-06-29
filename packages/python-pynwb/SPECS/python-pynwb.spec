# Enabled by default
%bcond_with tests

%global pypi_name pynwb

%global desc %{expand:
PyNWB is a Python package for working with NWB files. It provides a high-level
API for efficiently working with Neurodata stored in the NWB format.
https://pynwb.readthedocs.io/en/latest/}

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        2%{?dist}
Summary:        PyNWB is a Python package for working with NWB files
License:        BSD
URL:            https://github.com/NeurodataWithoutBorders/pynwb
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %{desc}

%{?python_provide:%python_provide python2-%{pypi_name}}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-certifi
BuildRequires:  python3-chardet
BuildRequires:  python3-h5py
BuildRequires:  python3-idna
BuildRequires:  python3-numpy
BuildRequires:  python3-dateutil
BuildRequires:  python3-requests
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-six
BuildRequires:  python3-urllib3
BUildRequires:  python3-pandas
BuildRequires:  python3-hdmf

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Multiple tests fail on this one file:
# An issue should be filed upstream
# get_build_manager should be get_manager
# forms should be pynwb.forms
# .. ?
rm -f tests/build_fake_data.py
rm -f tests/unit/__init__.py

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license license.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.9

* Sun Feb 16 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.1-1
- Update to new release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.2-2
- Remove dependency on unittest2 (#1789200)

* Fri Oct 25 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.2-1
- Update to 1.1.2

* Tue Sep 24 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.1.0-2
- disable test

* Mon Sep 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.1.0-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.3-1
- New upstream version

* Mon Apr 22 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.2-1
- New upstream version

* Mon Apr 15 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.1-2
- remove py2

* Mon Apr 15 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.1-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.6.1-3
- Add buildrequires
- Enable tests (thanks Ankur)

* Mon Nov 26 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.6.1-2
- Fix comment 2 in BZ 1651365

* Mon Nov 26 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.6.1-1
- New upstream
