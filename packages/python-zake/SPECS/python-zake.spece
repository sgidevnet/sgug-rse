%{?python_enable_dependency_generator}
%global pypi_name zake

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        20%{?dist}
Summary:        Testing utilities for the kazoo library

License:        ASL 2.0
URL:            https://github.com/yahoo/Zake
Source0:        https://pypi.python.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/yahoo/Zake/master/LICENSE
BuildArch:      noarch

%description
It is a python package that works to provide a nice set of testing
utilities for the `kazoo`_ library.
It includes the following functionality:
* Storage access (for viewing what was saved/created).
* Kazoo *mostly* compatible client API.
* Sync/transaction/create/get/delete... ...

%package -n python3-%{pypi_name}
Summary:        Testing utilities for the kazoo library
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:       python3-devel
BuildRequires:       python3-kazoo
BuildRequires:       python3-six
BuildRequires:       python3-setuptools

%description -n python3-%{pypi_name}
It is a python package that works to provide a nice set of testing
utilities for the `kazoo`_ library.
It includes the following functionality:
* Storage access (for viewing what was saved/created).
* Kazoo *mostly* compatible client API.
* Sync/transaction/create/get/delete... ...

%prep
%autosetup -n %{pypi_name}-%{version}
cp -p %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-15
- Subpackage python2-zake has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-13
- Enable python dependency generator

* Mon Jan 21 2019 Javier Peña <jpena@redhat.com> - 0.2.2-12
- Fix python3-kazoo requirement for the python3 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 30 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.2-1
- Initial package.
