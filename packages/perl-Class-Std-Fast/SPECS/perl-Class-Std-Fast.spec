Name:           perl-Class-Std-Fast
Version:        0.0.8
Release:        14%{?dist}
Summary:        Faster but less secure replacement for Class::Std
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Class-Std-Fast
Source0:        https://cpan.metacpan.org/authors/id/A/AC/ACID/Class-Std-Fast-v%{version}.tar.gz
# Based on the statement in the README file:
# "This library is free software; you can redistribute it and/or modify
# it under the same terms as Perl itself."
Source1:        http://dev.perl.org/licenses/#/%{name}-Licensing.html

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Std)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(lib)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Class::Std)
Requires:       perl(Data::Dumper)


%description
Class::Std::Fast allows you to use the beautiful API of Class::Std in a faster
way than Class::Std does. You can get the object's identity via scalar-ifying 
our object. Getting the objects identity is still possible via the ident method.


%prep
%setup -q -n Class-Std-Fast-v%{version}
cp -a %{SOURCE1} Licensing.html

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT


%check
make test


%files
%license Licensing.html
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/man3/*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.8-14
- Perl 5.32 rebuild

* Mon Mar 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.8-13
- Specify all dependencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.8-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.8-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.8-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.0.8-2
- Remove duplicate perl-generators BR
- Update license URL

* Tue Jan 31 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> 0.0.8-1
- Initial RPM release.
