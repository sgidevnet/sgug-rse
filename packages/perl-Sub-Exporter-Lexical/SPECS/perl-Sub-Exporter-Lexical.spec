Name:           perl-Sub-Exporter-Lexical
Version:        0.092292
Release:        10%{?dist}
Summary:        Export lexically-available subs with Sub::Exporter
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sub-Exporter-Lexical
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-Lexical-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-interpreter >= 1:v5.12.0
BuildRequires:  perl-generators

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Lexical::Sub)
BuildRequires:  perl(Sub::Exporter) >= 0.978
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Sub::Exporter::Lexical provides an alternate installer for Sub::Exporter.
Installers are documented in Sub::Exporter's documentation; all you need to
know is that by using Sub::Exporter::Lexical's installer, you can import
routines into a lexical scope that will be cleaned up when that scope ends.

%prep
%setup -q -n Sub-Exporter-Lexical-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT

# Bogusly installed script
rm $RPM_BUILD_ROOT%{perl_vendorlib}/Sub/Exporter/snippet.pl

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.092292-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.092292-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.092292-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.092292-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.092292-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.092292-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.092292-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.092292-3
- Perl 5.26 rebuild

* Wed Feb 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.092292-2
- Reflect feedback from package review.

* Fri Feb 03 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.092292-1
- Initial Fedora package.
