Name:           perl-Net-IPv6Addr
Version:        1.01
Release:        2%{?dist}
Summary:        Perl module to check validity of IPv6 addresses

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-IPv6Addr
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/Net-IPv6Addr-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Math::Base85) >= 0.2
BuildRequires:  perl(Math::BigInt) >= 1.999813
BuildRequires:  perl(Net::IPv4Addr) >= 0.10
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Math::Base85) >= 0.2
Requires:       perl(Math::BigInt) >= 1.999813
Requires:       perl(Net::IPv4Addr) >= 0.10

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::Base85\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Math::BigInt\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Net::IPv4Addr\\)\s*$

%description
Net::IPv6Addr checks strings for valid IPv6 addresses, as specified in
RFC1884. You throw possible addresses at it, it either accepts them or throws
an exception.

%prep
%setup -q -n Net-IPv6Addr-%{version}
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc examples Changes README
%{perl_vendorlib}/*
%{_mandir}/man?/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-2
- Perl 5.32 rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump

* Wed Jun 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-1
- 1.0 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-1
- 0.96 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-1
- 0.91 bump

* Mon Oct 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.9-1
- 0.9 bump

* Mon Aug 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.7-1
- 0.7 bump

* Fri Aug 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6-1
- 0.6 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-22
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-18
- Specify all dependencies
- Modernize spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-16
- Perl 5.22 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.2-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2-8
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2-7
- Mass rebuild with perl-5.12.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2-4
- rebuild for new perl

* Mon May 28 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.2-3
- Fix license
- Add explicit Requires on perl(Math::Base85)
- Add missing BRs

* Fri May 11 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.2-2
- Add missing perl-Math-Base85 BR

* Sat May 05 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.2-1
- Initial build
