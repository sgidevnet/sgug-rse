%global pypi_name peewee

Name:		python-%{pypi_name}
Version:	3.13.3
Release:	2%{?dist}
Summary:	A small, expressive orm

License:	MIT
URL:		http://github.com/coleifer/peewee/
Source0:	https://github.com/coleifer/%{pypi_name}/archive/%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
BuildRequires:	gcc

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-Cython
BuildRequires:	sqlite-devel
BuildRequires:	sqlcipher-devel
BuildRequires:	python3-psycopg2
#Required for documentation build
BuildRequires:	python3-sphinx

# Required for running tests
BuildRequires:	python3-apsw
BuildRequires:	python3-flask

%description
A small, expressive ORM written in python with built-in support for sqlite,
mysql and postgresql and special extensions like hstore. For flask
integration, including an admin interface and RESTful API, check out
flask-peewee.

%package -n python3-%{pypi_name}

Summary:	A small, expressive orm
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A small, expressive ORM written in python with built-in support for sqlite,
mysql and postgresql and special extensions like hstore. For flask
integration, including an admin interface and RESTful API, check out
flask-peewee.

%prep
%setup -q -n %{pypi_name}-%{version}
#Point pwiz.py and pskel to Python 3
sed -i '1s=^#!/usr/bin/\(python\|env python.*\)$=#!%{__python3}=' pwiz.py
#Remove executable bits
chmod -x runtests.py examples/diary.py examples/analytics/run_example.py examples/twitter/run_example.py
#Remove shebangs from files that point to usr/bin/python
sed -i '1d' runtests.py
sed -i '1d' examples/diary.py
sed -i '1d' examples/analytics/run_example.py
sed -i '1d' examples/twitter/run_example.py

%build
%py3_build

#Build the documentation
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
rm %{buildroot}%{python3_sitearch}/pwiz.*
rm %{buildroot}%{python3_sitearch}/__pycache__/pwiz.*
mv %{buildroot}%{_bindir}/{pwiz.py,pwiz}

%ifnarch ppc64 ppc64le
# Tests for PPC architecture nondeterministically fail for concurrent writes.
# FAIL: test_multiple_writers (playhouse.tests.test_database.TestMultiThreadedQueries)
# OperationalError: database is locked
# https://bugzilla.redhat.com/show_bug.cgi?id=1606807
%check
%{__python3} runtests.py -e sqlite
%endif
# end ifnarch

%files -n python3-%{pypi_name}
%doc README.rst html
%license LICENSE
%{python3_sitearch}/peewee.py*
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitearch}/playhouse/
%{python3_sitearch}/__pycache__/*
%{_bindir}/pwiz

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.13.3-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Viliam Krizan <vkrizan@redhat.com> - 3.13.3-1
- Update to 3.13.2 (#1827517)

* Fri Apr 03 2020 Viliam Krizan <vkrizan@redhat.com> - 3.13.2-1
- Update to 3.13.2 (#1818146)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Viliam Krizan <vkrizan@redhat.com> - 3.13.1-1
- Update to 3.13.1 (#1776044)

* Fri Sep 27 2019 Viliam Krizan <vkrizan@redhat.com> - 3.11.2-1
- Update to 3.11.2 (#1742474)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.9.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Viliam Krizan <vkrizan@redhat.com> - 3.9.6-1
- Update to 3.9.6 (#1703665)

* Fri Apr 26 2019 Viliam Krizan <vkrizan@redhat.com> - 3.9.4-1
- Update to 3.9.4 (#1692015)

* Mon Mar 11 2019 Viliam Krizan <vkrizan@redhat.com> - 3.9.2-1
- Update to 3.9.2 (#1685885)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Viliam Krizan <vkrizan@redhat.com> - 3.7.1-1
- Update to 3.7.1 (#1539964)

* Fri Oct 05 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-8
- Removal of python2 subpackage as part of
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
  (RHBZ #1634869)

* Mon Jul 30 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-7
- skip check for PPC architecture (#1606807)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-5
- fix StopIteration raises for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.10.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 2.10.2-2
- Fix directory ownership

* Tue Jan 02 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-1
- Update to 2.10.2

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.10.1-4
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1 (#1448980)

* Mon Apr 10 2017 Viliam Krizan <vkrizan@redhat.com> - 2.9.2-1
- Update to 2.9.2

* Fri Mar 03 2017 Viliam Krizan <vkrizan@redhat.com> - 2.8.8-1
- Update to 2.8.8

* Tue Feb 07 2017 Viliam Krizan <vkrizan@redhat.com> - 2.8.5-2
- Backport upstream fix to force limit and offset to be numeric

* Mon Jan 09 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.8.5-1
- Update to 2.8.5

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.8.2-4
- Rebuild for Python 3.6

* Thu Nov 10 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-3
- Make pskel script install under usr/bin/
- Remove bytecompiled pwiz files

* Fri Nov 04 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-2
- Change runtime requirement from python2-simplejson to python-simplejson

* Wed Nov 02 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-1
- Update to 2.8.2
- Changed the installation directories to be arch dependent as the package
is now compiled using Cython

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-5
- Fix shebangs so python 2 is not dragged with the python 3 subpackage
- Build documentation

* Thu Jun 02 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-4
- Provide Python 3 subpackage
- Move binaries to Python 3 subpackage
- Modernize SPEC

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 29 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Wed Aug 27 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Mon Jun 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.2.4-1
- Update to 2.2.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.1.7-1
- Update to 2.1.7

* Tue Aug 13 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.1.4-2
- Added patch increasing timeout in concurrency test

* Wed Aug 07 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.1.4-1
- Updated to 2.1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.0.9-2
- Review fixes

* Fri Mar 29 2013 mstuchli <mstuchli@redhat.com> - 2.0.9-1
- Initial spec
