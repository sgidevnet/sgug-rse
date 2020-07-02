Name:           perl-Crypt-ECB
Version:        2.22
Release:        2%{?dist}
Summary:        Encrypt data using ECB Mode
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Crypt-ECB
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-ECB-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module is a Perl-only implementation of the ECB mode. In combination
with a block cipher such as DES, IDEA or Blowfish, you can encrypt and
decrypt messages of arbitrarily long length. Though for security reasons
other modes than ECB such as CBC should be preferred. See textbooks on
cryptography if you want to know why.

%prep
%setup -q -n Crypt-ECB-%{version}
chmod -x eg/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC GPLv1
%doc CHANGES eg README README.XTEA
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-2
- Perl 5.32 rebuild

* Wed May 20 2020 Charles R. Anderson <cra@wpi.edu> - 2.22-1
- Update to 2.22
- No longer BR coreutils and findutils

* Thu May 14 2020 Charles R. Anderson <cra@wpi.edu> - 2.21-13
- use versioned BR for perl(ExtUtils::MakeMaker)

* Thu May 14 2020 Charles R. Anderson <cra@wpi.edu> - 2.21-12
- Use latest perl packaging best practices

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-1
- 2.21 bump

* Tue Aug 30 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-1
- 2.20 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-2
- Perl 5.22 rebuild

* Thu Nov 27 2014 David Dick <ddick@cpan.org> - 1.45-1
- Initial release
