# Declare the CPAN name of the module
%define mod_basename CAD-Format-STL

Name:           perl-%{mod_basename}
Version:        0.2.1
Release:        22%{?dist}
Summary:        Read and Write STL (STereo Lithography) format files 
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{mod_basename}
Source:         https://cpan.metacpan.org/modules/by-module/CAD/%{mod_basename}-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Classy) >= 0.1.3
BuildRequires:  perl(Module::Build) >= 0.35
# These are needed for "Build test"
BuildRequires:  perl(bytes)
BuildRequires:  perl(Test::More)
Requires:       perl(bytes)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Class::Accessor::Classy) >= 0.1.3
# RPM's auto require for perl(Class::Accessor::Classy) fails, handle manually
%define __requires_exclude ^perl\\(Class::Accessor::Classy\\)$

%description
The CAD::Format::STL perl module provides object-oriented methods to read
and write files in STL (STereo Lithography) format. Support is provided
for both the ASCII and binary versions of the STL format.

%prep
%setup -q -n %{mod_basename}-v%{version}

%build
# Using Module::Build since a Build.PL is present
perl Build.PL installdirs=vendor
./Build

%install
%if 0%{?rhel} && 0%{?rhel} < 6
rm -rf %{buildroot}
%endif
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc files Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-22
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-19
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-16
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-13
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-11
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-8
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 John C. Peterson <jcp@eskimo.com> 0.2.1-5
- Moved def of __requires_exclude macro to just before description section
- Replaced the __perl macro with just perl in the expansion of MODULE_COMPAT_
- Package approved and should be ready to build for distribution.

* Wed Oct 16 2013 John C. Peterson <jcp@eskimo.com> 0.2.1-4
- Various fixes that were required or suggested by the package reviewer:
  Added the package's version number build requirement for perl(Module::Build)
  Added filter rule for rpm's auto require of perl(Class::Accessor::Classy)
  Added perl(bytes) to both the build and runtime requirements
  Removed the redundant defattr macro from the files section
  Replaced the __perl macro with just perl in the build section

* Tue Aug 13 2013 John C. Peterson <jcp@eskimo.com> 0.2.1-3
- Some cosmetic tweaks to the macros that check for the specific case of RHEL.

* Mon Aug 12 2013 John C. Peterson <jcp@eskimo.com> 0.2.1-2
- Some corrections to the macros that check for the specific case of RHEL.
- Eliminated find command in the install section as suggested by the reviewer.

* Mon Aug 12 2013 John C. Peterson <jcp@eskimo.com> 0.2.1-1
- Some minor cosmetic fixes to improve readability and to pacify rpmlint.

* Tue Jun 18 2013 John C. Peterson <jcp@eskimo.com> 0.2.1-1
- Baseline specfile autogenerated by cpanspec 1.78.

