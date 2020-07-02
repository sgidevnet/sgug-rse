Name:		perl-Parallel-Runner
Version:	0.013
Release:	21%{?dist}
Summary:	An object to manage running things in parallel processes
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Parallel-Runner
Source0:	https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Parallel-Runner-%{version}.tar.gz
Patch0:		Parallel-Runner-0.013-T::E.patch
BuildArch:	noarch
BuildRequires:	perl-generators
BuildRequires:	perl(Carp)
BuildRequires:	perl(Child) >= 0.009
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Module::Build) >= 0.40
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
There are several other modules to do this, you probably want one of them. This
module exists as a super-specialized parallel task manager. You create the
object with a process limit and callbacks for what to do while waiting for a
free process slot, as well as a callback for what a process should do just
before exiting.

You must explicitly call $runner->finish() when you are done. If the runner is
destroyed before its children are finished, a warning will be generated and
your child processes will be killed, by force if necessary.

If you specify a maximum of 1 then no forking will occur, and run() will block
until the coderef returns. You can force a fork by providing a boolean true
value as the second argument to run(), which will force the runner to fork
before running the coderef; however, run() will still block until the child
exits.

%prep
%setup -q -n Parallel-Runner-%{version}

# Use Test::Exception rather than Text::Exception::LessClever
%patch0

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} $R%{buildroot}

%check
./Build test

%files
%doc CHANGES README
%{perl_vendorlib}/Parallel/
%{_mandir}/man3/Parallel::Runner.3pm*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-21
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.013-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-7
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.013-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 21 2013 Paul Howarth <paul@city-fan.org> - 0.013-4
- Switch to cpan.org upstream URLs
- Don't run the kill tests as they're prone to intermittent failures

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 0.013-3
- Sanitize for Fedora submission

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 0.013-2
- Enable the optional "kill" tests

* Wed Aug 14 2013 Paul Howarth <paul@city-fan.org> - 0.013-1
- Initial RPM version
