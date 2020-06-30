Name:       perl-Text-PDF
Version:    0.31
Release:    12%{?dist}
# lib/Text/PDF.pm -> GPL+ or Artistic
License:    GPL+ or Artistic
Summary:    Module for manipulating PDF files
Source:     https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Text-PDF-%{version}.tar.gz
Patch0:     Text-PDF-0.29-formats.patch
Url:        https://metacpan.org/release/Text-PDF
Requires:   perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
BuildArch:  noarch

BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Simple)
Requires:      pdf-tools = %{version}-%{release}

%{?perl_default_filter}

%description
This module allows interaction with existing PDF files directly. It
includes various tools:

    pdfbklt   - make booklets out of existing PDF files
    pdfrevert - remove edits from a PDF file
    pdfstamp  - stamp text on each page of a PDF file

%package -n pdf-tools
License:    GPL+ or Artistic
Summary:    Manipulate PDF files
Requires:   %{name} = %{version}-%{release}

%description -n pdf-tools
This package allows existing PDF files to be modified; and includes various
tools:

    pdfbklt   - make booklets out of existing PDF files
    pdfrevert - remove edits from a PDF file
    pdfstamp  - stamp text on each page of a PDF file

%prep
%setup -q -n Text-PDF-%{version}
find . -type f -exec chmod -c -x     {} ';'
sed -i 's/\r//' examples/CD.CFG
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc readme.txt examples/
%license LICENSE
%{perl_vendorlib}/Text*
%{_mandir}/man3/Text*.3*

%files -n pdf-tools
%doc readme.txt
%{_bindir}/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 27 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.31-1
- Update to 0.31
- Add perl default filter
- Pass NO_PACKLIST=1 to Makefile.PL
- Use %%license macro
- Tighten file listing

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.29a-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.29a-17
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.29a-16
- Perl 5.20 rebuild

* Wed Jun 18 2014 Petr Šabata <contyk@redhat.com> - 0.29a-15
- Support A0-A5 paper sizes (#1105775)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.29a-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.29a-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.29a-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.29a-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.29a-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.29a-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.29a-1
- submission
- add pdf-tools subpackage

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.29a-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

