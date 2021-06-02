Name:           perl-Authen-Radius
Version:        0.31
Release:        2%{?dist}
Summary:        Provide simple Radius client facilities
License:        Artistic 2.0
URL:            https://metacpan.org/release/Authen-Radius
Source0:        https://cpan.metacpan.org/modules/by-module/Authen/Authen-Radius-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper) >= 1
BuildRequires:  perl(Data::HexDump) >= 0.02
BuildRequires:  perl(Digest::MD5) >= 2.20
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO) >= 1.12
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Net::IP) >= 1.26
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional Tests
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper) >= 1
Requires:       perl(Data::HexDump) >= 0.02
Requires:       perl(Digest::MD5) >= 2.20
Requires:       perl(IO) >= 1.12
Requires:       perl(Net::IP) >= 1.26

# Filter unversioned dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Data::Dumper\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Data::HexDump\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Digest::MD5\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Net::IP\\)\\s*$

%description
The Authen::Radius module provides a simple class that allows you to
send/receive Radius requests/responses to/from a Radius server.

You can just authenticate usernames/passwords via Radius, or completely
imitate AAA requests and process server responses.

%prep
%setup -q -n Authen-Radius-%{version}

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
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Authen/
%{_mandir}/man3/Authen::Radius.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Paul Howarth <paul@city-fan.org> - 0.31-1
- Update to 0.31
  - Fixed check_pwd() method when dictionaries are not loaded and attribute ID
    is used instead of Name

* Tue Jun 11 2019 Paul Howarth <paul@city-fan.org> - 0.30-1
- Update to 0.30
  - Fixed warning when NodeList parameter used without Host

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Paul Howarth <paul@city-fan.org> - 0.29-1
- Update to 0.29
  - Fixed tagged integer attribute encoding
  - Fix tests if FreeRADIUS dictionary not available

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul  8 2018 Paul Howarth <paul@city-fan.org> - 0.27-1
- Update to 0.27
  - Force FreeRADIUS dictionary format when BEGIN-VENDOR directive is found
  - Load included files using the requested format
  - Added full support for octets type

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Paul Howarth <paul@city-fan.org> - 0.26-4
- Classify buildreqs by usage

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- Update to 0.26
  - Require Perl v5.10+
  - Fixed warnings in tests
  - Fix sublist attribute type encoding

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 31 2013 Paul Howarth <paul@city-fan.org> - 0.24-1
- Update to 0.24
  - Added support for changing I/O activity timeouts, so that custom
    retransmission policies can be implemented
  - Added ACCESS_CHALLENGE packet type definition
  - Fix the excessive wait on processing broadcasts when at least one of the
    nodes in node list did not listen on the requested port (a side-effect is
    that it is now possible to set timeout in floating seconds since the epoch)
- BR: perl(Time::HiRes)

* Thu Oct 31 2013 Paul Howarth <paul@city-fan.org> - 0.23-1
- Update to 0.23
  - Authen::Radius is now distributed under the Perl Artistic License v2.0
  - Support for RADIUS retransmits
  - For the "check_pwd" method, place the local socket's "real" IP address into
    the NAS-IP-Address attribute instead of 127.0.0.1
  - Bugfixes in error handling
  - Generate random authenticators
  - Support for CoA request
  - Ability to specify the source IP/port for outgoing packets
  - Support for RFC3579 - Message-Authenticator
  - Support for a list of multiple RADIUS servers (RADIUS cluster)
  - Ability to work with dictionaries in FreeRADIUS format
  - Support (partial) for WIMAX attributes
  - Fixed the bug with the incorrect encoding of Cisco AVPair attributes
  - Added support for attribute values for byte and short attribute types
  - Fix the excessive "types mismatch" warnings on PoD packets
  - Clear authenticator as a part of clear_attibutes(), so multiple requests,
    sent using the same object, will have different authenticators (as they
    should)
- Specify all dependencies
- Drop %%defattr, redundant since rpm 4.4
- Package upstream's new LICENSE file
- Make %%files list more explicit
- Use %%{_fixperms} macro rather than our own chmod incantation
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Don't use macros for commands
- Run the test suite now that it skips tests that require a Radius server

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.13-15
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.13-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.13-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-8
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.13-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.13-3
- fix license tag (with permission from upstream)

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.13-2
- rebuild for new perl

* Sat Mar 10 2007 Andreas Thienemann <andreas@bawue.net> - 0.13-1
- Updated to 0.13
- Added perl-devel BuildReq

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 0.12-3
- FE6 Rebuild

* Thu Apr 13 2006 Andreas Thienemann <andreas@bawue.net> 0.12-2
- Final cleanup for inclusion.

* Wed Mar 29 2006 Andreas Thienemann <andreas@bawue.net> 0.12-1
- Cleaned up for FE
- Specfile autogenerated by cpanspec 1.64.
