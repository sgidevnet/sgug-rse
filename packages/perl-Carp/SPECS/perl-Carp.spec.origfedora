Name:           perl-Carp
Version:        1.50
Release:        439%{?dist}
Summary:        Alternative warn and die for modules
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Carp
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Carp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
# IPC::Open3  >= 1.0103 in reality, but the provides is 2-digit number only
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Do not export private DB module stub
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)

%description
The Carp routines are useful in your own modules because they act like
die() or warn(), but with a message which is more likely to be useful to a
user of your module. In the case of cluck, confess, and longmess that
context is a summary of every call in the call-stack. For a shorter message
you can use carp or croak which report the error as being from where your
module was called. There is no guarantee that that is where the error was,
but it is a good educated guess.

%prep
%setup -q -n Carp-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.50-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.50-416
- Increase release to favour standalone package

* Wed May 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.50-1
- Upgrade to 1.50 as provided in perl-5.28.0

* Fri Apr 20 2018 Petr Pisar <ppisar@redhat.com> - 1.42-396
- Prevent from some stack-not-ref-counted crashes in Carp (RT#52610)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-393
- Perl 5.26 rebuild

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 1.42-1
- Upgrade to 1.42 as provided in perl-5.25.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-1
- 1.40 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> - 1.38-1
- 1.38 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-2
- Perl 5.22 rebuild

* Fri Mar 20 2015 Petr Pisar <ppisar@redhat.com> - 1.36-1
- 1.36 bump

* Mon Mar 16 2015 Petr Pisar <ppisar@redhat.com> - 1.35-1
- 1.35 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.33.01-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.33.01-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Petr Pisar <ppisar@redhat.com> - 1.33.01-1
- 1.3301 bump

* Wed Mar 26 2014 Petr Pisar <ppisar@redhat.com> - 1.33-1
- 1.33 bump

* Tue Sep 10 2013 Petr Pisar <ppisar@redhat.com> - 1.32-1
- 1.32 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-245
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.26-244
- Link minimal build-root packages against libperl.so explicitly

* Tue Apr 30 2013 Petr Pisar <ppisar@redhat.com> - 1.26-243
- Increase release number to supersede perl sub-package (bug #957931)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-241
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.26-240
- Bump release to override sub-package from perl.spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.26-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 1.26-1
- 1.26 bump

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.25-2
- Perl 5.16 rebuild

* Thu Mar 15 2012 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 07 2011 Petr Pisar <ppisar@redhat.com> 1.22-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr code from spec
- Do not export private module DB
