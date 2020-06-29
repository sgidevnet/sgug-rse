%global modname chai

Name:               python-%{modname}
Version:            1.1.2
Release:            17%{?dist}
Summary:            Easy to use mocking/stub/spy framework

License:            BSD
URL:                http://pypi.python.org/pypi/chai
Source0:            http://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

%description
Chai provides a very easy to use api for mocking/stubbing your python
objects, patterned after the `Mocha <http://mocha.rubyforge.org/>`_ library
for Ruby.

%package -n         python%{python3_pkgversion}-%{modname}
Summary:            Easy to use mocking/stub framework
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-nose

%description -n python%{python3_pkgversion}-%{modname}
Chai provides a very easy to use api for mocking/stubbing your python
objects, patterned after the `Mocha <http://mocha.rubyforge.org/>`_ library
for Ruby.

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

# Remove py2-only files.  They make our tests fail on py3.
rm chai/python2.py

# Remove py2-only file for the py3 tests.
rm tests/comparator_py2.py

%build
%{py3_build}

%install
%{py3_install}

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-15
- Subpackage python2-chai has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-10
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Kevin Fenzi <kevin@scrye.com> - 1.1.2-6
- Update to 1.1.2. Fixes bug #1463021

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuild for Python 3.6

* Wed Jul 27 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-4
- Explicit python2 subpackage.

* Wed Jul 27 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-3
- Get python34 working for EPEL7.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- new version

* Wed Oct 15 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0.0
- Update to 1.0.0

* Wed Jul 09 2014 Ralph Bean <rbean@redhat.com> - 0.4.8-2
- Modernize with_python3 macro definition.

* Wed Jul 02 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.8-1
- Update to 0.4.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Jan 08 2014 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.7-1
- Update to 0.4.7

* Wed Dec 04 2013 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.6-1
- Update to 0.4.6

* Sun Nov 03 2013 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.5-1
- Update to 0.4.5
- Upstream ships LICENSE file
- Re-activate the tests

* Tue Oct 29 2013 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.4-1
- initial package for Fedora
