Name:           perl-Carton
Version:        1.0.34
Release:        8%{?dist}
Summary:        Perl module dependency manager (aka Bundler for Perl)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Carton
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Carton-v%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# NOTE: there's no real non-interactive test suite
# BuildRequires:  perl(App::FatPacker)
# BuildRequires:  perl(Carp)
# BuildRequires:  perl(Class::Tiny) >= 1.001
# BuildRequires:  perl(Config)
# BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::Meta) >= 2.120921
# BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
# BuildRequires:  perl(File::Find)
# BuildRequires:  perl(File::pushd)
# BuildRequires:  perl(Getopt::Long) >= 2.39
# BuildRequires:  perl(JSON::PP) >= 2.27300
# BuildRequires:  perl(Menlo::CLI::Compat) >= 1.9018
# BuildRequires:  perl(Module::CoreList)
# BuildRequires:  perl(Module::CPANfile) >= 0.9031
# BuildRequires:  perl(overload)
# BuildRequires:  perl(parent) >= 0.223
# BuildRequires:  perl(Path::Tiny) >= 0.033
# BuildRequires:  perl(Scalar::Util)
# BuildRequires:  perl(subs)
# BuildRequires:  perl(Try::Tiny) >= 0.09
# BuildRequires:  perl(version)
# Optional run-time
# BuildRequires:  perl(IO::Compress::Gzip)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(CPAN::Meta) >= 2.120921
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Getopt::Long) >= 2.39
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(Menlo::CLI::Compat) >= 1.9018
Requires:       perl(Module::CPANfile) >= 0.9031
Requires:       perl(parent) >= 0.223
Requires:       perl(Path::Tiny) >= 0.033
Requires:       perl(Try::Tiny) >= 0.09
# See the docs
Recommends:     perl
Suggests:       perl(IO::Compress::Gzip)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::Requirements\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Module::CPANfile\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Path::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Try::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(parent\\)$

%description
carton is a command line tool to track the Perl module dependencies for
your Perl application.  Dependencies are declared using cpanfile format,
and the managed dependencies are tracked in a cpanfile.snapshot file,
which is meant to be version controlled, and the snapshot file allows
other developers of your application to have the exact same versions of
the modules.

%prep
%setup -q -n Carton-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/carton
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.34-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.34-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.34-2
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.34-1
- 1.0.34 bump

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.33-2
- Perl 5.28 rebuild

* Mon May 07 2018 Petr Pisar <ppisar@redhat.com> - 1.0.33-1
- 1.0.33 bump

* Thu May 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.31-1
- 1.0.31 bump

* Wed Apr 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.30-1
- 1.0.30 bump

* Mon Apr 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.29-1
- 1.0.29 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.28-4
- Perl 5.26 rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.28-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.28-1
- 1.0.28 bump

* Mon May 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.26-1
- 1.0.26 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.24-2
- Perl 5.24 rebuild

* Tue May 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.24-1
- 1.0.24 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Petr Šabata <contyk@redhat.com> 1.0.22-1
- Initial packaging
