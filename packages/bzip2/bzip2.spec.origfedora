%global library_version 1.0.8

Summary: A file compression utility
Name: bzip2
Version: 1.0.8
Release: 1%{?dist}
License: BSD
URL: http://www.bzip.org/
#Source0: http://www.bzip.org/%{version}/%{name}-%{version}.tar.gz
Source0: https://sourceware.org/pub/bzip2/%{name}-%{version}.tar.gz
Source1: bzip2.pc

Patch0: bzip2-saneso.patch
Patch1: bzip2-cflags.patch
Patch2: bzip2-ldflags.patch

BuildRequires: gcc

%description
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

Install bzip2 if you need a compression utility.

%package devel
Summary: Libraries and header files for apps which will use bzip2
Requires: bzip2-libs = %{version}-%{release}

%description devel

Header files and a library of bzip2 functions, for developing apps
which will use the library.

%package libs
Summary: Libraries for applications using bzip2

%description libs

Libraries for applications using the bzip2 compression format.

%package static
Summary: Libraries for applications using bzip2

%description static

Static libraries for applications using the bzip2 compression format.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp -a %{SOURCE1} .
sed -i "s|^libdir=|libdir=%{_libdir}|" bzip2.pc

%build
%if 0%{?rhel} >= 7
    %ifarch ppc64
        export O3="-O3"
    %else
        export O3=""
    %endif
%else
    export O3=""
%endif

make -f Makefile-libbz2_so CC="%{__cc}" AR="%{__ar}" RANLIB="%{__ranlib}" \
    CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -fpic -fPIC $O3" \
    LDFLAGS="%{__global_ldflags}" \
    %{?_smp_mflags} all

rm -f *.o
make CC="%{__cc}" AR="%{__ar}" RANLIB="%{__ranlib}" \
    CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 $O3" \
    LDFLAGS="%{__global_ldflags}" \
    %{?_smp_mflags} all

%install
chmod 644 bzlib.h
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/pkgconfig,%{_includedir}}
cp -p bzlib.h $RPM_BUILD_ROOT%{_includedir}
install -m 755 libbz2.so.%{library_version} $RPM_BUILD_ROOT%{_libdir}
install -m 644 libbz2.a $RPM_BUILD_ROOT%{_libdir}
install -m 644 bzip2.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/bzip2.pc
install -m 755 bzip2-shared  $RPM_BUILD_ROOT%{_bindir}/bzip2
install -m 755 bzip2recover bzgrep bzdiff bzmore  $RPM_BUILD_ROOT%{_bindir}/
cp -p bzip2.1 bzdiff.1 bzgrep.1 bzmore.1  $RPM_BUILD_ROOT%{_mandir}/man1/
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bunzip2
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bzcat
ln -s bzdiff $RPM_BUILD_ROOT%{_bindir}/bzcmp
ln -s bzmore $RPM_BUILD_ROOT%{_bindir}/bzless
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzegrep
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzfgrep
ln -s libbz2.so.%{library_version} $RPM_BUILD_ROOT%{_libdir}/libbz2.so.1
ln -s libbz2.so.1 $RPM_BUILD_ROOT%{_libdir}/libbz2.so
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzip2recover.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bunzip2.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcat.1
ln -s bzdiff.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcmp.1
ln -s bzmore.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzless.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzegrep.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzfgrep.1

%ldconfig_scriptlets libs

%files
%doc LICENSE CHANGES README
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/*
%{_mandir}/*/*

%files libs
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libbz2.so.1*

%files static
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libbz2.a

%files devel
%doc manual.html manual.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/bzip2.pc

%changelog
* Tue Aug 06 2019 Jakub Martisko <jamartis@redhat.com> - 1.0.8-1
- Update to version 1.0.8
  resolves: #1724797
  resolves: #1717478 	

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Jakub Martisko <jamartis@redhat.com> - 1.0.6-27
- Add gcc to buildrequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-25
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Jan Chaloupka <jchaloup@redhat.com> - 1.0.6-21
- CVE-2016-3189 bzip2: heap use after free in bzip2recover
  resolves: #1348179

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.6-19
- Adding static lib (#1253934)

* Tue Dec 08 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.6-18
- Adding bzip2.pc to the devel subpackage (#1289576)

* Fri Aug 14 2015 Adam Jackson <ajax@redhat.com> 1.0.6-17
- Pass ldflags through so hardening actually works

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.0.6-15
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.6-13
- fix license marking

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 11 2014 jchaloup <jchaloup@redhat.com> - 1.0.6-11
- resolves: #1063849
  recompiled with -O3 flag for ppc64 arch

* Wed Dec 11 2013 Peter Schiffer <pschiffe@redhat.com> - 1.0.6-10
- resolves: #1034855
  provided missing bzegrep and bzfgrep shortcuts

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Peter Schiffer <pschiffe@redhat.com> - 1.0.6-7
- moved libraries from /lib to /usr/lib

* Fri Oct 26 2012 Peter Schiffer <pschiffe@redhat.com> - 1.0.6-6
- .spec file cleanup

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.0.6-2
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.0.6-1
- update to 1.0.6

* Mon Jul 12 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.0.5-7
- add LICENSE to bzip2-libs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Ivana Varekova <varekova@redhat.com> 1.0.5-5
- remove static library

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  1 2008 Ivana Varekova <varekova@redhat.com> 1.0.5-3
- minor spec file changew

* Thu Apr 10 2008 Ivana Varekova <varekova@redhat.com> 1.0.5-2
- Resolves: #441775
  fix libs link

* Tue Mar 25 2008 Ivana Varekova <varekova@redhat.com> 1.0.5-1
- update to 1.0.5

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-14
- Autorebuild for GCC 4.3

* Wed Jan 23 2008 Ivana Varekova <varekova@redhat.com> 1.0.4-13
- rebuild

* Mon May 21 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-12
- fix *.so,*.a directory

* Mon May 21 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-11
- remove libbz2.* from /usr/lib* to /lib*

* Wed Apr  4 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-10
- change libz.a permissions

* Wed Apr  4 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-9
- remove useless -p 

* Thu Mar 15 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-8
- remove unnecessary "/" after RPM_BUILD_ROOT macro

* Mon Feb 19 2007 Jesse Keating <jkeating@redhat.com> 1.0.4-7
- Temporarily add static lib back in for rpm

* Fri Feb 16 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-6
- incorporate the next review feedback

* Thu Feb 15 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-5
- incorporate package review feedback

* Tue Feb  6 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-4
- fix bzip2recover patch

* Mon Feb  5 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-3
- Resolves: 226979 
  Buffer overflow in bzip2's bzip2recover

* Mon Jan  8 2007 Ivana Varekova <varekova@redhat.com> 1.0.4-1
- update to 1.0.4
- spec file cleanup

* Mon Jul 17 2006 Ivana Varekova <varekova@redhat.com> 1.0.3-3
- add cflags (#198926)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.3-2.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.3-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.3-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 25 2005 Ivana Varekova <varekova@redhat.com> 1.0.3-2
- fix bug 174172 - CAN-2005-0758 bzgrep has security issue in sed usage

* Mon Aug 29 2005 Ivana Varekova <varekova@redhat.com> 1.0.3-1
- 1.0.3
- add NULL-ptr-check patch 
  (patch author: Mihai Limbasan <mihailim@gmail.com)

* Thu May 19 2005 Jiri Ryska <jryska@redhat.com>
- fixed permission setting for decompressed files #155742
- fixed decompression bomb (DoS) #157548

* Fri Mar 04 2005 Jiri Ryska <jryska@redhat.com>
- rebuilt

* Thu Dec 09 2004 Jiri Ryska <jryska@redhat.com>
- changed temp file creation in bzdiff #92444

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 17 2003 Jeff Johnson <jbj@redhat.com> 1.0.2-11
- rebuilt because of crt breakage on ppc64.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar 31 2003 Jeff Johnson <jbj@redhat.com> 1.0.2-9
- rebuild to get rid of undefined __ctype_b in libbz2.a.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com>
- Pass __cc/__ar/__ranlib to makefiles
- Use _smp_mflags

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches
- fix %%doc file list

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.2-3
- Rebuild in new environment

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.2-2
- Rebuild

* Wed Jan 30 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.2-1
- 1.0.2
- Total overhaul of build precedure
- Add many small helper programs added to 1.0.2
- drop old patches

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Nov 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.0.1-5
- Don't segfault when infile is a directory and "-f" is used (#56623)
- Automake is evil. Add workaround

* Fri Mar 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- use "License" instead of "Copyright"
- split out libs

* Fri Jul 21 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new URL and source location

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jul 01 2000 Trond Eivind Glomsrød <teg@redhat.com>
- 1.0.1
- ported my patch

* Tue Jun 13 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging to build on solaris2.5.1.
- remove config.cache from autoconf patch.
- sparc: use %%configure, but not the m4 macros.

* Tue Jun 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- Use %%configure, %%makeinstall, %%{_manpath} and %%{_tmpdir}

* Wed May 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- 1.0.0 - ported my 1.0pre8 libtoolizedautoconf patch

* Tue May 16 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use soft links, not hardlinks, for binaries
- mv .so to devel

* Mon May 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- autoconfed and libtoolized package 
- fixed Copyright (it's BSD, not GPL)
- dumped bzless (less works fine with bz2-files)
- rewrote build and install parts
- separated main package and devel package

* Mon May  8 2000 Bernhard Rosenkränzer <bero@redhat.com>
- 1.0pre8

* Fri Apr 14 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Add bzgrep (a version of zgrep hacked to do bzip2)

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Fri Dec 31 1999 Bernhard Rosenkränzer <bero@redhat.com>
- 0.9.5d
- Update download URL, add URL: tag in header

* Tue Aug 10 1999 Jeff Johnson <jbj@redhat.com>
- upgrade to 0.9.5c.

* Mon Aug  9 1999 Bill Nottingham <notting@redhat.com>
- install actual bzip2 binary, not libtool cruft.

* Sun Aug  8 1999 Jeff Johnson <jbj@redhat.com>
- run ldconfig to get shared library.

* Mon Aug  2 1999 Jeff Johnson <jbj@redhat.com>
- create shared libbz1.so.* library.

* Sun Apr  4 1999 Jeff Johnson <jbj@redhat.com>
- update to bzip2-0.9.0c.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- force compilation with egcs to avoid gcc optimization bug (thank God 
  we haven't been beaten by it)

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- version 0.9.0b

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.9.0

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- first build for Manhattan
