%global base_version 2.173

Name:           perl-Data-Dumper
Version:        2.174
Release:        440%{?dist}
Summary:        Stringify perl data structures, suitable for printing and eval
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Dumper
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Data-Dumper-%{base_version}.tar.gz
# Fix a memory leak when croaking about a too deep recursion,
# fixed in perl after 5.29.9
Patch0:         Data-Dumper-2.173-Data-Dumper-avoid-leak-on-croak.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(strict)
# perl-Test-Simple is in cycle with perl-Data-Dumper
%if !%{defined perl_bootstrap}
# Run-time:
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Tests only:
BuildRequires:  perl(Config)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional tests:
BuildRequires:  perl(Encode)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(B::Deparse)
Requires:       perl(bytes)
Requires:       perl(Scalar::Util)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The content of each
variable is output in a single Perl statement. Handles self-referential
structures correctly.

%prep
%setup -q -n Data-Dumper-%{base_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
make test
%endif

%files
%doc Changes Todo
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.174-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.174-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.174-438
- Increase release to favour standalone package

* Fri Apr 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.174-1
- Update version to 2.174 as provided in perl-5.29.10

* Wed Apr 03 2019 Petr Pisar <ppisar@redhat.com> - 2.173-3
- Fix a memory leak when croaking about a too deep recursion

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.173-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Petr Pisar <ppisar@redhat.com> - 2.173-1
- 2.173 bump

* Thu Sep 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.172-1
- 2.172 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.170-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.170-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.170-416
- Increase release to favour standalone package

* Wed May 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.170-1
- Upgrade to 2.170 as provided in perl-5.28.0-RC1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.167-399
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Petr Pisar <ppisar@redhat.com> - 2.167-398
- Fix postentry for quoted glob (bug #1532524)

* Tue Dec 05 2017 Petr Pisar <ppisar@redhat.com> - 2.167-397
- Fix quoting glob names (RT#119831)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.167-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.167-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.167-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.167-393
- Perl 5.26 rebuild

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 2.167-1
- Upgrade to 2.167 as provided in perl-5.25.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.161-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 2.161-1
- 1.161 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.160-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.160-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.160-1
- 2.160 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.158-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.158-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.158-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.158-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.158-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 2.158-1
- 2.158 bump in order to dual-live with perl 5.22

* Fri Sep 19 2014 Petr Pisar <ppisar@redhat.com> - 2.154-1
- 2.154 bump (fixes CVE-2014-4330 (limit recursion when dumping deep data
  structures))

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.151-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.151-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.151-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.151-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.151-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Petr Pisar <ppisar@redhat.com> - 2.151-1
- 2.151 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.145-292
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.145-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 2.145-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.145-2
- Perl 5.18 rebuild

* Mon Mar 18 2013 Petr Pisar <ppisar@redhat.com> - 2.145-1
- 2.145 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 2.143-1
- 2.143 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.139-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Petr Pisar <ppisar@redhat.com> - 2.139-1
- 2.139 bump

* Fri Oct 05 2012 Petr Pisar <ppisar@redhat.com> - 2.136-1
- 2.136 bump

* Fri Aug 24 2012 Petr Pisar <ppisar@redhat.com> - 2.135.07-241
- Disable tests on bootstrap

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 2.135.07-240
- update the version to override the module from perl.srpm
- bump release to override sub-package from perl.spec 

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.131-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.131-2
- Perl 5.16 rebuild

* Tue Apr 10 2012 Petr Pisar <ppisar@redhat.com> 2.131-1
- Specfile autogenerated by cpanspec 1.78.
