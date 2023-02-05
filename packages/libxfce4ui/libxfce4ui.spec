# Review at https://bugzilla.redhat.com/show_bug.cgi?id=554599

%global xfceversion 4.14

Name:           libxfce4ui
Version:        4.14.1
Release:        1%{?dist}
Summary:        Commonly used Xfce widgets

License:        LGPLv2+
URL:            http://xfce.org/
#VCS git:git://git.xfce.org/xfce/libxfce4ui
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

## Downstream patches
# add more keyboard shortcuts to make multimedia keyboards work out of the box
# Terminal changed to xfce4-terminal in the patch
Patch10:        libxfce4ui-%{xfceversion}-keyboard-shortcuts.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gobject-2.0) >= 2.24.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20.0
BuildRequires:  libSM-devel
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfceversion}
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.4
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
#BuildRequires:  glade3-libgladeui-devel >= 3.5.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala

#
# libxfcegui4 was depreciated in the Xfce 4.8 days.
# Finally obsolete it now in 4.12
#
Obsoletes:      libxfcegui4 < 4.10.0-9

%description
Libxfce4ui is used to share commonly used Xfce widgets among the Xfce
applications.


%package -n     xfce4-about
Summary:        Xfce 4 'About' dialog

%description -n xfce4-about
This package contains the 'About Xfce' dialog with info on the desktop
environment, it's contributors, and it's licensing.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel
Requires:       libxfce4util-devel
#Requires:       glade3-libgladeui-devel
Requires:       pkgconfig
Obsoletes:      libxfcegui4-devel < 4.10.0-9

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch10

%build
export CFLAGS="-Wno-error -I/usr/sgug/include/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -liconv"
autoreconf -i --force
automake --add-missing
%configure --disable-static

# Remove rpaths
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="/usr/sgug/lib32:/usr/lib32:/lib32:/usr/lib:/lib:./libxfce4ui/.libs"

%make_build

%install
%make_install

# fix permissions for installed libraries
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

# Move xfce4-about to the 'Documentation' category
desktop-file-install \
  --delete-original \
  --remove-category=X-Xfce-Toplevel \
  --add-category=Documentation \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/xfce4-about.desktop


%ldconfig_scriptlets


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README THANKS
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/%{name}-2.0.typelib
%{_datadir}/gir-1.0/%{name}-2.0.gir
%{_datadir}/vala/vapi/%{name}-2.deps
%{_datadir}/vala/vapi/%{name}-2.vapi

%files -n xfce4-about
%{_bindir}/xfce4-about
%{_datadir}/applications/xfce4-about.desktop
%{_datadir}/icons/hicolor/48x48/apps/xfce4-logo.png

%files devel
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/
#%{_libdir}/glade3/modules/lib*.so
#%{_datadir}/glade3/catalogs/%{name}.xml*
#%{_datadir}/glade3/pixmaps/hicolor/*/actions/*

%changelog
* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.1-1
- Update to 4.14.1

* Tue Jul 30 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 4.13.7-2
- rebuild for xfconf vala

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.7-1
- Update to 4.13.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 4.13.6-3
- rebuild for xfconf

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.6-2
- Enable gobject introspection

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.6-1
- Update to 4.13.6

* Fri May 17 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.5-1
- Update to 4.13.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.4-20
- Update to 4.13.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.1-11
- Add BR:gcc-c++

* Sun May 27 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.1-10
- Drop gtk-doc flag (fixes bug# 1582900)
- Modernize spec
- Drop all fedora version conditionals (no longer needed)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Kevin Fenzi <kevin@scrye.com> - 4.12.1-5
- Drop control-alt-del for logout shortcut. Fixes bug #1229218

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Kevin Fenzi <kevin@scrye.com> 4.12.1-2
- Obsolete libxfcegui4.
- Drop amixer for volume buttons should be handled by xfce4-pulseaudio-plugin now.
- Fixes bug #1211313

* Sun Mar 15 2015 Kevin Fenzi <kevin@scrye.com> 4.12.1-1
- Update to 4.12.1 with various bugfixes.

* Sun Mar 1 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-2
- Add shortcuts patch

* Sat Feb 28 2015 Mukundan Ragavan <noamedotc@fedoraproject.org> - 4.12.0-1
- Update to latest stable release 4.12.0
- Remove upstreamed patches
- Built with GTK3 enabled
- change Terminal to xfce4-terminal in shortcuts patch

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 4.10.0-14
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.10.0-11
- patch to fix bug #1095362
- patch13 - enable-shortcut.patch

* Fri May 16 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.10.0-10
- Add patches to fix bug #1095362
- Patch11 - enable-shift-modifier-in-shortcut-dialog.patch
- Patch12 - enable-shift-modifier-in-shortcut-grabber.patch

* Wed Nov 06 2013 Kevin Fenzi <kevin@scrye.com> 4.10.0-9
- Add patch to fix double fork issue that prevents some apps from running from the menu. 
- Fixes bug #879922

* Wed Nov 06 2013 Kevin Fenzi <kevin@scrye.com> 4.10.0-8
- Conditionalize glade3 stuff so we can keep the same spec over branches. 

* Wed Nov 06 2013 Lubomir Rintel <lkundrak@v3.sk> - 4.10.0-7
- Re-enable glade3 module, it works now

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-4
- Don't ship xfce4-about in libxfce4ui-devel (#902537)

* Sat Oct 13 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-3
- Make a separate package for xfce4-about
- Add more keyboard shortcuts
- Move xfce4-about menu entry to 'Documentation' category

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0 final

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.2-1
- Update to 4.9.2 (Xfce 4.10pre2)

* Sun Apr 01 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.1-1
- Update to 4.9.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.1-1
- Update to 4.8.1

* Sun Dec 18 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.0-6
- Fix Control shortcuts (#768704)
- Add review # and VCS key

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.8.0-5
- Rebuild for new libpng

* Wed Mar 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.0-5
- Remove requirements for libxfcegui4-devel now that glade support was omitted

* Tue Feb 22 2011 Rakesh Pandit <rakesh@fedoraproject.org> - 4.8.0-4
- Disable glade as it still uses old API

* Tue Feb 22 2011 Rakesh Pandit <rakesh@fedoraproject.org> - 4.8.0-3
- Rebuild for new glade

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.0-1
- Update to 4.8.0 final. 

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.6-1
- Update to 4.7.6

* Mon Nov 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.5-1
- Update to 4.7.5

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4

* Sun Sep 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3
- Drop dependency on gtk-doc (#604399)

* Tue Jul 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.2-2
- Fix file conflict with libxfce4gui (#618719)

* Fri May 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Wed May 19 2010 Kevin Fenzi <kevin@tummy.com> - 4.7.1-3
- Rebuild for new glade version. 

* Tue Jan 12 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.1-2
- Fix license tag
- Build gtk-doc

* Tue Jan 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.1-1
- Initial spec file, based on libxfcegui4.spec

