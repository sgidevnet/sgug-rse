Name:		perl-Data-Binary
Version:	0.01
Release:	6%{?dist}
Summary:	Simple detection of binary versus text in strings
License:	Artistic 2.0
URL:		https://metacpan.org/release/Data-Binary
Source0:	https://cpan.metacpan.org/modules/by-module/Data/Data-Binary-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This simple module provides string equivalents to the -T / -B operators. Since
these only work on file names and file handles, this module provides the same
functions but on strings.

Note that the actual implementation is currently different, basically because
the -T / -B functions are in C/XS, and this module is written in pure Perl. For
now, anyway.

%prep
%setup -q -n Data-Binary-%{version}

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
%doc changes.txt README readme.txt
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Binary.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Paul Howarth <paul@city-fan.org> - 0.01-1
- Initial RPM version
