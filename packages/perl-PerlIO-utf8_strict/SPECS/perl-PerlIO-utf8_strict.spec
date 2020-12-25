Name:           perl-PerlIO-utf8_strict
Version:        0.008
Release:        1%{?dist}
Summary:        Fast and correct UTF-8 I/O
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/PerlIO-utf8_strict
Source0:        https://cpan.metacpan.org/modules/by-module/PerlIO/PerlIO-utf8_strict-%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a fast and correct UTF-8 PerlIO layer. Unlike perl''s
default :utf8 layer it checks the input for correctness.

%prep
%setup -q -n PerlIO-utf8_strict-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/PerlIO/
%{perl_vendorarch}/PerlIO/
%{_mandir}/man3/PerlIO::utf8_strict.3*

%changelog
* Fri Nov 27 2020 Daniel Hams <daniel.hams@gmail.com> - 0.008-1
- Bump to latest FC31 version

* Sat Sep 05 2020  HAL <notes2@gmx.de> - 
- compiles on Irix 6.5 with sgug-rse gcc 9.2, passing all tests.

* Sat Sep 19 2020 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Make unread by :crlf on top of :utf8_strict reliable
- Use author-independent source URL

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
