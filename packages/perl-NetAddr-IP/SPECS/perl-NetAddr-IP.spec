Name:           perl-NetAddr-IP
Version:        4.079
Release:        14%{?dist}
Summary:        Manages IPv4 and IPv6 addresses and subnets
# Lite/Util/Util.xs is GPLv2+
# Other files are (GPLv2+ or Artistic clarified)
License:        GPLv2+ and (GPLv2+ or Artistic clarified)
URL:            https://metacpan.org/release/NetAddr-IP
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Text)
# Module Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(overload)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Math::BigInt)
Requires:       perl(Socket6)

# Don't "provide" private Perl libs or redundant unversioned provides
%global __provides_exclude ^(perl\\(NetAddr::IP(::(InetBase|Util(PP)?))?\\)$|Util\\.so)

%description
This module provides an object-oriented abstraction on top of IP addresses
or IP subnets, that allows for easy manipulations.

%prep
%setup -q -n NetAddr-IP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license Artistic Copying
%else
%doc Artistic Copying
%endif
%doc About-NetAddr-IP.txt Changes TODO docs/rfc1884.txt
%{perl_vendorarch}/auto/NetAddr/
%{perl_vendorarch}/NetAddr/
%{_mandir}/man3/NetAddr::IP.3*
%{_mandir}/man3/NetAddr::IP::InetBase.3*
%{_mandir}/man3/NetAddr::IP::Lite.3*
%{_mandir}/man3/NetAddr::IP::Util.3*
%{_mandir}/man3/NetAddr::IP::UtilPP.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.079-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.079-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.079-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.079-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.079-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.079-2
- Perl 5.24 rebuild

* Sun Mar 27 2016 Paul Howarth <paul@city-fan.org> - 4.079-1
- Update to 4.079
  - Correct non-suppression of leading zeros in certain instances of new_no use
  - Put in missing code to propagate NetAddr::IP::Lite :nofqdn to IP.pm
- Explicitly BR: perl-devel, needed for EXTERN.h
- Simplify find commands using -empty and -delete

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.078-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 Paul Howarth <paul@city-fan.org> - 4.078-1
- Update to 4.078
  - Fix typo in Util.pm 1.53 MakefilePL that caused failure to find compiler

* Fri Aug 14 2015 Paul Howarth <paul@city-fan.org> - 4.077-1
- Update to 4.077
  - Added method is_local() to Lite.pm
  - Fix Util/Makefile.PL to work around bug in Android's sh
  - Add method full6m()
  - Fix Util/Makefile.PL issue with clang compiler (CPAN RT#86831)
- Classify buildreqs by usage
- Use %%license where possible


* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.075-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.075-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.075-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.075-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Paul Howarth <paul@city-fan.org> - 4.075-1
- Update to 4.075
  - Change input filter for resolvable hostnames to allow the underscore
    character

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.073-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr  5 2014 Paul Howarth <paul@city-fan.org> - 4.073-1
- Update to 4.073
  - Add documentation about FQDN conversion and an option to disable

* Tue Jan 28 2014 Paul Howarth <paul@city-fan.org> - 4.072-1
- Update to 4.072
  - Modify Makefile.PL to bypass missing 'pod2text'
- BR: perl(Pod::Text) to ensure we get pod2text

* Tue Oct  1 2013 Paul Howarth <paul@city-fan.org> - 4.071-1
- Update to 4.071
  - Add method "canon"

* Fri Sep 13 2013 Paul Howarth <paul@city-fan.org> - 4.070-1
- Update to 4.070
  - Yet another documention error fixed
  - Add new6FFFF, RFC4291 compliant ipv4->ipV6 new in Lite.pm

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.069-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 4.069-2
- Perl 5.18 rebuild

* Sun May 26 2013 Paul Howarth <paul@city-fan.org> - 4.069-1
- Update to 4.069
  - Add proper pod encoding in Lite.pm
  - Changed Makefile.PL to check for config.h when building for XS with 'gcc',
    try building with 'cc', and check again; if config.h is not found, force
    Pure Perl mode
  - Kill XS in winduhs and Darwin, both of which misbehave when compiling XS
    code
- Drop UTF8 patch, no longer needed

* Wed Apr  3 2013 Paul Howarth <paul@city-fan.org> - 4.068-1
- Update to 4.068
  - Update Makefile.PL in Util.pm to better detect 'winduhs'

* Sun Mar 31 2013 Paul Howarth <paul@city-fan.org> - 4.067-1
- Update to 4.067
  - Improved diagnostic message for "die" with bad mask for hostenum,
    hostenumref, split, splitref, rsplit, rsplitref
- Include new docfile About-NetAddr-IP.txt

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.066-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Petr Pisar <ppisar@redhat.com> - 4.066-2
- Change license to reflect some files allow Artistic license

* Tue Oct 30 2012 Paul Howarth <paul@city-fan.org> - 4.066-1
- Update to 4.066
  - Support bracketed IPv6 URI notation as described in RFC-3986

* Wed Oct  3 2012 Paul Howarth <paul@city-fan.org> - 4.065-1
- Update to 4.065
  - Correct format for IPv6 embedded IPv4 addresses (CPAN RT#79964)

* Thu Sep 27 2012 Paul Howarth <paul@city-fan.org> - 4.064-1
- Update to 4.064
  - Updated GPL v2.0 text and address in all modules
  - Added support for rfc3021 /31 networks to hostenum
- Update UTF8 patch

* Thu Aug 09 2012 Petr Pisar <ppisar@redhat.com> - 4.062-5
- Declare encoding of POD

* Thu Aug 09 2012 Petr Pisar <ppisar@redhat.com> - 4.062-4
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.062-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 4.062-2
- Perl 5.16 rebuild

* Fri Jun  8 2012 Paul Howarth <paul@city-fan.org> 4.062-1
- update to 4.062 (#802994)
  - add is_rfc1918 to Lite.pm v1.42
  - fix change in behavior introduced in v4.050 where an empty string supplied
    to "new" previously returned 'undef' and now returns 'default' for ipV4 or
    ipV6 (CPAN RT#75976)
  - documentation updates
- don't need to remove empty directories from the buildroot
- recode NetAddr::IP::Lite module and manpage as UTF-8
- don't use macros for commands

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 4.058-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 12 2011 Paul Howarth <paul@city-fan.org> 4.058-1
- update to 4.058
  - in Lite.pm v1.40:
    - add call to InetBase::fillIPv4 to all uses of gethostbyname
  - in InetBase.pm v0.06:
    - break out the code that expands short IPv4 addresses into dotquad format
      to account for broken BSD implementations of inet_aton and gethostbyname
      that do not recognize the short format, and EXPORT this as sub 'fillIPv4'
  - in Util.pm v1.45:
    - add 'fillIPv4' to calls to gethostbyname to work around broken inet_aton
      and gethostbyname implementations in certain BSD implementations

* Fri Nov  4 2011 Paul Howarth <paul@city-fan.org> 4.056-1
- update to 4.056
  - in InetBase.pm v0.04:
    - improve inet_aton to overcome broken gethostbyname found in NetBSD and
      OpenBSD

* Sat Oct 29 2011 Paul Howarth <paul@city-fan.org> 4.055-1
- update to 4.055
  - in Lite.pm v1.38:
    - patch for CPAN RT#71869: issues with Math::BigInt variants

* Fri Oct 28 2011 Paul Howarth <paul@city-fan.org> 4.054-1
- update to 4.054
  - in Lite.pm v1.37:
    - fix CPAN RT#71925, a sub-variant of CPAN RT#62521 that showed up only for
      short notation for IPv4, e.g. 127/n, 127.0/n, 127.0.0/n but not
      127.0.0.0/n
    - remove Calc.pm
    - add detection of early Math::BigInt object structure
    - fix CPAN RT#71869 - a failed test routine
- upstream no longer ships README so no need to fix its encoding

* Wed Oct 26 2011 Paul Howarth <paul@city-fan.org> 4.052-1
- update to 4.052
  - in InetBase.pm v0.03:
    - Socket6 prior to version 0.23 does not have AF_INET6 in the EXPORT_OK
      array; modify InetBase.pm to work around this
    - remove reference to Config{osname}
  - in Lite.pm v1.35:
    - add support for Math::BigInt to NetAddr::IP::Lite
    - use Math::BigInt::Calc for creating BigInt values and fall back to
      NetAddr::IP::Calc if Math::BigInt is not present (fixes CPAN RT#71869)
- BR: perl(Data::Dumper) and perl(Math::BigInt)
- add runtime dependency on perl(Math::BigInt) for performance and consistency
- update UTF-8 patch to apply cleanly

* Thu Oct 20 2011 Paul Howarth <paul@city-fan.org> - 4.049-1
- update to 4.049
  - in Lite v1.32:
    - add capability to parse input of the form ->new6(12345,1); this should
      have been there but was missing (CPAN RT#68723)
  - in Util v1.41:
    - add inet_pton, inet_ntop, AF_INET, AF_INET6
    - modify inet_n2dx and inet_n2ad to recognize the new 128-bit IPv4 format
      ::FFFF:FFFF:0:0
    - replace isIPv4 with a pure perl version for portability
  - split the following into NetAddr::IP::InetBase v0.01 to provide better
    long-term support for IPv6:
    - inet_aton
    - inet_ntoa
    - ipv6_aton
    - ipv6_n2x
    - ipv6_n2d
    - inet_any2n
    - inet_n2dx
    - inet_n2ad
    - inet_ntop
    - inet_pton
    - packzeros
    - isIPv4
    - isNewIPv4
    - isAnyIPv4
    - AF_INET
    - AF_INET6
- BR: perl(Carp)
- BR: perl(Socket6) for test suite
- update UTF-8 patch to apply cleanly
- license is now GPL+ or Artistic in most of the code but Util.xs is GPLv2+ so
  we ship the whole thing under that license

* Fri Oct 07 2011 Petr Sabata <contyk@redhat.com> - 4.047-1
- 4.047 bump

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 4.044-4
- Fix RPM 4.9 dependency filtering

* Thu Jul 21 2011 Paul Howarth <paul@city-fan.org> - 4.044-3
- use a patch rather than scripted iconv to fix character encoding
- use rpm native provides filtering
- make %%files list more explicit

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.044-2
- Perl mass rebuild

* Tue Jun  7 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.044-1
- update to 4.044
- clean specfile

* Wed Apr  6 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.042-1
- update to 4.042, because we had terribly old release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.027-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.027-5
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.027-4
- Mass rebuild with perl-5.12.0

* Wed Feb 17 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4.027-3
- make rpmlint happy

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4.027-2
- rebuild against perl 5.10.1

* Wed Sep 16 2009 Warren Togami <wtogami@redhat.com> - 4.027-1
- 4.027

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.007-3
- fix license tag

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.007-2
- rebuild for new perl

* Tue Feb 12 2008 Andreas Thienemann <athienem@redhat.com> 4.007-1
- Updated to 4.007
- Rebuilt against gcc-4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 4.004-4
- Rebuild for selinux ppc32 issue.

* Tue Jul 10 2007 Andreas Thienemann <andreas@bawue.net> 4.004-3
- Fixed missing BR on rawhide

* Thu Apr 26 2007 Andreas Thienemann <andreas@bawue.net> 4.004-2
- Moar docs!

* Thu Apr 12 2007 Andreas Thienemann <andreas@bawue.net> 4.004-1
- Specfile autogenerated by cpanspec 1.69.1.
- Cleand up for FE
