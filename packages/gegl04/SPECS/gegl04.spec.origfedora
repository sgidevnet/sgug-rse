%global apiver 0.4

Name:           gegl04
Version:        0.4.26
Release:        1%{?dist}
Summary:        Graph based image processing framework

# The binary is under the GPL, while the libs are under LGPL.
# The main package only installs the libs, which makes the license:
License:        LGPLv3+
URL:            http://www.gegl.org/
Source0:        http://download.gimp.org/pub/gegl/%{apiver}/gegl-%{version}.tar.xz

BuildRequires:  chrpath
BuildRequires:  enscript
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.19.8
BuildRequires:  gobject-introspection-devel >= 1.32.0
BuildRequires:  gtk-doc
BuildRequires:  libspiro-devel
BuildRequires:  meson
BuildRequires:  perl-interpreter
BuildRequires:  ruby
BuildRequires:  suitesparse-devel
BuildRequires:  vala

BuildRequires:  pkgconfig(babl) >= 0.1.78
BuildRequires:  pkgconfig(cairo) >= 1.12.2
BuildRequires:  pkgconfig(exiv2) >= 0.25
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(jasper) >= 1.900.1
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(lensfun) >= 0.2.5
BuildRequires:  pkgconfig(libraw) >= 0.15.4
BuildRequires:  pkgconfig(libpng) >= 1.6.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(libv4l2) >= 1.0.1
BuildRequires:  pkgconfig(libwebp) >= 0.5.0
BuildRequires:  pkgconfig(lua) >= 5.1.0
%ifarch %{arm} %{ix86} x86_64
BuildRequires:  pkgconfig(luajit) >= 2.0.4
%endif
BuildRequires:  pkgconfig(OpenEXR) >= 1.6.1
BuildRequires:  pkgconfig(pango) >= 1.38.0
BuildRequires:  pkgconfig(pangocairo) >= 1.38.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.2
BuildRequires:  pkgconfig(sdl2) >= 2.0.5
BuildRequires:  pkgconfig(vapigen) >= 0.20.0
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.0

# operations/common/magick-load.c has a fallback image loader which uses /usr/bin/convert
# However, this code path has no error handling, so no application should rely on it; and
# there is a general trend to migrate away from ImageMagick.
# Requires:       /usr/bin/convert

# gegl contains a stripped down version of poly2tri-c, a C+glib port of
# poly2tri, a 2D constrained Delaunay triangulation library.
# Version information:
#     CURRENT REVISION: b27c5b79df2ffa4e2cb37f9e5536831f16afb11b
#     CACHED ON: August 11th, 2012
Provides:       bundled(poly2tri-c)
Obsoletes:      gegl03 < 0.3.31

%description
GEGL (Generic Graphics Library) is a graph based image processing framework.
GEGLs original design was made to scratch GIMP's itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies and a simple well defined API.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.4.2
Obsoletes:      gegl03-devel < 0.3.31
Conflicts:      %{name}-devel < 0.4.2

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use GEGL API version %{apiver}.


%package        devel-docs
Summary:        Documentation files for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.4.2
Obsoletes:      gegl03-devel-docs < 0.3.31
Conflicts:      %{name}-devel < 0.4.2
Conflicts:      gegl-devel < 0.4

%description    devel-docs
The %{name}-devel-docs package contains documentation files for developing
applications that use GEGL API version %{apiver}.


%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        GPLv3+
Obsoletes:      gegl03-tools < 0.3.31
Conflicts:      gegl < 0.4

%description    tools
The %{name}-tools package contains tools for the command line that use the
GEGL library.


%prep
%autosetup -p1 -n gegl-%{version}


%build
%meson --auto-features=auto -Ddocs=true
%meson_build


%install
%meson_install

# Remove rpaths
chrpath --delete %{buildroot}%{_bindir}/*
chrpath --delete %{buildroot}%{_libdir}/*.so*
chrpath --delete %{buildroot}%{_libdir}/gegl-%{apiver}/*.so

%find_lang gegl-%{apiver}


%ldconfig_scriptlets


%files -f gegl-%{apiver}.lang
%license COPYING.LESSER
%{_libdir}/gegl-%{apiver}/
%{_libdir}/libgegl-%{apiver}.so.*
%{_libdir}/libgegl-npd-%{apiver}.so
%{_libdir}/libgegl-sc-%{apiver}.so
%{_libdir}/girepository-1.0/Gegl-%{apiver}.typelib
%ifarch %{arm} %{ix86} x86_64
%dir %{_datadir}/gegl-%{apiver}/
%{_datadir}/gegl-%{apiver}/lua/
%endif

%files devel
%{_includedir}/gegl-%{apiver}/
%{_libdir}/libgegl-%{apiver}.so
%{_libdir}/pkgconfig/gegl-%{apiver}.pc
%{_libdir}/pkgconfig/gegl-sc-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gegl-%{apiver}.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gegl-%{apiver}.deps
%{_datadir}/vala/vapi/gegl-%{apiver}.vapi

%files devel-docs
%doc %{_datadir}/gtk-doc/

%files tools
%license COPYING
%{_bindir}/*


%changelog
* Mon Aug 24 2020 Josef Ridky <jridky@redhat.com> - 0.4.26-1
- New upstream release 0.4.26

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Josef Ridky <jridky@redhat.com> - 0.4.24-1
- New upstream release 0.4.24

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.4.22-2
- Rebuild for new LibRaw

* Wed Feb 19 2020 Josef Ridky <jridky@redhat.com> - 0.4.22-1
- Update to 0.4.22

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Kalev Lember <klember@redhat.com> - 0.4.18-1
- Update to 0.4.18
- Switch to meson build system
- Build against SDL2 instead of SDL 1
- Enable gexiv2 support

* Thu Sep 12 2019 Josef Ridky <jridky@redhat.com> -0.4.16-4
- Obsoletes gegl03 (#1751416)

* Tue Aug 27 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.16-3
- Rebuild for new libspiro

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Kalev Lember <klember@redhat.com> - 0.4.16-1
- Update to 0.4.16

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 0.4.14-2
- Rebuild for OpenEXR 2.3.0.

* Mon Mar 25 2019 Josef Ridky <jridky@redhat.com> - 0.4.14-1
- version 0.4.14

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.4.12-3
- Update BRs for vala packaging changes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.12-1
- version 0.4.12

* Fri Aug 24 2018 Debarshi Ray <rishi@fedoraproject.org> - 0.4.8-2
- Drop the run-time requirement on ImageMagick

* Mon Aug 20 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.8-1
- version 0.4.8

* Thu Jul 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.4.4-3
- Rebuilt for LibRaw soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.4-1
- version 0.4.4

* Mon May 21 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.2-2
- split off devel docs
- let gegl04-devel-docs explicitly conflict with old gegl-devel (#1577595)

* Mon May 21 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.2-1
- version 0.4.2

* Wed May 02 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.0-2
- don't require asciidoc for building
- always install unversioned executables

* Sat Apr 28 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.0-1
- import into Fedora dist-git

* Fri Apr 27 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.0-0.4
- own all created directories
- remove rpaths

* Fri Apr 27 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.0-0.3
- use %%ldconfig_scriptlets macro

* Fri Apr 27 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.0-0.2
- add tools subpackage
- tidy up remains of 0.3
- add back gtk-doc documentation

* Fri Apr 27 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.0-0.1
- initial import
