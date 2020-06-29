%global module pyasn1
%global modules_version 0.2.8

Name:           python-pyasn1
Version:        0.4.8
Release:        2%{?dist}
Summary:        ASN.1 tools for Python
License:        BSD
Source0:        https://github.com/etingof/pyasn1/archive/v%{version}.tar.gz
Source1:        https://github.com/etingof/pyasn1-modules/archive/v%{modules_version}.tar.gz
URL:            http://pyasn1.sourceforge.net/
BuildArch:      noarch

%description
This is an implementation of ASN.1 types and codecs in the Python programming
language.

%package -n python3-pyasn1
Summary:    ASN.1 tools for Python 3
%{?python_provide:%python_provide python3-pyasn1}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-pyasn1
This is an implementation of ASN.1 types and codecs in the Python 3 programming
language.

%package -n python3-pyasn1-modules
Summary:    Modules for pyasn1
Requires:   python3-pyasn1 >= %{version}-%{release}
%{?python_provide:%python_provide python3-modules}

%description -n python3-pyasn1-modules
ASN.1 types modules for python3-pyasn1.

%package doc
Summary:        Documentation for pyasn1
BuildRequires:  python3-sphinx

%description doc
%{summary}.


%prep
%setup -n %{module}-%{version} -q -b1


%build
%py3_build

pushd ../pyasn1-modules-%{modules_version}
%py3_build
popd

pushd docs
PYTHONPATH=%{buildroot}%{python3_sitelib} make SPHINXBUILD=sphinx-build-3 html
popd


%install
%py3_install

pushd ../pyasn1-modules-%{modules_version}
%py3_install
popd


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test


%files -n python3-pyasn1
%doc README.md
%license LICENSE.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}-*.egg-info/

%files -n python3-pyasn1-modules
%{python3_sitelib}/%{module}_modules/
%{python3_sitelib}/%{module}_modules-%{modules_version}-*.egg-info/

%files doc
%license LICENSE.rst
%doc docs/build/html/*

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.8-2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Rob Crittenden <rcritten@redhat.com> - 0.4.8-1
- Update to 0.4.8 (#1747820)
- Update modules to 0.2.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Rob Crittenden <rcritten@redhat.com> - 0.4.6-3
- Remove python2 subpackages (#1764573)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Rob Crittenden <rcritten@redhat.com> - 0.4.6-1
- Update to 0.4.6 (#1742424)
- Update modules to 0.2.6

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Rob Crittenden <rcritten@redhat.com> - 0.4.4-3
- Restore python2 subpackages

* Mon Oct 15 2018 Rob Crittenden <rcritten@redhat.com> - 0.4.4-2
- Add back accidentally removed buildrequires

* Mon Oct 15 2018 Rob Crittenden <rcritten@redhat.com> - 0.4.4-1
- Update to 0.4.4 (#1582010)
- Update modules to 0.2.2
- Drop python 2 subpackages

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.7-5
- Use Python 3 Sphinx if with Python 3
- Cleanup

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.7-4
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.7-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Christian Heimes <cheimes@redhat.com> - 0.3.7-1
- Update to upstream release 0.3.7 (#1492446)
- Update modules to 0.1.5

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.3.4-2
- Cleanup spec file conditionals

* Fri Sep 15 2017 Rob Crittenden <rcritten@redhat.com> - 0.3.4-1
- Update to upstream release 0.3.4 (#1485669)
- Update modules to 0.1.2
- Patch to fixed crash at SequenceOf native decoder

* Wed Aug 16 2017 Rob Crittenden <rcritten@redhat.com> - 0.3.2-1
- Update to upstream release 0.3.2 (#1475594)
- Update modules to 0.0.11

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Rob Crittenden <rcritten@redhat.com> - 0.2.3-1
- Update to upstream release 0.2.3 (#1426979)
- Adapt to the way upstream changed the way tests are executed
- Pass PYTHONPATH when building the documentation

* Mon Feb  6 2017 Rob Crittenden <rcritten@redhat.com> - 0.2.1-1
- Update to upstream release 0.2.1 (#1419310)
- Added doc subpackage and moved documentation there

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.1.9-8.1
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-7.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Rob Crittenden <rcritten@redhat.com> - 0.1.9-5.1
- Add in missing colon after Provides

* Mon Jan 11 2016 Rob Crittenden <rcritten@redhat.com> - 0.1.9-5
- If python_provide wasn't defined then the python2 subpackages
  didn't provide python-pyasn1-*

* Tue Jan  5 2016 Martin Kosek <mkosek@redhat.com> - 0.1.9-4
- Fix python2 provides for pyasn1 modules (#1295693)

* Mon Jan  4 2016 Rob Crittenden <rcritten@redhat.com> - 0.1.9-3
- Explicitly provide python2 subpackages, use python_provide macro

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 0.1.9-2
- Rebuilt for Python3.5 rebuild

* Mon Oct 19 2015 Rob Crittenden <rcritten@redhat.com> - 0.1.9-1
- Update to new upstream release 0.1.9, modules 0.0.8.

* Sat Aug 15 2015 Rob Crittenden <rcritten@redhat.com> - 0.1.8-2
- Move LICENSE to the license tag instead of doc.

* Wed Jul 15 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.1.8-1
- Update to new upstream release 0.1.8, modules 0.0.6.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Rob Crittenden <rcritten@redhat.com> - 0.1.7-1
- update to upstream release 0.1.7
- update modules to 0.0.5

* Sat Feb 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.6-1
- update to upstream release 0.1.6
- update modules to 0.0.4
- update description
- add python3-pyasn1 subpackage
- add versioned Requires for the module subpackages
- add %%check section

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 02 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1.2-1
- New upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Rob Crittenden <rcritten@redhat.com> - 0.0.12a-1
- Update to upstream version 0.0.12a

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.0.9a-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Nov 16 2009 Rob Crittenden <rcritten@redhat.com> - 0.0.9a-1
- Update to upstream version 0.0.9a
- Include patch that adds parsing for the Any type

* Wed Sep  2 2009 Rob Crittenden <rcritten@redhat.com> - 0.0.8a-5
- Include doc/notes.html in the package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.0.8a-2
- Rebuild for Python 2.6

* Tue Sep  9 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.8a-1
- Update to upstream version 0.0.8a

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 0.0.7a-4
- Use setuptools to install the package
- simplify the files included in the rpm so it includes the .egg-info

* Mon Jan 14 2008 Rob Crittenden <rcritten@redhat.com> - 0.0.7a-3
- Rename to python-pyasn1
- Spec file cleanups

* Mon Nov 19 2007 Karl MacMillan <kmacmill@redhat.com> - 0.0.7a-2
- Update rpm to be more fedora friendly

* Thu Nov 8 2007 Simo Sorce <ssorce@redhat.com> 0.0.7a-1
- New release

* Mon May 28 2007 Andreas Hasenack <andreas@mandriva.com> 0.0.6a-1mdv2008.0
+ Revision: 31989
- fixed (build)requires
- Import pyasn1

