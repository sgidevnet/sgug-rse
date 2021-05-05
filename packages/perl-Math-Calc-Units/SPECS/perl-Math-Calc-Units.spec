# Provides/Requires filtering is different from rpm 4.9 onwards
%global rpm49 %(rpm --version | perl -p -e 's/^.* (\\d+)\\.(\\d+).*/sprintf("%d.%03d",$1,$2) ge 4.009 ? 1 : 0/e' 2>/dev/null || echo 0)

Name:		perl-Math-Calc-Units
Version:	1.07
Release:	29%{?dist}
Summary:	Human-readable unit-aware calculator
License:	GPLv2 or Artistic
URL:		https://metacpan.org/release/Math-Calc-Units
Source0:	https://cpan.metacpan.org/modules/by-module/Math/Math-Calc-Units-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl(vars)
# Script Runtime
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Remove unwanted provide if we have rpm 4.9 or later
%global __provides_exclude ^perl\\(Parse::Yapp::Driver\\)

%description
Math::Calc::Units is a simple calculator that keeps track of units. It
currently handles combinations of byte sizes and duration only, although
adding any other multiplicative types is easy. Any unknown type is treated
as a unique user type (with some effort to map English plurals to their
singular forms).

%prep
%setup -q -n Math-Calc-Units-%{version}

# Remove unwanted provide if we don't have rpm 4.9 or later
%if ! %{rpm49}
%global provfilt /bin/sh -c "%{__perl_provides} | sed -e '/perl(Parse::Yapp::Driver)/d'"
%global __perl_provides %{provfilt}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

# Remove file we don't need packaging
rm %{buildroot}%{perl_vendorlib}/Math/Calc/Units/Grammar.y

%check
make test

%files
%if 0%{?_licensedir:1}
%license Artistic.html COPYING LICENSE
%else
%doc Artistic.html COPYING LICENSE
%endif
%doc Changes README
%{_bindir}/ucalc
%{perl_vendorlib}/Math/
%{_mandir}/man3/Math::Calc::Units.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-28
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Paul Howarth <paul@city-fan.org> - 1.07-26
- Spec tidy-up
  - Drop redundant buildroot cleaning in %%install section
  - Drop redundant explicit %%clean section
  - Simplify find command using -delete
  - Use author-independent source URL

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-24
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-21
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 1.07-19
- Adjust RPM version detection to SRPM build root without perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-18
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Paul Howarth <paul@city-fan.org> - 1.07-16
- Classify buildreqs by usage
- Prefer %%global over %%define
- Use %%license where possible

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-14
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.07-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.07-7
- Perl 5.16 rebuild

* Sun Apr  1 2012 Paul Howarth <paul@city-fan.org> - 1.07-6
- License is "GPLv2 or Artistic", not "GPLv2+ or Artistic"
- BR: perl(Test::Pod) for additional test coverage
- BR: Perl core modules that might be dual-lived
- Make %%files list more explicit
- Drop %%defattr, redundant since rpm 4.4
- Fix provides filter to work with rpm ≥ 4.9
- Don't need to remove empty directories from buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Don't use macros for commands
- Reinstate buildroot definition and cleaning for EPEL-5 compatibility
- Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.07-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.07-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.07-1
- Upstream released new version

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.06-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.06-3
- Rebuild against perl 5.10.1

* Wed Jul 29 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.06-2
- Review fixes (#513874)

* Sun Jul 26 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 1.06-1
- Initial import
