%global pypi_name anymarkup-core
%global modulename anymarkup_core

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        2%{?dist}
Summary:        Core library for anymarkup

License:        BSD
URL:            https://github.com/bkabrda/anymarkup-core
Source0:        https://github.com/bkabrda/anymarkup-core/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is the core library that implements functionality of
python-anymarkup.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-configobj
BuildRequires:  python3-flexmock
BuildRequires:  python3-six
BuildRequires:  python3-xmltodict
BuildRequires:  python3-PyYAML
BuildRequires:  python3-toml
BuildRequires:  python3-json5
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is the core library that implements functionality of
python-anymarkup.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modulename}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modulename}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-1
- Update to latest upstream release 0.8.1 (rhbz#1805546, rhbz#1795949)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update spec file
- Update BR (rhbz#1721645, rhbz#1736473)
- Update to latest upstream release 0.8.0 (rhbz#1333990)
- Update source location

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-14
- Subpackage python2-anymarkup-core has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-8
- Python 2 binary package renamed to python2-anymarkup-core
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 jchaloup <jchaloup@redhat.com> - 0.5.0-1
  Initial package for Fedora
  resolves: #1273471
