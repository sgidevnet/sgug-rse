Name:           perl-Email-MIME-Encodings
Version:        1.315
Release:        19%{?dist}
Summary:        Unified interface to MIME encoding and decoding
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Email-MIME-Encodings
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-Encodings-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(MIME::Base64) >= 3.05
BuildRequires:  perl(MIME::QuotedPrint) >= 3.05
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Carp)

%description
This module simply wraps "MIME::Base64" and "MIME::QuotedPrint" so that
you can throw the contents of a "Content-Transfer-Encoding" header at
some text and have the right thing happen.


%prep
%setup -q -n Email-MIME-Encodings-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}


%check
make test


%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::MIME::Encodings.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.315-19
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Paul Howarth <paul@city-fan.org> - 1.315-17
- Spec tidy-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Use %%license
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.315-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.315-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.315-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.315-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.315-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.315-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.315-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.315-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.315-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar  7 2014 Tom Callaway <spot@fedoraproject.org> - 1.315-1
- update to 1.315

* Fri Aug  9 2013 Paul Howarth <paul@city-fan.org> - 1.314-1
- Update to 1.314
  - Add a third argument to encode/decode/codec to allow a fallback codec
- Package upstream's LICENSE file
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.313-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.313-14
- Perl 5.18 rebuild

* Sun Feb 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.313-13
- Add BR: perl(ExtUtils::MakeMaker) (Fix FTBFS #914272).
- Modernize spec.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.313-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.313-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.313-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.313-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.313-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.313-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.313-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.313-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.313-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.313-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.313-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.313-1
- update to 1.313

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.312-1
- update to 1.312

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.311-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.311-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.311-2
- rebuild for new perl

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.311-1
- Update to 1.311.

- New upstream maintainer.
* Tue Sep 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.310-2
- Bump release dir to tagging problems.

* Tue Sep 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.310-1
- Update to 1.310.
- New upstream maintainer.

* Thu Sep 08 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3-1
- First build.
