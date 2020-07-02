Name:           perl-Class-Std
Version:        0.013
Release:        14%{?dist}
Summary:        Support for creating standard "inside-out" classes
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Class-Std
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Std-%{version}.tar.gz
# Recode to UTF-8
Patch0:         Class-Std-0.013-POD-encoding.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Test Suite
BuildRequires:  perl(Test::More)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Data::Dumper)

%description
This module provides tools that help to implement the "inside out object"
class structure in a convenient and standard way.

%prep
%setup -q -n Class-Std-%{version}
%patch0 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Std.3pm*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Petr Pisar <ppisar@redhat.com> - 0.013-1
- 0.013 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.011-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov  1 2013 Paul Howarth <paul@city-fan.org> - 0.011-1
- Update to 0.011
  - Added 'how can I help' POD
  - Fix overwritten warnings in UNIVERSAL::can (CPAN RT#30833)
  - Removed git repository information
  - Fixed incompatibility with Perl 5.11+ label constraints
  - Remove unneeded dependency on version.pm
- Specify all dependencies
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Don't need to remove empty directories from the buildroot
- Don't use macros for commands
- Supply missing POD encoding (CPAN RT#78196)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.0.8-15
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.0.8-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.0.8-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0.8-8
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0.8-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.0.8-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.8-3
- Rebuild for new perl

* Sun Jan 20 2008 Andreas Thienemann <andreas@bawue.net> - 0.0.8-2
- Added changed BuildReqs to handle changed Perl packaging in fedora (bz
- Detailed License to specify "GPL2 or later" clause
- Thx to Ralf Corsépius for the heads up

* Thu Mar 15 2007 Andreas Thienemann <andreas@bawue.net> - 0.0.8-1
- Specfile autogenerated by cpanspec 1.69.1.
- Adapted for FE
