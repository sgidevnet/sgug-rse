Name:		perl-Jcode
Version:	2.07
Release:	32%{?dist}
Summary:	Perl extension interface for converting Japanese text
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Jcode
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Jcode-%{version}.tar.gz
Patch0:		Jcode-2.07-UTF-8.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Encode::Alias)
BuildRequires:	perl(Encode::Guess)
BuildRequires:	perl(Encode::JP::H2Z)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(diagnostics)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:	perl(Encode)
Requires:	perl(Encode::Alias)
Requires:	perl(Encode::Guess)
Requires:	perl(Encode::JP::H2Z)
Requires:	perl(MIME::Base64)
Requires:	perl(Scalar::Util)

%description
%{summary}.

%prep
%setup -q -n Jcode-%{version}

# Fix character encoding of pod file
%patch0 -p1 -b .timestamp
touch --reference=Jcode/Nihongo.pod.timestamp Jcode/Nihongo.pod
rm Jcode/Nihongo.pod.timestamp

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
%doc Changes* README
%{perl_vendorlib}/Jcode.pm
%dir %{perl_vendorlib}/Jcode/
%doc %{perl_vendorlib}/Jcode/Nihongo.pod
%{_mandir}/man3/Jcode.3*
%{_mandir}/man3/Jcode::Nihongo.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-32
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Paul Howarth <paul@city-fan.org> - 2.07-30
- Spec tidy-up
  - Classify buildreqs by usage
  - Drop redundant buildroot cleaning in %%install section
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Retain timestamp of Jcode/Nihongo.pod when patching

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-28
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-25
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-22
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-17
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-16
- Perl 5.20 rebuild

* Mon Aug 11 2014 Paul Howarth <paul@city-fan.org> - 2.07-15
- Specify all dependencies
- Drop %%defattr, redundant since rpm 4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.07-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.07-9
- Perl 5.16 rebuild

* Thu Apr 26 2012 Paul Howarth <paul@city-fan.org> 2.07-8
- Don't need to remove empty directories from buildroot
- Don't need to run test suite with LC_ALL=C
- BR: perl(Data::Dumper)
- Use search.cpan.org source URL

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> 2.07-7
- Add buildreqs for perl core modules that might be dual-lived
- Nobody else likes macros for commands
- Use patch rather than scripted edit to fix encoding of Nihongo.pod

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> 2.07-6
- Perl mass rebuild

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> 2.07-4
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sun May  2 2010 Marcela Maslanova <mmaslano@redhat.com> 2.07-3
- Mass rebuild with perl 5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> 2.07-2
- Rebuild against perl 5.10.1

* Mon Aug 24 2009 Paul Howarth <paul@city-fan.org> 2.07-1
- Update to 2.07 (fix mime_encode, CPAN RT#29049)
- Run test suite in "C" locale to support build on old distributions
- Fix argument order for find with -depth
- Encode manpages in UTF-8
- Include old Changes file too
- Mark POD file as %%doc
- Add explicit perl(MIME::Base64) dependency for MIME header support

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.06-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 2.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.06-6
- Rebuild for new perl

* Thu Sep 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.06-5
- Fix license (thanks Tom)

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.06-4
- Fix license tag (like perl itself)

* Mon Aug 13 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.06-3
- BR perl-Test-Simple

* Mon Aug 13 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.06-2
- BR perl-devel

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.06-1
- Update to 2.06

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 2.03-3
- Rebuild for FC5

* Thu Oct 27 2005 Aurelien Bompard <gauret[AT]free.fr> 2.03-2
- Build as noarch (#171916)

* Sat Sep 03 2005 Aurelien Bompard <gauret[AT]free.fr> 2.03-1
- Update to 2.03
- Be closer to perl spec template

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- Rebuilt

* Sat Dec 04 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.88-0.fdr.1
- Update to 0.88

* Sun Jul 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.87-0.fdr.1
- Update to 0.87
- Require perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

* Mon Jun 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.86-0.fdr.1
- Update to 0.86

* Sat Jun 19 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.85-0.fdr.1
- Update to 0.85
- Bring up to date with current fedora.us Perl spec template

* Mon Feb  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.83-0.fdr.4
- Reduce directory ownership bloat

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.83-0.fdr.3
- Install into vendor dirs
- Specfile cleanup

* Sun Jul  6 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.83-0.fdr.2
- Regenerate %%install section with cpanflute2, omit spurious *.pl

* Wed May  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.83-0.fdr.1
- Update to 0.83 and to current Fedora guidelines

* Sun Mar  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.82-1.fedora.1
- First Fedora release
