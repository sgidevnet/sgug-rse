Name:           perl-Storable
Epoch:          1
Version:        3.15
Release:        442%{?dist}
Summary:        Persistence for Perl data structures
# __Storable__.pm:  GPL+ or Artistic
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Storable
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Storable-%{version}.tar.gz
# Fix deep cloning regular expression objects, RT#134179,
# in Perl upstream after 5.31.0
Patch0:         Storable-3.15-perl-134179-include-regexps-in-the-seen-objects-tabl.patch
# Fix array length check in a store hook, in Perl upstream after 5.31.2
Patch1:         Storable-3.16-Storable-make-count-large-enough.patch
# Fix a buffer overflow when processing a vstring longer than 2^31-1,
# Perl GH#17306, in perl upstream after 5.31.6
Patch2:         perl-5.31.6-disallow-vstring-magic-strings-over-2GB-1.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Win32 not used on Linux
# Win32API::File not used on Linux
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Fcntl is optional, but locking is good
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File)
# Log::Agent is optional
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(utf8)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Array)
# Optional tests:
# gzip not used
# Data::Dump not used
# Data::Dumper not used
BuildRequires:  perl(B::Deparse) >= 0.61
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Hash::Util)
# Test::LeakTrace omitted because it's not a core module requried for building
# core Storable.
BuildRequires:  perl(Tie::Hash)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Config)
# Fcntl is optional, but locking is good
Requires:       perl(Fcntl)
Requires:       perl(IO::File)

%{?perl_default_filter}

%description
The Storable package brings persistence to your Perl data structures
containing scalar, array, hash or reference objects, i.e. anything that
can be conveniently stored to disk and retrieved at a later time.

%prep
%setup -q -n Storable-%{version}
%patch0 -p3
%patch1 -p3
%patch2 -p3

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
find $RPM_BUILD_ROOT -type f -name '*.3pm' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset PERL_CORE PERL_TEST_MEMORY PERL_RUN_SLOW_TESTS
make test

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Storable*
%{_mandir}/man3/*

%changelog
* Mon Nov 25 2019 Petr Pisar <ppisar@redhat.com> - 1:3.15-442
- Fix a buffer overflow when processing a vstring longer than 2^31-1
  (Perl GH#17306)

* Thu Aug 08 2019 Petr Pisar <ppisar@redhat.com> - 1:3.15-441
- Fix array length check in a store hook

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.15-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Petr Pisar <ppisar@redhat.com> - 1:3.15-439
- Fix deep cloning regular expression objects (RT#134179)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.15-438
- Increase release to favour standalone package

* Wed Apr 24 2019 Petr Pisar <ppisar@redhat.com> - 1:3.15-1
- 3.15 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Petr Pisar <ppisar@redhat.com> - 1:3.11-6
- Storable-3.11 source archive repackaged without a t/CVE-2015-1592.inc file
  (RT#133706)

* Mon Aug 27 2018 Petr Pisar <ppisar@redhat.com> - 1:3.11-5
- Fix recursion check (RT#133326)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.11-3
- Perl 5.28 rebuild

* Tue Jun 05 2018 Petr Pisar <ppisar@redhat.com> - 1:3.11-2
- Do not package empty Storable::Limit(3pm) manual page

* Mon Apr 30 2018 Petr Pisar <ppisar@redhat.com> - 1:3.11-1
- 3.11 bump

* Mon Apr 23 2018 Petr Pisar <ppisar@redhat.com> - 1:3.09-1
- 3.09 bump

* Thu Apr 19 2018 Petr Pisar <ppisar@redhat.com> - 1:3.06-1
- 3.06 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.62-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.62-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.62-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.62-393
- Perl 5.26 rebuild

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 1:2.62-1
- Upgrade to 2.62 as provided in perl-5.25.12

* Mon Feb 06 2017 Petr Pisar <ppisar@redhat.com> - 1:2.56-368
- Fix a stack buffer overflow in deserialization of hooks (RT#130635)
- Fix a memory leak of a class name from retrieve_hook() on an exception
  (RT#130635)

* Tue Dec 20 2016 Petr Pisar <ppisar@redhat.com> - 1:2.56-367
- Fix crash in Storable when deserializing malformed code reference
  (RT#68348, RT#130098)

* Wed Aug 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.56-366
- Avoid loading optional modules from default . (CVE-2016-1238)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.56-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.56-1
- 2.56 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.53-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.53-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.53-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.53-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 1:2.53-1
- 2.53 bump in order to dual-live with perl 5.22

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.51-4
- Increase Epoch to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.51-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 07 2014 Petr Pisar <ppisar@redhat.com> - 2.51-1
- 2.51 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 2.45-1
- 2.45 bump

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.39-3
- Link minimal build-root packages against libperl.so explicitly

* Tue Jun 11 2013 Petr Pisar <ppisar@redhat.com> - 2.39-2
- Do not export private libraries

* Fri May 24 2013 Petr Pisar <ppisar@redhat.com> 2.39-1
- Specfile autogenerated by cpanspec 1.78.
