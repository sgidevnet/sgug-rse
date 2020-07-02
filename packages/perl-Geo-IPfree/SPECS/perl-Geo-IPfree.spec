%global cpan_name Geo-IPfree
%global cpan_version 1.151940
%global cpan_author BRICAS
Name:           perl-%{cpan_name}
# Normalize version to dotted format
Version:        %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:        12%{?dist}
Summary:        Look up the country of an IPv4 Address
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/%(echo '%{cpan_author}' | sed 's=\(.\)\(.\)=\1/\1\2/\1\2=')/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Memoize)
# Socket not used
# Tests only:
BuildRequires:  perl(Test::More) >= 0.47
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Socket)

%description
This package comes with it's own database to look up the IPv4's country, and
is totally free.

%prep
%setup -q -n %{cpan_name}-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes misc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 03 2016 Petr Pisar <ppisar@redhat.com> - 1.151.940-1
- Normalize version format

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.5.1.9.4.0-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5.1.9.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Petr Pisar <ppisar@redhat.com> - 1.1.5.1.9.4.0-1
- 1.151940 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4.3.6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.4.3.6.3.0-2
- Perl 5.22 rebuild

* Wed Feb 18 2015 Petr Pisar <ppisar@redhat.com> - 1.1.4.3.6.3.0-1
- 1.143630 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.4.1.6.7.0-2
- Perl 5.20 rebuild

* Tue Jul 01 2014 Petr Pisar <ppisar@redhat.com> - 1.1.4.1.6.7.0-1
- 1.141670 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3.2.8.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.2.8.7.0-1
- 1.132870 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3.1.6.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.1.6.5.0-2
- Perl 5.18 rebuild

* Wed Jun 26 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.1.6.5.0-1
- 1.131650 bump

* Fri May 17 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.0.4.5.0-1
- 1.130450 bump

* Wed Feb 13 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.0.1.1.0-1
- 1.130110 bump

* Tue Oct 23 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.2.8.8.0-1
- 1.122880 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.1.6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.1.6.6.0-1
- 1.121660 bump

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.0.4.6.0-2
- Perl 5.16 rebuild

* Tue Mar 20 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.0.4.6.0-1
- 1.1.2.0.4.6.0 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1.2.8.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Petr Pisar <ppisar@redhat.com> - 1.1.1.2.8.7.0-1
- 1.112870 bump
- Remove BuildRoot and defattr from spec code

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.0.2.8.7.0-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.2.8.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Petr Pisar <ppisar@redhat.com> - 1.1.0.2.8.7.0-2
- Add BuildRequires needed for tests

* Mon Nov 08 2010 Petr Pisar <ppisar@redhat.com> - 1.1.0.2.8.7.0-1
- 1.102870 bump

* Wed Aug 11 2010 Petr Pisar <ppisar@redhat.com> - 1.1.0.1.6.5.0-1
- 1.101650 bump
- Experimental RPM-extensible version numbering

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.4-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Allisson Azevedo <allisson@gmail.com> 0.4-1
- Initial rpm release.
