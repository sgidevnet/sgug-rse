Name:		perl-Data-Validate-IP
Version:	0.27
Release:	10%{?dist}
Summary:	Perl IP address validation routines

License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Data-Validate-IP
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-IP-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(base)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(NetAddr::IP) >= 4
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Socket)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Taint)
BuildRequires:	perl(warnings)

Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))


%description
This module collects IP address validation routines to make input validation,
and untainting easier and more readable.


%prep
%setup -q -n Data-Validate-IP-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-1
- 0.27 bump

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- 0.26 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.24 rebuild

* Thu Mar 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-1
- 0.25 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-1
- 0.24 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.18-3
- Perl 5.18 rebuild

* Fri Mar 01 2013 Normunds Neimanis <fedorapkg at rule.lv> 0.18-2
- Improved summary sentence

* Thu Feb 21 2013 Normunds Neimanis <fedorapkg at rule.lv> 0.18-1
- Initial package for Fedora
