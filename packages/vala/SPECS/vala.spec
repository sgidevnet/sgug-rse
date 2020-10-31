%global api_ver 0.46
%global priority 90

Name:           vala
Version:        0.46.10
Release:        2%{?dist}
Summary:        A modern programming language for GNOME

# Most files are LGPLv2.1+, curses.vapi is 2-clause BSD
License:        LGPLv2+ and BSD
URL:            https://wiki.gnome.org/Projects/Vala
Source0:        https://download.gnome.org/sources/vala/0.46/vala-%{version}.tar.xz

BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz-devel
BuildRequires:  libxslt
# only if Vala source files are patched
#BuildRequires:  vala

# for tests
#BuildRequires:  dbus-x11

# alternatives; remove in F32
%global vala_binaries vala valac vala-gen-introspect vapigen
%global vala_manpages valac vala-gen-introspect vapigen
Requires(pre): %{_sbindir}/alternatives

Requires: libvala%{?_isa} = %{version}-%{release}

# For GLib-2.0 and GObject-2.0 .gir files
Requires: gobject-introspection-devel

# Removed in F25
Obsoletes: vala-tools < 0.34.0
Conflicts: vala-tools < 0.34.0
Provides: vala-tools = %{version}-%{release}

Provides: vala(api) = %{api_ver}

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code. It's also planned to generate GIDL files when gobject-
introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.


%package -n     libvala
Summary:        Vala compiler library

%description -n libvala
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains the shared libvala library.


%package -n     libvala-devel
Summary:        Development files for libvala
Requires:       libvala%{?_isa} = %{version}-%{release}
# Renamed in F30
Provides:       vala-devel = %{version}-%{release}
Provides:       vala-devel%{?_isa} = %{version}-%{release}
Obsoletes:      vala-devel < 0.43

%description -n libvala-devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files for libvala. This is not
necessary for using the %{name} compiler.


%package        doc
Summary:        Documentation for %{name}
License:        LGPLv2+

BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
#Requires:       devhelp

%description    doc
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains documentation in a devhelp HTML book.


%package -n     valadoc
Summary:        Vala documentation generator
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n valadoc
Valadoc is a documentation generator for generating API documentation from Vala
source code.


%package -n     valadoc-devel
Summary:        Development files for valadoc
Requires:       valadoc%{?_isa} = %{version}-%{release}

%description -n valadoc-devel
Valadoc is a documentation generator for generating API documentation from Vala
source code.

The valadoc-devel package contains libraries and header files for
developing applications that use valadoc.


%prep
%autosetup -p1


%build
%configure
# Don't use rpath!
#sed -i 's|/lib /usr/lib|/lib /usr/lib /lib64 /usr/lib64|' libtool
make %{?_smp_mflags}


%install
%make_install

# own this directory for third-party *.vapi files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vala/vapi
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
make check


# Drop the pre script in F32
%pre
if [ $1 -gt 1 ] ; then
    for f in %{vala_binaries};
    do
        %{_sbindir}/alternatives --remove-all $f >& /dev/null || :
    done
    for f in %{vala_manpages};
    do
        %{_sbindir}/alternatives --remove-all $f.1.gz >& /dev/null || :
    done
fi


%files
%license COPYING
%{_bindir}/vala
%{_bindir}/vala-%{api_ver}
%{_bindir}/valac
%{_bindir}/valac-%{api_ver}
%{_bindir}/vala-gen-introspect
%{_bindir}/vala-gen-introspect-%{api_ver}
%{_bindir}/vapigen
%{_bindir}/vapigen-%{api_ver}
%{_libdir}/pkgconfig/vapigen*.pc
%{_libdir}/vala-%{api_ver}/
%{_datadir}/aclocal/vala.m4
%{_datadir}/aclocal/vapigen.m4
%{_datadir}/vala/
%{_datadir}/vala-%{api_ver}/
%{_mandir}/man1/valac.1*
%{_mandir}/man1/valac-%{api_ver}.1*
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vala-gen-introspect-%{api_ver}.1*
%{_mandir}/man1/vapigen.1*
%{_mandir}/man1/vapigen-%{api_ver}.1*

%files -n libvala
%license COPYING
%{_libdir}/libvala-%{api_ver}.so.*

%files -n libvala-devel
%{_includedir}/vala-%{api_ver}
%{_libdir}/libvala-%{api_ver}.so
%{_libdir}/pkgconfig/libvala-%{api_ver}.pc

%files doc
%doc %{_datadir}/devhelp/books/vala-%{api_ver}

%files -n valadoc
%{_bindir}/valadoc
%{_bindir}/valadoc-%{api_ver}
%{_libdir}/libvaladoc-%{api_ver}.so.0*
%{_libdir}/valadoc-%{api_ver}/
%{_datadir}/valadoc-%{api_ver}/
%{_mandir}/man1/valadoc-%{api_ver}.1*
%{_mandir}/man1/valadoc.1*

%files -n valadoc-devel
%{_includedir}/valadoc-%{api_ver}/
%{_libdir}/libvaladoc-%{api_ver}.so
%{_libdir}/pkgconfig/valadoc-%{api_ver}.pc


%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 0.46.10-2
- Rebuild for jpegturbo

* Sat Sep 26 2020  HAL <notes2@gmx.de> - 0.46.10-1
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Tue May 19 2020 Kalev Lember <klember@redhat.com> - 0.46.10-1
- Update to 0.46.10
