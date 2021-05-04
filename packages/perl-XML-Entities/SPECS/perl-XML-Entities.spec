%global perlname XML-Entities

Name:      perl-XML-Entities
Version:   1.0002
Release:   12%{?dist}
Summary:   Decode strings with XML entities

License:   GPL+ or Artistic
URL:       https://metacpan.org/release/XML-Entities
Source:    https://cpan.metacpan.org/authors/id/S/SI/SIXTEASE/%{perlname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(open)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Parser) perl(LWP::Simple) perl(Test::More)

Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}


%description
This module provides a mapping from the standard XML entities to their Unicode
characters. A function for decoding is provided. The mapping can be generated
from a DTD file with entity definitions.


%prep
%setup -q -n %{perlname}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';' -print
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';' -print
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%{_mandir}/man3/XML*
%{_mandir}/man3/download-entities.*
%{_mandir}/man1/download-entities.*
%{_bindir}/download-entities.pl
%{perl_vendorlib}/XML


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0002-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0002-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0002-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0002-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0002-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Remi Collet <remi@fedoraproject.org> - 1.0002-1
- update to 1.0002 (cleanup only)

* Mon Jun 22 2015 Remi Collet <remi@fedoraproject.org> - 1.0001-1
- update to 1.0001 (doc only)
- add BR perl(open)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0000-13
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0000-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.0000-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.0000-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.0000-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0000-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Aug 30 2010 Remi Collet <Fedora@famillecollet.com> 1.0000-1
- update to 1.000 
- remove Source1 as Entities are now shipped with the module itself

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0307-2
- Mass rebuild with perl-5.12.0

* Sat Jan 09 2010 Remi Collet <Fedora@famillecollet.com> 0.0307-1
- update to 0.0307

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 10 2008 Remi Collet <Fedora@famillecollet.com> 0.03-1
- update to 0.03

* Fri Apr 04 2008 Remi Collet <Fedora@famillecollet.com> 0.02-3
- enable test in all distro 
  (known to fail on EL4, must work on this issue)

* Thu Apr 03 2008 Remi Collet <Fedora@famillecollet.com> 0.02-2
- comment from review (#436611)

* Sat Mar  8 2008 Remi Collet <Fedora@famillecollet.com> 0.02-1
- initial spec

