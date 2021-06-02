Name:           perl-Time-OlsonTZ-Download
Version:        0.009
Release:        7%{?dist}
Summary:        Olson time zone database from source
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Time-OlsonTZ-Download
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Time-OlsonTZ-Download-%{version}.tar.gz
# Use GnuPG2 instead of GnuPG1, CPAN RT#124132
Patch0:         Time-OlsonTZ-Download-0.008-Use-gpgv2-from-GnuPG-2.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# coreutils for cp, sha512sum, not used at tests
# gnupg2 for gpgv2, not used at tests
# gzip for gunzip, not used at tests
# lzip not used at tests
# make not used at tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 1.75
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(IO::Dir) >= 1.03
BuildRequires:  perl(IO::File) >= 1.03
BuildRequires:  perl(IPC::Filter) >= 0.002
BuildRequires:  perl(Net::FTP) >= 3.07
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(utf8)
# tar not used at tests
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# coreutils for cp, sha512sum
Requires:       coreutils
# gnupg2 for gpgv2
Requires:       gnupg2
# gzip for gunzip
Requires:       gzip
Requires:       lzip
Requires:       make
Requires:       tar

%{?perl_default_filter}

%description
An object of this Perl class represents a local copy of the source of the
Olson time zone database, possibly used to build binary tzfiles. The source
copy always begins by being downloaded from the canonical repository of the
Olson database. This class provides methods to help with extracting useful
information from the source.

%prep
%setup -q -n Time-OlsonTZ-Download-%{version}
%patch0 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Petr Pisar <ppisar@redhat.com> - 0.009-1
- 0.009 bump

* Fri Jan 19 2018 Petr Pisar <ppisar@redhat.com> - 0.008-1
- 0.008 bump
- Use GnuPG2 instead of GnuPG1 (CPAN RT#124132)

* Tue Oct 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-1
- 0.007 bump

* Mon Aug 14 2017 Petr Pisar <ppisar@redhat.com> - 0.006-2
- Fix a dependency on gunzip tool

* Wed Aug 09 2017 Petr Pisar <ppisar@redhat.com> - 0.006-1
- 0.006 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-13
- Perl 5.26 rebuild

* Mon May 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-12
- Fix regexp syntax for Perl 5.26

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-7
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.004-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 0.004-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.003-2
- Perl 5.16 rebuild

* Sun Mar 25 2012 Iain Arnell <iarnell@gmail.com> 0.003-1
- Specfile autogenerated by cpanspec 1.79.
