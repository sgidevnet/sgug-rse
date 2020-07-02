Name: 		perl-Pod-Tests
Version: 	1.20
Release: 	5%{?dist}
Summary: 	Extract embedded tests and code examples from POD
License: 	GPL+ or Artistic
URL: 		https://metacpan.org/release/Pod-Tests
Source0: 	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Pod-Tests-%{version}.tar.gz

Requires:  	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
BuildArch: 	noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Harness) >= 1.22
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Pod::Tests extracts embedded tests and code examples from POD.
pod2test convert embedded tests and code examples to .t files. 

%prep
%setup -q -n Pod-Tests-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes
%license LICENSE
%{_bindir}/*
%{perl_vendorlib}/Pod
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-2
- Perl 5.30 rebuild

* Wed Mar 06 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.20-1
- Update to 1.20.
- Reflect Source0:-URL having changed.
- Rework BRs.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-28
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-25
- Perl 5.26 rebuild

* Thu May 18 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.19-24
- Eliminate inc. BR: perl(inc::Module::Install) (RHBZ#1452113).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-22
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.19-20
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-18
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.19-15
- Modernize spec.
- Remove some historic hacks.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.19-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.19-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.19-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.19-6
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.19-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.19-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 10 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.19-1
- Upstream update.

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.18-6
- rebuild for new perl

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 0.18-5
- Update license tag.
- BR: perl(ExtUtils::MakeMaker).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.18-4
- Mass rebuild.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 0.18-3
- Rebuild for perl-5.8.8.

* Sun Oct 02 2005 Ralf Corsepius <rc040203@freenet.de> - 0.18-2
- Pollute the spec file with dos2unix to accommodate PR 169112.

* Fri Sep 23 2005 Ralf Corsepius <rc040203@freenet.de> - 0.18-1
- FE submission.
