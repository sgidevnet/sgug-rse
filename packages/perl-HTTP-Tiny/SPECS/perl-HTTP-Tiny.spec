Name:           perl-HTTP-Tiny
Version:        0.076
Release:        439%{?dist}
Summary:        Small, simple, correct HTTP/1.1 client
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTTP-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/HTTP-Tiny-%{version}.tar.gz
# Check for write failure, bug #1031096, refused by upstream,
# <https://github.com/chansen/p5-http-tiny/issues/32>
Patch0:         HTTP-Tiny-0.070-Croak-on-failed-write-into-a-file.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Socket)
# IO::Socket::IP 0.32 is optional
# IO::Socket::SSL 1.56 is optional
BuildRequires:  perl(MIME::Base64)
# Mozilla::CA is optional
# Net::SSLeay 1.49 is an optional fall-back for IO::Socket::SSL
BuildRequires:  perl(Socket)
BuildRequires:  perl(Time::Local)
# Tests:
# Data::Dumper not used
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename) 
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::INET)
# IO::Socket::SSL 1.56 not needed
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
# Mozilla::CA not needed
# Net::SSLeay 1.49 not needed
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(bytes)
Requires:       perl(Carp)
Requires:       perl(Fcntl)
Recommends:     perl(IO::Socket::IP) >= 0.32
Recommends:     perl(IO::Socket::SSL) >= 1.56
Requires:       perl(MIME::Base64)
Recommends:     perl(Mozilla::CA)
Requires:       perl(Time::Local)

%description
This is a very simple HTTP/1.1 client, designed for doing simple GET requests
without the overhead of a large framework like LWP::UserAgent.

It is more correct and more complete than HTTP::Lite. It supports proxies
(currently only non-authenticating ones) and redirection. It also correctly
resumes after EINTR.

%prep
%setup -q -n HTTP-Tiny-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR='%{buildroot}'
%{_fixperms} '%{buildroot}'/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn eg README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.076-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.076-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.076-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Petr Pisar <ppisar@redhat.com> - 0.076-1
- 0.076 bump

* Tue Jul 31 2018 Petr Pisar <ppisar@redhat.com> - 0.074-1
- 0.074 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.070-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.070-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.070-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.070-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.070-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.070-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Petr Pisar <ppisar@redhat.com> - 0.070-1
- 0.070 bump

* Mon Sep 26 2016 Petr Pisar <ppisar@redhat.com> - 0.068-1
- 0.068 bump

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 0.064-1
- 0.064 bump

* Tue Aug 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-3
- Avoid loading optional modules from default . (CVE-2016-1238)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-2
- Perl 5.24 rebuild

* Wed May 04 2016 Petr Pisar <ppisar@redhat.com> - 0.058-1
- 0.058 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.056-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.056-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.056-2
- Perl 5.22 rebuild

* Tue May 19 2015 Petr Pisar <ppisar@redhat.com> - 0.056-1
- 0.056 bump

* Mon Feb 02 2015 Petr Pisar <ppisar@redhat.com> - 0.054-1
- 0.054 bump

* Mon Dec 15 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.053-1
- 0.053 bump

* Fri Nov 21 2014 Petr Pisar <ppisar@redhat.com> - 0.051-1
- 0.051 bump

* Wed Sep 24 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-1
- 0.050 bump

* Wed Sep 10 2014 Petr Pisar <ppisar@redhat.com> - 0.049-1
- 0.049 bump

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.048-2
- Perl 5.20 rebuild

* Fri Aug 22 2014 Petr Pisar <ppisar@redhat.com> - 0.048-1
- 0.048 bump

* Wed Jul 30 2014 Petr Pisar <ppisar@redhat.com> - 0.047-1
- 0.047 bump

* Tue Jul 29 2014 Petr Pisar <ppisar@redhat.com> - 0.046-1
- 0.046 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Petr Pisar <ppisar@redhat.com> - 0.043-1
- 0.043 bump

* Wed Feb 19 2014 Petr Pisar <ppisar@redhat.com> - 0.042-1
- 0.042 bump

* Thu Nov 28 2013 Petr Pisar <ppisar@redhat.com> - 0.039-1
- 0.039 bump

* Wed Nov 27 2013 Petr Pisar <ppisar@redhat.com> - 0.038-2
- Croak on failed write into a file (bug #1031096)
- Do not use already existing temporary files (bug #1031096)

* Tue Nov 19 2013 Petr Pisar <ppisar@redhat.com> - 0.038-1
- 0.038 bump

* Tue Oct 29 2013 Petr Pisar <ppisar@redhat.com> - 0.037-1
- 0.037 bump

* Thu Sep 26 2013 Petr Pisar <ppisar@redhat.com> - 0.036-1
- 0.036 bump

* Wed Sep 11 2013 Petr Pisar <ppisar@redhat.com> - 0.035-1
- 0.035 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.034-2
- Link minimal build-root packages against libperl.so explicitly

* Mon Jul 01 2013 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Mon Jun 24 2013 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Fri Jun 21 2013 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Thu Jun 20 2013 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump

* Fri Jun 14 2013 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Thu Apr 18 2013 Petr Pisar <ppisar@redhat.com> - 0.029-1
- 0.029 bump

* Fri Mar 15 2013 Petr Pisar <ppisar@redhat.com> 0.028-1
- Specfile autogenerated by cpanspec 1.78.
