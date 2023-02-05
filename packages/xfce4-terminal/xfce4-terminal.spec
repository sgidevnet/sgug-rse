%global minorversion 0.8
%global xfceversion 4.13

Name:           xfce4-terminal
Version:        0.8.9.1
Release:        1%{?dist}
Summary:        Terminal Emulator for the Xfce Desktop environment

License:        GPLv2+
URL:            http://docs.xfce.org/apps/terminal/start
Source0:        http://archive.xfce.org/src/apps/xfce4-terminal/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  vte291-devel >= 0.38
BuildRequires:  gtk3-devel >= 3.14.0
BuildRequires:  glib2-devel >= 2.26.0

BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
# required for Terminal-default-apps.xml (only works in late GNOME 2)
%{?el6:Requires: control-center-filesystem}
# require a small monospace font
#Requires:       dejavu-sans-mono-fonts
# This package replaces the Terminal package
Provides: Terminal = %{version}-%{release}
Obsoletes: Terminal < 0.4.8-5

%description
Xfce4-terminal is a lightweight and easy to use terminal emulator application 
with many advanced features including drop down, tabs, unlimited scrolling, 
full colors, fonts, transparent backgrounds, and more.

%prep
%setup -q

%build
export CFLAGS="-Wno-error -I/usr/sgug/include/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -liconv"
autoreconf -i --force
automake --add-missing
%configure
%make_build

%install
%make_install

%find_lang %{name}
desktop-file-install                                       \
  --delete-original                                        \
  --add-category="GTK"                                     \
  --dir=%{buildroot}%{_datadir}/applications          \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install                                       \
  --delete-original                                        \
  --add-category="GTK"                                     \
  --dir=%{buildroot}%{_datadir}/applications          \
  %{buildroot}%{_datadir}/applications/%{name}-settings.desktop

%{!?el6:rm -rf %{buildroot}%{_datadir}/gnome-control-center/}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc README ChangeLog NEWS AUTHORS HACKING THANKS
%{_bindir}/xfce4-terminal
%{_datadir}/xfce4/terminal
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{?el6:%{_datadir}/gnome-control-center/default-apps/xfce4-terminal-default-apps.xml}
%{_mandir}/man1/xfce4-terminal.1.*

%changelog
* Sat Dec 28 2019 Kevin Fenzi <kevin@scrye.com> - 0.8.9.1-1
- Update to 0.8.9.1.

* Fri Dec 27 2019 Kevin Fenzi <kevin@scrye.com> - 0.8.9-1
- Update to 0.8.9. Fixes bug #1786824

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.8-1
- Update to 0.8.8

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.4-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.4-2
- Add xfce4-terminal-settings desktop file

* Tue May 15 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.4-1
- Update to 0.8.7.4

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.3-2
- Fix build issues (el6 line)

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.3-1
- Update to 0.8.7.3 (bugfix release)
- Drop upstreamed patch

* Mon Mar 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.2-3
- Add patch to fix drop-down flickering

* Thu Mar 15 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.2-2
- Add BR:gcc-c++

* Thu Mar 15 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.2-1
- Update to 0.8.7.2

* Mon Feb 26 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7.1-1
- Update to 0.8.7.1

* Sun Feb 25 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.7-1
- Update to 0.8.7
- Modernize specfile

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.8.6-1
- Update to 0.8.6. Fixes bug #1471447

* Sun May 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.5.1-1
- Update to 0.8.5.1
- Bug fix for 0.8.5

* Sun May 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5

* Mon Feb 06 2017 Kevin Fenzi <kevin@scrye.com> - 0.8.4-1
- Update to 0.8.4.

* Mon Jan 16 2017 Kevin Fenzi <kevin@scrye.com> - 0.8.3-2
- Improve Summary and description. Fixes bug #1412956

* Tue Jan 10 2017 Kevin Fenzi <kevin@scrye.com> - 0.8.3-1
- Update to 0.8.3

* Fri Dec 30 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2
- Drop upstreamed patches

* Mon Nov 21 2016 Dan Horák <dan[at]danny.cz> - 0.8.1-2
- fix Alt+<Num> handling

* Mon Oct 31 2016 Kevin Fenzi <kevin@scrye.com> - 0.8.1-1
- Update to 0.8.1

* Mon Oct 17 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Tue Sep 06 2016 Kevin Fenzi <kevin@scrye.com> - 0.6.92-1
- Update to 0.6.92. Fixes various bugs.

* Wed Aug 31 2016 Kevin Fenzi <kevin@scrye.com> - 0.6.91-1
- Update to 0.6.91. Fixes bugs #1369594 and #1369939

* Fri Jul 29 2016 Kevin Fenzi <kevin@scrye.com> - 0.6.90-1
- Update to 0.6.90. Fixes bug #1361560

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.6.3-7
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.6.3-6
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Oct 05 2014 Kevin Fenzi <kevin@scrye.com> 0.6.3-5
- Add dejavu-sans-mono-fonts as required. Works around bug #718121

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Mukundan Ragavan <nonamedotc@gmail.com> - 0.6.3-3
- Initial build for EPEL-7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Kevin Fenzi <kevin@scrye.com> 0.6.3-1
- Update to 0.6.3
- Drop unstreamed patches. 

* Mon Dec 23 2013 Kevin Fenzi <kevin@scrye.com> 0.6.2-4
- Add patch to fix crash in locale menu. Fixes bug #1015850

* Mon Dec 16 2013 Kevin Fenzi <kevin@scrye.com> 0.6.2-3
- Add patch to fix save/restore of terminal positions

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 05 2013 Kevin Fenzi <kevin@scrye.com> 0.6.2-1
- Update to 0.6.2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 01 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
- Install GNOME control-center integration only on EL6

* Fri Dec 28 2012 Kevin Fenzi <kevin@scrye.com> 0.6.0-2
- Various minor moderizations of the spec per the review. 

* Thu Dec 27 2012 Kevin Fenzi <kevin@scrye.com> 0.6.0-1
- Rename Terminal to xfce4-terminal
- Update to 0.6.0 upstream.

* Wed Apr 04 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.8-3
- Update for Xfce 4.10

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Kevin Fenzi <kevin@scrye.com> - 0.4.8-1
- Update to 0.4.8

* Tue Apr 05 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.7-1
- Update to 0.4.7
- Remove upstreamed background.patch

* Sun Jan 30 2011 Kevin Fenzi <kevin@tummy.com> - 0.4.6-2
- Add patch to fix cpu and memory issues. 

* Sun Jan 30 2011 Kevin Fenzi <kevin@tummy.com> - 0.4.6-1
- Update to 0.4.6

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-3
- Rebuild for libfxce4gui 4.7.0

* Thu Sep 09 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-2
- Fix build error with vte >= 0.25.90 (#631447,bugzilla.xfce.org #6686)

* Fri May 21 2010 Kevin Fenzi <kevin@tummy.com> - 0.4.5-1
- Update to 0.4.5

* Mon Feb 01 2010 Kevin Fenzi <kevin@tummy.com> - 0.4.4-1
- Update to 0.4.4

* Thu Dec 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Thu Oct 08 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-2
- Fix locale problems in the UI (bugzilla.xfce.org #5842)

* Tue Oct 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2
- Update icon cache scriptlets

* Thu Oct 01 2009 Kevin Fenzi <kevin@tummy.com> - 0.4.1-1
- Update to 0.4.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- Use desktop-file-install

* Sun Jul 19 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.99.1-1
- Update to 0.2.99.1

* Wed Apr 29 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.12-3
- Fix patch fuzz

* Tue Apr 28 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.12-2
- Add patch for MiscAlwaysShowTabs segfault (fixes bug 502135)

* Sun Apr 19 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.12-1
- Update to 0.2.12

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.8.3-1
- Update to 0.2.8.3
- BuildRequire intltool
- Fix rpm group

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 0.2.8-3
- Rebuild for gcc43

* Mon Dec  3 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.8-2
- Remove no longer shipped .ui file. 

* Sun Dec  2 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.8-1
- Update to 0.2.8
- Drop unneeded patch. 

* Tue Aug 14 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.6-3
- Add patch for CVE-2007-3770. 
- Update License tag

* Sat Mar 24 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.6-2
- Fix unowned directories (#233787)

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.6-1
- Upgrade to 0.2.6

* Thu Nov 16 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.8-0.2.rc2
- Add startup-notification-devel and dbus-glib-devel to BuildRequires

* Fri Nov 10 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.8-0.1.rc2
- Update to 0.2.5.8rc2

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.6-0.4.rc1
- Added gtk-update-icon-cache to post/postun

* Wed Oct  4 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.6-0.3.rc1
- Bump release for devel checkin

* Thu Sep  7 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.6-0.2.rc1
- Bump release for xfce rc repo

* Sun Sep  3 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.6-0.1.rc1
- Upgrade to 0.2.5.6-0.1.rc1

* Sun Aug 13 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.4-0.2.beta2
- Bump release for 4.4 beta repo

* Wed Aug  2 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.4-0.1.beta2
- Fix release

* Wed Jul 12 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.4-0.beta2
- Update to 0.2.5.4-0.beta2

* Fri Jun 23 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.5.1-0.beta1.fc6
- Update to 0.2.5.1-0.beta1

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.4-6.fc5
- Rebuild for fc5

* Wed Aug 17 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.4-5.fc5
- Rebuild for new libcairo and libpixman

* Thu Aug  4 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.4-4.fc5
- Add dist tag

* Mon May 30 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.4-3
- Removed incorrect Requires
- Changed the description text

* Fri May 27 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.4-2
- Fix group to be User Interface/X

* Sat Mar 19 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.4-1
- Upgraded to 0.2.4 version
- Added Terminal/apps desktops files. 

* Tue Mar  8 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.2-2
- Fixed to use %%find_lang
- Removed generic INSTALL from %%doc
- Change description wording: "makes it" to "make it"
- Fixed to include terminal.css 

* Sun Mar  6 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.2-1
- Inital Fedora Extras version
