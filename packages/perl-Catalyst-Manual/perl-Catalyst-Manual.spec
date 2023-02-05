Name:           perl-Catalyst-Manual
Summary:        Catalyst web framework manual
Epoch:          1
Version:        5.9010
Release:        3%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Manual-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Manual
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This is the manual to the Catalyst web framework.

%prep
%setup -q -n Catalyst-Manual-%{version}

#remove extraneous .gitignore
find -name .gitignore -print0 | xargs -0 rm -f

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.9010-2
- Perl 5.30 rebuild

* Sun Apr 28 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1:5.9010-1
- Update to 5.9010

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9009-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9009-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.9009-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9009-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.9009-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.9009-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.9009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.9009-2
- Perl 5.22 rebuild

* Sun Dec 14 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1:5.9009-1
- Update to 5.9009

* Fri Nov 21 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1:5.9008-1
- Update to 5.9008

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.9006-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.9006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.9006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1:5.9006-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.9006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 1:5.9006-1
- update to latest upstream version

* Fri Nov 02 2012 Iain Arnell <iarnell@gmail.com> 1:5.9005-1
- update to latest upstream version
- disable M:I:AutoInstall

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.9004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:5.9004-2
- Perl 5.16 rebuild

* Sat May 12 2012 Iain Arnell <iarnell@gmail.com> 1:5.9004-1
- update to latest upstream version

* Sat Feb 18 2012 Iain Arnell <iarnell@gmail.com> 1:5.9003-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 1:5.9002-3
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.9002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 01 2011 Iain Arnell <iarnell@gmail.com> 1:5.9002-1
- update to latest upstream version

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:5.8005-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.8005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Iain Arnell <iarnell@gmail.com> 1:5.8005-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:5.8004-4
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:5.8004-3
- Mass rebuild with perl-5.12.0

* Thu Feb 25 2010 Chris Weyl <cweyl@alumni.drew.edu> 1:5.8004-2
- rebuild so -tests correctly uses epoch in versioned dep

* Tue Feb 23 2010 Chris Weyl <cweyl@alumni.drew.edu> 1:5.8004-1
- update by Fedora::App::MaintainerTools 0.003
- PERL_INSTALL_ROOT => DESTDIR
- dropped old BR on perl(Test::Pod)
- dropped old BR on perl(Test::Pod::Coverage)

* Thu Jan 28 2010 Chris Weyl <cweyl@alumni.drew.edu> 1:5.8003-1
- auto-update to 5.8003 (by cpan-spec-update 0.01)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:5.8002-2
- rebuild against perl 5.10.1

* Sun Dec 06 2009 Chris Weyl <cweyl@alumni.drew.edu> 1:5.8002-1
- auto-update to 5.8002 (by cpan-spec-update 0.01)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.8000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.8000-2
- add br on CPAN until bundled M::I is installed

* Sun May 31 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.8000-1
- auto-update to 5.8000 (by cpan-spec-update 0.01)

* Sun May 17 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.7021-1
- auto-update to 5.7021 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)

* Sat Apr 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.7020-2
- reclaim Catalyst::Manual

* Wed Apr 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.7020-1
- update to 5.7020

* Mon Mar 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.7017-1
- update to 5.7017

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.7016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 5.7016-1
- update to 5.7016

* Sat Nov 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7014-1
- update to 5.7014

* Fri Jul 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7013-1
- update to 5.7013
- don't just exclude Catalyst::Manual's man page, but the .pm as well.
  (RH BZ#455151)

* Wed Jun 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7012-2
- re-exclude Catalyst::Manual.3pm

* Sun Jun 22 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.7012-1
- update to 7.012...
- ...and add an epoch.  sigh.

* Sun Jun 22 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.701003-1
- update to 5.701003
- un-exclude Catalyst::Manual pod as it's been moved over from
  Catalyst::Runtime to this dist
- License tag update: GPL -> GPL+

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.700701-3
- rebuild for new perl

* Tue Jun 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.700701-2
- bump

* Fri Apr 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.700701-1
- Specfile autogenerated by cpanspec 1.71.
