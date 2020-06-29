Name:           perl-App-a2p
Version:        1.012
Release:        3%{?dist}
Summary:        Awk to Perl translator
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/App-a2p
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-a2p-%{version}.tar.gz
# Current code will fail test tests if the code will run for more than 5
# seconds. This is not much portable test.
Patch0:         App-a2p-1.007-Remove-alarm-call-from-test.patch

# Fix BZ#1177672
# - Add a2p.y from https://github.com/Leont/app-a2p/a2p.y
Patch1:         App-a2p-1.007-a2p-y.patch

# Required for App-a2p-1.009-Check-for-n-argument-length.patch
Patch2:         App-a2p-1.009-Capture-stderr-in-tests.patch

# Fix a buffer overflow when parsing long enough -n argument, CPAN RT#100361
Patch3:         App-a2p-1.009-Check-for-n-argument-length.patch

BuildRequires:  byacc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.89
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Conflicts:      perl < 4:5.18.2-300

%description
This package delivers a2p tool which takes an awk script specified on the
command line and produces a comparable Perl script.

%prep
%setup -q -n App-a2p-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Regenerate a2p.c from a2p.y
byacc -o a2p.c a2p.y

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-1
- 1.012 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-2
- Perl 5.30 rebuild

* Tue Apr 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-1
- 1.011 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-5
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-4
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-3
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-1
- 1.010 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-8
- Perl 5.26 re-rebuild of bootstrapped packages

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-5
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-4
- Perl 5.24 rebuild

* Mon Feb 29 2016 Petr Pisar <ppisar@redhat.com> - 1.009-3
- Fix a buffer overflow when parsing long enough -n argument (CPAN RT#100361)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-1
- 1.009 bump

* Tue Jul 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-1
- 1.008 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.007-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-7
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-6
- Perl 5.22 rebuild

* Thu Feb 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-5
- Add a2p.y and regenerate a2p.c (BZ#1177672)

* Thu Jan 08 2015 Petr Pisar <ppisar@redhat.com> - 1.007-4
- Skip test on bootstrap because of non-core Devel::FindPerl

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-1
- Specfile autogenerated by cpanspec 1.78.
