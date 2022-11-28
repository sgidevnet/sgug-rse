Name:           perl-Spellunker
Version:        0.4.0
Release:        15%{?dist}
Summary:        Pure perl spelling checker implementation
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Spellunker
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Spellunker-v%{version}.tar.gz
# Remove /usr/bin/env from shebang
Patch0:         Spellunker-v0.4.0-Remove-usr-bin-env-from-shebang.patch
BuildArch:      noarch
# build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Simple::Methody)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(version)
# test only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Win32::Console::ANSI\\)$

%description
%{summary}, also usable as a library.

%prep
%setup -q -n Spellunker-v%{version}
%patch0 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{_bindir}/spellunker
%{_bindir}/spellunker-pod
%{perl_vendorlib}/Spellunker.pm
%{perl_vendorlib}/Spellunker/
%{perl_vendorlib}/Test/
%{perl_vendorlib}/auto/share/dist/Spellunker/
%{_mandir}/man1/spellunker.1*
%{_mandir}/man1/spellunker-pod.1*
%{_mandir}/man3/Spellunker.3*
%{_mandir}/man3/Test::Spellunker.3*

%changelog
* Tue Oct 06 2020  HAL <notes2@gmx.de> - 0.4.0-15
- compiles on Irix 6.5 with sgug-rse gcc 9.2. All tests pass.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-14
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Petr Pisar <ppisar@redhat.com> - 0.4.0-9
- Remove /usr/bin/env from shebang

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-2
- Perl 5.22 rebuild

* Tue Nov 18 2014 Paul Howarth <paul@city-fan.org> - 0.4.0-1
- Update to 0.4.0
  - Added more stopwords
  - Support &amp;
  - Show correct test line number if all_pod_files_spelling_ok fails
  - Documentation fixes
  - Test "bin" and "script" directories if "blib" does not exist
  - Allow git sha1 hash
  - Fix overly-recursive regex
  - Added clear_stopwords method
- Use %%license
- Make %%files list more explicit

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.3-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.2.3-2
- Perl 5.18 rebuild

* Wed Apr 24 2013 Petr Šabata <contyk@redhat.com> 0.2.3-1
- Specfile generated with help of cpanspec 1.78.
