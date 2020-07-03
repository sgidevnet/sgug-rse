Name: 		perl-Tree-Simple
Version: 	1.33
Release: 	9%{?dist}
Summary: 	Tree::Simple Perl module
License: 	GPL+ or Artistic
URL: 		https://metacpan.org/release/Tree-Simple
Source0: 	https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-Simple-%{version}.tgz
BuildArch: 	noarch

BuildRequires:  perl-generators
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(Test::Exception) >= 0.15 
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::Memory::Cycle) >= 1.02
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:  	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
A simple tree object.

%prep
%setup -q -n Tree-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Tree
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.33-1
- Update to 1.33.

* Fri Dec 22 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.32-1
- Update to 1.32.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-2
- Perl 5.26 rebuild

* Wed Apr 19 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.31-1
- Update to 1.31.

* Fri Mar 17 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.30-1
- Update to 1.30.
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-2
- Perl 5.24 rebuild

* Sat May 07 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.29-1
- Update to 1.29.

* Wed May 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.28-1
- Update to 1.28.

* Mon Apr 25 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.27-2
- Add %%license.

* Mon Apr 25 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.27-1
- Update to 1.27.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.26-2
- Modernize spec.

* Tue Dec 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.26-1
- Update to 1.26.
- Reflect upstream change to BRs.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-2
- Perl 5.22 rebuild

* Mon Jan 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.25-1
- Upstream update.

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-2
- Perl 5.20 mass

* Mon Sep 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.24-1
- Upstream update.
- Reflect upstream having dropped Test::Version.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.23-1
- Upstream update.
- BR: perl(Test::Version).

* Mon Sep 30 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.22-1
- Upstream update.

* Tue Sep 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.19-1
- Upstream update.
- Reflect upstream Source0-URL: having changed.
- Reflect upstream not being interested in Pod checks.
- Modernize spec.
- Fix bogus %%changelog date.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.18-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.18-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.18-9
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.18-7
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.18-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.18-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.18-2
- rebuild for new perl

* Mon Nov 19 2007 Ralf Corsépius <rc040203@freenet.de> - 1.18-1
- Upstream bugfix.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.17-2
- Update license tag.

* Fri Nov 03 2006 Ralf Corsépius <rc040203@freenet.de> - 1.17-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.16-2
- Mass rebuild.

* Tue Apr 04 2006 Ralf Corsépius <rc040203@freenet.de> - 1.16-1
- Upsteam update.
- BR: Scalar::Util >= 1.18.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 1.15-3
- Rebuild for perl-5.8.8.

* Sat Aug 20 2005 Ralf Corsepius <ralf@links2linux.de> - 1.15-2
- Spec cleanup.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 1.15-1
- Upstream update.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 1.14-1
- FE submission.
