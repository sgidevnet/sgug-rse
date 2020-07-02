Name:           perl-Email-Address-XS
Version:        1.04
Release:        8%{?dist}
Summary:        Parse and format RFC 2822 email addresses and groups
License:        (GPL+ or Artistic) and MIT
URL:            https://metacpan.org/release/Email-Address-XS
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALI/Email-Address-XS-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Provides:       bundled(dovecot)

%description
This module implements RFC 2822 parser and formatter of email addresses and
groups. It parses an input string from email headers which contain a list
of email addresses or a groups of email addresses (like From, To, Cc, Bcc,
Reply-To, Sender, ...). Also it can generate a string value for those
headers from a list of email addresses objects.

%prep
%setup -q -n Email-Address-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Email*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-2
- Perl 5.28 rebuild

* Mon Jun 11 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- 1.04 bump

* Fri Mar 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-1
- 1.02 bump

* Thu Oct 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump

* Tue Aug 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-1
- Initial release
