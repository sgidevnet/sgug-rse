Name:           perl-IO-Pty-Easy
Version:        0.10
Release:        13%{?dist}
Summary:        Easy interface to IO::Pty
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IO-Pty-Easy
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Pty-Easy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
IO::Pty::Easy provides an interface to IO::Pty which hides most of the
ugly details of handling ptys, wrapping them instead in simple
spawn/read/write commands.

%prep
%setup -q -n IO-Pty-Easy-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-13
- Perl 5.32 rebuild

* Tue Feb 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-12
- Modernize spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-1
- 0.10 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-7
- Perl 5.24 rebuild

* Fri Mar 04 2016 Petr Pisar <ppisar@redhat.com> - 0.09-6
- Fix a race in t/read-write.t test (bug #1314777)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.20 rebuild

* Thu Jul 24 2014 David Dick <ddick@cpan.org> - 0.09-1
- Initial release
