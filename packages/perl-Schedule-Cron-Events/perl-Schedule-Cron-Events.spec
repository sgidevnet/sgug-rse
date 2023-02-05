Name:           perl-Schedule-Cron-Events
Version:        1.96
Release:        1%{?dist}
Summary:        Take a line from a crontab and find out when events will occur
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Schedule-Cron-Events
# http://www.cpan.org/modules/by-module/Schedule/Schedule-Cron-Events-%%{version}.tar.gz
# is the original upstream source. Unfortunately Schedule-Cron-Events includes the file
# cron_event_predict.plx - being not covered by any of the license statements inside of
# the upstream tarball. And per Fedora Legal, we have to remove this file once upstream
# has clarified the licensing of this file. Cleaning sources can be simply done using:
#   tar zxvf Schedule-Cron-Events-<version>.tar.gz
#   rm Schedule-Cron-Events-<version>/cron_event_predict.plx
#   comment out some lines in Schedule-Cron-Events-1.93/Makefile.PL
#   tar cvfz Schedule-Cron-Events-<version>-noplx.tar.gz Schedule-Cron-Events-<version>
Source0:        Schedule-Cron-Events-%{version}-noplx.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Set::Crontab)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Given a line from a crontab, tells you the time at which cron will next run
the line, or when the last event occurred, relative to any date you choose.
The object keeps that reference date internally, and updates it when you
call nextEvent() or previousEvent() - such that successive calls will give
you a sequence of events going forward, or backwards, in time.

%prep
%setup -q -n Schedule-Cron-Events-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -delete
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%endif

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Feb 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-1
- 1.96 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.95-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.95-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.95-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.95-1
- 1.95 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Miroslav Suchý <msuchy@redhat.com> 1.94-1
- rebase to 1.94

* Thu Jun 18 2015 Miroslav Suchy <msuchy@redhat.com> 1.93-1
- rebase to 1.93

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-32
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-31
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.8-28
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.8-25
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.8-23
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.8-21
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.8-20
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.8-19
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Robert Scheck <robert@fedoraproject.org> 1.8-16
- removed not clearly licensed *.plx file (#483390 #c11)

* Thu Sep 11 2008 Miroslav Suchý <msuchy@redhat.com> 1.8-15
- add build requires ExtUtils::MakeMaker

* Wed Sep 10 2008 Miroslav Suchý <msuchy@redhat.com> 1.8-14
- fix mixed tab and space

* Thu Sep  4 2008 Miroslav Suchý <msuchy@redhat.com> 1.8-12
- add build requires

* Fri Aug 29 2008 Miroslav Suchý <msuchy@redhat.com> 1.8-2
- Specfile autogenerated by cpanspec 1.77.
