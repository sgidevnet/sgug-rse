%global pkgname linecache2

# For bootstrapping Python
%bcond_without tests

Name:           python-%{pkgname}
Version:        1.0.0
Release:        27%{?dist}
Summary:        Backport of the linecache module

License:        Python
URL:            https://github.com/testing-cabal/linecache2
Source0:        http://pypi.python.org/packages/source/l/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# Test dependencies
%if %{with tests}
BuildRequires:  python3-fixtures
%endif

%global _description\
A backport of linecache to older supported Pythons.\


%description %_description

%package     -n python3-%{pkgname}
Summary:        Backport of the linecache module

%description -n python3-%{pkgname}
A backport of linecache to older supported Pythons.



%prep
%setup -qn %{pkgname}-%{version}
# tests shouldn't be installed
mv %{pkgname}/tests .

# use the standard library unittest module
sed -i 's/import unittest2 as unittest/import unittest/' tests/*.py

%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
mv tests %{pkgname}/
%{__python3} -m unittest -v
mv %{pkgname}/tests .
%endif


%files -n python3-%{pkgname}
%doc AUTHORS ChangeLog README.rst
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-27
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-25
- Remove dependency on unittest2 (#1789200)

* Mon Oct 07 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-24
- Subpackage python2-linecache2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Sep 26 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-23
- Reduce the build dependencies by not running tests on Python 2

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-22
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-21
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-16
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-15
- Bootstrap for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.0.0-12
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-11
- Python 2 binary package renamed to python2-linecache2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.0.0-8
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.0.0-7
- Rebuild for Python 3.6
- Disable python3 tests

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Toshio Kuratomi <toshio@fedoraproject.org> - - 1.0.0-4
- And re-enable the tests

* Sat Nov 14 2015 Toshio Kuratomi <toshio@fedoraproject.org> - - 1.0.0-3
- Temproarily disable tests to bootstrap testtools

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jul 22 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.0-1
- Initial package
