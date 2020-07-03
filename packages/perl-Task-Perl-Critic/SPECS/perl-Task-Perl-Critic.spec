# This file is licensed under the terms of GNU GPLv2+.

# Perform optinoal tests
%bcond_without perl_Task_Perl_Critic_enables_optional_test

Name:           perl-Task-Perl-Critic
Version:        1.008
Release:        24%{?dist}
Summary:        Install everything Perl::Critic
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Task-Perl-Critic
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Task-Perl-Critic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Other requires from META.yml are not needed at build and check time. There
# is no code, no provided modules. Do not BuildRequire them.
# Tests only:
BuildRequires:  perl(Test::More)
%if %{with perl_Task_Perl_Critic_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(criticism) >= 1.02
Requires:       perl(Perl::Critic) >= 1.117
Requires:       perl(Perl::Critic::Bangs) >= 1.00
Requires:       perl(Perl::Critic::Compatibility) >= 1.000
Requires:       perl(Perl::Critic::Dynamic) >= 0.05
Requires:       perl(Perl::Critic::Itch)
Requires:       perl(Perl::Critic::Lax) >= 0.007
Requires:       perl(Perl::Critic::Moose)
Requires:       perl(Perl::Critic::More) >= 1.000
Requires:       perl(Perl::Critic::Nits) >= 1.000000
Requires:       perl(Perl::Critic::PetPeeves::JTRAMMELL) >= 0.01
Requires:       perl(Perl::Critic::Pulp) >= 3
Requires:       perl(Perl::Critic::Storable)
Requires:       perl(Perl::Critic::StricterSubs) >= 0.03
# Perl::Critic::Swift: 1.000003 is decimal notion for 1.0.3 version
Requires:       perl(Perl::Critic::Swift) >= 1.0.3
Requires:       perl(Perl::Critic::Tics) >= 0.005
Requires:       perl(Test::Perl::Critic) >= 1.02
Requires:       perl(Test::Perl::Critic::Progressive) >= 0.03

%description
This module does nothing but act as a placeholder. See Task.

%prep
%setup -q -n Task-Perl-Critic-%{version}

%build
perl Makefile.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-24
- Perl 5.32 rebuild

* Fri Mar 06 2020 Petr Pisar <ppisar@redhat.com> - 1.008-23
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-20
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-17
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-14
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-9
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.008-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.008-2
- Perl 5.16 rebuild

* Thu Jan 19 2012 Petr Pisar <ppisar@redhat.com> - 1.008-1
- 1.008 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.007-2
- Perl mass rebuild

* Tue Jan 25 2011 Petr Pisar <ppisar@redhat.com> 1.007-1
- Specfile autogenerated by cpanspec 1.78.
- Do not BuildRequire run-time dependencies, they are not used at build and
  check time indeed.
- Remove BuildRoot stuff
- Remove explicit defattr 

