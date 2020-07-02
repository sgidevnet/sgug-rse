# Perform optional tests
%bcond_without perl_Statistics_Basic_enables_optional_test

Name:           perl-Statistics-Basic
Version:        1.6611
Release:        17%{?dist}
Summary:        A collection of very basic statistics modules
# lib/Statistics/Basic/Mean.pod:    LGPLv2+
# lib/Statistics/Basic.pod:         LGPLv2
License:        LGPLv2 and LGPLv2+
URL:            https://metacpan.org/release/Statistics-Basic
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JETTERO/Statistics-Basic-%{version}.tar.gz
BuildArch:      noarch
%if !%{with perl_Statistics_Basic_enables_optional_test}
BuildRequires:  coreutils
%endif
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Number::Format) >= 1.42
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
%if %{with perl_Statistics_Basic_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Math::BigFloat) >= 1.60
# Test::Perl::Critic not used
# Test::Pod not used
# Test::Pod::Coverage not used
%endif
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Number::Format) >= 1.42

# Remove underspecified dependecies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Number::Format\\)$

%description
use Statistics::Basic qw(:all);

my $median = median( 1,2,3 );
my $mean   = mean(  [1,2,3]); # array refs are ok too

my $variance = variance( 1,2,3 );
my $stddev   = stddev(   1,2,3 );

my $correlation = correlation( [1 .. 3], [1 .. 3] );


%prep
%setup -q -n Statistics-Basic-%{version}
%if !%{with perl_Statistics_Basic_enables_optional_test}
rm t/60_bigfloats.t
perl -i -ne 'print $_ unless m{^t/60_bigfloats\.t\b}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset DEBUG_STATS_B IPRES NOFILL TEST_AUTHOR TOLER
make test

%files
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.6611-17
- Perl 5.32 rebuild

* Fri May 29 2020 Petr Pisar <ppisar@redhat.com> - 1.6611-16
- Modernize a spec file
- License corrected to "LGPLv2 and LGPLv2+"

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.6611-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6611-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6611-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6611-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6611-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6611-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6611-2
- Perl 5.22 rebuild

* Thu Dec 18 2014 Petr Šabata <contyk@redhat.com> - 1.6611-1
- 1.6611 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.6607-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.6607-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.6607-2
- Perl 5.16 rebuild

* Thu Jan 26 2012 Petr Pisar <ppisar@redhat.com> - 1.6607-1
- 1.6607 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6602-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6602-5
- add new filter

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6602-4
- Perl mass rebuild

* Wed Feb 16 2011 Petr Pisar <ppisar@redhat.com> - 1.6602-3
- Version unversioned Provides

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6602-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Petr Pisar <ppisar@redhat.com> 1.6602-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Install into perl core directory
- Description from README
