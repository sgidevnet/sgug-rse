Name:           perl-podlinkcheck
Version:        15
Release:        9%{?dist}
Summary:        Check Perl POD L<> link references
License:        GPLv3+
URL:            https://metacpan.org/release/podlinkcheck
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/podlinkcheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# Config not used at tests
BuildRequires:  perl(constant::defer)
# File::Find::Iterator not used at tests
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(File::Temp)
# FindBin not used at tests
# Getopt::Long not used at tests
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::TextDomain)
# Pod::Find not used at tests
BuildRequires:  perl(Pod::Simple)
# Search::Dict not used at tests
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(vars)
# Recommended run-time:
# Sort::Key::Natural not used at tests
# Tests:
BuildRequires:  perl(Config)
# Data::Dumper not used
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Data::Dumper)
# Disable BR Devel::FindRef, because it does not built with Perl 5.22
%if ! 0%(perl -e 'print $] >= 5.022')
#BuildRequires:  perl(Devel::FindRef)
%endif
# Devel::StackTrace not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Config)
Requires:       perl(File::Find::Iterator)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(File::Temp)
Requires:       perl(FindBin)
Requires:       perl(Getopt::Long)
Requires:       perl(IPC::Run)
Requires:       perl(Pod::Find)
Requires:       perl(Search::Dict)
# Recommended:
Recommends:     perl(Sort::Key::Natural)
# We do not (build-)require CPAN, CPANPLUS on purpose
Suggests:       perl(CPAN)
Suggests:       perl(CPAN::SQLite)
Suggests:       perl(CPANPLUS::Backend)
Suggests:       perl(CPANPLUS::Configure)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

%description
PodLinkCheck parses Perl POD from a script, module or documentation
and checks that L<> links within it refer to a known program, module,
or man page.

%prep
%setup -q -n podlinkcheck-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 15-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 15-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 15-2
- Perl 5.26 rebuild

* Tue May 02 2017 Petr Pisar <ppisar@redhat.com> - 15-1
- 15 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 14-2
- Perl 5.24 rebuild

* Mon Mar 07 2016 Petr Pisar <ppisar@redhat.com> - 14-1
- 14 bump

* Mon Feb 22 2016 Petr Pisar <ppisar@redhat.com> - 13-1
- 13 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 12-7
- Perl 5.22 rebuild

* Tue Jun 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 12-6
- Disable optional BR Devel::FindRef for Perl 5.22

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 12-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 12-2
- Perl 5.18 rebuild

* Mon Feb 18 2013 Petr Pisar <ppisar@redhat.com> - 12-1
- 12 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Petr Pisar <ppisar@redhat.com> - 11-1
- 11 bump

* Mon Nov 26 2012 Petr Pisar <ppisar@redhat.com> - 10-1
- 10 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 9-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 9-1
- 9 bump

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 8-2
- Perl 5.16 rebuild

* Wed Apr 25 2012 Petr Pisar <ppisar@redhat.com> 8-1
- Specfile autogenerated by cpanspec 1.78.
