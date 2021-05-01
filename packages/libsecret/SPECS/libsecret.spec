%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

# first two digits of version
%global release_version %%(echo %{version} | awk -F. '{print $1"."$2}')

#%%ifarch %%{valgrind_arches}
#%%global has_valgrind 1
#%%endif

Name:           libsecret
Version:        0.19.1
Release:        1%{?dist}
Summary:        Library for storing and retrieving passwords and other secrets

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Libsecret
Source0:        https://download.gnome.org/sources/libsecret/%{release_version}/libsecret-%{version}.tar.xz

Patch100:       libsecret.sgifixes.patch

BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libgcrypt-devel >= 1.2.2
BuildRequires:  vala
#BuildRequires:  gtk-doc
BuildRequires:  libxslt-devel
BuildRequires:  docbook-style-xsl
%if 0%{?has_valgrind}
BuildRequires:  valgrind-devel
%endif

Provides:       bundled(egglib)

Recommends:     gnome-keyring

%description
libsecret is a library for storing and retrieving passwords and other secrets.
It communicates with the "Secret Service" using DBus. gnome-keyring and
KSecretService are both implementations of a Secret Service.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

# Use system valgrind headers instead
%if 0%{?has_valgrind}
rm -rf build/valgrind/
%endif

%patch100 -p1 -b .sgifixes

# A place to build the IRIX patch
#exit 1

%build
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="-g -Og"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%endif
%configure --disable-static --disable-gtk-doc

# Ensure we are using the sgug libtool
cp %{_bindir}/libtool ./

%make_build


%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%find_lang libsecret


%files -f libsecret.lang
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/secret-tool
%{_libdir}/libsecret-1.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Secret-1.typelib
%{_mandir}/man1/secret-tool.1*

%files devel
%{_includedir}/libsecret-1/
%{_libdir}/libsecret-1.so
%{_libdir}/pkgconfig/libsecret-1.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Secret-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsecret-1.deps
%{_datadir}/vala/vapi/libsecret-1.vapi
%doc %{_datadir}/gtk-doc/


%changelog
* Sun Nov 08 2020 Daniel Hams <daniel.hams@gmail.com> - 0.19.1-1
- Import into sgugrse

* Fri Sep 06 2019 Kalev Lember <klember@redhat.com> - 0.19.1-1
- Update to 0.19.1

* Fri Sep 06 2019 Kalev Lember <klember@redhat.com> - 0.19.0-2
- Recommend gnome-keyring (#1725412)

* Thu Sep 05 2019 Kalev Lember <klember@redhat.com> - 0.19.0-1
- Update to 0.19.0
