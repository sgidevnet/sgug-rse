%global modname pycxx

%if 0%{?el6}%{?el7}%{?fc29}%{?fc30}%{?fc31}
%bcond_without python2
%else
%bcond_with    python2
%endif
%if 0%{?el6}%{?el7}%{?el8}%{?fedora}
%bcond_without python3
%else
%bcond_with    python3
%endif

Name:           python-%{modname}
Version:        7.1.4
Release:        2%{?dist}
Summary:        Write Python extensions in C++

License:        BSD
URL:            http://CXX.sourceforge.net/

BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/cxx/%{modname}-%{version}.tar.gz
# Patch0:  remove unnecessary 'Src/' directory from include path in sources
Patch0:         %{name}-7-change-include-paths.patch


%global _description\
PyCXX is a set of classes to help create extensions of Python in the\
C++ language. The first part encapsulates the Python C API taking care\
of exceptions and ref counting. The second part supports the building\
of Python extension modules in C++.

%description %_description

%if %{with python2}
%package -n python2-%{modname}-devel
Summary:        PyCXX header and source files
%{?python_provide:%python_provide python2-%{modname}-devel}
BuildRequires:  python2-devel
Requires:       python2
# Obsoletes/Provides needed only for EL6
Provides:       python-pycxx-devel = %{version}-%{release}
Obsoletes:      python-pycxx-devel < 7.1.3-5

%description -n python2-%{modname}-devel %_description

The python2-%{modname}-devel package provides the header and source files
for Python 2.  There is no non-devel package needed.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{modname}-devel
Summary:        PyCXX header and source files
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}-devel}
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}

%description -n python%{python3_pkgversion}-%{modname}-devel %_description

The python%{python3_pkgversion}-%{modname}-devel package provides the header and source files
for Python 3.  There is no non-devel package needed.
%endif

%prep
%autosetup -p1 -n %{modname}-%{version}


%build
# Nothing to build.


%install
%global py_install_args --prefix=%{_prefix} --install-headers=%{_includedir}/CXX --install-data=%{_usrsrc}
%{?with_python2:%py2_install -- %{py_install_args}}
%{?with_python3:%py3_install -- %{py_install_args}}

# Write pkg-config PyCXX.pc file
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cat > %{buildroot}%{_datadir}/pkgconfig/PyCXX.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
includedir=%{_includedir}
srcdir=%{_usrsrc}/CXX

Name: PyCXX
Description: Write Python extensions in C++
Version: %{version}
Cflags: -I\${includedir}
EOF


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion PyCXX)" = "%{version}"


%if %{with python2}
%files -n python2-%{modname}-devel
%doc README.html COPYRIGHT Doc/Python2/
%dir %{_includedir}/CXX
%{_includedir}/CXX/*.hxx
%{_includedir}/CXX/*.h
%{_includedir}/CXX/Python2
%{python2_sitelib}/CXX*
%dir %{_usrsrc}/CXX
%{_usrsrc}/CXX/*.cxx
%{_usrsrc}/CXX/*.c
%{_usrsrc}/CXX/Python2
%{_datadir}/pkgconfig/PyCXX.pc
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{modname}-devel
%doc README.html COPYRIGHT Doc/Python3/ 
%dir %{_includedir}/CXX
%{_includedir}/CXX/*.hxx
%{_includedir}/CXX/*.h
%{_includedir}/CXX/Python3
%{python3_sitelib}/CXX*
%dir %{_usrsrc}/CXX
%{_usrsrc}/CXX/*.cxx
%{_usrsrc}/CXX/*.c
%{_usrsrc}/CXX/Python3
%{_datadir}/pkgconfig/PyCXX.pc
%endif


%changelog
* Wed Jun 10 2020 Barry Scott <barry@barrys-emacs.org> - 7.1.4-2
- Update to 7.1.4 which include support for Python 3.9 changes

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.1.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Xavier Bachelot <xavier@bachelot.org> - 7.1.3-5
- Re-introduce python2 subpackage and conditionalize py2/py3 build.

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 7.1.3-4
- Subpackage python2-pycxx-devel has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Barry Scott <barry@barrys-emacs.org> - 7.1.3-1
- Update to 7.1.3 which includes mempry leak fix in
  python 3 Py::String

* Mon Mar 04 2019 Barry Scott <barry@barrys-emacs.org> - 7.1.2-1
- Update to 7.1.2 which includes the setup.py patches
  and the fix for _Py_PackageContext compile error

* Mon Feb 18 2019 Richard Shaw <hobbes1069@gmail.com> - 7.1.1-1
- Update to 7.1.1.
- Clean up python install to be more guidelines compliant.
- Remove gcc-c++ from build requirements as this is a noarch package.


* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Richard Shaw <hobbes1069@gmail.com> - 7.1.0-1
- Update to 7.1.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 7.0.3-3
- Add Python 3.7 patch to add const
- Invoke python2 with python2, not python

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 7.0.3-2
- Rebuilt for Python 3.7

* Wed Apr 11 2018 Richard Shaw <hobbes1069@gmail.com> - 7.0.3-1
- Update to 7.0.3.

* Wed Apr 11 2018 Richard Shaw <hobbes1069@gmail.com> - 7.0.2-1
- Update to 7.0.2.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.2.8-6
- Python 2 binary package renamed to python2-pycxx
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 6.2.8-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.8-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Richard Shaw <hobbes1069@gmail.com> - 6.2.8-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-12.20130805svn280
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.4-11.20130805svn280
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.4-10.20130805svn280
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.4-9.20130805svn280
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 6.2.4-8.20130805svn280
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug  5 2013 John Morris <john@zultron.com> - 6.2.4-7.280svn20130805
- Update to SVN r280 for python3 compatibility
- Update python-pycxx-6.2.4-setup.py.patch to apply correctly
- Fix %%setup for SVN zipball
- Add diff extensions to %%patch macros
- Enable python3 pkg by default except for EPEL; see BZ 991342

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 John Morris <john@zultron.com> - 6.2.4-4
- Minor macro fixes for compiling on el6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012  <john@zultron.com> - 6.2.4-2
- Fix Source0 URL

* Thu Jun 28 2012  <john@zultron.com> - 6.2.4-1
- Install headers into /usr/include/CXX instead of default
  /usr/include/python2.7/CXX (setup.py command line option)
- Install sources into /usr/src/CXX rather than /usr/share/python2.7/CXX
- setup.py patch:
  - Update PyCXX version number
  - Convert tabs to spaces (from original patch)
  - Add omitted headers and sources to install
    - Extend install_headers to handle subdirs
  - Install only Python v2 or v3 code as appropriate
- Add --with=python3 option to build python3-pycxx-devel RPM

* Wed Jun 27 2012  <john@zultron.com> - 6.2.4-0
- Add a pkg-config PyCXX.pc file
- Update to 6.2.4
- Build only a -devel package; no regular package needed
- Beautify specfile, fix macros

* Thu Mar 29 2012  <jman@greaser.zultron.com> - 6.2.3-2
- rebuild with koji

* Wed Feb 22 2012 John Morris <john@zultron.com> - 6.2.3-1
- update to compile on el5 as well as fc16 (missing python_sitelib macro)

* Tue Feb 21 2012  <jman@greaser.zultron.com> - 6.2.3-1
- changed python_sitearch to python_sitelib in files section,
  since package installs in /usr/lib even on x86_64

* Tue Nov 03 2009 Steve Huff <shuff@vecna.org> - 6.1.1-1 - 7987/shuff
- Renamed per RPMforge naming convention.

* Thu Oct 08 2009 Steve Huff <shuff@vecna.org> - 6.1.1-1
- Initial package.

