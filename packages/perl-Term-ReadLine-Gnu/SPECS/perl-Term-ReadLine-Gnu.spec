Name:           perl-Term-ReadLine-Gnu
Version:        1.36
Release:        5%{?dist}
Summary:        Perl extension for the GNU Readline/History Library
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Term-ReadLine-Gnu
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  readline-devel >= 2.1
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# POSIX not used at tests
# Term::ReadLine not used at tests
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  expect
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(open)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
An implementation of Term::ReadLine using the GNU Readline/History Library.


%prep
%setup -q -n Term-ReadLine-Gnu-%{version}

%build
# Fix permissions and shebang paths at one shot
find . -type f -exec chmod 0664 '{}' \; \
       -exec sed 's,^#! */usr/local,#!%{_prefix},' -i '{}' \;
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT

%check
# Expect is used so that we get a PTY, as if we were
# in a real terminal, where readline works
expect -c '
	spawn make test
	expect eof
	exit [lindex [wait] 3]
'


%files
%doc README
%{_bindir}/perlsh
%{perl_vendorarch}/auto/Term*
%{perl_vendorarch}/Term*
%{_mandir}/man1/perlsh.1.gz
%{_mandir}/man3/Term*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-4
- Perl 5.30 rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.36-3
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.36-1
- Update to 1.36

* Fri Jul 20 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.35-11
- Correct previous changelog entry

* Fri Jul 20 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.35-10
- Add gcc as a build requirement (#1605419)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.35-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.35-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Paul Howarth <paul@city-fan.org> - 1.35-2
- Rebuild for readline 7

* Sun Nov 06 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.35-1
- Update to 1.35

* Sat Jun 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.34-1
- Update to 1.34

* Fri Jun 10 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.33-1
- Update to 1.33

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-2
- Perl 5.24 rebuild

* Mon Mar 07 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.31-1
- Update to 1.31, dropping no-longer-needed patch
- Use DESTDIR instead of PERL_INSTALL_ROOT
- Pass NO_PACKLIST to Makefile.PL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Petr Pisar <ppisar@redhat.com> - 1.28-2
- Specify all dependencies

* Fri Sep 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.28-1
- Update to 1.28

* Wed Sep 23 2015 Petr Pisar <ppisar@redhat.com> - 1.27-3
- Port Propagete-PerlIO_return_value_from_STORE.patch to 1.27 properly
  (bug #1264742)

* Wed Sep 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.27-2
- Re-add patch that was in fact not upstreamed

* Wed Sep 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.27-1
- Update to 1.27
- Remove upstreamed patch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-3
- Perl 5.22 rebuild

* Tue Feb 17 2015 Petr Pisar <ppisar@redhat.com> - 1.26-2
- Fix regression with Debug::Client (bug #1189459)

* Sun Feb 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.26-1
- Update to 1.26
- Tighten file listing

* Wed Dec 24 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.25-1
- Update to 1.25

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-6
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Petr Pisar <ppisar@redhat.com> - 1.24-4
- Revert removal of rl_executing_key and rl_executing_keyseq because readline
  library have been fixed (bugs #1112614)

* Wed Jul 16 2014 Petr Pisar <ppisar@redhat.com> - 1.24-3
- Cope with removed rl_executing_key and rl_executing_keyseq (bug #1112614)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.24-1
- Update to 1.24

* Sun Mar 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.23-1
- Update to 1.23

* Sun Mar 09 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.22-1
- Update to 1.22

* Sun Mar 02 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.21-1
- Update to 1.21

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.20-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 1.20-7
- Clean up spec file
- Add perl default filter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.20-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.20-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 1.20-1
- Bump to a later release

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.19-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.19-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 1.19-1
- New upstream release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 1.17a-4
- Remote the workaround introduced in previous change
- Disable Visual Bell test

* Tue Jul 01 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 1.17a-3
- Patch around rt#56500 perl bug hoping for better tomorrows

* Sat Jun 28 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 1.17a-2
- Run the test suite with a pseudo-terminal

* Fri Jun 27 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 1.17a-1
- Specfile autogenerated by cpanspec 1.75.
