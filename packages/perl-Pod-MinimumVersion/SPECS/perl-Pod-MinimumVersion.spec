Name:           perl-Pod-MinimumVersion
Version:        50
Release:        28%{?dist}
Summary:        Perl version for POD directives used
License:        GPLv3+
URL:            https://metacpan.org/release/Pod-MinimumVersion
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Pod-MinimumVersion-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
# inc/my_pod2html not executed
# Run-time:
# Getopt::Long not used at tests
BuildRequires:  perl(IO::String) >= 1.02
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Data::Dumper)
# Devel::FindRef not used
# Devel::StackTrace not used
BuildRequires:  perl(Exporter)
# Scalar::Util not used
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(IO::String) >= 1.02
# This module has been divided from perl-Perl-Critic-Pulp
Conflicts:      perl-Perl-Critic-Pulp < 49

%description
Pod::MinimumVersion parses the POD in a Perl script, module, or document,
and reports what version of Perl is required to process the directives in
it with pod2man etc.

%prep
%setup -q -n Pod-MinimumVersion-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc Changes
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 50-28
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 50-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Petr Pisar <ppisar@redhat.com> - 50-26
- Modernize a spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 50-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 50-24
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 50-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 50-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 50-21
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 50-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 50-18
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 50-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 50-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Petr Pisar <ppisar@redhat.com> - 50-14
- Modernize spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 50-12
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 50-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 50-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 50-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 50-3
- Perl mass rebuild

* Thu Apr 21 2011 Petr Pisar <ppisar@redhat.com> - 50-2
- Splitted from perl-Perl-Critic-Pulp, conficts with old perl-Perl-Critic-Pulp
  versions

* Wed Apr 06 2011 Petr Pisar <ppisar@redhat.com> 50-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
