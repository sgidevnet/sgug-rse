# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary:	The ASN.1 library used in GNUTLS
Name:		libtasn1
Version:	4.14
Release:	4%{?dist}

# The libtasn1 library is LGPLv2+, utilities are GPLv3+
License:	GPLv3+ and LGPLv2+
URL:		http://www.gnu.org/software/libtasn1/
Source0:	http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz
Source1:	http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz.sig
Source2:	gpgkey-1F42418905D8206AA754CCDC29EE58B996865171.gpg
#Patch1:		libtasn1-3.4-rpath.patch
Patch100:       libtasn1.sgifixes.patch

#BuildRequires:	gnupg2
BuildRequires:	gcc
BuildRequires:	bison, pkgconfig, help2man
BuildRequires:	autoconf, automake, libtool
#BuildRequires:	valgrind-devel
BuildRequires:  libdicl-devel >= 0.1.19

Requires:       libdicl >= 0.1.19
# Wildcard bundling exception https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = 20130324

%package devel
Summary:	Files for development of applications which will use libtasn1
Requires:	%{name}%{?_isa} = %{version}-%{release}

Requires:	%name = %version-%release
Requires:	%{name}-tools = %{version}-%{release}
Requires:	pkgconfig
Requires:       libdicl-devel

%package tools
Summary:	Some ASN.1 tools
License:	GPLv3+
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description
A library that provides Abstract Syntax Notation One (ASN.1, as specified
by the X.680 ITU-T recommendation) parsing and structures management, and
Distinguished Encoding Rules (DER, as per X.690) encoding and decoding functions.

%description devel
This package contains files for development of applications which will
use libtasn1.


%description tools
This package contains simple tools that can decode and encode ASN.1
data.


%prep
#gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

#patch1 -p1 -b .rpath
%patch100 -p1 -b .sgifixes

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
autoreconf -v -f --install
%configure --disable-static --disable-silent-rules
# libtasn1 likes to regenerate docs
touch doc/stamp_docs

make %{?_smp_mflags}


%install
make DESTDIR="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT{%_libdir/*.la,%_infodir/dir}


%check
make check

%files
%license LICENSE doc/COPYING*
%doc AUTHORS NEWS README.md
%{_libdir}/*.so.6*

%files tools
%{_bindir}/asn1*
%{_mandir}/man1/asn1*

%files devel
%doc doc/TODO doc/*.pdf
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_infodir}/*.info.*
%{_mandir}/man3/*asn1*


%changelog
* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 4.14-4
- Remove hard coded shell paths

* Thu Feb 20 2020 Daniel Hams <daniel.hams@gmail.com> - 4.14-3
- Rebuild due to libdicl upgrade to 0.1.19

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.14-1
- Update to 4.14 (#1621973)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 James Antill <james.antill@redhat.com> - 4.13-6
- Remove ldconfig scriptlet, now done via. transfiletrigger in glibc.

* Mon Oct 22 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.13-5
- libtasn1-devel requires the tools subpackage; it is necessary for
  development.

* Sat Jul 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 4.13-4
- Add missing gcc/gnupg2 deps, spec cleanups

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.13-1
- Update to 4.13 (#1535261)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.12-1
- Update to 4.12 (#1456190)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.10-1
- Update to 4.10 (#1413792)

* Mon Nov  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 4.9-2
- Move development related docs to devel sub package
- Cleanup spec and macros
- Update valgrind ExclusiveArch

* Fri Aug 26 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.9-1
- Update to 4.9 (#1360315)

* Fri Jul  8 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.8-2
- Resolve issue which prevented the decoding of long OIDs (#1353838)

* Mon Apr 11 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.8-1
- Update to 4.8
- Resolves infinite loop recursion in the decode of certain BER structures.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.7-1
- Update to 4.7 (#1260325)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.5-1
- Update to 4.5 (#1217282)

* Mon Mar 30 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.4-1
- new upstream release (#1206968)
- fixes stack overflow in DER decoder

* Tue Mar 10 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.3-1
- new upstream release

* Tue Sep 16 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.2-1
- new upstream release

* Mon Aug 25 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.1-2
- added bug fix for octet string decoding (#1138218)

* Mon Aug 25 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.1-1
- new upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 4.0-2
- fix license handling

* Mon Jun 30 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 4.0-1
- new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.6-1
- new upstream release

* Fri May 02 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.5-1
- new upstream release

* Wed Nov 27 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.4-1
- new upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Tomáš Mráz <tmraz@redhat.com> - 3.3-1
- new upstream release
- improved description

* Thu Mar  7 2013 Tomas Mraz <tmraz@redhat.com> - 3.2-3
- drop the temporary compat libtasn1

* Tue Feb  5 2013 Tomas Mraz <tmraz@redhat.com> - 3.2-2
- now with temporary compat libtasn1 taken from old build

* Tue Feb  5 2013 Tomas Mraz <tmraz@redhat.com> - 3.2-1
- new upstream release
- SONAME bumped

* Fri Nov  9 2012 Tomas Mraz <tmraz@redhat.com> - 2.14-1
- new upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Tomas Mraz <tmraz@redhat.com> - 2.13-1
- new upstream release

* Tue Mar 20 2012 Tomas Mraz <tmraz@redhat.com> - 2.12-1
- new upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 3 2010 Tomas Mraz <tmraz@redhat.com> - 2.7-1
- new upstream release

* Thu Jan 28 2010 Tomas Mraz <tmraz@redhat.com> - 2.4-2
- drop superfluous rpath

* Mon Jan 18 2010 Tomas Mraz <tmraz@redhat.com> - 2.4-1
- new upstream release

* Mon Jan 11 2010 Tomas Mraz <tmraz@redhat.com> - 2.3-2
- no longer ignore make check result on ppc64

* Tue Aug 11 2009 Tomas Mraz <tmraz@redhat.com> - 2.3-1
- updated to new upstream version
- fix warnings when installed with --excludedocs (#515950)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Tomas Mraz <tmraz@redhat.com> - 2.2-1
- updated to new upstream version
- SMP build should work now
- drop fix for spurious rpath - no longer necessary

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.8-1
- updated to 1.8
- updated URLs
- disabled SMP builds for now

* Fri Dec 12 2008 Caolán McNamara <caolanm@redhat.com> - 1.7-2
- rebuild to get provides pkgconfig(libtasn1)

* Fri Nov 21 2008 Tomas Mraz <tmraz@redhat.com> - 1.7-1
- updated to new upstream version

* Tue Sep 30 2008 Tomas Mraz <tmraz@redhat.com> - 1.5-1
- updated to new upstream version
- fix license tag
- fix spurious rpath in the tool binaries

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-2
- fix license tag

* Thu Jun  5 2008 Tomas Mraz <tmraz@redhat.com> - 1.4-1
- updated to new upstream version

* Wed Feb 13 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.3-1
- updated to 1.3 (#426488, #431334)
- use wrapper around libtasn1-config which should make it multilib
  safe (#342411); this implies an untagged 'Requires: pkgconfig' for
  -devel now
- conditionalized BR of valgrind (#401041)

* Mon Sep  3 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.1-1
- updated to 1.1
- workaround 'make check' errors on ppc64

* Thu Jun 14 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.10-1
- updated to 0.3.10

* Fri Mar  2 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.9-1
- updated to 0.3.9

* Sat Feb  3 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.8-1
- updated to 0.3.8

* Sun Nov  5 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.6-1
- updated to 0.3.6
- BR valgrind

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.5-1
- updated to 0.3.5

* Sat Jun  3 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.4-1
- updated to 0.3.4

* Sun Mar 26 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.2-1
- updated to 0.3.2
- added -tools subpackage

* Wed Mar  8 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.1-1
- updated to 0.3.1

* Mon Mar  6 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.0-1
- updated to 0.3.0
- removed unneeded curlies
- created -devel subpackage

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.2.6-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 18 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.2.6-0.fdr.1
- updated to 0.2.6

* Mon Aug  4 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.5-0.fdr.1
- updated to 0.2.5
- changed license to LGPL
- rearranged %%check to reflect execution order
- minor cosmetical changes

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.4-0.fdr.1
- Initial build.
