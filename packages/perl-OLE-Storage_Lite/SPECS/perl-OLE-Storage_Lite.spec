Name:		perl-OLE-Storage_Lite
Version:	0.20
Release:	3%{?dist}
Summary:	Simple Class for OLE document interface
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/OLE-Storage_Lite
Source0:	https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/OLE-Storage_Lite-%{version}.tar.gz
BuildArch:	noarch
# Build:
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl(vars)
# Tests:
BuildRequires:	perl(Test::More)
# Dependencies:
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:	perl(IO::Scalar)

%description
Simple Class for OLE document interface.

%prep
%setup -q -n OLE-Storage_Lite-%{version} 

# Fix line endings
perl -pi -e 's/\r\n/\n/g' Changes README sample/{README,*.pl}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README sample/
%{perl_vendorlib}/OLE/
%{_mandir}/man3/OLE::Storage_Lite.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Petr Pisar <ppisar@redhat.com> - 0.20-1
- 0.20 bump (CPAN RT#124513)

* Mon Oct  7 2019 Paul Howarth <paul@city-fan.org> - 0.19-27
- Spec tidy-up
  - Specify all build dependencies
  - Drop redundant buildroot cleaning in %%install section
  - Don't need to remove empty directories from the buildroot
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Make %%files list more explicit
  - Use tabs consistently

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-22
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-17
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-14
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.19-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.19-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.19-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.19-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.19-2
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.19-1
- Update to 0.19

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.18-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.18-1
- update to 0.18

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.17-1
- update to 0.17

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-1
- 0.15

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-9
- license tag fix

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-8
- bump for fc6

* Fri Jul  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-7
- bump to fix disttag

* Tue May 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-6
- fix defattr order

* Mon May  9 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-5
- fix spec file

* Sun Apr 24 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-4
- spec file cleanup

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-3
- rework spec to match template
- set to noarch

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-2
- add MODULE_COMPAT requires

* Fri Apr 1 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.14-1
- initial package
