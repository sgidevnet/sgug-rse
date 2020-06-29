Name:           python-shapely
Version:        1.7.0
Release:        4%{?dist}
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

License:        BSD
URL:            https://github.com/Toblerity/Shapely
Source0:        https://github.com/Toblerity/Shapely/archive/%{version}%{?prerel}.tar.gz
BuildRequires:  gcc
BuildRequires:  geos-devel

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-setuptools
# Tests
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-matplotlib


%global _description\
Shapely is a package for creation, manipulation, and analysis\
of planar geometry objects – designed especially for developers\
of cutting edge geographic information systems. In a nutshell:\
Shapely lets you do PostGIS-ish stuff outside the context of a\
database using idiomatic Python.\
\
You can use this package with python-matplotlib and numpy.\
See README.rst for more information!

%description %_description

%package -n python3-shapely
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane
%{?python_provide:%python_provide python3-shapely}

%description -n python3-shapely %_description


%prep
%autosetup -p1 -n Shapely-%{version}%{?prerel}

# Remove pre-generated sources
rm -f shapely/speedups/_speedups.c
rm -f shapely/vectorized/_vectorized.c


%build
%py3_build


%check
%{python3} setup.py test


%install
%py3_install

rm %{buildroot}%{python3_sitearch}/shapely/speedups/_speedups.c


%files -n python3-shapely
%doc CHANGES.txt README.rst CREDITS.txt LICENSE.txt
%doc docs
%doc %{python3_sitearch}/shapely/examples/
%exclude %{python3_sitearch}/shapely/examples/
%{python3_sitearch}/shapely/
%{python3_sitearch}/Shapely-%{version}%{?prerel}-py*.egg-info/

%changelog
* Wed Jun 17 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Update to 1.7.0 final (#1795751)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7-3b1
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Volker Fröhlich <volker27@gmx.at> - 1.7-1.b1

* Tue Jan 07 2020 Volker Fröhlich <volker27@gmx.at> - 1.7-1.a3
- New upstream release
- Don't run cython on our own
- Change source URL
- Remove generated C file unconditionally

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-9.post2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-8.post2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-7.post2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-6.post2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-5.post2
- Remove python2 subpackage

* Thu Aug 02 2018 Volker Fröhlich <volker27@gmx.at> - 1.6.4-4.post2
- New upstream release
- Add missing BR on gcc (Cython)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Volker Fröhlich <volker27@gmx.at> - 1.6.4-2.post1
- Merge Miro's pull request removing filter_provides and 
  correcting the python_provide macro; Also adding it to the Python 3
  sub-package

* Wed Jul 04 2018 Volker Fröhlich <volker27@gmx.at> - 1.6.4-1.post1
- New upstream release
- Use unambiguous python2 macros

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.16-13
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.16-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 2018 Lumír Balhar <lbalhar@redhat.com> - 1.5.16-11
- Fix directory ownership

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.16-9
- Python 2 binary package renamed to python2-shapely
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5.16-6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.16-4
- Rebuild for Python 3.6

* Sat Oct 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.16-3
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.16-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 28 2016 Volker Fröhlich <volker27@gmx.at> - 1.5.16-1
- New upstream release

* Tue Mar 29 2016 Volker Fröhlich <volker27@gmx.at> - 1.5.15-1
- New upstream release

* Wed Mar 02 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.13-1
- Update to 1.5.13 (#1181550)
- BR pytest and matplotlib for tests

* Wed Mar 02 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.13-1
- Update to 1.5.13 (#1181550)
- BR pytest and matplotlib for tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan  5 2015 Volker Fröhlich <volker27@gmx.at> - 1.5.2-1
- New upstream release

* Sat Dec  6 2014 Volker Fröhlich <volker27@gmx.at> - 1.5.1-1
- New upstream release

* Tue Nov  4 2014 Volker Fröhlich <volker27@gmx.at> - 1.4.4-1
- New upstream release

* Wed Oct  8 2014 Volker Fröhlich <volker27@gmx.at> - 1.4.3-1
- New upstream release

* Tue Sep 30 2014 Volker Fröhlich <volker27@gmx.at> - 1.4.2-1
- New upstream release

* Wed Sep 24 2014 Volker Fröhlich <volker27@gmx.at> - 1.4.1-1
- New upstream release

* Thu Sep 18 2014 Volker Fröhlich <volker27@gmx.at> - 1.4.0-1
- New upstream release
- Add BR on Cython/python3-cython and build the C extension
- Update URL
- Remove the obsolete encoding patch

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri May 23 2014 Volker Fröhlich <volker27@gmx.at> - 1.3.2-1
- New upstream release

* Thu Apr 24 2014 Volker Fröhlich <volker27@gmx.at> - 1.3.1-1
- New upstream release

* Sat Apr 19 2014 Volker Fröhlich <volker27@gmx.at> - 1.3.0-2
- Replace obsolete python-setuptools-devel with python-setuptools

* Wed Feb 12 2014 Volker Fröhlich <volker27@gmx.at> - 1.3.0-1
- New upstream release
- Use a better summary
- Add Python 3 builds
- Change BR python-devel to python2-devel

* Mon Sep 16 2013 Volker Fröhlich <volker27@gmx.at> - 1.2.18-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 27 2013 Volker Fröhlich <volker27@gmx.at> - 1.2.17-1
- New upstream release

* Tue Sep 18 2012 Volker Fröhlich <volker27@gmx.at> - 1.2.16-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Volker Fröhlich <volker27@gmx.at> - 1.2.15-1
- New upstream release
- Pyx file is no longer part of the sources, thus Cython is no longer BR
- Chaintest is working fine now, drop the patch

* Sun Apr  8 2012 Volker Fröhlich <volker27@gmx.at> - 1.2.14-1
- Update for release 1.2.14
- Remove duplicate PKG-INFO file
- Correct description -- pointing to README.rst now
- Add patch that corrects the attribute chaining test
- Tests now work fine, therefore respect their outcome
- Remove ready-made _speedups.c

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Volker Fröhlich <volker27@gmx.at> - 1.2.13-1
- Update for release 1.2.13

* Tue Aug 16 2011 Volker Fröhlich <volker27@gmx.at> - 1.2.12-1
- Update for release 1.2.12
- Don't ship tests
- Label examples as documentation

* Mon Aug 15 2011 Volker Fröhlich <volker27@gmx.at> - 1.2.11-2
- BR numpy for the tests

* Mon Aug 15 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.2.11-2
- BR geos-devel to actually build arch specific bits
- Drop unneeded geos dep

* Fri Aug 12 2011 Volker Fröhlich <volker27@gmx.at> - 1.2.11-1 
- Updated for 1.2.11
- Switch away from noarch
- Remove useless clean section and rm in install
- Debian patch to rebuild Cython .c file
- Avoid private provides for .so
- Extend package description

* Fri Apr 01 2011 Volker Fröhlich <volker27@gmx.at> - 1.2.9-1 
- Updated for 1.2.9
- Added tests again, but ignore the results

* Fri Feb 25 2011 Volker Fröhlich <volker27@gmx.at> - 1.2.8-1 
- Updated for 1.2.8
- Disable tests

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 27 2010 Volker Fröhlich <volker27@gmx.at> - 1.2.7-2 
- Explained excluded files; added check section

* Wed Nov 24 2010 Volker Fröhlich <volker27@gmx.at> - 1.2.7-1 
- Initial package for Fedora
