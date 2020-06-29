%global srcname rencode

Name:           python-rencode
Version:        1.0.6
Release:        10%{?dist}
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            https://github.com/aresch/rencode

Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz

# PyPi source tarball doesn't contain the .pyx file. This is the .pyx file
# corresponding to tag 1.0.6. Updating the version will also require this file
# to be updated.
# https://github.com/aresch/rencode/issues/22
Source1:        https://raw.githubusercontent.com/aresch/rencode/53d72ac53d9df007aad3a980f049a80d81836619/rencode/rencode.pyx

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-wheel


%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.


%package -n python3-rencode
Summary:    Web safe object pickling/unpickling
%{?python_provide:%python_provide python%{python3_pkgversion}-rencode}


%description -n python3-rencode
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.


%prep
%autosetup -n rencode-%{version}
cp -a %{SOURCE1} ./rencode

# Make sure we rebuild the module
rm -f ./rencode/rencode.c

%build
%py3_build


%install
%py3_install


%check
pushd tests
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} %{__python3} test_rencode.py
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} %{__python3} timetest.py
popd


%files -n python%{python3_pkgversion}-rencode
%{python3_sitearch}/rencode
%{python3_sitearch}/rencode*.egg-info
%doc README.md
%license COPYING


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-5
- Subpackage python2-rencode has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov  4 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.6-3
- Remove package .c extension file before building

* Sun Nov  4 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.6-2
- Bump release

* Sun Nov  4 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.6-1
- Update to version 1.0.6
- Switch URL to point to PyPi
- Cleanup old macros in spec file
- Add rencode.pyx file from git repository
- Add BuildRequires for python{2,3}-wheel

* Sun Jul 22 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-12
- Fix usage of macros for file list

* Sun Jul 22 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-11
- Fix running of tests (BZ #1605871)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-4
- Rebuild for Python 3.6

* Tue Nov 8 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.5-3
- Enable builds on EPEL7

* Sat Oct  1 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-2
- Revert to using github tarballs as PyPi tarballs omit tests

* Sat Oct  1 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.5-1
- Update to 1.0.5
- Update source URL

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Feb 27 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.4-0
- Update to 1.0.4
- Split out python2-rencode subpackage, and leave main package empty
- Add use of python_provide macros according to guidelines
- Clean up spec file, remove redundant code
- Use python build and install macros
- Build and test both python2 and python3 packages in same directory

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.3-1
- Update to version 1.0.3
- Update upstream location (now on github)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.2-4.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3.20121209svn33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2.20121209svn33
- use macros consistently
- fix permissions on shared objects
- drop useless setuptools copypasta
- fix License tag

* Thu Apr 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1.20121209svn33
- initial package
