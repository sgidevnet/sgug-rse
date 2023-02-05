
# use cmake-buildsys, else autofoo
# will probably rip this macro out soon, did so to help make
# upstreamable patches -- Rex
%global cmake_build 1

# enable conformance tests
#global runcheck 1

Name:    openjpeg
Version: 1.5.1
Release: 24%{?dist}
Summary: JPEG 2000 command line tools

License: BSD
URL:     http://code.google.com/p/openjpeg/

Source0: http://downloads.sourceforge.net/openjpeg.mirror/%{name}-%{version}.tar.gz
%if 0%{?runcheck}
# svn checkout http://openjpeg.googlecode.com/svn/data
Source1: data.tar.xz
%endif

# revert soname bump compared to 1.5.0 release (for now)
Patch1: openjpeg-1.5.1-soname.patch
# 1.5.2 -> 1.5.1 backport
Patch2: openjpeg-1.5.1-offset-check.patch

## upstreamable patches
Patch50: openjpeg-1.5.1-cmake_libdir.patch
Patch51: openjpeg-1.5.1-doxygen_timestamp.patch
# Only compile with -ffast-math, linking with it causes problem for library users
# https://bugzilla.redhat.com/show_bug.cgi?id=1127544
Patch52: openjpeg-fast-math.patch

## upstream patches:
# http://code.google.com/p/openjpeg/issues/detail?id=155
Patch100: openjpeg-1.5-r2029.patch
# http://code.google.com/p/openjpeg/issues/detail?id=152
Patch101: openjpeg-1.5-r2031.patch
# http://code.google.com/p/openjpeg/issues/detail?id=169
Patch102: openjpeg-1.5-r2032.patch
# http://code.google.com/p/openjpeg/issues/detail?id=166
Patch103: openjpeg-1.5-r2033.patch

## security patches
# https://bugzilla.redhat.com/show_bug.cgi?id=1036491
Patch200: openjpeg-1.5.1-CVE-2013-6052.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1036493
Patch201: openjpeg-1.5.1-CVE-2013-6053.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1036495
# omitted due to regression https://bugzilla.redhat.com/show_bug.cgi?id=1047494
Patch202: openjpeg-1.5.1-CVE-2013-6045.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1037945
Patch203: openjpeg-1.5.1-CVE-2013-1447.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1037948
Patch204: openjpeg-1.5.1-CVE-2013-6887.patch

%if 0%{?cmake_build}
BuildRequires: cmake
%else
BuildRequires: automake libtool
%endif
#BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
OpenJPEG is an open-source JPEG 2000 codec written in C. It has been
developed in order to promote the use of JPEG 2000, the new still-image
compression standard from the Joint Photographic Experts Group (JPEG).

%package libs
Summary: JPEG 2000 codec runtime library
%description libs
The %{name}-libs package contains runtime libraries for applications that use
OpenJPEG.

%package  devel
Summary:  Development files for %{name} 
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use OpenJPEG.

#%%package  devel-docs
#Summary:  Developer documentation for #%%{name}
#%BuildArch: noarch
#%%description devel-docs
#%%{summary}.


%prep
%setup -q %{?runcheck:-a 1}

%patch1 -p1 -b .soname
%patch2 -p1 -b .offset

%if 0%{?cmake_build}
%patch50 -p1 -b .cmake_libdir
%else
autoreconf -i -f
%endif

%patch51 -p1 -b .doxygen_timestamp
%patch52 -p1 -b .fast-math

%patch100 -p0 -b .r2029
%patch101 -p0 -b .r2031
%patch102 -p0 -b .r2032
%patch103 -p0 -b .r2033

%patch200 -p1 -b .CVE-2013-6052
%patch201 -p1 -b .CVE-2013-6053
%patch202 -p1 -b .CVE-2013-6045
%patch203 -p1 -b .CVE-2013-1447
%patch204 -p1 -b .CVE-2013-6887


%build

%{?runcheck:export OPJ_DATA_ROOT=$(pwd)/data}

%if 0%{?cmake_build}
mkdir -p %{_target_platform}
#pushd 
PREVWD=`pwd`
cd %{_target_platform}
%{cmake} \
  -DBUILD_DOC:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBUILD_MJ2:BOOL=ON \
  %{?runcheck:-DBUILD_TESTING:BOOL=ON} \
  -DCMAKE_BUILD_TYPE=Release \
  -DOPENJPEG_INSTALL_LIB_DIR:PATH=%{_lib} \
   ..
#popd
cd $PREVWD

%make_build -C %{_target_platform}

%else
%configure \
  --enable-shared \
  --disable-static

%make_build
%endif


%install
%if 0%{?cmake_build}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%else
%make_install
%endif

# continue to ship compat header symlink
ln -s openjpeg-1.5/openjpeg.h %{buildroot}%{_includedir}/openjpeg.h

## unpackaged files
# we use %%doc in -libs below instead
rm -rfv %{buildroot}%{_docdir}/openjpeg-1.5/
rm -fv  %{buildroot}%{_libdir}/lib*.la


%check
test -f %{buildroot}%{_includedir}/openjpeg.h
## known failures (on rex's f16/x86_64 box anyway)
%if 0%{?runcheck}
%make_build test -C %{_target_platform}
%endif


%files
%{_bindir}/image_to_j2k
%{_bindir}/j2k_dump
%{_bindir}/j2k_to_image
%{_bindir}/extract_j2k_from_mj2
%{_bindir}/frames_to_mj2
%{_bindir}/mj2_to_frames
%{_bindir}/wrap_j2k_in_mj2
%{_mandir}/man1/*image_to_j2k.1*
%{_mandir}/man1/*j2k_dump.1*
%{_mandir}/man1/*j2k_to_image.1*

#%%ldconfig_scriptlets libs

%files libs
%doc CHANGES
%license LICENSE
%{_libdir}/libopenjpeg.so.1*
%{_mandir}/man3/*libopenjpeg.3*

%files devel
%{_includedir}/openjpeg-1.5/
# fedora-only compat symlink
%{_includedir}/openjpeg.h
%{_libdir}/libopenjpeg.so
%{_libdir}/pkgconfig/libopenjpeg.pc
%{_libdir}/pkgconfig/libopenjpeg1.pc
%if 0%{?cmake_build}
%{_libdir}/openjpeg-1.5/
%endif

#%%files devel-docs
#%%doc %{?cmake_build:#%%{_target_platform}/}doc/html/


%changelog
* Sat Aug 22 2020  HAL <notes2@gmx.de> - 1.5.1-24
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.5.1-21
- BR: gcc-c++, use %%ldconfig_scriptlets %%license %%make_build %%make_install

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Orion Poplawski <orion@cora.nwra.com> - 1.5.1-14
- Do not link with -ffast-math (bug #1127544)

* Wed Oct 08 2014 Jaromir Capik <jcapik@redhat.com> - 1.5.1-13
- Reworked fix for CVE-2013-6045 (#1093379)
- Offset check (1.5.2 -> 1.5.1 backport)

* Thu Sep 04 2014 Petr Hracek <phracek@redhat.com> - 1.5.1-12
- OpenJPEG does not provide some binaries (#1138141)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Jaromir Capik <jcapik@redhat.com> - 1.5.1-9
- Minor spec file changes according to the latest guidelines
- Fixing source URL

* Sat Jan 11 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-8
- revert CVE-2013-6045 patch due to regression (#1047494)

* Tue Jan 07 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-7
- plethora of security updates (#1038409)
- CVE-2013-6052 (#1036491)
- CVE-2013-6053 (#1036493)
- CVE-2013-6045 (#1036495)
- CVE-2013-1447 (#1037945)
- CVE-2013-6887 (#1037948)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-4
- *really* fix multilib bugs due to timestamps in generated doc files (#884827)

* Fri Dec 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-3
- int main() in t1_generate_luts.c breaks mplayer (issue#152)
- jp2_read_boxhdr() can trigger random pointer memory access (issue#155)
- missing range check in j2k_read_coc et al (issue#166)
- division by zero in j2k_read_siz (issue#169)

* Thu Dec 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-2
- fix multilib bugs due to timestamps in generated doc files (#884827)

* Thu Sep 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-1
- 1.5.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-3
- -DCMAKE_BUILD_TYPE=Release

* Sat Feb 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-2
- first try at fixing pkgconfig includedir paths (upstream issue #118)

* Thu Feb 09 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-1
- 1.5.0

* Wed Feb 01 2012 Jaromir Capik <jcapik@redhat.com> 1.4-11
- fix for #726262 - /usr/include/openjpeg changed to a symlink
- rpm bug workaround

* Tue Jan 31 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4-10
- backport upstream patch to avoid poppler regressions (upstream issue #104)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 01 2011 Oliver Falk <oliver@linux-kernel.at> 1.4-8
- Remove pkgconfig from reqs (my fault)

* Mon Aug 01 2011 Oliver Falk <oliver@linux-kernel.at> 1.4-7
- devel package requires pkgconfig

* Wed Mar 30 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4-6
- fix pkgconfig support (upstream issue 67)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.4-4
- actually apply patch for OpenJPEGConfig.cmake (#669425)

* Mon Jan 31 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.4-3
- fix OpenJPEGConfig.cmake (#669425)

* Thu Jan 13 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.4-2
- -devel: %%_includedir/openjpeg/ symlink
- add pkgconfig support (to cmake build)

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.4-1
- openjpeg-1.4

* Fri Oct  1 2010 Tomas Hoger <thoger@fedoraproject.org> - 1.3-10
- Use calloc in opj_image_create0 (SVN r501, rhbz#579548)
- Avoid NULL pointer deref in jp2_decode (SVN r505, rhbz#609385)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3-9
- include test samples, enable tests
- tighten subpkg deps
- explicitly set/use -DBUILD_SHARED_LIBS:BOOL=ON
- move %%doc files to -libs

* Wed Feb 17 2010 Adam Goode <adam@spicenitz.org> - 1.3-8
- Fix typo in description
- Fix charset of ChangeLog (rpmlint)
- Fix file permissions (rpmlint)
- Make summary more clear (rpmlint)

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3-7
- FTBFS openjpeg-1.3-6.fc12: ImplicitDSOLinking (#564783)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.3-5
- libopenjpeg has undefined references (#467661)
- openjpeg.h is installed in a directory different from upstream's default (#484887)
- drop -O3 (#504663)
- add %%check section
- %%files: track libopenjpeg somajor (2)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Rex Dieter <rdieter@fedoraproject.org> 1.3-3
- FTBFS (#464949)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-2
- Autorebuild for GCC 4.3

* Thu Dec 27 2007 Callum Lerwick <seg@haxxed.com> 1.3-1
- New upstream release.

* Tue Dec 11 2007 Callum Lerwick <seg@haxxed.com> 1.2-4.20071211svn484
- New snapshot. Fixes bz420811.

* Wed Nov 14 2007 Callum Lerwick <seg@haxxed.com> 1.2-3.20071114svn480
- Build using cmake.
- New snapshot.

* Thu Aug 09 2007 Callum Lerwick <seg@haxxed.com> 1.2-2.20070808svn
- Put binaries in main package, move libraries to -libs subpackage.

* Sun Jun 10 2007 Callum Lerwick <seg@haxxed.com> 1.2-1
- Build the mj2 tools as well.
- New upstream version, ABI has broken, upstream has bumped soname.

* Fri Mar 30 2007 Callum Lerwick <seg@haxxed.com> 1.1.1-3
- Build and package the command line tools.

* Fri Mar 16 2007 Callum Lerwick <seg@haxxed.com> 1.1.1-2
- Link with libm, fixes building on ppc. i386 and x86_64 are magical.

* Fri Feb 23 2007 Callum Lerwick <seg@haxxed.com> 1.1.1-1
- New upstream version, which has the SL patches merged.

* Sat Feb 17 2007 Callum Lerwick <seg@haxxed.com> 1.1-2
- Move header to a subdirectory.
- Fix makefile patch to preserve timestamps during install.

* Sun Feb 04 2007 Callum Lerwick <seg@haxxed.com> 1.1-1
- Initial packaging.
