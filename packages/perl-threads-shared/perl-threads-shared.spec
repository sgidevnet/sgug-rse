%global base_version 1.59

Name:           perl-threads-shared
Version:        1.60
Release:        440%{?dist}
Summary:        Perl extension for sharing data structures between threads
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/threads-shared
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDHEDDEN/threads-shared-%{base_version}.tar.gz
# Unbundled from perl 5.29.10
Patch0:         threads-shared-1.59-Upgrade-to-1.60.patch
# Fix a memory leak when assigning a shared reference to a shared string
# variable, in perl after 5.31.1
Patch1:         threads-shared-1.60-threads-shared-fix-leak.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
# Config_m not needed
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(threads) >= 1.73
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
# Win32 not needed
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(threads) >= 1.73
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
By default, variables are private to each thread, and each newly created
thread gets a private copy of each existing variable. This module allows
you to share variables across different threads (and pseudo-forks on
Win32). It is used together with the threads module.

%prep
%setup -q -n threads-shared-%{base_version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset GIT_DIR PERL_BUILD_PACKAGING PERL_CORE PERL_RUNPERL_DEBUG \
    RUN_MAINTAINER_TESTS
make test

%files
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/threads*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Petr Pisar <ppisar@redhat.com> - 1.60-439
- Fix a memory leak when assigning a shared reference to a shared string
  variable

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-438
- Increase release to favour standalone package

* Fri Apr 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-1
- Upgrade to 1.60 as provided in perl-5.29.10

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Petr Pisar <ppisar@redhat.com> - 1.59-1
- 1.59 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.58-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Petr Pisar <ppisar@redhat.com> - 1.58-1
- 1.58 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.57-2
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Petr Pisar <ppisar@redhat.com> - 1.57-1
- 1.57 bump

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-393
- Perl 5.26 rebuild

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 1.56-1
- Upgrade to 1.56 as provided in perl-5.25.12

* Fri Apr 21 2017 Petr Pisar <ppisar@redhat.com> - 1.55-2
- Fix arenas allocation (RT#131124)

* Mon Feb 27 2017 Petr Pisar <ppisar@redhat.com> - 1.55-1
- 1.55 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Petr Pisar <ppisar@redhat.com> - 1.54-1
- 1.54 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-3
- Perl 5.24 rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-2
- Perl 5.24 rebuild

* Tue May 17 2016 Petr Pisar <ppisar@redhat.com> - 1.52-1
- 1.52 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-365
- Increase release to favour standalone package

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 1.51-1
- 1.51 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-341
- Perl 5.22 rebuild

* Tue May 05 2015 Petr Pisar <ppisar@redhat.com> - 1.48-340
- 1.48 bump in order to dual-live with perl 5.22

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Petr Pisar <ppisar@redhat.com> - 1.46-2
- Declare optional tests

* Wed Feb 05 2014 Petr Pisar <ppisar@redhat.com> - 1.46-1
- 1.46 bump

* Thu Nov 14 2013 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1.43-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.43-5
- Link minimal build-root packages against libperl.so explicitly

* Tue Jul 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-4
- Remove BR perl(Test)

* Tue Jul 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-3
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Fri Nov 23 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-2
- Add BR perl(File::Spec)
- Replace PERL_INSTALL_ROOT with DESTDIR
- Remove deleting empty directories
- Remove defattr

* Wed Oct 03 2012 Petr Pisar <ppisar@redhat.com> - 1.42-1
- 1.42 bump

* Mon Sep 10 2012 Petr Pisar <ppisar@redhat.com> - 1.41-1
- 1.41 bump

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.40-240
- bump release to override sub-package from perl.spec 

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.40-3
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Petr Pisar <ppisar@redhat.com> - 1.40-1
- 1.40 bump

* Tue Sep 06 2011 Petr Pisar <ppisar@redhat.com> - 1.39-1
- 1.39 bump

* Wed Aug 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.37-3
- change path on vendor, so our debuginfo are not conflicting with
 perl core debuginfos

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.37-2
- Perl mass rebuild

* Tue Apr 26 2011 Petr Pisar <ppisar@redhat.com> - 1.37-1
- 1.37 bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Petr Pisar <ppisar@redhat.com> - 1.36-1
- 1.36 bump

* Mon Oct 11 2010 Petr Pisar <ppisar@redhat.com> - 1.34-1
- 1.34 bump

* Thu Sep 23 2010 Petr Pisar <ppisar@redhat.com> 1.33-1
- Specfile autogenerated by cpanspec 1.78.
- Fix dependencies
- Requires perl(Scalar::Util) is autodetected
- Do not provide private library
- Remove pre-F12 BuildRoot stuff
