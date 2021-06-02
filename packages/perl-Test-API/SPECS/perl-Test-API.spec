Name:		perl-Test-API
Version:	0.010
Release:	6%{?dist}
Summary:	Test a list of subroutines provided by a module
License:	ASL 2.0
URL:		https://metacpan.org/release/Test-API
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-API-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::Builder::Module) >= 0.86
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Builder::Tester) >= 1.18
BuildRequires:	perl(Test::More)
# Optional Test Requirements (not available in EPEL-6)
%if "%{?rhel}" != "6"
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.120900
%endif
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This simple test module checks the subroutines provided by a module. This is
useful for confirming a planned API in testing and ensuring that other
functions aren't unintentionally included via import.

%prep
%setup -q -n Test-API-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::API.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-2
- Perl 5.28 rebuild

* Mon Feb 19 2018 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Revised internals for constants/subrefs in the stash (a breaking change
    planned for Perl 5.28)
- Test::Builder::Module dependency now detected correctly everywhere

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-2
- Perl 5.26 rebuild

* Tue Apr  4 2017 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Fixed tests for perls without '.' in @INC
- Simplify find command using -delete
- Use %%license where possible

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Common methods treated as private (e.g. AUTOLOAD, BUILD) are ignored

* Mon Mar 17 2014 Paul Howarth <paul@city-fan.org> - 0.004-2
- Sanitize for Fedora submission

* Fri Mar 14 2014 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004
  - class_api_ok function tests methods that may be provided the module
    tested or a superclass
  - Dropped dependencies on superclass and Devel::Symdump

* Thu Mar 13 2014 Paul Howarth <paul@city-fan.org> - 0.003-1
- Initial RPM version
