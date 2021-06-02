Name:		perl-Params-Coerce
Version:	0.14
Release:	34%{?dist}
Summary:	Allows your classes to do coercion of parameters
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Params-Coerce
Source0:	https://cpan.metacpan.org/modules/by-module/Params/Params-Coerce-%{version}.tar.gz
Patch0:		https://rt.cpan.org/Ticket/Attachment/1727800/928987/Params-Coerce-0.14-Fix-building-on-Perl-without-.-in-INC.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
# Dependencies of bundled Module::Install
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(YAML)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Params::Util) >= 0.05
BuildRequires:	perl(Scalar::Util) >= 1.11
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
A big part of good API design is that we should be able to be flexible in
the ways that we take parameters. Params::Coerce attempts to encourage this,
by making it easier to take a variety of different arguments, while adding
negligible additional complexity to your code.

%prep
%setup -q -n Params-Coerce-%{version}

# Fix building on Perl without "." in @INC (CPAN RT#121730)
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test AUTOMATED_TESTING=1

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendorlib}/Params/
%{_mandir}/man3/Params::Coerce.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-33
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Paul Howarth <paul@city-fan.org> - 0.14-30
- Spec clean-up
  - Drop %%defattr, redundant since rpm 4.4
  - Drop buildroot cleaning in %%install section
  - Drop legacy Group: tag
  - Use %%license where possible
  - Simplify find command using -delete
  - Classify buildreqs by usage

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-29
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-26
- Perl 5.26 rebuild

* Wed May 17 2017 Petr Pisar <ppisar@redhat.com> - 0.14-25
- Fix building on Perl without "." in @INC (CPAN RT#121730)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-23
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-20
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-19
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.14-16
- Perl 5.18 rebuild

* Sun Feb 17 2013 Paul Howarth <paul@city-fan.org> - 0.14-15
- BR: perl(Cwd), perl(ExtUtils::MakeMaker), perl(File::Path) and
  perl(File::Spec), needed by bundled Module::Install

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.14-12
- Perl 5.16 rebuild

* Wed Feb 15 2012 Paul Howarth <paul@city-fan.org> - 0.14-11
- Spec clean-up:
  - Drop redundant perl and perl(ExtUtils::AutoInstall) buildreqs
  - BR: perl(Carp), perl(Scalar::Util) ≥ 1.11, perl(Test::More)
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Set AUTOMATED_TESTING=1 to enable Pod test
  - Use search.cpan.org source URL
  - Fix typo in %%description
  - Make %%files list more explicit
  - Don't use macros for commands
  - Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.14-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-7
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.14-5
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.14-2
- Rebuild for new perl

* Sun Oct 15 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.14-1
- Update to 0.14

* Thu Sep 07 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.13-2
- Add additional verbosity to %%description 

* Tue Sep 05 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.13-1
- Specfile autogenerated by cpanspec 1.69.1
