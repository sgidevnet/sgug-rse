Name:           gmime30
Version:        3.2.7
Release:        1%{?dist}
Summary:        Library for creating and parsing MIME messages

# The library is LGPLv2+; various files (which we don't package)
# in examples/ and tests/ are GPLv2+.
License:        LGPLv2+
URL:            http://spruce.sourceforge.net/gmime/
Source0:        http://download.gnome.org/sources/gmime/3.2/gmime-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpgme-devel
BuildRequires:  gtk-doc
BuildRequires:  libgpg-error-devel
BuildRequires:  vala
BuildRequires:  zlib-devel

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n gmime-%{version}

%build
%configure --disable-static  --with-libiconv=native
%make_build V=1

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/libgmime-3.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GMime-3.0.typelib

%files devel
%{_libdir}/libgmime-3.0.so
%{_libdir}/pkgconfig/gmime-3.0.pc
%{_includedir}/gmime-3.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GMime-3.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gmime-3.*/
%{_datadir}/vala/

%changelog
* Fri Apr 23 2021  HAL <notes2@gmx.de> - 3.2.7-1
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.2.7-1
- Update to 3.2.7

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.2.6-1
- Update to 3.2.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Kalev Lember <klember@redhat.com> - 3.2.5-1
- Update to 3.2.5

* Fri Oct 04 2019 Kalev Lember <klember@redhat.com> - 3.2.4-1
- Update to 3.2.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Kalev Lember <klember@redhat.com> - 3.2.3-1
- Update to 3.2.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.2.0-1
- Update to 3.2.0
- Remove ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Kalev Lember <klember@redhat.com> - 3.0.5-1
- Update to 3.0.5

* Tue Nov 21 2017 Kalev Lember <klember@redhat.com> - 3.0.4-1
- Update to 3.0.4

* Thu Nov 02 2017 Kalev Lember <klember@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Fri Sep 08 2017 Kalev Lember <klember@redhat.com> - 3.0.2-1
- Initial Fedora packaging
