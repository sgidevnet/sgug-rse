Name:           perl-Apache-LogRegex
Version:        1.71
Release:        14%{?dist}
Summary:        Parse a line from an Apache logfile into a hash
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Apache-LogRegex
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPACEBAT/Apache-LogRegex-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Designed as a simple class to parse Apache log files.  It will construct
a regex that will parse the given log file format and can then parse
lines from the log file line by line returning a hash of each line.

%prep
%setup -q -n Apache-LogRegex-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Petr Šabata <contyk@redhat.com> - 1.71-1
- 1.71 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.70-2
- Perl 5.22 rebuild

* Tue Feb 17 2015 Petr Šabata <contyk@redhat.com> - 1.70-1
- 1.70 bump

* Fri Feb 13 2015 Petr Šabata <contyk@redhat.com> - 1.60-1
- 1.60 bump

* Tue Nov 11 2014 Petr Šabata <contyk@redhat.com> - 1.52-1
- 1.52 bump
- Modernize spec

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.5-16
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.5-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.5-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.5-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.5-6
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.5-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.5-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Steven Pritchard <steve@kspei.com> 1.5-1
- Update to 1.5.

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4-4
- rebuild for new perl

* Tue Dec 11 2007 Steven Pritchard <steve@kspei.com> 1.4-3
- Update License tag.
- BR Test::More.

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 1.4-2
- BR ExtUtils::MakeMaker.

* Mon Oct 30 2006 Steven Pritchard <steve@kspei.com> 1.4-1
- Update to 1.4.
- Cleanup to more closely match cpanspec output.

* Tue Sep 26 2006 Steven Pritchard <steve@kspei.com> 1.3-1
- Update to 1.3.
- Fix find option order.

* Sat Aug 20 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 1.2-4
- Changed Licence names to COPYING and Artistic

* Fri Aug 19 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 1.2-3
- Added new perldoc commands for GPL and Artistic Licences

* Thu Aug 18 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 1.2-2
- Second build.

* Sun Jul 3 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 1.2-1
- First build.
