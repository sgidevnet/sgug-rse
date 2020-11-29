Name:           four-in-a-row
Version:        3.34.1
Release:        1%{?dist}
Summary:        GNOME Four-in-a-row game

License:        GPLv2+ and GFDL and GPLv3+
URL:            https://wiki.gnome.org/Apps/Four-in-a-row
Source0:        https://download.gnome.org/sources/four-in-a-row/3.34/four-in-a-row-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  gtk3-devel >= 3.13.2
BuildRequires:  gsound-devel
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  zlib-devel
BuildRequires:  vala


%description
The objective of Four-in-a-row is to build a line of four of your marbles
while trying to stop your opponent (human or computer) building a line
of his or her own.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --all-name --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Four-in-a-row.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/four-in-a-row
%{_datadir}/metainfo/org.gnome.Four-in-a-row.appdata.xml
%{_datadir}/applications/org.gnome.Four-in-a-row.desktop
%{_datadir}/four-in-a-row
%{_datadir}/glib-2.0/schemas/org.gnome.Four-in-a-row.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Four-in-a-row*
%{_mandir}/man6/four-in-a-row.6*


%changelog
* Sun Nov 29 2020  HAL <notes2@gmx.de> - 3.34.1-1
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Tue Aug  6 2019 Yanko Kaneti <yaneti@declera.com> - 3.33.90-1
- Update to 3.33.90. BR: libcanberra -> gsound

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Mar  4 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb  5 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.90-1
- Update to 3.31.90
- Switch to meson and vala
- Appplication ID change to org.gnome.Four-in-a-row

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Yanko Kaneti <yaneti@declera.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.90-1
- Update to 3.27.90

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.22.2-2
- Remove obsolete scriptlets

* Sat Sep  9 2017 Yanko Kaneti <yaneti@declera.com> - 3.22.2-1
- Update to 3.22.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov  8 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.1-1
- Update to 3.22.0

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section
- Use make_install macro

* Sat May  7 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.1-1
- Update to 3.20.1

* Mon Mar 21 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.0-1
- Update to 3.20.0

* Mon Feb 29 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.91-1
- Update to 3.19.91

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov  8 2015 Yanko Kaneti <yaneti@declera.com> - 3.18.2-1
- Update to 3.18.2

* Sun Oct 11 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sun Sep 13 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.92-1
- Update to 3.17.92

* Thu Aug 13 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.2-1
- Update to 3.16.2
- No more separate HighContrast icons

* Mon Apr 13 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro

* Mon Feb 16 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.90-1
- Update to 3.15.90

* Mon Oct 27 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.1-1
- First devlopment release from the 3.16 cycle

* Fri Oct 10 2014 Yanko Kaneti <yaneti@declera.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.92-1
- Update to 3.13.92

* Tue Aug 19 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.4-1
- Update to 3.13.4

* Tue Jun 24 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.3-1
- First devlopment release from the 3.14 cycle

* Tue Jun 17 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.3-1
- Update to 3.12.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.2-1
- Update to 3.12.2

* Mon Apr 14 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.0-1
- Update to 3.12.0

* Sun Mar 16 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.92-1
- Update to 3.11.92

* Mon Feb 17 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.90-1
- Update to 3.11.90. Add license for the new theme.

* Mon Dec 16 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.3-1
- Update to 3.11.3. New url.

* Sat Oct 12 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.1-1
- Update to 3.10.1

* Mon Sep 23 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 17 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.92-1
- Update to 3.9.92
- Add appdata.

* Tue Aug 20 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-2
- Obsolete gnome-games-extra (for upgrades from f17)

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Yanko Kaneti <yaneti@declera.com> - 3.8.0-1
- Update to 3.8.0
- Drop po patch

* Tue Mar 19 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.92-1
- Update to 3.7.92

* Wed Mar  6 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.90-1
- Initial packaging of standalone four-in-a-row
