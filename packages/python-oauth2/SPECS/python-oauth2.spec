%global reltag post1
%global with_py2 1

Name:			python-oauth2
Summary:		Python support for improved oauth
Version:		1.9.0
Release:		18.%{reltag}%{?dist}
License:		MIT
Source0:		http://pypi.python.org/packages/source/o/oauth2/oauth2-%{version}.%{reltag}.tar.gz
# https://github.com/pmakowski/python-oauth2/commit/7002422bb39bc137713933bc2e55251853830fcc
Patch1:			python-oauth2-1.9.0-CVE-2013-4346.patch
URL:			http://pypi.python.org/pypi/oauth2/
BuildArch:		noarch
%if 0%{?with_py2}
BuildRequires:		python2-devel, python2-setuptools
%endif
BuildRequires:		python3-devel
# These are the test requires, but since we don't run the tests, we disable them here.
# BuildRequires:	python2-mock, python2-httplib2, python2-coverage
%if 0%{?with_py2}
Requires:		python2-httplib2
%endif

%description
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.

%if 0%{?with_py2}
%package -n python2-oauth2
Summary:        Python support for improved oauth
%{?python_provide:%python_provide python2-oauth2}

%description -n python2-oauth2
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.
%endif

%package -n python3-oauth2
Summary:        Python support for improved oauth
%{?python_provide:%python_provide python3-oauth2}

%description -n python3-oauth2
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.

%prep
%setup -q -n oauth2-%{version}.%{reltag}
%patch1 -p1 -b .CVE-2013-4346

%build
%if 0%{?with_py2}
%py2_build
%endif
%py3_build

%install
%if 0%{?with_py2}
%py2_install
%endif
%py3_install

# Do not package the "tests"
%if 0%{?with_py2}
rm -rf %{buildroot}%{python2_sitelib}/tests/
%endif
rm -rf %{buildroot}%{python3_sitelib}/tests/

%check
# Tests try to access the network, which doesn't work in koji.
# export PYTHONPATH=$RPM_BUILD_ROOT/%%{python_sitelib}
# %{__python} setup.py test

%if 0%{?with_py2}
%files -n python2-oauth2
%doc PKG-INFO
%{python2_sitelib}/*
%endif

%files -n python3-oauth2
%doc PKG-INFO
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-18.post1
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 1.9.0-17.post1
- conditionalize python2 support (so we can shut it off easily when trac is modernized)
- remove unnecessary (and dead) dependency on python2-simplejson

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-16.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-15.post1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-14.post1
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-13.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-12.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.9.0-11.post1
- Remove tests from python3 sitelib root

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-9.post1
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.0-7.post1
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-4.post1
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3.post1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Tom Callaway <spot@fedoraproject.org> - 1.9.0-1.post1
- update to 1.9.0.post1
- split into py2/py3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.211-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct  8 2014 Tom Callaway <spot@fedoraproject.org> - 1.5.211-8
- actually apply patch to fix CVE-2013-4347 (thanks to Jason Green, Matt Wilson)

* Fri Sep 12 2014 Tom Callaway <spot@fedoraproject.org> - 1.5.211-7
- Fix CVE-2013-4346 and CVE-2013-4347 (thanks to Philippe Makowski)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.211-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.211-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.211-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.211-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Tom Callaway <spot@fedoraproject.org> - 1.5.211-2
- do not package the "tests", resolves conflicts (bz797812)

* Thu Feb 16 2012 Tom Callaway <spot@fedoraproject.org> - 1.5.211-1
- update to 1.5.211
- add multiple GET fix from Jason Connor (bz 784426)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.170-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep  7 2011 Tom Callaway <spot@fedoraproject.org> - 1.5.170-2
- add Requires: python-httplib2 (bz736133)

* Mon Jul 18 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.170-1
- New upstream release
- Match current guidelines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.1-1
- Initial package for Fedora
