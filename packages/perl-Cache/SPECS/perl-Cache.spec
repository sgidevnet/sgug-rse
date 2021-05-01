Name:           perl-Cache
Version:        2.11
Release:        14%{?dist}
Summary:        The Cache interface
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Cache
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Cache-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DB_File) >= 1.72
BuildRequires:  perl(Date::Parse) >= 2.24
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::NFSLock) >= 1.2
BuildRequires:  perl(File::Path) >= 1
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Heap::Elem)
BuildRequires:  perl(Heap::Fibonacci) >= 0.01
BuildRequires:  perl(IO::File) >= 1.08
BuildRequires:  perl(IO::Handle) >= 1.21
BuildRequires:  perl(IO::String) >= 1.02
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Storable) >= 1
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol) >= 1.02
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::TrailingSpace)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:  perl(IO::Handle) >= 1.21

%{?perl_default_filter}

%description
The Cache modules are designed to assist a developer in persisting data 
for a specified period of time. Often these modules are used in web 
applications to store data locally to save repeated and redundant 
expensive calls to remote machines or databases.

The Cache interface is implemented by derived classes that store cached 
data in different manners (such as as files on a filesystem, or in memory).


%package -n perl-Cache-Tester
Summary:        Test utility for perl Cache implementations
Requires:       %{name} = %{version}-%{release}

%description -n perl-Cache-Tester
This module is used to run tests against an instance of a Cache implementation
to ensure that it operates as required by the Cache specification.


%prep
%setup -q -n Cache-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes design.dia LICENSE README
%exclude %{perl_vendorlib}/Cache/Tester.pm
%exclude %{_mandir}/man3/Cache::Tester.3*
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%files -n perl-Cache-Tester
%{perl_vendorlib}/Cache/Tester.pm
%{_mandir}/man3/Cache::Tester.3*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-2
- Perl 5.22 rebuild

* Sun Mar 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.11-1
- Update to 2.11

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.10-1
- Update to 2.10

* Sun Feb 09 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.09-1
- Update to 2.09

* Sun Feb 02 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.08-1
- Update to 2.08

* Sun Sep 15 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 2.06-1
- Update to 2.06
- Remove defattr and Group macros (no longer used)

* Sun Sep 08 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 2.05-1
- Update to 2.05
- Convert build-system to Module::Build
- Add perl(Test::Pod) as a BR to run more tests

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.04-16
- Perl 5.18 rebuild
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.04-13
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.04-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-9
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Iain Arnell <iarnell@gmail.com> 2.04-8
- split Cache::Tester into separate sub-package to avoid runtime dependency on
  Test::More
- use perl_default_filter
- clean up spec for modern rpmbuild

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.04-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.04-3
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.04-2.3
- add BR: perl(Test::More)

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.04-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Wed Sep 20 2006 Patrice Dumas <pertusus@free.fr> 2.04-2
- add missing BuildRequires

* Tue Jul 18 2006 Patrice Dumas <pertusus@free.fr> 2.04-1
- Initial packaging
