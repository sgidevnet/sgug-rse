Name:           perl-JSON-XS
Summary:        JSON serializing/de-serializing, done correctly and fast
Epoch:          1
Version:        4.02
Release:        3%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/JSON-XS
Source0:        https://cpan.metacpan.org/modules/by-module/JSON/JSON-XS-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(common::sense)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(XSLoader)
# Script Runtime
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
#%%{?perl_default_subpackage_tests}

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast. To
reach the latter goal it was written in C.

%prep
%setup -q -n JSON-XS-%{version}

sed -i 's/\r//' t/*
perl -pi -e 's|^#!/opt/bin/perl|#!%{__perl}|' eg/*
perl -pi -e 's|^#!/opt/bin/perl|#!%{__perl}|' bin/*
chmod -c -x eg/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README eg/
%license COPYING
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_bindir}/*
%{_mandir}/man[13]/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.02-2
- Perl 5.30 rebuild

* Wed Mar  6 2019 Paul Howarth <paul@city-fan.org> - 1:4.02-1
- Update to 4.02

* Mon Feb 25 2019 Paul Howarth <paul@city-fan.org> - 1:4.01-1
- Update to 4.01

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Paul Howarth <paul@city-fan.org> - 1:4.0-1
- Update to 4.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.04-4
- Perl 5.28 rebuild

* Wed Feb 21 2018 Paul Howarth <paul@city-fan.org> - 1:3.04-3
- Specify all dependencies

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1:3.04-1
- Update to 3.04

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.03-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1:3.03-2
- Update to 3.03

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.02-2
- Perl 5.24 rebuild

* Fri Mar 11 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1:3.02-1
- Update to 3.02
- Add needed BuildRequires
- PAss NO_PACKLIST to Makefile.PL
- Use %%license macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.01-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.01-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 03 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1:3.01-1
- Update to 3.01

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1:2.34-2
- Perl 5.18 rebuild

* Sun May 26 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1:2.34-1
- Update to 2.34

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 02 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1:2.33-1
- Update to 2.33

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:2.32-2
- Perl 5.16 rebuild
- Specify all dependencies

* Thu Jan 12 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1:2.32-1
- Update to 2.32
- Clean up spec file

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:2.30-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1:2.30-1
- update

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:2.27-2
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Chris Weyl <cweyl@alumni.drew.edu> 1:2.27-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- added a new br on perl(common::sense) (version 0)
- added a new req on perl(common::sense) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:2.24-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 2.24-1
- auto-update to 2.24 (by cpan-spec-update 0.01)

* Thu Mar 26 2009 Chris Weyl <cweyl@alumni.drew.edu> - 2.2311-4
- Stripping bad provides of private Perl extension libs

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2311-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2311-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 2.2311-1
- update to 2.2311

* Sun Sep 07 2008 Chris Weyl <cweyl@alumni.drew.edu> 2.2222-1
- update to the increasingly silly version of 2.2222
- update files to include bin

* Wed Jun 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 2.21-1
- update to 2.21

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 2.2-1
- update to 2.2

* Sun Mar 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 2.01-1
- update to 2.x series before F9

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.52-3
Rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.52-2
- Autorebuild for GCC 4.3

* Wed Oct 17 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.52-1
- update to 1.52
- license tag update: GPL -> GPL+

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.43-2
- bump

* Thu Aug 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.43-1
- update to 1.43

* Fri Jun 01 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.22-1
- update to 1.22

* Mon May 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.21-3
- bump

* Mon May 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.21-2
- add eg/ to doc

* Sun May 13 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.21-1
- Specfile autogenerated by cpanspec 1.71.
