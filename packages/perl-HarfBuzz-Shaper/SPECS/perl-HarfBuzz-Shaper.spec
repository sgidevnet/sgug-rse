# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName HarfBuzz-Shaper

Name: perl-%{FullName}
Summary: Access to a small subset of the native HarfBuzz library
License: GPL+ or Artistic
Version: 0.023
Release: 6%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

BuildRequires: coreutils findutils gcc make perl-devel
BuildRequires: harfbuzz-devel >= 1.7.7
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Devel::CheckLib)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(charnames)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
HarfBuzz::Shaper is a perl module that provides access to a small
subset of the native HarfBuzz library.

The subset is suitable for typesetting programs that need to deal with
complex languages like Devanagari.

This module is intended to be used with module L<Text::Layout>.

%prep
%setup -q -n %{FullName}-%{version}

# Make sure the included sources for harfbuzz are not used.
rm -fr ./hb_src
# Same for Devel::CheckLib.
rm -fr ./inc
# And adjust the MANIFEST.
perl -i -ne 'print $_ unless m{^(hb_src|inc)/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test VERBOSE=1

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HarfBuzz/Shaper.pm
%{_mandir}/man3/*

%changelog
* Mon Jul 13 2020 Johan Vromans <jvromans@squirrel.nl> - 0.023-6
- Upgrade to new upstream version.

* Fri Jun 05 2020 Johan Vromans <jvromans@squirrel.nl> - 0.022-5
- Upgrade to new upstream version.

* Tue Mar 03 2020 Johan Vromans <jvromans@squirrel.nl> - 0.021-4
- Upgrade to new upstream version.

* Wed Feb 26 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.4-3
- Incorporate reviewer feedback.

* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.4-2
- Incorporate reviewer feedback.

* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.4-1
- Initial Fedora package.
