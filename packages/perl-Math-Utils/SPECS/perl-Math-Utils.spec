Name:           perl-Math-Utils
Version:        1.14
Release:        2%{?dist}
Summary:        Useful mathematical functions not in Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Math-Utils
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGAMBLE/Math-Utils-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
# Tests
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Test::More)
# Optional tests
# Test::CheckManifest not used
BuildRequires:  perl(Test::Pod) >= 1.22
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Math::Utils contains implementations of commonly used mathematical
functions and operations that are not part of standard Perl.

%prep
%setup -q -n Math-Utils-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-2
- Perl 5.32 rebuild

* Tue Apr 28 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-1
- 1.14 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-1
- 1.13 bump

* Tue Aug 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-1
- 1.12 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-1
- 1.11 bump; Change licence from Artistic 2.0 to GPL+ or Artistic

* Thu Aug 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-1
- Initial release
