%global base_version 3.75

Name:           perl-PathTools
Version:        3.78
Release:        441%{?dist}
Summary:        PathTools Perl module (Cwd, File::Spec)
# Cwd.xs:                   BSD
# other files:              GPL+ or Artistic
License:        (GPL+ or Artistic) and BSD
URL:            https://metacpan.org/release/PathTools
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/PathTools-%{base_version}.tar.gz
# Disable VMS tests (bug #973713)
Patch0:         PathTools-3.74-Disable-VMS-tests.patch
# Unbundled from perl 5.29.10
Patch1:         PathTools-3.75-Upgrade-to-3.78.patch
# Fix an off-by-one in bsd_realpath(), in perl after 5.33.3
Patch2:         perl-5.33.3-PathTools-Cwd.xs-fix-off-by-one-in-bsd_realpath.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
# File::Basename not needed because of removed File::Spec::VMS
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
# Optional run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(Errno)
Requires:       perl(Scalar::Util)
# XSLoader is optional only because miniperl does not support XS. With perl we
# almost certainly want it.
Recommends:     perl(XSLoader)

%{?perl_default_filter}

%description
This is the combined distribution for the File::Spec and Cwd modules.

%prep
%setup -q -n PathTools-%{base_version}
%patch0 -p1
%patch1 -p1
%patch2 -p3

# Do not distribute File::Spec::VMS as it works on VMS only (bug #973713)
rm lib/File/Spec/VMS.pm
perl -i -ne 'print $_ unless m{^\Qlib/File/Spec/VMS.pm\E}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/File/
%{_mandir}/man3/*

%changelog
* Thu Nov 05 2020 Petr Pisar <ppisar@redhat.com> - 3.78-441
- Fix an off-by-one in bsd_realpath()

* Thu Feb 06 2020 Tom Stellard <tstellar@redhat.com> - 3.78-440
- Spec file cleanups: Use make_build and make_install macros
- https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make
- https://fedoraproject.org/wiki/Perl/Tips#ExtUtils::MakeMake

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.78-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.78-438
- Increase release to favour standalone package

* Thu Apr 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.78-1
- Upgrade to 3.78 as provided in perl-5.29.10

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Petr Pisar <ppisar@redhat.com> - 3.75-1
- 3.75 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.74-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.74-416
- Increase release to favour standalone package

* Mon Feb 19 2018 Petr Pisar <ppisar@redhat.com> - 3.74-1
- 3.74 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.67-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.67-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.67-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.67-393
- Perl 5.26 rebuild

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 3.67-1
- Upgrade to 3.67 as provided in perl-5.25.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.63-367
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.63-366
- Avoid loading optional modules from default . (CVE-2016-1238)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.63-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.63-1
- 3.63 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Petr Pisar <ppisar@redhat.com> - 3.62-1
- 3.62 bump

* Mon Jan 11 2016 Petr Pisar <ppisar@redhat.com> - 3.60-2
- Fix CVE-2015-8607 (File::Spec::canonpath() loses tain) (bug #1297455)

* Thu Nov 19 2015 Petr Pisar <ppisar@redhat.com> - 3.60-1
- 3.60 bump

* Mon Nov 16 2015 Petr Pisar <ppisar@redhat.com> - 3.59-1
- 3.59 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.56-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.56-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.56-2
- Perl 5.22 rebuild

* Mon Apr 27 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.56-1
- 3.56 bump in order to dual-live with Perl 5.22

* Tue Jan 13 2015 Petr Pisar <ppisar@redhat.com> - 3.47-311
- Require constant module

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.47-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.47-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.47-1
- 3.47 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 3.40-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 3.40-4
- Link minimal build-root packages against libperl.so explicitly

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 3.40-3
- Disable VMS test (bug #973713)

* Fri Jun 14 2013 Petr Pisar <ppisar@redhat.com> - 3.40-2
- Do not distribute File::Spec::VMS (bug #973713)

* Mon Feb 04 2013 Petr Pisar <ppisar@redhat.com> - 3.40-1
- 3.40 bump

* Tue Sep 18 2012 Petr Pisar <ppisar@redhat.com> - 3.39.01-1
- 3.39_01 bump

* Wed Aug 15 2012 Petr Pisar <ppisar@redhat.com> - 3.33-8
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 3.33-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 3.33-4
- RPM 4.9 dependency filtering added

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.33-3
- Perl mass rebuild

* Sun May 29 2011 Ville Skyttä <ville.skytta@iki.fi> - 3.33-2
- Own the %%{perl_vendorarch}/File dir.

* Mon Feb 28 2011 Marcela Mašláňová <mmaslano@redhat.com> 3.33-1
- Specfile autogenerated by cpanspec 1.79.
