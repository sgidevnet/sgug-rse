Name:           perl-WWW-Twilio-API
Version:        0.21
Release:        10%{?dist}
Summary:        Accessing Twilio's REST API with Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/WWW-Twilio-API

Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCOTTW/WWW-Twilio-API-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(LWP::UserAgent) >= 2.03
BuildRequires:  perl(URI::Escape) >= 3.28

# Testing
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(List::Util) >= 1.29
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent) >= 2.03
Requires:       perl(URI::Escape) >= 3.28

%{?perl_default_filter}
%global __requires_exclude perl\\(LWP::UserAgent\\)|perl\\(URI::Escape\\)

%description
WWW::Twilio::API aims to make connecting to and making REST calls on the
Twilio API easy, reliable, and enjoyable.

%prep
%setup -q -n WWW-Twilio-API-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

# remove examples
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/WWW/Twilio/examples.pl

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md examples.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 10 2016 Denis Fateyev <denis@fateyev.com> - 0.21-1
- Update to 0.21 release

* Thu Aug 04 2016 Denis Fateyev <denis@fateyev.com> - 0.20-1
- Update to 0.20 release

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Denis Fateyev <denis@fateyev.com> - 0.18-2
- Improve package dependencies

* Mon Jan 11 2016 Denis Fateyev <denis@fateyev.com> - 0.18-1
- Initial release
