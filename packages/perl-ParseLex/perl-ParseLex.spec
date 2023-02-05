Name:           perl-ParseLex
Summary:        Generator of lexical analyzers
Version:        2.21
Release:        12%{?dist}
License:        GPL+ or Artistic
BuildArch:      noarch
URL:            https://metacpan.org/release/ParseLex
Source:         https://cpan.metacpan.org/authors/id/P/PS/PSCUST/ParseLex-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  sed
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(integer)
BuildRequires:  perl(Parse::Template) >= 3.01
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
The classes "Parse::Lex" and "Parse::CLex" create lexical analyzers.

%prep
%setup -q -n ParseLex-%{version} 

# remove all execute bits from the doc stuff and fix interpreter
# so that dependency generator doesn't try to fulfill deps
find examples -type f -exec chmod -x {} 2>/dev/null ';'
find examples -type f -exec sed -i 's#/usr/local/bin/perl#/usr/bin/perl#' {} 2>/dev/null ';'

%build
perl Makefile.PL INSTALLDIRS="vendor"
make %{?_smp_mflags}

%check
make test

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT create_packlist=0

### Clean up buildroot
find $RPM_BUILD_ROOT -name .packlist -exec rm {} \;

%files
%doc Changes README examples
%{perl_vendorlib}/Parse/
%{_mandir}/man3/*.3pm*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-1
- 2.21 bump
- Modernize spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.19-13
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.19-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.19-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.19-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.19-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.19-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 15 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.19-1
- Upstream upgrade (Fix perl-5.12.0 build breakdown).
- Spec file cleanup.

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.15-17
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.15-16
- rebuild against perl 5.10.1

* Mon Nov 16 2009 Jeff Fearn <jfearn@redhat.com> - 2.15-15
- Fix Requires

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 7 2008  Jeff Fearn <jfearn@redhat.com> 2.15-12
- Need Requires for EPEL

* Fri Jan 18 2008 Jeff Fearn <jfearn@redhat.com> 2.15-11
- iconv in the prep, beer on the way

* Thu Jan 17 2008 Jeff Fearn <jfearn@redhat.com> 2.15-10
- Fixed unwanted Provides Filter
- Consistant use of macros
- Better summary

* Wed Jan 16 2008 Jeff Fearn <jfearn@redhat.com> 2.15-9
- Add missing BuildRequires

* Wed Jan 16 2008 Jeff Fearn <jfearn@redhat.com> 2.15-8
- Changed Development/Languages to Development/Libraries
- Fixed test
- Removed useless-explicit-provides
- Converted Changes to utf-8

* Tue Jan 08 2008 Jeff Fearn <jfearn@redhat.com> 2.15-7
- Remove %%doc from man files, used glob
- Simplify Parse in filelist
- Simplify %%clean
- Remove OPTIMIZE setting from make call
- Change buildroot to fedora style
- Remove unused defines

* Mon Jan 07 2008 Jeff Fearn <jfearn@redhat.com> 2.15-6
- Tidy up spec

* Mon Dec 10 2007 Jeff Fearn <jfearn@redhat.com> 2.15-5
- noarch FTW
- add dist to release

* Tue Apr 10 2007 ttrinks@redhat.com
- Rebuilt for RHEL5
- Changed arch from noarch to i386

* Mon Jul 31 2006 mschick@redhat.com
- Tagged for e-s-o repo
- Rebuilt for RHEL4 

* Thu Sep 25 2003 pgampe@redhat.com
- Patch broken syntax in upstream Template.pm
