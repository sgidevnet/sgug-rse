Name:           perl-ExtUtils-CBuilder
# Compete with perl.spec
Epoch:          1
# Mimic perl.spec
Version:        0.280231
Release:        439%{?dist}
Summary:        Compile and link C code for Perl modules
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ExtUtils-CBuilder
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-CBuilder-%{version}.tar.gz
# Link XS modules to libperl.so with EU::CBuilder on Linux, bug #960048
Patch0:         ExtUtils-CBuilder-0.280230-Link-XS-modules-to-libperl.so-with-EU-CBuilder-on-Li.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
# ExtUtils::Mksymlists 6.30 not used at test time
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 3.13
# File::Spec::Functions not used at test time
BuildRequires:  perl(File::Temp)
# IO::File not used at test time
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Perl::OSType) >= 1
BuildRequires:  perl(Text::ParseWords)
# Optional run-time:
# C and C++ compilers are highly recommended because compiling code is the
# purpose of ExtUtils::CBuilder, bug #1547165
BuildRequires:  gcc
BuildRequires:  gcc-c++
# Tests:
BuildRequires:  perl(Test::More) >= 0.47
# vmsish not used
# C and C++ compilers are highly recommended because compiling code is the
# purpose of ExtUtils::CBuilder, bug #1547165
Requires:       gcc
Requires:       gcc-c++
Requires:       perl-devel
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Mksymlists) >= 6.30
Requires:       perl(File::Spec) >= 3.13
Requires:       perl(Perl::OSType) >= 1

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Perl::OSType)\\)$

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.

%prep
%setup -q -n ExtUtils-CBuilder-%{version}
%patch0 -p1

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
%doc Changes CONTRIBUTING README README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.280231-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.280231-438
- Increase release to favour standalone package

* Wed Apr 03 2019 Petr Pisar <ppisar@redhat.com> - 1:0.280231-1
- 0.280231 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.280230-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.280230-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.280230-416
- Increase release to favour standalone package

* Fri Feb 23 2018 Petr Pisar <ppisar@redhat.com> - 1:0.280230-3
- Add a dependency on gcc and gcc-c++ (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.280230-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Petr Pisar <ppisar@redhat.com> - 1:0.280230-1
- 0.280230 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.280226-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Petr Pisar <ppisar@redhat.com> - 1:0.280226-1
- 0.280226 bump

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.280225-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.280225-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.280225-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.280225-1
- 0.280225 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.280224-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Petr Pisar <ppisar@redhat.com> - 1:0.280224-1
- 0.280224 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.280223-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.280223-2
- Perl 5.22 rebuild

* Thu Jun 04 2015 Petr Pisar <ppisar@redhat.com> - 1:0.280223-1
- 0.280223 bump

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.280221-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 1:0.280221-1
- 0.280221 bump in order to dual-live with perl 5.22

* Mon Nov 03 2014 Petr Pisar <ppisar@redhat.com> - 1:0.280220-1
- 0.280220 bump

* Thu Sep 18 2014 Petr Pisar <ppisar@redhat.com> - 1:0.280219-1
- Specfile autogenerated by cpanspec 1.78.
