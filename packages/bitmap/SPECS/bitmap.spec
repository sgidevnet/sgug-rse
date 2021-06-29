Name: bitmap
Version: 1.0.8
Release: 11%{?dist}
Summary: Bitmaps editor and converter utilities for the X Window System
Url: http://www.x.org

Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1: bitmap.desktop
Source2: bitmap.png

License: MIT

# the bitmap-devel virtual provide is needed as it installs header files.
# this is currently used by lesstif package.
Provides: %{name}-devel = %{version}-%{release}

# libXaw-devel requires libXmu-devel 
# libXmu-devel requires libX11-devel, libXt-devel, xorg-x11-util-macros
BuildRequires:  gcc
BuildRequires: xorg-x11-xbitmaps libXaw-devel libXext-devel
BuildRequires: desktop-file-utils pkgconfig
# also needed at runtime
Requires: xorg-x11-xbitmaps

%description
Bitmap provides a bitmap editor and misc converter utilities for the X
Window System.

The package also includes files defining bitmaps associated with the 
Bitmap x11 editor.

%prep
%setup -q


%build
%configure --disable-dependency-tracking
make %{?_smp_mflags} AM_LDFLAGS=-lXmu

%install
%make_install INSTALL='install -p'

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/

%files
# COPYING is a stub!
%doc ChangeLog
%{_bindir}/atobm
%{_bindir}/bmtoa
%{_bindir}/bitmap
%{_includedir}/X11/bitmaps/*
%{_datadir}/X11/app-defaults/Bitmap*
%{_datadir}/applications/*bitmap*
%{_datadir}/icons/hicolor/32x32/apps/bitmap.png
%{_mandir}/man1/*.1*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.8-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.8-1
- Updating to 1.0.8 (#1183499)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Jaromir Capik <jcapik@redhat.com> - 1.0.7-1
- Update to 1.0.7 (#965215)
- Removing the aarch64 patch (not needed anymore)

* Tue Mar 26 2013 Jaromir Capik <jcapik@redhat.com> - 1.0.6-4
- aarch64 support (#925101)

* Mon Feb 11 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.6-3
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Jaromir Capik <jcapik@redhat.com> - 1.0.6-1
- Update to 1.0.6 (#808705)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 29 2011 Dan Horák <dan[at]danny.cz> - 1.0.3-10
- fix build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 27 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.0.3-8
- Make sure this package follows current packaging guidelines.
- Removed old provides.

* Tue Dec 15 2009 Stepan Kasal <skasal@redhat.com> - 1.0.3-7
- silence scriptlets

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.3-4
- Autorebuild for GCC 4.3

* Mon Dec 17 2007 Patrice Dumas <pertusus@free.fr> 1.0.3-3
- keep timestamps

* Mon Jan 29 2007 Patrice Dumas <pertusus@free.fr> 1.0.3-2
- update to 1.0.3

* Tue Oct 10 2006 Patrice Dumas <pertusus@free.fr> 1.0.2-3
- use consistently %%{buildroot}
- provides xorg-x11-%%{name}-devel

* Mon Oct  9 2006 Patrice Dumas <pertusus@free.fr> 1.0.2-2
- buildrequires pkgconfig, libXext-devel

* Sun Sep  3 2006 Patrice Dumas <pertusus@free.fr> 1.0.2-1
- Packaged for fedora extras
