Name:           perl-Net-OpenSSH
Version:        0.79
Release:        2%{?dist}
Summary:        Perl SSH client package implemented on top of OpenSSH
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-OpenSSH
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-OpenSSH-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
# Data::Dumper not used at tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
# File::Glob not used at tests
BuildRequires:  perl(File::Spec)
# Moo not used at tests
# Object::Remote::Role::Connector::PerlInterpreter not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
# Sys::Hostname not used at tests
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       openssh-clients
Requires:       perl(File::Glob)
Suggests:       perl(IO::Pty)
Suggests:       perl(Net::SFTP::Foreign) >= 1.47
Requires:       perl(Object::Remote::Role::Connector::PerlInterpreter)
Suggests:       perl(Sys::Hostname)

# Needed to stop the sample scripts pulling in more perl packages.
%{?perl_default_filter}

%description
Net::OpenSSH is a secure shell client package implemented on top of OpenSSH
binary client (ssh).

%prep
%setup -q -n Net-OpenSSH-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-2
- Perl 5.32 rebuild

* Tue May 12 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-1
- 0.79 bump
- Modernize spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-2
- Perl 5.28 rebuild

* Tue May 15 2018 steve traylen <steve.traylen@cern.ch> - 0.78-1
- 0.78 update

* Thu Mar 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-1
- 0.77 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-2
- Perl 5.26 rebuild

* Thu Mar 23 2017 Steve Traylen <steve.traylen@cern.ch> - 0.74-1
- 0.74 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Petr Pisar <ppisar@redhat.com> - 0.73-1
- 0.73 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-2
- Perl 5.24 rebuild

* Mon Feb 15 2016 Petr Pisar <ppisar@redhat.com> - 0.70-1
- 0.70 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-2
- Perl 5.22 rebuild

* Mon Jun 1 2015 Steve Traylen <steve.traylen@cern.ch> - 0.64-1
- Upstream to 0.64

* Wed Sep 24 2014 Steve Traylen <steve.traylen@cern.ch> - 0.62-1
- Upstream to 0.62.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Steve Traylen <steve.traylen@cern.ch> - 0.60-1
- Upstream to 0.60.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.57-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 0.57-5
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 0.57-4
- Do not require specific architecture of openssh-clients

* Fri May 18 2012 Steve Traylen <steve.traylen@cern.ch> - 0.57-3
- Rebuild for bad _isa rpm macro.

* Fri Apr 27 2012 Steve Traylen <steve.traylen@cern.ch> 0.57-2
- Remove requires perl(Test::More) since only needed for tests. rhbz#813668
- Add requires openssh-clients
- Add sample files as docs


* Wed Apr 18 2012 Steve Traylen <steve.traylen@cern.ch> 0.57-1
- Specfile autogenerated by cpanspec 1.78.
