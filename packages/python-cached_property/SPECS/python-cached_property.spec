# Disable Python 2 builds for Fedora > 29, EPEL > 7
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
%bcond_with         python2
%global obsolete2   1
%else
%bcond_without      python2
%global obsolete2   0
%endif

%global py2dir      %{_builddir}/python2-%{name}-%{version}-%{release}
%global projectname cached-property
%global modulename  cached_property

Name:           python-%{modulename}
Version:        1.5.1
Release:        8%{?dist}
Summary:        A cached-property for decorating methods in Python classes
License:        BSD
URL:            https://github.com/pydanny/%{projectname}
Source0:        https://github.com/pydanny/%{projectname}/archive/%{version}/%{projectname}-%{version}.tar.gz
# Disable a couple of test checks that fail with freezegun 0.3.11
# See https://github.com/pydanny/cached-property/issues/131
Patch0:         0001-Disable-checks-broken-with-freezegun-0.3.11-131.patch

BuildArch:      noarch

%description
cached_property allows properties in Python classes to be cached until the cache
is invalidated or expired.

%if 0%{?with_python2}
%package -n python2-%{modulename}
Summary:        A cached-property for decorating methods in Python classes.
BuildRequires:  python2-devel
BuildRequires:  python2-dateutil
BuildRequires:  python2-freezegun
BuildRequires:  python2-pytest
%{?python_provide:%python_provide python2-%{modulename}}
# I messed up at 1.3.0-1 and called this package python2-{projectname}
Provides:       python2-%{projectname} = %{version}-%{release}
Obsoletes:      python2-%{projectname} < 1.3.0-2

%description -n python2-%{modulename}
cached_property allows properties in Python classes to be cached until the cache
is invalidated or expired.
%endif # with_python2

%package -n python%{python3_pkgversion}-%{modulename}
Summary:        A cached-property for decorating methods in Python classes.
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modulename}}
# This package was python3-{projectname} for a long time, but never should've
# been
Provides:       python%{python3_pkgversion}-%{projectname} = %{version}-%{release}
Obsoletes:      python%{python3_pkgversion}-%{projectname} < 1.3.0-2
%if 0%{?obsolete2}
Obsoletes:      python2-%{modulename} < %{version}-%{release}
%endif # obsolete2

%description -n python%{python3_pkgversion}-%{modulename}
cached_property allows properties in Python classes to be cached until the cache
is invalidated or expired.

%prep
%autosetup -p1 -n %{projectname}-%{version}

%if 0%{?with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
%endif # with_python2

%build
%{__python3} setup.py build

%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif # with_python2

%check
PYTHONPATH=./ py.test-3
%if 0%{?with_python2}
%if 0%{?rhel} && 0%{?rhel} < 8
# py.test-2 isn't a thing on EL 7 apparently
PYTHONPATH=./ py.test
%else
PYTHONPATH=./ py.test-2
%endif # rhel < 8
%endif # with_python2

%if 0%{?with_python2}
%files -n python2-%{modulename}
%{!?_licensedir:%global license %%doc}
%doc AUTHORS.rst HISTORY.rst CONTRIBUTING.rst README.rst
%license LICENSE
%{python2_sitelib}/%{modulename}*
%endif # with_python2

%files -n python%{python3_pkgversion}-%{modulename}
%doc AUTHORS.rst HISTORY.rst CONTRIBUTING.rst README.rst
%license LICENSE
%{python3_sitelib}/%{modulename}*
%{python3_sitelib}/__pycache__/%{modulename}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Adam Williamson <awilliam@redhat.com> - 1.5.1-3
- Disable a couple of test checks that fail with freezegun 0.3.11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Adam Williamson <awilliam@redhat.com> - 1.5.1-1
- New release 1.5.1
- Disable Python 2 build on F30+, EL8+

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-1
- Update to 1.4.3 (used by pipenv)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-12
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.0-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 10 2017 Adam Williamson <awilliam@redhat.com> - 1.3.0-7
- Enable Python 3 build on EPEL 7

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 03 2016 Adam Williamson <awilliam@redhat.com> - 1.3.0-4
- disable tests on F22 (it doesn't know about py3.5)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Adam Williamson <awilliam@redhat.com> - 1.3.0-2
- try to repair the mess I made of package naming:
- # both subpackages now use module name not project name
- # try to ensure all previous names are provided/obsoleted

* Thu Nov 26 2015 Adam Williamson <awilliam@redhat.com> - 1.3.0-1
- new release 1.3.0, drop patch (merged upstream)
- switch to python2-foo / python3-foo package naming

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Adam Williamson <awilliam@redhat.com> - 1.2.0-1
- new upstream release 1.2.0 (refactoring, bug fixes)
- patch out non-ASCII characters in HISTORY.rst (breaks py3 build in koji)

* Thu Apr 16 2015 Adam Williamson <awilliam@redhat.com> - 1.1.0-1
- new upstream release 1.1.0 (insignificant changes)

* Wed Mar 25 2015 Adam Williamson <awilliam@redhat.com> - 1.0.0-4
- python3 build only for Fedora (no python3 in RHEL6 or 7)
- provide python2-cached_property
- guard against #license not being available
- only run tests on F>=22 (tox is too old on everything else)

* Fri Mar 13 2015 Pete Travis <me@petetravis.com> - 1.0.0-2
- Use the module name for the package name.

* Fri Feb 20 2015 Pete Travis <me@petetravis.com> 1.0.0-1
- Initial packaging. 
