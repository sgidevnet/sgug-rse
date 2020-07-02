Name:           perl-Pod-PseudoPod-LaTeX
Version:        1.20190729
Release:        3%{?dist}
Summary:        Pod::PseudoPod::LaTeX Perl module
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-PseudoPod-LaTeX
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-PseudoPod-LaTeX-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(IO::String)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::PseudoPod) >= 0.15
BuildRequires:  perl(Test::More) >= 0.60
Requires:       perl(Pod::PseudoPod) >= 0.15
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

# The patch changes 'Verbatim' to 'verbatim' in:
#   lib/Pod/PseudoPod/LaTeX.pm
#   t/sections.t
#
Patch0:         Pod-PseudoPod-LaTeX-1.20190729.patch

%description
This module is a Pod::PseudoPod subclass, itself a Pod::Simple subclass. This
means that this is a full-fledged POD parser.

%prep
%setup -q -n Pod-PseudoPod-LaTeX-%{version}
%patch0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT%{_bindir}/ppod2latex

%check
make test

%files
%doc Changes dist.ini LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man1/ppod2latex.1.gz
%{_mandir}/man3/Pod::PseudoPod::LaTeX.3pm.gz
%{_bindir}/ppod2latex

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20190729-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20190729-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 1.20190729-1
- Update to 1.20190729
- Add corresponding patch for changing Verbatim to verbatim (lowercase)
- Add man page for section 1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20110710-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20110710-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20110710-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20110710-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.20110710-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20110710-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20110710-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20110710-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20110710-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.20110710-6
- Perl 5.24 rebuild

* Sat Feb 13 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.20110710-5
- Add patch to fix verbatim uppercace problem and quote curly braces in tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20110710-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20110710-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.20110710-2
- Perl 5.22 rebuild

* Mon Mar 23 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 1.20110710-1
- update to 1.20110710
- changed from "perl Build.PL" to "perl Makefile.PL" (perl(ExtUtils::MakeMaker))

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-14
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.000-11
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.000-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.000-6
- Perl mass rebuild

* Thu Jan 27 2011 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.000-5
- rebuild with perl-5.12.3

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.000-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.000-3
- Mass rebuild with perl-5.12.0

* Fri Jan 22 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> 1.000-2
- changed back to share the ownership of the directorys Pod and Pod/PseudoPod
- this is removed: BuildRequires: perl >= 1:v5.6.2

* Thu Jan 21 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> 1.000-1
- some wildcards are replaced by explizit file names
- scripts directory removed from document files
- ppod2latex added to files section
- the description needed correction
- Specfile autogenerated by cpanspec 1.78.
