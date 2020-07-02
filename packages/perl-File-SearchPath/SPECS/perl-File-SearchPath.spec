Name:           perl-File-SearchPath
Version:        0.07
Release:        16%{?dist}
Summary:        Search for a file in an environment variable path
License:        GPLv2+
URL:            https://metacpan.org/release/File-SearchPath
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJENNESS/File-SearchPath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Env::Path)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Env::Path)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module provides the ability to search a path-like environment variable
for a file (that does not necessarily have to be an executable).

%prep
%setup -q -n File-SearchPath-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc ChangeLog README
%{perl_vendorlib}/File*
%{_mandir}/man3/File*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.22 rebuild

* Sat Apr 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.07-1
- Update to 0.07

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Kostas Georgiou <georgiou@opengamma.com> 0.06-2
- Review changes/fixes #1018862.

* Wed Oct 02 2013 Kostas Georgiou <georgiou@opengamma.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
