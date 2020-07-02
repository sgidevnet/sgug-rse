Name:		perl-IO-Socket-Socks
Version:	0.74
Release:	9%{?dist}
Summary:	Provides a way to create socks (4 or 5) client or server
License:	LGPLv2+
URL:		https://metacpan.org/release/IO-Socket-Socks
Source0:	https://cpan.metacpan.org/authors/id/O/OL/OLEG/IO-Socket-Socks-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant) >= 1.03
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(overload)
BuildRequires:	perl(Socket) >= 1.94
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Time::HiRes)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:	perl(constant) >= 1.03
Requires:	perl(Socket) >= 1.94

# IPv6 support requires perl(IO::Socket::IP) ≥ 0.36, which is not available in EL-7
# so we have to fall back to IPv4-only IO::Socket::INET
%if 0%{?el7}
BuildRequires:	perl(IO::Socket::INET)
Requires:	perl(IO::Socket::INET)
%else
BuildRequires:	perl(IO::Socket::IP) >= 0.36
Requires:	perl(IO::Socket::IP) >= 0.36
%endif

%description
IO::Socket::Socks connects to a SOCKS proxy and tells it to open a connection
to a remote host/port when the object is created. The object you receive can be
used directly as a socket (with IO::Socket interface) for sending and receiving
data to and from the remote host. In addition to creating a socks client, this
module could be used to create a socks server.

%prep
%setup -q -n IO-Socket-Socks-%{version}

# Don't want executable documentation
chmod -c -x examples/*.pl

# Fix up shellbangs too
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' examples/*.pl

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
%doc Changes examples/ README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Socket::Socks.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-3
- Perl 5.28 rebuild

* Mon Feb 19 2018 Paul Howarth <paul@city-fan.org> - 0.74-2
- Incorporate feedback from package review (#1546648)
  - Add version requirements for constant and Socket runtime dependencies
  - Add examples/ as documentation

* Fri Feb 16 2018 Paul Howarth <paul@city-fan.org> - 0.74-1
- Initial RPM version
