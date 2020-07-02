Name:           perl-Convert-Binary-C
Version:        0.79
Release:        2%{?dist}
Summary:        Binary data conversion using C types
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Convert-Binary-C
Source0:        https://cpan.metacpan.org/modules/by-module/Convert/Convert-Binary-C-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.10
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Pod) >= 0.95
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Thread)
BuildRequires:  perl(threads)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Convert::Binary::C is a preprocessor and parser for C type definitions. It
is highly configurable and supports arbitrarily complex data structures.
Its object-oriented interface has pack and unpack methods that act as
replacements for Perl's pack and unpack and allow to use C types instead of
a string representation of the data structure for conversion of binary data
from and to Perl's complex data structures.

%prep
%setup -q -n Convert-Binary-C-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Convert*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-2
- Perl 5.32 rebuild

* Tue May 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-1
- 0.79 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.78-8
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-2
- Perl 5.24 rebuild

* Thu Mar 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-1
- 0.78 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-1
- 0.77 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-11
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-10
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.76-6
- Perl 5.18 rebuild
- Fix POD syntax (CPAN RT#85264)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.76-3
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 0.76-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.74-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.74-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.74-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.74-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.74-1
- Update to latest upstream (0.74)
- Drop GCC 4.4 patch (fixed upstream)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.71-2
- Add patch to fix #elif directives for new GCC 4.4

* Wed Jun  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.71-1
- Update to latest upstream (0.71)

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.70-5
- rebuild for new perl (again)

* Sat Feb 23 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.70-4
- Bump release to fix koji problem that prevented tagging the previous
  (correct) build.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.70-3
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.70-2
- rebuild for new perl

* Sun Jan  6 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.70-1
- Update to latest upstream (0.70)

* Thu Aug 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.68-2
- License tag to GPL+ or Artistic as per new guidelines.

* Sat Aug 18 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.68-1
- Update to latest upstream

* Mon Apr 02 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-4
- Remove '%%{?_smp_mflags}', package does not support parallel make.

* Thu Mar 29 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-3
- Add BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)

* Tue Mar 27 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-2
- Add perl(ExtUtils::MakeMaker) BR.

* Fri Mar 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-1
- Specfile autogenerated by cpanspec 1.69.1.
