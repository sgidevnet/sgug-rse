Name:           perl-Class-MethodMaker
Version:        2.24
Release:        16%{?dist}
Summary:        Perl module for creating generic object-oriented methods

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Class-MethodMaker
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/class-methodmaker/Class-MethodMaker-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(AutoLoader) >= 5.57
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Required by the tests
BuildRequires:  perl(B::Deparse) >= 0.59
BuildRequires:  perl(Cwd) >= 2.01
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Env)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Fatal) >= 1.02
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(File::Compare) >= 1.1002
BuildRequires:  perl(File::Path) >= 1.04.01
BuildRequires:  perl(File::Spec) >= 0.6
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin) >= 1.42
BuildRequires:  perl(IO::File) >= 1.08
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX) >= 1.03
BuildRequires:  perl(Test) >= 1.12.2
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(Tie::StdArray)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Tie::StdScalar)
BuildRequires:  perl(vars)

Requires:  perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:  perl(B::Deparse)
Requires:  perl(Data::Dumper)

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(AutoLoader\\)$

%description
Class::MethodMaker solves the problem of having to continually write accessor
methods for your objects that perform standard tasks.

%prep
%setup -q -n Class-MethodMaker-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README TODO
%{perl_vendorarch}/Class/
%{perl_vendorarch}/auto/Class/
%{_mandir}/man3/Class::MethodMaker.3*
%{_mandir}/man3/Class::MethodMaker::Constants.3*
%{_mandir}/man3/Class::MethodMaker::Engine.3*
%{_mandir}/man3/Class::MethodMaker::OptExt.3*
%{_mandir}/man3/Class::MethodMaker::V1Compat.3*
%{_mandir}/man3/Class::MethodMaker::array.3*
%{_mandir}/man3/Class::MethodMaker::hash.3*
%{_mandir}/man3/Class::MethodMaker::scalar.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-6
- Perl 5.24 rebuild

* Thu Apr 21 2016 Paul Howarth <paul@city-fan.org> - 2.24-5
- Fix FTBFS due to missing buildreq perl-devel
- Simplify find commands using -delete
- Don't use macros for commands
- Drop redundant Group: tag

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Petr Pisar <ppisar@redhat.com> - 2.24-1
- 2.24 bump

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-2
- Perl 5.22 rebuild

* Mon Jan 26 2015 Paul Howarth <paul@city-fan.org> - 2.22-1
- Update to 2.22
  - Use File::Temp::tmpnam as needed in Android
- Make %%files list more explicit

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.21-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 21 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.21-1
- Upstream update.

* Thu Feb 13 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.20-1
- Upstream update.
- Minor spec cleanup.

* Thu Dec 26 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.19-1
- Upstream update.
- Fix up Source0:-URL.
- Rework spec.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.18-8
- Perl 5.18 rebuild
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.18-5
- Perl 5.16 rebuild
- Specify all dependencies

* Sun Jan 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.18-4
- Add %%{perl_default_filter}.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.18-2
- Perl mass rebuild

* Sun Apr 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.18-1
- Upstream update.

* Mon Mar 28 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.17-1
- Upstream update.
- Spec file cleanup.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.16-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 18 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.16-2
- Rebuild with perl-5.12.0.

* Tue May 18 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.16-1
- Upstream update.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.15-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.15-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.15-1
- Upstream update.
- Build in subdir to work-around rpm breaking the testsuite.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.13-1
- Upstream update.

* Fri Sep  5 2008 Daniel P. Berrange <berrange@redhat.com> - 2.12-1
- Update to new release for rhbz #461285

* Fri Jul 18 2008 Ralf Corsépius <rc040203@freenet.de> - 2.11-1
- Upstream update.

* Fri Jul 18 2008 Ralf Corsépius <rc040203@freenet.de> - 2.10-4
- Remove %%clean ||: (BZ 449442, FTBFS).
- Use %%version in Source0-URL.
- Don't skip 0-signature.t.
- Misc. minor spec-file overhaul.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.10-3
- Rebuild for perl 5.10 (again)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.10-2
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.10-1
- fix compile bug by going to 2.10 (CPAN says it is unauthorized, 
  but the copyright holder says it is ok)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.08-5
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.08-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Feb 17 2006 Dennis Gregorovic <dgregor@redhat.com> - 2.08-4
- Rebuild for FC6

* Fri Feb 17 2006 Dennis Gregorovic <dgregor@redhat.com> - 2.08-3
- Appended the dist tag to the Release number

* Fri Feb 17 2006 Dennis Gregorovic <dgregor@redhat.com> - 2.08-2
- Rebuild for FC5 (perl 5.8.8)

* Sat Feb 11 2006 Dennis Gregorovic <dgregor@redhat.com> - 2.08-1
- Rebuilt for version 2.08 of source

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.06-3
- rebuild on all arches

* Mon Mar 21 2005 Dennis Gregorovic <dgregor@redhat.com> - 2.06-2
- Rebuilt for version 2.06 of source

* Thu Feb 24 2005 Dennis Gregorovic <dgregor@redhat.com> - 2.05-2
- Incorporated feedback from Jose Pedro Oliveira. (#149637)

* Fri Feb  4 2005 Dennis Gregorovic <dgregor@redhat.com> - 2.05-1
- First build.
