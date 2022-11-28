Name:           perl-LWP-Protocol-connect
Version:        6.09
Release:        15%{?dist}
Summary:        Provides HTTP/CONNECT proxy support for LWP::UserAgent
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/LWP-Protocol-connect
Source0:        https://cpan.metacpan.org/authors/id/B/BE/BENNING/LWP-Protocol-connect-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(URI::http)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))


%description
The LWP::Protocol::connect module provides support for using https over a proxy
via the HTTP/CONNECT method.

%prep
%setup -q -n LWP-Protocol-connect-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*
%doc LICENSE
%doc CHANGES
%doc README

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.09-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.09-11
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.09-10
- Add missing run-requires MODULE_COMPAT

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.09-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.09-3
- Perl 5.22 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Sven Nierlein <sven.nierlein@consol.de> 6.09-1
- new upstream version

* Sun Apr 06 2014 Sven Nierlein <sven.nierlein@consol.de> 6.06-2
- added changes and readme
- used description from the module itself
- used DESTDIR instead of PERL_INSTALL_ROOT
- removed author test only build requires

* Sun Mar 23 2014 Sven Nierlein <sven.nierlein@consol.de> 6.06-1
- Specfile created
