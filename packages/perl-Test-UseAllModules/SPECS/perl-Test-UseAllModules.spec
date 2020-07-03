Name:           perl-Test-UseAllModules
Version:        0.17
Release:        17%{?dist}
Summary:        Do use_ok() for all the MANIFESTed modules
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-UseAllModules
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-UseAllModules-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(strict)
# perl(Test::Builder) needed for lib/Test/UseAllModules.pm:52:
# Test::More->builder->has_plan;
BuildRequires:  perl(Test::Builder) >= 0.30
BuildRequires:  perl(Test::More) >= 0.60
BuildRequires:  perl(warnings)
# Tests only:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.18
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Dependencies:
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Test::Builder) >= 0.30
Requires:       perl(Test::More) >= 0.60

# Remove underspecifies dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Test::More\\)

%description
I'm sick of writing 00_load.t (or something like that) that will do use_ok()
for every module I write. I'm sicker of updating 00_load.t when I add
another file to the distribution. This module reads MANIFEST to find modules
to be tested and does use_ok() for each of them. Now all you have to do is
update MANIFEST. You don't have to modify the test any more (hopefully).

%prep
%setup -q -n Test-UseAllModules-%{version}

# Fix line endings without changing timestamps
for F in Changes README; do
    tr -d '\r' <"$F" >"$F.unix"
    touch -r "$F"{,.unix}
    mv "${F}"{.unix,}
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::UseAllModules.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep  4 2019 Paul Howarth <paul@city-fan.org> - 0.17-15
- Spec tidy-up
  - Use author-independent source URL
  - Explicitly specify more build requirements
  - Simplify find command using -delete
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-2
- Perl 5.22 rebuild

* Fri Nov 14 2014 Petr Pisar <ppisar@redhat.com> - 0.17-1
- 0.17 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.20 rebuild

* Wed Jul 16 2014 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.14-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.13-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Petr Pisar <ppisar@redhat.com> 0.13-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr code
- Recode documentation to UNIX end-of-lines
