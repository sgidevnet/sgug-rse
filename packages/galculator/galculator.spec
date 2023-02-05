Name:           galculator
Version:        2.1.4
Release:        9%{?dist}
Summary:        GTK 3 based scientific calculator

License:        GPLv2+
URL:            http://galculator.mnim.org/
Source0:        http://galculator.mnim.org/downloads/galculator-%{version}.tar.bz2


BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  autoconf, automake, libtool

%description
A GTK 3 based scientific calculator with ordinary notation, reverse
polish notation, a formula entry mode, different number bases, and
different units of angular measure.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=${RPM_BUILD_ROOT} install
%find_lang %{name}

desktop-file-install --delete-original \
  %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
  %endif
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  --add-category "Calculator;GTK;" \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README COPYING THANKS
%attr(0755,root,root) %{_bindir}/galculator
%{_datadir}/applications/*galculator.desktop
%{_datadir}/galculator/
%{_datadir}/appdata/galculator.*
%{_datadir}/pixmaps/galculator.*
%{_datadir}/icons/hicolor/48x48/apps/galculator.*
%{_datadir}/icons/hicolor/scalable/apps/galculator.*
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Tomáš Mráz <tmraz@redhat.com> - 2.1.4-1
- new upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Tomáš Mráz <tmraz@redhat.com> - 2.1.3-1
- new upstream release

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.1.2-5
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.2-1
- new upstream release
- remove upstreamed gtk3-fix.patch
- make --vendor conditional so spec can be used for older releases, too

* Mon Feb 25 2013 Tomáš Mráz <tmraz@redhat.com> - 2.1-1
- new upstream release

* Fri Feb  8 2013 Tomas Mraz <tmraz@redhat.com> - 2.0.1-2
- drop --vendor from desktop-file-install call

* Wed Jan 16 2013 Tomas Mraz <tmraz@redhat.com> - 2.0.1-1
- new upstream release built against Gtk3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Tomas Mraz <tmraz@redhat.com> - 1.3.4-5
- Rebuilt for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Tomas Mraz <tmraz@redhat.com> - 1.3.4-3
- fix FTBFS due to linker changes (#564759)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  1 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun  4 2008 Tomas Mraz <tmraz@redhat.com> - 1.3.1-1
- upgrade to latest upstream

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.5.2-3
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Tomas Mraz <tmraz@redhat.com> - 1.2.5.2-2
- rebuild

* Mon Aug 13 2007 Tomas Mraz <tmraz@redhat.com> - 1.2.5.2-1
- upgrade to latest upstream
- fix build on new GTK 2

* Thu Sep  7 2006 Tomas Mraz <tmraz@redhat.com> - 1.2.5-5
- rebuilt for FC6

* Wed Feb 15 2006 Tomas Mraz <tmraz@redhat.com> - 1.2.5-4
- rebuilt for gcc changes

* Wed Feb  8 2006 Tomas Mraz <tmraz@redhat.com> - 1.2.5-3
- GladeXML is GObject and cannot be g_free-d (#178227)

* Thu Aug 18 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2.5-2
- rebuilt

* Mon Jul 25 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2.5-1
- Update to 1.2.5 (also fixes #162018).

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Nov 28 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 1.2.4-2
- Spec cleanup, bump release.

* Thu Oct 21 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 1.2.4-0.fdr.1
- 1.2.4.

* Fri May 28 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.2.3-0.fdr.1
- 1.2.3.

* Mon Apr 12 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.2.2-0.fdr.3
- BuildReq perl-XML-Parser.

* Mon Apr 12 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.2.2-0.fdr.2
- BuildReq intltool.

* Sat Apr 10 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.2.2-0.fdr.1
- Updated to 1.2.2.
- Using upstream desktop entry.
- Dropped icon.

* Tue Nov 11 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.4-0.fdr.1
- Updated to 1.1.4.

* Mon Sep 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.3-0.fdr.1
- Updated to 1.1.3.

* Tue Jul 08 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.2-0.fdr.1
- Updated to 1.1.2.

* Sat Jun 28 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.1-0.fdr.2
- Added BuildReq gettext.
- Added find_lang.
- Explicitly set permissions on install of icon and desktop entry.
- Changed path of Source0.

* Mon Jun 23 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.1-0.fdr.1
- Updated to 1.1.1.

* Sun Apr 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0-0.fdr.2
- Applied Spec Patch from Adrian Reber.

* Fri Apr 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0-0.fdr.1
- Fedorafied.

* Thu Oct 3 2002 Simon Floery <simon.floery@gmx.at>
- description update
