Summary:	OO interface for spell-checking a block of text 
Name:		perl-Text-SpellChecker
Version:	0.14
Release:	18%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Text-SpellChecker
Source0:	https://cpan.metacpan.org/modules/by-module/Text/Text-SpellChecker-%{version}.tar.gz
Patch0:		Text-SpellChecker-0.14-dictpath.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(Text::Hunspell)
BuildRequires:	perl(warnings)
# Test Suite
%if 0%{?fedora} > 23 || 0%{?rhel} > 7
BuildRequires:	glibc-langpack-en
%endif
BuildRequires:	hunspell-en
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)
# Optional Tests
BuildRequires:	perl(Test::Pod)
%if 0%{?fedora:1}
BuildRequires:	perl(Text::Aspell), aspell-en
%endif
# Runtime
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
# hunspell is the preferred spell checking backend in Fedora
Requires:	perl(Text::Hunspell)

%description
This module is a thin layer above Text::Hunspell and allows one to spellcheck
a body of text. Whereas Text::Hunspell deals with words, Text::Spellchecker
deals with blocks of text. For instance, we provide methods for iterating
through the text, serializing the object (thus remembering where we left off),
and highlighting the current misspelled word within the text.

%prep
%setup -q -n Text-SpellChecker-%{version}

# Fedora hunspell dictionaries are in /usr/share/myspell rather than /usr/share/hunspell
%patch0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
LANG=en_US make test TEST_VERBOSE=1

%files
%doc Changes README
%{perl_vendorlib}/Text/
%{_mandir}/man3/Text::SpellChecker.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-18
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-15
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov  7 2018 Paul Howarth <paul@city-fan.org> - 0.14-13
- Explicitly BR: glibc-langpack-en

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-11
- Perl 5.28 rebuild

* Thu Feb 15 2018 Paul Howarth <paul@city-fan.org> - 0.14-10
- Drop legacy Group: tag
- Simplify find command using -delete
- Specify all explicitly-used build requirements
- Avoid use of aspell in EL builds

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.22 rebuild

* Fri Nov  7 2014 Paul Howarth <paul@city-fan.org> - 0.14-1
- Update to 0.14
  - Fixed tests: some dictionaries apparently have coördinator
  - Added set_option
- Run the tests with LANG=en_US to ensure we use the right dictionary

* Tue Nov  4 2014 Paul Howarth <paul@city-fan.org> - 0.12-1
- Update to 0.12
  - Fixes for unicode letters
- Classify buildreqs by usage
- Use %%{_fixperms} macro rather than our own chmod incantation
- Don't need to remove empty directories from the buildroot
- Do the aspell tests as well as the hunspell ones

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-10
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.11-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.11-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 25 2011 Paul Howarth <paul@city-fan.org> - 0.11-2
- Perl mass rebuild

* Sat Jun 25 2011 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11
  - POD fixes and POD test
- Re-diff dictionary path patch
- BR: perl(Test::Pod)

* Fri Jun 24 2011 Paul Howarth <paul@city-fan.org> - 0.09-2
- Perl mass rebuild

* Fri Jun 24 2011 Paul Howarth <paul@city-fan.org> - 0.09-1
- Update to 0.09
  - Better tests, use of LANG
  - Compile time check for at least one speller
- Update dictionary path patch
- Drop test suite patch, no longer needed
- Nobody else likes macros for commands
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Drop buildroot definition and cleaning
- Drop redundant defattr

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.08-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 20 2010 Paul Howarth <paul@city-fan.org> - 0.08-1
- Update to 0.08 (test suite doesn't fail in absence of Text::Aspell)
- Update testsuite patch

* Fri Sep 17 2010 Paul Howarth <paul@city-fan.org> - 0.07-1
- Update to 0.07 (use hunspell backend rather than aspell)
- Add patch for Fedora dictionary locations
- Add patch to remove dependency of Text::Aspell in test suite
- Buildreq Text::Hunspell rather than Text::Aspell
- Add buildreq hunspell-en
- Add manual dependency on perl(Text::Hunspell)
- Run test suite in verbose mode

* Wed Sep 15 2010 Paul Howarth <paul@city-fan.org> - 0.06-1
- Update to 0.06 (made deserialization accept non-blessed refs)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.05-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Paul Howarth <paul@city-fan.org> 0.05-1
- Update to 0.05

* Mon Dec 15 2008 Paul Howarth <paul@city-fan.org> 0.04-1
- Update to 0.04

* Tue Oct  7 2008 Paul Howarth <paul@city-fan.org> 0.03-1
- Initial RPM version
