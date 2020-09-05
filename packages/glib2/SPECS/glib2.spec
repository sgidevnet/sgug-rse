%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

%global _changelog_trimtime %(date +%s -d "1 year ago")

Name: glib2
Version: 2.62.6
Release: 4%{?dist}
Summary: A library of handy utility functions

License: LGPLv2+
URL: http://www.gtk.org
Source0: http://download.gnome.org/sources/glib/2.62/glib-%{version}.tar.xz

Patch1000:  glib2.sgifixes.patch

#BuildRequires: chrpath
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
#BuildRequires: gtk-doc
BuildRequires: perl-interpreter
# for sys/inotify.h
#BuildRequires: glibc-devel
#BuildRequires: libattr-devel
#BuildRequires: libselinux-devel
BuildRequires: meson
# for sys/sdt.h
#BuildRequires: systemtap-sdt-devel
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libpcre)
#BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-devel

BuildRequires: libdicl-devel >= 0.1.34

# for GIO content-type support
Recommends: shared-mime-info

# glib 2.59.0 hash table changes broke older gcr versions / password prompts in gnome-shell
Conflicts: gcr < 3.28.1

%description
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality
as an event loop, threads, dynamic loading, and an object system.


%package devel
Summary: A library of handy utility functions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The glib2-devel package includes the header files for the GLib library.

#%%package doc
#Summary: A library of handy utility functions
#Requires: #{name} = #{version}-#{release}
#BuildArch: noarch

#%%description doc
#The glib2-doc package includes documentation for the GLib library.

#%package fam
#Summary: FAM monitoring module for GIO
#Requires: #{name}#{?_isa} = #{version}-#{release}
#BuildRequires: gamin-devel
#
#%description fam
#The glib2-fam package contains the FAM (File Alteration Monitor) module for GIO.

%package static
Summary: glib static
Requires: %{name}-devel = %{version}-%{release}

%description static
The %{name}-static subpackage contains static libraries for %{name}.

%package tests
Summary: Tests for the glib2 package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The glib2-tests package contains tests that can be used to verify
the functionality of the installed glib2 package.

%prep
%autosetup -n glib-%{version} -p1

# For patch generation
#exit 1

# Rewrite some hardcoded paths
perl -pi -e "s|/usr/bin/python3|%{_bindir}/python3|g" gobject/tests/genmarshal.py
perl -pi -e "s|/usr/bin/python3|%{_bindir}/python3|g" gobject/tests/mkenums.py

# Ensure we're using c99 compliant compilation options
perl -pi -e "s|gnu89|gnu99|g" meson.build

%build
# Bug 1324770: Also explicitly remove PCRE sources since we use --with-pcre=system
rm glib/pcre/*.[ch]
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
export CPPFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS -I%{_includedir}/libdicl-0.1"
# Meson/ninja use ORIGIN a lot, only way to do that is explicit
# add what we need to the LD_LIBRARYN32_PATH before the build
export GLIB2_BUILD_DIR=`pwd`/mips-sgug-irix
export LD_LIBRARYN32_PATH=$GLIB2_BUILD_DIR/gobject:$GLIB2_BUILD_DIR/gmodule:$GLIB2_BUILD_DIR/gio:$GLIB2_BUILD_DIR/glib:$LD_LIBRARYN32_PATH

%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif
%meson \
    --default-library=both \
    -Dman=true \
    -Ddtrace=false \
    -Dsystemtap=false \
    -Dgtk_doc=false \
    -Dfam=false \
    -Dxattr=false \
    -Dinstalled_tests=true

#    -Ddtrace=true \
#    -Dsystemtap=true \
#    -Dfam=true \
#

%meson_build

%install
%meson_install
# Since this is a generated .py file, set it to a known timestamp for
# better reproducibility.
# Also copy the timestamp for other .py files, because meson doesn't
# do this, see https://github.com/mesonbuild/meson/issues/5027.
touch -r gio/gdbus-2.0/codegen/config.py.in %{buildroot}%{_datadir}/glib-2.0/codegen/*.py
#chrpath --delete %{buildroot}%{_libdir}/*.so

# Perform byte compilation manually to avoid issues with
# irreproducibility of the default invalidation mode, see
# https://www.python.org/dev/peps/pep-0552/ and
# https://bugzilla.redhat.com/show_bug.cgi?id=1686078
export PYTHONHASHSEED=0
%py_byte_compile %{__python3} %{buildroot}%{_datadir}

# Don't do fedora multilib stuff on IRIX
#mv  %{buildroot}%{_bindir}/gio-querymodules %{buildroot}%{_bindir}/gio-querymodules-%{__isa_bits}

mkdir -p %{buildroot}%{_libdir}/gio/modules
touch %{buildroot}%{_libdir}/gio/modules/giomodule.cache

%find_lang glib20

%transfiletriggerin -- %{_libdir}/gio/modules
#gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :
gio-querymodules %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerpostun -- %{_libdir}/gio/modules
#gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :
gio-querymodules %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerin -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%transfiletriggerpostun -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f glib20.lang
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libglib-2.0.so.*
%{_libdir}/libgthread-2.0.so.*
%{_libdir}/libgmodule-2.0.so.*
%{_libdir}/libgobject-2.0.so.*
%{_libdir}/libgio-2.0.so.*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/gapplication
%{_datadir}/bash-completion/completions/gdbus
%{_datadir}/bash-completion/completions/gio
%{_datadir}/bash-completion/completions/gsettings
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%dir %{_libdir}/gio
%dir %{_libdir}/gio/modules
%ghost %{_libdir}/gio/modules/giomodule.cache
%{_bindir}/gio
%{_bindir}/gio-launch-desktop
%{_bindir}/gio-querymodules*
%{_bindir}/glib-compile-schemas
%{_bindir}/gsettings
%{_bindir}/gdbus
%{_bindir}/gapplication
%{_mandir}/man1/gio.1*
%{_mandir}/man1/gio-querymodules.1*
%{_mandir}/man1/glib-compile-schemas.1*
%{_mandir}/man1/gsettings.1*
%{_mandir}/man1/gdbus.1*
%{_mandir}/man1/gapplication.1*

%files devel
%{_libdir}/lib*.so
%{_libdir}/glib-2.0
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/*
%{_datadir}/glib-2.0/gdb
%{_datadir}/glib-2.0/gettext
%{_datadir}/glib-2.0/schemas/gschema.dtd
%{_datadir}/glib-2.0/valgrind/glib.supp
%{_datadir}/bash-completion/completions/gresource
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gobject-query
%{_bindir}/gtester
%{_bindir}/gdbus-codegen
%{_bindir}/glib-compile-resources
%{_bindir}/gresource
%{_datadir}/glib-2.0/codegen
%attr (0755, root, root) %{_bindir}/gtester-report
%{_mandir}/man1/glib-genmarshal.1*
%{_mandir}/man1/glib-gettextize.1*
%{_mandir}/man1/glib-mkenums.1*
%{_mandir}/man1/gobject-query.1*
%{_mandir}/man1/gtester-report.1*
%{_mandir}/man1/gtester.1*
%{_mandir}/man1/gdbus-codegen.1*
%{_mandir}/man1/glib-compile-resources.1*
%{_mandir}/man1/gresource.1*
%{_datadir}/gdb/
%{_datadir}/gettext/
#%%{_datadir}/systemtap/

#%%files doc
#%%doc %%{_datadir}/gtk-doc/html/*

#%%files fam
#%%{_libdir}/gio/modules/libgiofam.so

%files static
%{_libdir}/libgio-2.0.a
%{_libdir}/libglib-2.0.a
%{_libdir}/libgmodule-2.0.a
%{_libdir}/libgobject-2.0.a
%{_libdir}/libgthread-2.0.a

%files tests
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
* Sat Sep 05 2020 Daniel Hams <daniel.hams@gmail.com> - 2.62.6-4
- Get more tests passing fixing spawn, socket bits, some other pieces

* Sun Jun 21 2020 Daniel Hams <daniel.hams@gmail.com> - 2.62.6-3
- Correct more hardcoded paths that break mime lookups, remove more fedora multi-lib-isms

* Sun May 31 2020 Daniel Hams <daniel.hams@gmail.com> - 2.62.6-2
- Bug fix - include missing rpl_isnanf replacement func

* Tue May 19 2020 Daniel Hams <daniel.hams@gmail.com> - 2.62.6-1
- Pull official fc31 version into wip

* Wed Mar 18 2020 Kalev Lember <klember@redhat.com> - 2.62.6-1
- Update to 2.62.6

* Tue Feb 18 2020 Kalev Lember <klember@redhat.com> - 2.62.5-1
- Update to 2.62.5

* Fri Feb 07 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 2.62.4-2
- Add patch for CVE-2020-6750 and related issues.
