# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Name:           libAfterImage
Version:        1.20
Release:        22%{?dist}
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
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.20-21
- Fix FTBFS (rhbz#1604550, rhbz#1675256)
- Add build requires on gcc
- Change build requires from libungif-devel to giflib-devel
  (the libungif compat library is no longer available since Fedora 28)
- Port to giflib version 5 and allow unbundling of giflib
- Link the shared library with its dependencies and adjust afterimage-libs
  and afterimage-config --libs to not list the dependencies
- Add build requires on librsvg2-devel and build the package with SVG support
- Create an -apps subpackage containing the sample programs (used to be part
  of the -devel subpackage)
- Do not enable the GLX extension - it causes problems on newer Fedora
  releases (rhbz#1708922, rhbz#1615383 [aterm], rhbz#1704691 [root])
- Update the license file with new FSF address

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.20-8
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.20-7
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.20-5
- fix some issues with newer libpng (rhbz#817780)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.20-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.20-1
- version upgrade
- add improvements/fixes from #672671 (thanks to Mattias Ellert)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 27 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.18-2
- add glx context patch (suggested by Frank Schmitt)

* Sat Oct 04 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.18-1
- version upgrade

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 1.15-4
- Rebuilt for gcc43

* Sat Jan 05 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.15-3
- fix #341871 multiarch

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.15-2
- upgrade BR

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.15-1
- version upgrade
- new license tag

* Mon Sep 11 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-8
- FE6 rebuild

* Wed Feb 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-7
- Rebuild for Fedora Extras 5

* Thu Dec 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-6
- fix typo

* Thu Dec 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-5
- modular X

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-4
- add -fPIC

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-3
- build with debug information
- add dist tag

* Thu Aug 18 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-2
- fix issues mentioned in #166046 #1

* Tue Aug 16 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.07-1
- Initial Release
- 
