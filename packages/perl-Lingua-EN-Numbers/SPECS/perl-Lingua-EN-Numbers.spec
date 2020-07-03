Name:           perl-Lingua-EN-Numbers
Version:        2.03
Release:        14%{?dist}
Summary:        Turn "407" into "four hundred and seven", etc
License:        GPLv2
URL:            https://metacpan.org/release/Lingua-EN-Numbers
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-EN-Numbers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Lingua::EN::Numbers turns numbers into English text. It exports (upon
request) two functions, num2en and num2en_ordinal. Each takes a scalar
value and returns a scalar value. The return value is the English text
expressing that number; or if what you provided wasn't a number, then they
return undefined.

%prep
%setup -q -n Lingua-EN-Numbers-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Miro Hrončok <mhroncok@redhat.com> - 2.03-1
- New version 2.03 (#1279866)

* Thu Oct 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-4
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-2
- Perl 5.22 rebuild

* Wed Mar 18 2015 Miro Hrončok <mhroncok@redhat.com> - 2.02-1
- New version 2.02 (#1201279)

* Sun Feb 22 2015 Miro Hrončok <mhroncok@redhat.com> - 2.01-1
- New version 2.01 (#1195042)

* Fri Sep 26 2014 Miro Hrončok <mhroncok@redhat.com> - 2.00-1
- New version 2.00 (#1131066)

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Miro Hrončok <mhroncok@redhat.com> - 1.07-1
- New version 1.07 (#1101989)

* Mon Jan 13 2014 Miro Hrončok <mhroncok@redhat.com> - 1.06-1
- New version 1.06 (#1052193)

* Tue Nov 26 2013 Miro Hrončok <mhroncok@redhat.com> - 1.05-1
- New version 1.05 (#1034103)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.04-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 1.04-2
- Removed BRs provided by perl package
- Removed perl autofilter
- Added Test::More

* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 1.04-1
- Specfile autogenerated by cpanspec 1.78.
