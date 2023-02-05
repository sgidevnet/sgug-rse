%global base_version 2.21
Name:           perl-threads
Epoch:          1
Version:        2.22
Release:        439%{?dist}
Summary:        Perl interpreter-based threads
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/threads
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDHEDDEN/threads-%{base_version}.tar.gz
# Unbundled from perl 5.28.0
Patch0:         threads-2.21-Upgrade-to-2.22.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(overload)
BuildRequires:  perl(XSLoader)
# Tests only:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads::shared)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)

%{?perl_default_filter}

%description
Since Perl 5.8, thread programming has been available using a model called
interpreter threads which provides a new Perl interpreter for each thread,
and, by default, results in no data or state information being shared
between threads.

(Prior to Perl 5.8, 5005threads was available through the "Thread.pm" API.
This threading model has been deprecated, and was removed as of Perl 5.10.0.)

%prep
%setup -q -n threads-%{base_version}
%patch0 -p1
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/threads*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.22-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.22-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.22-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.22-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.22-416
- Upgrade to 2.22 as provided in perl-5.28.0
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Petr Pisar <ppisar@redhat.com> - 1:2.21-1
- 2.21 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.16-2
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Petr Pisar <ppisar@redhat.com> - 1:2.16-1
- 2.16 bump

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.15-393
- Perl 5.26 rebuild

* Mon Feb 27 2017 Petr Pisar <ppisar@redhat.com> - 1:2.15-1
- 2.15 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Petr Pisar <ppisar@redhat.com> - 1:2.12-1
- 2.12 bump

* Mon May 23 2016 Petr Pisar <ppisar@redhat.com> - 1:2.09-1
- 2.09 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.08-3
- Perl 5.24 rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.08-2
- Perl 5.24 rebuild

* Tue May 17 2016 Petr Pisar <ppisar@redhat.com> - 1:2.08-1
- 2.08 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.07-365
- Increase release to favour standalone package

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 1:2.07-1
- 2.07 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Petr Pisar <ppisar@redhat.com> - 1:2.02-1
- 2.02 bump

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.01-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.01-2
- Perl 5.22 rebuild

* Fri Mar 13 2015 Petr Pisar <ppisar@redhat.com> - 1:2.01-1
- 2.01 bump

* Mon Mar 09 2015 Petr Pisar <ppisar@redhat.com> - 1:1.99-1
- 1.99 bump

* Fri Mar 06 2015 Petr Pisar <ppisar@redhat.com> - 1:1.98-1
- 1.98 bump

* Thu Mar 05 2015 Petr Pisar <ppisar@redhat.com> - 1:1.97-1
- 1.97 bump

* Wed Sep 10 2014 Petr Pisar <ppisar@redhat.com> - 1:1.96-1
- 1.96 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.92-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Petr Pisar <ppisar@redhat.com> - 1:1.92-1
- 1.92 bump

* Wed Oct 02 2013 Petr Pisar <ppisar@redhat.com> - 1:1.89-1
- 1.89 bump

* Tue Sep 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.87-6
- Update dependencies

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.87-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.87-4
- Link minimal build-root packages against libperl.so explicitly

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.87-3
- Perl 5.18 rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.87-2
- Perl 5.18 rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.87-1
- Increase epoch to compete with perl.spec

* Mon Jul 01 2013 Petr Pisar <ppisar@redhat.com> - 1.87-2
- Specify all dependencies

* Thu May 30 2013 Petr Pisar <ppisar@redhat.com> - 1.87-1
- 1.87 bump

* Tue Apr 30 2013 Petr Pisar <ppisar@redhat.com> - 1.86-243
- Increase release number to supersede perl sub-package (bug #957931)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-242
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 01 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.86-241
- Update dependencies.
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.86-240
- bump release to override sub-package from perl.spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.86-3
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Petr Pisar <ppisar@redhat.com> - 1.86-1
- 1.86 bump

* Tue Sep 06 2011 Petr Pisar <ppisar@redhat.com> - 1.85-1
- 1.85 bump

* Tue Aug 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.83-4
- change path on vendor, so our debuginfo are not conflicting with
  perl core debuginfos

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.83-3
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.83-2
- Perl 5.14 mass rebuild

* Tue Apr 26 2011 Petr Pisar <ppisar@redhat.com> - 1.83-1
- 1.83 bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Petr Pisar <ppisar@redhat.com> - 1.82-1
- 1.82 bump

* Wed Oct 06 2010 Petr Pisar <ppisar@redhat.com> - 1.81-1
- 1.81 bump

* Fri Oct 01 2010 Petr Pisar <ppisar@redhat.com> 1.79-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
