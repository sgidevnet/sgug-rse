Name:           perl-File-NFSLock
Version:        1.29
Release:        6%{?dist}
Summary:        Perl module to do NFS (or not) locking
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-NFSLock
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBB/File-NFSLock-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Sys::Hostname)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Program based of concept of hard linking of files being atomic across NFS. 
This concept was mentioned in Mail::Box::Locker (which was originally 
presented in Mail::Folder::Maildir). Some routine flow is taken from 
there -- particularly the idea of creating a random local file, hard 
linking a common file to the local file, and then checking the nlink 
status. Some ideologies were not complete (uncache mechanism, shared 
locking) and some coding was even incorrect (wrong stat index). 
File::NFSLock was written to be light, generic, and fast.

%prep
%setup -q -n File-NFSLock-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
chmod a-x examples/lock_test

%check
make test

%files
%doc Changes README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-1
- 1.29 bump

* Fri Nov 02 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-1
- 1.28 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-8
- Perl 5.26 rebuild

* Wed May 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-7
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-2
- Perl 5.22 rebuild

* Fri Nov 14 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-1
- 1.27 bump

* Wed Nov 12 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-1
- 1.26 bump

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-2
- Perl 5.20 rebuild

* Mon Aug 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-1
- 1.24 bump

* Tue Jul 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-1
- 1.23 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.21-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.21-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.21-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.21-2
- Perl mass rebuild

* Thu Jul 14 2011 Petr Sabata <contyk@redhat.com> - 1.21-1
- 1.21 bump
- Removing now obsolete Buildroot and defattr, general cleanup
- Correcting dependencies

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.20-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-8
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.20-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.20-3
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.20-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Jul 18 2006 Patrice Dumas <pertusus@free.fr> 1.20-2
- add examples/ to %%doc

* Tue Jul 18 2006 Patrice Dumas <pertusus@free.fr> 1.20-1
- Initial packaging
