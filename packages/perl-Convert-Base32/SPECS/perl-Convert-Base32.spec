Name:           perl-Convert-Base32
Version:        0.06
Release:        7%{?dist}
Summary:        Encoding and decoding of base32 strings
License:        GPL+ or Artistic
URL:            https://metacpan.org/pod/Convert::Base32
Source0:        http://www.cpan.org/modules/by-module/Convert/Convert-Base32-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::Exception)
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module provides functions to convert string from / to Base32 encoding,
specified in RACE internet-draft. The Base32 encoding is designed to encode
non-ASCII characters in DNS-compatible host name parts.

%prep
%setup -q -n Convert-Base32-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-7
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Xavier Bachelot <xavier@bachelot.org> 0.06-2
- Specfile fixes following package review.

* Thu Oct 18 2018 Xavier Bachelot <xavier@bachelot.org> 0.06-1
- Initial package.
