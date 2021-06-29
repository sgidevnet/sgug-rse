# http://sourceforge.net/projects/mhash
# As of 2007-08-18 11:03, this project is no longer under active development.

Summary: Thread-safe hash algorithms library
Name: mhash
Version: 0.9.9.9
Release: 20%{?dist}
URL: http://mhash.sourceforge.net/
License: LGPLv2+
Source: http://downloads.sourceforge.net/mhash/mhash-%{version}.tar.bz2
Patch2: mhash-0.9.9.9-align.patch
Patch3: mhash-0.9.9.9-force64bit-tiger.patch
# Taken from Gentoo: 
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-fix-snefru-segfault.patch
Patch4: mhash-0.9.9.9-fix-snefru-segfault.patch
# Taken from Gentoo:
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-fix-mem-leak.patch
Patch5: mhash-0.9.9.9-fix-mem-leak.patch
# Taken from Gentoo:
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-fix-whirlpool-segfault.patch
Patch6: mhash-0.9.9.9-fix-whirlpool-segfault.patch
# Taken from Gentoo:
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-autotools-namespace-stomping.patch
Patch7: mhash-0.9.9.9-autotools-namespace-stomping.patch
# Taken from openpkg:
# http://www.mail-archive.com/openpkg-cvs@openpkg.org/msg26353.html
Patch8: mhash-0.9.9.9-maxint.patch
# Taken from Jitesh Shah
# http://ftp.uk.linux.org/pub/armlinux/fedora/diffs-f11/mhash/0001-Alignment-fixes.patch
Patch9: mhash-0.9.9.9-alignment.patch
# Fix keygen_test
Patch10: mhash-0.9.9.9-keygen_test_fix.patch
# Fix mhash_test
# Credit to Hanno Böck back in 2015.
Patch11: mhash-0.9.9-no-free-before-use.patch

BuildRequires:  gcc
BuildRequires: autoconf, automake
Provides: libmhash = %{version}-%{release}

%description
Mhash is a free library which provides a uniform interface to a
large number of hash algorithms.

These algorithms can be used to compute checksums, message digests,
and other signatures. The HMAC support implements the basics for
message authentication, following RFC 2104. In the later versions
some key generation algorithms, which use hash algorithms, have been
added. Currently, the library supports the algorithms: ADLER32, GOST,
HAVAL256, HAVAL224, HAVAL192, HAVAL160, HAVAL128, MD5, MD4, MD2,
RIPEMD128/160/256/320, TIGER, TIGER160, TIGER128, SHA1/224/256/384/512,
Whirlpool, SNEFRU128/256, CRC32B and CRC32 checksums.


%package -n %{name}-devel
Summary: Header files and libraries for developing apps which use mhash
Requires: %{name} = %{version}-%{release}
Provides: libmhash-devel = %{version}-%{release}

%description -n %{name}-devel
This package contains the header files and libraries needed to
develop programs that use the mhash library.


%prep
%setup -q
%patch2 -p1 -b .alignment
%patch3 -p1 -b .force64bit-tiger
%patch4 -p1 -b .fix-snefru-segfault
%patch5 -p1 -b .fix-mem-leak
%patch6 -p1 -b .fix-whirlpool-segfault
%patch7 -p1 -b .fix-autotool-stomping
%patch8 -p1 -b .maxint
%patch9 -p1 -b .alignment2
%patch10 -p1 -b .fix
%patch11 -p1 -b .nofree
autoconf

%build
%configure --enable-shared %{?_with_static: --enable-static} %{!?_with_static: --disable-static}

# If this exits, the multiarch patch needs an update.
grep 'define SIZEOF_' include/mutils/mhash_config.h && exit 1

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

# Eliminate some autoheader definitions which should not enter a public API.
# There are more which wait for a fix upstream.
sed -i 's!\(#define \(PACKAGE\|VERSION \).*\)!/* \1 */!g' ${RPM_BUILD_ROOT}%{_includedir}/mutils/mhash_config.h


%check
make check


%ldconfig_scriptlets -n %{name}



%files -n %{name}
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_libdir}/*.so.*


%files -n %{name}-devel
%doc ChangeLog ./doc/*.c ./doc/skid2-authentication
%{_includedir}/*.h
%{_includedir}/mutils/
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%exclude %{_libdir}/*.la
%{_mandir}/man3/*


%changelog
* Mon Jul 29 2019 Tom Callaway <spot@fedoraproject.org> - 0.9.9.9-20
- fix mhash_test (thanks to Hanno Böck for posting a fix back in 2015)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.9.9-2
- bump rawhide, fixed the last bug

* Wed Jul 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.9.9-1
- update to 0.9.9.9
- apply all the fixes that I could find

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Dennis Gilmore <dennis@ausil.us> - 0.9.9-6
- fix memory alignment issues

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.9-5
- Autorebuild for GCC 4.3

* Tue Oct 23 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.9-4
- Remove AC_CHECK_SIZEOF definitions from mhash_config.h
  since stdint.h is used. Add a guard after running configure.
  This shall fix the multiarch conflict in mhash-devel (#342601).

* Tue Aug 21 2007 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Aug  2 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.9-2
- Clarify licence (LGPLv2+).

* Fri Apr  6 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.9-1
- Update to 0.9.9 (bug-fixes).

* Mon Feb 19 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.8-1
- Update to 0.9.8 (includes the patch).

* Fri Feb  2 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.7.1-4
- Fix big-endian memory leaks in haval.c
- Patch is sufficient to pass test-suite on ppc. Fixes #226987.

* Fri Feb  2 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.7.1-2
- Add check section.

* Sat Nov 25 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.7.1-1
- Update to 0.9.7.1.

* Mon Aug 28 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-5
- rebuilt

* Wed Feb 22 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-4
- rebuilt for FC5
- Disable static library.

* Thu May 12 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-3
- rebuilt

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-2
- rebuilt

* Wed Jan 12 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9.2-1
- Update to 0.9.2.

* Sun Apr 18 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9.1-0.fdr.1
- Update to 0.9.1.
- Add EVR to virtual provides.
- Move some doc files into the main package.

* Tue Aug 12 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.8.18-0.fdr.1
- Initial package.

