Name:           perl-Smart-Comments
Summary:        Comments that do more than just sit there
Epoch:          1
Version:        1.06
Release:        14%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Smart-Comments-%{version}.tar.gz
URL:            https://metacpan.org/release/Smart-Comments
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Simple) >= 0.8
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.99
BuildRequires:  perl(Text::Balanced) >= 2
BuildRequires:  perl(warnings)

# Drop the old tests subpackage
# Can be removed diromg F22 development cycle
Obsoletes:      %{name}-tests < 1:1.000004-1
Provides:       %{name}-tests = %{epoch}:%{version}-%{release}

%{?perl_default_filter}

%description
Smart comments provide an easy way to insert debugging and tracking code into
a program. They can report the value of a variable, track the progress of a
loop, and verify that particular assertions are true.

Best of all, when you're finished debugging, you don't have to remove them.
Simply commenting out the use Smart::Comments line turns them back into
regular comments. Leaving smart comments in your code is smart because if you
needed them once, you'll almost certainly need them again later.

%prep
%setup -q -n Smart-Comments-%{version}
perl -pi -e 's|^#!perl -T|#!%{_perl}|' t/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.06-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.06-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.06-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.06-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.06-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.06-1
- 1.06 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.000005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.000005-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.000005-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.000005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 1:1.000005-3
- Correct tests sub-package obsoleteness

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.000005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.000005-1
- 1.000005 bump

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:1.000004-2
- Perl 5.18 rebuild

* Mon Jul 01 2013 Petr Šabata <contyk@redhat.com> - 1:1.000004-1
- 1.000004 bump (new versioning scheme)
- Update source URL
- Drop the tests subpackage
- Modernize spec

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:1.0.4-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.0.4-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.0.4-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.0.4-2
- Mass rebuild with perl-5.12.0

* Sun Mar 14 2010 Chris Weyl <cweyl@alumni.drew.edu> 1:1.0.4-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (1.0.4)
- altered br on perl(Filter::Simple) (0 => 0.8)
- altered br on perl(Text::Balanced) (0 => 2)
- dropped old BR on perl(Test::Pod)
- dropped old BR on perl(Test::Pod::Coverage)
- added a new req on perl(Data::Dumper) (version 0)
- added a new req on perl(Filter::Simple) (version 0.8)
- added a new req on perl(List::Util) (version 0)
- added a new req on perl(Text::Balanced) (version 2)
- added a new req on perl(version) (version 0)

* Sat Feb 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 1:v1.0.3-6
- add perl_default_filter, etc
- PERL_INSTALL_ROOT => DESTDIR
- drop t/ from doc

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:v1.0.3-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:v1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:v1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:v1.0.3-2
Rebuild for new perl

* Sat Mar 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 1:v1.0.3-1
- update to v1.0.3
- update lic tag
- add epoch, to move away from the 1.000... representation of the version

* Tue Mar 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.000002-4
- be more explicit with core requires

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.000002-3
- bump for mass rebuild

* Sun Aug 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.000002-2
- bump for build & release

* Sun Aug 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.000002-1
- Initial spec file for F-E
