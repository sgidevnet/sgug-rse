Name:       perl-rpm-build-perl 
Version:    0.82
Release:    27%{?dist}
# README: GPLv2+
# perl.prov: LGPLv2+
# ConstOptree/ppport.h: GPL+ or Artistic
License:    GPLv2+ and (GPL+ or Artistic)
Summary:    Perl compiler back-end to extract Perl dependencies 
Url:        https://metacpan.org/release/rpm-build-perl
Source:     https://cpan.metacpan.org/authors/id/A/AT/ATOURBIN/rpm-build-perl-%{version}.tar.gz 
# Perl 5.18 compatibility, CPAN RT#85411
Patch0:     rpm-build-perl-0.82-Fix-non-deterministic-failures-on-newer-perls.patch
# Perl 5.22 compatibility, bug #1231258, CPAN RT#104885
Patch1:     rpm-build-perl-0.82-Adjust-to-perl-5.22.patch
# Perl 5.26 compatibility, CPAN RT#117350
Patch2:     rpm-build-perl-0.82-Port-to-OpSIBLING-like-macros-required-since-Perl-5..patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(version)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(encoding)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(Encode)
Requires:       perl(version)

%{?perl_default_filter}
# Do not export private modules
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(fake\\)

%description
B::PerlReq is a back-end module for the Perl compiler that extracts
dependencies from Perl source code, based on the internal compiled
structure that Perl itself creates after parsing a program. The output of
B::PerlReq is suitable for automatic dependency tracking (e.g. for RPM
packaging).

%package scripts
Summary:    Perl RPM prov/req scripts
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description scripts
The provides/requires scripts packaged along with perl-rpm-build-perl.

%prep
%setup -q -n rpm-build-perl-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl Makefile.PL NO_PACKLIST=1 INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README* Changes perl5-alt-rpm-macros macros.env
%{perl_vendorarch}/*
%{_mandir}/man3/*.3*

%files scripts
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-26
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-23
- Perl 5.28 rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.82-22
- Modernize spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-18
- Perl 5.26 rebuild

* Mon Jun 05 2017 Petr Pisar <ppisar@redhat.com> - 0.82-17
- Restore compatibility with Perl 5.26.0 (CPAN RT#117350)

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-16
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-14
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Petr Pisar <ppisar@redhat.com> - 0.82-12
- Other perl-5.22 fix for GV to IV optimization (bug #1231258)

* Wed Jun 17 2015 Petr Pisar <ppisar@redhat.com> - 0.82-11
- Make adjustments for perl-5.22 compatible with older perls (bug #1231258)

* Tue Jun 16 2015 Petr Pisar <ppisar@redhat.com> - 0.82-10
- Adjust to perl-5.22 (bug #1231258)

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-9
- Perl 5.22 rebuild

* Tue Nov 18 2014 Petr Pisar <ppisar@redhat.com> - 0.82-8
- Specify more dependencies (bug #1165197)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.82-3
- Perl 5.18 rebuild
- Perl 5.18 compatibility (CPAN RT#85411)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 01 2012 Petr Pisar <ppisar@redhat.com> - 0.82-1
- 0.82 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.80-2
- Perl 5.16 rebuild
- Specify all dependencies
- Adapt tests to perl 5.16 (RT #77778)

* Fri Jan 27 2012 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.74-1
- update to 0.74, clean spec, fix tests for 5.14.1

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.72-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.72-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.72-1
- Mass rebuild with perl-5.12.0 & update

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.6.8-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.6.8-1
- update for submission
- split scripts off into their own package

* Tue Nov 18 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.6.8-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)
