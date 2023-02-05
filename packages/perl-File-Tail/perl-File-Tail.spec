Name:           perl-File-Tail
Version:        1.3
Release:        13%{?dist}
Summary:        Perl extension for reading from continously updated files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-Tail
Source0:	https://cpan.metacpan.org/authors/id/M/MG/MGRABNAR/File-Tail-%{version}.tar.gz
Patch0:		File-Tail-1.3-sanity-checks.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The primary purpose of File::Tail is reading and analysing log files
while they are being written, which is especially useful if you are
monitoring the logging process with a tool like Tobias Oetiker's MRTG.

%prep
%setup -q -n File-Tail-%{version}
%patch0 -p1 -b .fix

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Tail.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 1.3-7
- apply sanity checks

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug  4 2015 Tom Callaway <spot@fedoraproject.org> - 1.3-1
- update to 1.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-2
- Perl 5.22 rebuild

* Tue Apr 21 2015 Tom Callaway <spot@fedoraproject.org> - 1.2-1
- update to 1.2

* Thu Mar 19 2015 Tom Callaway <spot@fedoraproject.org> - 1.0-1
- update to 1.0

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.3-21
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.99.3-18
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.99.3-15
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.99.3-13
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.99.3-11
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.99.3-10
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.99.3-9
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.99.3-6
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.99.3-5.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Jun  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.99.3-5
- Added the requirement perl(:MODULE_COMPAT_x.x.x).

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.99.3-4
- Rebuild for FC5 (perl 5.8.8).

* Fri Jan  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.99.3-3
- Another typo corrected.

* Wed Jan  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.99.3-2
- Correction of spelling error in the description.

* Thu Sep 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.99.3-1
- 0.99.3.
- Specfile cleanups.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.98-4
- rebuilt

* Sun Feb  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.98-0.fdr.3
- BuildRequire Time::HiRes (bug 731).
- Run tests in the %%check section.
- Reduce directory ownership bloat.

* Mon Nov 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.98-0.fdr.2
- Specfile rewrite.

* Tue Sep 17 2003 Warren Togami <warren@togami.com> - 0.98-0.fdr.1
- Specfile autogenerated.
