Name:           perl-Net-CIDR
Version:        0.20
Release:        5%{?dist}
Summary:        Manipulate IPv4/IPv6 netblocks in CIDR notation
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-CIDR
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-CIDR-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Test Suite
# (no additional dependencies)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
The Net::CIDR package contains functions that manipulate lists of IP netblocks
expressed in CIDR notation. The Net::CIDR functions handle both IPv4 and IPv6
addresses.

%prep
%setup -q -n Net-CIDR-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc ChangeLog README
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::CIDR.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-2
- Perl 5.30 rebuild

* Wed Apr 17 2019 Paul Howarth <paul@city-fan.org> - 0.20-1
- Update to 0.20
  - _ipcmp: Handle comparison of mixed IPv4 and IPv6-specified addresses,
    allowing cidrlookup() to look up IPv6-mapped IPv4 addresses in IPv4
    address ranges, and vice versa

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.28 rebuild

* Tue Jun 12 2018 Paul Howarth <paul@city-fan.org> - 0.19-1
- Update to 0.19
- Drop redundant %%{?perl_default_filter}
- Classify buildreqs by usage
- Don't need to delete empty directories from the buildroot
- Use %%license
- Make %%files list more explicit

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-2
- Perl 5.22 rebuild

* Sun Feb 08 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.18-1
- Update to 0.18

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.17-2
- Perl 5.18 rebuild

* Sun Jun 09 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.17-1
- Update to 0.17
- Add perl default filter
- Remove no-longer-used macros

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 0.15-2
- Perl 5.16 rebuild

* Sun Apr 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.15-1
- Update to 0.15

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Jul 01 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.14-1
- Update to 0.14

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.13-3
- rebuild against perl 5.10.1

* Mon Nov  9 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.13-2
- Fix License tag
- Remove Net-CIDR.spec from %%doc
- List files more explicitely

* Fri Sep 25 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.13-1
- Specfile autogenerated by cpanspec 1.78.
