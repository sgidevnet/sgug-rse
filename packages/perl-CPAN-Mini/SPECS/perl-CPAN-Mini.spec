Name:           perl-CPAN-Mini
Summary:        Create a minimal mirror of CPAN
Version:        1.111016
Release:        15%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CPAN-Mini-%{version}.tar.gz 
URL:            https://metacpan.org/release/CPAN-Mini
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib) >= 1.20
# CPAN is optional and not used at tests
# CPANPLUS::Backend is optional and not used at tests
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir) >= 0.57
BuildRequires:  perl(File::Path) >= 2.04
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(LWP::UserAgent) >= 5
BuildRequires:  perl(Pod::Usage) >= 1.00
BuildRequires:  perl(URI) >= 1
# Tests:
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %__requires_exclude|^perl\\(File::HomeDir\\)$

%description
CPAN::Mini provides a simple mechanism to build and update a minimal 
mirror of the CPAN on your local disk containing only those files 
needed to install the newest version of every distribution. 

%prep
%setup -q -n CPAN-Mini-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} + 
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man[13]/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.111016-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.111016-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.111016-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.111016-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.111016-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.111016-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.111016-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.111016-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.111016-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.111016-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.111016-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.111016-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.111016-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.111016-2
- Perl 5.20 rebuild

* Tue Aug 12 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.111016-1
- 1.111016 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.111015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 17 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.111015-1
- 1.111015 bump

* Mon Nov 25 2013 Petr Pisar <ppisar@redhat.com> - 1.111014-1
- 1.111014 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.111013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.111013-2
- Perl 5.18 rebuild

* Mon Apr 15 2013 Petr Pisar <ppisar@redhat.com> - 1.111013-1
- 1.111013 bump
- Stop packaging internal tests

* Tue Apr 02 2013 Petr Pisar <ppisar@redhat.com> - 1.111012-1
- 1.111012 bump

* Fri Feb 08 2013 Petr Šabata <contyk@redhat.com> - 1.111011-1
- 1.111011 bump

* Thu Oct 25 2012 Petr Šabata <contyk@redhat.com> - 1.111010-1
- 1.111010 bugfix bump
- Drop command macros
- Drop the old tests subpackage obsolete/provides

* Wed Sep 12 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.111009-1
- 1.111009 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.111008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.111008-2
- Perl 5.16 rebuild

* Fri Jan 27 2012 Marcela Mašláňová <mmaslano@redhat.com> 1.111008-1
- update

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 1.111007-3
- drop tests subpackage; move tests to main package documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.111007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 1.111007-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- don't package tests as doc
- remove explicit requires

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.100630-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100630-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.100630-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.100630-2
- Mass rebuild with perl-5.12.0

* Tue Mar 23 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.100630-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (1.100630)
- added a new br on perl(Carp) (version 0)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.11)
- added a new br on perl(File::Basename) (version 0)
- added a new br on perl(File::Copy) (version 0)
- added a new br on perl(File::Find) (version 0)
- added a new br on perl(File::Spec) (version 0)
- added a new br on perl(File::Temp) (version 0)
- added a new br on perl(Getopt::Long) (version 0)
- added a new br on perl(LWP::UserAgent) (version 5)
- added a new br on perl(Pod::Usage) (version 1.00)
- dropped old BR on perl(LWP)
- added a new req on perl(Carp) (version 0)
- added a new req on perl(Compress::Zlib) (version 1.20)
- added a new req on perl(File::Basename) (version 0)
- added a new req on perl(File::Copy) (version 0)
- added a new req on perl(File::Find) (version 0)
- added a new req on perl(File::HomeDir) (version 0.57)
- added a new req on perl(File::Path) (version 2.04)
- added a new req on perl(File::Spec) (version 0)
- added a new req on perl(File::Temp) (version 0)
- added a new req on perl(Getopt::Long) (version 0)
- added a new req on perl(LWP::UserAgent) (version 5)
- added a new req on perl(Pod::Usage) (version 1.00)
- added a new req on perl(URI) (version 1)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.576-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.576-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.576-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.576-1
- update to 0.576

* Fri May 30 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.571-2
- bump

* Thu May 29 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.571-1
- update to 0.571

* Wed Apr 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.568-2
- additional br 

* Wed Apr 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.568-1
- Specfile autogenerated by cpanspec 1.74.
