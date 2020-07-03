Name:           perl-TeX-Hyphen
Version:        1.18
Release:        12%{?dist}
Summary:        Hyphenate words using TeX's patterns
License:        GPL+ or Artistic
URL:            http://www.adelton.com/perl/TeX-Hyphen/
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JANPAZ/TeX-Hyphen-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Benchmark)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
%{summary}.

%prep
%setup -q -n TeX-Hyphen-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/TeX/
%{_mandir}/man3/TeX::Hyphen.3pm*
%{_mandir}/man3/TeX::Hyphen::czech.3pm*
%{_mandir}/man3/TeX::Hyphen::german.3pm*
%{_mandir}/man3/TeX::Hyphen::utf8.3pm*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Jan Pazdziora <jpazdziora@redhat.com> - 1.18-1
- 1404061 - Rebase to upstream version 1.18.

* Sun Aug 28 2016 Jan Pazdziora <jpazdziora@redhat.com> - 1.17-1
- 1370818 - Rebase to upstream version 1.17.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Petr Šabata <contyk@redhat.com> - 1.16-1
- 1.16 bump

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-2
- Perl 5.22 rebuild

* Tue Feb 03 2015 Petr Šabata <contyk@redhat.com> - 1.15-1
- 1.15 bump

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Paul Howarth <paul@city-fan.org> - 1.01-1
- Update to 1.01
  - Updated the upstream URL to http://www.adelton.com/perl/TeX-Hyphen/
- Specify all dependencies
- Use %%{_fixperms} macro rather than our own chmod incantation
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Don't use macros for commands

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.140-19
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.140-16
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.140-14
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.140-12
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.140-11
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.140-10
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.140-7
- Rebuild for perl 5.10 (again)

* Wed Jan 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.140-6
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.140-5.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.140-5
- Rebuild for FC6.

* Thu Feb 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.140-4
- Rebuild for FC5 (perl 5.8.8).

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.140-3
- Dist tag.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.140-2
- rebuilt

* Fri Jun 11 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.140-0.fdr.1
- First build.
