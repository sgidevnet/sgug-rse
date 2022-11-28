Name:           perl-Test-Timer
Version:        2.11
Release:        1%{?dist}
Summary:        Test module to test/assert response times
License:        Artistic 2.0
URL:            https://metacpan.org/release/Test-Timer
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Test-Timer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Error)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tester) >= 1.302111
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Test::Timer implements a set of test primitives to test and assert test
times from bodies of code.

%prep
%setup -q -n Test-Timer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
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
* Mon Sep 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-1
- 2.11 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-2
- Perl 5.30 rebuild

* Wed Feb 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-1
- 2.10 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-1
- 2.09 bump

* Tue Nov 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-1
- 2.08 bump

* Mon Nov 20 2017 Petr Pisar <ppisar@redhat.com> - 2.07-1
- 2.07 bump

* Wed Nov 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.06-1
- 2.06 bump

* Mon Nov 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-1
- 2.05 bump

* Tue Oct 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-1
- 2.04 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-1
- 2.03 bump

* Tue Jun 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-1
- 2.01 bump

* Mon Jun 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1
- 2.00 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Mon Dec 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-1
- 0.15 bump

* Tue Aug 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-1
- 0.13 bump

* Wed Aug 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-1
- Initial release
