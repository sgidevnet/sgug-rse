# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName App-Packager

Name: perl-%{FullName}
Summary: Abstract interface to a number of common packagers
License: GPL+ or Artistic
Version: 1.430.1
Release: 4%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

Requires: perl(:VERSION) >= 5.10.1
Requires: perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
App::Packager provides an abstract interface to a number of common
packagers, trying to catch as much common behavior as possible.

The main purpose is to have uniform access to application specific
resources.

Supported packagers are PAR::Packer, Cava::Packager and unpackaged. In the
latter case, the packager functions are emulated via Cava::Packager which
provides fallback for unpackaged use.

%prep
%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.430.1-4
- Perl 5.32 rebuild

* Wed Feb 26 2020 Johan Vromans <jvromans@squirrel.nl> - 1.430.1-3
- Incorporate reviewer feedback.
* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 1.430.1-2
- Incorporate reviewer feedback.
* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 1.430.1-1
- Initial Fedora package.
