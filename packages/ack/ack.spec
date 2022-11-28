Name:           ack
Version:        3.1.1
%global cpan_version v%{version}
Release:        1%{?dist}
Summary:        Grep-like text finder
License:        Artistic 2.0
URL:            http://beyondgrep.com/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.04
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Next) >= 1.18
BuildRequires:  perl(File::Spec) >= 3.00
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Text::ParseWords) >= 3.1
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Harness) >= 2.5
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)
Requires:       perl(File::Next) >= 1.18
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Ack is designed as a replacement for grep.

%prep
%setup -q -n %{name}-%{cpan_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%license LICENSE.md
%{perl_vendorlib}/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Mon Sep  2 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.1.1-1
- Release 3.1.1

* Mon Aug 26 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.1.0-1
- Release 3.1.0 (BZ#1744861)

* Wed Aug 21 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.0.3-1
- Release 3.0.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Thu Jun 27 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1 (BZ#1724012)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.0-2
- Perl 5.30 rebuild

* Tue May 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Tue Mar 19 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.999.06-1
- Update to 3.0 beta

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-2
- Perl 5.28 rebuild

* Wed Jun 27 2018 Robin Lee <cheeselee@fedoraproject.org> - 2.24-1
- Update to 2.24 (#1594219)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 24 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.22-1
- Update to 2.22 (#1528821)

* Mon Dec 11 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.20-1
- Update to 2.20 (#1524382)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-2
- Perl 5.26 rebuild

* Sat Mar 25 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.18-1
- Update to 2.18 (#1435841)

* Sat Mar 11 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.16-1
- Update to 2.16 (#1431301)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-5
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-2
- Perl 5.22 rebuild

* Sat Sep 13 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.14-1
- Update to 2.14
- Update URL

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-5
- Perl 5.20 rebuild

* Fri Aug 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-4
- Specify all dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.12-2
- BR perl(IO::Pty) for running more tests

* Wed Dec 11 2013 Robin Lee <cheeselee@fedoraproject.org> - 2.12-1
- Update to 2.12
- fixes BZ#1040228, BZ#1040229,
  CVE request http://www.openwall.com/lists/oss-security/2013/12/10/10

* Wed Sep 25 2013 Robin Lee <cheeselee@fedoraproject.org> - 2.10-1
- Update to 2.10

* Fri Aug 23 2013 Robin Lee <cheeselee@fedoraproject.org> - 2.08-1
- Update to 2.08

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 2.04-2
- Perl 5.18 rebuild

* Mon Apr 29 2013 Robin Lee <cheeselee@fedoraproject.org> - 2.04-1
- Update to 2.04

* Thu Apr 18 2013 Robin Lee <cheeselee@fedoraproject.org> - 2.00-1
- Update to 2.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 1.96-5
- Perl 5.16 rebuild

* Wed Jun 13 2012 Robin Lee <cheeselee@fedoraproject.org> - 1.96-4
- BR: perl(Data::Dumper)

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.96-3
- Perl 5.16 rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 11 2012 Robin Lee <cheeselee@fedoraproject.org> - 1.96-1
- Update to 1.96
- License changed to 'Artistic 2.0' since 1.90

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.94-2
- Perl mass rebuild

* Thu Apr 21 2011  <ianburrell@gmail.com> - 1.94-1
- Update to 1.94

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug  4 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.92-2
- rebuild with perl-5.12.1 again

* Wed Jun 16 2010 Ian Burrell <ianburrell@gmail.com> - 1.92-1
- Update to 1.92

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.86-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.86-4
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 23 2008 Ian Burrell <ianburrell@gmail.com> - 1.86-1
- Update to 1.86

* Mon Mar 24 2008 Ian M. Burrell <ianburrell@gmail.com> - 1.78-1
- Update to 1.78

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.76-2
- rebuild for new perl

* Thu Jan 17 2008 Ian Burrell <ianburrell@gmail.com> - 1.76-1
- Update to 1.76

* Thu Aug 16 2007 Ian Burrell <ianburrell@gmail.com> - 1.64-1
- Update to 1.64
- Add BuildRequires Test::More

* Mon Jun 18 2007 Ian Burrell <ianburrell@gmail.com> - 1.62-2
- Disable tests since bug not fixed

* Sun Jun 17 2007 Ian Burrell <ianburrell@gmail.com> - 1.62-1
- Update to 1.62
- Enable tests

* Tue May 15 2007 Ian Burrell <ianburrell@gmail.com> - 1.60-1
- add BuildRequires perl(ExtUtils::MakeMaker)

* Sat May  5 2007 Ian Burrell <ianburrell@gmail.com> - 1.60-4
- Update to 1.60; requires File::Next 0.40

* Mon Feb 12 2007 Ian Burrell <ianburrell@gmail.com> - 1.56-4
- Fix minor issues

* Tue Jan 30 2007 Ian Burrell <ianburrell@gmail.com> - 1.56-3
- Fix source URL

* Mon Jan 29 2007 Ian Burrell <ianburrell@gmail.com> - 1.56-2
- Rename to ack

* Mon Jan 29 2007 Ian Burrell <ianburrell@gmail.com> 1.56-1
- Specfile autogenerated by cpanspec 1.69.1.
