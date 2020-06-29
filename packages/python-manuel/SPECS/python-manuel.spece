%global srcname manuel

Name:           python-%{srcname}
Version:        1.10.1
Release:        9%{?dist}
Summary:        Build tested documentation

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/manuel
Source0:        https://github.com/benji-york/manuel/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(zope.testing)

%description
Manuel lets you mix and match traditional doctests with custom test
syntax.  Several plug-ins are included that provide new test syntax.
You can also create your own plug-ins.

%package -n python3-%{srcname}
Summary:        Build tested documentation
Provides:       bundled(jquery)

# This can be removed when Fedora 30 reaches EOL
Obsoletes:      python2-%{srcname} < 1.10.1-6
Provides:       python2-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}
Manuel lets you mix and match traditional doctests with custom test
syntax.  Several plug-ins are included that provide new test syntax.
You can also create your own plug-ins.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
sphinx-build -c sphinx src/manuel docs
rm -fr docs/.buildinfo docs/.doctrees

rst2html --no-datestamp CHANGES.rst CHANGES.html

# The copyright and license files are really just plain text
cp -p COPYRIGHT.rst COPYRIGHT
cp -p LICENSE.rst LICENSE

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc CHANGES.html docs/*
%license COPYRIGHT LICENSE
%{python3_sitelib}/manuel/
%{python3_sitelib}/manuel-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Jerry James <loganjerry@gmail.com> - 1.10.1-7
- Use zope.testing instead of zope.testrunner

* Mon Sep 16 2019 Jerry James <loganjerry@gmail.com> - 1.10.1-6
- Drop the python2 subpackage (bz 1752149)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 1.10.1-2
- Restore accidentally dropped python3 subpackage

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 1.10.1-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-4
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jerry James <loganjerry@gmail.com> - 1.9.0-1
- New upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 1.8.0-4
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 1.8.0-2
- Note bundled jquery

* Wed Jul 23 2014 Jerry James <loganjerry@gmail.com> - 1.8.0-1
- New upstream release
- Drop upstreamed patch
- Drop conf.py, now included in upstream source
- Avoid use of py3dir, which is not cleaned

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Jan 24 2014 Ralph Bean <rbean@redhat.com> - 1.7.2-4
- Conditionalized python3 for epel builds.
- Defined python2 macros for el6.
- Added python3 tests to the check section.

* Thu Oct  3 2013 Jerry James <loganjerry@gmail.com> - 1.7.2-3
- Update project and source URLs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Jerry James <loganjerry@gmail.com> - 1.7.2-1
- New upstream release

* Wed Feb 27 2013 Jerry James <loganjerry@gmail.com> - 1.7.1-2
- Add python-six Requires (bz 915431)

* Tue Feb 19 2013 Jerry James <loganjerry@gmail.com> - 1.7.1-1
- New upstream release

* Mon Jan 28 2013 Jerry James <loganjerry@gmail.com> - 1.6.1-1
- New upstream release

* Fri Aug 10 2012 Jerry James <loganjerry@gmail.com> - 1.6.0-3
- Rebuild for python 3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Jerry James <loganjerry@gmail.com> - 1.6.0-1
- New upstream release
- Python3 subpackage now possible

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 1.5.0-4
- Rebuild for bz 772699

* Sun Jan  8 2012 Jerry James <loganjerry@gmail.com> - 1.5.0-3
- Mass rebuild for Fedora 17

* Wed Apr 27 2011 Jerry James <loganjerry@gmail.com> - 1.5.0-2
- Do not Require python-zope-testing
- Change Group to Development/Libraries
- Remove text files from python_sitelib; they are already in docs

* Tue Apr 26 2011 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Initial RPM
