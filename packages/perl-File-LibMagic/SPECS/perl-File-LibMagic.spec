# Filter the Perl extension module
%{?perl_default_filter}

Name:		perl-File-LibMagic
Version:	1.22
Release:	2%{?dist}
Summary:	Perl wrapper/interface for libmagic
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/File-LibMagic
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-LibMagic-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	file-devel
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config::AutoConf)
# ExtUtils::CBuilder needed for Config::AutoConf to handle C language
# gcc needed on EL-8 because ExtUtils::CBuilder is missing dependency on it (#1547165)
BuildRequires:	perl(ExtUtils::CBuilder) %{?el8: gcc}
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Getopt::Long)
# Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.96
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
The File::LibMagic module is a simple perl interface to libmagic from the
file (4.x or 5.x) package.

%prep
%setup -q -n File-LibMagic-%{version}

%build
perl Makefile.PL \
  INSTALLDIRS=vendor \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1 \
  OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{perl_vendorarch}/File/
%{perl_vendorarch}/auto/File/
%{_mandir}/man3/File::LibMagic.3*
%{_mandir}/man3/File::LibMagic::Constants.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-2
- Perl 5.32 rebuild

* Sun Apr 26 2020 Paul Howarth <paul@city-fan.org> - 1.22-1
- Update to 1.22
  - Removed embedded copy of Config::AutoConf from distro.; instead, this is
    now a configure phase prereq. (GH#19)
  - Moved list of constants in libmagic that we care about to one module (GH#20)
  - Add support for setting libmagic processing limits (GH#15, GH#22)
  - Add two class methods that provide introspection on the available limit
    processing parameters, max_param_constant() and limit_key_is_supported()
    (GH#24)
  - Check all libmagic function return values properly and croak on failure
    (GH#21)
  - Switched to using GitHub issues
- Package CONTRIBUTING.md

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Paul Howarth <paul@city-fan.org> - 1.16-9
- Explicitly BR: gcc on EL-8 because ExtUtils::CBuilder is missing dependency
  on it (#1547165)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Paul Howarth <paul@city-fan.org> - 1.16-7
- Modernize spec
  - BR: file-devel rather than %%{_includedir}/magic.h (#1731720)
  - Use %%{make_build} and %%{make_install}
  - Drop now-redundant workaround for CPAN RT#107081

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Paul Howarth <paul@city-fan.org> - 1.16-1
- 1.16 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-1
- 1.15 bump

* Mon Sep 14 2015 Petr Pisar <ppisar@redhat.com> - 1.13-1
- 1.13 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 09 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-1
- 1.00 bump
- Update source link
- Specify all dependencies

* Tue Aug 27 2013 Josh Kayse <jokajak@gmail.com> 0.99-1
- update to 0.99

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.96-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.96-7
- Perl 5.16 rebuild

* Mon Apr 23 2012 Paul Howarth <paul@city-fan.org> - 0.96-6
- Update test suite to work with file 5.10 (CPAN RT#75457)
- Don't need to link against libz (CPAN RT#56479)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.96-4
- Own vendor_perl/File dirs.
- Include Changes in docs.

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.96-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Robert Scheck <robert@fedoraproject.org> 0.96-1
- Upgrade to 0.96 and some spec file cleanup
- Replaced Test::Base by Test::More (thanks to Andreas Koenig)

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.91-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.91-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 22 2009 Robert Scheck <robert@fedoraproject.org> 0.91-1
- Upgrade to 0.91 and some spec file cleanup

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 28 2008 Josh Kayse <josh.kayse@gtri.gatech.edu> 0.88-0.f10
- update to 0.88

* Sat Mar 01 2008 Josh Kayse <josh.kayse@gtri.gatech.edu> 0.85-3
- add perl Require
- specify specific directories in files

* Fri Feb 29 2008 Josh Kayse <josh.kayse@gtri.gatech.edu> 0.85-2
- added patch to fix test cases

* Thu Feb 28 2008 Josh Kayse <josh.kayse@gtri.gatech.edu> 0.85-1
- update to 0.85

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.82-5mdk
- Fix previous mistake

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.82-4mdk
 - buildrequires fix

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.82-3mdk
- fix url
- fix buildrequires

* Sun Jun 19 2005 Olivier Thauvin <nanardon@mandriva.org> 0.82-2mdk
- patch0: add search ldflags
- BuildRequires libmagic-devel

* Wed Jun 15 2005 Olivier Thauvin <nanardon@mandriva.org> 0.82-1mdk
- First mandriva spec
