Name:           perl-File-Listing
Version:        6.07
Release:        1%{?dist}
Summary:        Parse directory listing
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-Listing
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Listing-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Date) >= 6.00
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Config)
# LWP::Simple not used
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(HTTP::Date) >= 6.00
Requires:       perl(Time::Local)
Conflicts:      perl-libwww-perl < 6

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(HTTP::Date\\)$
# Do not provide private modules
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(File::Listing::

%description
This module exports a single function called parse_dir(), which can be used
to parse directory listings.

%prep
%setup -q -n File-Listing-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Nov 27 2020  HAL <notes2@gmx.de> - 6.07-1
- Upgrade to latest from FC31

* Mon Sep 28 2020  HAL <notes2@gmx.de> - 6.04-22
- compiles on Irix 6.5 with sgug-rse gcc 9.2. All tests pass.

* Thu Oct 01 2020 Petr Pisar <ppisar@redhat.com> - 6.07-1
- 6.07 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
