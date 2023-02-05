# Test::Warnings introduced in Fedora 18
%if 0%{?fedora} < 18 && 0%{?rhel} < 7
%global no_test_warnings 1
%else
%global no_test_warnings 0
%endif

Name:		perl-Exporter-Tiny
Version:	1.002001
Release:	4%{?dist}
Summary:	An exporter with the features of Sub::Exporter but only core dependencies
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Exporter-Tiny
Source0:	https://cpan.metacpan.org/modules/by-module/Exporter/Exporter-Tiny-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.47
# Optional Tests
BuildRequires:	perl(Test::Fatal)
%if ! %{no_test_warnings}
BuildRequires:	perl(Test::Warnings)
%endif
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Carp)

# Avoid doc-file dependency on perl(base)
%{?perl_default_filter}

%description
Exporter::Tiny supports many of Sub::Exporter's external-facing features
including renaming imported functions with the -as, -prefix and -suffix
options; explicit destinations with the into option; and alternative
installers with the installer option. But it's written in only about 40%%
as many lines of code and with zero non-core dependencies.

Its internal-facing interface is closer to Exporter.pm, with configuration
done through the @EXPORT, @EXPORT_OK and %%EXPORT_TAGS package variables.

Exporter::Tiny performs most of its internal duties (including resolution of
tag names to sub names, resolution of sub names to coderefs, and installation
of coderefs into the target package) as method calls, which means they can be
overridden to provide interesting behavior.

%prep
%setup -q -n Exporter-Tiny-%{version}

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
%license COPYRIGHT LICENSE
%else
%doc COPYRIGHT LICENSE
%endif
%doc Changes CREDITS examples/ README TODO
%{perl_vendorlib}/Exporter/
%{_mandir}/man3/Exporter::Tiny.3*
%{_mandir}/man3/Exporter::Tiny::Manual::Etc.3*
%{_mandir}/man3/Exporter::Tiny::Manual::Exporting.3*
%{_mandir}/man3/Exporter::Tiny::Manual::Importing.3*
%{_mandir}/man3/Exporter::Tiny::Manual::QuickStart.3*
%{_mandir}/man3/Exporter::Shiny.3*

%changelog
* Tue Oct 06 2020  HAL <notes2@gmx.de> - 1.002001-4
- compiles on Irix 6.5 with sgug-rse gcc 9.2. All tests pass.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.002001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.002001-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.002001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Paul Howarth <paul@city-fan.org> - 1.002001-1
- Update to 1.002001
  - Added support for generating and exporting non-code symbols such as $Foo,
    @Bar, and %%Baz
  - Improved test coverage, up from 88.78%% on coveralls.io to 96.74%%

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.000000-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.000000-2
- Perl 5.26 rebuild

* Mon May 22 2017 Paul Howarth <paul@city-fan.org> - 1.000000-1
- Update to 1.000000
  - Repackage as 1.000000
- All shipped files are now GPL+ or Artistic
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.044-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Paul Howarth <paul@city-fan.org> - 0.044-1
- Update to 0.044
  - Support { -as => CODE } to programmatically rename functions
  - Restructure documentation
- Simplify find command using -delete

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.042-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.042-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.042-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.042-3
- Perl 5.22 rebuild

* Fri Mar  6 2015 Paul Howarth <paul@city-fan.org> - 0.042-2
- Correct license tagging (#1199491)

* Thu Oct  9 2014 Paul Howarth <paul@city-fan.org> - 0.042-1
- Update to 0.042
  - Add an 'unimport' feature
  - Option validation needs to happen after expanding tags
  - Housekeeping on %%TRACKED

* Wed Sep 17 2014 Paul Howarth <paul@city-fan.org> - 0.040-1
- Update to 0.040
  - Document warning and error messages produced by Exporter::Tiny
  - Exporter::Tiny would previously cause B.pm to be loaded into memory any
    time it exported anything: it no longer does
  - No longer die when redefining locally defined subs
  - Warn when redefining any subs
- Use %%license where possible

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.038-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.038-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr  4 2014 Paul Howarth <paul@city-fan.org> - 0.038-1
- Update to 0.038
  - Added: Support Exporter.pm's import negation syntax qw( !foo )
  - Added: Support Exporter.pm's regexp import syntax qw( /foo/ )
  - Fix minor error in documentation of generators
  - Improved handling of hashrefs of options passed to tags, and hashrefs of
    options found within %%EXPORT_TAGS arrayrefs
  - Only attempt to merge hashes if we're sure they're both really hashes!

* Mon Mar 17 2014 Paul Howarth <paul@city-fan.org> - 0.036-2
- Sanitize for Fedora submission

* Thu Mar 13 2014 Paul Howarth <paul@city-fan.org> - 0.036-1
- Initial RPM version
