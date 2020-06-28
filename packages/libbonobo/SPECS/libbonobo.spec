%define libxml2_version 2.4.21
%define orbit2_version 2.7.5

%define po_package libbonobo-2.0

Summary: Bonobo component system
Name: libbonobo
Version: 2.32.1
Release: 17%{?dist}
URL: http://ftp.gnome.org
Source0: http://download.gnome.org/sources/libbonobo/2.32/%{name}-%{version}.tar.bz2
License: GPLv2+ and LGPLv2+
# bonobo-activation-server, bonobo-activation-sysconf and bonobo-slay are GPL
# libbonobo and libbonobo-activation are LGPLv2+
BuildRequires: libxml2-devel >= %{libxml2_version}
BuildRequires: ORBit2-devel >= %{orbit2_version}
BuildRequires: intltool >= 0.14-1
BuildRequires: automake autoconf libtool
#BuildRequires: gtk-doc
BuildRequires: flex, bison, zlib-devel, popt-devel
#BuildRequires: dbus-glib-devel
BuildRequires: gettext

Patch0: libbonobo-multishlib.patch
Patch1: libbonobo-2.32.1-srcdir-macro.patch
Patch2: 0001-Remove-use-of-G_DISABLE_DEPRECATED.patch
Patch100: libbonobo3.sgifixes.patch
%description
Bonobo is a component system based on CORBA, used by the GNOME desktop.

%package devel
Summary: Libraries and headers for libbonobo
Requires:  %name = %{version}-%{release}
Requires:  ORBit2-devel >= %{orbit2_version}
Requires:  libxml2-devel >= %{libxml2_version}
Requires:  popt-devel


%description devel
Bonobo is a component system based on CORBA, used by the GNOME desktop.

This package contains header files used to compile programs that
use Bonobo.

%prep
%setup -q -n %{name}-%{version}

%ifarch ppc64 s390x x86_64
%patch0 -p1 -b .multishlib
%endif

%patch1 -p0 -b .srcmacro
%patch2 -p1
%patch100 -p1 -b sgifixes.

autoreconf -i -f

%build
%configure --disable-gtk-doc

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

## just kill this wherever it lives
rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo-2.0/samples/bonobo-echo-2
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/bonobo-2.0/samples/bonobo-echo-2

## kill other stuff
rm $RPM_BUILD_ROOT%{_bindir}/echo-client-2
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.*a
rm $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/*.*a
rm $RPM_BUILD_ROOT%{_bindir}/bonobo-slay

for serverfile in $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

# noarch packages install to /usr/lib/bonobo/servers
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/bonobo/servers

%find_lang %{po_package}

#%%ldconfig_scriptlets

%files -f %{po_package}.lang

%doc AUTHORS COPYING NEWS README doc/NAMESPACE

%{_libdir}/lib*.so.*
%{_libdir}/bonobo
%{_libdir}/orbit-2.0/*.so*
%{_bindir}/*
%{_libexecdir}/*
%{_sbindir}/*
%dir %{_prefix}/lib/bonobo/servers
%dir %{_prefix}/lib/bonobo
%dir %{_sysconfdir}/bonobo-activation
%config %{_sysconfdir}/bonobo-activation/*
%{_datadir}/man/man*/*

%files devel

%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/idl/*
%{_datadir}/gtk-doc/html/libbonobo
%{_datadir}/gtk-doc/html/bonobo-activation

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 Colin Walters <walters@verbum.org> - 2.32.1-5
- Backport patch from upstream to fix build with recent GLib

* Thu Feb 07 2013 Jon Ciesla <limburgher@gmail.com> - 2.32.1-4
- Merge review fixes, BZ 225989.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr  4 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.32.1-1
- Update to 2.32.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91
- Spec file cleanups

* Sun Feb 14 2010 Matthias Clasen <mclasen@redhat.com> - 2.24.2-2
- Rebuild

* Wed Sep 23 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.2-1
- Update to 2.24.2

* Wed Jul 29 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-4
- Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-2
- Minor directory ownership cleanup
- Fix installation

* Sun Mar 15 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008 Caolán McNamara <caolanm@redhat.com> - 2.24.0-3
- rebuild to get new rpm provides of pkgconfig(libbonobo-2.0)

* Tue Oct  7 2008 Ray Strode <rstrode@redhat.com> - 2.24.0-2
- Own /usr/lib/bonobo for noarch packages (bug 463054)

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Sat Sep 20 2008 Peter Robinson <probinson@gmail.com> - 2.23.1-2
- Kill dependency on perl RHBZ #462901

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Tue Jun 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.0-1
- Update to 2.23.0

* Tue May  6 2008 Ray Strode <rstrode@redhat.com> - 2.22.0-3
- Tie bonobo-activation-server more closely to session
  bgo #530615

* Tue Apr 29 2008 Ray Strode <rstrode@redhat.com> - 2.22.0-2
- Take name on message bus to tie activation server to desktop session

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Fri Feb 22 2008 Ray Strode <rstrode@redhat.com> - 2.21.90-3
- Drop upstreamed patch

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.21.90-2
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 2.20.4-1
- Update to 2.20.4

* Fri Dec 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.3-1
- Update to 2.20.3

* Wed Dec 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.2-1
- Update to 2.20.2

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-1
- Update to 2.20.1 (memory leak fixes, translation updates)
- Drop upstreamed patches 

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Wed Sep 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-6
- Plug a memory leak in bonobo-activation-server

* Wed Sep 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-5
- Plug a memory leak in bonobo-activation-server

* Tue Aug 28 2007 Jesse Keating <jkeating@redhat.com> - 2.19.6-4
- Require popt-devel in -devel.
- And BuildRequire popt-devel.

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 2.19.6-2
- Rebuild for ppc toolchain bug

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-2
- Update the license field

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-1
- Update to 2.19.6

* Tue Jun 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Fri Apr 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-3
- Use the more correct upstream fix for the leak fixed in -2

* Mon Apr  9 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-2
- Don't leak strings from the bonobo activation environment

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0
- Require pkgconfig in the -devel package

* Mon Aug 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1.fc6
- Update to 2.15.3

* Sat Aug 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-1.fc6
- Update to 2.15.2

* Fri Aug 11 2006 Alexander Larsson <alexl@redhat.com> - 2.15.0-3
- Add patch to close fds when activating component (#200477)

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.0-2
- disable gtk-doc to fix multilib conflicts
- Don't ship static libraries

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.0-1
- Update to 2.15.0

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.14.0-4.1
- rebuild

* Mon Jun 12 2006 Bill Nottingham <notting@redhat.com> 2.14.0-4
- buildreq automake, not automake16

* Sat Jun 10 2006 Matthias Clasen <mclasen@redhat.com> 2.14.0-3
- Add missing BuildRequires

* Mon Jun  5 2006 Matthias Clasen <mclasen@redhat.com> 2.14.0-2
- Rebuild

* Tue Mar 14 2006 Ray Strode <rstrode@redhat.com> 2.14.0-1
- Update to 2.14.0

* Tue Mar  7 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 2.13.93

* Wed Feb 15 2006 Ray Strode <rstrode@redhat.com> 2.13.1-9
- yet another iteration of the shlib patch

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.1-8.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.1-8.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 25 2006 Ray Strode <rstrode@redhat.com> 2.13.1-8
- one more iteration of the shlib patch

* Wed Jan 25 2006 Ray Strode <rstrode@redhat.com> 2.13.1-7
- run automake in %%build so that shlib patch gets
  built
- change libdir logic to happen at configure time because
  automake's conditional support isn't that sophisticated
- s/%%makeinstall/make install DESTDIR=$RPM_BUILD_ROOT/

* Thu Jan 19 2006 Ray Strode <rstrode@redhat.com> 2.13.1-6
- s/sed -ie/sed -i -e/

* Thu Jan 19 2006 Ray Strode <rstrode@redhat.com> 2.13.1-5
- Step three (unbreak the step two breakage)

* Thu Jan 19 2006 Ray Strode <rstrode@redhat.com> 2.13.1-4
- Step two (bug 156982)

* Wed Jan 18 2006 Ray Strode <rstrode@redhat.com> 2.13.1-3
- Step one of the multi-bonoboshlib process
  (bug 156982)

* Mon Jan 16 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 2.13.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  1 2005 Matthias Clasen <mclasen@redhat.com> 2.13.0
- Update to 2.13.0

* Fri Sep 09 2005 Florian La Roche <laroche@redhat.com>
- add a version-release to the Provides: bonobo-activation since
  many packages still try to request a specific version number

* Thu Sep  8 2005 Matthias Clasen <mclasen@redhat.com> 2.10.1-1
- Update to 2.10.1

* Fri Aug  5 2005 Matthias Clasen <mclasen@redhat.com> 2.10.0-1
- New upstream version

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> 2.8.1-1
- Update to 2.8.1

* Tue Sep 28 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-2
- Add patch to make bonobo-activation notice epiphany being
  installed. Bug #117790

* Wed Sep 22 2004 Alexander Larsson <alexl@redhat.com> - 2.8.0-1
- update to 2.8.0

* Fri Jul 30 2004 Ray Strode <rstrode@redhat.com> 2.6.2-2
- rebuilt

* Fri Jul 30 2004 Ray Strode <rstrode@redhat.com> 2.6.2-1
- Update to 2.6.2

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar 22 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-2
- BuildRequire gtk-doc - bug #110795

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-1
- Update to 2.6.0

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 23 2004 Alexander Larsson <alexl@redhat.com> 2.5.4-1
- update to 2.5.4

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Jonathan Blandford <jrb@redhat.com> 2.5.3-1
- new version

* Wed Jan 14 2004 Jeremy Katz <katzj@redhat.com> 2.4.3-1
- update to 2.4.3

* Wed Sep  3 2003 Alexander Larsson <alexl@redhat.com> 2.4.0-1
- 2.4.0

* Wed Aug 13 2003 Alexander Larsson <alexl@redhat.com> 2.3.6-2
- rebuild

* Mon Aug 11 2003 Alexander Larsson <alexl@redhat.com> 2.3.6-1
- Rebuild for gnome 2.4

* Tue Jul 22 2003 Havoc Pennington <hp@redhat.com>
- automated rebuild

* Tue Jul  8 2003 Havoc Pennington <hp@redhat.com> 2.2.3-1
- 2.2.3

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb  4 2003 Havoc Pennington <hp@redhat.com> 2.2.0-1
- 2.2.0

* Tue Jan 28 2003 Matt Wilson <msw@redhat.com> 2.1.1-3
- use LIBTOOL=/usr/bin/libtool

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sun Jan 12 2003 Havoc Pennington <hp@redhat.com>
- 2.1.1

* Fri Nov  8 2002 Havoc Pennington <hp@redhat.com>
- 2.1.0
- fix installed but unpackaged files

* Wed Jun 26 2002 Owen Taylor <otaylor@redhat.com>
- Fix find_lang

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- 1.117.0

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.116.0

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- 1.113.0

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 1.111.0

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0
- Rebuild for dependencies
- Intltoolize, the included version has problems with our Perl

* Tue Jan 22 2002 Havoc Pennington <hp@redhat.com>
- automake-1.4

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 cvs snap

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- 1.107.0, glib 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib, new snap

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- move to 1.103.0 tarball
- call automake after patching Makefile.am
- patch for parallel install

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- add some requires

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- conflict with bonobo < 1.0.8 to avoid header conflicts
- update group

* Mon Sep 17 2001 Havoc Pennington <hp@redhat.com>
- moved IDL files into subdir
- remove smp_mflags, libbonobo does not like those

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- remove IDL files as temporary hack

* Wed Sep 12 2001 Havoc Pennington <hp@redhat.com>
- Initial build.


