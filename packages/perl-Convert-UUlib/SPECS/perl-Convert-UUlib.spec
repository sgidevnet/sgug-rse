# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Convert-UUlib

Summary:	Perl interface to the uulib library
Name:		perl-Convert-UUlib
Epoch:		2
Version:	1.71
Release:	1%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/%{pkgname}
Source:		https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{pkgname}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(Canary::Stability)
BuildRequires:	perl(Carp)
BuildRequires:	perl(common::sense)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl interface to the uulib library (a.k.a. uudeview/uuenview).

%prep
%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%make_install
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING*
%doc Changes README doc/*
%{perl_vendorarch}/Convert
%{perl_vendorarch}/auto/Convert
%{_mandir}/man?/Convert::UUlib*

%changelog
* Sun Apr 26 2020 Robert Scheck <robert@fedoraproject.org> 2:1.71-1
- Upgrade to 1.71 (#1804272)
 
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Robert Scheck <robert@fedoraproject.org> 2:1.6-1
- Upgrade to 1.6 (#1711098)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.5-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.5-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:1.5-9
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.5-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.5-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.5-1
- 1.5 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.4-11
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.4-10
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2:1.4-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 2:1.4-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Robert Scheck <robert@fedoraproject.org> 2:1.4-1
- Upgrade to 1.4

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.34-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Robert Scheck <robert@fedoraproject.org> 1:1.34-1
- Upgrade to 1.34

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.33-3
- Rebuild for fixing problems with vendorach/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.33-2
- Mass rebuild with perl-5.12.0

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 1:1.33-1
- Upgrade to 1.33

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1:1.12-2
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Robert Scheck <robert@fedoraproject.org> 1:1.12-1
- Upgrade to 1.12

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1:1.11-2
- Rebuild against gcc 4.4 and rpm 4.6

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:1.11-1
- Fedora 10 alpha general package cleanup

* Sat May 31 2008 Robert Scheck <robert@fedoraproject.org>
- 1:1.09-5
- Fixed %%check section in order to get the package built

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com>
- 1:1.09-4
- Rebuild for new perl

* Fri Feb 08 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:1.09-3
- gcc 4.3 rebuild

* Mon Aug 13 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:1.09-2
- Fix License

* Sun Aug 12 2007 Robert Scheck <robert@fedoraproject.org> 1:1.09-1
- Upgrade to 1.09 and rebuilt for EPEL branches (#250865)
- Added build requirement to perl(ExtUtils::MakeMaker)

* Tue Mar 20 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:1.08-2
- add perl-devel BR

* Mon Jan 08 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.08-1

* Sat Sep 02 2006  Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.06-4
- FE6 Rebuild

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.06-3
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 17 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.06-2
- bump epoch to force updates

* Mon Jan 16 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.06-1
- 1.06 (can't believe I'm still listed as this package owner)

* Thu Jun  2 2005 Paul Howarth <paul@city-fan.org>
- 1.051-2%%{?dist}
- add dist tags for ease of syncing with FC-3 & FC-4
- remove redundant perl buildreq
- remove redundant "make test" from %%build (it's in %%check)
- remove MANIFEST from %%doc

* Sat May 21 2005 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 1.051-1
- update to 1.051

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Apr 19 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 0:1.03-0.fdr.1
- Updated to 1.03

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 0:1.02-0.fdr.1
- Updated to 1.02

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 0:1.01-0.fdr.2
- Merge a few tweaks from 0:0.31-0.fdr.4 (bug #375)

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 0:1.01-0.fdr.1
- Fedorization
- Cleanup

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com>
- 1.01-0
- Updated to release 1.01.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com>
- 0.31-0
- Updated to release 0.31.
- Initial package. (using DAR)
