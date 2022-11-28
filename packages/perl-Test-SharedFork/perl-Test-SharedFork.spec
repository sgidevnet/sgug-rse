Name:           perl-Test-SharedFork
Summary:        Fork test
Version:        0.35
Release:        13%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-SharedFork-%{version}.tar.gz
URL:            https://metacpan.org/release/Test-SharedFork

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder) >= 0.32
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Test::SharedFork is utility module for Test::Builder. It manages testing
by keeping the test count consistent between parent and child processes.

%prep
%setup -q -n Test-SharedFork-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-12
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.35-2
- Modernize spec.

* Sat Jan 02 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.35-1
- Upstream update.

* Wed Oct 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.34-1
- Upstream update.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.33-1
- Upstream update.

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-2
- Perl 5.22 rebuild

* Fri May 01 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.31-1
- Upstream update.
- Add %%license.
- Cleanup BRs.

* Mon Sep 22 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.29-1
- Upstream update.
- Reflect upstream URL having changed.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-2
- Perl 5.20 rebuild

* Mon Jul 07 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.28-1
- Upstream update.

* Mon Jun 30 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.26-1
- Upstream update.
- Reflect BR-changes.
- Reflect upstream having switched to ExtUtils::MakeMaker.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.24-1
- Upstream update.

* Tue Mar 25 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-1
- Upstream update.
- Extend BR:s.

* Thu Mar 13 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.22-1
- Upstream update.
- Remove Obsoletes/Provides perl-Test-SharedFork-tests.
- Reflect upstream having switched to Module::Build.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.21-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.21-1
- Upstream update.
- Modernize spec.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.20-2
- Perl 5.16 rebuild

* Tue Feb 14 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.20-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.19-1
- Upstream update.

* Thu Oct 13 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-1
- Upstream update.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-3
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-2
- Perl 5.14 mass rebuild

* Fri Feb 18 2011 Ralf Corsepius <corsepiu@fedoraproject.org> - 0.16-1
- Update to 0.16.
- Abandon perl-Test-SharedFork-tests.
- Spec file overhaul.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-3
- re-add macros. -tests sub-package was missing during update

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Dec 22 2010 Ralf Corsepius <corsepiu@fedoraproject.org> - 0.15-1
- Update to 0.15.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-2
- Mass rebuild with perl-5.12.0

* Sat Mar 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11-1
- specfile by Fedora::App::MaintainerTools 0.006


