%global glib2_version 2.62.6-3

Name:           gdk-pixbuf2
Version:        2.40.0
Release:        5%{?dist}
Summary:        An image loading library

License:        LGPLv2+
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdk-pixbuf/2.40/gdk-pixbuf-%{version}.tar.xz

Patch100:       gdk-pixbuf2.sgifixes.patch
 
BuildRequires:  gettext
#BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  jasper-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.3
# gdk-pixbuf does a configure time check which uses the GIO mime
# layer; we need to actually have the mime type database.
#BuildRequires:  shared-mime-info

Requires: glib2%{?_isa} >= %{glib2_version}
# We also need MIME information at runtime
Requires: shared-mime-info

%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
clutter.

%package modules
Summary: Additional image modules for gdk-pixbuf
Requires: %{name}%{?_isa} = %{version}-%{release}

%description modules
This package contains the additional modules that are needed to load various
image formats such as ICO and JPEG.

%package xlib
Summary: Additional library for using gdk-pixbuf with bare xlib
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xlib
This package contains the old libgdk-pixbuf-xlib library that is needed by some
programs to load GdkPixbuf using bare XLib calls.

%package xlib-devel
Summary: Development files for gdk-pixbuf-xlib
Requires: %{name}-xlib%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description xlib-devel
This package contains the libraries and header files that are needed
for writing applications that are using gdk-pixbuf-xlib.

%package devel
Summary: Development files for gdk-pixbuf
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa} >= %{glib2_version}

%description devel
This package contains the libraries and header files that are needed
for writing applications that are using gdk-pixbuf.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -n gdk-pixbuf-%{version} -p1
export CUR_WD=`pwd`
export LD_LIBRARYN32_PATH=$CUR_WD/mips-sgug-irix/gdk-pixbuf/:$LD_LIBRARYN32_PATH

# A place to generate the sgug patch
#exit 1

export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-gcc

export CFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS -I%{_includedir}/libdicl-0.1 $RPM_OPT_FLAGS"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"

export LD_LIBRARYN32_PATH=`pwd`/mips-sgug-irix/gdk-pixbuf:$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=`pwd`/mips-sgug-irix/contrib/gdk-pixbuf-xlib:$LD_LIBRARYN32_PATH

%meson -Dbuiltin_loaders=png \
       -Ddocs=false \
       -Djasper=true

#       -Ddocs=true \
#

%meson_build

%install
%meson_install

touch $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache

# Don't do fedora multilib stuff on IRIX
#(cd $RPM_BUILD_ROOT%{_bindir}
# mv gdk-pixbuf-query-loaders gdk-pixbuf-query-loaders-%%{__isa_bits}
#)

%find_lang gdk-pixbuf

%transfiletriggerin -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
#gdk-pixbuf-query-loaders-%%{__isa_bits} --update-cache
gdk-pixbuf-query-loaders --update-cache

%transfiletriggerpostun -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
#gdk-pixbuf-query-loaders-%%{__isa_bits} --update-cache
gdk-pixbuf-query-loaders --update-cache

%files -f gdk-pixbuf.lang
%license COPYING
%doc NEWS
%{_libdir}/libgdk_pixbuf-2.0.so.*
%{_libdir}/girepository-1.0
%dir %{_libdir}/gdk-pixbuf-2.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%ghost %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
#%%{_bindir}/gdk-pixbuf-query-loaders-%%{__isa_bits}
%{_bindir}/gdk-pixbuf-query-loaders
%{_bindir}/gdk-pixbuf-thumbnailer
%{_mandir}/man1/gdk-pixbuf-query-loaders.1*
%{_datadir}/thumbnailers/

%files modules
%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.so

%files xlib
%{_libdir}/libgdk_pixbuf_xlib-2.0.so.*

%files xlib-devel
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf-xlib
%{_libdir}/libgdk_pixbuf_xlib-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-xlib-2.0.pc

%files devel
%dir %{_includedir}/gdk-pixbuf-2.0
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf
%{_libdir}/libgdk_pixbuf-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-pixdata
%{_datadir}/gir-1.0
#%%{_datadir}/gtk-doc/html/*
%{_mandir}/man1/gdk-pixbuf-csource.1*

%files tests
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2.40.0-5
- Rebuild for jpegturbo

* Mon Jul 20 2020 Daniel Hams <daniel.hams@gmail.com> - 2.40.0-4
- Fix missing RPM_OPT_FLAGS needed in the CFLAGS

* Sun Jun 21 2020 Daniel Hams <daniel.hams@gmail.com> - 2.40.0-3
- Now we have mime lookups working in glib2, switch back to the internal png loader, remove workarounds, remove fedora multi-lib-isms

* Mon Jun 08 2020  HAL <notes2@gmx.de> - 2.40.0-2 
- compiles on Irix 6.5 with sgug-rse gcc 9.2.
