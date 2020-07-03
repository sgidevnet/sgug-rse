Name:           perl-CSS-DOM
Version:        0.17
Release:        9%{?dist}
Summary:        Document Object Model for Cascading Style Sheets

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CSS-DOM
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPROUT/CSS-DOM-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Clone) >= 0.09
BuildRequires:  perl(Encode) >= 2.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)
# Dependencies not detected automatically:
Requires:       perl(Clone) >= 0.09
Requires:       perl(Encode) >= 2.10
Requires:  perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%{?perl_default_filter}

%description
This set of modules provides the CSS-specific interfaces described in
the W3C DOM recommendation.


%prep
%setup -q -n CSS-DOM-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/CSS/
%{_mandir}/man3/CSS::DOM*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.17-1
- Update to 0.17

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.16-1
- Update to 0.16
- Use NO_PACKLIST when creating Makefile
- Use %%license

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.15-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.15-1
- Update to 0.15
- Drop no longer needed patch
- Clean up spec file
- Add perl default filter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.14-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-6
- Perl mass rebuild

* Thu Feb 17 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.14-5
- Patch to avoid incorrect automatic dependencies with rpmbuild < 4.9.0-rc1.
- Bring back BuildRoot lost in previous commit.
- Fix perl(Encode) build dependency.

* Tue Feb 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-4
- remove filter, which is now useless with RPM4.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Dec 13 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.14-1
- Update to 0.14.

* Thu Aug 26 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.13-2
- Add explicit dependency on perl(Encode), not detected automatically.

* Tue Aug 24 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.13-1
- Update to 0.13.

* Fri Aug 20 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.11-1
- Update to 0.11.

* Fri Apr  2 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.10-1
- Update to 0.10.

* Sun Feb 21 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.09-1
- 0.09.

* Sun Jan 24 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.08-1
- First build.
