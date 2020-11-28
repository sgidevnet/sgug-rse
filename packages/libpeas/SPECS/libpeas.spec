%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

%global apiver 1.0

Name:           libpeas
Version:        1.24.1
Release:        3%{?dist}
Summary:        Plug-ins implementation convenience library

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Libpeas
Source0:        https://download.gnome.org/sources/%{name}/1.24/%{name}-%{version}.tar.xz

Patch100:       libpeas.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  gettext
#BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
#BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel

%description
libpeas is a convenience library making adding plug-ins support
to glib-based applications.

%package gtk
Summary:        GTK+ plug-ins support for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gtk
libpeas-gtk is a convenience library making adding plug-ins support
to GTK+-based applications.

%package loader-python3
Summary:        Python 3 loader for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject

Obsoletes: libpeas-loader-python < %{version}-%{release}
Provides: libpeas-loader-python = %{version}-%{release}

%description loader-python3
This package contains the Python 3 loader that is needed to
run Python 3 plugins that use libpeas.

%package devel
Summary:        Development files for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk%{?_isa} = %{version}-%{release}

%description devel
This package contains development libraries and header files
that are needed to write applications that use libpeas.

%prep
%autosetup -p1

# A place to generate sgug patch
#exit 1

# Create a shell script that can be used to set the right environment
# for running/debugging the tests
export BUILD_DIR=`pwd`/mips-sgug-irix
%define build_dir $BUILD_DIR
cat << EOF >>testlibpeas_setupenv.sh
#!%{_bindir}/bash
export LD_LIBRARYN32_PATH=%{build_dir}/libpeas:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/libpeas-gtk:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/loaders/python3:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/testing-util:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/libpeas/introspection:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/libpeas/testing:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/libpeas/plugins/embedded:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/libpeas/plugins/extension-c:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/libpeas-gtk/testing:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/libpeas-gtk/plugins/builtin-configurable:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/libpeas-gtk/plugins/configurable:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/plugins/builtin:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/plugins/has-dep:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/plugins/loadable:\$LD_LIBRARYN32_PATH
export LD_LIBRARYN32_PATH=%{build_dir}/tests/plugins/self-dep:\$LD_LIBRARYN32_PATH
cd %{build_dir}
ninja tests/libpeas/introspection/Introspection-1.0.typelib
meson test
EOF
chmod u+x ./testlibpeas_setupenv.sh

%build
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -Og"
export LDFLAGS="-ldicl-0.1 -Wl,-z,relro -Wl,-z,now"
%else
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif
export CXXFLAGS="$CFLAGS"
%meson \
  -Ddemos=false \
  -Dvapi=true \
  -Dgtk_doc=true \
  -Dintrospection=true

%meson_build

%check
cd mips-sgug-irix
../testlibpeas_setupenv.sh

%install
%meson_install

%find_lang libpeas-1.0

#%%ldconfig_scriptlets

%files -f libpeas-1.0.lang
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/libpeas-%{apiver}.so.0*
%dir %{_libdir}/libpeas-%{apiver}/
%dir %{_libdir}/libpeas-%{apiver}/loaders
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Peas-%{apiver}.typelib
%{_datadir}/icons/hicolor/*/actions/libpeas-plugin.*

%files gtk
%{_libdir}/libpeas-gtk-%{apiver}.so.0*
%{_libdir}/girepository-1.0/PeasGtk-%{apiver}.typelib

%files loader-python3
%{_libdir}/libpeas-%{apiver}/loaders/libpython3loader.so

%files devel
%{_includedir}/libpeas-%{apiver}/
#%%dir %%{_datadir}/gtk-doc/
#%%dir %%{_datadir}/gtk-doc/html/
#%%{_datadir}/gtk-doc/html/libpeas/
%{_libdir}/libpeas-%{apiver}.so
%{_libdir}/libpeas-gtk-%{apiver}.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Peas-%{apiver}.gir
%{_datadir}/gir-1.0/PeasGtk-%{apiver}.gir
%{_libdir}/pkgconfig/libpeas-%{apiver}.pc
%{_libdir}/pkgconfig/libpeas-gtk-%{apiver}.pc
#%%{_datadir}/glade/catalogs/libpeas-gtk.xml

%changelog
* Sat Nov 28 2020 Daniel Hams <daniel.hams@gmail.com> - 1.24.1-3
- Now we have gtk3 + gtkdoc, ensure the new files are taken into account

* Sat Nov 22 2020 Daniel Hams <daniel.hams@gmail.com> - 1.24.1-2
- Getting tests launching and some (not all) passing.

* Thu Oct 31 2019 Kalev Lember <klember@redhat.com> - 1.24.1-1
- Update to 1.24.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 1.24.0-1
- Update to 1.24.0

* Thu Sep 05 2019 Kalev Lember <klember@redhat.com> - 1.23.92-1
- Update to 1.23.92

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 1.23.90.1-2
- Revert inadvertent soname bump
- Tighten spec file globs to avoid accidental soname bumps in the future

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 1.23.90.1-1
- Update to 1.23.90.1
- Switch to the meson build system

* Thu Aug 01 2019 Bastien Nocera <bnocera@redhat.com> - 1.22.0-13
+ libpeas-1.22.0-13
- Force disable the Python2 loader, which could still be built by accident (#1736043)
