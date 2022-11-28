Name:           perl-Modern-Perl
Version:        1.20190727
Release:        1%{?dist}
Summary:        Enable all of the features of Modern Perl with one command
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Modern-Perl
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 4:5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(feature)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.98
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Modern Perl often relies on the presence of several core and CPAN pragmas
and modules.  Wouldn't it be nice to use them all with a single command?

%prep
%setup -q -n Modern-Perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Modern/
%{perl_vendorlib}/odern/
%{_mandir}/man3/Modern::Perl.3*
%{_mandir}/man3/odern::Perl.3*

%changelog
* Sun Jul 28 2019 Paul Howarth <paul@city-fan.org> - 1.20190727-1
- Update to 1.20190727
  - Remove explicit autodie dependency (GH#11)
  - Add description of odern::Perl module (GH#12)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20190601-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20190601-2
- Perl 5.30 re-rebuild updated packages

* Sun Jun  2 2019 Paul Howarth <paul@city-fan.org> - 1.20190601-1
- Update to 1.20190601
  - Update for 2019
  - Reduce scope of lexical %%dates (CPAN RT#128406)
  - Support 'perl -Modern::Perl=20xx' (CPAN RT#96319)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20181021-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20181021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Paul Howarth <paul@city-fan.org> - 1.20181021-1
- Update to 1.20181021
  - Autogenerate META.json file (GH#7)
  - Remove Module::Build build dependency to make installation easier
- Switch to ExtUtils::MakeMaker flow

* Fri Sep 28 2018 Paul Howarth <paul@city-fan.org> - 1.20180928-1
- Update to 1.20180928
  - Skip tests for Perls without arraybase (GH#10)

* Mon Sep  3 2018 Paul Howarth <paul@city-fan.org> - 1.20180901-1
- Update to 1.20180901
  - Skip tests when PERL5OPT is set (GH#9)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20180701-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 1.20180701-2
- Perl 5.28 rebuild

* Mon Jul  2 2018 Paul Howarth <paul@city-fan.org> - 1.20180701-1
- Update to 1.20180701
  - Added support for Perl 5.26 and 5.28
- Drop legacy Group: tag

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.20170117-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20170117-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20170117-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20170117-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20170117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Paul Howarth <paul@city-fan.org> - 1.20170117-1
- Update to 1.20170117
  - Cleaned up test suite
  - Fixed Perl 5.25 failures (CPAN RT#114690)

* Mon Jan 16 2017 Paul Howarth <paul@city-fan.org> - 1.20170115-1
- Update to 1.20170115
  - Updated for 2017 release
  - Maybe 2016 should have supported 5.22, but given how long I waited... oops
  - Improved documentation about re-exporting (CPAN RT#109076)

* Thu Dec 29 2016 Paul Howarth <paul@city-fan.org> - 1.20161229-1
- Update to 1.20161229
  - Improved VERSION numbering (GH#5)

* Thu Oct  6 2016 Paul Howarth <paul@city-fan.org> - 1.20161005-1
- Update to 1.20161005
  - Updated for 2016 release
  - Added support for 5.24
- Add back in the package version, needed for provides

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.20150127-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20150127-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20150127-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.20150127-2
- Perl 5.22 rebuild

* Mon May 25 2015 Paul Howarth <paul@city-fan.org> - 1.20150127-1
- Update to 1.20150127
  - Updated for 2015 release
  - Added support for 5.20

* Mon May 25 2015 Paul Howarth <paul@city-fan.org> - 1.20140107-1
- Update to 1.20140107
  - Updated for 2014 release
  - Added support for 5.18
- Use %%license
- Classify buildreqs by usage
- Add runtime dependency on distribution prerequsite perl(autodie)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.20121103-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20121103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Paul Howarth <paul@city-fan.org> - 1.20121103-1.5
- Specify all dependencies
- Package upstream's LICENSE file
- Make %%files list more explicit
- Clean up for modern rpmbuild (deps can't be satisfied on EL-6)
- Don't use macros for commands

* Mon Oct 28 2013 Conrad Meyer <cemeyer@uw.edu> - 1.20121103-1
- Bump to latest version because 1.03 tarball disappeared from CPAN

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.03-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.03-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 16 2011 Conrad Meyer <konrad@tylerc.org> 1.03-1
- Specfile autogenerated by cpanspec 1.78.
