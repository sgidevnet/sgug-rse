%global cpan_version 1.190840

Name:           perl-WebService-Rajce
# Normalize version to dotted format
Version:        %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:        5%{?dist}
Summary:        Perl interface for www.rajce.idnes.cz
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/WebService-Rajce
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEK/WebService-Rajce-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time (No tests exhibiting the code are performed)
# AutoLoader not used at tests
# Carp not used at tests
# Digest::MD5 not used at tests
# Encode not used at tests
# Exporter not used at tests
# File::Basename not used at tests
# File::Path not used at tests
# Getopt::Long not used at tests
# Image::Magick not used at tests
# https URLs are passed to the LWP
# LWP::Protocol::https not used at tests
# Net::Netrc not used at tests
# Pod::Usage not used at tests
# POSIX not used at tests
# vars not used at tests
# WWW::Mechanize not used at tests
# XML::Simple not used at tests
# Tests:
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More)
# Test::Pod::Coverage 1.08 not used
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(AutoLoader)
# https URLs are passed to the LWP
Requires:       perl(LWP::Protocol::https)

%description
This is a Perl library implementing an API of a photo gallery service running
on www.rajce.idnes.cz server.

%package tools
Summary:        Utilities for accessing www.rajce.idnes.cz
License:        GPL+ or Artistic
BuildArch:      noarch

%description tools
Command line tools for uploading and downloading images from a photo gallery
service running on www.rajce.idnes.cz server.


%prep
%setup -q -n WebService-Rajce-%{cpan_version}

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

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.190.840-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.190.840-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.190.840-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.190.840-2
- Perl 5.30 rebuild

* Tue Mar 26 2019 Petr Pisar <ppisar@redhat.com> - 1.190.840-1
- 1.190840 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.180.380-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.180.380-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.180.380-2
- Perl 5.28 rebuild

* Thu Feb 08 2018 Petr Pisar <ppisar@redhat.com> - 1.180.380-1
- 1.180380 bump

* Wed Feb 07 2018 Petr Pisar <ppisar@redhat.com> - 1.180.370-1
- 1.180370 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.152.450-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.152.450-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.152.450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 03 2016 Petr Pisar <ppisar@redhat.com> - 1.152.450-1
- Normalize version to dotted format

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.15.2450-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 04 2015 Petr Pisar <ppisar@redhat.com> - 1.15.2450-1
- 1.152450 bump

* Mon Aug 31 2015 Petr Pisar <ppisar@redhat.com> - 1.15.2420-1
- 1.152420 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0930-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.13.0930-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.13.0930-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0930-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0930-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.13.0930-2
- Perl 5.18 rebuild

* Fri Apr 05 2013 Petr Pisar <ppisar@redhat.com> - 1.13.0930-1
- 1.130930 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.07-2
- Perl 5.16 rebuild

* Wed Feb 29 2012 Petr Pisar <ppisar@redhat.com> 0.07-1
- Specfile autogenerated by cpanspec 1.78.
