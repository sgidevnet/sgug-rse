%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

%global glib2_version 2.58.0

%global __python %{__python3}

Name:           gobject-introspection
Version:        1.62.0
Release:        10%{?dist}
Summary:        Introspection system for GObject-based libraries

License:        GPLv2+, LGPLv2+, MIT
URL:            https://wiki.gnome.org/Projects/GObjectIntrospection
Source0:        https://download.gnome.org/sources/gobject-introspection/1.62/%{name}-%{version}.tar.xz

Patch100:       gobject-introspection.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  cairo-gobject-devel
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel >= %{glib2_version}
#BuildRequires:  gtk-doc
BuildRequires:  libffi-devel >= 3.2.1-26
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXft-devel
BuildRequires:  libxml2-devel
#BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-markdown

Requires:       glib2%{?_isa} >= %{glib2_version}

%description
GObject Introspection can scan C header and source files in order to
generate introspection "typelib" files.  It also provides an API to examine
typelib files, useful for creating language bindings among other
things.

%package devel
Summary:        Libraries and headers for gobject-introspection
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Not always, but whatever, it's a tiny dep to pull in
Requires:       libtool
# For g-ir-doctool
Requires:       python3-mako
# This package only works with the Python version it was built with
# https://bugzilla.redhat.com/show_bug.cgi?id=1691064
Requires:       (python(abi) = %{python3_version} if python3)

%description devel
Libraries and headers for gobject-introspection

%prep
%autosetup -p1

# A place to generate patches
#exit 1

# Fix some hardcoded paths
perl -pi -e "s|/usr/share|%{_datadir}|g" giscanner/transformer.py
perl -pi -e "s|/usr/share|%{_datadir}|g" giscanner/utils.py
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" giscanner/dumper.py

%build
export LD_LIBRARYN32_PATH=%{_builddir}/gobject-introspection-1.62.0/mips-sgug-irix/girepository/:$LD_LIBRARYN32_PATH
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++

export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif

%meson -Ddoctool=true -Dgtk_doc=false -Dpython=%{__python3}
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/lib*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/gobject-introspection/
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_bindir}/g-ir-*
%{_datadir}/gir-1.0
%{_datadir}/gobject-introspection-1.0/
%{_datadir}/aclocal/introspection.m4
%{_mandir}/man1/*.gz
#%%dir %%{_datadir}/gtk-doc
#%%dir %%{_datadir}/gtk-doc/html
#%%{_datadir}/gtk-doc/html/gi/

%changelog
* Sat Nov 21 2020 Daniel Hams <daniel.hams@gmail.com> - 1.62.0-10
- Depend on bugfixed libffi

* Wed Sep 23 2020 Daniel Hams <daniel.hams@gmail.com> - 1.62.0-9
- Add extra IRIX defines to ensure thread local errno

* Thu Jul 30 2020 Daniel Hams <daniel.hams@gmail.com> - 1.62.0-8
- Be explicit about which compilers to use

* Sat Jun 20 2020 Daniel Hams <daniel.hams@gmail.com> - 1.62.0-7
- Fix some hardcoded paths + reenable deps now we have packaged enough python pieces

* Fri May 1 2020 HAL <hal@null.not> - 1.16.0-6
- some slight changes so it will build on Irix 6.5 and gcc 9.2

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 1.62.0-1
- Update to 1.62.0
