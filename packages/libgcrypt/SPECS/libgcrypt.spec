Name: libgcrypt
Version: 1.8.5
Release: 1%{?dist}
URL: http://www.gnupg.org/
Source0: libgcrypt-%{version}-hobbled.tar.xz
# The original libgcrypt sources now contain potentially patented ECC
# cipher support. We have to remove it in the tarball we ship with
# the hobble-libgcrypt script. 
# (We replace it with RH approved ECC in Source4-5)
#Source0: ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-{version}.tar.bz2
#Source1: ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-{version}.tar.bz2.sig
Source2: wk@g10code.com
Source3: hobble-libgcrypt
# Approved ECC support
Source4: ecc-curves.c
Source5: curves.c
Source6: t-mpi-point.c
Source7: random.conf
# make FIPS hmac compatible with fipscheck - non upstreamable
# update on soname bump
Patch2: libgcrypt-1.6.2-use-fipscheck.patch
# modify FIPS RSA and DSA keygen to comply with requirements
Patch5: libgcrypt-1.8.4-fips-keygen.patch
# fix the tests to work correctly in the FIPS mode
Patch6: libgcrypt-1.8.4-tests-fipsmode.patch
# update the CAVS tests
Patch7: libgcrypt-1.7.3-fips-cavs.patch
# use poll instead of select when gathering randomness
Patch11: libgcrypt-1.8.4-use-poll.patch
# slight optimalization of mpicoder.c to silence Valgrind (#968288)
Patch13: libgcrypt-1.6.1-mpicoder-gccopt.patch
# fix tests to work with approved ECC
Patch14: libgcrypt-1.7.3-ecc-test-fix.patch
# Run the FIPS mode initialization in the shared library constructor
Patch18: libgcrypt-1.8.3-fips-ctor.patch
# Block some operations if in FIPS non-operational state
Patch22: libgcrypt-1.7.3-fips-reqs.patch
# Do not try to open /dev/urandom if getrandom() works
Patch24: libgcrypt-1.8.4-getrandom.patch
# CMAC selftest for FIPS POST
Patch25: libgcrypt-1.8.3-cmac-selftest.patch
# Continuous FIPS entropy test
Patch26: libgcrypt-1.8.3-fips-enttest.patch
# Disable non-approved FIPS hashes in the enforced FIPS mode
Patch27: libgcrypt-1.8.3-md-fips-enforce.patch

%define gcrylibdir %{_libdir}

# Technically LGPLv2.1+, but Fedora's table doesn't draw a distinction.
# Documentation and some utilities are GPLv2+ licensed. These files
# are in the devel subpackage.
License: LGPLv2+
Summary: A general-purpose cryptography library
BuildRequires: gcc
BuildRequires: gawk, libgpg-error-devel >= 1.11, pkgconfig
#BuildRequires: fipscheck
# This is needed only when patching the .texi doc.
BuildRequires: texinfo

%package devel
Summary: Development files for the %{name} package
License: LGPLv2+ and GPLv2+
Requires: libgpg-error-devel
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This is a development version.

%description devel
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This package contains files needed to develop
applications using libgcrypt.

%prep
%setup -q
%{SOURCE3}
#%%patch2 -p1 -b .use-fipscheck
#%%patch5 -p1 -b .fips-keygen
#%%patch6 -p1 -b .tests-fipsmode
%patch7 -p1 -b .cavs
%patch11 -p1 -b .use-poll
%patch13 -p1 -b .gccopt
%patch14 -p1 -b .eccfix
#%%patch18 -p1 -b .fips-ctor
#%%patch22 -p1 -b .fips-reqs
%patch24 -p1 -b .getrandom
%patch25 -p1 -b .cmac-selftest
#%%patch26 -p1 -b .fips-enttest
#%%patch27 -p1 -b .fips-enforce

cp %{SOURCE4} cipher/
cp %{SOURCE5} %{SOURCE6} tests/

%build
%configure --disable-static \
%ifarch sparc64
     --disable-asm \
%endif
     --enable-noexecstack \
     --enable-pubkey-ciphers='dsa elgamal rsa ecc' \
     --disable-O-flag-munging

#     --enable-hmac-binary-check \
#

#sed -i -e '/^sys_lib_dlsearch_path_spec/s,/lib /usr/lib,/usr/lib /lib64 /usr/lib64 /lib,g' libtool
make %{?_smp_mflags}

%check
#fipshmac src/.libs/libgcrypt.so.??
make check

# Add generation of HMAC checksums of the final stripped binaries 
#%%define __spec_install_post \
#    %{?__debug_package:%{__debug_install_post}} \
#    %{__arch_install_post} \
#    %{__os_install_post} \
#    fipshmac $RPM_BUILD_ROOT%{gcrylibdir}/*.so.?? \
#%%{nil}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Change /usr/lib64 back to /usr/lib.  This saves us from having to patch the
# script to "know" that -L/usr/lib64 should be suppressed, and also removes
# a file conflict between 32- and 64-bit versions of this package.
# Also replace my_host with none.
#sed -i -e 's,^libdir="/usr/lib.*"$,libdir="/usr/lib",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config
sed -i -e 's,^my_host=".*"$,my_host="none",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config

rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir ${RPM_BUILD_ROOT}/%{_libdir}/*.la
#/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_libdir}

%if "%{gcrylibdir}" != "%{_libdir}"
# Relocate the shared libraries to %{gcrylibdir}.
mkdir -p $RPM_BUILD_ROOT%{gcrylibdir}
for shlib in $RPM_BUILD_ROOT%{_libdir}/*.so* ; do
	if test -L "$shlib" ; then
		rm "$shlib"
	else
		mv "$shlib" $RPM_BUILD_ROOT%{gcrylibdir}/
	fi
done

# Add soname symlink.
#/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_lib}/
%endif

# Overwrite development symlinks.
export PREV_WD=`pwd`
cd $RPM_BUILD_ROOT/%{gcrylibdir}
for shlib in lib*.so.?? ; do
	target=$RPM_BUILD_ROOT/%{_libdir}/`echo "$shlib" | sed -e 's,\.so.*,,g'`.so
%if "%{gcrylibdir}" != "%{_libdir}"
	shlib=%{gcrylibdir}/$shlib
%endif
	ln -sf $shlib $target
done
cd $PREV_WD

# Create /etc/gcrypt (hardwired, not dependent on the configure invocation) so
# that _someone_ owns it.
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/gcrypt
install -m644 %{SOURCE7} $RPM_BUILD_ROOT/etc/gcrypt/random.conf

#%%ldconfig_scriptlets

%files
%dir /etc/gcrypt
%config(noreplace) /etc/gcrypt/random.conf
%{gcrylibdir}/libgcrypt.so.*
#%%{gcrylibdir}/.libgcrypt.so.*.hmac
%{!?_licensedir:%global license %%doc}
%license COPYING.LIB
%doc AUTHORS NEWS THANKS

%files devel
%{_bindir}/%{name}-config
%{_bindir}/dumpsexp
%{_bindir}/hmac256
%{_bindir}/mpicalc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgcrypt.pc
%{_datadir}/aclocal/*
%{_mandir}/man1/*

%{_infodir}/gcrypt.info*
%{!?_licensedir:%global license %%doc}
%license COPYING

%changelog
* Tue Sep  3 2019 Tomáš Mráz <tmraz@redhat.com> 1.8.5-1
- new upstream version 1.8.5
- add CMAC selftest for FIPS POST
- add continuous FIPS entropy test
- disable non-approved FIPS hashes in the enforced FIPS mode

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Tomáš Mráz <tmraz@redhat.com> 1.8.4-3
- fix the build tests to pass in the FIPS mode

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Tomáš Mráz <tmraz@redhat.com> 1.8.4-1
- new upstream version 1.8.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Tomáš Mráz <tmraz@redhat.com> 1.8.3-2
- make only_urandom a default in non-presence of configuration file
- run the full FIPS selftests only when the library is called from
  application

* Thu Jun 14 2018 Tomáš Mráz <tmraz@redhat.com> 1.8.3-1
- new upstream version 1.8.3

* Tue Feb  6 2018 Tomáš Mráz <tmraz@redhat.com> 1.8.2-2
- fix behavior when getrandom syscall is not present (#1542453)

* Thu Dec 21 2017 Tomáš Mráz <tmraz@redhat.com> 1.8.2-1
- new upstream version 1.8.2

* Tue Dec  5 2017 Tomáš Mráz <tmraz@redhat.com> 1.8.1-3
- do not try to access() /dev/urandom either if getrandom() works

* Mon Dec  4 2017 Tomáš Mráz <tmraz@redhat.com> 1.8.1-2
- do not try to open /dev/urandom if getrandom() works (#1380866)

* Tue Sep  5 2017 Tomáš Mráz <tmraz@redhat.com> 1.8.1-1
- new upstream version 1.8.1

* Wed Aug 16 2017 Tomáš Mráz <tmraz@redhat.com> 1.8.0-1
- new upstream version 1.8.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Tomáš Mráz <tmraz@redhat.com> 1.7.8-1
- new upstream version 1.7.8

* Fri Jun  2 2017 Tomáš Mráz <tmraz@redhat.com> 1.7.7-1
- new upstream version 1.7.7
- GOST is now enabled

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Tomáš Mráz <tmraz@redhat.com> 1.7.6-1
- new upstream version 1.7.6

* Fri Dec 16 2016 Tomáš Mráz <tmraz@redhat.com> 1.7.5-1
- new upstream version 1.7.5

* Wed Nov 23 2016 Tomáš Mráz <tmraz@redhat.com> 1.7.3-1
- new upstream version 1.7.3

* Wed Aug 17 2016 Tomáš Mráz <tmraz@redhat.com> 1.6.6-1
- new upstream version with important security fix (CVE-2016-6316)

* Thu Jul 21 2016 Tomáš Mráz <tmraz@redhat.com> 1.6.5-1
- new upstream version fixing low impact issue CVE-2015-7511

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep  9 2015 Tomáš Mráz <tmraz@redhat.com> 1.6.4-1
- new upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr  3 2015 Tomáš Mráz <tmraz@redhat.com> 1.6.3-4
- deinitialize the RNG after the selftest is run

* Tue Mar 24 2015 Tomáš Mráz <tmraz@redhat.com> 1.6.3-3
- touch only urandom in the selftest and when /dev/random is
  unavailable for example by SELinux confinement
- fix the RSA selftest key (p q swap) (#1204517)

* Fri Mar 13 2015 Tomáš Mráz <tmraz@redhat.com> 1.6.3-2
- do not use strict aliasing for bufhelp functions (#1201219)

* Fri Mar  6 2015 Tomáš Mráz <tmraz@redhat.com> 1.6.3-1
- new upstream version

* Wed Feb 25 2015 Tomáš Mráz <tmraz@redhat.com> 1.6.2-4
- do not initialize secure memory during the selftest (#1195850)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.6.2-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Jan 14 2015 Tomáš Mráz <tmraz@redhat.com> 1.6.2-2
- fix buildability of programs using gcrypt.h with -ansi (#1182200)

* Mon Dec  8 2014 Tomáš Mráz <tmraz@redhat.com> 1.6.2-1
- new upstream version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Tom Callaway <spot@fedoraproject.org> - 1.6.1-6
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Kyle McMartin <kyle@fedoraproject.org> 1.6.1-4
- Re-enable below algos, apply patch from upstream list to make
  that code -fPIC friendly. (rhbz#1069792)

* Mon May 19 2014 Kyle McMartin <kyle@fedoraproject.org> 1.6.1-3
- Disable rijndael, cast5, camellia ARM assembly, as it's non-PIC as
  presently written, which results in .text relocations in the shared
  library. (rhbz#1069792)

* Thu Apr 24 2014 Tomáš Mráz <tmraz@redhat.com> 1.6.1-2
- drop the temporary compat shared library version
- fix the soname version in -use-fipscheck.patch

* Fri Feb 28 2014 Tomáš Mráz <tmraz@redhat.com> 1.6.1-1
- new upstream version breaking ABI compatibility
- this release temporarily includes old compatibility .so

* Tue Jan 21 2014 Tomáš Mráz <tmraz@redhat.com> 1.5.3-3
- add back the nistp521r1 EC curve
- fix a bug in the Whirlpool hash implementation
- speed up the PBKDF2 computation

* Sun Oct 20 2013 Tom Callaway <spot@fedoraproject.org> - 1.5.3-2
- add cleared ECC support

* Fri Jul 26 2013 Tomáš Mráz <tmraz@redhat.com> 1.5.3-1
- new upstream version fixing cache side-channel attack on RSA private keys

* Thu Jun 20 2013 Tomáš Mráz <tmraz@redhat.com> 1.5.2-3
- silence false error detected by valgrind (#968288)

* Thu Apr 25 2013 Tomáš Mráz <tmraz@redhat.com> 1.5.2-2
- silence strict aliasing warning in Rijndael
- apply UsrMove
- spec file cleanups

* Fri Apr 19 2013 Tomáš Mráz <tmraz@redhat.com> 1.5.2-1
- new upstream version

* Wed Mar 20 2013 Tomas Mraz <tmraz@redhat.com> 1.5.1-1
- new upstream version

* Tue Mar  5 2013 Tomas Mraz <tmraz@redhat.com> 1.5.0-11
- use poll() instead of select() when gathering randomness (#913773)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan  3 2013 Tomas Mraz <tmraz@redhat.com> 1.5.0-9
- allow empty passphrase in PBKDF2 needed for cryptsetup (=891266)

* Mon Dec  3 2012 Tomas Mraz <tmraz@redhat.com> 1.5.0-8
- fix multilib conflict in libgcrypt-config
- fix minor memory leaks and other bugs found by Coverity scan

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr  5 2012 Tomas Mraz <tmraz@redhat.com> 1.5.0-5
- Correctly rebuild the info documentation

* Wed Apr  4 2012 Tomas Mraz <tmraz@redhat.com> 1.5.0-4
- Add GCRYCTL_SET_ENFORCED_FIPS_FLAG command

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 15 2011 Kalev Lember <kalevlember@gmail.com> 1.5.0-2
- Rebuilt for rpm bug #728707

* Thu Jul 21 2011 Tomas Mraz <tmraz@redhat.com> 1.5.0-1
- new upstream version

* Mon Jun 20 2011 Tomas Mraz <tmraz@redhat.com> 1.4.6-4
- Always xor seed from /dev/urandom over /etc/gcrypt/rngseed

* Mon May 30 2011 Tomas Mraz <tmraz@redhat.com> 1.4.6-3
- Make the FIPS-186-3 DSA implementation CAVS testable
- add configurable source of RNG seed /etc/gcrypt/rngseed
  in the FIPS mode (#700388)

* Fri Feb 11 2011 Tomas Mraz <tmraz@redhat.com> 1.4.6-1
- new upstream version with minor changes

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Tomas Mraz <tmraz@redhat.com> 1.4.5-6
- fix a bug in the fips-186-3 dsa parameter generation code

* Tue Feb  1 2011 Tomas Mraz <tmraz@redhat.com> 1.4.5-5
- use /dev/urandom for seeding in the FIPS mode
- make the tests to pass in the FIPS mode also fixing
  the FIPS-186-3 DSA keygen

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> 1.4.5-4
- FTBFS libgcrypt-1.4.5-3.fc13: ImplicitDSOLinking (#564973)

* Wed Feb  3 2010 Tomas Mraz <tmraz@redhat.com> 1.4.5-3
- drop the S390 build workaround as it is no longer needed
- additional spec file cleanups for merge review (#226008)

* Mon Dec 21 2009 Tomas Mraz <tmraz@redhat.com> 1.4.5-1
- workaround for build on S390 (#548825)
- spec file cleanups
- upgrade to new minor upstream release

* Tue Aug 11 2009 Tomas Mraz <tmraz@redhat.com> 1.4.4-8
- fix warning when installed with --excludedocs (#515961)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Tomas Mraz <tmraz@redhat.com> 1.4.4-6
- and now really apply the padlock patch

* Wed Jun 17 2009 Tomas Mraz <tmraz@redhat.com> 1.4.4-5
- fix VIA padlock RNG inline assembly call (#505724)

* Thu Mar  5 2009 Tomas Mraz <tmraz@redhat.com> 1.4.4-4
- with the integrity verification check the library needs to link to libdl
  (#488702)

* Tue Mar  3 2009 Tomas Mraz <tmraz@redhat.com> 1.4.4-3
- add hmac FIPS integrity verification check

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Tomas Mraz <tmraz@redhat.com> 1.4.4-1
- update to 1.4.4
- do not abort when the fips mode kernel flag is inaccessible
  due to permissions (#470219)
- hobble the library to drop the ECC support

* Mon Oct 20 2008 Dennis Gilmore <dennis@ausil.us> 1.4.3-2
- disable asm on sparc64

* Thu Sep 18 2008 Nalin Dahyabhai <nalin@redhat.com> 1.4.3-1
- update to 1.4.3
- own /etc/gcrypt

* Mon Sep 15 2008 Nalin Dahyabhai <nalin@redhat.com>
- invoke make with %%{?_smp_mflags} to build faster on multi-processor
  systems (Steve Grubb)

* Mon Sep  8 2008 Nalin Dahyabhai <nalin@redhat.com> 1.4.2-1
- update to 1.4.2

* Tue Apr 29 2008 Nalin Dahyabhai <nalin@redhat.com> 1.4.1-1
- update to 1.4.1
- bump libgpgerror-devel requirement to 1.4, matching the requirement enforced
  by the configure script

* Thu Apr  3 2008 Joe Orton <jorton@redhat.com> 1.4.0-3
- add patch from upstream to fix severe performance regression
  in entropy gathering

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.0-2
- Autorebuild for GCC 4.3

* Mon Dec 10 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.4.0-1
- update to 1.4.0

* Tue Oct 16 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.2.4-6
- use ldconfig to build the soname symlink for packaging along with the
  shared library (#334731)

* Wed Aug 22 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.2.4-5
- add missing gawk buildrequirement
- switch from explicitly specifying the /dev/random RNG to just verifying
  that the non-LGPL ones were disabled by the configure script

* Thu Aug 16 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.2.4-4
- clarify license
- force use of the linux /dev/random RNG, to avoid accidentally falling back
  to others which would affect the license of the resulting library

* Mon Jul 30 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.2.4-3
- disable static libraries (part of #249815)

* Fri Jul 27 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.2.4-2
- move libgcrypt shared library to /%%{_lib} (#249815)

* Tue Feb  6 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.2.4-1
- update to 1.2.4

* Mon Jan 22 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.2.3-2
- make use of install-info more failsafe (Ville Skyttä, #223705)

* Fri Sep  1 2006 Nalin Dahyabhai <nalin@redhat.com> - 1.2.3-1
- update to 1.2.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.2-3.1
- rebuild

* Mon Jun 05 2006 Jesse Keating <jkeating@redhat.com> 1.2.2-3
- Added missing buildreq pkgconfig

* Tue May 16 2006 Nalin Dahyabhai <nalin@redhat.com> 1.2.2-2
- remove file conflicts in libgcrypt-config by making the 64-bit version
  think the libraries are in /usr/lib (which is wrong, but which it also
  prunes from the suggest --libs output, so no harm done, hopefully)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct  5 2005 Nalin Dahyabhai <nalin@redhat.com> 1.2.2-1
- update to 1.2.2

* Wed Mar 16 2005 Nalin Dahyabhai <nalin@redhat.com> 1.2.1-1
- update to 1.2.1

* Fri Jul 30 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- another try to package the symlink

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun May  2 2004 Bill Nottingham <notting@redhat.com> - 1.2.0-1
- update to official 1.2.0

* Fri Apr 16 2004 Bill Nottingham <notting@redhat.com> - 1.1.94-1
- update to 1.1.94

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb 21 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- add symlinks to shared libs at compile time

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Mar 20 2003 Jeff Johnson <jbj@redhat.com> 1.1.12-1
- upgrade to 1.1.12 (beta).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Jeff Johnson <jbj@redhat.com>
- update to 1.1.7
- change license to LGPL.
- include splint annotations patch.
- install info pages.

* Tue Apr  2 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.6-1
- update to 1.1.6

* Thu Jan 10 2002 Nalin Dahyabhai <nalin@redhat.com> 1.1.5-1
- fix the Source tag so that it's a real URL

* Thu Dec 20 2001 Nalin Dahyabhai <nalin@redhat.com>
- initial package
