Name:		perl-Net-HL7
Version:	0.82
Release:	8%{?dist}
Summary:	Simple perl API for HL7 messages
License:	Beerware and (GPL+ or Artistic)
URL:		https://metacpan.org/release/Net-HL7
Source0:	https://cpan.metacpan.org/authors/id/D/DD/DDOKTER/Net-HL7-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Config)
BuildRequires:	perl(Errno)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(IO::Socket::INET)
BuildRequires:	perl(IO::Socket::Timeout)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Test::More)
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	coreutils

Requires:	perl(Sys::Hostname)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Net-HL7 package is a simple Perl API for creating, parsing, sending and
receiving HL7 messages.

%prep
%setup -q -n Net-HL7-%{version}
find . -type f -executable -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%{perl_vendorlib}/*
%{_mandir}/man3/Net::HL7*.3pm*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Bill Pemberton <wfp5p@worldbroken.com> - 0.82-1
- update to version 0.82

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.81-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.81-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Bill Pemberton <wfp5p@worldbroken.com> - 0.81-2
- update the BuildRequires
- update the files section to get everything

* Thu Sep 17 2015 Bill Pemberton <wfp5p@worldbroken.com> - 0.81-1
- Initial version
