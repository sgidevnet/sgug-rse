Name:           perl-Crypt-OpenSSL-DSA
Version:        0.19
Release:        13%{?dist}
Summary:        Perl interface to OpenSSL for DSA
License:        GPL+ or Artistic 
URL:            https://metacpan.org/release/Crypt-OpenSSL-DSA
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMX/Crypt-OpenSSL-DSA-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Crypt::OpenSSL::DSA - Digital Signature Algorithm using OpenSSL

%prep
%setup -q -n Crypt-OpenSSL-DSA-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump

* Fri Dec 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Tue Nov 01 2016 Petr Pisar <ppisar@redhat.com> - 0.15-7
- Restore support for setting private key before public key (bug #1383651)

* Thu Oct 27 2016 Petr Pisar <ppisar@redhat.com> - 0.15-6
- Adapt to OpenSSL 1.1.0 (bug #1383651)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.22 rebuild

* Tue Feb 17 2015 Wes Hardaker <wjhns174@hardakers.net> - 0.15-1
- Update to 0.15

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.14-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Wes Hardaker <wjhns174@hardakers.net> - 0.14-1
- Update to upstream 0.14 for bug fixes

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.13-21
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.13-19
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-17
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-16
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.13-15
- rebuild against perl 5.10.1

* Mon Aug 31 2009 Stepan Kasal <skasal@redhat.com> - 0.13-14
- re-enable tests

* Fri Aug 28 2009 Stepan Kasal <skasal@redhat.com> - 0.13-13
- disable tests to work around bug #520152

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.13-12
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Wes Hardaker <wjhns174@hardakers.net> - 0.13-9
- Fix CVE-2009-0129 and have do_verify croak on fatal error

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.13-8
- rebuild with new openssl

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.13-7
- rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.13-6
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.13-5
 - Rebuild for deps

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.13-4
- Rebuild for selinux ppc32 issue.

* Mon May 14 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.13-3
- BuildRequire perl(Test) perl(ExtUtils::MakeMaker) perl(Digest::SHA1)
  and perl(File::Temp)
- Fixed source code URL

* Tue May  8 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.13-2
- Add BuildRequire openssl-devel
- Don't manually require openssl
- Use vendorarch instead of vendorlib 

* Thu Apr 19 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.13-1
- Initial version
