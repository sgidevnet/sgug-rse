Name:           perl-Unicode-Map
Version:        0.112
Release:        48%{?dist}
Summary:        Perl module for mapping charsets from and to utf16 unicode
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Unicode-Map
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWARTZ/Unicode-Map-0.112.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Script Runtime
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::Simple)
# Test Suite
# (no additional dependencies)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module converts strings from and to 2-byte Unicode UCS2
format. All mappings happen via 2 byte UTF16 encodings, not via 1 byte
UTF8 encoding. To convert between UTF8 and UTF16 use Unicode::String.
For historical reasons this module coexists with Unicode::Map8.
Please use Unicode::Map8 unless you need to care for >1 byte character
sets, e.g. chinese GB2312. Anyway, if you stick to the basic
functionality (see documentation) you can use both modules
equivalently.

%prep
%setup -q -n Unicode-Map-%{version}

# See bug 191387
echo '
# Add support for perl-Spreadsheet-ParseExcel
name:    CP932Excel
srcURL:  $SrcUnicode/VENDORS/MICSFT/WINDOWS/CP932.TXT
src:     $DestUnicode/VENDORS/MICSFT/WINDOWS/CP932.TXT
map:     $DestMap/MS/WIN/CP932Excel.map
' >> Map/REGISTRY

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -a -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%license COPYING
%doc Changes README
%{_bindir}/map
%{_bindir}/mirrorMappings
%{_bindir}/mkCSGB2312
%{_bindir}/mkmapfile
%{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/Unicode/
%{_mandir}/man1/map.1*
%{_mandir}/man1/mkmapfile.1*
%{_mandir}/man3/Unicode::Map.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-47
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-44
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-40
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-38
- Perl 5.24 rebuild

* Tue Apr 19 2016 Paul Howarth <paul@city-fan.org> - 0.112-37
- Classify buildreqs by usage
- Simplify find commands using -empty and -delete

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-34
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-33
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Paul Howarth <paul@city-fan.org> - 0.112-31
- Update spec file to more modern style
  - Specify all dependencies
  - Simplify %%build and %%install
  - No longer need to define %%perl_vendorarch
  - Use %%license
  - Make %%files list more explicit
  - Remove paragraph from %%description about this module disappearing when
    the perl core can handle Unicode

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.112-28
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.112-26
- Add perl default filter
- Remove no-longer-used macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.112-24
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.112-22
- Perl mass rebuild

* Fri Jul  8 2011 Paul Howarth <paul@city-fan.org> - 0.112-21
- Add perl(:MODULE_COMPAT_*) dependency

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.112-19
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.112-18
- Mass rebuild with perl-5.12.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.112-15
- fix build

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.112-14
- rebuild for new perl (again)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.112-13
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.112-12
- rebuild for new perl

* Thu Sep 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.112-11
- fix license tag (thanks Tom)

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.112-10
- rebuild for BuildID
- fix license tag (like perl itself)

* Mon Aug 13 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.112-9
- BR: perl-devel

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.112-8
- Add support for perl-Spreadsheet-ParseExcel (bug 191387)

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.112-7
- rebuild for FC5

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.112-0.fdr.5
- Reduce directory ownership bloat.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.112-0.fdr.4
- Install into vendor dirs.
- Specfile cleanup.

* Mon Jul  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.112-0.fdr.3
- Regenerate %%install section with cpanflute2.
- Improve %%description.

* Sun May  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.112-0.fdr.2
- Own more dirs.

* Fri Mar 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.112-0.fdr.1
- Update to current Fedora guidelines.

* Sun Mar  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.112-1.fedora.1
- First Fedora release.
