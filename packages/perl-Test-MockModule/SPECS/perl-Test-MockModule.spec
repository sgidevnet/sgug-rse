# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Test_MockModule_enables_optional_test
%else
%bcond_with perl_Test_MockModule_enables_optional_test
%endif

Name:           perl-Test-MockModule
Version:        0.173.0
Release:        2%{?dist}
Summary:        Override subroutines in a module for unit testing
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-MockModule
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-MockModule-v%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SUPER) >= 1.20
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
%if %{with perl_Test_MockModule_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Test::MockModule lets you temporarily redefine subroutines in other packages
for the purposes of unit testing.

A Test::MockModule object is set up to mock subroutines for a given module. The
object remembers the original subroutine so it can easily be restored. This
happens automatically when all MockModule objects for the given module go out
of scope, or when you unmock() the subroutine.

%prep
%setup -q -n Test-MockModule-v%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::MockModule.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.173.0-2
- Perl 5.32 rebuild

* Sun Jun 14 2020 Paul Howarth <paul@city-fan.org> - 0.173.0-1
- Update to 0.173.0

* Wed Feb 19 2020 Tom Callaway <spot@fedoraproject.org> - 0.172.0-1
- Update to 0.172.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.171.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Paul Howarth <paul@city-fan.org> - 0.171.0-1
- Update to 0.171.0

* Tue Oct  8 2019 Paul Howarth <paul@city-fan.org> - 0.170.0-5
- Spec tidy-up
  - Use author-independent source URL
  - Enhance %%description
  - Fix permissions verbosely
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.170.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.170.0-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.170.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep  5 2018 Tom Callaway <spot@fedoraproject.org> - 0.170.0-1
- update to 0.170.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.28 rebuild

* Mon May 14 2018 Tom Callaway <spot@fedoraproject.org> - 0.15-1
- update to 0.15

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Petr Pisar <ppisar@redhat.com> - 0.13-2
- Remove unused CGI dependency

* Wed Oct 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-1
- 0.13 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Tom Callaway <spot@fedoraproject.org> - 0.12-1
- update to 0.12

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Tom Callaway <spot@fedoraproject.org> - 0.11-1
- update to 0.11

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-2
- Perl 5.22 rebuild

* Tue Jun  2 2015 Tom Callaway <spot@fedoraproject.org> - 0.10-1
- update to 0.10

* Fri Mar 27 2015 Tom Callaway <spot@fedoraproject.org> - 0.09-1
- update to 0.09

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-22
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.05-19
- Perl 5.18 rebuild

* Sat Feb 23 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-19
- Add BR: perl(ExtUtils::MakeMaker) (Fix FTBFS #914317).
- Modernize spec.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.05-16
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.05-14
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-12
- Add BR: perl(CGI) (Fix FTBFS: BZ 661082).

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-11
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.05-10
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-7
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.05-6
- rebuild for new perl

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.05-5
- license tag fix

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.05-4
- bump for fc6

* Wed Jul 27 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.05-3
- add missing BuildRequires

* Fri Jul  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.05-2
- cleanups

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.05-1
- Initial package for Fedora Extras
