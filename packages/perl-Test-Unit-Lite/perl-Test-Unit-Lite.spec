# Perl and RPM versioning don't work the same :-(
%global extraversion 02

# Provides/Requires filtering is different from rpm 4.9 onwards
%global rpm49 %(rpm --version | perl -p -e 's/^.* (\\d+)\\.(\\d+).*/sprintf("%d.%03d",$1,$2) ge 4.009 ? 1 : 0/e' 2>/dev/null || echo 0)

Name:		perl-Test-Unit-Lite
Epoch:		1
Version:	0.12
Release:	36%{?dist}
Summary:	Unit testing without external dependencies
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Test-Unit-Lite
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Unit-Lite-%{version}%{?extraversion}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Error)
BuildRequires:	perl(lib)
BuildRequires:	perl(Taint::Runtime)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Filter unwanted provides and requires (rpm 4.9 onwards)
%global __provides_exclude ^perl\\(Test::Unit::(Debug|HarnessUnit|Result|TestCase|TestRunner|TestSuite)\\)$
%global __requires_exclude ^perl\\(Test::Unit::Test(Runner|Suite)\\)

%description
This framework provides a lighter version of Test::Unit framework. It
implements some of the Test::Unit classes and methods needed to run test
units. Test::Unit::Lite tries to be compatible with public API of
Test::Unit. It doesn't implement all classes and methods at 100% and only
those necessary to run tests are available.

%prep
%setup -q -n Test-Unit-Lite-%{version}%{?extraversion}

# Filter unwanted provides and (prior to rpm 4.9)
# Unwanted requires not actually detected prior to rpm 4.9
%if ! %{rpm49}
%global provfilt /bin/sh -c "%{__perl_provides} | grep -Evx 'perl\\(Test::Unit::(Debug|HarnessUnit|Result|TestCase|TestRunner|TestSuite)\\)'"
%global __perl_provides %{provfilt}
%endif

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Unit::Lite.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-35
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Paul Howarth <paul@city-fan.org> - 1:0.12-33
- Drop redundant buildroot cleaning in %%install section
- Drop redundant explicit %%clean section

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-31
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-28
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 1:0.12-26
- Adjust rpm version detection to SRPM build root without perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-25
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Paul Howarth <paul@city-fan.org> - 1:0.12-23
- Use %%license where possible
- Don't use %%define
- Classify buildreqs by usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-21
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-20
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1:0.12-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Paul Howarth <paul@city-fan.org> - 1:0.12-15
- Update to 0.1202
  - Fix for hash key randomization after 5.17.5 (CPAN RT#81879)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:0.12-13
- Perl 5.16 rebuild

* Sun Mar 25 2012 Paul Howarth <paul@city-fan.org> - 1:0.12-12
- Update to 0.1201
  - Repackaged with newer Module::Builder

* Sat Mar 24 2012 Paul Howarth <paul@city-fan.org> - 1:0.12-11
- Add buildreqs for Perl core modules that could be dual-lived
- Don't need to remove empty directories from buildroot
- Drop %%defattr, redundant since rpm 4.4

* Sat Sep 24 2011 Paul Howarth <paul@city-fan.org> - 1:0.12-10
- BR: perl(Carp) and perl(Cwd)
- Make %%files list more explicit
- Reduce requires filtering to what's actually needed
- Don't use macros for commands

* Wed Jun 22 2011 Petr Pisar <ppisar@redhat.com> - 1:0.12-9
- Do not require private modules

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.12-8
- Perl mass rebuild

* Thu May  5 2011 Paul Howarth <paul@city-fan.org> - 1:0.12-7
- Fix provides filter for rpm 4.9
- BR: perl(Taint::Runtime) for additional test coverage
- Include upstream LICENSE file

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.12-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.12-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1:0.12-3
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> - 1:0.12-1
- Auto-update to 0.12 (by cpan-spec-update 0.01)
- Add epoch of 1 (0.1101 => 0.12)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Allisson Azevedo <allisson@gmail.com> - 0.1101-2
- Added filter provides

* Thu Jan 29 2009 Allisson Azevedo <allisson@gmail.com> - 0.1101-1
- Initial rpm release
