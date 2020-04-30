Summary: glib 2.59.0 (the last one not requiring meson and ninja) with onre\'s patch
Name: glib2
Version: 2.59.0
Release: 1wip%{?dist}
License: GLPv3+
URL: https://developer.gnome.org/glib/
Source: ftp://ftp.acc.umu.se/pub/gnome/sources/glib/2.59/glib-2.59.0.tar.xz

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

Patch0: glib-2.59.0-irix.patch

%description
A quick and dirty port of glib 2.59.0

%prep

%setup -q -n glib-%{version}
%patch0 -p1 -b .irix~ 

%build
# Package can fail with some incorrectly discovered cache entries
# We can get a "unique" cache by introducing a unique CPPFLAGS define
export CPPFLAGS="-DSGUG_GLIB2_UNIQ_CCACHE=1 $CPPFLAGS"
./autogen.sh
%{configure} --with-libiconv=gnu
make %{?_smp_mflags}

%check

%install

make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
rm -f $RPM_BUILD_ROOT/%{_libdir}/charset.alias # provided by some other package, identical content

%files
%{_bindir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/gio/*
%{_libdir}/glib-2.0/*
%{_libdir}/libg*
%{_prefix}/include/*
%{_prefix}/share/*