Summary:	Perl module implementing the Diffie-Hellman key exchange system
Name:		perl-Crypt-DH
Version:	0.07
Release:	21%{?dist}
License:	GPL+ or Artistic
Url:		https://metacpan.org/release/Crypt-DH
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/Crypt-DH-%{version}.tar.gz
Patch0:		Crypt-DH-0.07-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:	noarch
# =============== Module Build ==================
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	sed
# =============== Module Runtime ================
BuildRequires:	perl(Math::BigInt) >= 1.60
BuildRequires:	perl(Math::BigInt::GMP) >= 1.24
# =============== Test Suite ====================
BuildRequires:	perl(Test::Builder::Module)
# =============== Module Runtime ================
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Math::BigInt) >= 1.60
Requires:	perl(Math::BigInt::GMP) >= 1.24

%description
Crypt::DH is a Perl implementation of the Diffie-Hellman key exchange system.
Diffie-Hellman is an algorithm by which two parties can agree on a shared
secret key, known only to them. The secret is negotiated over an insecure
network without the two parties ever passing the actual shared secret, or their
private keys, between them.

%prep
%setup -q -n Crypt-DH-%{version}
%patch0 -p1

# Remove unnecessary exec bits
find . -type f -print0 | xargs -0 chmod -c -x

# Fix line endings of documentation
sed -i -e 's/\r$//' README

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README ToDo
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::DH.3pm*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-20
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-17
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-14
- Perl 5.26 rebuild

* Tue May 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-13
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-11
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-8
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.07-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul  6 2012 Paul Howarth <paul@city-fan.org> 0.07-1
- Update to 0.07
  - Made Math::BigInt::* dependency dynamic to avoid Math::BigInt falling back
    to BigInt backends that are too slow for practical use
- This release by MITHALDU -> update source URL
- Always require perl(Math::BigInt) >= 1.60 and perl(Math::BigInt::GMP) ≥ 1.24
- Drop BR: perl(Test::More) as it's bundled
- BR: perl(Test::Builder::Module), requirement of bundled perl(Test::More)
- BR: perl(base), perl(Cwd), perl(File::Path), perl(File::Spec),
  perl(File::Temp) and perl(Text::ParseWords) for installer
- Use --skipdeps with Makefile.PL to stop it trying to download and install
  Math::BigInt::Pari
- Drop without-checks conditional as test suite is no longer slow
- Remove unnecessary exec bits from files in upstream tarball
- Package README, with fixed line endings

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> 0.06-18
- Perl 5.16 rebuild

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> 0.06-17
- Nobody else likes macros for commands

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.06-16
- Perl mass rebuild

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> 0.06-14
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> 0.06-13
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> 0.06-12
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Paul Howarth <paul@city-fan.org> 0.06-9
- BuildRequire and Require a GMP support module, either Math::GMP or
  Math::BigInt::GMP depending on how recent Math::BigInt is

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.06-8
- Rebuild for new perl

* Sat Aug 11 2007 Paul Howarth <paul@city-fan.org> 0.06-7
- Clarify license as GPL v1 or later, or Artistic (same as perl)
- Add buildreq perl(Test::More)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 0.06-6
- Buildrequire perl(ExtUtils::MakeMaker)
- Fix argument order for find with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 0.06-5
- FE6 mass rebuild

* Thu Feb 16 2006 Paul Howarth <paul@city-fan.org> 0.06-4
- Simplify conditional build by not using %%bcond_* macros

* Mon Dec 12 2005 Paul Howarth <paul@city-fan.org> 0.06-3
- Add support for FC-3, which doesn't have %%bcond_with{,out} predefined

* Fri Dec  9 2005 Paul Howarth <paul@city-fan.org> 0.06-2
- Add facility to skip test suite at build time if desired

* Tue Nov 29 2005 Paul Howarth <paul@city-fan.org> 0.06-1
- Initial build
