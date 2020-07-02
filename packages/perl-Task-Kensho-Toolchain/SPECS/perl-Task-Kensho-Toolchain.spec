Name:           perl-Task-Kensho-Toolchain
Version:        0.40
Release:        6%{?dist}
Summary:        Glimpse at an Enlightened Perl (basic toolchain)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Task-Kensho-Toolchain
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-Toolchain-%{version}.tar.gz
# Carton does not work in our distribution
Patch0:         Task-Kensho-Toolchain-0.39-Do-not-use-Carton.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# No run-time dependency is needed for tests.
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(App::cpanminus)
Requires:       perl(App::cpm)
Requires:       perl(App::FatPacker)
Requires:       perl(App::perlbrew)
# Do not use perl(Carton)
# Carton is not provided by Fedora. Carton does not work correctly, if the
# system uses perl installed by a vendor package with modules stripped from
# core as Fedora does.
Requires:       perl(CPAN::Mini)
Requires:       perl(local::lib)
Requires:       perl(Pinto)
Requires:       perl(version)

%{?perl_default_filter}

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
%setup -q -n Task-Kensho-Toolchain-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-2
- Perl 5.24 rebuild

* Mon May 16 2016 Petr Pisar <ppisar@redhat.com> - 0.39-1
- 0.39 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-1
- 0.38 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-1
- 0.36 bump

* Mon Feb 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-1
- 0.35 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.28-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
- Modernize spec file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.28-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.28-4
- Perl mass rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.28-3
- Perl mass rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.28-2
- Perl mass rebuild

* Wed May 11 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.28-1
- update to 0.28
- remove deffattr

* Tue Mar 22 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.27-1
- Specfile autogenerated by cpanspec 1.79.
