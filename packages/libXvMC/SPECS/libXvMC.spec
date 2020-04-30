%global tarball libXvMC
#global gitdate 20130524
%global gitversion e9415ddef

Summary: X.Org X11 libXvMC runtime library
Name: libXvMC
Version: 1.0.11
Release: 2%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(videoproto) pkgconfig(xv)
BuildRequires: libX11-devel >= 1.5.99.902

%description
X.Org X11 libXvMC runtime library

%package devel
Summary: X.Org X11 libXvMC development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXvMC development package

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# do this ourself in %%doc so we get %%version
rm $RPM_BUILD_ROOT%{_docdir}/*/*.txt

# Touch XvMCConfig for rpm to package the ghost file. (#192254)
{
    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11
    touch $RPM_BUILD_ROOT%{_sysconfdir}/X11/XvMCConfig
}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md
%{_libdir}/libXvMC.so.1
%{_libdir}/libXvMC.so.1.0.0
%{_libdir}/libXvMCW.so.1
%{_libdir}/libXvMCW.so.1.0.0
%ghost %config(missingok,noreplace) %verify (not md5 size mtime) %{_sysconfdir}/X11/XvMCConfig

%files devel
%doc XvMC_API.txt
%{_includedir}/X11/extensions/XvMClib.h
%{_libdir}/libXvMC.so
%{_libdir}/libXvMCW.so
%{_libdir}/pkgconfig/xvmc.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Adam Jackson <ajax@redhat.com> - 1.0.11-1
- libXvMC 1.0.11

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 1.0.10-6
- Drop useless %%defattr

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.0.10-1
- libXvMC 1.0.10
- fixes CVE-2016-7953

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 14 2015 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.0.9-1
- libXvMC 1.0.9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.0.8-1
- libXvMC 1.0.8

* Mon May 27 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.7-7.20130524gite9415ddef
- Require libX11 1.6RC2 for _XEatDataWords

* Fri May 24 2013 Dave Airlie <airlied@redhat.com 1.0.7-6.20130524git8c164524d
- Update to latest XvMC to fix fixes for CVEs

* Fri May 24 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.0.7-5.20130524gite9415ddef
- Update to latest git to fix the following CVEs
- CVE-2013-1999

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.7-4
- autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 08 2012 Adam Jackson <ajax@redhat.com> 1.0.7-1
- libXvMC 1.0.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Parag Nemade <paragn AT fedoraproject.org> 1.0.6-2
- Merge-review cleanup (#226092)

* Mon Aug 16 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-1
- libXvMC 1.0.6
- remove AUTHORS, not in tarball anymore

* Wed Oct 07 2009 Adam Jackson <ajax@redhat.com> 1.0.5-1
- libXvMC 1.0.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.4-7
- Un-require xorg-x11-filesystem
- Remove useless %%dir

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.4-5
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.0.4-3
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.0.4-2
- Don't install INSTALL

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 1.0.4-1
- Update to 1.0.4

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 1.0.3-1
- Update to 1.0.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.0.2-2.1
- rebuild

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-2
- Added "BuildRequires: pkgconfig" for (#193506)
- Replace "makeinstall" with "make install DESTDIR=..."
- Touch XvMCConfig during install phase, and add to file manifest as a ghost
  file, so that it is owned by the package if the user creates it. (#192254)

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.2-1
- Update to 1.0.2.  Drop #180902 patch, already fixed upstream.

* Tue Feb 21 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-3
- Added libXvMC-1.0.1-libXvMC-XConfigDir-fix-bug180902.patch to fix (#180902)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Added "Requires: libXv-devel, xorg-x11-proto-devel" to fix (#176862)

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated libXvMC to version 1.0.1 from X11R7.0

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXvMC to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXvMC to version 0.99.2 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libXvMC to version 0.99.1 from X11R7 RC1

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
