Name:		perl-Algorithm-LUHN
Version:	1.02
Release:	14%{?dist}
Summary:	Calculate the Modulus 10 Double Add Double checksum
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Algorithm-LUHN
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Algorithm-LUHN-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Test)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	findutils
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module calculates the Modulus 10 Double Add Double checksum, also
known as the LUHN Formula. This algorithm is used to verify credit
card numbers and Standard & Poor's security identifiers such as
CUSIP's and CSIN's.

%prep
%setup -q -n Algorithm-LUHN-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%{perl_vendorlib}/Algorithm/
%{_mandir}/man3/Algorithm::LUHN.3pm*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.02-1
- update to version 1.02
- updates to documentation

* Sun Jul 19 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.01-3
- add perl back to BuildRequires

* Sun Jul 19 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.01-2
- update BuildRequires to include make, findutils, and coreutils
- remove perl version in BuildRequires
- add min version for ExtUtils::MakeMaker
- remove Exporter as explict Requires
- remove dist.init from doc files

* Mon Jul  6 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.01-1
- Initial version
