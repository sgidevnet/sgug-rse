%global cpan_name MogileFS-Utils

Name:           perl-%{cpan_name}
Version:        2.30
Release:        9%{?dist}
Summary:        Utilities for MogileFS
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# These listed in META.yml are needed at run-time only, but no test loads them:
# perl(MogileFS::Client) >= 1.16
# perl(Compress::Zlib)
# perl(LWP::Simple)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(MogileFS::Client) >= 1.16

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MogileFS::Client\\)$

%description
Utilities for the MogileFS distributed storage system.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make %{?_smp_mflags} pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make %{?_smp_mflags} test

%files
%doc Changes
%{perl_vendorlib}/MogileFS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-1
- 2.30 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-2
- Perl 5.22 rebuild

* Fri Dec 19 2014 Petr Šabata <contyk@redhat.com> - 2.29-1
- 2.29 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.28-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Petr Pisar <ppisar@redhat.com> - 2.28-1
- 2.28 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.27-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Petr Pisar <ppisar@redhat.com> - 2.27-1
- 2.27 bump

* Wed Oct 24 2012 Petr Pisar <ppisar@redhat.com> - 2.26-3
- Parallelize all make runs

* Thu Oct 18 2012 Petr Pisar <ppisar@redhat.com> - 2.26-2
- Modernize spec file

* Tue Aug 14 2012 Petr Pisar <ppisar@redhat.com> - 2.26-1
- 2.26 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 2.25-2
- Perl 5.16 rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 2.25-1
- 2.25 bump

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 2.24-1
- 2.24 bump

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.23-2
- Perl 5.16 rebuild

* Mon Apr 02 2012 Petr Pisar <ppisar@redhat.com> - 2.23-1
- 2.23 bump

* Mon Jan 30 2012 Petr Pisar <ppisar@redhat.com> - 2.22-1
- 2.22 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Petr Pisar <ppisar@redhat.com> - 2.21-1
- 2.21 bump
- Remove RPM 4.8 filtering

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 2.20-3
- RPM 4.9 dependency filtering added

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.20-2
- Perl mass rebuild

* Wed Jul 13 2011 Petr Pisar <ppisar@redhat.com> - 2.20-1
- 2.20 bump
- Clean up spec file
- Correct description
- Consolidate dependencies

* Wed Feb 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.19-1
- Upstream released new version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.16-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Jun 25 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.16-1
- Upstream released new version

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.12-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.12-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.12-2
Rebuild for new perl

* Thu Aug 09 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.12-1
- Upstream released new version
* Wed Jun 20 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.11-1
- Initial import
