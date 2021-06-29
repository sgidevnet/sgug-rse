Name:		perl-URI-cpan
Version:	1.007
Release:	4%{?dist}
Summary:	URLs that refer to things on the CPAN
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/URI-cpan
Source0:	https://cpan.metacpan.org/modules/by-module/URI/URI-cpan-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(CPAN::DistnameInfo)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(URI::_generic)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(URI)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module is for handling URLs that refer to things on the CPAN.

%prep
%setup -q -n URI-cpan-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/URI/
%{_mandir}/man3/URI::cpan.3*
%{_mandir}/man3/URI::cpan::author.3*
%{_mandir}/man3/URI::cpan::dist.3*
%{_mandir}/man3/URI::cpan::distfile.3*
%{_mandir}/man3/URI::cpan::module.3*
%{_mandir}/man3/URI::cpan::package.3*

%changelog
* Tue Sep 15 2020 Paul Howarth <paul@city-fan.org> - 1.007-4
- Modernize spec using %%{make_install}

* Tue Sep 15 2020 Paul Howarth <paul@city-fan.org> - 1.007-3
- perl(URI) is a test requirement, not a module requirement (#1876259)

* Sun Sep  6 2020 Paul Howarth <paul@city-fan.org> - 1.007-2
- Sanitize for Fedora

* Sun Sep  6 2020 Paul Howarth <paul@city-fan.org> - 1.007-1
- Initial RPM version
