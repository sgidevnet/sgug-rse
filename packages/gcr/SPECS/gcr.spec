#%%ifarch %%{valgrind_arches}
#%%global has_valgrind 1
#%%endif
%global has_valgrind 0

Name:           gcr
Version:        3.34.0
Release:        1%{?dist}
Summary:        A library for bits of crypto UI and parsing

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/CryptoGlue
Source0:        https://download.gnome.org/sources/%{name}/3.34/%{name}-%{version}.tar.xz
Patch100:       gcr.sgifixes.patch

BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
#BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(p11-kit-1)
#BuildRequires:  chrpath
BuildRequires:  docbook-style-xsl
BuildRequires:  libgcrypt-devel
BuildRequires:  desktop-file-utils
#BuildRequires:  intltool
BuildRequires:  vala
%if 0%{?has_valgrind}
BuildRequires:  valgrind-devel
%endif
BuildRequires:  %{_bindir}/gpg2
BuildRequires:  %{_bindir}/valac
BuildRequires:  %{_bindir}/xsltproc
Requires: %{name}-base%{?_isa} = %{version}-%{release}

%description
gcr is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides a viewer for crypto files on the GNOME
desktop.

gck is a library for accessing PKCS#11 modules like smart cards.

%package devel
Summary: Development files for gcr
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The gcr-devel package includes the header files for the gcr library.

%package base
Summary: Library files for gcr
Conflicts: %{name} < 3.28.1-3

%description base
The gcr-base package includes the gcr-base library.

%prep
%autosetup -p1

# Use system valgrind headers instead
%if 0%{?has_valgrind}
rm -rf build/valgrind/
%endif

# A place to generate the irix patch
#exit 1

# Rewrite some hardcoded paths to allow running tests
perl -pi -e "s|/usr/bin/python|%{_bindir}/python|g" build/tap-driver
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" build/tap-gtester

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%configure --enable-introspection --disable-gtk-doc --without-gtk --enable-valgrind=no
%make_build


%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libmock-test-module.*
%find_lang %{name}

#chrpath --delete $RPM_BUILD_ROOT%%{_libdir}/lib*.so.*
#chrpath --delete $RPM_BUILD_ROOT%%{_bindir}/gcr-viewer
#chrpath --delete $RPM_BUILD_ROOT%%{_libexecdir}/gcr-prompter


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gcr-viewer.desktop


%files -f %{name}.lang
%doc README NEWS
%license COPYING
#%%{_bindir}/gcr-viewer
#%%{_datadir}/applications/gcr-viewer.desktop
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp.convert
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
%{_datadir}/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml
%{_libdir}/girepository-1.0
#%%{_libdir}/libgcr-3.so.*
#%%{_libdir}/libgcr-ui-3.so.*
#%%{_datadir}/icons/hicolor/*/apps/*
#%%{_datadir}/mime/packages/gcr-crypto-types.xml
#%%{_libexecdir}/gcr-prompter
%{_libexecdir}/gcr-ssh-askpass
%{_datadir}/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
%{_datadir}/dbus-1/services/org.gnome.keyring.SystemPrompter.service
#%%{_datadir}/applications/gcr-prompter.desktop

%files devel
%{_includedir}/gck-1
%{_includedir}/gcr-3
%{_libdir}/libgck-1.so
#%%{_libdir}/libgcr-3.so
%{_libdir}/libgcr-base-3.so
#%%{_libdir}/libgcr-ui-3.so
%{_libdir}/pkgconfig/gck-1.pc
#%%{_libdir}/pkgconfig/gcr-3.pc
%{_libdir}/pkgconfig/gcr-base-3.pc
#%%{_libdir}/pkgconfig/gcr-ui-3.pc
%{_datadir}/gir-1.0
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gck
%{_datadir}/gtk-doc/html/gcr-3
%{_datadir}/vala/

%files base
%{_libdir}/libgck-1.so.*
%{_libdir}/libgcr-base-3.so.*

%changelog
* Sun Nov 08 2020 Daniel Hams <daniel.hams@gmail.com> - 3.34.0-1
- Import into sgugrse

* Mon Oct 14 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Dan Horák <dan[at]danny.cz> - 3.28.1-4
- fix gcr-prompter crash (rhbz#1631759)
