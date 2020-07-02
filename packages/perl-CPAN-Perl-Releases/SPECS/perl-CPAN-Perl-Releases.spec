Name:           perl-CPAN-Perl-Releases
Version:        5.20200620
Release:        2%{?dist}
Summary:        Mapping Perl releases on CPAN to the location of the tarballs
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CPAN-Perl-Releases
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/CPAN-Perl-Releases-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%{?perl_default_filter}

%description
CPAN::Perl::Releases is a module that contains the mappings of all perl
releases that have been uploaded to CPAN to the authors/id/ path that the
tarballs reside in.

%prep
%setup -q -n CPAN-Perl-Releases-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README tools
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200620-2
- Perl 5.32 rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200620-1
- 5.20200620 bump

* Mon Jun 08 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200607-1
- 5.20200607 bump

* Tue Jun 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200601-1
- 5.20200601 bump

* Mon Jun 01 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200530-1
- 5.20200530 bump

* Mon May 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200524-1
- 5.20200524 bump

* Wed Apr 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200428-1
- 5.20200428 bump

* Mon Mar 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200320-1
- 5.20200320 bump

* Mon Mar 16 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200314-1
- 5.20200314 bump

* Mon Mar 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200229-1
- 5.20200229 bump

* Fri Feb 21 2020 Petr Pisar <ppisar@redhat.com> - 5.20200220-1
- 5.20200220 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.20200120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20200120-1
- 5.20200120 bump

* Thu Jan 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.20191220-1
- 5.20191220 bump

* Thu Nov 21 2019 Petr Pisar <ppisar@redhat.com> - 4.22-1
- 4.22 bump

* Mon Nov 11 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.20-1
- 4.20 bump

* Tue Oct 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.18-1
- 4.18 bump

* Mon Oct 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.16-1
- 4.16 bump

* Mon Sep 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.14-1
- 4.14 bump

* Tue Aug 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.12-1
- 4.12 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-1
- 4.10 bump

* Fri Jun 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.08-1
- 4.08 bump

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-2
- Perl 5.30 rebuild

* Mon May 27 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-1
- 4.06 bump

* Wed May 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-1
- 4.04 bump

* Mon May 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.02-1
- 4.02 bump

* Mon May 13 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.00-1
- 4.00 bump

* Tue Apr 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.98-1
- 3.98 bump

* Mon Apr 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.94-1
- 3.94 bump

* Thu Mar 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.92-1
- 3.92 bump

* Thu Feb 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.90-1
- 3.90 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.88-1
- 3.88 bump

* Wed Dec 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.86-1
- 3.86 bump

* Fri Nov 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.84-1
- 3.84 bump

* Wed Nov 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.82-1
- 3.82 bump

* Mon Oct 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.80-1
- 3.80 bump

* Tue Oct 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.78-1
- 3.78 bump

* Fri Sep 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.76-1
- 3.76 bump

* Tue Aug 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.74-1
- 3.74 bump

* Mon Jul 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.72-1
- 3.72 bump

* Mon Jul 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.70-1
- 3.70 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.68-2
- Perl 5.28 rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.68-1
- 3.68 bump

* Sat Jun 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.66-1
- 3.66 bump

* Wed Jun 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.64-1
- 3.64 bump

* Tue Jun 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.62-1
- 3.62 bump

* Thu Jun 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.60-1
- 3.60 bump

* Tue May 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.58-1
- 3.58 bump

* Mon Apr 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.56-1
- 3.56 bump

* Mon Apr 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.54-1
- 3.54 bump

* Tue Apr 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.52-1
- 3.52 bump

* Wed Mar 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.50-1
- 3.50 bump

* Wed Feb 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.48-1
- 3.48 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.46-1
- 3.46 bump

* Fri Dec 22 2017 Petr Pisar <ppisar@redhat.com> - 3.44-1
- 3.44 bump

* Tue Nov 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.42-1
- 3.42 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.40-1
- 3.40 bump

* Mon Sep 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.38-1
- 3.38 bump

* Thu Sep 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.36-1
- 3.36 bump

* Mon Sep 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.34-1
- 3.34 bump

* Tue Aug 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.32-1
- 3.32 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.30-1
- 3.30 bump

* Mon Jul 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.28-1
- 3.28 bump

* Mon Jul 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.26-1
- 3.26 bump

* Tue Jun 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.24-1
- 3.24 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.22-2
- Perl 5.26 rebuild

* Thu Jun 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.22-1
- 3.22 bump

* Wed May 31 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.20-1
- 3.20 bump

* Wed May 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.18-1
- 3.18 bump

* Fri May 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.16-1
- 3.16 bump

* Fri Apr 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.14-1
- 3.14 bump

* Tue Mar 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.12-1
- 3.12 bump

* Tue Feb 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.10-1
- 3.10 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.08-1
- 3.08 bump

* Mon Jan 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.06-1
- 3.06 bump

* Tue Jan 03 2017 Petr Pisar <ppisar@redhat.com> - 3.04-1
- 3.04 bump

* Wed Dec 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.02-1
- 3.02 bump

* Mon Nov 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.00-1
- 3.00 bump

* Fri Oct 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.98-1
- 2.98 bump

* Thu Oct 13 2016 Petr Pisar <ppisar@redhat.com> - 2.96-1
- 2.96 bump

* Thu Sep 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.94-1
- 2.94 bump

* Mon Aug 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.92-1
- 2.92 bump

* Mon Aug 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.90-1
- 2.90 bump

* Tue Jul 26 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.88-1
- 2.88 bump

* Thu Jul 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-1
- 2.84 bump

* Mon Jul 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.82-1
- 2.82 bump

* Tue Jun 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.80-1
- 2.80 bump

* Mon May 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.78-1
- 2.78 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.76-2
- Perl 5.24 rebuild

* Tue May 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.76-1
- 2.76 bump

* Thu May 05 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.74-1
- 2.74 bump

* Tue May 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.72-1
- 2.72 bump

* Mon May 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.70-1
- 2.70 bump

* Thu Apr 28 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.68-1
- 2.68 bump

* Mon Apr 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.66-1
- 2.66 bump

* Thu Apr 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.64-1
- 2.64 bump

* Mon Apr 11 2016 Petr Pisar <ppisar@redhat.com> - 2.62-1
- 2.62 bump

* Mon Mar 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.60-1
- 2.60 bump

* Mon Feb 22 2016 Petr Šabata <contyk@redhat.com> - 2.58-1
- 2.58 bump, updated for v5.23.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Petr Šabata <contyk@redhat.com> - 2.56-1
- 2.56 bump, updated for v5.23.7

* Tue Dec 22 2015 Petr Šabata <contyk@redhat.com> - 2.54-1
- 2.54 bump, updated for v5.23.6

* Tue Dec 15 2015 Petr Šabata <contyk@redhat.com> - 2.52-1
- 2.52 bump, updated for v5.22.1

* Wed Dec 09 2015 Petr Šabata <contyk@redhat.com> - 2.50-1
- 2.50 bump, updated for v5.22.1-RC3 and RC4

* Mon Nov 23 2015 Petr Šabata <contyk@redhat.com> - 2.46-1
- 2.46 bump, updated for v5.23.5 and v5.22.1-RC2

* Mon Nov 02 2015 Petr Pisar <ppisar@redhat.com> - 2.42-1
- 2.42 bump

* Wed Oct 21 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-1
- 2.40 bump, updated for v5.23.4

* Mon Sep 21 2015 Petr Šabata <contyk@redhat.com> - 2.38-1
- 2.38 bump, updated for v5.23.3

* Tue Sep 15 2015 Petr Šabata <contyk@redhat.com> - 2.36-1
- 2.36 bump, updated for v5.20.3

* Mon Aug 31 2015 Petr Šabata <contyk@redhat.com> - 2.34-1
- 2.34 bump, updated for v5.20.3-RC2

* Mon Aug 24 2015 Petr Šabata <contyk@redhat.com> - 2.32-1
- 2.32 bump, updated for v5.20.3-RC1 and v5.23.2

* Tue Jul 21 2015 Petr Šabata <contyk@redhat.com> - 2.28-1
- 2.28 bump, updated for v5.23.1

* Tue Jun 30 2015 Petr Šabata <contyk@redhat.com> - 2.26-1
- 2.26 bump

* Mon Jun 22 2015 Petr Šabata <contyk@redhat.com> - 2.24-1
- 2.24 bump, updated for v5.23.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-2
- Perl 5.22 rebuild

* Tue Jun 02 2015 Petr Šabata <contyk@redhat.com> - 2.22-1
- 2.22 bump, updated for v5.22.0

* Mon May 25 2015 Petr Šabata <contyk@redhat.com> - 2.18-1
- 2.18 bump, updated for v5.22.0-rc2

* Wed May 20 2015 Petr Šabata <contyk@redhat.com> - 2.16-1
- 2.16 bump, updated for v5.22.0-rc1

* Tue Apr 21 2015 Petr Šabata <contyk@redhat.com> - 2.14-1
- 2.14 bump, updated for v5.21.11

* Mon Mar 23 2015 Petr Šabata <contyk@redhat.com> - 2.12-1
- 2.12 bump, updated for v5.21.10

* Thu Mar 19 2015 Petr Šabata <contyk@redhat.com> - 2.10-1
- 2.10 bump, updated for v5.21.9

* Tue Feb 17 2015 Petr Šabata <contyk@redhat.com> - 2.08-1
- 2.08 bump, updated for v5.20.2

* Tue Feb 03 2015 Petr Šabata <contyk@redhat.com> - 2.06-1
- 2.06 bump, updates for v5.20.2-rc1 and v5.21.8

* Fri Jan 02 2015 Petr Šabata <contyk@redhat.com> - 2.02-1
- 2.02 bump, updates for v5.21.7

* Wed Dec 10 2014 Petr Šabata <contyk@redhat.com> - 2.00-1
- 2.00 bump, add XZ tarballs

* Tue Nov 25 2014 Petr Šabata <contyk@redhat.com> - 1.98-1
- 1.96 bump, updates for v5.21.6

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 1.96-1
- 1.96 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 10 2013 Iain Arnell <iarnell@gmail.com> 1.32-1
- update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.94-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.94-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 0.92-1
- update to latest upstream version

* Fri Oct 19 2012 Iain Arnell <iarnell@gmail.com> 0.76-1
- update to latest upstream version

* Fri Sep 07 2012 Iain Arnell <iarnell@gmail.com> 0.68-1
- update to latest upstream version

* Sat Aug 18 2012 Iain Arnell <iarnell@gmail.com> 0.66-1
- update to latest upstream version

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 0.62-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.58-2
- Perl 5.16 rebuild

* Tue May 29 2012 Iain Arnell <iarnell@gmail.com> 0.58-1
- update to latest upstream version

* Fri May 18 2012 Iain Arnell <iarnell@gmail.com> 0.52-1
- update to latest upstream version

* Sat May 12 2012 Iain Arnell <iarnell@gmail.com> 0.48-1
- update to latest upstream version

* Sun Mar 25 2012 Iain Arnell <iarnell@gmail.com> 0.46-1
- update to latest upstream version

* Tue Feb 21 2012 Iain Arnell <iarnell@gmail.com> 0.44-1
- update to latest upstream version

* Tue Feb 07 2012 Iain Arnell <iarnell@gmail.com> 0.42-2
- tweak BuildRequires following review

* Sat Feb 04 2012 Iain Arnell <iarnell@gmail.com> 0.42-1
- Specfile autogenerated by cpanspec 1.79.
