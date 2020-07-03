Name:       perl-Module-Util
Version:    1.09
Release:    23%{?dist}
# see lib/Module/Util.pm
License:    GPL+ or Artistic
Summary:    Module name tools and transformations
Source:     https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-%{version}.tar.gz
Url:        https://metacpan.org/release/Module-Util
Requires:   perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
BuildArch:  noarch
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Module::Build)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time
BuildRequires: perl(Exporter)
# ExtUtils::MakeMaker not used at tests
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec::Functions)
# Getopt::Long not used at tests
# List::Util not used at tests
# Pod::Usage not used at tests
# Tests
BuildRequires: perl(Test::More)

%{?perl_default_filter}

%description
This module provides a few useful functions for manipulating module names.
Its main aim is to centralize some of the functions commonly used by
modules that manipulate other modules in some way, like converting module
names to relative paths.

%prep
%setup -q -n Module-Util-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man[13]/*.[13]*

%changelog
* Sat Jun 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-23
- Perl 5.32 re-rebuild updated packages

* Thu Jun 25 2020 Petr Pisar <ppisar@redhat.com> - 1.09-22
- Modernize a spec file

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-21
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-10
- Fix FTBFS when perl is not in the SRPM build root

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.09-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 1.09-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.08-2
- Perl 5.16 rebuild

* Sun Jun 10 2012 Iain Arnell <iarnell@gmail.com> 1.08-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter
- use Module::Build, not EU::MM

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.07-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.07-5
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.07-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.07-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.07-1
- auto-update to 1.07 (by cpan-spec-update 0.01)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 16 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.05-1
- update to 1.05

* Wed Nov 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.04-1
- clean up for submission

* Wed Nov 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.04-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)
