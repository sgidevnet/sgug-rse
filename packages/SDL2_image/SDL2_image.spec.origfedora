Name:           SDL2_image
Version:        2.0.5
Release:        2%{?dist}
Summary:        Image loading library for SDL

# IMG_png.c is LGPLv2+ and zlib, rest is just zlib
# nanosvg is zlib
# miniz is Public Domain
License:        LGPLv2+ and zlib
URL:            http://www.libsdl.org/projects/SDL_image/
Source0:        http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  SDL2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  chrpath
Provides:       bundled(miniz) = 1.15
# Some custom version of it
Provides:       bundled(nanosvg)

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL surfaces.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
rm -rf external/
sed -i -e 's/\r//g' README.txt CHANGES.txt COPYING.txt

%build
%configure --disable-dependency-tracking \
           --disable-jpg-shared \
           --disable-png-shared \
           --disable-tif-shared \
           --disable-webp-shared \
           --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_bindir}
./libtool --mode=install /usr/bin/install showimage %{buildroot}%{_bindir}/showimage2
chrpath -d %{buildroot}%{_bindir}/showimage2

rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING.txt
%doc CHANGES.txt
%{_bindir}/showimage2
%{_libdir}/libSDL2_image-2.0.so.*

%files devel
%doc README.txt
%{_libdir}/libSDL2_image.so
%{_includedir}/SDL2/SDL_image.h
%{_libdir}/pkgconfig/SDL2_image.pc

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Pete Walter <pwalter@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar  4 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.3-1
- Update to 2.0.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-3
- Switch to %%ldconfig_scriptlets

* Wed Nov 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-2
- Add Provides: bundled(nanosvg) and add zlib to License

* Wed Nov 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Wed Oct 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-8
- Fixed security vulnerability in XCF image loader

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 2.0.1-4
- Rebuild (libwebp)

* Tue Jan 03 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.1-3
- Stop requiring pkgconfig

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.1-1
- Update to 2.0.1 (RHBZ #1296751)

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-9
- Rebuilt for libwebp soname bump

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Dan Horák <dan[at]danny.cz> - 2.0.0-5
- fix FTBFS on big endian arches

* Fri Jan 03 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.0-4
- Rebuilt for libwebp soname bump

* Fri Sep  6 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-3
- showimage -> showimage2 (rhbz 1005324)

* Fri Sep  6 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-2
- Move README.txt to -devel subpackage

* Fri Sep  6 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-1
- Based on SDL_image
