# Add a support for the egd daemon
%bcond_without perl_Crypt_Random_Seed_enables_egd

Name:           perl-Crypt-Random-Seed
Version:        0.03
Release:        17%{?dist}
Summary:        Simple method to get strong randomness
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Crypt-Random-Seed
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-Random-Seed-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Fcntl)
# Win32 not used
# Optional run-time:
# Skip egd to exhibit /dev/random
# Crypt::Random::TESHA2 not used since we have /dev/random
# Skip IO::Socket to exhibit /dev/random
# Tests
BuildRequires:  perl(Test::More) >= 0.45
# Optional tests:
# Test::CheckManifest not used
# Test::Kwalitee not used
# Test::Perl::Critic not used
# Test::Pod not used
# Test::Pod::Coverage not used
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
# Crypt::Random::TESHA2 not used since we have /dev/random
%if %{with perl_Crypt_Random_Seed_enables_egd}
Suggests:       egd
Suggests:       perl(IO::Socket)
%endif

%description
A simple mechanism to get strong randomness. The main purpose of this
module is to provide a simple way to generate a seed for a PRNG such as
Math::Random::ISAAC, for use in cryptographic key generation, or as the
seed for an upstream module such as Bytes::Random::Secure. Flags for
requiring non-blocking sources are allowed, as well as a very simple method
for plugging in a source.

%prep
%setup -q -n Crypt-Random-Seed-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README TODO examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-17
- Perl 5.32 rebuild

* Wed Mar 25 2020 Petr Pisar <ppisar@redhat.com> - 0.03-16
- Modernize a spec file

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-2
- Perl 5.22 rebuild

* Sun Jan 18 2015 David Dick <ddick@cpan.org> - 0.03-1
- Initial release
