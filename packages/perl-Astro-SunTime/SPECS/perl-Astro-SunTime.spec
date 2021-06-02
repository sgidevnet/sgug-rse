Name:      perl-Astro-SunTime
Summary:   Calculates sun rise/set times 
Version:   0.06
Release:   7%{?dist}
License:   GPLv3
URL:       https://metacpan.org/release/Astro-SunTime
Source:    https://cpan.metacpan.org/authors/id/R/RO/ROBF/Astro-SunTime-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: findutils

# Needed during build for the perl test
BuildRequires: perl(Test)
BuildRequires: perl(POSIX)
BuildRequires: perl(strict)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(vars)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:  perl(Time::ParseDate)

%description
Astro::SunTime Perl module provides a function interface to calculate sun
rise/set times.

%prep
%autosetup -n Astro-SunTime-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}
# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -delete

%check
%make_build test

%files
%license LICENSE
%doc Changes README.md
%dir %{perl_vendorlib}/Astro
%{perl_vendorlib}/Astro/SunTime.pm

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.06-1
- Bump version to 0.06
- Add license file, since it is now included, filename of the README changed

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.05-2
- Add perl(Time::ParseDate) requires. It is not autodetected.

* Fri Jan 20 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.05-1
- Update to release 0.05
- Added Perl(Test) buildrequries to run new tests in 0.05 release

* Tue Jan 03 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-5
- Additional feedback from bugzilla 1409869

* Tue Jan 03 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-4
- bugzilla 1409869 feedback applies to this package too

* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-3
- Add perl-generators buildrequires 
- move make test to %%check

* Sun Jan 01 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-2
- Update spec file to modern Fedora packaging guidelines 

* Fri Aug 23 2013 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-1
- Initial build using cpan2rpm.
