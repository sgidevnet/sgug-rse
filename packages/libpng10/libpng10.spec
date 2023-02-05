Summary:	Old version of libpng, needed to run old binaries
Name:		libpng10
Version:	1.0.69
Release:	7%{?dist}
License:	zlib
URL:		http://www.libpng.org/pub/png/libpng.html
Source0:	https://ftp-osl.osuosl.org/pub/libpng/src/libpng10/libpng-%{version}.tar.gz
Patch0:		libpng-1.0.63-soname.patch
Patch1:		libpng10-1.0.69-cve-2018-13785.patch
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	zlib-devel
Conflicts:	libpng < 2:1.2.0

# Move to unversioned documentation directories from F-20
# https://fedoraproject.org/wiki/Changes/UnversionedDocdirs
%global libpng10_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

%description
The libpng10 package contains an old version of libpng, a library of functions
for creating and manipulating PNG (Portable Network Graphics) image format
files.

This package is needed if you want to run binaries that were linked dynamically
with libpng 1.0.x.

%package devel
Summary:	Development tools for version 1.0 of libpng
Requires:	libpng10 = %{version}-%{release}
Requires:	pkgconfig
Requires:	zlib-devel%{?_isa}

%description devel
The libpng10-devel package contains the header files necessary for developing
programs using version 1.0 of the PNG (Portable Network Graphics) library.

If you want to develop programs that will manipulate PNG image format files,
while still running on previous old Linux releases, you should install
libpng10-devel.

%prep
%setup -q -n libpng-%{version}

# We want an soname of 2.%%{version}
%patch0 -b .soname

# Fix the calculation of row_factor in png_check_chunk_length (CVE-2018-13785)
# https://sourceforge.net/p/libpng/bugs/278/
# https://github.com/ctruta/libpng/commit/8a05766cb74af05c04c53e6c9d60c13fc4d59bf2
%patch1 -b .cve-2018-13785

%build
%configure \
	--disable-static \
	--disable-dependency-tracking \
	--without-binconfigs
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" install

# Install docs
# This is done manually so that the docs, which are all in the same directory,
# can be split between the main and devel package. If the %%doc macro is used
# in the files list with a non-absolute path, it clears out the docs directory
# first, which means the splitting of docs into two packages won't work.
# The alternative would be to have the devel docs in a different directory,
# but I don't want to do that.
mkdir -p %{buildroot}%{libpng10_docdir}
# Docs for main package
install -p -m 644 ANNOUNCE README TODO CHANGES %{!?_licensedir:LICENSE} Y2KINFO \
	%{buildroot}%{libpng10_docdir}/
# Docs for devel package
install -p -m 644 example.c libpng-%{version}.txt \
	%{buildroot}%{libpng10_docdir}/

# Unpackaged files
rm -f \
	%{buildroot}%{_bindir}/libpng-config \
	%{buildroot}%{_includedir}/png.h \
	%{buildroot}%{_includedir}/pngconf.h \
	%{buildroot}%{_libdir}/libpng.a \
	%{buildroot}%{_libdir}/libpng.la \
	%{buildroot}%{_libdir}/libpng.so \
	%{buildroot}%{_libdir}/libpng10.la \
	%{buildroot}%{_libdir}/libpng10.so.* \
	%{buildroot}%{_libdir}/pkgconfig/libpng.pc \
	%{buildroot}%{_mandir}/man3/libpng.3 \
	%{buildroot}%{_mandir}/man3/libpngpf.3 \
	%{buildroot}%{_mandir}/man5/png.5

# Fix devel link
rm -f %{buildroot}%{_libdir}/libpng10.so
ln -s libpng.so.2 %{buildroot}%{_libdir}/libpng10.so

%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 27)
# ldconfig scriptlets replaced by RPM File Triggers from Fedora 28
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%dir %{libpng10_docdir}/
%doc %{libpng10_docdir}/ANNOUNCE
%doc %{libpng10_docdir}/CHANGES
%doc %{libpng10_docdir}/README
%doc %{libpng10_docdir}/TODO
%doc %{libpng10_docdir}/Y2KINFO
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc %{libpng10_docdir}/LICENSE
%endif
%{_libdir}/libpng.so.2
%{_libdir}/libpng.so.2.%{version}

%files devel
%doc %{libpng10_docdir}/example.c
%doc %{libpng10_docdir}/libpng-%{version}.txt
%{_includedir}/libpng10/
%{_libdir}/libpng10.so
%{_libdir}/pkgconfig/libpng10.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.69-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.69-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Paul Howarth <paul@city-fan.org> - 1.0.69-5
- Fix the calculation of row_factor in png_check_chunk_length (CVE-2018-13785)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Paul Howarth <paul@city-fan.org> - 1.0.69-3
- Avoid use of arch-specific build-requires (#1545195)

* Tue Feb  6 2018 Paul Howarth <paul@city-fan.org> - 1.0.69-2
- ldconfig scriptlets replaced by RPM File Triggers from Fedora 28
- Make zlib-devel dependencies arch-specific
- Preserve upstream timestamps where possible

* Fri Sep 29 2017 Paul Howarth <paul@city-fan.org> - 1.0.69-1
- Update to 1.069
  - Added PNGMINUS_UNUSED macro to contrib/pngminus/p*.c and added missing
    parenthesis in contrib/pngminus/pnm2png.c
  - Compute a larger limit on IDAT because some applications write a deflate
    buffer for each row
  - Initialize memory allocated by png_inflate to zero, using memset, to stop
    an oss-fuzz "use of uninitialized value" detection in png_set_text_2() due
    to truncated iTXt or zTXt chunk

* Fri Aug 25 2017 Paul Howarth <paul@city-fan.org> - 1.0.68-1
- Update to 1.068
  - Added png_check_chunk_length() function, and check all chunks except IDAT
    against the default 8MB limit; check IDAT against the maximum size computed
    from IHDR parameters
  - Check for 0 return from png_get_rowbytes() and added some (size_t)
    typecasts in contrib/pngmi to stop some Coverity issues (162705, 162706
    and 162707)
- Specify explictly-used build requirements

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.67-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Paul Howarth <paul@city-fan.org> - 1.0.67-3
- Update source URL (#1459086)
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Paul Howarth <paul@city-fan.org> - 1.0.67-1
- Update to 1.0.67
  - Fix typos in libpng.3 synopses
  - Fixed undefined behavior in png_push_save_buffer(); do not call memcpy()
    with a null source, even if count is zero
  - Fixed a potential null pointer dereference in png_set_text_2()
    (CVE-2016-10087)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Paul Howarth <paul@city-fan.org> - 1.0.66-1
- Update to 1.0.66
  - Fixed an out-of-range read in png_check_keyword() (CVE-2015-8540)
  - Corrected copyright dates in source files
  - Moved png_check_keyword() from pngwutil.c to pngset.c

* Fri Dec  4 2015 Paul Howarth <paul@city-fan.org> - 1.0.65-1
- Update to 1.0.65
  - Avoid potential pointer overflow in png_handle_iTXt(), png_handle_zTXt(),
    png_handle_sPLT(), and png_handle_pCAL()
  - Fixed incorrect implementation of png_set_PLTE() that uses png_ptr, not
    info_ptr, which left png_set_PLTE() open to the CVE-2015-8126 vulnerability
    (CVE-2015-8472)
  - Discontinued distributing tar.bz2 archives
  - Discontinued distributing libpng-oldversion-newversion-diff.txt
- Switch back to gzipped tarball as upstream is no longer providing the bzipped
  version

* Thu Nov 12 2015 Paul Howarth <paul@city-fan.org> - 1.0.64-1
- Update to 1.0.64
  - Fix typecast in a png_debug2() statement in png_set_text_2() to avoid a
    compiler warning in PNG_DEBUG builds
  - Fixed printf formats in pngtest.c to avoid compiler warnings and a Coverity
    warning in PNG_DEBUG builds
  - Avoid Coverity issue 80858 (REVERSE NULL) in pngtest.c PNG_DEBUG builds
  - Removed WRITE_WEIGHTED_FILTERED code
  - Avoid potentially dereferencing NULL info_ptr in png_info_init_3()
  - Fixed potential leak of png_pixels in contrib/pngminus/pnm2png.c
  - Use nanosleep() instead of usleep() in contrib/gregbook/rpng2-x.c because
    usleep() is deprecated (port from libpng16)
  - Fixed some bad links in the man page
  - Added a safety check in png_set_tIME() (CVE-2015-7981)
  - Prevent writing over-length PLTE chunk (CVE-2015-8126)
  - Silently truncate over-length PLTE chunk while reading (CVE-2015-8126)
  - Clarified COPYRIGHT information to state explicitly that versions are
    derived from previous versions
  - Removed much of the long list of previous versions from png.h and libpng.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Paul Howarth <paul@city-fan.org> - 1.0.63-1
- Update to 1.0.63
  - Issue a png_error() instead of a png_warning() when width is potentially
    too large for the architecture, in case the calling application has
    overridden the default 1,000,000-column limit (fixes CVE-2014-9495 and
    CVE-2015-0973)
  - Quieted some harmless warnings from Coverity-scan
  - Display user limits in the output from pngtest (not packaged)
  - Changed PNG_USER_CHUNK_MALLOC_MAX from unlimited to 8,000,000; it only
    affects the maximum memory that can be allocated to an ancillary chunk,
    and does not limit the size of IDAT data, which is instead limited by
    PNG_USER_WIDTH_MAX
  - Rebuilt configure scripts with automake-1.15 and libtool-2.4.6
- Update soname patch

* Fri Nov 21 2014 Paul Howarth <paul@city-fan.org> 1.0.62-1
- update to 1.0.62
  - avoid out-of-bounds memory access while checking version string in
    pngread.c and pngwrite.c
  - build fix for Windows
- use %%license where possible

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.61-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun  7 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.61-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb  7 2014 Paul Howarth <paul@city-fan.org> 1.0.61-1
- update to 1.0.61
  - ignore, with a warning, out-of-range value of num_trans in png_set_tRNS()
  - replaced AM_CONFIG_HEADER(config.h) with AC_CONFIG_HEADERS([config.h]) in
    configure.ac
  - changed default value of PNG_USER_CACHE_MAX from 0 to 32767 in pngconf.h
  - avoid a possible memory leak in contrib/gregbook/readpng.c
  - revised libpng.3 so that "doclifter" can process it
  - changed '"%%s"m' to '"%%s" m' in png_debug macros to improve portability
    among compilers
  - rebuilt the configure scripts with autoconf-2.69 and automake-1.14.1
  - removed potentially misleading warning from png_check_IHDR()
  - quiet set-but-not-used warnings in pngset.c
  - quiet an uninitialized memory warning from VC2013 in png_get_png()
  - quiet unused variable warnings from clang by porting PNG_UNUSED() from
    libpng-1.4.6
  - added -DZ_SOLO to CFLAGS in contrib/pngminim/*/makefile
  - added an #ifdef PNG_FIXED_POINT_SUPPORTED/#endif in pngset.c
- drop upstreamed aarch64 patch
- drop patch for CVE-2013-6954, which only actually affected libpng versions
  1.6.1 to 1.6.7

* Thu Jan 23 2014 Paul Howarth <paul@city-fan.org> 1.0.60-6
- handle zero-length PLTE chunk or NULL palette with png_error(), to avoid
  later reading from a NULL pointer (png_ptr->palette) in
  png_do_expand_palette() (CVE-2013-6954)

* Sat Jul 27 2013 Paul Howarth <paul@city-fan.org> 1.0.60-5
- install docs to %%{_pkgdocdir} where available

* Sun Mar 24 2013 Paul Howarth <paul@city-fan.org> 1.0.60-4
- tweak config.guess and config.sub to add aarch64 support (#925862)
- update source URL, moved upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.60-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.60-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Paul Howarth <paul@city-fan.org> 1.0.60-1
- update to 1.0.60
  - changed "a+w" to "u+w" in Makefile.in to fix CVE-2012-3386

* Thu Mar 29 2012 Paul Howarth <paul@city-fan.org> 1.0.59-1
- update to 1.0.59
  - revised png_set_text_2() to avoid potential memory corruption
    (CVE-2011-3048)
  - prevent PNG_EXPAND+PNG_SHIFT doing the shift twice

* Fri Mar  9 2012 Paul Howarth <paul@city-fan.org> 1.0.58-1
- update to 1.0.58
  - fix bug with png_handle_hIST with odd chunk length
  - fix incorrect type (int copy should be png_size_t copy) in png_inflate()
    (CVE-2011-3045)
  - fix off-by-one bug in png_handle_sCAL() when using fixed point arithmetic,
    causing out-of-bounds read in png_set_sCAL() because of failure to copy
    the string terminators
  - remove the png_free() of unused png_ptr->current_text from pngread.c
  - remove all of the assembler code from pnggccrd.c and just "return 2;"

* Sun Feb 19 2012 Paul Howarth <paul@city-fan.org> 1.0.57-1
- update to 1.0.57 (fixed CVE-2011-3026 buffer overrun bug)

* Thu Jan  5 2012 Paul Howarth <paul@city-fan.org> 1.0.56-2
- rebuilt for gcc 4.7

* Sat Jul  9 2011 Paul Howarth <paul@city-fan.org> 1.0.56-1
- update to 1.0.56
  - fix regression in Makefile.am/Makefile.in
  - fix "make distcheck"
- drop upstreamed fix for libpng.sym build failure

* Thu Jul  7 2011 Paul Howarth <paul@city-fan.org> 1.0.55-1
- update to 1.0.55
  - fixed uninitialized memory read in png_format_buffer()
    (CVE-2011-2501, related to CVE-2004-0421)
  - pass "" instead of '\0' to png_default_error() in png_err() (CVE-2011-2691)
  - check for up->location !PNG_AFTER_IDAT when writing unknown chunks before
    IDAT
  - ported bugfix in pngrtran.c from 1.5.3: when expanding a paletted image,
    always expand to RGBA if transparency is present
  - check for integer overflow in png_set_rgb_to_gray() (CVE-2011-2690)
  - check for sCAL chunk too short (CVE-2011-2692)
- drop upstreamed patch for CVE-2011-2501
- add patch to fix build failure due to regression in libpng.sym creation

* Wed Jun 29 2011 Paul Howarth <paul@city-fan.org> 1.0.54-3
- fix 1-byte uninitialized memory reference in png_format_buffer()
  (CVE-2011-2501, related to CVE-2004-0421)
- nobody else likes macros for commands

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.54-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul  2 2010 Paul Howarth <paul@city-fan.org> 1.0.54-1
- update to 1.0.54
  - fixes CVE-2010-1205 (out-of-bounds write to memory)
  - fixes CVE-2010-2249 (memory leak with images having malformed sCAL chunks)

* Thu Feb 25 2010 Paul Howarth <paul@city-fan.org> 1.0.53-1
- update to 1.0.53
  - fixes CVE-2010-0205 (libpng stalls on highly compressed ancillary chunks)
- drop patch for #555485, included upstream

* Fri Jan 15 2010 Paul Howarth <paul@city-fan.org> 1.0.52-2
- add upstream fix reinstating PNG_READ_16_TO_8_SUPPORTED and
  PNG_READ_GRAY_TO_RGB_SUPPORTED (not defined in 1.0.51 and 1.0.52),
  causing API/ABI regressions (#555485)

* Mon Jan  4 2010 Paul Howarth <paul@city-fan.org> 1.0.52-1
- update to 1.0.52 (minor changes, see ANNOUNCE for details)

* Thu Dec  3 2009 Paul Howarth <paul@city-fan.org> 1.0.51-1
- update to 1.0.51 (see ANNOUNCE for details)
- update soname patch to apply to 1.0.51

* Fri Sep 11 2009 Paul Howarth <paul@city-fan.org> 1.0.50-1
- update to 1.0.50 (garbage removal patch upstreamed)

* Thu Sep 10 2009 Paul Howarth <paul@city-fan.org> 1.0.49-1
- update to 1.0.49 (minor bugfixes)
- patch out garbage in source files left over from edit gone wrong

* Thu Aug 13 2009 Paul Howarth <paul@city-fan.org> 1.0.48-1
- update to 1.0.48
  - avoid a possible NULL dereference in debug build, in png_set_text_2()
  - reject attempt to write iCCP chunk with negative embedded profile length
- rebase soname patch to remove fuzz

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.47-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Paul Howarth <paul@city-fan.org> 1.0.47-1
- update to 1.0.47 (changes to unknown chunk handling and documentation)

* Thu Jun 18 2009 Paul Howarth <paul@city-fan.org> 1.0.46-1
- garbage removal patch upstreamed

* Thu Jun 18 2009 Paul Howarth <paul@city-fan.org> 1.0.45-2
- patch out garbage in devel config files left over from edit gone wrong

* Thu Jun  4 2009 Paul Howarth <paul@city-fan.org> 1.0.45-1
- update to 1.0.45 (mainly cosmetic code changes)

* Fri May  8 2009 Paul Howarth <paul@city-fan.org> 1.0.44-1
- update to 1.0.44 (fix possible UMR/memory leak issues, revise fflush() usage)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.43-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Paul Howarth <paul@city-fan.org> 1.0.43-1
- update to 1.0.43 (#486355, CVE-2009-0040 - clear pointer arrays created using
  png_malloc())

* Fri Dec 19 2008 Paul Howarth <paul@city-fan.org> 1.0.42-1
- update to 1.0.42 (#480321, CVE-2008-5907 - various minor bugfixes and code
  cleanups, not really a security issue)

* Fri Oct 31 2008 Paul Howarth <paul@city-fan.org> 1.0.41-1
- update to 1.0.41 (#468990, CVE-2008-6218 - memory leak after reading a
  malformed tEXt chunk)

* Fri Sep 19 2008 Paul Howarth <paul@city-fan.org> 1.0.40-1
- update to 1.0.40 (#461599, CVE-2008-3964 - multiple off-by-one errors
  allowing context-dependent attackers to cause a denial of service (crash) or
  have unspecified other impact via a PNG image with crafted zTXt chunks)

* Thu Aug 21 2008 Paul Howarth <paul@city-fan.org> 1.0.39-1
- update to 1.0.39

* Sun Aug 17 2008 Paul Howarth <paul@city-fan.org> 1.0.38-1
- update to 1.0.38
- update soname patch to apply without fuzz

* Fri May  9 2008 Paul Howarth <paul@city-fan.org> 1.0.37-1
- update to 1.0.37
- autotools patch no longer needed
- explicitly specify the library filename in %%files as a consistency check

* Wed Apr 30 2008 Paul Howarth <paul@city-fan.org> 1.0.34-1
- update to 1.0.34
- update autotools patch

* Wed Apr 30 2008 Paul Howarth <paul@city-fan.org> 1.0.33-1
- update to 1.0.33 (CVE-2008-1382, #441839)
- add patch to fix broken autotools build scripts

* Thu Apr  3 2008 Paul Howarth <paul@city-fan.org> 1.0.32-1
- update to 1.0.32

* Tue Feb 19 2008 Paul Howarth <paul@city-fan.org> 1.0.31-1
- update to 1.0.31

* Wed Feb 13 2008 Paul Howarth <paul@city-fan.org> 1.0.30-2
- rebuild with gcc 4.3.0 for Fedora 9

* Tue Oct 16 2007 Paul Howarth <paul@city-fan.org> 1.0.30-1
- update to 1.0.30

* Fri Oct  5 2007 Paul Howarth <paul@city-fan.org> 1.0.29-1
- update to 1.0.29 (fixes DoS issue, #327791, CVE-2007-5269)

* Tue Sep 11 2007 Paul Howarth <paul@city-fan.org> 1.0.28-1
- update to 1.0.28

* Mon Aug 20 2007 Paul Howarth <paul@city-fan.org> 1.0.27-1
- update to 1.0.27
- add new file ANNOUNCE, which lists changes since last release
- use shortname "zlib" for the license tag (package is zlib/libpng licensed)
- drop pkgconf patch, which should no longer be needed

* Sun May 20 2007 Paul Howarth <paul@city-fan.org> 1.0.26-1
- update to 1.0.26 to address DoS issue (#240398, CVE-2007-2445)
- update soname patch
- libpng.txt now has a versioned filename

* Sun Mar 25 2007 Paul Howarth <paul@city-fan.org> 1.0.21-2
- Own directory %%{_docdir}/%%{name}-%%{version} (#233869)
- Describe license as "zlib/libpng" rather than just "zlib"

* Sat Nov 18 2006 Paul Howarth <paul@city-fan.org> 1.0.21-1
- update to 1.0.21 to address DoS issue (#216263, CVE-2006-5793)
- update soname patch

* Sun Oct  1 2006 Paul Howarth <paul@city-fan.org> 1.0.20-4
- rebuild with latest toolchain

* Tue Aug  1 2006 Paul Howarth <paul@city-fan.org> 1.0.20-3
- reenable %%{_smp_mflags}
- use patched configure script rather than old Makefiles

* Thu Jul 20 2006 Paul Howarth <paul@city-fan.org> 1.0.20-2
- don't use %%{_smp_mflags}

* Thu Jul  6 2006 Paul Howarth <paul@city-fan.org> 1.0.20-1
- update to 1.0.20
- use Fedora Extras standard buildroot
- update URL
- include release in fully versioned dependency between devel and main pkgs
- wrap description text at 80 columns
- don't build static libraries
- devel package requires pkgconfig
- unpack tarball quietly
- update rhconf patch
- move doc files libpng.txt and example.c to devel package
- add doc Y2KINFO
- changed license tag from "OSI Certified" to "zlib License"
  (see http://www.opensource.org/licenses/zlib-license.php)
- minor cosmetic spec file changes

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.18-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.18-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Jul 31 2005 Florian La Roche <laroche@redhat.com>
- build with newest rpm, rm -f libpng.so

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 1.0.18-2
- Rebuild with gcc4

* Mon Dec 06 2004 Matthias Clasen <mclasen@redhat.com> - 1.0.18-1
- Update to 1.0.18

* Tue Aug 17 2004 Matthias Clasen <mclasen@redhat.com> - 1.0.16-1
- Update to 1.0.16
- Combine rhconf patches
- Include LICENSE

* Wed Aug 4 2004 Matthias Clasen <mclasen@redhat.com> 1.0.15-9
- Build for FC3

* Fri Jul 23 2004 Matthias Clasen <mclasen@redhat.com> 1.0.15-8
- Build for FC2

* Fri Jul 23 2004 Matthias Clasen <mclasen@redhat.com> 1.0.15-7
- Replace the patches for individual security problems with the
  cumulative patch issued by the png developers.
- Build for FC1

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 14 2004 Matthias Clasen <mclasen@redhat.com> - 1.0.15-5
- Rebuilt for FC2

* Mon Jun 14 2004 Matthias Clasen <mclasen@redhat.com> - 1.0.15-4
- Rebuilt for FC1

* Mon Jun 14 2004 Matthias Clasen <mclasen@redhat.com> - 1.0.15-3
- Reinstate and improve the transfix patch which got lost sometime ago,
  but is still needed for CAN-2002-1363 (#125934)

* Wed May 19 2004 Matthias Clasen <mclasen@redhat.com> 1.0.15-2
- Don't provide libpng-devel (#110161)

* Wed May 19 2004 Matthias Clasen <mclasen@redhat.com> 1.0.15-1
- 1.0.15
- Update rhconf2 patch
- Remove bogus badchunks patch (#89854)

* Mon May 03 2004 Matthias Clasen <mclasen@redhat.com> 1.0.13-13
- Redo the out-of-bounds fix in a slightly better way.

* Wed Apr 21 2004 Matthias Clasen <mclasen@redhat.com> 1.0.13-12
- Bump release number to disambiguate n-v-rs.

* Mon Apr 19 2004 Matthias Clasen <mclasen@redhat.com>
- fix a possible out-of-bounds read in the error message
  handler. #121229

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 9 2003  Elliot Lee <sopwith@redhat.com>
- This package has no epochs! remove usage thereof

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Elliot Lee <sopwith@redhat.com> 1.0.13-7
- Bump & rebuild

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 1.0.13-6
- Rebuild, merging in multilib change

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Elliot Lee <sopwith@redhat.com> 1.0.13-3
- The package totally broke the backwards compatibility that it was intended to provide.
  Fixed by setting soname to libpng.so.2, and only tweaking the build (libpng*.{so,a}) files.
- Use _smp_mflags
- Fix rhconf patch because it was patching a symlink instead of the actual file.
- Don't provide libpng = {version}, because then the package conflicts with itself

* Thu May  9 2002 Jeremy Katz <katzj@redhat.com> 1.0.13-2
- rebuild

* Thu May  2 2002 Havoc Pennington <hp@redhat.com> 1.0.13-1
- upgrade to 1.0.13, plus patch tarball from libpng web site
- update rhconf patch to work with new makefiles

* Mon Mar  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.12-6
- Revert fix for #59988 as it introduces a worse problem, #60410

* Tue Feb 26 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.12-5
- Conflict with libpng < 1.2.0 (#59988)

* Wed Jan 30 2002 Bill Nottingham <notting@redhat.com> 1.0.12-4
- provide libpng = %%{version}, libpng-devel = %%{version}

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jan  4 2002 Bill Nottingham <notting@redhat.com> 1.0.12-2
- add devel stuff (we may change this around later)

* Wed Sep 19 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.12-1
- initial compat package
