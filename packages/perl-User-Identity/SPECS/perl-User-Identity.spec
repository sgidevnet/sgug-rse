Name:           perl-User-Identity
Version:        0.99
Release:        10%{?dist}
Summary:        Maintains info about a physical person
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/User-Identity
Source0:        https://cpan.metacpan.org/modules/by-module/User/User-Identity-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Geography::Countries)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Geography::Countries)

%description
A module designed to store and maintain a set of informational objects that
are related to one user.

%prep
%setup -q -n User-Identity-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README.md
%{perl_vendorlib}/Mail/
%{perl_vendorlib}/User/
%{_mandir}/man3/Mail::Identity.3*
%{_mandir}/man3/User::Identity.3*
%{_mandir}/man3/User::Identity::Archive.3*
%{_mandir}/man3/User::Identity::Archive::Plain.3*
%{_mandir}/man3/User::Identity::Collection.3*
%{_mandir}/man3/User::Identity::Collection::Emails.3*
%{_mandir}/man3/User::Identity::Collection::Locations.3*
%{_mandir}/man3/User::Identity::Collection::Systems.3*
%{_mandir}/man3/User::Identity::Collection::Users.3*
%{_mandir}/man3/User::Identity::Item.3*
%{_mandir}/man3/User::Identity::Location.3*
%{_mandir}/man3/User::Identity::System.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Paul Howarth <paul@city-fan.org> - 0.99-8
- Spec tidy-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Explicitly require perl(Geography::Countries)
  - Use %%{make_build} and %%{make_install}
  - Fix permissions verbosely
  - Make %%files list more explicit
  - Package README.md rather than README

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-1
- 0.99 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.97-2
- Perl 5.26 rebuild

* Wed Feb  8 2017 Tom Callaway <spot@fedoraproject.org> - 0.97-1
- update to 0.97

* Wed Sep 21 2016 Tom Callaway <spot@fedoraproject.org> - 0.96-1
- update to 0.96

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-1
- 0.94 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-13
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.93-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.93-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.93-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.93-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jul 12 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.93-1
- update to 0.93

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.92-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.92-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.92-3
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.92-2
- rebuild for new perl

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.92-1
- bump to 0.92
- license tag fix

* Mon Apr  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.91-1
- Initial package for Fedora
