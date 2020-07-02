# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Config-Std

Summary:        Perl module to load and save configuration files in a standard format
Name:           perl-Config-Std
Version:        0.903
Release:        9%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/B/BR/BRICKER/%{pkgname}-%{version}.tar.gz
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Std)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests only
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  perl(TAP::Harness)
%else
BuildRequires:  perl(TAP::Harness) >= 3.31
%endif
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildArch:      noarch

%description
A perl module to load and save configuration files in a standard format.
The configuration language is deliberately simple and limited, and the
module works hard to preserve as much information (section order, comments
etc.) as possible when a configuration file is updated.

%prep
%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -delete
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%if 0%{?rhel} && 0%{?rhel} <= 7
make test HARNESS_OPTIONS=j1
%else
make test
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Config/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.903-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.903-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.903-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.903-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.903-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.903-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.903-3
- Perl 5.28 rebuild

* Mon Apr 02 2018 Robert Scheck <robert@fedoraproject.org> 0.903-2
- Changes to match Fedora Packaging Guidelines (#1562632 #c1/#c2)

* Sun Apr 01 2018 Robert Scheck <robert@fedoraproject.org> 0.903-1
- Upgrade to 0.903 (#1562632)
- Initial spec file for Fedora and Red Hat Enterprise Linux
