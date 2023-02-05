# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Name:           libAfterImage
Version:        1.20
Release:        23%{?dist}
Summary:        A generic image manipulation library

License:        LGPLv2+
URL:            http://www.afterstep.org/afterimage/index.php
Source0:        ftp://ftp.afterstep.org/stable/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}-COPYING
#               Don't call ldconfig as part of "make install"
Patch0:         %{name}-Makefile-ldconfig.patch
#               Port to libpng 1.5 and later (patch from gentoo)
Patch1:         %{name}-libpng15.patch
#               Port to giflib version 5 and allow unbundling of giflib
Patch2:         %{name}-unbundle-libgif.patch
#               Link the shared library with its dependencies
Patch3:         %{name}-link.patch

Patch10:        %{name}.useldflagsforso.patch

BuildRequires:  gcc
#BuildRequires:  freetype-devel
BuildRequires:  zlib-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
#BuildRequires:  librsvg2-devel
#BuildRequires:  libX11-devel
#BuildRequires:  libXext-devel
BuildRequires:  gawk

%description
libAfterImage is a generic image manipulation library. It was initially
implemented to address AfterStep Window Manager's needs for image handling,
but it evolved into extremely powerful and flexible software, suitable for
virtually any project that has needs for loading, manipulating, displaying
images, as well as writing images in files. Most of the popular image formats
are supported using standard libraries, with XCF, XPM, PPM/PNM, BMP, ICO and
TGA being supported internally.

GIF, PNG, JPEG, TIFF and SVG formats are supported via standard libraries.

Powerful text rendering capabilities included, providing support for
TrueType fonts using FreeType library, and anti-aliasing of standard fonts
from X window system. 

# Here's a terminator

%package devel
Summary:        Files needed for software development with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
#               Package split (apps split out from devel)
Obsoletes:      %{name}-devel < 1.20-21

%description devel
The %{name}-devel package contains the files needed for development with
%{name}.

%package apps
Summary:        Sample programs using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
#               Package split (apps split out from devel)
Obsoletes:      %{name}-devel < 1.20-21

%description apps
The %{name}-apps package contains sample programs using %{name}.

%prep
%setup -q
%patch0 
%patch1
%patch2 -p1
%patch3 -p1

%patch10 -p1 -b .useldflagsforso

# Delete bundled sources
rm libjpeg/*
rm libpng/*
rm libungif/*
rm zlib/*

sed /zlib/d -i .depend

%build
export CPPFLAGS="-DLIBAFTERIMAGE_UNIQ_CC"
%configure --enable-i18n --disable-staticlibs --enable-sharedlibs \
--disable-mmx-optimization --without-builtin-gif --without-afterbase \
--x-includes=%{_includedir} --x-libraries=%{_libdir}

make CCFLAGS="-DNO_DEBUG_OUTPUT -fPIC $RPM_OPT_FLAGS" %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT %{?_smp_mflags}

cp %{SOURCE1} COPYING

#ldconfig_scriptlets

%files
%doc README ChangeLog
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_bindir}/afterimage-*
%{_includedir}/%{name}
%{_libdir}/*.so

%files apps
%{_bindir}/as*

%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 1.20-23
- Rebuild for jpegturbo

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
