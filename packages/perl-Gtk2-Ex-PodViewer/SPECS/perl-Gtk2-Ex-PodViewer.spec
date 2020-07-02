Name:           perl-Gtk2-Ex-PodViewer
Version:        0.18
Release:        33%{?dist}
Summary:        Gtk2 widget for displaying Plain Old Documentation (POD)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Gtk2-Ex-PodViewer
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/Gtk2-Ex-PodViewer-%{version}.tar.gz
# Allow bulding the package without run-time depenencies because of no tests
Patch0:         Gtk2-Ex-PodViewer-0.18-Do-not-insist-on-run-time-dependencies-when-building.patch
# Remove "use lib" from podviewer, CPAN RT#115717
Patch1:         Gtk2-Ex-PodViewer-0.18-Do-not-search-modules-in-relative-paths.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# No tests exist
## Run-time:
# perl(base)
# perl(bytes)
# perl(Carp)
# perl(Data::Dumper)
# perl(Exporter)
# perl(File::Basename)
# perl(Gtk2)
# perl(Gtk2::Ex::Simple::List)
# perl(Gtk2::Gdk::Keysyms)
# perl(Gtk2::Pango)
# perl(IO::Scalar)
# perl(lib)
# perl(Pod::Parser)
# perl(Pod::Simple::Search)
# perl(vars)
## Optional run-time:
# perl(Locale::gettext)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Recommends:     perl(Locale::gettext)

%description
This is a Perl Gtk2 widget for displaying Plain Old Documentation (POD) files.

%prep
%setup -q -n Gtk2-Ex-PodViewer-%{version}
%patch0 -p1
%patch1 -p1
find . -type f -exec chmod a-x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test


%files
%doc README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-33
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-30
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-27
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-24
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 29 2016 Petr Pisar <ppisar@redhat.com> - 0.18-22
- Modernize spec file
- Remove "use lib" from podviewer (CPAN RT#115717)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-21
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-18
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-17
- Perl 5.20 rebuild

* Mon Jun 09 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-16
- Add missing BR:s (Address FTBFS, RHBZ #1106052).
- Modernize spec.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.18-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.18-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.18-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.18-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 06 2008 Bernard Johnson <bjohnson@symetrix.com> - 0.18-1
- v 0.18

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.17-4
Rebuild for new perl

* Thu May 03 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.17-3
- BR on perl(ExtUtils::MakeMaker) rather than perl

* Sun Mar 25 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.17-2
- use perl(...) style requires (bz #233767)

* Mon Mar 19 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.17-1
- initial release
