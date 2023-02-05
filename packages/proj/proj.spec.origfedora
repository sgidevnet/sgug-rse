%global proj_version 5.2.0
%global datumgrid_version 1.8

Name:		proj
Version:	%{proj_version}
Release:	5%{?dist}
Summary:	Cartographic projection software (PROJ.4)

License:	MIT
URL:		https://proj4.org
Source0:	https://download.osgeo.org/%{name}/%{name}-%{version}.tar.gz
Source1:	https://download.osgeo.org/%{name}/%{name}-datumgrid-%{datumgrid_version}.tar.gz
# https://github.com/OSGeo/proj.4/pull/1246
Patch0001:	0001-Allow-building-against-external-GTest-with-autotools.patch

BuildRequires:	libtool gcc-c++
BuildRequires:	gtest-devel >= 1.8.0

# Merged into main package; remove after Fedora 31.
Obsoletes:	proj-epsg < 5.2.0-2
Provides:	proj-epsg = %{version}-%{release}

Requires:	proj-datumgrid = %{datumgrid_version}-%{release}

%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions.


%package devel
Summary:	Development files for PROJ.4
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libproj and the appropriate header files and man pages.


%package static
Summary:	Development files for PROJ.4
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains libproj static library.


%package datumgrid
Summary:	Additional datum shift grids for PROJ.4
Version:	%{datumgrid_version}
# See README.DATUMGRID
License:	CC-BY and Freely Distributable and Ouverte and Public Domain
BuildArch:	noarch

# Renamed; remove after Fedora 31.
Obsoletes:	proj-nad < 5.2.0-2
Provides:	proj-nad = %{proj_version}-%{release}

%description datumgrid
This package contains additional datum shift grids.


%prep
%autosetup -p1

# Prepare datumgrid and file list (in {datadir}/proj and README marked as doc)
tar xvf %{SOURCE1} -C nad | \
    sed -e 's!^!%{_datadir}/%{name}/!' -e '/README/s!^!%%doc !' > datumgrid.files


%build
# rebuild due to patch
autoreconf -i
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
chmod -x %{buildroot}%{_libdir}/libproj.la
install -p -m 0644 nad/README.DATUMGRID %{buildroot}%{_datadir}/%{name}


# Install cmake config manually because we use autotools for building
mkdir -p %{buildroot}%{_datadir}/cmake/Modules/

cat << EOF > %{buildroot}%{_datadir}/cmake/Modules/FindPROJ4.cmake
set(PROJ4_FOUND 1)
set(PROJ4_INCLUDE_DIRS %{_includedir})
set(PROJ4_LIBRARIES proj)
if(\${LIB_SUFFIX} MATCHES 64)
set(PROJ4_LIBRARY_DIRS /usr/lib64)
else()
set(PROJ4_LIBRARY_DIRS /usr/lib)
endif()
set(PROJ4_BINARY_DIRS %{_bindir})
set(PROJ4_VERSION %{proj_version})
message(STATUS "Found PROJ4: version \${PROJ4_VERSION}")
EOF


%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
    make PROJ_LIB=%{buildroot}%{_datadir}/%{name} check || ( cat src/test-suite.log; exit 1 )


%files
%doc NEWS AUTHORS COPYING README ChangeLog
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_libdir}/libproj.so.13*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CH
%{_datadir}/%{name}/GL27
%{_datadir}/%{name}/IGNF
%{_datadir}/%{name}/ITRF2000
%{_datadir}/%{name}/ITRF2008
%{_datadir}/%{name}/ITRF2014
%{_datadir}/%{name}/epsg
%{_datadir}/%{name}/esri
%{_datadir}/%{name}/esri.extra
%{_datadir}/%{name}/nad.lst
%{_datadir}/%{name}/nad27
%{_datadir}/%{name}/nad83
%{_datadir}/%{name}/null
%{_datadir}/%{name}/other.extra
%{_datadir}/%{name}/proj_def.dat
%{_datadir}/%{name}/world

%files devel
%{_mandir}/man3/*.3*
%{_includedir}/*.h
%{_libdir}/libproj.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/cmake/Modules/FindPROJ4.cmake
%exclude %{_libdir}/libproj.a
%exclude %{_libdir}/libproj.la

%files static
%{_libdir}/libproj.a
%{_libdir}/libproj.la

%files datumgrid -f datumgrid.files
%dir %{_datadir}/%{name}


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Dan Horák <dan[at]danny.cz> - 5.2.0-4
- fix condition in cmake config

* Tue Apr 16 2019 Dan Horák <dan[at]danny.cz> - 5.2.0-3
- install cmake config

* Sat Apr 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.2.0-2
- Rename proj-nad subpackage as proj-datumgrid
- Fold proj-epsg package into main one
- Enable full test suite during build
- Various spec file cleanups

* Mon Feb 04 2019 Devrim Gündüz <devrim@gunduz.org> - 5.2.0-1
- Update to 5.2.0
- Update to new datumgrid (1.8)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Devrim Gündüz <devrim@gunduz.org> 4.9.3-1
- Update to 4.9.3
- Update to new datumgrid (1.6)
- Fix rpmlint warnings
- Cosmetic cleanup  in spec file.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Devrim Gündüz <devrim@gunduz.org> 4.9.2-1
- Update to 4.9.2, per bz # 1294604
- Update URLs.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-2
- track soname so bumps are not a suprise
- -devel: include .pc file here (left copy in -nad too)
- -static: Requires: -devel

* Wed Mar 11 2015 Devrim Gündüz <devrim@gunduz.org> 4.9.1-1
- Update to 4.9.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Devrim Gündüz <devrim@gunduz.org> 4.8.0-3
- Install projects.h manually, per #830496.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Devrim Gündüz <devrim@gunduz.org> 4.8.0-1
- Update to 4.8.0, per bz #814851

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 4.7.0-3
- fix for bz#562671

* Thu Mar 18 2010 Balint Cristian <cristian.balint@gmail.com> - 4.7.0-2
- fix for bz#556091

* Fri Dec 4 2009 Devrim Gündüz <devrim@gunduz.org> 4.7.0-1
- Update to 4.7.0
- Update to new datumgrid (1.5)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Balint Cristian <rezso@rdsor.ro> - 4.6.1-1
- new stable upstream
- new nad datumgrids
- drop debian license patch
- change homepage URLs

* Sun Apr 20 2008 Balint Cristian <rezso@rdsor.ro> - 4.6.0-1
- new branch

* Thu Mar 27 2008 Balint Cristian <rezso@rdsor.ro> - 4.5.0-4
- BuildRequire: libtool

* Thu Mar 27 2008 Balint Cristian <rezso@rdsor.ro> - 4.5.0-3
- enable EPSG dataset to be packed GRASS really needs it
- no more license issue over epsg dataset, proj didnt altered
  EPSG dataset in any way, so its fully EPSG license compliant
- add support for tests during buildtime
- disable hardcoded r-path from libs
- fix shebag for nad scripts

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.5.0-2
- Autorebuild for GCC 4.3

* Tue Jan   2 2007 Shawn McCann <mccann0011@hotmail.com> - 4.5.0-1
- Updated to proj-4.5.0 and datumgrid-1.3

* Sat Sep  16 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-4
- Rebuild for Fedora Extras 6

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-3
- Rebuild for Fedora Extras 5

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-2
- Rebuild for Fedora Extras 5

* Thu Jul  7 2005 Shawn McCann <mccann0011@hotmail.com> - 4.4.9-1
- Updated to proj-4.4.9 and to fix bugzilla reports 150013 and 161726. Patch2 can be removed once this package is upgraded to the next release of the source.

* Sun May 22 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 4.4.8-6
- rebuilt

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 4.4.8-5
- rebuilt

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-4
- Added testvarious to nad distribution

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-0.fdr.3
- Added patch for test scripts so that they will work in installed rpm

* Wed Dec 29 2004 David Kaplan <dmk@erizo.ucdavis.edu> - 0:4.4.8-0.fdr.2
- Fixed permissions on nad27 and nad83
- Included test27 and test83 in the nad rpm and made them executable

* Fri Aug 13 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.8-0.fdr.1
- Updated to version 4.4.8 of library.
- Changed license file so that it agrees with Debian version.
- Updated web addresses of packages.

* Wed Aug 11 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.7-0.fdr.3
- Removed the "Requires(post,postun)"

* Tue Dec 30 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:4.4.7-0.fdr.2
- proj-nad now owns %%{_datadir}/%%{name}

* Wed Oct 29 2003 Steve Arnold <sarnold@arnolds.dhs.org>
- Basically re-wrote previous spec file from scratch so as
- to comply with both Fedora and RedHat 9 packaging guidelines.
- Split files into proj, proj-devel, and proj-nad (additional grids)
- and adjusted the EXE path in the test scripts.
