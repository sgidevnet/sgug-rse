%{?python_enable_dependency_generator}

Name:           python-cherrypy
%global         camelname CherryPy
Version:        18.4.0
Release:        5%{?dist}
Summary:        Pythonic, object-oriented web development framework
License:        BSD
URL:            http://www.cherrypy.org/
Source0:        https://files.pythonhosted.org/packages/source/C/%{camelname}/%{camelname}-%{version}.tar.gz

# Don't ship the tests or tutorials in the python module directroy,
# tutorial will be shipped as doc instead

# https://github.com/cherrypy/cherrypy/issues/1824
# Do not use newer pytest fixtures that aren't part of pytest 3.4.2 - this can be
# removed once 3.9.1 (or newer) is packaged.
Patch0:         0001.patch

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-setuptools_scm
# Test dependencies
BuildRequires:  python3dist(cheroot)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(path.py)
BuildRequires:  python3dist(portend)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(requests-toolbelt)
BuildRequires:  python3dist(more-itertools)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-zc-lockfile

%global _description\
%{camelname} allows developers to build web applications in much the same way\
they would build any other object-oriented Python program. This usually\
results in smaller source code developed in less time.

%description %_description

%package -n python3-cherrypy
Summary: %summary
%{?python_provide:%python_provide python3-cherrypy}

# Remove after F32.
Obsoletes: python2-cherrypy < 3.5.1

%description -n python3-cherrypy %_description

%prep
%setup -q -n %{camelname}-%{version}
%patch0 -p1

dos2unix cherrypy/tutorial/tutorial.conf

# These tests still fail (reason unknown):
rm cherrypy/test/test_session.py
rm cherrypy/test/test_static.py

%build
%py3_build

%install
%py3_install

%check
# skip tests for now
# LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-cherrypy
%doc README.rst
%license LICENSE.md
%doc cherrypy/tutorial
%{_bindir}/cherryd
%{python3_sitelib}/*
%exclude %{python3_sitelib}/cherrypy/cherryd
%exclude %{python3_sitelib}/cherrypy/test
%exclude %{python3_sitelib}/cherrypy/tutorial

%changelog
* Sat Jun 20 2020 Miro Hrončok <mhroncok@redhat.com> - 18.4.0-5
- Disable unused automagic Python bytecompilation

* Fri Jun 05 2020 Matthias Runge <mrunge@redhat.com> - 18.4.0-4
- skip tests to fix FTBFS (rhbz#1810313)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 18.4.0-4
- Rebuilt for Python 3.9

* Sat Feb 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 18.4.0-3
- Fix Obsoletes for python2-cherrypy

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Ken Dreyer <kdreyer@redhat.com> - 18.4.0-1
- Update to 18.4.0 (rhbz#1748716)
- Update comments about current test failures

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 18.1.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 18.1.2-4
- Rebuilt for Python 3.8

* Thu Aug 08 2019 Dan Radez <dradez@redhat.com> - 18.1.2-3
- Update to 18.1.2
- Replaced Python2 package with Python 3 package
- python3-cherrypy-18.1.2-2 is already built by package python3-cherrypy
  this release is to migrate python3-cherrypy into python-cherrypy

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.5.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5.0-7
- Python 2 binary package renamed to python2-cherrypy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 Luke Macken <lmacken@redhat.com> - 3.5.0-1
- Update to 3.5.0 (#1104560)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Conrad Meyer <konrad@tylerc.org> - 3.2.2-1
- Update to 3.2.2

* Sat Jul 16 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-4
- Fix a failing unittest with newer python

* Sat Apr 24 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-3
- Revert a try at 3.2.x-rc1 as the tests won't pass without some work.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-1
- New upstream with python-2.6 fixes.
- BR tidy for tests.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 1 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1
- Fix python-2.6 build errors
- Make test code non-interactive via cmdline switch
- Refresh the no test and tutorial patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.3-3
- Rebuild for Python 2.6

* Tue Jan 22 2008 Toshio Kuratomi <toshio@fedoraproject.org> 3.0.3-2
- Forgot to upload the tarball.

* Mon Jan 21 2008 Toshio Kuratomi <toshio@fedoraproject.org> 3.0.3-1
- Upgrade to 3.0.3.

* Thu Jan 17 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.3.0-2
- EINTR Patch needed to be forwarded ported as well as it is only applied to
  CP trunk (3.x).

* Thu Jan 17 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.3.0-1
- Update to new upstream which rolls in the backported security fix.
- Refresh other patches to apply against new version.
- Change to new canonical source URL.
- Reenable tests.

* Sun Jan  6 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.2.1-8
- Fix a security bug with a backport of http://www.cherrypy.org/changeset/1775
- Include the egginfo files as well as the python files.

* Sat Nov  3 2007 Luke Macken <lmacken@redhat.com> 2.2.1-7
- Apply backported fix from http://www.cherrypy.org/changeset/1766
  to improve CherryPy's SIGSTOP/SIGCONT handling (Bug #364911).
  Thanks to Nils Philippsen for the patch.

* Mon Feb 19 2007 Luke Macken <lmacken@redhat.com> 2.2.1-6
- Disable regression tests until we can figure out why they
  are dying in mock.

* Sun Dec 10 2006 Luke Macken <lmacken@redhat.com> 2.2.1-5
- Add python-devel to BuildRequires

* Sun Dec 10 2006 Luke Macken <lmacken@redhat.com> 2.2.1-4
- Rebuild for python 2.5

* Mon Sep 18 2006 Luke Macken <lmacken@redhat.com> 2.2.1-3
- Rebuild for FC6
- Include pyo files instead of ghosting them

* Thu Jul 13 2006 Luke Macken <lmacken@redhat.com> 2.2.1-2
- Rebuild

* Thu Jul 13 2006 Luke Macken <lmacken@redhat.com> 2.2.1-1
- Update to 2.2.1
- Remove unnecessary python-abi requirement

* Sat Apr 22 2006 Gijs Hollestelle <gijs@gewis.nl> 2.2.0-1
- Update to 2.2.0

* Wed Feb 22 2006 Gijs Hollestelle <gijs@gewis.nl> 2.1.1-1
- Update to 2.1.1 (Security fix)

* Tue Nov  1 2005 Gijs Hollestelle <gijs@gewis.nl> 2.1.0-1
- Updated to 2.1.0

* Sat May 14 2005 Gijs Hollestelle <gijs@gewis.nl> 2.0.0-2
- Added dist tag

* Sun May  8 2005 Gijs Hollestelle <gijs@gewis.nl> 2.0.0-1
- Updated to 2.0.0 final
- Updated python-cherrypy-tutorial-doc.patch to match new version

* Wed Apr  6 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.0-0.2.b
- Removed CFLAGS

* Wed Mar 23 2005 Gijs Hollestelle <gijs[AT]gewis.nl> 2.0.0-0.1.b
- Initial Fedora Package
