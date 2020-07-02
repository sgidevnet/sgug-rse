# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Pod_Parser_enables_optional_test
%else
%bcond_with perl_Pod_Parser_enables_optional_test
%endif

Name:           perl-Pod-Parser
Version:        1.63
Release:        443%{?dist}
Summary:        Basic perl modules for handling Plain Old Documentation (POD)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Parser
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.82
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
# Getopt::Long not used for tests
# Pod::Usage not used for tests
BuildRequires:  perl(strict)
# Symbol not used since perl 5.6
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.6
# Circular dependency Pod::Checker <-> Pod::Parser
BuildRequires:  perl(Pod::Checker) >= 1.40
# VMS::Filespec not used
%if %{with perl_Pod_Parser_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(IO::String)
%endif
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Config)
# Circular dependency Pod::Usage <-> Pod::Select

%description
This software distribution contains the packages for using Perl5 POD (Plain
Old Documentation). See the "perlpod" and "perlsyn" manual pages from your
Perl5 distribution for more information about POD.

%prep
%setup -q -n Pod-Parser-%{version}
find -type f -exec chmod -x {} +
chmod +x scripts/*
for F in ANNOUNCE CHANGES README TODO; do
    tr -d '\r' < "$F" > "${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ANNOUNCE CHANGES README TODO
%{_bindir}/podselect
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-443
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-442
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-441
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-367
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.63-2
- Perl 5.22 rebuild

* Wed Feb 11 2015 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.62-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.62-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.62-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Petr Pisar <ppisar@redhat.com> - 1.62-1
- 1.62 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.61-2
- Perl 5.18 rebuild

* Tue Jun 04 2013 Petr Pisar <ppisar@redhat.com> - 1.61-1
- 1.61 bump

* Mon Feb 11 2013 Petr Pisar <ppisar@redhat.com> - 1.60-3
- Correct dependencies

* Fri Feb 08 2013 Petr Pisar <ppisar@redhat.com> - 1.60-2
- Remove bootstrap conditions

* Tue Feb 05 2013 Petr Pisar <ppisar@redhat.com> - 1.60-1
- 1.60 bump

* Mon Feb 04 2013 Petr Pisar <ppisar@redhat.com> - 1.51-248
- Sub-package Pod-Usage
- Sub-package Pod-Checker

* Wed Jan 16 2013 Petr Pisar <ppisar@redhat.com> - 1.51-247
- Increase release to supersede perl sub-package

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 1.51-2
- Perl 5.16 rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> 1.51-1
- Specfile autogenerated by cpanspec 1.78.
