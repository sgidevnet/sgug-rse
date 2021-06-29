Name:           perl-Email-Simple
Version:        2.216
Release:        6%{?dist}
Summary:        Simple parsing of RFC2822 message format and headers
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Email-Simple
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Simple-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Email::Date::Format)

%description
"Email::Simple" is the first deliverable of the "Perl Email Project", a
reaction against the complexity and increasing bugginess of the
"Mail::*" modules. In contrast, "Email::*" modules are meant to be
simple to use and to maintain, pared to the bone, fast, minimal in their
external dependencies, and correct.

%prep
%setup -q -n Email-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::Simple.3*
%{_mandir}/man3/Email::Simple::Creator.3*
%{_mandir}/man3/Email::Simple::Header.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.216-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.216-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.216-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.216-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.216-2
- Perl 5.28 rebuild

* Thu Jun  7 2018 Paul Howarth <paul@city-fan.org> - 2.216-1
- Update to 2.216
  - Do not re-fold folded lines
- Classify buildreqs by usage
- Drop legacy Group: tag
- Drop provides/obsoletes for perl-Email-Simple-Creator added in 2010
- Make %%files list more explicit
- Simplify find command using -delete
- Don't need to remove empty directories from the buildroot

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.214-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov  6 2017 Tom Callaway <spot@fedoraproject.org> - 2.214-2
- remove invalid BR: perl(Test::MinimumVersion)

* Tue Sep 12 2017 Tom Callaway <spot@fedoraproject.org> - 2.214-1
- update to 2.214

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.213-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.213-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Tom Callaway <spot@fedoraproject.org> - 2.213-1
- update to 2.213

* Mon Nov 14 2016 Tom Callaway <spot@fedoraproject.org> - 2.211-1
- update to 2.211

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.210-2
- Perl 5.24 rebuild

* Tue Mar  8 2016 Tom Callaway <spot@fedoraproject.org> - 2.210-1
- update to 2.210

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.208-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Tom Callaway <spot@fedoraproject.org> - 2.2208-1
- update to 2.2208

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Tom Callaway <spot@fedoraproject.org> - 2.206-1
- update to 2.206

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.203-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.203-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar  6 2014 Tom Callaway <spot@fedoraproject.org> - 2.203-1
- update to 2.203

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 2.102-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 17 2012 Tom Callaway <spot@fedoraproject.org> - 2.102-1
- update to 2.102
- add explicit Requires: perl(Email::Date::Format)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.100-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 2.100-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 2.100-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.100-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jul 12 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.100-1
- update to 2.100
- absorbs perl-Email-Simple-Creator

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.005-6
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.005-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.005-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.005-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.003-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.003-2
- rebuild for new perl, disable unnecessary BR on perl-Email-MIME

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.003-1
- bump to 2.003

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.999-1
- Update to 1.999.

* Sat Feb 10 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.998-1
- Update to 1.998.

* Fri Dec  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.996-1
- Update to 1.996.

* Thu Oct 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.995-1
- Update to 1.995.

* Sat Oct  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.992-1
- Update to 1.992.

* Wed Sep  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.990-1
- Update to 1.990.

* Mon Aug 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.980-1
- Update to 1.980.

* Sat Jul 29 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.96-1
- Update to 1.96.

* Sat Jul 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.95-1
- Update to 1.95.

* Tue Jul 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.94-1
- Update to 1.94.

* Thu Sep 08 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.92-1
- First build.
