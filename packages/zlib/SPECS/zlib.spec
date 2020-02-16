# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

%bcond_without minizip

Name:    zlib
Version: 1.2.11
Release: 19%{?dist}
Summary: The compression and decompression library
# /contrib/dotzlib/ have Boost license
License: zlib and Boost
URL: http://www.zlib.net/

Source: http://www.zlib.net/zlib-%{version}.tar.xz
# https://github.com/madler/zlib/pull/210
Patch0: zlib-1.2.5-minizip-fixuncrypt.patch
# resolves: #805113
#Patch1: zlib-1.2.11-optimized-s390.patch
# general aarch64 optimizations
#Patch4: 0001-Neon-Optimized-hash-chain-rebase.patch
#Patch5: 0002-Porting-optimized-longest_match.patch
#Patch6: 0003-arm64-specific-build-patch.patch
# IBM Z optimalizations
#Patch7: zlib-1.2.11-IBM-Z-hw-accelrated-deflate-s390x.patch
# IBM CRC32 optimalization for POWER archs
#Patch8: zlib-1.2.11-optimized-CRC32-framework.patch
# fixed firefox crash + added test case
#Patch9: zlib-1.2.11-firefox-crash-fix.patch

BuildRequires: automake, autoconf, libtool

%global __provides_exclude_from ^%{_libdir}/pkgconfig/minizip\\.pc$

%description
Zlib is a general-purpose, patent-free, lossless data compression
library which is used by many different programs.


%package devel
Summary: Header files and libraries for Zlib development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The zlib-devel package contains the header files and libraries needed
to develop programs that use the zlib compression and decompression
library.


%package static
Summary: Static libraries for Zlib development
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The zlib-static package includes static libraries needed
to develop programs that use the zlib compression and
decompression library.


%if %{with minizip}
%package -n minizip-compat
Summary: Library for manipulation with .zip archives
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n minizip-compat
Minizip is a library for manipulation with files from .zip archives.


%package -n minizip-compat-devel
Summary: Development files for the minizip library
Requires: minizip-compat%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Conflicts: minizip-devel

%description -n minizip-compat-devel
This package contains the libraries and header files needed for
developing applications which use minizip.
%endif


%prep
%setup -q
%patch0 -p1 -b .fixuncrypt
#%ifarch s390 s390x
#%patch1 -p1 -b .optimized-deflate
#%endif
#%ifarch aarch64
#%patch4 -p1 -b .optimize-aarch64
#%patch5 -p1 -b .optimize-aarch64
#%patch6 -p1 -b .optimize-aarch64
#%endif
#%patch7 -p1
#%patch8 -p1
#%patch9 -p1


iconv -f iso-8859-2 -t utf-8 < ChangeLog > ChangeLog.tmp
mv ChangeLog.tmp ChangeLog


%build
export CFLAGS="$RPM_OPT_FLAGS"
%ifarch ppc64
CFLAGS+=" -O3"
%endif
%ifarch aarch64
CFLAGS+=" -DARM_NEON -O3"
%endif

export LDFLAGS="$RPM_LD_FLAGS"
# no-autotools, %%configure is not compatible
./configure --libdir=%{_libdir} --includedir=%{_includedir} --prefix=%{_prefix}
%make_build

%if %{with minizip}
cd contrib/minizip
autoreconf --install
%configure --enable-static=no
%make_build
%endif


%check
make test


%install
export LDFLAGS="$RPM_LD_FLAGS"
%make_install
mkdir $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_prefix}/share/man/* $RPM_BUILD_ROOT%{_mandir}/

%if %{with minizip}
%make_install -C contrib/minizip
# https://github.com/madler/zlib/pull/229
rm $RPM_BUILD_ROOT%_includedir/minizip/crypt.h
%endif

find $RPM_BUILD_ROOT -name '*.la' -delete


%files
%license README
%doc ChangeLog FAQ
%{_libdir}/libz.so.*


%files devel
%doc doc/algorithm.txt test/example.c
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
%{_includedir}/zlib.h
%{_includedir}/zconf.h
%{_mandir}/man3/zlib.3*


%files static
%license README
%{_libdir}/libz.a


%if %{with minizip}
%files -n minizip-compat
%doc contrib/minizip/MiniZip64_info.txt contrib/minizip/MiniZip64_Changes.txt
%{_libdir}/libminizip.so.*


%files -n minizip-compat-devel
%dir %{_includedir}/minizip
%{_includedir}/minizip/*.h
%{_libdir}/libminizip.so
%{_libdir}/pkgconfig/minizip.pc
%endif


%changelog
* Thu Sep 05 2019 Ondrej Dubaj <odubaj@redhat.com> - 1.2.11-19
- IBM CRC32 optimalization for POWER 8+ architectures re-add
- fixed firefox crash duer to zlib (#1741266)
- added test for crc32

* Thu Aug 15 2019 Ondrej Dubaj <odubaj@redhat.com> - 1.2.11-18
- IBM CRC32 optimalization for POWER 8+ architectures revert

* Thu Aug 01 2019 Ondrej Dubaj <odubaj@redhat.com> - 1.2.11-17
- IBM Z hardware-accelerated deflate for s390x architectures
- IBM CRC32 optimalization for POWER 8+ architectures

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct  2 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.11-14
- Bump build

* Tue Sep 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.11-13
- Revert aarch64 neon inflate optimisation

* Wed Aug 29 2018 Patrik Novotný <panovotn@redhat.com> - 1.2.11-12
- Rename minizip and minizip-devel to minizip-compat and minizip-compat-devel respectively

* Thu Aug 23 2018 Patrik Novotný <panovotn@redhat.com> - 1.2.11-11
- Provides minizip-compat and minizip-compat-devel

* Fri Aug 03 2018 Pavel Raiskup <praiskup@redhat.com> - 1.2.11-10
- add %%bcond for minizip
- use %%make_* macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.11-8
- Optimisations for aarch64
- Minor spec cleanups

* Thu Mar 15 2018 Pavel Raiskup <praiskup@redhat.com> - 1.2.11-7
- don't install crypt.h (rhbz#1424609)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.11-5
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Pavel Raiskup <praiskup@redhat.com> - 1.2.11-2
- fix s390(x) optimizing patch (FTBFS on s390(x))
- simplify ppc64 hack with -O3

* Mon Jan 30 2017 Pavel Raiskup <praiskup@redhat.com> - 1.2.11-1
- latest upstream release (rhbz#1409372)
- cleanup rpmlint
- revert fix for rhbz#985344
- requires with %%_isa tag
- drop zlib Z_BLOCK flush patch (rhbz#1417355)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 14 2015 Adam Jackson <ajax@redhat.com> 1.2.8-9
- Link with -z now for full RELRO

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug  6 2014 Tom Callaway <spot@fedoraproject.org> - 1.2.8-6
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 jchaloup <jchaloup@redhat.com> - 1.2.8-4
- resolves: #1064213
  recompiled with -O3 flag for ppc64 arch

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 1.2.8-3
- resolves: #985344
  add a patch to fix missing minizip include

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun  7 2013 Peter Schiffer <pschiffe@redhat.com> - 1.2.8-1
- resolves: #957680
  updated to 1.2.8

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct  4 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-9
- updated patch optimizing deflate on s390(x) architectures

* Wed Aug 29 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-8
- related: #832545
  reverted changes for this bug, static libraries shouldn't be compiled with
  -fPIC flag

* Mon Aug 27 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-7
- resolves: #844791
  rank Z_BLOCK flush below Z_PARTIAL_FLUSH only when last flush was Z_BLOCK
- done some minor .spec file cleanup

* Mon Aug 13 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-6
- added patch from IBM which optimizes deflate on s390(x) architectures

* Thu Aug 02 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-5
- resolves: #832545
  recompiled with -fPIC flag

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-3
- moved /lib* to /usr/lib*

* Mon Jun 11 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-2
- recompiled with -Wl,-z,relro flags

* Thu May 10 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.7-1
- resolves: #785726
- resolves: #805874
  update to 1.2.7

* Tue Jan 10 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.5-6
- resolves: #719139
  Zlib fails to read zip64 files on 64-bit system

* Fri Nov 11 2011 Tom Callaway <spot@fedoraproject.org> - 1.2.5-5
- fix minizip to permit uncrypt when NOUNCRYPT is not defined

* Wed Apr  6 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 1.2.5-4
- Resolves: #678603
  zlib from minizip allowed NULL pointer parameter of function unzGetCurrentFileInfo 

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.2.5-2
- Resolves: #591317
  pdfedit fails to compile on i686 with zlib.h errors

* Thu Apr 22 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.2.5-1
- update to 1.2.5

* Mon Mar 29 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.2.4-1
- update to 1.2.4
  use the upstream make/configure files for zlib,
  change additional makefile/configure file to be used only to minizip
  add pkgconfig to zlib

* Mon Mar  8 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.2.3-25
- add Boost license

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.2.3-24
- Use bzipped upstream tarball.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Stepan Kasal <skasal@redhat.com> - 1.2.3-22
- fix the libz.so symlink

* Tue Mar 17 2009 Stepan Kasal <skasal@redhat.com> - 1.2.3-21
- consolidate the autoconfiscation patches into one and clean it up
- consequently, clean up the %%build and %%install sections
- zconf.h includes unistd.h again (#479133)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Ivana Varekova <varekova@redhat.com> - 1.2.3-19
- fix 473490 - unchecked malloc

* Wed Feb 13 2008 Ivana Varekova <varekova@redhat.com> - 1.2.3-18
- change license tag (226671#c29)

* Mon Feb 11 2008 Ivana Varekova <varekova@redhat.com> - 1.2.3-17
- spec file changes

* Fri Nov 23 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-16
- remove minizip headers to minizip-devel
- spec file cleanup
- fix minizip.pc file

* Wed Nov 14 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-15
- separate static subpackage

* Wed Aug 15 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-14
- create minizip subpackage

* Mon May 21 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-13
- remove .so,.a

* Mon May 21 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-12
- Resolves #240277
  Move libz to /lib(64)

* Mon Apr 23 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-11
- Resolves: 237295
  fix Summary tag

* Fri Mar 23 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-10
- remove zlib .so.* packages to /lib

* Fri Mar  9 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-9
- incorporate package review feedback

* Wed Feb 21 2007 Adam Tkac <atkac redhat com> - 1.2.3-8
- fixed broken version of libz

* Tue Feb 20 2007 Adam Tkac <atkac redhat com> - 1.2.3-7
- building is now automatized
- specfile cleanup

* Tue Feb 20 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-6
- remove the compilation part to build section
  some minor changes

* Mon Feb 19 2007 Ivana Varekova <varekova@redhat.com> - 1.2.3-5
- incorporate package review feedback

* Mon Oct 23 2006 Ivana Varekova <varekova@redhat.com> - 1.2.3-4
- fix #209424 - fix libz.a permissions

* Wed Jul 19 2006 Ivana Varekova <varekova@redhat.com> - 1.2.3-3
- add cflags (#199379)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.3-2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Aug 24 2005 Florian La Roche <laroche@redhat.com>
- update to 1.2.3

* Fri Jul 22 2005 Ivana Varekova <varekova@redhat.com> 1.2.2.2-5
- fix bug 163038 - CAN-2005-1849 - zlib buffer overflow

* Thu Jul 7  2005 Ivana Varekova <varekova@redhat.com> 1.2.2.2-4
- fix bug 162392 - CAN-2005-2096 

* Wed Mar 30 2005 Ivana Varekova <varekova@redhat.com> 1.2.2.2-3
- fix bug 122408 - zlib build process runs configure twice

* Fri Mar  4 2005 Jeff Johnson <jbj@redhat.com> 1.2.2.2-2
- rebuild with gcc4.

* Sat Jan  1 2005 Jeff Johnson <jbj@jbj.org> 1.2.2.2-1
- upgrade to 1.2.2.2.

* Fri Nov 12 2004 Jeff Johnson <jbj@jbj.org> 1.2.2.1-1
- upgrade to 1.2.2.1.

* Sun Sep 12 2004 Jeff Johnson <jbj@redhat.com> 1.2.1.2-1
- update to 1.2.1.2 to fix 2 DoS problems (#131385).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Jan 18 2004 Jeff Johnson <jbj@jbj.org> 1.2.1.1-1
- upgrade to zlib-1.2.1.1.

* Sun Nov 30 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.2.1 release

* Mon Oct 13 2003 Jeff Johnson <jbj@jbj.org> 1.2.0.7-3
- unrevert zlib.h include constants (#106291), rejected upstream.

* Wed Oct  8 2003 Jeff Johnson <jbj@jbj.org> 1.2.0.7-2
- fix: gzeof not set when reading compressed file (#106424).
- fix: revert zlib.h include constants for now (#106291).

* Tue Sep 23 2003 Jeff Johnson <jbj@redhat.com> 1.2.0.7-1
- update to 1.2.0.7, penultimate 1.2.1 release candidate.

* Tue Jul 22 2003 Jeff Johnson <jbj@redhat.com> 1.2.0.3-0.1
- update to release candidate.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 19 2003 Jeff Johnson <jbj@redhat.com> 1.1.4-9
- rebuild, revert from 1.2.0.1.

* Mon Feb 24 2003 Jeff Johnson <jbj@redhat.com> 1.1.4-8
- fix gzprintf buffer overrun (#84961).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.1.4-7
- rebuilt

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 1.1.4-6
- Make ./configure use $CC to ease cross-compilation

* Tue Nov 12 2002 Jeff Johnson <jbj@redhat.com> 1.1.4-5
- rebuild from cvs.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 26 2002 Jakub Jelinek <jakub@redhat.com> 1.1.4-2
- remove glibc patch, it is no longer needed (zlib uses gcc -shared
  as it should)
- run tests and only build the package if they succeed

* Thu Apr 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.1.4-1
- 1.1.4

* Wed Jan 30 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.1.3-25.7
- Fix double free

* Sun Aug 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.1.3-24
- Add example.c and minigzip.c to the doc files, as
  they are listed as examples in the README (#52574)

* Mon Jun 18 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Updated URL
- Add version dependency for zlib-devel
- s/Copyright/License/

* Wed Feb 14 2001 Trond Eivind Glomsrød <teg@redhat.com>
- bumped version number - this is the old version without the performance enhancements

* Fri Sep 15 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add -fPIC for shared libs (patch by Fritz Elfert)

* Thu Sep  7 2000 Jeff Johnson <jbj@redhat.com>
- on 64bit systems, make sure libraries are located correctly.

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 02 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Tue Jun 13 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging to build on solaris2.5.1.

* Wed Jun 07 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_mandir} and %%{_tmppath}

* Fri May 12 2000 Trond Eivind Glomsrød <teg@redhat.com>
- updated URL and source location
- moved README to main package

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man page.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- link against glibc

* Mon Jul 27 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 1.1.3

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.2
- buildroot

* Tue Oct 07 1997 Donnie Barnes <djb@redhat.com>
- added URL tag (down at the moment so it may not be correct)
- made zlib-devel require zlib

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
