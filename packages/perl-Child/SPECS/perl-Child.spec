Name:           perl-Child
Version:        0.013
Release:        13%{?dist}
Summary:        Object oriented simple interface to fork()
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Child
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Child-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Capture::Tiny) >= 0.31
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Exporter) >= 5.57
Requires:       perl(POSIX)

# Filter under-specified dependency
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$

%description
Fork is too low level and difficult to manage. Often people forget to exit
at the end, reap their children, and check exit status. The problem is the
low level functions provided to do these things. Throw in pipes for IPC and
you just have a pile of things nobody wants to think about.

%prep
%setup -q -n Child-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendorlib}/Child.pm
%{perl_vendorlib}/Child/
%{_mandir}/man3/Child.3*
%{_mandir}/man3/Child::IPC::Pipe.3*
%{_mandir}/man3/Child::Link.3*
%{_mandir}/man3/Child::Link::IPC.3*
%{_mandir}/man3/Child::Link::IPC::Pipe.3*
%{_mandir}/man3/Child::Link::IPC::Pipe::Parent.3*
%{_mandir}/man3/Child::Link::IPC::Pipe::Proc.3*
%{_mandir}/man3/Child::Link::Parent.3*
%{_mandir}/man3/Child::Link::Proc.3*
%{_mandir}/man3/Child::Util.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Paul Howarth <paul@city-fan.org> - 0.013-11
- Spec tidy-up
  - Drop redundant buildroot cleaning in %%install section
  - Fix permissions verbosely

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Paul Howarth <paul@city-fan.org> - 0.013-1
- Update to 0.013
  - Fix Windows
- BR: perl-generators
- Simplify find command using -delete
- Drop redundant %%{?perl_default_filter}

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.012-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 30 2015 Paul Howarth <paul@city-fan.org> - 0.012-1
- Update to 0.012
  - Switch to Dist::Zilla
  - Switch to new Changes Layout
  - Fix destructor bug (#12)
- Switch to ExtUtils::MakeMaker flow
- Package upstream's new LICENSE file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-2
- Perl 5.22 rebuild

* Thu Jun 04 2015 Petr Šabata <contyk@redhat.com> - 0.011-1
- 0.011 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Paul Howarth <paul@city-fan.org> - 0.010-2
- Downgrade Module::Build version requirement from 0.42 to 0.40

* Wed Apr 23 2014 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Processes created by fork will have negative pids on Windows

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.009-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.009-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Iain Arnell <iarnell@gmail.com> 0.009-1
- Specfile autogenerated by cpanspec 1.78.
