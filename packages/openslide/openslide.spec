Name:		openslide
Version:	3.4.1
Release:	14%{?dist}
Summary:	C library for reading virtual slides

License:	LGPLv2
URL:		http://openslide.org/
Source0:	https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)

BuildRequires:	gcc
BuildRequires:	libjpeg-turbo-devel

# Required for gdk-pixbuf2 to actually be able to load image files
Requires:	gdk-pixbuf2-modules%{?_isa}


%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package   	tools
Summary:	Command line tools for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	tools
The %{name}-tools package contains command line tools for working
with virtual slides.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc README.txt CHANGELOG.txt
%license lgpl-2.1.txt LICENSE.txt
%{_libdir}/*.so.0*


%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%files tools
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.1-12
- Avoid soname-concealing glob per new policy

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.1-10
- Drop ldconfig scriptlets per new policy

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.1-6
- Drop Group tags

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 21 2016 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.1-4
- BuildRequire gcc per new policy

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.1-1
- New release
- Switch to OpenJPEG 2

* Sun Mar 22 2015 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.0-4
- Add dependency on new gdk-pixbuf2-modules subpackage
- Move license files to %%license

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 26 2014 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.0-1
- New release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.3-1
- New upstream release
   + Minor compatibility improvements for Aperio JP2K and Hamamatsu slides
- Update Source0 URL

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.3.2-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.3.2-3
- rebuild against new libjpeg

* Fri Dec 21 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.2-2
- Rebuild for jpeg8

* Sat Dec 01 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.2-1
- New upstream release
   + Fix seams in MIRAX 2.2 slides
   + Fix associated images in single-level Aperio slides
   + Improve performance on MIRAX and Hamamatsu VMU

* Sun Oct 14 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.1-1
- New upstream release
   + Parallelize concurrent openslide_read_region calls
   + Performance improvements for MIRAX and Hamamatsu VMS

* Sat Sep 22 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.0-1
- New upstream release
   + Support for Leica SCN format (requires libtiff 4)
   + Partial support for MIRAX 2.2
   + Standard properties for microns-per-pixel and objective power
   + Improved reporting of open errors
   + Command-line tool improvements
- Add versioned dependency on main package to subpackages

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Adam Goode <adam@spicenitz.org> - 3.2.6-1
- New upstream release
   + Support for downsampled MIRAX files
   + Improved MIRAX performance and bugfixes
   + Fix for openslide_read_region with large dimensions

* Thu Feb 09 2012 Rex Dieter <rdieter@fedoraproject.org> 3.2.5-2
- rebuild (openjpeg)

* Mon Jan 16 2012 Adam Goode <adam@spicenitz.org> - 3.2.5-1
- New upstream release
   + Support for MIRAX 1.03 files
   + openslide_read_region now works for large dimensions
   + quickhash-1 is disabled for unusual TIFFs where it is very slow

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.2.4-2
- Rebuild for new libpng

* Fri Aug 12 2011 Adam Goode <adam@spicenitz.org> - 3.2.4-1
- New upstream release, see http://github.com/openslide/openslide/blob/master/CHANGELOG.txt

* Fri Aug 12 2011 Adam Goode <adam@spicenitz.org> - 3.2.3-5
- Clean up the spec file a little

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.2.3-3
- rebuild (openjpeg)

* Wed Sep 29 2010 jkeating - 3.2.3-2
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Adam Goode <adam@spicenitz.org> - 3.2.3-1
- New upstream release, see http://github.com/openslide/openslide/blob/master/CHANGELOG.txt

* Sat Jun 19 2010 Adam Goode <adam@spicenitz.org> - 3.2.2-2
- Restore missing clean section

* Wed Jun 16 2010 Adam Goode <adam@spicenitz.org> - 3.2.2-1
- New upstream release
   + Add openslide-write-png
   + Support for VMU files
   + New error handling system

* Tue Apr 27 2010 Adam Goode <adam@spicenitz.org> - 3.1.1-1
- New upstream release
   + Don't crash or leak memory on some invalid VMS files
   + Ignore extra layers in VMS files

* Thu Apr  1 2010 Adam Goode <adam@spicenitz.org> - 3.1.0-1
- New upstream release
   + Support newer Aperio files (compression 33005)
   + Be more robust in reading raw TIFF tiles
   + Reject invalid TIFF files earlier
   + Fix many memory leaks when probing for TIFF files

* Tue Mar  2 2010 Adam Goode <adam@spicenitz.org> - 3.0.3-1
- New upstream release
   + Fix nasty MIRAX seam problem

* Wed Feb 17 2010 Adam Goode <adam@spicenitz.org> - 3.0.2-1
- New upstream release
   + Allow building on RHEL

* Thu Feb  4 2010 Adam Goode <adam@spicenitz.org> - 3.0.1-1
- New upstream release
   + Fix rendering of the edges of TIFF files
   + Include CHANGELOG.txt

* Mon Feb  1 2010 Adam Goode <adam@spicenitz.org> - 3.0.0-1
- New upstream release
   + License change from GPLv2 to LGPLv2
   + Bug fixes
   + Support more MIRAX files
   + Improve perforamance of MIRAX
   + Add some command-line tools
   + Rework API documentation
   + Add some new properties
   + Remove some unimplemented functions from the header file

* Mon Dec 21 2009 Adam Goode <adam@spicenitz.org> - 2.3.1-1
- New upstream release
   + Support for generic tiled TIFF
   + Bug fixes
   + Try to be less chatty with TIFF output

* Thu Nov 12 2009 Adam Goode <adam@spicenitz.org> - 2.2.1-1
- New upstream release
   + Fix thread safety problems from 2.2.0

* Tue Sep 22 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-3
- Use xz instead of gz

* Mon Sep 21 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-2
- Be more explicit about include directory in files section

* Tue Sep 15 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-1
- New upstream release
   + Thread safety (sometimes lockless)

* Thu Sep 10 2009 Adam Goode <adam@spicenitz.org> - 2.1.0-1
- New upstream release
   + MIRAX support
   + More Aperio support
   + Properties and associated images support
   + Bug fixes

* Wed Feb 25 2009 Adam Goode <adam@spicenitz.org> - 1.1.1-1
- New upstream release
- No more included OpenJPEG
- Much faster rendering and loading

* Tue Dec  9 2008 Adam Goode <adam@spicenitz.org> - 1.0.0-1
- First release
