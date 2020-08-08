Summary: A GUI text editor for systems with X
Name: nedit
Version: 5.7
Release: 7%{?dist}
Source: http://sourceforge.net/projects/nedit/files/nedit-source/nedit-%{version}-src.tar.gz
Source1: nedit.desktop
Source2: nedit-icon.png
Patch0: nedit-5.5-security.patch
# https://sourceforge.net/p/nedit/git/ci/838292fe4034fc4ab4567f1d87193a4e6a57eca0/
Patch1: 0001-Force-C89-on-gcc-linux-to-prevent-accidental-changes.patch
# Append to Fedora's C_OPT_FLAGS and LD_OPT_FLAGS rather than overriding them.
Patch2: nedit-5.7-makefiles.patch
Patch3: nedit-5.6-utf8.patch
Patch5: nedit-5.7-nc-manfix.patch
Patch6: nedit-5.5-visfix.patch
Patch8: nedit-5.5-scroll.patch

Patch100: nedit.sgifixes.patch

URL: http://nedit.org
License: GPLv2
Requires: xorg-x11-fonts-ISO8859-1-75dpi
BuildRequires:  gcc
BuildRequires: motif-devel, libXau-devel, libXpm-devel, libXmu-devel
BuildRequires: desktop-file-utils
# Needed for generating manpages; see doc/Makefile
BuildRequires: perl(Pod::Man)

%description
NEdit is a GUI text editor for the X Window System. NEdit is
very easy to use, especially if you are familiar with the
Macintosh or Microsoft Windows style of interface.

%prep
%setup -q
%patch0 -p1 -b .security
%patch1 -p1 -b .c89
%patch2 -p1 -b .makefiles
%patch3 -p1 -b .utf8
%patch5 -p1 -b .nc-manfix
%patch6 -p1 -b .visfix
%patch8 -p1 -b .scroll

%patch100 -p1 -b .sgifixes

# A place to generate the sgug patch
#exit 1

%build
export PREV_WD=`pwd`
cd doc
# Upstream really doesn't want you generating the manpages, but they forgot to
# include the manpages in 5.7. So generate them.
make VERSION='NEdit 5.7' man
cd $PREV_WD
#make linux C_OPT_FLAGS="$RPM_OPT_FLAGS"
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
make %{_smp_mflags} irix C_OPT_FLAGS="$RPM_OPT_FLAGS" LD_OPT_FLAGS="$LDFLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
mv source/nc source/nedit-client
install -m 755 source/nedit source/nedit-client $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 doc/nedit.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit.1x
mv doc/nc.man doc/nedit-client.man
install -p -m 644 doc/nedit-client.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit-client.1x

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/nedit.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category "Development;" \
        %{SOURCE1}

%files
%doc README ReleaseNotes
%{_mandir}/*/*
%{_bindir}/*
%{_prefix}/share/applications/*
%{_datadir}/icons/hicolor/

%changelog
* Sat Jul 04 2020 Daniel Hams <daniel.hams@gmail.com> - 5.7-7
- Pull into wip

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 12 2017 Mike DePaulo <mikedep333@gmail.com> - 5.7-1
- Update to 5.7
- Backport upstream commit to force C89 "to prevent accidental changes to C90/GNU dialect"

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Jon Ciesla <limburgher@gmail.com> - 5.6-2
- Move from lesstif to motif

* Wed Jun 17 2015 Jindrich Novy <novyjindrich@gmail.com> - 5.6
- update to 5.6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Jindrich Novy <jnovy@redhat.com> 5.5-32
- fix broken build because of missing format string (#1106275)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 5.5-29
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb  9 2011 Jindrich Novy <jnovy@redhat.com> 5.5-25
- regenerate makefiles patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 19 2010 Jindrich Novy <jnovy@redhat.com> 5.5-23
- remove (TM) from package description (#542473)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Jindrich Novy <jnovy@redhat.com> 5.5-20
- BR: xorg-x11-fonts-ISO8859-1 to avoid incorrect font
  substitutions (#464945)

* Fri Sep 26 2008 Jindrich Novy <jnovy@redhat.com> 5.5-19
- rediff security patch to be applicable with zero fuzz

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> 5.5-18
- manual rebuild because of gcc-4.3 (#434192)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.5-17
- Autorebuild for GCC 4.3

* Sun Jan  6 2008 Patrice Dumas <pertusus@free.fr> 5.5-16
- minor cleanups

* Tue Oct 30 2007 Jindrich Novy <jnovy@redhat.com> 5.5-15
- make mouse wheel scrolling compatible with lesstif (#354591)

* Mon Oct 29 2007 Jindrich Novy <jnovy@redhat.com> 5.5-14
- don't use /bin/csh but /bin/sh as default shell (#355441)

* Fri Oct 26 2007 Jindrich Novy <jnovy@redhat.com> 5.5-13
- spec cleanup

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 5.5-12
- update License
- rebuild for BuildID

* Mon Jan  8 2007 Jindrich Novy <jnovy@redhat.com> 5.5-11
- explicitly depend on lesstif to avoid nedit crashes
  (binary lesstif/openmotif incompatibilities) (#221535)
- fix buildroot

* Sat Sep  2 2006 Jindrich Novy <jnovy@redhat.com> 5.5-10.fc6
- remove dependency on openmotif and build against lesstif
- add missing libXmu-devel dependency

* Wed Aug 30 2006 Jindrich Novy <jnovy@redhat.com> 5.5-9
- don't use the autodetected, but default visual to avoid
  crashes (#199770)

* Wed May 24 2006 Jindrich Novy <jnovy@redhat.com> 5.5-8
- don't strip binaries so that we have usable debuginfo
  nedit package (#192607)

* Sun Mar  5 2006 Jindrich Novy <jnovy@redhat.com> 5.5-7
- rebuild

* Fri Dec 16 2005 Jindrich Novy <jnovy@redhat.com> 5.5-6
- fix openmotif dependencies
- build with modular X

* Mon Oct 10 2005 Jindrich Novy <jnovy@redhat.com> 5.5-5
- update nedit file locations to new xorg standards (#167208, #170937)
- rename nc to nedit-client to avoid conflict with netcat and
  modify its manpage to reflect this
- fix License to GPL

* Wed Jul 27 2005 Jindrich Novy <jnovy@redhat.com> 5.5-4
- initial Extras built

* Thu Jan 20 2005 Jindrich Novy <jnovy@redhat.com> 5.5-3
- prepare the spec and desktop file for Extras inclusion

* Wed Jan 12 2005 Jindrich Novy <jnovy@redhat.com> 5.5-2
- fix usage of uninitialized variable (#144790)

* Mon Dec 27 2004 Jindrich Novy <jnovy@redhat.com> 5.5-1
- new version 5.5

* Mon Sep 20 2004 Jindrich Novy <jnovy@redhat.com>
- added nedit icon to be present in menus #131601
- updated spec to put it to the right place
- icon made by Joor Loohuis (joor@users.sourceforge.net)
- the icon processed by Peter Vrabec (pvrabec@usu.cz)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 17 2004 Thomas Woerner <twoerner@redhat.com> 5.4-1
- new version 5.4

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Dec  5 2003 Tim Waugh <twaugh@redhat.com>
- Don't explicitly require openmotif, since rpm does library dependencies
  automatically.
- Binary package doesn't require desktop-file-install.

* Fri Dec  5 2003 Tim Waugh <twaugh@redhat.com> 5.3-6
- Add ugly hack to work around openmotif's lack of UTF-8 support (bug #75189).
- Back-port 5.4RC2 fix for uninitialized variable (bug #110898).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Nov  8 2002 Tim Waugh <twaugh@redhat.com> 5.3-3
- Handle X11 libdir issue.

* Tue Oct 22 2002 Tim Waugh <twaugh@redhat.com> 5.3-2
- Remove original desktop file when installing.
- Fix desktop file icon (bug #61677).

* Wed Jul 24 2002 Karsten Hopp <karsten@redhat.de>
- 5.3
- use desktop-file-utils (#69461)
- redo all patches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Mar 22 2002 Tim Powers <timp@redhat.com>
- rebuilt against openmotif-2.2.2

* Fri Mar  1 2002 Than Ngo <than@redhat.com> 1.2-1
- update to 1.2
- cleanup patch files

* Thu Jan 17 2002 Than Ngo <than@redhat.com> 5.1.1-13
- rebuild against openmotif

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Oct 25 2001 Bill Nottingham <notting@redhat.com>
- 0 != NULL. lather, rinse, repeat. (#54943)

* Mon Aug 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix crash while printing (#45149)
  I still think removing the package would be the better fix, though.

* Sun Jun 10 2001 Than Ngo <than@redhat.com>
- requires lesstif-devel

* Tue May 22 2001 Tim Powers <timp@redhat.com>
- patched to use lesstif

* Fri Apr 27 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix security bug, use mkstemp()

* Fri Oct 13 2000 Preston Brown <pbrown@redhat.com>
- .desktop file added

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Sat Jun 17 2000 Than Ngo <than@redhat.de>
- rebuilt against openmotif-2.1.30
- use PRM macros

* Tue May 16 2000 Tim Powers <timp@redhat.com>
- updated to 5.1.1
- updated URL and source location

* Wed Aug 18 1999 Tim Powers <timp@redhat.com>
- excludearch alpha

* Mon Jul 19 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Thu Apr 15 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Wed Oct 14 1998 Michael Maher <mike@redhat.com>
- built package for 5.2

* Thu May 21 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 5.0.2

* Thu Nov 20 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig

* Mon Nov 17 1997 Otto Hammersmith <otto@redhat.com>
- added changelog
- fixed src url
- added URL tag
