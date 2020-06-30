Name:           perl-Lexical-Var
Version:        0.009
Release:        23%{?dist}
Summary:        Static variables without name space pollution
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Lexical-Var
Source0:        https://cpan.metacpan.org/modules/by-module/Lexical/Lexical-Var-%{version}.tar.gz
# Update code to work with Perl 5.21.x (CPAN RT#101058)
Patch0:         Lexical-Var-0.009-Fix-RT-101058.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-Time
BuildRequires:  perl(Lexical::SealRequireHints) >= 0.006
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Conflicts:      perl(B::Hooks::OP::Check) < 0.19

%{?perl_default_filter}

%description
This module implements lexical scoping of static variables and subroutines.
Although it can be used directly, it is mainly intended to be
infrastructure for modules that manage name spaces.

%prep
%setup -q -n Lexical-Var-%{version}
%patch0 -p1

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} -c $RPM_BUILD_ROOT

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Lexical*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-23
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-20
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-17
- Perl 5.28 rebuild

* Thu Mar  1 2018 Paul Howarth <paul@city-fan.org> - 0.009-16
- Arch-specific package using Module::Build needs to use ExtUtils::CBuilder
  (https://bugzilla.redhat.com/show_bug.cgi?id=1547165#c7)
- Drop explicit gcc build-require as EU::CB is effectively our compiler here
- Add build-require coreutils for %%{_fixperms}
- Simplify find command using -empty

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-15
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-6
- Perl 5.22 rebuild

* Mon May 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-5
- Fix CPAN RT#101058

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-1
- 0.009 bump

* Mon Aug 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-1
- 0.008 bump
- Modernize spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.007-5
- Perl 5.18 rebuild
- Perl 5.18 compatibility (CPAN RT#80309)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.007-2
- Perl 5.16 rebuild

* Tue May 22 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.007-1
- Specfile autogenerated by cpanspec 1.78.
