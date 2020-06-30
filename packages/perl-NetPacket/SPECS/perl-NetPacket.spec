Name:           perl-NetPacket
Version:        1.7.2
Release:        5%{?dist}
Summary:        Assemble/disassemble network packets at the protocol level
# CODE_OF_CONDUCT.md:   CC-BY
# lib/NetPacket.pm:     Artistic 2.0
License:        Artistic 2.0 and CC-BY
URL:            https://metacpan.org/release/NetPacket
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/NetPacket-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(Socket) >= 1.87
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
NetPacket provides a base class for a cluster of modules related to decoding
and encoding of network protocols. Each NetPacket descendant module knows how
to encode and decode packets for the network protocol it implements. Consult
the documentation for the module in question for protocol-specific
implementation.

%prep
%setup -q -n NetPacket-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.2-5
- Perl 5.32 rebuild

* Fri Feb 28 2020 Petr Pisar <ppisar@redhat.com> - 1.7.2-4
- Build-requires blib for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Petr Pisar <ppisar@redhat.com> - 1.7.2-1
- 1.7.2 bump

* Mon Jun 10 2019 Petr Pisar <ppisar@redhat.com> - 1.7.1-1
- 1.7.1

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Petr Pisar <ppisar@redhat.com> - 1.7.0-1
- 1.7.0 bump
- License changed to (Artistic 2.0 and CC-BY)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-8
- Perl 5.26 rebuild

* Mon Mar 20 2017 Petr Pisar <ppisar@redhat.com> - 1.6.0-7
- Modernize spec file

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-2
- Perl 5.22 rebuild

* Sat Mar 14 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.0-1
- Update to 1.6.0

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.0-2
- Perl 5.20 rebuild

* Sun Jun 15 2014 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.5.0-1
- Update to 1.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 30 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.4-1
- Update to 1.4.4

* Tue Nov 26 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.3-1
- Update to 1.4.3

* Thu Sep 26 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.2-1
- Update to 1.4.2

* Fri Sep  6 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.1-1
- Update to 1.4.1

* Thu Aug 29 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.0-1
- Update to 1.4.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.3.3-3
- Perl 5.18 rebuild

* Thu May 16 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.3-2
- No longer disable the 000-report-versions.t test

* Thu May 16 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.3-1
- Update to 1.3.3.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.3.1-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.1-1
- Update to 1.3.1.

* Mon Nov 14 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.0-1
- Update to 1.3.0.
- Rebased patch0.

* Sat Jul 30 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-1
- Update to 1.2.0.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.1-2
- Perl mass rebuild

* Thu Feb 10 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.1.1-1
- Update to 1.1.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.1.0-1
- Update to 1.1.0.

* Fri Dec 24 2010 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0.1-1
- Update to 1.0.1.
- Disable test t/000-report-versions.t and downgrade build requirements
  (NetPacket-1.0.1-Build.PL-downgrade-modules-requirements.patch) in order
  to support EPEL >= 5 and Fedora >= 12.

* Mon Mar 29 2010 Jan Klepek 0.42.0-1
- Changed license to Artistic 2.0 and updated version

* Mon Mar 15 2010 Jan Klepek 0.41.1-1
- Specfile autogenerated by cpanspec 1.78.
