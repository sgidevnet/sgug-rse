# This package is able to use optimised linker flags.
# Nope, can't otherwise it skips out on linking in pthread
#%%global build_ldflags %%{sgug_optimised_ldflags}

# Not needed for f21+ and probably RHEL8+
%{!?_licensedir:%global license %%doc}

Summary:	LZMA compression utilities
Name:		xz
Version:	5.2.4
Release:	7%{?dist}

# Scripts xz{grep,diff,less,more} and symlinks (copied from gzip) are
# GPLv2+, binaries are Public Domain (linked against LGPL getopt_long but its
# OK), documentation is Public Domain.
License:	GPLv2+ and Public Domain
# official upstream release
Source0:	http://tukaani.org/%{name}/%{name}-%{version}.tar.xz

Source100:	colorxzgrep.sh
Source101:	colorxzgrep.csh

URL:		http://tukaani.org/%{name}/
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

# For /usr/libexec/grepconf.sh (RHBZ#1189120).
# Unfortunately F21 has a newer version of grep which doesn't
# have grepconf, but we're only concerned with F22 here.
Requires:	grep >= 2.20-5

BuildRequires:	gcc
BuildRequires:	perl-interpreter


%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.


%package 	libs
Summary:	Libraries for decoding LZMA compression
License:	Public Domain
Obsoletes:	%{name}-compat-libs < %{version}-%{release}

%description 	libs
Libraries for decoding files compressed with LZMA or XZ utils.


%package 	static
Summary:	Statically linked library for decoding LZMA compression
License:	Public Domain

%description 	static
Statically linked library for decoding files compressed with LZMA or
XZ utils.  Most users should *not* install this.


%package 	devel
Summary:	Devel libraries & headers for liblzma
License:	Public Domain
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
Devel libraries and headers for liblzma.


%package 	lzma-compat
Summary:	Older LZMA format compatibility binaries
# Just a set of symlinks to 'xz' + two Public Domain binaries.
License:	Public Domain
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	lzma < %{version}
Provides:	lzma = %{version}

%description	lzma-compat
The lzma-compat package contains compatibility links for older
commands that deal with the older LZMA format.


%prep
%autosetup


%build
export CFLAGS="$RPM_OPT_FLAGS"

%ifarch %{power64}
  CFLAGS="$CFLAGS -O3"
%endif

%ifarch %ix86
  # rhbz#1630650, annocheck reports the following message because liblzma uses
  # crc*_x86.S asm code on i686:
  CFLAGS="$CFLAGS -Wa,--generate-missing-build-notes=yes"
%endif

# liblzma has undefined pthread symbols without this
export LIBS="-lpthread"

%configure
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# xzgrep colorization
%global profiledir %{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE100} %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE101} %{buildroot}%{profiledir}

%find_lang %name


%check
LD_LIBRARY_PATH=$PWD/src/liblzma/.libs make check

%ldconfig_scriptlets libs


%files -f %{name}.lang
%license %{_pkgdocdir}/COPYING*
%doc %{_pkgdocdir}
%exclude %_pkgdocdir/examples*
%{_bindir}/*xz*
%{_mandir}/man1/*xz*
%{profiledir}/*


%files libs
%license %{_pkgdocdir}/COPYING
%{_libdir}/lib*.so.5*


%files static
%license %{_pkgdocdir}/COPYING
%{_libdir}/liblzma.a


%files devel
%dir %{_includedir}/lzma
%{_includedir}/lzma/*.h
%{_includedir}/lzma.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/liblzma.pc
%doc %_pkgdocdir/examples*


%files lzma-compat
%{_bindir}/*lz*
%{_mandir}/man1/*lz*


%changelog
* Thu May 21 2020 Daniel Hams <daniel.hams@gmail.com> - 5.2.4-7
- Add pthread lib during link to avoid unresolved symbols from things using this.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Pavel Raiskup <praiskup@redhat.com> - 5.2.4-4
- fix annocheck failures on i686 (rhbz#1630650)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Pavel Raiskup <praiskup@redhat.com> - 5.2.4-2
- drop ppc64p7 hack, per fedora devel list discussion:
  https://lists.fedoraproject.org/archives/list/
  devel@lists.fedoraproject.org/thread/2OWD2QRDFBEC6HTPVQ7FMJENH32BWT54/
- don't explicitly set _FILE_OFFSET_BITS, package uses AC_SYS_LARGEFILE

* Tue May 08 2018 Pavel Raiskup <praiskup@redhat.com> - 5.2.4-1
- rebase to 5.2.4 (rhbz#1574039), per release notes:
  https://www.mail-archive.com/xz-devel@tukaani.org/msg00295.html

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.2.3-6
- Switch to %%ldconfig_scriptlets

* Wed Sep 13 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 5.2.3.-5
- Cleanup spec

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Pavel Raiskup <praiskup@redhat.com> - 5.2.3-1
- rebase to stable 5.2.3 per release notes:
  http://www.mail-archive.com/xz-devel@tukaani.org/msg00285.html

* Mon Nov 28 2016 Lubomir Rintel <lkundrak@v3.sk> - 5.2.2-3
- Fix FTBFS by requiring Perl

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Pavel Raiskup <praiskup@redhat.com> - 5.2.2-1
- rebase to stable 5.2.2 per release notes:
  http://www.mail-archive.com/xz-devel@tukaani.org/msg00244.html

* Thu Jul 09 2015 Pavel Raiskup <praiskup@redhat.com> - 5.2.1-3
- remove xz-compat-libs as it is not necessary (#1179193)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Pavel Raiskup <praiskup@redhat.com> - 5.2.1-1
- bugfix rebase to 5.2.1, per release notes
  http://www.mail-archive.com/xz-devel@tukaani.org/msg00226.html

* Wed Feb 04 2015 Richard W.M. Jones <rjones@redhat.com> - 5.2.0-2
- Depend on grep that contains grepconf.sh (#1189120)

* Tue Dec 23 2014 Pavel Raiskup <praiskup@redhat.com> - 5.2.0-1
- rebase per upstream release notes (#1023718)
  http://www.mail-archive.com/xz-devel@tukaani.org/msg00216.html
- fedora-review fixes, documentation/license fixes in spec

* Tue Aug 26 2014 Pavel Raiskup <praiskup@redhat.com> - 5.1.2-15alpha
- xz*grep's output is colored iff grep's is (#1034846)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-14alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug  6 2014 Tom Callaway <spot@fedoraproject.org> - 5.1.2-13alpha
- fix license handling

* Fri Jun 13 2014 Pavel Raiskup <praiskup@redhat.com> - 5.1.2-12alpha
- xzgrep: return 0 when at least one file matches (#1109122)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-11alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Peter Robinson <pbrobinson@fedoraproject.org> 5.1.2-10alpha
- Drop ChangeLog, it's big and the excitement is summarised in NEWS

* Fri May 16 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.2-9alpha
- Add a -static subpackage (see RHBZ#547011).

* Wed Apr 02 2014 Pavel Raiskup <praiskup@redhat.com> - 5.1.2-8alpha
- add _isa requirements where appropriate
- better check the version of less binary (#1015924)

* Fri Jan 10 2014 Pavel Raiskup <praiskup@redhat.com> - 5.1.2-7alpha
- build with -O3 on ppc64 (private #1051078)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-6alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 09 2013 Pavel Raiskup <praiskup@redhat.com> - 5.1.2-5alpha
- fix manual page inconsistencies with help output (private #948533)
- enable/fix the 'xzgrep -h' (private #850898)

* Thu Feb 21 2013 Karsten Hopp <karsten@redhat.com> 5.1.2-4alpha
- add support for ppc64p7 arch (Power7 optimized)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-3alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-2alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Jindrich Novy <jnovy@redhat.com> 5.1.2alpha-1
- update to 5.1.2alpha

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-2alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Jindrich Novy <jnovy@redhat.com> 5.1.1alpha-1
- update to 5.1.1alpha

* Mon Jun 20 2011 Jindrich Novy <jnovy@redhat.com> 5.0.3-2
- better to have upstream tarballs in different formats than XZ
  to allow bootstrapping (#714765)

* Mon May 23 2011 Jindrich Novy <jnovy@redhat.com> 5.0.3-1
- update to 5.0.3

* Mon Apr 04 2011 Jindrich Novy <jnovy@redhat.com> 5.0.2-1
- update to 5.0.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Jindrich Novy <jnovy@redhat.com> 5.0.1-1
- update to 5.0.1

* Tue Oct 26 2010 Jindrich Novy <jnovy@redhat.com> 5.0.0-4
- call ldconfig for compat-libs and fix description

* Mon Oct 25 2010 Jindrich Novy <jnovy@redhat.com> 5.0.0-3
- introduce compat-libs subpackage with older soname to
  resolve problems with soname bump and for packages requiring
  older xz-4.999.9beta

* Mon Oct 25 2010 Jindrich Novy <jnovy@redhat.com> 5.0.0-2
- rebuild

* Mon Oct 25 2010 Jindrich Novy <jnovy@redhat.com> 5.0.0-1
- update to the new upstream release

* Sat Oct 16 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.3.beta.212.gacbc
- update to latest git snapshot

* Thu Apr 01 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.2.20100401.beta
- sync with upstream (#578925)

* Thu Feb 18 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.2.20091007.beta
- move xz man pages to main package, leave lzma ones where they belong (#566484)

* Wed Oct 07 2009 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.20091007.beta
- sync with upstream again

* Fri Oct 02 2009 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.20091002.beta
- sync with upstream to generate the same archives on machines with different
  endianess

* Fri Aug 28 2009 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta
- update to 4.999.9beta

* Mon Aug 17 2009 Jindrich Novy <jnovy@redhat.com> 4.999.8-0.10.beta.20090817git
- sync with upstream because of #517806

* Tue Aug 04 2009 Jindrich Novy <jnovy@redhat.com> 4.999.8-0.9.beta.20090804git
- update to the latest GIT snapshot

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.8-0.8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Bill Nottingham <notting@redhat.com> 4.999.8-0.7.beta
- tweak summary
- add %%check section (<tibbs@math.uh.edu>)
 
* Thu Jul 09 2009 Bill Nottingham <notting@redhat.com> 4.999.8-0.6.beta
- fix release versioning to match guidelines
- fix up lzma-compat summary/description
- tweak licensing

* Mon Jun 22 2009 Jindrich Novy <jnovy@redhat.com> 4.999.8beta-0.5
- introduce lzma-compat subpackage

* Fri Jun 19 2009 Jindrich Novy <jnovy@redhat.com> 4.999.8beta-0.4
- try to not to conflict with lzma

* Thu Jun 18 2009 Jindrich Novy <jnovy@redhat.com> 4.999.8beta-0.3
- obsolete but don't provide lzma, they are largely incompatible
- put beta to Release

* Wed Jun 17 2009 Jindrich Novy <jnovy@redhat.com> 4.999.8beta-0.2
- obsolete old lzma
- add Requires: pkgconfig

* Tue Jun 16 2009 Jindrich Novy <jnovy@redhat.com> 4.999.8beta-0.1
- package XZ Utils, based on LZMA Utils packaged by Per Patrice Bouchand
