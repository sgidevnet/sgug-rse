Name:           dillo
Version:        3.0.5
Release:        6%{?dist}

Summary:        Very small and fast GUI web browser

License:        GPLv3+
URL:            http://www.dillo.org/
Source0:        http://www.dillo.org/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         dillo-openssl.patch
Patch100:       dillo.irixfixes.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
# BuildRequires:  gtk+-devel
BuildRequires:  perl-generators
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libpng-devel >= 1.2.0
BuildRequires:  libjpeg-devel = 6b
BuildRequires:  openssl-devel
BuildRequires:  libXft-devel
BuildRequires:  fltk-devel >= 1.3.0
BuildRequires:  gettext
BuildRequires:  autoconf automake

# #676710 dillo requires iso8859 fonts
Requires:       wget
Requires:       xorg-x11-fonts-ISO8859-1-100dpi, xorg-x11-fonts-ISO8859-1-75dpi
Provides:       webclient

%description
Dillo is a very small and fast web browser using GTK.
Currently: no frames,https,javascript.

%prep
%setup -q

%patch0 -p1 -b.dso
%patch100 -p1 -b .sgifixes

autoreconf -vif

%build
%configure --disable-dependency-tracking --enable-ipv6 --enable-ssl LIBS="-liconv"

make %{?_smp_mflags}

%install
%make_install
rm -f doc/Makefile*

%{__install} -d -m0755 $RPM_BUILD_ROOT/%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE1}

%{__install} -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/dillo.png

# included with doc
rm -fr $RPM_BUILD_ROOT%{_datadir}/doc/dillo

# silence rpmlint and convert to utf8
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
cd doc
iconv -f iso8859-1 -t utf-8 Cache.txt > Cache.txt.conv && mv -f Cache.txt.conv Cache.txt
iconv -f iso8859-1 -t utf-8 Cookies.txt > Cookies.txt.conv && mv -f Cookies.txt.conv Cookies.txt

%files
%doc AUTHORS COPYING README ChangeLog doc
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_mandir}/man1/dillo.1.gz
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/dillo.png
%{_libdir}/%{name}

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Ranjan Maitra <aarem@fedoraproject.org>
- 3.0.5-2
- patched for dillo to use openssl 1.1 using patch provided  by Mattias Ellert <mattias.ellert AT physics DOT uu DOT se> 
- fixes BZ #1470354

* Fri Feb 17 2017 Ranjan Maitra <aarem@fedoraproject.org>
- 3.0.5-1
- version upgrade (BZ #1238891)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.4.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.0.4.1-2
- rebuild (fltk)

* Mon Dec 29 2014 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 3.0.4.1-1
- version upgrade (rhbz#1177439)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.4-1
- version upgrade (rhbz#1087222)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.0.3-2
- Perl 5.18 rebuild

* Thu May 30 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.3-1
- version upgrade

* Fri Feb 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.2-7
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.0.2-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.0.2-4
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.2-1
- version upgrade

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.0.1-2
- Rebuild for new libpng

* Sun Sep 25 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.1-1
- new upstream release

* Thu Sep 08 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.0-1
- upgrade to release

* Thu Sep 01 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.0-0.2.20110901
- current snapshot

* Thu Aug 04 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.0-0.1.20110804
- pull hg snapshot of dillo 3
- license change to GPLv3+
- build against latest fltk (rhbz#545273)
- fixes crash described in (rhbz#676710)

* Sun Feb 13 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.8.6-14
- require iso8859 fonts (#676710)
- clean up desktop files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 15 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.8.6-13
- fix desktop entries (#487771)

* Sun Apr 11 2010 Bruno Wolff III <bruno@wolff.to> - 0.8.6-12
- Fix DSO linking bug 564723
- Cleanup i18n area before trying to mv source there

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.8.6-11
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 0.8.6-8
- rebuild with new openssl

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0.8.6-7
- Rebuilt for gcc43

* Thu Dec 06 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.8.6-6
- fix desktop file(s) #413111

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.8.6-5
 - Rebuild for deps

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-4
- new license tag
- rebuild for buildid

* Tue Sep 12 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-3
- FE6 rebuild

* Tue Jul 04 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-2
- fix some more aspects of #187691 (package now contains dillo and dillo-i18n)
- fix #197370

* Sun Jun 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.6-1
- version upgrade
- fix #187691

* Mon Apr 17 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.5-3
- enable some options

* Wed Apr 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.5-2
- add i18n patch (#147381)

* Sat Mar 04 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.5-1
- reenable build
- version upgrade
- add dist

* Thu Apr 07 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.4-2
- Add icon, thanks to Robin Humble.

* Tue Jan 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.4-1
- Update to 0.8.4, fixes CAN-2005-0012 (#144953).

* Tue Sep  7 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.2-0.fdr.1
- Update to 0.8.2.
- Disable dependency tracking to speed up the build.

* Sun Jun 20 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.8.1-0.fdr.1
- 0.8.1 release

* Mon Apr 19 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.8.0-0.fdr.3
- Require wget for https support.

* Thu Feb 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.0-0.fdr.2
- Use "make install DESTDIR" instead of the %%makeinstall macro to avoid
  buildroot traces in installed files.
- Fix files list so that debuginfo files are not included in main package.
- Desktop entry improvements, split into external file.
- Include more docs.
- Convert spec file to UTF-8.

* Tue Feb 10 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.8.0-0.fdr.1
- 0.8.0 release
- Add patch to silence debug messages

* Mon Aug 25 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.7.3-0.fdr.2
- Include ChangeLog in docs.
- Use X-Fedora , not X-Red-Hat-Extra.
- Add proper BuildRequires,remove Requires, since they're automatically
  picked up.
- use config(noreplace) for dillorc.
- add Provides webclient.

* Sat Aug 23 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.7.3-0.fdr.1
- Initial RPM release for fedora
