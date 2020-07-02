Name:           perl-ExtUtils-CChecker
Version:        0.10
Release:        15%{?dist}
Summary:        Configure-time utilities for using C headers, libraries, or OS features
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ExtUtils-CChecker
Source0:        https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-CChecker-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
# Tests:
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Optional Tests:
BuildRequires:  perl(Test::Pod) >= 1.00
# Dependencies:
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Module::Build)

%description
Often Perl modules are written to wrap functionality found in existing C
headers, libraries, or to use OS-specific features. It is useful in the
Build.PL or Makefile.PL file to check for the existence of these
requirements before attempting to actually build the module.

%prep
%setup -qn ExtUtils-CChecker-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/ExtUtils::CChecker.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-15
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct  4 2019 Paul Howarth <paul@city-fan.org> - 0.10-13
- Spec tidy-up
  - Use author-independent source URL
  - Specify all build dependencies
  - Fix permissions verbosely
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Christopher Meng <rpm@cicku.me> - 0.09-1
- Update to 0.09

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.08-4
- Perl 5.18 rebuild

* Wed Jun 05 2013 Petr Šabata <contyk@redhat.com> - 0.08-3
- Spec cleanup and dep list fixes

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 20 2012 Marcela Mašláňová <mmaslano@redhat.com> 0.08-1
- update to 0.08

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.04-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.04-1
- Update to 0.04

* Tue Jun 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.03-2
- rebuilt for perl 

* Mon Apr 19 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.03-1
- Specfile autogenerated by cpanspec 1.78.
