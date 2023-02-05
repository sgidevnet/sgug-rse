Name:           perl-Server-Starter
Version:        0.35
Release:        1%{?dist}
Summary:        Superdaemon for hot-deploying server programs
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Server-Starter
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Server-Starter-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# For the tests
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Test::TCP) >= 2.08
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::SharedFork)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%package start_server
Summary:        perl-Server-Starter start_server script
Requires:       perl-Server-Starter = %{version}-%{release}

%description
It is often a pain to write a server program that supports graceful
restarts, with no resource leaks. Server::Starter, solves the problem by
splitting the task into two. One is start_server, a script provided as a
part of the module, which works as a superdaemon that binds to zero or
more TCP ports, and repeatedly spawns the server program that actually
handles the necessary tasks (for example, responding to incoming
connections). The spawned server programs under Server::Starter call
accept(2) and handle the requests.

%description start_server
perl-Server-Starter's start_server script.

%prep
%setup -q -n Server-Starter-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files start_server
%{_bindir}/start_server
%{_mandir}/man1/start_server.*

%changelog
* Wed Sep 25 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.35-1
- Upstream update to 0.35.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.28 rebuild

* Thu Mar 01 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.34-1
- Upstream update to 0.34.
- Drop Server-Starter-0.33-Fix-building-on-Perl-without-.-in-INC.patch
  (Adopted by upstream).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-3
- Perl 5.26 rebuild

* Thu May 18 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.33-2
- Add Server-Starter-0.33-Fix-building-on-Perl-without-.-in-INC.patch
  (RHBZ#1451638).

* Wed Mar 01 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.33-1
- Upstream update.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.32-2
- Modernize spec.

* Wed Aug 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.32-1
- Upstream update.

* Sun Jul 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.31-1
- Upstream update.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.30-1
- Upstream update.

* Thu Jun 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.29-1
- Upstream update.

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-2
- Perl 5.22 rebuild

* Sat May 30 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.28-1
- Upstream update.

* Fri May 01 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.27-1
- Upstream update.
- Reflect upstream having dropped bundling modules.
- Reflect upstream having re-added LICENCE.
- Reflect upstream having switched to Module::Build.

* Tue Apr 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Upstream update.
- Rework spec.
- Remove bundled modules.
- Drop Fedora/RH-patches.

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-9
- Perl 5.20 mass

* Tue Sep 09 2014 Petr Pisar <ppisar@redhat.com> - 0.17-8
- Fix a race between t/06-autorestart.t and t/05-killolddelay-echod.pl
  (bug #1100158)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-7
- Perl 5.20 rebuild

* Thu Aug 21 2014 Petr Pisar <ppisar@redhat.com> - 0.17-6
- Fix t/05-killolddelay.t race (bug #1100158)

* Fri Aug 08 2014 Petr Pisar <ppisar@redhat.com> - 0.17-5
- Fix t/01-starter.t race (bug #1100158)

* Thu Jul 10 2014 Petr Pisar <ppisar@redhat.com> - 0.17-4
- Fix t/06-autorestart.t race (bug #1100158)

* Tue Jun 17 2014 Petr Pisar <ppisar@redhat.com> - 0.17-3
- Fix races in t/07-envdir.t test (bug #1100158)
- Load the environment directory just before restartin a server (bug #1100158)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 30 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.17-1
- Upstream update.

* Sun Nov 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.16-1
- Upstream update.

* Tue Aug 27 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.15-1
- Upstream update.
- Minor spec cleanup.

* Fri Aug 16 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.14-1
- Upstream update.
- BR: perl(Test::TCP) >= 2.00.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.12-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.12-1
- Upstream update.
- Modernize spec.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.11-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-2
- Add "Requires: perl-Server-Starter = %%{version}-%%{release}"
  per reviewer's demand.

* Thu Jan 20 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-1
- Upstream update.
- Reflect package review.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-2
- Put start_server into separate subpackage.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-1
- Initial Fedora package.
