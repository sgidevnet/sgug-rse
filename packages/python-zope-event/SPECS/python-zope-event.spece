
Name:           python-zope-event
Version:        4.2.0
Release:        18%{?dist}
Summary:        Zope Event Publication
License:        ZPLv2.1
URL:            http://pypi.python.org/pypi/zope.event/
Source0:        http://pypi.python.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz
BuildArch:      noarch

%description
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

%package -n python3-zope-event
Summary:        Zope Event Publication (Python 3)
%{?python_provide:%python_provide python3-zope-event}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-sphinx

Requires:       python3

%description -n python3-zope-event
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

This package contains the version for Python 3.

%prep
%setup -q -n zope.event-%{version}
rm -rf %{modname}.egg-info

%build
%py3_build

# build the sphinx documents
pushd docs
PYTHONPATH=../src make SPHINXBUILD=sphinx-build-3 html
rm -f _build/html/.buildinfo
popd


%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-zope-event
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%doc docs/_build/html/
%license LICENSE.txt
%{python3_sitelib}/zope/event/
%exclude %{python3_sitelib}/zope/event/tests.py*
%exclude %{python3_sitelib}/zope/event/__pycache__/tests*
%dir %{python3_sitelib}/zope/
#%{python3_sitelib}/zope/__init__*
%{python3_sitelib}/zope.event-*.egg-info
%{python3_sitelib}/zope.event-*-nspkg.pth

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-16
- Subpackage python2-zope-event has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-10
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-9
- Build the docs with Python 3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 4.2.0-7
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 4.2.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.2.0-2
- Modernized python macros.
- Added an explicit python2 subpackage.

* Fri Feb 19 2016 Ralph Bean <rbean@redhat.com> - 4.2.0-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.5

* Mon Oct 19 2015 Ralph Bean <rbean@redhat.com> - 4.1.0-1
- new version

* Mon Oct 19 2015 Ralph Bean <rbean@redhat.com> - 4.0.3-4
- No longer own zope/__init__.py.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Ralph Bean <rbean@redhat.com> - 4.0.3-2
- Fix a python3 conditional block.

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 4.0.3-1
- Latest upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Ralph Bean <rbean@redhat.com> - 4.0.2-1
- Latest upstream.
- Conditionalized python3 subpackage for el6.

* Thu Oct 18 2012 Robin Lee <cheeselee@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2 (ZTK 1.1.5)

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 3.5.1-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep  1 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1 (#728489)
- Build subpackage for Python 3.
- Include the sphinx documents
- Exclude the module for tests.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 31 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.0.1-4
- Add a missed percent character

* Tue Aug 31 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.0.1-3
- Remove python-zope-filesystem from requirements
- Own %%{python_sitelib}/zope/
- Spec cleaned up

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 17 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.0.1-1
- Update to 3.5.0-1
- Include more documents

* Sun Jul 5 2009 Conrad Meyer <konrad@tylerc.org> - 3.4.1-1
- Add missing BR on python-setuptools.
- Enable testing stuff as zope-testing is in devel.

* Sun Dec 14 2008 Conrad Meyer <konrad@tylerc.org> - 3.4.0-1
- Initial package.
