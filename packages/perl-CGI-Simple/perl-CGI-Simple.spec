Name:           perl-CGI-Simple
Epoch:          1
Version:        1.21
Release:        4%{?dist}
Summary:        Simple totally OO CGI interface that is CGI.pm compliant
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CGI-Simple
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/CGI-Simple-%{version}.tar.gz
# https://github.com/markstos/CGI--Simple/commit/e811ab874a5e0ac8a99e76b645a0e537d8f714da
Patch0:         perl-CGI-Simple-CVE-2010-4411.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional tests
BuildRequires:  perl(HTTP::Request::Common)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.

%prep
%setup -q -n CGI-Simple-%{version}
%patch0 -p1
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make 

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license Artistic COPYING
%doc Changes README
%{perl_vendorlib}/CGI
%{_mandir}/man3/*.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.21-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Jitka Plesnikova <jplesnik@redhat.com> -  1:1.21-1
- update to 1.21

* Thu Oct  4 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.19-1
- update to 1.19

* Fri Jul 27 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.16-1
- update to 1.16

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.15-2
- Perl 5.28 rebuild

* Fri Apr 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.150-1
- 1.15 bump
- Add epoch of 1 (0.115 => 0.15)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.115-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.115-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.115-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.115-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.115-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.115-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.115-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.115-2
- Perl 5.22 rebuild

* Mon Mar 30 2015 Tom Callaway <spot@fedoraproject.org> - 1.115-1
- update to 1.115

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.113-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.113-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.113-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.113-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.113-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.113-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.113-6
- Perl 5.16 rebuild
- Specify all dependencies

* Sun Jan 22 2012 Tom Callaway <spot@fedoraproject.org> - 1.113-5
- rebuild with fixed perldoc BR

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.113-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.113-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Tom Callaway <spot@fedoraproject.org> - 1.113-1
- Update to 1.113, apply additional patch to fully resolve CVE-2010-4411

* Wed Dec  1 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.112-2
- patch for randomizing boundary (bz 658973)

* Mon Jul 12 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.112-1
- update to 1.112

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.108-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.108-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.108-1
- update to 1.108

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.103-3
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.103-2
- BR Test::More

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.103-1
- bump to 1.103

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-8
- add BR: perl(ExtUtils::MakeMaker)

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-7
- license fix

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-6
- rebuild for FC-6

* Sun Sep  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-5
- remove BR: perl
- add license texts

* Fri Jul 29 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-4
- cleanup chmod -x

* Wed Jul 27 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-3
- add missing documentation
- fix URL

* Fri Jul  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-2
- cleanups

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.077-1
- Initial package for Fedora Extras
