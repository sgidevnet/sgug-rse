Name:           perl-Palm
Version:        1.400
Release:        14%{?dist}
Summary:        Palm OS utility functions
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Palm
Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Palm::PDB)
BuildRequires:  perl(Palm::Raw)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Provides:       perl-p5-Palm = %{version}-%{release}
Obsoletes:      perl-p5-Palm =< 1.013-4
%{?perl_default_filter}

%description
This module provides functions and handlers to manipulate files used
by Palm PDAs (AddressBook, ToDo, Memo, ...).

%prep
%setup -q -n Palm-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes FAQ README TODO examples
%{perl_vendorlib}/Palm*
%{_mandir}/man3/Palm*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.400-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.400-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.400-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.400-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.400-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.400-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.400-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.400-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.400-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.400-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.400-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.400-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.400-2
- Perl 5.22 rebuild

* Sun Mar 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.400-1
- Update to 1.400

* Sun Feb 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.015-1
- Update to 1.015

* Tue Feb 03 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.014-2
- Take into account review comments (#1188648)

* Sat Jan 31 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.014-1
- Rename package to perl-Palm
- Update to 1.0.14

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.013-1
- Update to 1.013
- Fix incorrect dates in spec changelog

* Mon Aug  5 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.012-13
- Fix build with unversioned %%{_docdir_fmt}.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.012-11
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 1.012-9
- Remove no-longer-used macros
- Add perl default filter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.012-7
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.012-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.012-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.012-2
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.012-1
- Update to 1.012

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.011-2
- rebuild against perl 5.10.1

* Mon Sep 21 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.011-1
- Update to 1.011
- Fix an rpmlint complaint in the changelog

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.009-3
- Add Test::More to the BuildRequires so that the tests can actually run

* Wed Jun 17 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.009-2
- Enable tests
- Add examples directory to the documentation

* Mon Jun 11 2007 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.009-1
- Specfile autogenerated by cpanspec 1.70.
