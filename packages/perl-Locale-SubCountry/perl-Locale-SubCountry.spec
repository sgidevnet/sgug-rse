Name:           perl-Locale-SubCountry
Version:        2.06
Release:        1%{?dist}
Summary:        ISO 3166-2 two letter subcountry codes
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Locale-SubCountry
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/Locale-SubCountry-%{version}.tar.gz
# Normalize Changes encoding
Patch0:         Locale-SubCountry-2.04-Convert-to-UTF-8.patch
BuildArch:      noarch 
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON) >= 1
BuildRequires:  perl(locale) >= 1
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(JSON) >= 1
Requires:       perl(locale) >= 1

# Filter under-sepcified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((JSON|locale)\\)$

%description
This module allows you to convert the full name for a countries administrative
region to the code commonly used for postal addressing. The reverse look-up
can also be done. Sub country codes are defined in "ISO 3166-2:2007, Codes for
the representation of names of countries and their subdivisions".

Sub countries are termed as states in the US and Australia, provinces in
Canada and counties in the UK and Ireland.

%prep
%setup -q -n Locale-SubCountry-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Tue Aug 13 2019 Petr Pisar <ppisar@redhat.com> - 2.06-1
- 2.06 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-2
- Perl 5.30 rebuild

* Mon Apr 08 2019 Petr Pisar <ppisar@redhat.com> - 2.05-1
- 2.05 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-1
- 2.04 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-2
- Perl 5.26 rebuild

* Tue Mar 07 2017 Petr Pisar <ppisar@redhat.com> - 2.02-1
- 2.02 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 2.01-1
- 2.01 bump

* Fri Aug 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1
- 2.00 bump

* Mon Jul 25 2016 Petr Pisar <ppisar@redhat.com> - 1.66-1
- 1.66 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.65-2
- Perl 5.24 rebuild

* Tue Apr 26 2016 Petr Pisar <ppisar@redhat.com> - 1.65-1
- 1.65 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.64-2
- Perl 5.22 rebuild

* Tue Apr 07 2015 Petr Pisar <ppisar@redhat.com> - 1.64-1
- 1.64 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.62-2
- Perl 5.18 rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 1.62-1
- 1.62 bump

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.61-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Petr Pisar <ppisar@redhat.com> - 1.61-1
- 1.61 bump

* Wed Feb 13 2013 Petr Pisar <ppisar@redhat.com> - 1.60-1
- 1.60 bump

* Thu Jan 24 2013 Petr Pisar <ppisar@redhat.com> - 1.59-1
- 1.59 bump

* Tue Jan 15 2013 Petr Pisar <ppisar@redhat.com> - 1.57-1
- 1.57 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Petr Pisar <ppisar@redhat.com> - 1.56-2
- Perl 5.16 rebuild

* Wed Jul 11 2012 Petr Pisar <ppisar@redhat.com> - 1.56-1
- 1.56 bump

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 1.51-2
- Perl 5.16 rebuild

* Tue Jul 03 2012 Petr Pisar <ppisar@redhat.com> - 1.51-1
- 1.51 bump

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.50-2
- Perl 5.16 rebuild

* Wed Apr 18 2012 Petr Pisar <ppisar@redhat.com> - 1.50-1
- 1.50 bump

* Thu Jan 26 2012 Petr Pisar <ppisar@redhat.com> - 1.47-1
- 1.47 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.41-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.41-7
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.41-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.41-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.41-1
- update to 1.41
- chmod -x everything

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.38-2
- rebuild for new perl

* Tue Dec 05 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.38-1
- update to 1.38
- minor specfile tweaks

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.37-2
- bump for mass rebuild

* Wed Jul  5 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.37-1
- bump release for f-e build

* Mon Jul  3 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.37-0.1
- add additional buildreq's

* Thu Jun 29 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.37-0
- Initial spec file for F-E
