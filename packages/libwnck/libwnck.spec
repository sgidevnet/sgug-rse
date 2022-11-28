Summary: Window Navigator Construction Kit
Name: libwnck
Version: 2.31.0
Release: 13%{?dist}
URL: http://download.gnome.org/sources/libwnck/
#VCS: git:git://git.gnome.org/libwnck
Source0: http://download.gnome.org/sources/libwnck/2.31/%{name}-%{version}.tar.xz
License: LGPLv2+

Requires: startup-notification

BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  libXt-devel
BuildRequires:  libXres-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel


%description
libwnck (pronounced "libwink") is used to implement pagers, tasklists,
and other such things. It allows applications to monitor information
about open windows, workspaces, their names/icons, and so forth.

%package devel
Summary: Libraries and headers for libwnck
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build

%configure --disable-static --enable-introspection
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

# This package is merely compat for gtk2 apps, now.
# The binaries are shipped in libwnck3
rm -f $RPM_BUILD_ROOT%{_bindir}/wnckprop
rm -f $RPM_BUILD_ROOT%{_bindir}/wnck-urgency-monitor

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/Wnck-1.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/Wnck-1.0.gir
%doc %{_datadir}/gtk-doc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.31.0-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 30 2013 Kevin Fenzi <kevin@scrye.com> 2.31.0-1
- Update to 2.31.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.7-2
- Rebuilt for glibc bug#747377

* Wed Aug 31 2011 Matthias Clasen <mclasen@redhat.com> 2.30.7-1
- Update to 2.30.7

* Wed Jul 6 2011 Matthias Clasen <mclasen@redhat.com> 2.30.6-1
- Update to 2.30.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Ray Strode <rstrode@redhat.com> 2.30.4-2
- Drop wnck binaries since they're going to be shipped in libwnck3
- turn on introspection

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.4-1
- Update to 2.30.4

* Wed Sep 29 2010 jkeating - 2.30.3-4
- Rebuilt for gcc bug 634757

* Sat Sep 11 2010 Parag Nemade <paragn AT fedoraproject.org> 2.30.3-3
- Merge-review cleanup (#226059)

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.3-2
- Co-own /usr/share/gtk-doc (#604398)

* Thu Aug  5 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.3-1
- Update to 2.30.3

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.91-1
- Update to 2.29.91

* Thu Feb 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.6-1
- Update to 2.29.6

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Wed Sep  9 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-1
- Update to 2.27.4

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/libwnck/2.26/libwnck-2.26.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Feb 24 2009 Warren Togami <wtogami@redhat.com> - 2.25.91-2
- libwnck-devel Requires libxRes-devel (#485957)

* Tue Feb 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Tue Dec 16 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.3-1
- Update to 2.25.3

* Wed Oct 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Mon Aug  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Tue Jun 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-1
- Update to 2.21.91

* Mon Jan 28 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.5-1
- Update to 2.21.5

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2.1-1
- Update to 2.21.2.1

* Mon Nov 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-1
- Update to 2.21.2
- Drop upstreamed patch

* Mon Oct 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-3
- Fix a small oversight in the previous patch

* Mon Oct 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-2
- Don't crash if the X resource extension is missing (#343881)

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-1
- Update to 2.20.1 (crash fixes, translation updates)

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-1
- Update to 2.19.92 (translations)

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 2.19.90-2
- Rebuild for build id

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-1
- Update to 2.19.90

* Fri Aug  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-2
- Upate the license field

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-1
- Update to 2.19.6

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 2.19.5-3
- Rebuild for RH #249435

* Tue Jul 24 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-2
- Fix a crash on shutdown in the wnck-applet

* Sun Jul  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1
- Update to 2.19.5

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3.1-1
- Update to 2.19.3.1

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-2
- Require startup-notification-devel in the -devel package

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-1
- Update to 2.19.3
- Update viewport patch

* Sat May 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2
- Update patches

* Tue Apr 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-3
- Plug a small memory leak

* Wed Mar 28 2007 Kristian Høgsberg <krh@redhat.com> - 2.18.0-2
- Add compiz integration patches from GNOME #352383:
   - libwnck-2.18.0-appearance.patch
   - libwnck-2.18.0-viewport.patch
   - libwnck-2.18.0-above.patch

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.2-1
- Update to 2.16.2

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.16.0-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-3
- Make the pager visible when using compiz

* Mon Sep 11 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-2
- Avoid excessive icon geometry updates

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92
- Require pkgconfig in the -devel package

* Sat Aug 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-1.fc6
- Update to 2.15.91
- Don't ship static libraries

* Thu Aug 10 2006 Kristian Høgsberg <krh@redhat.com> - 2.15.90-1.fc5.aiglx
- Build for fc5 aiglx repo.

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.90-1.fc6
- Update to 2.15.90

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-1
- Update to 2.15.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.3-1.1
- rebuild

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Sat Jun 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-3
- More BuildRequires

* Sat May 20 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-2
- Fix missing BuildRequires (#129340)

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-1
- Update to 2.15.2

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Mon Feb 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.92-1
- Update to 2.13.92

* Mon Feb 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.91-1
- Update to 2.13.91

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.90-1
- Update to 2.13.90

* Mon Jan 16 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.5-1
- Update to 2.13.5

* Tue Jan 03 2006  Matthias Clasen <mclasen@redhat.com> - 2.13.4-1
- Update to 2.13.4

* Wed Dec 14 2005 Matthias Clasen <mclasen@redhat.com> - 2.13.3-1
- Update to 2.13.3

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Matthias Clasen <mclasen@redhat.com> - 2.13.2-1
- Update to 2.13.2

* Thu Oct  6 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1
- Update to 2.12.1

* Thu Sep  8 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> - 2.11.91-2
- rebuild for new cairo

* Tue Aug  9 2005 Ray Strode <rstrode@redhat.com> 2.11.91-1
- New upstream version

* Mon Jul 11 2005 Matthias Clasen <mclasen@redhat.com> 2.11.4-1
- New upstream version

* Mon May 30 2005 Elijah Newren  <newren@gamil.com> 2.10.0-4
- add support for urgent hint (#157271)

* Tue May 10 2005 Ray Strode <rstrode@redhat.com> 2.10.0-3
- fix some rendering issues with the last patch 

* Tue May 10 2005 Ray Strode <rstrode@redhat.com> 2.10.0-2
- add noticable glowing effect to task bar to counteract
  focus stealing prevention (bug #157285)

* Mon Mar 14 2005 Matthias Clasen <mclasen@redhat.com> 2.10.0-1
- Update to 2.10.0

* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 2.9.91-2
- Rebuild with gcc4

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> 2.9.91-1
- Update to 2.9.91

* Fri Jan 28 2005 Matthias Clasen <mclasen@redhat.com> 2.9.90-1
- Update to 2.9.90

* Tue Oct 12 2004 Mark McLoughlin <markmc@redhat.com> 2.8.1-1
- Update to 2.8.1

* Tue Sep 28 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-1
- Update to 2.8.0.1

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.0-2
- Add patch to fix runtime warning spew - bug #132921

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-1
- Update to 2.8.0

* Mon Aug 30 2004 Mark McLoughlin <markmc@redhat.com> 2.7.92-1
- Update to 2.7.92
- Include API docs

* Wed Aug 18 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91-1
- Update to 2.7.91

* Wed Aug  4 2004 Mark McLoughlin <markmc@redhat.com> 2.7.90-1
- Update to 2.7.90

* Tue Jul 27 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0.1-4
- Rebuilt

* Tue Jul 27 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0.1-3
- Patch from upstream which fixes a nasty viewport issue obvious when
  using it with sawfish (#120652)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 31 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0.1-1
- Update to 2.6.0.1

* Mon Mar 22 2004 Mark McLoughlin <markmc@redhat.com>
- Don't explicitly require startup-notification in the .pc file - bug #111091

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Mark McLoughlin <markmc@redhat.com> 2.5.90-1
- Update to 2.5.90

* Tue Feb 17 2004 Alexander Larsson <alexl@redhat.com> 2.5.1-3
- Link to Xres now that it is PIC

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 26 2004 Alexander Larsson <alexl@redhat.com> 2.5.1-1
- Upgrade to 2.5.1
- Disable XRes usage due to #114292

* Fri Oct  3 2003 Alexander Larsson <alexl@redhat.com> 2.4.0.1-1
- 2.4.0.1

* Tue Sep  9 2003 Alexander Larsson <alexl@redhat.com> 2.4.0-1
- update to 2.4.0

* Thu Aug 14 2003 Alexander Larsson <alexl@redhat.com> 2.3.1-1
- update for gnome 2.3

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  4 2003 Havoc Pennington <hp@redhat.com> 2.2.2-1
- 2.2.2

* Thu Apr  3 2003 Matt Wilson <msw@redhat.com> 2.2.1-3
- make sure that _NET_DECKTOP_LAYOUT is only 4 elements.  Using
  "sizeof (data) / 4" results in 8 elements being set on 64 bit
  platforms.  Just use "4" instead. (#87951)

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 2.2.1-2
- remove Xft buildreq

* Wed Feb  5 2003 Havoc Pennington <hp@redhat.com> 2.2.1-1
- 2.2.1 adds StartupWMClass to tasklist
- require startup-notification 0.5

* Wed Feb  5 2003 Alexander Larsson <alexl@redhat.com>
- 2.2.0

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 10 2003 Havoc Pennington <hp@redhat.com>
- 2.1.90

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- 2.1.5

* Fri Nov  8 2002 Havoc Pennington <hp@redhat.com>
- 2.1.3

* Thu Oct 31 2002 Havoc Pennington <hp@redhat.com>
- 0.18 that displays standalone dialogs in task list

* Sun Aug 25 2002 Havoc Pennington <hp@redhat.com>
- 0.17 allows clicking a task to minimize it, and DND over a task to
  switch to it, adds translations, and fixes a couple crash things in
  the accessibility stuff.

* Thu Aug  8 2002 Havoc Pennington <hp@redhat.com>
- 0.16 with some tasklist fixes and 
  pager fixes

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- remove empty NEWS

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 0.14

* Thu Jun 06 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue Jun  4 2002 Havoc Pennington <hp@redhat.com>
- 0.13
- add ldconfig to post/postun

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Fri May 17 2002 Havoc Pennington <hp@redhat.com>
- 0.12

* Thu May  2 2002 Havoc Pennington <hp@redhat.com>
- 0.9

* Wed Apr 17 2002 Havoc Pennington <hp@redhat.com>
- 0.8

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 0.3

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Rebuild with new glib and gtk+

* Wed Jan 23 2002 Havoc Pennington <hp@redhat.com>
- Initial build

