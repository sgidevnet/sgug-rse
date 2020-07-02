Name:		perl-Text-Hunspell
Version:	2.14
Release:	19%{?dist}
Summary:	Perl interface to the Hunspell library
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Text-Hunspell
Source0:	https://cpan.metacpan.org/modules/by-module/Text/Text-Hunspell-%{version}.tar.gz
Patch1:		Text-Hunspell-2.14-no-Alien.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc-c++
BuildRequires:	hunspell-devel >= 1.2.8
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(vars)
# Test Suite
%if 0%{?fedora} > 23 || 0%{?rhel} > 7
BuildRequires:	glibc-langpack-en
%endif
BuildRequires:	hunspell-en
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(warnings)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provides a Perl interface to the Hunspell library. This module
is to meet the need of looking up many words, one at a time, in a single
session, such as spell-checking a document in memory.

%prep
%setup -q -n Text-Hunspell-%{version}

# We don't have (nor need) Alien::Hunspell, so revert to using ExtUtils::PkgConfig
%patch1

# Fix up shellbang in example
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' examples/basic.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
LANG=en_US make test TEST_POD=1 TEST_VERBOSE=1

%files
%doc Changes README examples/
%{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/Text/
%{_mandir}/man3/Text::Hunspell.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-16
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Paul Howarth <paul@city-fan.org> - 2.14-14
- Rebuild for hunspell 1.7.x

* Wed Nov  7 2018 Paul Howarth <paul@city-fan.org> - 2.14-13
- Explicitly BR: glibc-langpack-en

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-11
- Perl 5.28 rebuild

* Thu Feb 15 2018 Paul Howarth <paul@city-fan.org> - 2.14-10
- Fix up shellbang in example
- Simplify find commands using -empty and -delete

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.14-4
- Rebuild for hunspell 1.5.x

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Paul Howarth <paul@city-fan.org> - 2.14-1
- Update to 2.14
  - No functional changes
  - Text::Hunspell now depends on Alien::Hunspell version 0.04, and should
    finally compile nicely on Win32 platform
- Update patch for using ExtUtils::PkgConfig instead of Alien::Hunspell
- Get rid of some legacy spec boilerplate

* Mon Jan 11 2016 Paul Howarth <paul@city-fan.org> - 2.13-1
- Update to 2.13
  - Win32 build support added
- Update patch for using ExtUtils::PkgConfig instead of Alien::Hunspell

* Mon Dec 21 2015 Paul Howarth <paul@city-fan.org> - 2.12-1
- Update to 2.12
  - Replaced ExtUtils::PkgConfig with Alien::Hunspell
- Explicitly BR: perl-devel, needed for EXTERN.h
- We don't have (nor need) Alien::Hunspell, so revert to using
  ExtUtils::PkgConfig

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-2
- Perl 5.22 rebuild

* Wed May 13 2015 Paul Howarth <paul@city-fan.org> - 2.11-1
- Update to 2.11
  - Fix compilation on non-gcc based systems (CPAN RT#99810)
  - Minor clean-ups
  - No functional changes

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.10-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Paul Howarth <paul@city-fan.org> - 2.10-1
- Update to 2.10
  - Fix ExtUtils::PkgConfig usage in metadata and Makefile.PL
    (http://github.com/cosimo/perl5-text-hunspell/issues/5)

* Mon Oct 20 2014 Paul Howarth <paul@city-fan.org> - 2.09-1
- Update to 2.09
  - Use ExtUtils::PkgConfig to find libhunspell (CPAN RT#99548)
- Classify buildreqs by usage

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-6
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.08-2
- Perl 5.18 rebuild

* Thu May  2 2013 Paul Howarth <paul@city-fan.org> - 2.08-1
- Update to 2.08
  - Improved main POD documentation for Hunspell.pm (CPAN RT#84964)

* Tue Mar 26 2013 Paul Howarth <paul@city-fan.org> - 2.07-1
- Update to 2.07
  - DEPRECATED the delete() method and implemented proper object handles in
    the hunspell XS glue so that multiple speller objects can coexist
    (CPAN RT#84054)

* Sat Mar  9 2013 Paul Howarth <paul@city-fan.org> - 2.06-1
- Update to 2.06
  - Implemented new add_dic() function from hunspell API (CPAN RT#83765)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 21 2012 Paul Howarth <paul@city-fan.org> - 2.05-1
- Update to 2.05 (fix pod encoding - CPAN RT#79630)
- Drop upstreamed pod encoding patch

* Fri Sep 21 2012 Paul Howarth <paul@city-fan.org> - 2.04-1
- Update to 2.04 (specify pod encoding to placate pod test - CPAN RT#79630)
- Add patch to fix pod encoding
- BR: perl(File::Spec)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Paul Howarth <paul@city-fan.org> - 2.03-4
- BR: perl(Data::Dumper)
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot
- Use %%{_fixperms} macro rather than our own chmod incantation

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.03-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Paul Howarth <paul@city-fan.org> - 2.03-1
- Update to 2.03 (fixed use of "qw()" as parenthesis in inc/Devel/CheckLib.pm
  because it's deprecated in perl 5.14)

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.02-5
- Perl mass rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.02-4
- Perl mass rebuild

* Wed May 25 2011 Paul Howarth <paul@city-fan.org> - 2.02-3
- Rebuilt for new hunspell
- Remove remaining use of macros for system commands

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 24 2010 Paul Howarth <paul@city-fan.org> - 2.02-1
- Update to 2.02 (added an explicit warning if the unversioned libhunspell.so
  symlink or library is not found)

* Wed Sep 29 2010 jkeating - 2.01-3
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Paul Howarth <paul@city-fan.org> - 2.01-2
- Sanitize for Fedora submission

* Wed Sep  8 2010 Paul Howarth <paul@city-fan.org> - 2.01-1
- Initial RPM version
