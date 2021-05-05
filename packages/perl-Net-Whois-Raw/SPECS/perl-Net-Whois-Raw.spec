%global cpan_version 2.99026

Name:           perl-Net-Whois-Raw
# Keep 2-digit precision
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        1%{?dist}
Summary:        Get Whois information for domains
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-Whois-Raw
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Whois-Raw-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{_bindir}/iconv
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(Encode)
# HTTP::Headers not used at tests
# HTTP::Request not used at tests
BuildRequires:  perl(IO::Socket::IP)
# LWP::UserAgent not used at tests
BuildRequires:  perl(Regexp::IPv6)
# URI::URL not used at tests
BuildRequires:  perl(utf8)

# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI::URL)

%description
Net::Whois::Raw queries WHOIS servers about domains. The module supports
recursive WHOIS queries. Also queries via HTTP is supported for some TLDs.

%prep
%setup -q -n Net-Whois-Raw-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE COPYRIGHT
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n pwhois
Summary:        Perl written whois client
# Getopt::Long not used at tests
# Net::IDN::Punycode 1 not used at tests
# Win32API::Registry not used on Linux
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Getopt::Long) >= 2
Requires:       perl(Net::IDN::Punycode) >= 1
# Win32API::Registry not used on Linux

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Net::IDN::Punycode\\)$

%description -n pwhois
Command line whois client.  Invoke with a domain name, optionally with a whois
server name.

%files -n pwhois
%license LICENSE COPYRIGHT
%doc README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Fri Oct 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.026-1
- 2.99026 bump

* Thu Oct 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.025-1
- 2.99025 bump

* Wed Oct 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.024-1
- 2.99024 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.022-1
- 2.99022 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.021-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.021-1
- 2.99021 bump

* Tue Sep 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.020-1
- 2.99020 bump

* Thu Aug 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.018-1
- 2.99018 bump

* Mon Aug 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.016-1
- 2.99016 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.015-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.015-1
- 2.99015 bump

* Wed May 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.014-1
- 2.99014 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.013-1
- 2.99013 bump

* Mon Nov 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.011-1
- 2.99011 bump

* Mon Aug 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.010-1
- 2.99010 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.009-1
- 2.99009 bump

* Tue Jun 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.008-1
- 2.99008 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.006-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.006-1
- 2.99006 bump

* Thu Aug 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.001-1
- 2.99001 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.94-2
- Perl 5.24 rebuild

* Thu Mar 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.94-1
- 2.94 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.91-1
- 2.91 bump

* Wed Sep 23 2015 Petr Pisar <ppisar@redhat.com> - 2.86-1
- 2.86 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.82-2
- Perl 5.22 rebuild

* Sat Feb 14 2015 David Dick <ddick@cpan.org> - 2.82-1
- New TLDs for .MOSCOW and fix encoding for whois.jprs.jp

* Tue Jan 20 2015 David Dick <ddick@cpan.org> - 2.80-1
- New TLDs

* Mon Jul 07 2014 David Dick <ddick@cpan.org> - 2.76-1
- Initial release
