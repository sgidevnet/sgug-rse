Name:           perl-ExtUtils-HasCompiler
Version:        0.021
Release:        10%{?dist}
Summary:        Check for the presence of a compiler
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ExtUtils-HasCompiler
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-HasCompiler-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Mksymlists)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Mksymlists)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module tries to check if the current system is capable of compiling,
linking and loading an XS module.

%prep
%setup -q -n ExtUtils-HasCompiler-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-1
- 0.021 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-2
- Perl 5.26 rebuild

* Thu Feb 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-1
- 0.017 bump

* Thu Jul 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.016-1
- 0.016 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-2
- Perl 5.24 rebuild

* Tue May 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-1
- 0.014 bump

* Mon Apr 11 2016 Petr Pisar <ppisar@redhat.com> - 0.013-1
- 0.013 bump

* Mon Mar 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.012-1
- Initial release
