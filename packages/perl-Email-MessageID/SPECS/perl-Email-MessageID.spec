Name:           perl-Email-MessageID
Version:        1.406
Release:        16%{?dist}
Summary:        Generate world unique message-ids

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Email-MessageID
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MessageID-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(overload)
BuildRequires:  perl(Sys::Hostname)
# Optional run-time:
# Sys::Hostname::Long omitted to test Sys::Hostname
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Optional tests:
# CPAN::Meta 2.12090 not helpful
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Sys::Hostname)
Suggests:       perl(Sys::Hostname::Long)

%description
Message-ids are optional, but highly recommended, headers that identify
a message uniquely. This software generates a unique message-id.


%prep
%setup -q -n Email-MessageID-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} -c %{buildroot}


%check
unset AUTHOR_TESTING
make test


%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::MessageID.3*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.406-16
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Paul Howarth <paul@city-fan.org> - 1.406-14
- Spec tidy-up
  - Use author-independent source URL
  - Specify all build requirements
  - Use %%{make_build} and %%{make_install}
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.406-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Petr Pisar <ppisar@redhat.com> - 1.406-10
- Remove an unused dependency on Email::Address (bug #1475784)
- Modernize spec file and specify all dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.406-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.406-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.406-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.406-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Tom Callaway <spot@fedoraproject.org> - 1.406-1
- update to 1.406

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.405-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.405-2
- Perl 5.22 rebuild

* Mon Mar 30 2015 Tom Callaway <spot@fedoraproject.org> - 1.405-1
- update to 1.405

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.404-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.404-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar  7 2014 Tom Callaway <spot@fedoraproject.org> - 1.404-1
- update to 1.404

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.402-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.402-2
- Perl 5.18 rebuild

* Sun Feb 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.402-1
- Add BR: per(ExtUtils::MakeMaker) (Fix FTBFS #914273).
- Upstream update.
- Modernize spec.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.401-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.401-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.401-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.401-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.401-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.401-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.401-8
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.401-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.401-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.401-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.401-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.401-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.401-2
- Add R: perl(Email::Address).

* Thu Feb 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.401-1
- Upstream update.
- Add LICENSE to %%doc.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.351-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.351-2
- rebuild for new perl

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.351-1
- Update to 1.351.

* Tue Jul 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.35-1
- Update to 1.35.

* Thu Sep 08 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.31-1
- First build.
