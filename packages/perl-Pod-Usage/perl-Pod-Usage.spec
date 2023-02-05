Name:           perl-Pod-Usage
# Compete with perl.spec's epoch
Epoch:          4
Version:        2.01
Release:        1%{?dist}
Summary:        Print a usage message from embedded POD documentation
# License clarification CPAN RT#102529
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Usage
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Pod-Usage-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# scripts/pod2usage.PL uses Config
BuildRequires:  perl(Config)
# scripts/pod2usage.PL uses Cwd
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# scripts/pod2usage.PL uses File::Basename
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
# Getopt::Long not used, scripts/pod2usage not called
# Pod::Usage executes perldoc from perl-Pod-Perldoc by default
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl(Pod::Text) >= 4
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Pod::Perldoc) >= 3.28
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Test::More) >= 0.6
BuildRequires:  perl(vars)
# VMS::Filespec not used
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::Spec) >= 0.82
# Pod::Usage executes perldoc from perl-Pod-Perldoc by default
Requires:       perl-Pod-Perldoc
Requires:       perl(Pod::Text) >= 4

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude|%{__requires_exclude}|}^perl\\(File::Spec\\)$

%description
pod2usage will print a usage message for the invoking script (using its
embedded POD documentation) and then exit the script with the desired exit
status. The usage message printed may have any one of three levels of
"verboseness": If the verbose level is 0, then only a synopsis is printed.
If the verbose level is 1, then the synopsis is printed along with a
description (if present) of the command line options and arguments. If the
verbose level is 2, then the entire manual page is printed.

%prep
%setup -q -n Pod-Usage-%{version}
# Remove bundled modules
rm -rf t/inc
perl -i -ne 'print $_ unless m{^t/inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Oct 14 2020 Petr Pisar <ppisar@redhat.com> - 4:2.01-1
- 2.01 bump

* Mon Mar 16 2020 Petr Pisar <ppisar@redhat.com> - 4:1.70-1
- 1.70 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.69-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.69-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.69-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.69-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.69-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.69-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.69-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.69-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 24 2016 Petr Pisar <ppisar@redhat.com> - 4:1.69-1
- 1.69 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.68-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Petr Pisar <ppisar@redhat.com> - 4:1.68-1
- 1.68 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:1.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.67-2
- Perl 5.22 rebuild

* Mon Mar 02 2015 Petr Pisar <ppisar@redhat.com> - 4:1.67-1
- 1.67 bump

* Mon Feb 23 2015 Petr Pisar <ppisar@redhat.com> - 4:1.66-1
- 1.66 bump

* Mon Feb 16 2015 Petr Pisar <ppisar@redhat.com> - 4:1.65-1
- 1.65 bump

* Thu Nov 13 2014 Petr Pisar <ppisar@redhat.com> - 4:1.64-3
- Compete with perl.spec's epoch (bug #1163490)

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.64-2
- Perl 5.20 rebuild

* Tue Jul 01 2014 Petr Pisar <ppisar@redhat.com> - 1.64-1
- 1.64 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.63-3
- Link minimal build-root packages against libperl.so explicitly

* Tue Jun 25 2013 Petr Pisar <ppisar@redhat.com> - 1.63-2
- Correct dependencies

* Tue Jun 04 2013 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump

* Tue May 21 2013 Petr Pisar <ppisar@redhat.com> - 1.62-1
- 1.62 bump

* Wed Feb 06 2013 Petr Pisar <ppisar@redhat.com> - 1.61-1
- 1.61 bump

* Mon Feb 04 2013 Petr Pisar <ppisar@redhat.com> 1.60-1
- Specfile autogenerated by cpanspec 1.78.
