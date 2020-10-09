# Perform optional tests
%bcond_without perl_Pod_Simple_enables_optional_test

Name:           perl-Pod-Simple
# Epoch to compete with perl.spec
Epoch:          1
Version:        3.39
Release:        2%{?dist}
Summary:        Framework for parsing POD documentation
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Simple
Source0:        https://cpan.metacpan.org/authors/id/K/KH/KHW/Pod-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(if)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Escapes) >= 1.04
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::Wrap) >= 98.112902
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test) >= 1.25
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
%if %{with perl_Pod_Simple_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests:
# Text::Diff not helpful, used only in case of a failure
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Deep)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::Wrap\\)$

%description
Pod::Simple is a Perl library for parsing text in the POD (plain old
documentation) markup language that is typically used for writing
documentation for Perl and for Perl modules.

%prep
%setup -q -n Pod-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset PERL_CORE PERL_TEST_DIFF
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Petr Pisar <ppisar@redhat.com> - 1:3.39-1
- 3.39 bump

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.38-2
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Petr Pisar <ppisar@redhat.com> - 1:3.38-1
- 3.38 bump

* Thu May 30 2019 Petr Pisar <ppisar@redhat.com> - 1:3.37-2
- Do not package Pod::Escapes (upstream bug #102)

* Thu May 30 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.37-1
- update to 3.37

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.36-2
- Perl 5.30 rebuild

* Thu May 23 2019 Petr Pisar <ppisar@redhat.com> - 1:3.36-1
- 3.36 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.35-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.35-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.35-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.35-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.35-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.35-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 02 2016 Petr Pisar <ppisar@redhat.com> - 1:3.35-1
- 3.35 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.32-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Petr Pisar <ppisar@redhat.com> - 1:3.32-2
- Specify all dependencies

* Tue Nov  3 2015 Tom Callaway <spot@fedoraproject.org> - 1:3.32-1
- update to 3.32

* Tue Aug 25 2015 Tom Callaway <spot@fedoraproject.org> - 1:3.31-1
- update to 3.31

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.30-2
- Perl 5.22 rebuild

* Tue Feb 24 2015 Petr Pisar <ppisar@redhat.com> - 1:3.30-1
- 3.30 bump

* Fri Jan 30 2015 Petr Pisar <ppisar@redhat.com> - 1:3.29-1
- 3.29 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.28-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.28-294
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.28-293
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.28-292
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1:3.28-291
- Specify all dependencies

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:3.28-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:3.28-3
- Link minimal build-root packages against libperl.so explicitly

* Thu May 23 2013 Petr Pisar <ppisar@redhat.com> - 1:3.28-2
- Specify all dependencies

* Mon May 06 2013 Petr Pisar <ppisar@redhat.com> - 1:3.28-1
- 3.28 bump

* Mon Mar 18 2013 Petr Pisar <ppisar@redhat.com> 1:3.26-1
- Specfile autogenerated by cpanspec 1.78.
