Name:           perl-List-Compare
Version:        0.53
Release:        16%{?dist}
Summary:        Compare elements of two or more lists
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/List-Compare
Source0: https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/List-Compare-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
# Tests only
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Advanced functionality to compare members of two or more lists.

%prep
%setup -q -n List-Compare-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes FAQ README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-2
- Perl 5.22 rebuild

* Mon Jun 08 2015 Petr Šabata <contyk@redhat.com> - 0.53-1
- 0.53 bump

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-2
- Perl 5.22 rebuild

* Mon May 25 2015 Petr Šabata <contyk@redhat.com> - 0.52-1
- 0.52 bump

* Fri May 15 2015 Petr Šabata <contyk@redhat.com> - 0.51-1
- 0.51 bump, reverting some of the 0.50 changes

* Mon May 11 2015 Petr Šabata <contyk@redhat.com> - 0.50-1
- 0.50 bump, performance improvements

* Thu Mar 12 2015 Petr Šabata <contyk@redhat.com> - 0.49-1
- 0.49 bump, metadata updates

* Thu Feb 26 2015 Petr Šabata <contyk@redhat.com> - 0.48-1
- 0.48 bump, yet even more performance improvements

* Mon Feb 23 2015 Petr Šabata <contyk@redhat.com> - 0.47-1
- 0.47 bump, yet more performance improvements

* Thu Feb 19 2015 Petr Šabata <contyk@redhat.com> - 0.46-1
- 0.46 bump, more performance enhancements

* Tue Feb 17 2015 Petr Šabata <contyk@redhat.com> - 0.45-1
- 0.45 bump, more performance enhancements

* Fri Feb 13 2015 Petr Šabata <contyk@redhat.com> - 0.43-1
- 0.43 bump, performance enhancements

* Mon Feb 09 2015 Petr Šabata <contyk@redhat.com> - 0.41-1
- 0.41 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-2
- Perl 5.20 rebuild

* Mon Jul 07 2014 Petr Pisar <ppisar@redhat.com> - 0.39-1
- 0.39 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Petr Šabata <contyk@redhat.com> - 0.38-1
- 0.38 bump, documentation update
- Modernize the spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.37-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.37-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.37-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.37-7
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.37-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.37-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.37-1
- update to 0.37

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.33-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.33-2.2
- add BR: perl(Test::Simple)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.33-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.33-2
- bump for mass rebuild

* Thu Jun 29 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.33-1
- bump release for extras build

* Thu Jun 29 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.33-0
- Initial spec file for F-E
