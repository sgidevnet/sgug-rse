Name:           perl-IO-Interface
Version:        1.09
Release:        18%{?dist}
Summary:        Perl extension for accessing network card configuration information
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IO-Interface
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/IO-Interface-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
IO::Interface adds methods to IO::Socket objects that allows them to
be used to retrieve and change information about the network
interfaces on your system.  In addition to the object-oriented access
methods, you can use a function-oriented style.

%prep
%setup -q -n IO-Interface-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorarch}/IO/
%{perl_vendorarch}/auto/IO/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-18
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-12
- Perl 5.28 rebuild

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 1.09-11
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-2
- Perl 5.22 rebuild

* Fri Mar 27 2015 Tom Callaway <spot@fedoraproject.org> - 1.09-1
- update to 1.09

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-16
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.05-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.05-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.05-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.05-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-1
- update to 1.05

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.03-3
- rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.03-2.2
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.03-1.2
- add BR: perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.03-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Wed Jan 24 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-1
- Update do 1.03.

* Thu Sep 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.02-1
- Update do 1.02.

* Sun Sep 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.98-2
- Rebuild for FC6.

* Mon Jan 30 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.98-1
- First build.
