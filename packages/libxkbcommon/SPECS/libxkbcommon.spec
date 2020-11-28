#global gitdate  20120917

Name:           libxkbcommon
Version:        0.9.1
Release:        3%{?gitdate:.%{gitdate}}%{?dist}
Summary:        X.Org X11 XKB parsing library
License:        MIT
URL:            http://www.x.org

%if 0%{?gitdate}
Source0:       %{name}-%{gitdate}.tar.bz2
%else
Source0:        http://xkbcommon.org/download/%{name}-%{version}.tar.xz
%endif
Source1:        make-git-snapshot.sh

Patch01:        0001-keysym-handle-ssharp-in-XConvertCase.patch

BuildRequires:  git meson
BuildRequires:  xorg-x11-util-macros byacc flex bison
BuildRequires:  xorg-x11-proto-devel libX11-devel
BuildRequires:  xkeyboard-config-devel
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10

Requires:       xkeyboard-config

%description
%{name} is the X.Org library for compiling XKB maps into formats usable by
the X Server or other display servers.

%package devel
Summary:        X.Org X11 XKB parsing development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org X11 XKB parsing development package

%package x11
Summary:        X.Org X11 XKB keymap creation library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description x11
%{name}-x11 is the X.Org library for creating keymaps by querying the X
server.

%package x11-devel
Summary:        X.Org X11 XKB keymap creation library
Requires:       %{name}-x11%{?_isa} = %{version}-%{release}

%description x11-devel
X.Org X11 XKB keymap creation library development package

%prep

%autosetup -S git
%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1"
export LDFLAGS="-ldicl-0.1 -lc $RPM_LD_FLAGS"

%meson -Denable-docs=false \
       -Denable-wayland=false \
       -Denable-x11=true
%meson_build

%install
%meson_install

#%%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libxkbcommon.so.0.0.0
%{_libdir}/libxkbcommon.so.0

%files devel
%{_libdir}/libxkbcommon.so
%dir %{_includedir}/xkbcommon/
%{_includedir}/xkbcommon/xkbcommon.h
%{_includedir}/xkbcommon/xkbcommon-compat.h
%{_includedir}/xkbcommon/xkbcommon-compose.h
%{_includedir}/xkbcommon/xkbcommon-keysyms.h
%{_includedir}/xkbcommon/xkbcommon-names.h
%{_libdir}/pkgconfig/xkbcommon.pc

#%%ldconfig_scriptlets x11

%files x11
%{_libdir}/libxkbcommon-x11.so.0.0.0
%{_libdir}/libxkbcommon-x11.so.0

%files x11-devel
%{_libdir}/libxkbcommon-x11.so
%{_includedir}/xkbcommon/xkbcommon-x11.h
%{_libdir}/pkgconfig/xkbcommon-x11.pc

%changelog
* Fri Nov 27 2020  HAL & DH <notes2@gmx.de> - 0.9.1-3
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Dec 13 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.9.1-3
- convert ssharp to the correct uppercase letter

* Fri Nov 01 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.9.1-2
- drop the wayland-devel BR, we disable the wayland test programs

* Fri Oct 25 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.9.1-1
- libxkbcommon 0.9.1

* Mon Oct 21 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.8.4-3
- switch to meson as build system

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.8.4-1
- libxkbcommon 0.8.4

* Wed Feb 13 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.8.3-1
- libxkbcommon 0.8.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.8.2-1
- libxkbcommon 0.8.2

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.8.0-6
- Rebuild with fixed binutils

* Mon Jul 30 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.8.0-5
- Fix invalid pointer passed to FreeStmt()

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-2
- Switch to %%ldconfig_scriptlets

* Tue Dec 19 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.8.0-1
- libxkbcommon 0.8.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Hans de Goede <hdegoede@redhat.com> - 0.7.1-3
- Add patch from upstream adding XF86Keyboard and XF86RFKill keysyms

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.7.1-1
- xkbcommon 0.7.1

* Mon Nov 14 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.7.0-1
- xkbcommon 0.7.0

* Fri Jun 03 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.6.1-1
- xkbcommon 0.6.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Dan Horák <dan[at]danny.cz> - 0.5.0-3
- always build the x11 subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 22 2014 Hans de Goede <hdegoede@redhat.com> - 0.5.0-1
- Update to 0.5.0 (#1154574)

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.3-2
- Require xkeyboard-config (#1145260)

* Wed Aug 20 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.4.2-3
- make -x11 support conditional (f21+, #1000497)
- --disable-silent-rules

* Fri May 23 2014 Hans de Goede <hdegoede@redhat.com> - 0.4.2-2
- Bump release to 2 to avoid confusion with non official non scratch 0.4.2-1

* Thu May 22 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.4.2-1
- xkbcommon 0.4.2 (#1000497)
- own %%{_includedir}/xkbcommon/
- -x11: +ldconfig scriptlets
- -devel: don't include xkbcommon-x11.h
- run reautoconf in %%prep (instead of %%build)
- tighten subpkg deps via %%_isa
- .spec cleanup, remove deprecated stuff
- BR: pkgconfig(xcb-xkb) >= 1.10

* Wed Feb 05 2014 Peter Hutterer <peter.hutterer@redhat.com> 0.4.0-1
- xkbcommon 0.4.0
- Add new xkbcommon-x11 and xkbcommon-x11-devel subpackages

* Tue Aug 27 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.3.1-1
- xkbcommon 0.3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 18 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.3.0-1
- xkbcommon 0.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Adam Jackson <ajax@redhat.com> 0.2.0-1
- xkbcommon 0.2.0

* Mon Sep 17 2012 Thorsten Leemhuis <fedora@leemhuis.info> 0.1.0-8.20120917
- Today's git snapshot

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7.20120306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.1.0-6.20120306
- BuildRequire xkeyboard-config-devel to get the right XKB target path (#799717)

* Tue Mar 06 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.1.0-5.20120306
- Today's git snapshot

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4.20111109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Adam Jackson <ajax@redhat.com> 0.1.0-3
- Today's git snap

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2.20101110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 06 2010 Dave Airlie <airlied@redhat.com> 0.1.0-1.20101110
- inital import

