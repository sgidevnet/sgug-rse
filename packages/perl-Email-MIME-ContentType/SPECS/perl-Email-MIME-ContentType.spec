Name:           perl-Email-MIME-ContentType
Version:        1.024
Release:        2%{?dist}
Summary:        Parse a MIME Content-Type Header
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Email-MIME-ContentType
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-ContentType-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.87
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Extra Tests
BuildRequires:  perl(Test::Pod) >= 1.41
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module is responsible for parsing email content type headers according
to section 5.1 of RFC 2045. It returns a hash with entries for the type, the
subtype, and a hash of attributes.

For backward compatibility with a really unfortunate misunderstanding of RFC
2045 by the early implementors of this module, 'discrete' and 'composite' are
also present in the returned hashref, with the values of 'type' and 'subtype'
respectively.


%prep
%setup -q -n Email-MIME-ContentType-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}


%check
make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"


%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::MIME::ContentType.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.024-2
- Perl 5.32 rebuild

* Sun May 24 2020 Paul Howarth <paul@city-fan.org> - 1.024-1
- Update to 1.024
  - Silence an uninitialized value warning
  - Avoid allowing non-Latin digits in numbers
  - Add new functions build_content_type() and build_content_disposition()

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Paul Howarth <paul@city-fan.org> - 1.022-8
- Spec tidy-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Use %%license
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.022-1
- update to 1.022

* Fri Aug  4 2017 Tom Callaway <spot@fedoraproject.org> - 1.021-1
- update to 1.021

* Mon Jul 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.020-1
- update to 1.020

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.018-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.018-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.018-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Tom Callaway <spot@fedoraproject.rog> - 1.0.18-1
- update to 1.0.18

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.017-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.017-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Paul Howarth <paul@city-fan.org> - 1.017-1
- Update to 1.017
  - Correct the longstanding and embarrassing misuse of "discrete" and
    "composite" to mean "type" and "subtype"; the returned data still contains
    the wrong old names so your code shouldn't break
  - Repackage to update bugtracker, repo, etc.
  - Make $STRICT_PARAMS actually work! (CPAN RT#87460)
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4
- Explicitly run the release tests

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.015-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.015-15
- Perl 5.18 rebuild

* Sun Feb 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.015-14
- Add BR: perl(ExtUtils::MakeMaker) (Fix FTBFS #914271).
- Modernize spec.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.015-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.015-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.015-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.015-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.015-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.015-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.015-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.015-6
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.015-5
- Mass rebuild with perl-5.12.0

* Fri Apr 23 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.015-4
- rebuild

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.015-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.015-1
- update to 1.015

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.014-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.014-2
- rebuild for new perl

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.014-1
- Update to 1.014.

* Sat Nov 25 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.012-1
- Update to 1.012.

* Fri Oct 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.011-1
- Update to 1.011.

* Thu Sep 08 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- First build.
