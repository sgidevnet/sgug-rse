Name:           gnome-taquin
Version:        3.34.4
Release:        1%{?dist}
Summary:        Sliding-block puzzle game

License:        GPLv3+ and GPLv2+ and CC-BY-SA 
URL:            https://wiki.gnome.org/Apps/Taquin
Source0:        https://download.gnome.org/sources/gnome-taquin/3.34/gnome-taquin-%{version}.tar.xz

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(gsound)

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala


%description
Taquin is a computer version of the 15-puzzle and other sliding puzzles.
The object of Taquin is to move tiles so that they reach their places, 
either indicated with numbers, or with parts of a great image.

%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Taquin.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS
%license COPYING COPYING.sounds COPYING.themes
%{_bindir}/gnome-taquin
%{_datadir}/applications/org.gnome.Taquin.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Taquin.gschema.xml
%{_datadir}/gnome-taquin
%{_datadir}/icons/*/*/apps/org.gnome.Taquin*
%{_datadir}/metainfo/org.gnome.Taquin.appdata.xml
%{_mandir}/man6/gnome-taquin.6.*


%changelog
* Sat Nov 28 2020  HAL <notes2@gmx.de> - 3.34.4-1
- first commit, compiles on Irix 6.5 with sgug-rse gcc 9.2.
  works nicely, but can be revisited to fix dbus-path issues. 

* Fri Feb 14 2020 Yanko Kaneti <yaneti@declera.com> - 3.34.4-1
- Update to 3.34.4

* Mon Jan  6 2020 Yanko Kaneti <yaneti@declera.com> - 3.34.3-1
- Update to 3.34.3

* Sat Nov 23 2019 Yanko Kaneti <yaneti@declera.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Mon Aug  5 2019 Yanko Kaneti <yaneti@declera.com> - 3.33.90-1
- Update to 3.33.90. BR: libcanberra -> gsound

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Yanko Kaneti <yaneti@declera.com> - 3.33.4-1
- Update to 3.33.4

* Tue Mar 12 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Tue Feb  5 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.90-1
- Update to 3.31.90
- Switch to meson
- Application ID change to org.gnome.Taquin

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  8 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.4-1
- Update to 3.31.4

* Tue Sep  4 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-1
- Update to 3.30.0

* Sat Jul 14 2018 Yanko Kaneti <yaneti@declera.com> - 3.28.0-3
- BR: gcc - https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Sun Oct  1 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.1-1
- Update to 3.26.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 30 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.91-1
- Update to 3.21.91

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Thu Apr 14 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.1-1
- Update to 3.20.1

* Mon Mar 21 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.92-1
- Update to 3.19.92

* Tue Mar 1 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.91-1
- Update to 3.19.91

* Wed Feb 17 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Yanko Kaneti <yaneti@declera.com> - 3.19.1
- First release on the next development branch

* Thu Oct 15 2015 Kalev Lember <klember@redhat.com> - 3.18.1.1-1
- Update to 3.18.1.1

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.92-1
- Update to 3.17.92

* Tue Sep  1 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.91-1
- Update to 3.17.91

* Tue Aug 18 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.1-1
- New development release

* Mon Apr 13 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.1-1
- Update to 3.16.1
- No more separate HighContrast icons

* Mon Mar 23 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar  2 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.91.1-1
- Update to 3.15.91.1

* Tue Feb 17 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.90-1
- Update to 3.15.90

* Tue Jan 20 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.4-1
- Update to 3.15.4

* Thu Jan 15 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.3-1
- Packaging attempt
