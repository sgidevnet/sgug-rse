Name:           perl-File-Listing
Version:        6.04
Release:        24%{?dist}
Summary:        Parse directory listing
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-Listing
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/File-Listing-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
# Tests:
# Do not BuildRequire optinal perl(LWP::Simple) to break dependency circle.
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(Time::Local)
Conflicts:      perl-libwww-perl < 6

# RPM 4.9 style
# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(HTTP::Date\\)\s*$
# Do not provide private modules
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(File::Listing::

%description
This module exports a single function called parse_dir(), which can be used
to parse directory listings.

%prep
%setup -q -n File-Listing-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-24
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-21
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-18
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-15
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-10
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Šabata <contyk@redhat.com> - 6.04-6
- Add missing built-time dependencies
- Modernize the spec a bit

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 6.04-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 6.04-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.04-1
- 6.04 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Petr Pisar <ppisar@redhat.com> - 6.03-1
- 6.03 bump
- Build-require perl(Test::More) needed for tests

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 6.02-3
- RPM 4.9 dependency filtering added

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.02-2
- Perl mass rebuild

* Wed Mar 23 2011 Petr Pisar <ppisar@redhat.com> - 6.02-1
- 6.02 bump

* Wed Mar 16 2011 Petr Pisar <ppisar@redhat.com> 6.01-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Conflict with perl-libwww-perl-5* and older
- Do not provide private modules
