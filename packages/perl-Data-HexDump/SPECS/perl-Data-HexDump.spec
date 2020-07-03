Name:           perl-Data-HexDump
Version:        0.02
Release:        35%{?dist}
Summary:        Hexadecimal Dumper
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-HexDump
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-HexDump-%{version}.tar.gz
Patch0:         Data-HexDump-0.02-no-lib.patch
Patch1:         Data-HexDump-0.02-test-warnings.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
# (no additional dependencies)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Dump in hexadecimal the content of a scalar. The result is returned in a
string. Each line of the result consists of the offset in the source in the
leftmost column of each line, followed by one or more columns of data from
the source in hexadecimal. The rightmost column of each line shows the
printable characters (all others are shown as single dots).

%prep
%setup -q -n Data-HexDump-%{version}

# Avoid use of 'use lib' in shipped code (CPAN RT#123225)
%patch0

# Fix test warnings about pack 'c' (CPAN RT#123226)
%patch1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

# Rename binary not to conflict with util-linux (CPAN RT#123224)
mv %{buildroot}%{_bindir}/hexdump %{buildroot}%{_bindir}/hexdump.pl

%check
make test

%files
%doc README
%{_bindir}/hexdump.pl
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::HexDump.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-35
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-32
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-29
- Perl 5.28 rebuild

* Sat Mar 17 2018 Paul Howarth <paul@city-fan.org> - 0.02-28
- Fix typo in Summary
- Avoid use of 'use lib' in shipped code (CPAN RT#123225)
- Fix test warnings about pack 'c' (CPAN RT#123226)
- Clean up
  - Make %%files list more explicit
  - Drop %%defattr, redundant since rpm 4.4
  - Don't need to remove empty directories from the buildroot
  - Use %%{_fixperms} macro rather than our own chmod incantation
  - Simplify find command using -delete
  - Specify all build requirements
  - Avoid use of macros for basic commands
  - Drop explicit buildroot cleaning in %%install
  - Drop explicit %%clean section
  - Drop legacy Group: and BuildRoot: tags
  - Use DESTDIR rather than PERL_INSTALL_ROOT

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-25
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-23
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-20
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-19
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.02-16
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.02-13
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.02-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.02-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-4
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-3.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 0.02-3
- FE6 Rebuild

* Thu Mar 30 2006 Andreas Thienemann <andreas@bawue.net> 0.02-2
- Fixed review showstoppers

* Thu Mar 30 2006 Andreas Thienemann <andreas@bawue.net> 0.02-1
- Cleaned up for FE
- Specfile autogenerated by cpanspec 1.64.
