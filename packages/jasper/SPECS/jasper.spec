
# NOTE: packages that can use jasper:
# ImageMagick
# netpbm

Summary: Implementation of the JPEG-2000 standard, Part 1
Name:    jasper
Version: 2.0.14
Release: 10%{?dist}

License: JasPer
URL:     http://www.ece.uvic.ca/~frodo/jasper/
Source0: http://www.ece.uvic.ca/~frodo/jasper/software/jasper-%{version}.tar.gz

Patch1: jasper-2.0.14-CVE-2016-9396.patch
# skip hard-coded prefix/lib rpath
#Patch2: jasper-2.0.14-rpath.patch
# architecture related patches
Patch100: jasper-2.0.2-test-ppc64-disable.patch
Patch101: jasper-2.0.2-test-ppc64le-disable.patch

# autoreconf
BuildRequires: cmake
#BuildRequires: freeglut-devel 
#BuildRequires: libGLU-devel
BuildRequires: libjpeg-devel
BuildRequires: libXmu-devel libXi-devel
# BuildRequires: pkgconfig doxygen
BuildRequires: pkgconfig
#BuildRequires: mesa-libGL-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: gcc

%description
This package contains an implementation of the image compression
standard JPEG-2000, Part 1. It consists of tools for conversion to and
from the JP2 and JPC formats.

%package devel
Summary: Header files, libraries and developer documentation
Provides: libjasper-devel = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libjpeg-devel
Requires: pkgconfig
%description devel
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Conflicts: jasper < 1.900.1-4
%description libs
%{summary}.

#%%package utils
#Summary: Nonessential utilities for #%%{name}
#Requires: #%%{name} = #%%{version}-#%%{release}
#Requires: #%%{name}-libs#%%{?_isa} = #%%{version}-#%%{release}
#%%description utils
#%%{summary}, including jiv and tmrdemo.


%prep
%setup -q -n %{name}-%{version}

%patch1 -p1 -b .CVE-2016-9396
#%%patch2 -p1 -b .rpath
# Need to disable one test to be able to build it on ppc64 arch
# At ppc64 this test just stuck (nothing happend - no exception or error)

%if "%{_arch}" == "ppc64"
%patch100 -p1 -b .test-ppc64-disable
%endif

# Need to disable two tests to be able to build it on ppc64le arch
# At ppc64le this tests just stuck (nothing happend - no exception or error)

%if "%{_arch}" == "ppc64le"
%patch101 -p1 -b .test-ppc64le-disable
%endif

# Rewrite some hardcoded paths
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" test/bin/wrapper.in
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" test/bin/utilities
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" test/bin/run_test_*
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" test/bin/run_codec_test
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" test/bin/jpenc
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" test/bin/jpdec
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" test/bin/jpcod

#exit 1

%build
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
mkdir builder
#pushd 
PREVWD=`pwd`
cd builder
%cmake .. \
  -DJAS_ENABLE_DOC:BOOL=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
  -DCMAKE_SKIP_RPATH:BOOL=YES \
  -DJPEG_INCLUDE_DIR:STRING=%{_includedir} \
  -DJPEG_LIBRARY_RELEASE:STRING=%{_libdir}/libjpeg.so.9
#popd
cd $PREVWD

%make_build -C builder


%install
make install/fast DESTDIR=%{buildroot} -C builder

# Unpackaged files
rm -f doc/README
rm -f %{buildroot}%{_libdir}/lib*.la


%check
export LD_LIBRARYN32_PATH=`pwd`/builder/src/libjasper:$LD_LIBRARYN32_PATH
make test -C builder

#%%ldconfig_scriptlets libs

%files
%{_bindir}/imgcmp
%{_bindir}/imginfo
%{_bindir}/jasper
%{_mandir}/man1/img*
%{_mandir}/man1/jasper.1*
%{_docdir}/JasPer/*

%files devel
%doc doc/*
%{_includedir}/jasper/
%{_libdir}/libjasper.so
%{_libdir}/pkgconfig/jasper.pc

%files libs
%doc README
%license COPYRIGHT LICENSE
%{_libdir}/libjasper.so.4*

#%%files utils
#%%{_bindir}/jiv
#%%{_mandir}/man1/jiv.1*


%changelog
* Sun Jun 21 2020 Daniel Hams <daniel.hams@gmail.com> - 2.0.14-10
- Correct libjpeg discovery, get tests up and running (and all passing)

* Mon Jun 08 2020  HAL <notes2@gmx.de> - 
- compiles on Irix 6.5 with sgug-rse gcc 9.2, tests fail so compile with --nocheck.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
