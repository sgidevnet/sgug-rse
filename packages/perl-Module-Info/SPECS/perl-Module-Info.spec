Name:           perl-Module-Info
Version:        0.37
Release:        14%{?dist}
Summary:        Information about Perl modules
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-Info
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-Info-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(B::Utils) >= 0.27
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec) >= 0.8
# XXX: BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Safe)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Cwd) >= 1.1.2
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(File::Spec) >= 0.8
# XXX: Requires:       perl(IPC::Open3)
Requires:       perl(Safe)
Requires:       perl(version)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

%description
Module::Info gives you information about Perl modules without actually loading
the module. It isn't actually specific to modules and should work on any perl
code.

%prep
%setup -q -n Module-Info-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Petr Šabata <contyk@redhat.com> - 0.37-1
- 0.37 bump
- Modernize the spec, dropping el5 support

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-6
- Perl 5.22 rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-5
- Fixed bundled B::Utils to build with Perl 5.22

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Paul Howarth <paul@city-fan.org> - 0.35-2
- Drop pointless in-place edit flag from perl filter invocation

* Sun Sep  8 2013 Paul Howarth <paul@city-fan.org> - 0.35-1
- Update to 0.35
  - Handle 'package NAME VERSION' syntax
  - Added repository and license info to metadata
  - Tweaked format of Changes (this file) to match CPAN::Changes::Spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.34-2
- Perl 5.18 rebuild

* Tue May 21 2013 Paul Howarth <paul@city-fan.org> - 0.34-1
- Update to 0.34
  - Replace Text::Soundex in tests with Class::Struct, since Text::Soundex will
    not be in core in Perl 5.19 and up
  - Replace ExtUtils::MY_Metafile with META_MERGE in Makefile.PL

* Sun Feb 10 2013 Paul Howarth <paul@city-fan.org> - 0.33-1
- Update to 0.33
  - Fix tests under Perl 5.6.2 when some core modules have been upgraded
- Add provides filter that works with rpm ≥ 4.10
- Simplify provides filter for rpm < 4.10
- BR: perl(Carp), perl(Cwd), perl(File::Spec), perl(lib) and
  perl(Text::Soundex)
- BR:/R: perl(Safe)
- BR: at least version 1.00 of perl(Test::Pod) and perl(Test::Pod::Coverage)
- Don't use macros for commands
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.32-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.32-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Steven Pritchard <steve@kspei.com> 0.32-1
- Update to 0.32.

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.31-9
- Rebuild to fix problems with vendorarch/lib (#661697)

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.31-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.31-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Steven Pritchard <steve@kspei.com> 0.31-4
- BR Test::Pod::Coverage.
- Filter B::Utils auto-provides.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.31-2
- rebuild for new perl

* Wed May 30 2007 Steven Pritchard <steve@kspei.com> 0.31-1
- Update to 0.31.

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.30-5
- Use fixperms macro instead of our own chmod incantation.

* Sun Sep 17 2006 Steven Pritchard <steve@kspei.com> 0.30-4
- Rebuild.

* Wed May 24 2006 Steven Pritchard <steve@kspei.com> 0.30-3
- Rebuild.

* Sat May 06 2006 Steven Pritchard <steve@kspei.com> 0.30-2
- Add BR: perl(Test::Pod) and perl(version).
- Add Requires: perl(version).

* Fri Apr 21 2006 Steven Pritchard <steve@kspei.com> 0.30-1
- Update to 0.30.
- Use perl macro.
- Drop extra find.

* Fri Mar 24 2006 Steven Pritchard <steve@kspei.com> 0.290-1
- Specfile autogenerated by cpanspec 1.64.
- Add bindir and man1 files.
