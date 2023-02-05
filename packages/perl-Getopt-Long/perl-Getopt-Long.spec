Name:           perl-Getopt-Long
Epoch:          1
Version:        2.51
Release:        1%{?dist}
Summary:        Extended processing of command line options
License:        GPLv2+ or Artistic
URL:            https://metacpan.org/release/Getopt-Long
Source0:        https://cpan.metacpan.org/authors/id/J/JV/JV/Getopt-Long-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(overload)
Requires:       perl(Text::ParseWords)
# Recommended:
Requires:       perl(Pod::Usage) >= 1.14
# Dependencies on these Perl 4 files are generated as perl(foo.pl):
Provides:       perl(newgetopt.pl) = %{version}

%description
The Getopt::Long module implements an extended getopt function called
GetOptions(). It parses the command line from @ARGV, recognizing and removing
specified options and their possible values.  It adheres to the POSIX syntax
for command line options, with GNU extensions. In general, this means that
options have long names instead of single letters, and are introduced with
a double dash "--". Support for bundling of command line options, as was the
case with the more traditional single-letter approach, is provided but not
enabled by default.

%prep
%setup -q -n Getopt-Long-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Aug 13 2019 Petr Pisar <ppisar@redhat.com> - 1:2.51-1
- 2.51 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.50-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.50-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.50-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.50-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.50-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.50-2
- Perl 5.26 rebuild

* Mon May 29 2017 Petr Pisar <ppisar@redhat.com> - 2.50-1
- 2.50 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Petr Pisar <ppisar@redhat.com> - 2.49.1-1
- 2.49.1 bump

* Wed Jun 15 2016 Petr Pisar <ppisar@redhat.com> - 2.49-1
- 2.49 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.48-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Petr Pisar <ppisar@redhat.com> - 2.48-1
- 2.48 bump

* Wed Jun 17 2015 Petr Pisar <ppisar@redhat.com> - 2.47-1
- 2.47 bump

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.46-2
- Perl 5.22 rebuild

* Tue Jun 02 2015 Petr Pisar <ppisar@redhat.com> - 2.46-1
- 2.46 bump

* Tue Feb 24 2015 Petr Pisar <ppisar@redhat.com> - 2.45-1
- 2.45 bump

* Thu Feb 19 2015 Petr Pisar <ppisar@redhat.com> - 2.44-1
- 2.44 bump

* Fri Jan 30 2015 Petr Pisar <ppisar@redhat.com> - 2.43-1
- 2.43 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 02 2013 Petr Pisar <ppisar@redhat.com> - 2.42-1
- 2.42 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.41-2
- Link minimal build-root packages against libperl.so explicitly

* Wed Jul 10 2013 Petr Pisar <ppisar@redhat.com> - 2.41-1
- 2.41 bump

* Thu Jun 20 2013 Petr Pisar <ppisar@redhat.com> - 2.40-1
- 2.40 bump

* Fri Apr 05 2013 Petr Pisar <ppisar@redhat.com> 2.39-1
- Specfile autogenerated by cpanspec 1.78.
