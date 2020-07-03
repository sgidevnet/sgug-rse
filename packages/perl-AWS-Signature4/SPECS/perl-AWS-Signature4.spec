Name:           perl-AWS-Signature4
Version:        1.02
Release:        11%{?dist}
Summary:        Create a version4 signature for Amazon Web Services

License:        GPL+ or Artistic 2.0
URL:            https://metacpan.org/release/AWS-Signature4
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/AWS-Signature4-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::SHA) >= 5.47
BuildRequires:  perl(POSIX)
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Digest::SHA) >= 5.47
Requires:       perl(URI) >= 1.59

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Digest::SHA|URI)\\)$

%description
This module implement's Amazon Web Service's Signature version 4
(http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).


%prep
%setup -q -n AWS-Signature4-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test


%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-11
- Perl 5.32 rebuild

* Tue Mar 10 2020 Petr Pisar <ppisar@redhat.com> - 1.02-10
- Specify all dependencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jul 29 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.02-2
- initial package 
- fix duplicate BuildRequires issue
- fix macro-in-comment issue
