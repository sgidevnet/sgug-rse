# Perform tests that access the Internet.
%bcond_with perl_Net_FTP_RetrHandle_enables_network_test

%global         cpan_name Net-FTP-RetrHandle
Name:           perl-%{cpan_name}
Version:        0.2
Release:        29%{?dist}
Summary:        File reading interface for reading files on a remote FTP server
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GI/GIFF/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
%if %{with perl_Net_FTP_RetrHandle_enables_network_test}
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(Symbol)
%endif
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%{?perl_default_filter}

%description
This Perl module provides a file reading interface for reading all or parts of
files located on a remote FTP server, including emulation of seek and support
for downloading only the parts of the file requested.

Support for skipping the beginning of the file is implemented with the FTP REST
command, which starts a retrieval at any point in the file. Support for
skipping the end of the file is implemented with the FTP ABOR command, which
stops the transfer. With these two commands and some careful tracking of the
current file position, we're able to reliably emulate a seek/read pair, and get
only the parts of the file that are actually read.

This was originally designed for use with Archive::Zip; it's reliable enough
that the table of contents and individual files can be extracted from a remote
ZIP archive without downloading the whole thing.

An interface compatible with IO::Handle is provided, along with a tie-based
interface.

%prep
%setup -q -n %{cpan_name}-%{version}
# Remove any CVS files
find -type d -name CVS -exec rm -rf {} +
perl -i -ne 'print $_ unless m{/CVS/}' MANIFEST
# Remove network tests
%if !%{with perl_Net_FTP_RetrHandle_enables_network_test}
for T in t/10remote.t t/11tie.t; do
  rm "$T"
  perl -i -ne 'print $_ unless m{^'"$T"'}' MANIFEST
done
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc TODO NEWS
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-29
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Petr Pisar <ppisar@redhat.com> - 0.2-27
- Modernize a spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-22
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 29 2016 Petr Pisar <ppisar@redhat.com> - 0.2-17
- Modernize spec file

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-13
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.2-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.2-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.2-4
- Perl mass rebuild

* Wed Jul 20 2011 Bernard Johnson <bjohnson@symetrix.com> - 0.2-3
- remove extraneous doc section

* Sun Jul 17 2011 Bernard Johnson <bjohnson@symetrix.com> - 0.2-2
- add additional documentation files including test cases

* Fri Jul 08 2011 Bernard Johnson <bjohnson@symetrix.com> - 0.2-1
- initial package
