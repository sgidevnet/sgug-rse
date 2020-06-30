Summary:	High speed arbitrary size integer math
Name:		perl-Math-GMP
Version:	2.20
Release:	2%{?dist}
License:	LGPLv2+
URL:		https://metacpan.org/release/Math-GMP
Source0:	https://cpan.metacpan.org/modules/by-module/Math/Math-GMP-%{version}.tar.gz
Patch0:		Math-GMP-2.18-no-Alien::GMP.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	gmp-devel
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter >= 4:5.10.0
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(AutoLoader)
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(Config)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::More)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
Math::GMP was designed to be a drop-in replacement both for Math::BigInt and
for regular integer arithmetic. Unlike BigInt, though, Math::GMP uses the GNU
gmp library for all of its calculations, as opposed to straight Perl functions.
This can result in speed improvements.

%prep
%setup -q -n Math-GMP-%{version}

# Avoid need for Alien::GMP; our build environment doesn't need it
%patch0

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README.md
%{perl_vendorarch}/Math/
%{perl_vendorarch}/auto/Math/
%{_mandir}/man3/Math::GMP.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-2
- Perl 5.32 rebuild

* Mon Feb 10 2020 Paul Howarth <paul@city-fan.org> - 2.20-1
- Update to 2.20
  - Try to fix tests when using libgmp version 6.2.0 (CPAN RT#131718)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.19-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.19-2
- Perl 5.28 rebuild

* Sun Apr  8 2018 Paul Howarth <paul@city-fan.org> - 2.19-1
- Update to 2.19
  - Fix int() on large unsigned integers (GH#2)

* Sat Apr  7 2018 Paul Howarth <paul@city-fan.org> - 2.18-1
- Update to 2.18
  - Depend on Alien::GMP to automatically install GMP when missing
    (CPAN RT#125018, GH#1)
- Patch out usage of Alien::GMP, not needed in Fedora

* Thu Apr  5 2018 Paul Howarth <paul@city-fan.org> - 2.17-1
- Update to 2.17
  - Correct the link to the GitHub repository (CPAN RT#125018)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Paul Howarth <paul@city-fan.org> - 2.16-1
- Update to 2.16
  - Fix behaviour under "use feature 'bitwise'" (CPAN RT#123907)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Paul Howarth <paul@city-fan.org> - 2.15-1
- Update to 2.15
  - Bump required perl version to 5.10.x
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  1 2017 Paul Howarth <paul@city-fan.org> - 2.14-1
- Update to 2.14
  - Hopefully fix the GPG signature (CPAN RT#120062)

* Fri Nov 18 2016 Paul Howarth <paul@city-fan.org> - 2.13-1
- Update to 2.13
  - Fix the tests on older libgmps (CPAN RT#118816)
  - Refactoring of the test suite

* Thu Nov 10 2016 Paul Howarth <paul@city-fan.org> - 2.12-1
- Update to 2.12
  - Add support for testing methods that return lists
  - Add broot, brootrem, bsqrtrem, is_perfect_power, is_perfect_square
    (CPAN RT#118677)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-4
- Perl 5.24 rebuild

* Thu Apr 21 2016 Paul Howarth <paul@city-fan.org> - 2.11-3
- Fix FTBFS due to missing buildreq perl-devel
- Simplify find commands using -empty and -delete

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Paul Howarth <paul@city-fan.org> - 2.11-1
- Update to 2.11
  - Got the distribution to have full POD coverage and check all functions for
    usage (CPAN RT#92593)

* Thu Aug 13 2015 Paul Howarth <paul@city-fan.org> - 2.10-1
- Update to 2.10
  - Throw an exception on invalid input to Math::GMP->new (CPAN RT#27521)
  - Put RELEASE_TESTING tests under xt instead of t (CPAN RT#106365)
  - Document and test some functions that were improperly documented or not
    tested (CPAN RT#92593)

* Wed Jul 29 2015 Paul Howarth <paul@city-fan.org> - 2.09-1
- Update to 2.09
  - Add a link to the version control repository at various places
  - Get rid of indirect object notation in the code and the examples (it's a
    sign of Ancient Perl)
  - Overload bool to avoid fallback to intify (CPAN RT#101443)
  - Add tests for large numbers in some functions (CPAN RT#92641)
  - Add the binary-left-shift / << operator
  - Add the binary-right-shift / >> operator
  - Convert the build system to Dist-Zilla to ease future maintenance
  - Add a call to Devel::CheckLib for finding the "gmp.h" header
- Drop %%defattr, redundant since rpm 4.4
- Use %%license where possible
- Classify buildreqs by usage
- This release by SHLOMIF → update source URL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Paul Howarth <paul@city-fan.org> - 2.07-1
- Update to 2.07
  - Go direct to XS for more speed
  - Add lcm/blcm, bsqrt, bmodinv
- Don't bother trying to run the release tests
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Don't need to remove empty directories from the buildroot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 2.06-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Petr Pisar <ppisar@redhat.com> - 2.06-10
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> 2.06-9
- Use %%{_fixperms} macro rather than our own chmod incantation
- Add buildreqs for perl core modules, which might be dual-lived
- Don't run tests in VERBOSE mode anymore

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> 2.06-8.1
- Rebuild with new gmp

* Wed Jul 20 2011 Paul Howarth <paul@city-fan.org> 2.06-8
- Perl mass rebuild
- Work around MYMETA.yml causing signature test to fail
- Use LANG rather than LC_ALL to set locale for spell check test
- Nobody else likes macros for commands

* Wed Feb  9 2011 Paul Howarth <paul@city-fan.org> 2.06-7
- Fix spell check test to add words not in hunspell dictionary

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct  4 2010 Paul Howarth <paul@city-fan.org> 2.06-5
- Change BR: aspell-en to hunspell-en now that Text::SpellChecker uses a
  hunspell back-end

* Tue May 11 2010 Paul Howarth <paul@city-fan.org> 2.06-4
- Don't clobber ~/.gnupg

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> 2.06-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> 2.06-2
- Rebuild against perl 5.10.1

* Fri Sep 18 2009 Paul Howarth <paul@city-fan.org> 2.06-1
- Update to 2.06
  - Make Makefile.PL more forgiving of gmp library locations (CPAN RT#46323)
  - Update link to libgmp.org in INSTALL file (CPAN RT#46324)
- Use %%{?perl_default_filter}
- RELEASE_TESTING variable obsoletes TEST_{AUTHOR,CRITIC,SIGNATURE,SPELL}
- BuildConflict Test::Critic and Test::Pod::Coverage to avoid failing tests

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar  7 2009 Paul Howarth <paul@city-fan.org> 2.05-4
- Filter out unwanted provides for perl shared objects
- Do the build in a subdirectory so that the debug files list doesn't interfere
  with the signature test
- Enable the signature test
- Run the tests in the en_US locale - spell check tests now pass
- Add buildreq perl(YAML) to enable the YAML tests

* Thu Feb 26 2009 Paul Howarth <paul@city-fan.org> 2.05-3
- Add buildreq aspell-en as it's not pulled in by aspell after Fedora 10
- Add buildreq perl(File::Comments) to support spellchecking of comments
- Disable spellcheck tests as they fail anyway

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct  7 2008 Paul Howarth <paul@city-fan.org> 2.05-1
- New upstream maintainer, new upstream version 2.05
- 64-bit test suite compatibility issues fixed upstream, patch removed
- Run tests in verbose mode
- Add buildreq perl(Test::More) for basic test suite
- Add buildreqs perl(Module::Signature), perl(Perl::Critic), perl(Pod::Spell),
  perl(Test::Pod), perl(Test::YAML::Meta), and perl(Text::SpellChecker) for
  additional test suite functionality

* Fri Jun  6 2008 Paul Howarth <paul@city-fan.org> 2.04-10
- Apply 64-bit testsuite-fixing patch on sparc64 too

* Tue Mar 25 2008 Paul Howarth <paul@city-fan.org> 2.04-9
- Apply 64-bit testsuite-fixing patch on ia64 too (#436649)

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.04-8
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 2.04-7
- Autorebuild for GCC 4.3

* Mon Aug 13 2007 Paul Howarth <paul@city-fan.org> 2.04-6
- Clarify license as LGPL, version 2 or later

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 2.04-5
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 2.04-4
- FE6 mass rebuild

* Thu Feb 16 2006 Paul Howarth <paul@city-fan.org> 2.04-3
- Rebuild

* Tue Feb  7 2006 Paul Howarth <paul@city-fan.org> 2.04-2
- Apply patch to fix broken testsuite on 64-bit arches (CPAN RT#12751)

* Tue Nov 29 2005 Paul Howarth <paul@city-fan.org> 2.04-1
- Initial build
