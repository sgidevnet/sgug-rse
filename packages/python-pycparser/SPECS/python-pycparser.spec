%bcond_without tests

Name:           python-pycparser
Summary:        C parser and AST generator written in Python
Version:        2.20
Release:        1%{?dist}
License:        BSD
URL:            http://github.com/eliben/pycparser
Source0:        %{url}/archive/release_v%{version}.tar.gz
Source1:        pycparser-0.91.1-remove-relative-sys-path.py

# This is Fedora-specific; I don't think we should request upstream to
# remove embedded libraries from their distribuution, when we can remove
# them during packaging.
# It also ensures that pycparser uses the same YACC __tabversion__ as ply
# package to prevent "yacc table file version is out of date" problem.
Patch100:       pycparser-unbundle-ply.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-ply

# for unit tests
%if %{with tests}
BuildRequires:  cpp
%endif

%description
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.

%package -n python3-pycparser
Summary:        %{summary}
%{?python_provide:%python_provide python3-pycparser}

%description -n python3-pycparser
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.

%prep
%autosetup -p1 -n pycparser-release_v%{version}

# remove embedded copy of ply
rm -r pycparser/ply

# Remove relative sys.path from the examples
%{python3} %{SOURCE1} examples

%build
%py3_build
pushd build/lib/pycparser
%{python3} _build_tables.py
popd

%install
%py3_install

%check
%if %{with tests}
%{python3} tests/all_tests.py
%endif
 
%files -n python3-pycparser
%license LICENSE
%doc examples
%{python3_sitelib}/pycparser/
%{python3_sitelib}/pycparser-*.egg-info/

%changelog
* Fri Jun 05 2020 Miro Hrončok <mhroncok@redhat.com> - 2.20-1
- Update to 2.20 (#1810349)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.19-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Lumír Balhar <lbalhar@redhat.com> - 2.19-1
- New usptream version 2.19

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.14-23
- Subpackage python2-ply has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.14-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.14-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Marcel Plch <mplch@redhat.com> - 2.14-19
- Avoid invalid unicode escape sequences in Py3.8

* Tue Feb 26 2019 Christian Heimes <cheimes@redhat.com> - 2.14-18
- Add build dependency on cpp for unit tests
- Add dependency on python-ply version to prevent "yacc table file version is out of date"
- Fixes RHBZ#1668230

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 2.14-15
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.14-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 2.14-12
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 6 2017 Orion Poplawski <orion@cora.nwra.com> - 2.14-9
- Ship python2-pycparser
- Modernize spec

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.14-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul  8 2016 Tom Callaway <spot@fedoraproject.org> - 2.14-6
- rebuild to update yacctab.py

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 2.14-4
- Rebuilt for Python3.5 rebuild

* Tue Jul 14 2015 Stephen Gallagher <sgallagh@redhat.com> - 2.14-3
- Rebuild alongside python-ply 3.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Nathaniel McCallum <npmccallum@redhat.com> - 2.14-1
- Update to 2.14

* Wed Aug 20 2014 Eric Smith <brouhaha@fedoraproject.org> 2.10-1
- Update to latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.09.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-6
- Added Python 3 support.

* Mon Jul 22 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-5
- Renumbered Fedora-specific Patch1 to Patch100
- Added new Patch1 to fix table generation when the build system
  already has a python-pycparser package installed.
- Submitted Patch0 and Patch1 as upstream issues.
- Added comments about patches.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-4
- Upstream repository is now on github.
- Fix rpmlint strange-permission complaint.
- Rename patches, Source1 to all start with pycparser-{version}, to
  simplify updating patches for future upstream releases.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-3
- Run _build_tables.py to build the lextab.py and yacctab.py; otherwise
  they have to be regenerated at runtime for no benefit.

* Tue Mar 19 2013 Jos de Kloe <josdekloe@gmail.com> 2.09.1-2
- remove the embedded ply code

* Fri Jan 18 2013 Scott Tsai <scottt.tw@gmail.com> 2.09.1-1
- upstream 2.09.1
