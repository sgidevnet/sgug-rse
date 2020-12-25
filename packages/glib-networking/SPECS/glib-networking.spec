%define glib2_version 2.60.0

Name:           glib-networking
Version:        2.62.4
Release:        1%{?dist}
Summary:        Networking support for GLib

License:        LGPLv2+
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/glib-networking/2.62/%{name}-%{version}.tar.xz

# https://bugzilla.redhat.com/show_bug.cgi?id=1179295
Patch0:         fedora-crypto-policy.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  ca-certificates
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  gettext
#BuildRequires:  systemd

Requires:       ca-certificates
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains libproxy- and GSettings-based
GProxyResolver implementations and a gnutls-based GTlsConnection
implementation.

%package tests
Summary: Tests for the glib-networking package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The glib-networking-tests package contains tests that can be used to verify
the functionality of the installed glib-networking package.

%prep
%autosetup -p1

%build
%meson -Dinstalled_tests=true
%meson_build

%install
%meson_install

%find_lang %{name}

rm -f $RPM_BUILD_ROOT/usr/sgug/lib/systemd/user/glib-pacrunner.service


%files -f %{name}.lang
%license COPYING
%doc NEWS README
%{_libdir}/gio/modules/libgiolibproxy.so
%{_libdir}/gio/modules/libgiognomeproxy.so
%{_libdir}/gio/modules/libgiognutls.so
%{_libexecdir}/glib-pacrunner
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
#%%{_userunitdir}/glib-pacrunner.service

%files tests
%{_libexecdir}/installed-tests/glib-networking
%{_datadir}/installed-tests

%changelog
* Sat Sep 26 2020  HAL <notes2@gmx.de> - 2.62.4-1
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri May 29 2020 Kalev Lember <klember@redhat.com> - 2.62.4-1
- Update to 2.62.4

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 2.62.3-1
- Update to 2.62.3

* Mon Dec 09 2019 Kalev Lember <klember@redhat.com> - 2.62.2-1
- Update to 2.62.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 2.62.1-1
- Update to 2.62.1

* Sat Sep 07 2019 Kalev Lember <klember@redhat.com> - 2.62.0-1
- Update to 2.62.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 2.61.92-1
- Update to 2.61.92

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 2.61.90-1
- Update to 2.61.90

* Mon Aug  5 2019 Owen Taylor <otaylor@redhat.com> - 2.61.2-1
- Update to 2.61.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.61.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Kalev Lember <klember@redhat.com> - 2.61.1-1
- Update to 2.61.1

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 2.60.2-1
- Update to 2.60.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.60.1-2
- Rebuild with Meson fix for #1699099

* Tue Apr 02 2019 Kalev Lember <klember@redhat.com> - 2.60.1-1
- Update to 2.60.1

* Wed Mar 13 2019 Kalev Lember <klember@redhat.com> - 2.60.0.1-1
- Update to 2.60.0.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 2.60.0-1
- Update to 2.60.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 2.59.92-1
- Update to 2.59.92

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 2.59.91-1
- Update to 2.59.91

* Tue Feb 05 2019 Kalev Lember <klember@redhat.com> - 2.59.90-1
- Update to 2.59.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Kalev Lember <klember@redhat.com> - 2.59.2-1
- Update to 2.59.2

* Tue Nov 20 2018 Dan Winship <danw@redhat.com> - 2.58.0-3
- Remove Fedora-only conditional on the crypto policy patch

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 2.58.0-2
- Rebuilt for GNOME 3.30.0 megaupdate

* Sun Sep 02 2018 Michael Catanzaro <mcatanzaro@igalia.com> - 2.58.0-1
- Update to 2.58.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 2.57.90-1
- Update to 2.57.90

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.56.1-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Kalev Lember <klember@redhat.com> - 2.56.1-1
- Update to 2.56.1

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 2.56.0-1
- Update to 2.56.0

* Wed Feb 28 2018 Michael Catanzaro <mcatanzaro@igalia.com> - 2.55.90-1
- Update to 2.55.90

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.55.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 2.55.2-1
- Update to 2.55.2
- Switch to the meson build system

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 2.54.1-1
- Update to 2.54.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 2.54.0-1
- Update to 2.54.0

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 2.53.90-1
- Update to 2.53.90
- Rebase fedora-crypto-policy.patch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 2.50.0-1
- Update to 2.50.0
- Don't set group tags

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 2.49.90-1
- Update to 2.49.90

* Tue Jul  5 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.48.2-3
- Remove scriptlets handled by glib2's file triggers

* Wed Jun 15 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 2.48.2-2
- Comply with Fedora system-wide crypto policy

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 2.48.2-1
- Update to 2.48.2

* Thu Apr 28 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 2.48.1-1
- Update to 2.48.1
- Add patch for GNOME #765317

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 2.48.0-1
- Update to 2.48.0

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 2.47.90-1
- Update to 2.47.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 2.47.1-1
- Update to 2.47.1

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 2.46.0-1
- Update to 2.46.0
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Kalev Lember <kalevlember@gmail.com> - 2.45.1-1
- Update to 2.45.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.0-1
- Update to 2.44.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 2.43.92-1
- Update to 2.43.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 2.43.91-1
- Update to 2.43.91
- Use the %%license macro for the COPYING file

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 2.43.1-1
- Update to 2.43.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.42.0-1
- Update to 2.42.0

* Mon Sep 15 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.92-1
- Update to 2.41.92

* Thu Sep  4 2014 Vadim Rutkovsky <vrutkovs@redhat.com> - 2.41.4-3
- Build installed tests

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.41.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.4-1
- Update to 2.41.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 2.41.3-1
- Update to 2.41.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 2.40.1-1
- Update to 2.40.1

* Sat Apr 05 2014 Kalev Lember <kalevlember@gmail.com> - 2.40.0-2
- Update dep versions

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 2.40.0-1
- Update to 2.40.0

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 2.39.90-1
- Update to 2.39.90

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 2.39.3-1
- Update to 2.39.3

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 2.39.1-1
- Update to 2.39.1

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 2.38.2-1
- Update to 2.38.2

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 2.38.1-1
- Update to 2.38.1

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 2.38.0-1
- Update to 2.38.0

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.5-1
- Update to 2.37.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.2-1
- Update to 2.37.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.1-1
- Update to 2.37.1

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 2.36.1-1
- Update to 2.36.1

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.36.0-1
- Update to 2.36.0

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 2.35.9-1
- Update to 2.35.9

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 2.35.8-1
- Update to 2.35.8

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 2.35.6-1
- Update to 2.35.6

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 2.35.4-1
- Update to 2.35.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.35.3-1
- Update to 2.35.3

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.35.1-1
- Update to 2.35.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 2.34.0-1
- Update to 2.34.0

* Tue Sep 18 2012 Kalev Lember <kalevlember@gmail.com> - 2.33.14-1
- Update to 2.33.14

* Wed Sep  5 2012 Debarshi Ray <rishi@fedoraproject.org> - 2.33.12-1
- Update to 2.33.12

* Mon Sep  3 2012 Matthias Clasen <mclasen@redhat.com> - 2.33.10-1
- Update to 2.33.10

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Richard Hughes <hughsient@gmail.com> - 2.33.3-1
- Update to 2.33.3

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 2.33.2-1
- Update to 2.33.2
- Use --disable-static instead of removing built static libs in %%install

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 2.32.1-1
- Update to 2.32.1

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 2.32.0-1
- Update to 2.32.0

* Tue Mar 27 2012 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Mar 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.31.22-1
- Update to 2.31.22

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 2.31.20-1
- Update to 2.31.20

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 2.31.16-1
- Update to 2.31.16

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 2.31.6
- Update to 2.31.6

* Mon Nov 21 2011 Matthias Clasen <mclasen@redhat.com> - 2.31.2
- Update to 2.31.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.31.0
- Update to 2.31.0

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.1-2
- Rebuilt for glibc bug#747377

* Mon Oct 17 2011 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Sep 19 2011 Matthias Clasen <mclasen@redhat.com> 2.29.92-1
- Update to 2.29.92

* Tue Jul 05 2011 Bastien Nocera <bnocera@redhat.com> 2.29.9-1
- Update to 2.29.9

* Wed Apr 27 2011 Dan Winship <danw@redhat.com> - 2.28.6.1-2
- Require gsettings-desktop-schemas, for GNOME proxy support

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.6.1-1
- Update to 2.28.6.1

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.6-1
- Update to 2.28.6

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.5-1
- Update to 2.28.5

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.4-1
- Update to 2.28.4

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Dan Winship <danw@redhat.com> - 2.27.90-1
- Update to 2.27.90, including TLS support

* Mon Nov  1 2010 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Thu Oct  7 2010 Matthias Clasen <mclasen@redhat.com> - 2.25.0-1
- Initial packaging
