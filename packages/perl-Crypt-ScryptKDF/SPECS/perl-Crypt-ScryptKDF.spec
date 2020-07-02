Name:           perl-Crypt-ScryptKDF
Version:        0.010
Release:        16%{?dist}
Summary:        Scrypt password based key derivation function
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Crypt-ScryptKDF
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/Crypt-ScryptKDF-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Exporter) >= 5.59
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(XSLoader)

# Testing
BuildRequires:  perl(Crypt::OpenSSL::Random)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
# a strong PRNG required, the simplest one
Requires:       perl(Crypt::OpenSSL::Random)

%description
Scrypt is a password-based key derivation function (like for example
PBKDF2). Scrypt was designed to be "memory-hard" algorithm in order to make
it expensive to perform large scale custom hardware attacks.

%prep
%setup -q -n Crypt-ScryptKDF-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-16
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-10
- Perl 5.28 rebuild

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 0.010-9
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Denis Fateyev <denis@fateyev.com> - 0.010-1
- Update to 0.010 version

* Wed Nov 25 2015 Denis Fateyev <denis@fateyev.com> - 0.009-2
- Small spec improvements

* Mon Nov 16 2015 Denis Fateyev <denis@fateyev.com> - 0.009-1
- Initial release
