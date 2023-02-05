Name:          perl-Verilog-Perl
Version:       3.470
Release:       1%{?dist}
Summary:       Verilog parsing routines
License:       LGPLv3 or Artistic 2.0
URL:           http://www.veripool.org/wiki/verilog-perl
Source0:       https://cpan.metacpan.org/authors/id/W/WS/WSNYDER/Verilog-Perl-%{version}.tar.gz

BuildRequires: bison
BuildRequires: gcc-c++
BuildRequires: gdbm-devel
BuildRequires: findutils
BuildRequires: flex
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Copy)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::File)
BuildRequires: perl(Pod::Usage) >= 1.34
BuildRequires: perl(strict)
BuildRequires: perl(vars)
# Run-time
BuildRequires: perl(base)
BuildRequires: perl(Cwd)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
# Tests
BuildRequires: perl(lib)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(warnings)
# Optional tests
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Pod) >= 1.00

Requires:      perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

Provides:      perl-Verilog     = %{version}-%{release}
Obsoletes:     perl-Verilog     < 3.213-2

# Filtering Requires: and Provides
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((imp_test_pkg|mypackage)\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((imp_test_pkg|mypackage)\\)

%description
This package provides functions to support writing utilities
that use the Verilog language.

%prep
%setup -q -n Verilog-Perl-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}

%check
# Free Electronic Lab : Package Self Test
make test

%files
%license COPYING
%doc Changes README verilog/
%dir %{perl_vendorarch}/Verilog/
%dir %{perl_vendorarch}/auto/Verilog/
%{_bindir}/*
%{perl_vendorarch}/Verilog/*
%{perl_vendorarch}/auto/Verilog/*
%{_mandir}/man?/*


%changelog
* Tue Jan 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.470-1
- 3.470 bump

* Fri Sep 13 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.468-1
- 3.468 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.466-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.466-2
- Perl 5.30 rebuild

* Mon May 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.466-1
- 3.466 bump

* Fri May 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.464-1
- 3.464 bump

* Wed Apr 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.462-1
- 3.462 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.460-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.460-1
- 3.460 bump

* Fri Jan 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.458-1
- 3.458 bump

* Mon Oct 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.456-1
- 3.456 bump

* Wed Oct 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.454-1
- 3.454 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.452-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.452-2
- Perl 5.28 rebuild

* Fri Apr 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.452-1
- 3.452 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.448-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.448-1
- 3.448 bump

* Thu Nov 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.446-1
- 3.446 bump

* Fri Sep 22 2017 Petr Pisar <ppisar@redhat.com> - 3.444-1
- 3.444 bump

* Wed Sep 20 2017 Petr Pisar <ppisar@redhat.com> - 3.442-1
- 3.442 bump

* Fri Sep 01 2017 Petr Pisar <ppisar@redhat.com> - 3.440-1
- 3.440 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.430-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.430-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 3.430-1
- 3.430 bump

* Mon Jun 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.426-1
- 3.426 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.423-2
- Perl 5.26 rebuild

* Thu Apr 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.423-1
- 3.423 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.422-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.422-1
- 3.422 bump

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.420-1
- 3.420 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.418-2
- Perl 5.24 rebuild

* Wed Feb 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.418-1
- 3.418 bump

* Thu Oct 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.416-1
- 3.416 bump
- Modernize spec

* Tue Sep 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.414-1
- 3.414 bump

* Tue Jun 23 2015 Petr Pisar <ppisar@redhat.com> - 3.412-1
- 3.412 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.408-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.408-3
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.408-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 24 2015 Paul Howarth <paul@city-fan.org> - 3.408-1
- 3.408 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.401-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.401-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.401-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.401-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Petr Pisar <ppisar@redhat.com> - 3.401-1
- 3.401 bump

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 3.314-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.314-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.314-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 3.314-2
- Perl 5.16 rebuild
- Specify all dependencies

* Tue Feb 28 2012 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.314-1
- New upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.304-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.304-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 06 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.304-1
- New upstream release

* Sat Sep 25 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.303-1
- New upstream release

* Sat Aug 28 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.302-1
- New upstream release

* Sat Aug 14 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.301-1
- New upstream release

* Sun Jul 11 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.300-1.beta1
- New upstream beta release which supports 99% of the SystemVerilog 2009 standard

* Tue Jun 29 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.251-1
- New upstream release
- Shakthimaan: fix for rpmlint warning

* Sun Jun 27 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.250-1
- New upstream release and now supporting EL-6

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.223-2
- Mass rebuild with perl-5.12.0

* Mon Dec 21 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.223-1
- New upstream release

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.222-2
- rebuild against perl 5.10.1

* Wed Nov 25 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.222-1
- New upstream release

* Tue Nov 24 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.221-1
- New upstream release

* Fri Sep 11 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.213-2
- Pacakge review #522777 Comment2

* Fri Sep 11 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.213-1
- new upstream package

* Sat Sep 05 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.212-2
- prepared for second package review
- Bug 488670 -  Package should be renamed into perl-Verilog-Perl

* Mon Jul 20 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.212-1
- upstream v3.212

* Thu Jun 18 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.211-1
- upstream v3.211

* Thu May 21 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.210-1
- upstream v3.210

* Wed Mar 04 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.120-1
- upstream v3.120

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.110-1
- upstream v3.110

* Sat Jan 03 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.100-1
- upstream v3.100
- removed patch for rawhide's bison

* Sat Dec 20 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.045-1
- upstream v3.045
- updated to the recommendations of #476386-c3

* Sun Dec 14 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.044-2
- Added Bison and flex as BR
- fixed the arch build

* Sat Dec 06 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.044-1
- Initial package for fedora
