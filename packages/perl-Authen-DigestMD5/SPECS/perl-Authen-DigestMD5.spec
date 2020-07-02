Summary:	SASL DIGEST-MD5 authentication (RFC2831)
Name:		perl-Authen-DigestMD5
Version:	0.04
Release:	36%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Authen-DigestMD5
Source0:	https://cpan.metacpan.org/modules/by-module/Authen/Authen-DigestMD5-%{version}.tar.gz
Patch0:		Authen-DigestMD5-0.04-UTF8.patch
Patch1:		Authen-DigestMD5-0.04-shellbang.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module supports DIGEST-MD5 SASL authentication as defined in RFC-2831.

%prep
%setup -q -n Authen-DigestMD5-%{version}

# Fix wrong script interpreter, and set permissions to avoid extra deps
%patch1
chmod -c 644 digest-md5-auth.pl

# Fix character encoding
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

# Get rid of sample code that introduces additional dep on perl(OpenLDAP)
rm -f %{buildroot}%{perl_vendorlib}/Authen/digest-md5-auth.pl

%check
make test

%files
%doc Changes README digest-md5-auth.pl
%{perl_vendorlib}/Authen/
%{_mandir}/man3/Authen::DigestMD5.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-36
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-33
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul  4 2018 Paul Howarth <paul@city-fan.org> - 0.04-30
- Spec clean-up
  - Classify buildreqs by usage
  - Use patch rather than sed to fix shellbangs
  - Drop legacy Group: tag
  - Drop buildroot cleaning in %%install section
  - Drop %%defattr, redundant since rpm 4.4
  - Don't need to remove empty directories from the buildroot

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-29
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-26
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-24
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-21
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-20
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.04-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.04-14
- Perl 5.16 rebuild

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> 0.04-13
- Nobody else likes macros for commands
- Use a patch rather than scripted iconv to fix character encoding
- BR: perl(Carp) and perl(Digest::MD5)

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.04-12
- Perl mass rebuild

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> 0.04-10
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> 0.04-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> 0.04-8
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.04-5
- Rebuild for new perl

* Fri Aug 10 2007 Paul Howarth <paul@city-fan.org> 0.04-4
- Clarify license as GPL v1 or later, or Artistic (same as perl)
- Add buildreq perl(Test::More)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 0.04-3
- Add buildreq of perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 0.04-2
- FE6 mass rebuild

* Fri May 12 2006 Paul Howarth <paul@city-fan.org> 0.04-1
- Initial build
