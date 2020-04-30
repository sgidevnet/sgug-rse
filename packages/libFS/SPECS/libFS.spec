%global tarball libFS
#global gitdate 20130524
#global gitversion 26dc23446

Summary: X.Org X11 libFS runtime library
Name: libFS
Version: 1.0.7
Release: 13%{?dist}
License: MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
%endif

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-4

%description
X.Org X11 libFS runtime library

%package devel
Summary: X.Org X11 libFS development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libFS development package

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# hack, we'll %%doc this on our own
rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README
%{_libdir}/libFS.so.6
%{_libdir}/libFS.so.6.0.0

%files devel
%doc doc/FSlib.txt
%{_includedir}/X11/fonts/FSlib.h
%{_libdir}/libFS.so
%{_libdir}/pkgconfig/libfs.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 1.0.7-12
- Rebuild for xtrans 1.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 1.0.7-9
- Drop useless %%defattr

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 1.0.7-8
- Use ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Adam Jackson <ajax@redhat.com> 1.0.7-1
- libFS 1.0.7

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-1
- libFS 1.0.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.0.5-1
- libFS 1.0.5

* Fri May 24 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.0.4-6.20130524git26dc23446
- Update to git snapshot to fix CVEs listed below:
- CVE-2013-1996

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.4-5
- autoreconf needs xorg-x11-util-macros

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.4-4
- autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Adam Jackson <ajax@redhat.com> 1.0.4-1
- libFS 1.0.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Adam Jackson <ajax@redhat.com> 1.0.3-1
- libFS 1.0.3

* Mon Aug 30 2010 Adam Jackson <ajax@redhat.com> 1.0.2-1
- libFS 1.0.2
- merge review cleanups (#226005)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.1-4
- Un-require xorg-x11-filesystem

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.1-2
- Fix license tag.

* Tue Jun 10 2008 Adam Jackson <ajax@redhat.com> 1.0.1-1
- libFS 1.0.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0-7
- Autorebuild for GCC 4.3

* Thu Sep 20 2007 Adam Jackson <ajax@redhat.com> 1.0.0-6
- Update xtrans dep and rebuild.

* Mon Sep 17 2007 Adam Jackson <ajax@redhat.com> 1.0.0-5
- Rebuild for abstract socket support.

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.0.0-4
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> - 1.0.0-4
- Don't install INSTALL

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-3.1
- rebuild

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-3
- Added "Requires: xorg-x11-proto-devel" to devel package.
- Remove package ownership of mandir/libdir/etc.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.0-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.0-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 23 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-2
- Bumped and rebuilt

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libFS to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Updated libFS to version 0.99.3 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov 12 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-2
- Removed "Provides: {name}" that got left from old package naming.

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libFS to version 0.99.2 from X11R7 RC2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 31 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-4
- Remove CFLAGS -D_XOPEN_SOURCE hack to test if upstream now builds ok.

* Thu Oct 27 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-3
- Add RPM_OPT_FLAGS to CFLAGS, as redefining CFLAGS lost the defaults

* Thu Oct 27 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- Invoke 'make' in build stage
- Add -D_XOPEN_SOURCE to CFLAGS to work around build failure

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libFS to version 0.99.1 from X11R7 RC1

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-4
- Added BuildRequires: pkgconfig

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove "xorg-x11" from the name due to unanimous decision
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
