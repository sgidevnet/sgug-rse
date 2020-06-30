Name:		perl-Image-ExifTool
Version:	11.85
Release:	2%{?dist}
License:	GPL+ or Artistic
Summary:	Utility for reading and writing image meta info
URL:		http://www.sno.phy.queensu.ca/%7Ephil/exiftool/
Source0:	http://www.sno.phy.queensu.ca/%7Ephil/exiftool/Image-ExifTool-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
# Run-time:
BuildRequires:	perl(Exporter)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(integer)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Optional run-time:
# Archive::Zip not used at tests
# Compress::Zlib not used at tests
# Cwd not used at tests
# Digest::MD5 not used at tests
# Digest::SHA not used at tests
BuildRequires:	perl(Encode)
# File::Basename not used at tests
# File::Glob not used at tests
# IO::File not used at tests
# IO::String not used at tests
# IO::Uncompress::Bunzip2 not used at tests
BuildRequires:	perl(POSIX)
# Time::HiRes not used at tests
BuildRequires:	perl(Time::Local)
# Win32::API not used on Linux
# Win32::API not used on Linux
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:	perl(FileHandle)

%description
ExifTool is a Perl module with an included command-line application for 
reading and writing meta information in image, audio, and video files. 
It reads EXIF, GPS, IPTC, XMP, JFIF, MakerNotes, GeoTIFF, ICC Profile, 
Photoshop IRB, FlashPix, AFCP, and ID3 meta information from JPG, JP2, 
TIFF, GIF, PNG, MNG, JNG, MIFF, EPS, PS, AI, PDF, PSD, BMP, THM, CRW, 
CR2, MRW, NEF, PEF, ORF, DNG, and many other types of images. ExifTool 
also extracts information from the maker notes of many digital cameras 
by various manufacturers including Canon, Casio, FujiFilm, GE, HP, 
JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson, 
Panasonic/Leica, Pentax/Asahi, Reconyx, Ricoh, Samsung, Sanyo, 
Sigma/Foveon, and Sony.

%prep
%setup -q -n Image-ExifTool-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*

# Somehow, these empty directories are getting created.
# Delete them.
rm -rf %{buildroot}%{perl_vendorlib}/*-linux-thread-multi

%check
make test

%files
%doc README Changes
%{_bindir}/exiftool
%{perl_vendorlib}/File/
%{perl_vendorlib}/Image/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 11.85-2
- Perl 5.32 rebuild

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 11.85-1
- update to latest stable (11.85)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Tom Callaway <spot@fedoraproject.org> - 11.70-1
- update to latest stable (11.70)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Tom Callaway <spot@fedoraproject.org> - 11.50-1
- update to latest stable (11.50)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 11.30-2
- Perl 5.30 rebuild

* Thu Mar  7 2019 Tom Callaway <spot@fedoraproject.org> - 11.30-1
- update to latest stable (11.30)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  1 2018 Tom Callaway <spot@fedoraproject.org> - 11.11-1
- update to latest stable (11.11)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 11.01-2
- Perl 5.28 rebuild

* Tue Jun 19 2018 Tom Callaway <spot@fedoraproject.org> - 11.01-1
- new stable (11.01)

* Thu Jun  7 2018 Tom Callaway <spot@fedoraproject.org> - 11.00-1
- new stable (11.00)

* Mon Mar  5 2018 Tom Callaway <spot@fedoraproject.org> - 10.80-1
- update to 10.80

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 10.55-2
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun  7 2017 Tom Callaway <spot@fedoraproject.org> - 10.55-1
- new stable (10.55)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 10.50-2
- Perl 5.26 rebuild

* Thu Apr 20 2017 Tom Callaway <spot@fedoraproject.org> - 10.50-1
- update to 10.50

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Tom Callaway <spot@fedoraproject.org> - 10.40-1
- update to 10.40

* Mon Nov 28 2016 Tom Callaway <spot@fedoraproject.org> - 10.36-1
- update to 10.36

* Mon Jun 13 2016 Tom Callaway <spot@fedoraproject.org> - 10.20-1
- update to 10.20

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 10.15-2
- Perl 5.24 rebuild

* Wed Apr 20 2016 Tom Callaway <spot@fedoraproject.org> - 10.15-1
- update to 10.15

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Tom Callaway <spot@fedoraproject.org> - 10.10-1
- update to 10.10

* Tue Sep 01 2015 Petr Pisar <ppisar@redhat.com> - 10.00-2
- Specify all dependencies (CPAN RT#106809)

* Tue Aug 18 2015 Tom Callaway <spot@fedoraproject.org> - 10.00-1
- update to 10.00 (new stable)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 9.90-2
- Perl 5.22 rebuild

* Mon Mar 16 2015 Tom Callaway <spot@fedoraproject.org> - 9.90-1
- update to 9.90 (new stable)

* Mon Nov 24 2014 Tom Callaway <spot@fedoraproject.org> - 9.76-1
- update to 9.76 (new stable)

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 9.70-2
- Perl 5.20 rebuild

* Wed Sep  3 2014 Tom Callaway <spot@fedoraproject.org> - 9.70-1
- update to 9.70 (new stable)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 9.60-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 9.60-1
- update to 9.60 (new stable)

* Mon Jan 20 2014 Tom Callaway <spot@fedoraproject.org> - 9.46-1
- update to 9.46 (new stable)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 9.27-2
- Perl 5.18 rebuild

* Wed Apr 17 2013 Tom Callaway <spot@fedoraproject.org> - 9.27-1
- update to 9.27 (stable, bugfix for 9.25)

* Mon Apr  8 2013 Tom Callaway <spot@fedoraproject.org> - 9.25-1
- update to 9.25 (stable)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Tom Callaway <spot@fedoraproject.org> - 9.13-1
- update to 9.13 (stable)

* Thu Jan  3 2013 Tom Callaway <spot@fedoraproject.org> - 9.12-1
- update to 9.12 (stable)

* Mon Nov  5 2012 Tom Callaway <spot@fedoraproject.org> - 9.04-1
- update to 9.04 (stable)

* Sat Aug 25 2012 Tom Callaway <spot@fedoraproject.org> - 9.01-1
- update to 9.01 (stable)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 8.90-2
- Perl 5.16 rebuild

* Tue May  1 2012 Tom Callaway <spot@fedoraproject.org> - 8.90-1
- update to 8.90

* Tue Apr  3 2012 Tom Callaway <spot@fedoraproject.org> - 8.85-1
- update to 8.85

* Fri Feb 10 2012 Tom Callaway <spot@fedoraproject.org> - 8.77-1
- update to 8.77

* Mon Jan  9 2012 Tom Callaway <spot@fedoraproject.org> - 8.75-1
- update to 8.75

* Mon Sep 26 2011 Tom Callaway <spot@fedoraproject.org> - 8.65-1
- update to 8.65

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 8.60-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 8.60-2
- Perl mass rebuild

* Tue Jun 28 2011 Tom Callaway <spot@fedoraproject.org> - 8.60-1
- update to 8.60

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 8.50-2
- Perl mass rebuild

* Thu Mar  3 2011 Tom Callaway <spot@fedoraproject.org> - 8.50-1
- update to 8.50

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 8.40-1
- update to 8.40

* Tue Jul 13 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 8.25-1
- update to 8.25

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 8.15-2
- Mass rebuild with perl-5.12.0

* Tue Mar 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> 8.15-1
- update to 8.15

* Mon Feb 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> 8.10-1
- update to 8.10

* Mon Dec  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> 8.00-1
- update to 8.00 (Production)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 7.67-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 7.67-1
- update to 7.67

* Tue Jan  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> 7.60-1
- update to 7.60

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> 7.51-1
- update to 7.51

* Wed May 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 7.25-2
- get rid of empty arch-specific directories (bz 448744)

* Fri Apr 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> 7.25-1
- update to 7.25

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 7.15-1
- 7.15
- rebuild for new perl

* Mon Oct 29 2007 Tom "spot" Callaway <tcallawa@redhat.com> 7.00-1
- 7.00

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.95-1
- 6.95
- license tag fix

* Wed Aug  1 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.94-1
- bump to 6.94

* Wed Feb 21 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.77-1
- bump to 6.77

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.69-1

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 6.40-1
- bump to 6.40

* Wed Aug  2 2006 Tom "spot" Callaway <tcallawa@redhat.com> 6.30-1
- bump to 6.30
 
* Tue Jul 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 6.26-2
- clean up the places where "use the" shows up in the code as a workaround

* Fri Jul  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 6.26-1
- bump to 6.26

* Mon Apr 24 2006 Tom "spot" Callaway <tcallawa@redhat.com> 6.15-1
- bump to 6.15

* Fri Mar 31 2006 Tom "spot" Callaway <tcallawa@redhat.com> 6.09-1
- bump to 6.09

* Tue Jan 10 2006 Tom "spot" Callaway <tcallawa@redhat.com> 5.89-1
- bump to 5.89

* Thu Aug  4 2005 Tom "spot" Callaway <tcallawa@redhat.com> 5.53-1
- initial package for Fedora Extras
