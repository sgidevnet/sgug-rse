Name:           perl-App-find2perl
Version:        1.005
Release:        8%{?dist}
Summary:        Translate find command lines to Perl code
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/App-find2perl
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-find2perl-%{version}.tar.gz
BuildArch:      noarch
%if %{defined perl_bootstrap}
BuildRequires:  coreutils
%endif
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{defined perl_bootstrap}
BuildRequires:  sed
%endif
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib) >= 1.01
%if !%{defined perl_bootstrap}
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::FindPerl) >= 0.009
BuildRequires:  perl(File::Path)
%endif
BuildRequires:  perl(File::Spec)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(File::Temp)
%endif
BuildRequires:  perl(IO::Handle)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(IPC::Open2)
%endif
BuildRequires:  perl(IPC::Open3)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(open)
BuildRequires:  perl(Perl::OSType)
%endif
BuildRequires:  perl(Test::More)
%if !%{defined perl_bootstrap}
BuildRequires:  %{_bindir}/find
%endif
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Conflicts:      perl < 4:5.18.2-300

%description
This package delivers find2perl tool which is a little translator to convert
find command lines to equivalent Perl code.

%prep
%setup -q -n App-find2perl-%{version}
%if %{defined perl_bootstrap}
rm t/find2perl.t
sed -i -e '/^t\/find2perl.t/d' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
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
* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-8
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-7
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-1
- 1.005 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-2
- Perl 5.28 rebuild

* Tue Mar 20 2018 Petr Pisar <ppisar@redhat.com> - 1.004-1
- 1.004 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-12
- Perl 5.26 re-rebuild of bootstrapped packages

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-9
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-5
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-4
- Perl 5.22 rebuild

* Thu Jan 08 2015 Petr Pisar <ppisar@redhat.com> - 1.003-3
- Disable a test when bootstrapping because of non-core Devel::FindPerl

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-2
- Perl 5.20 rebuild

* Thu Jun 19 2014 Petr Pisar <ppisar@redhat.com> 1.003-1
- Specfile autogenerated by cpanspec 1.78.
