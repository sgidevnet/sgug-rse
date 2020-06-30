Name:           perl-Pod-Abstract
Version:        0.20
Release:        28%{?dist}
Summary:        Abstract document tree for Perl POD documents
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Abstract
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLILBURNE/Pod-Abstract-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Task::Weaken)

%description
POD::Abstract provides a means to load a POD (or POD compatible) document
without direct reference to it's syntax, and perform manipulations on the
abstract syntax tree.

%prep
%setup -q -n Pod-Abstract-%{version}
chmod 644 lib/Pod/Abstract/Filter/*.pm 

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/paf
%{_mandir}/man1/paf.1.gz

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-28
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-22
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-17
- Perl 5.24 rebuild

* Fri Feb 26 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-16
- Package cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-13
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.20-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.20-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.20-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.20-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 14 2010 Petr Sabata <psabata@redhat.com> - 0.20-1
- New release, v0.20

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.17-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.17-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.17-2
- fix rpmlint warnings

* Thu Jun 04 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.17-1
- Specfile autogenerated by cpanspec 1.78.
