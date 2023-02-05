Summary:	A Usenet newsreader for GNOME/GTK+
Name:		pan
Version:	0.146
Release:	1%{?dist}
Epoch:		1
License:	GPLv2
Source0:	http://pan.rebelbase.com/download/releases/%{version}/source/%{name}-%{version}.tar.bz2
URL:		http://pan.rebelbase.com/
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	glib2-devel  >= 2.26.0
BuildRequires:	gmime30-devel >= 2.6.20
BuildRequires:	gtk2-devel  >= 2.16.0
BuildRequires:	gtkspell-devel >= 2.0.7
BuildRequires:	enchant-devel >= 1.6.0
BuildRequires:	libappstream-glib
BuildRequires:	libnotify-devel >= 0.4.1
BuildRequires:	libgnome-keyring-devel >= 3.2.0
BuildRequires:	itstool
BuildRequires:	yelp-tools
# In the past, we could not link GPLv2-only Pan with GnuTLS due to libgnutls being effectively LGPLv3+
# However, the GnuTLS libs are now clearly LGPLv2+, which is compatible.
BuildRequires:	gnutls-devel

%description
Pan is a Usenet newsreader which attempts to be pleasant to
new and advanced users alike. It has all the standard
newsreaders features and also supports offline reading,
scoring and killfiles, yEnc, NZB, PGP handling, multiple
servers, and secure connections. It is also the only Unix
newsreader to get a perfect score on the Good Net-Keeping
Seal of Approval evaluations.

%prep
%setup -q

sed -i -e 's|StartupNotify=false|StartupNotify=true|' %{name}.desktop.in

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LDFLAGS="$RPM_LD_FLAGS -ldicl-0.1 -liconv"
%configure --with-gtk3 --with-gnutls \
    --with-gtkspell --enable-libnotify \
    --enable-gkr --enable-manual \
    --with-dbus --with-gmime-crypto \
    --with-gmime30 
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%find_lang %{name} --with-gnome

%check
#appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING COPYING-DOCS
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/pan.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/pan.1*

%changelog
* Fri Apr 23 2021  HAL <notes2@gmx.de> - 1:0.146-1
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Mon Dec 16 2019 Petr Kovar <pkovar@redhat.com> - 1:0.146-1
- Update to version 0.146

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.145-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.145-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.145-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Petr Kovar <pkovar@redhat.com> - 1:0.145-1
- Update to version 0.145

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.144-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Petr Kovar <pkovar@redhat.com> - 1:0.144-1
- Update to version 0.144
- Add man page and hicolor icons

* Sun Dec 3 2017 Petr Kovar <pkovar@redhat.com> - 1:0.143-1
- Update to version 0.143
- Bump gmime-devel version
- Fix license macro

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.142-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.142-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Petr Kovar <pkovar@redhat.com> - 1:0.142-1
- Update to version 0.142
- Enable built-in help

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.141-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.141-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Petr Kovar <pkovar@redhat.com> - 1:0.141-1
- Update to version 0.141
- Use license macro for COPYING
- Drop defattr

* Fri Mar 25 2016 Petr Kovar <pkovar@redhat.com> - 1:0.140-1
- Update to version 0.140
- Remove -D_GLIBCXX_USE_CXX11_ABI=0
- Remove ChangeLog
- Update description

* Mon Mar 07 2016 Petr Kovar <pkovar@redhat.com> - 1:0.140-0.4.20160306git
- Update to latest git snapshot

* Sun Mar 06 2016 Petr Kovar <pkovar@redhat.com> - 1:0.140-0.3.20160306git
- Update to latest git snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.140-0.2.20160114git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Petr Kovar <pkovar@redhat.com> - 1:0.140-0.1.20160114git
- Update to latest git snapshot
- Use -D_GLIBCXX_USE_CXX11_ABI=0
- Add appdata file
- Use desktop-file-validate instead of desktop-file-install

* Wed Dec 02 2015 Tom Callaway <spot@fedoraproject.org> - 1:0.139-11
- enable build with GnuTLS (bz 999582)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.139-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:0.139-9
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.139-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.139-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Petr Kovar <pkovar@redhat.com> - 1:0.139-6
- Fix changelog & explain in a comment why we cannot link Pan with GnuTLS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.139-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Jon Ciesla <limburgher@gmail.com> - 1:0.139-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.139-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.139-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Petr Kovar <pkovar@redhat.com> - 1:0.139-1
- Update to version 0.139

* Mon Jun 18 2012 Petr Kovar <pkovar@redhat.com> - 1:0.138-1
- Update to version 0.138
- Disable support for GnuTLS: we cannot link GPLv2-only Pan with GnuTLS due to
  libgnutls being effectively LGPLv3+

* Sun May 20 2012 Petr Kovar <pkovar@redhat.com> - 1:0.137-1
- Update to version 0.137
- Update BuildRequires
- Remove upstreamed patch

* Mon Apr 09 2012 Petr Kovar <pkovar@redhat.com> - 1:0.136-1
- Update to version 0.136
- Update BuildRequires
- Correct License
- Remove upstreamed patch and add a new one

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.135-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.135-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.135-2
- Rebuilt for glibc bug#747377

* Thu Jul 21 2011 Petr Kovar <pkovar@redhat.com> - 1:0.135-1
- Update to version 0.135
- Add intltool to BuildRequires
- Remove pcre-devel from BuildRequires
- Remove upstreamed patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.133-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.133-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1:0.133-3
- Add patch to fix build against GCC 4.4
- Rebuild against new gmime22 compatibility package (#476250)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.133-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep 6 2008 Erik van Pienbroek <info@nntpgrab.nl> - 1:0.133-1
- Update to version 0.133 (fixes GCC 4.3 compilation problems)
- Remove upstreamed patch

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.132-4
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.132-3
- Autorebuild for GCC 4.3

* Thu Sep 13 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.132-2
- Add patch for BZ #283241 (upstream #467446)

* Sat Aug 25 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.132-1
- Update to 0.132

* Wed Jun 06 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.131-1
- Update to 0.131 (fixing #241610)

* Sat May 12 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.129-1
- Update to 0.129

* Sun May 06 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.128-1
- Update to 0.128

* Sat Apr 14 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.127-1
- Update to 0.127

* Tue Mar 20 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 1:0.125-2
- Bump release for FE6 -> Fedora 7 upgrade path.

* Tue Feb 27 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.125-1
- Update to 0.125

* Sun Feb 11 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.123-1
- Update to 0.123

* Sun Feb 04 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.122-1
- Update to 0.122

* Sun Jan 14 2007 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.120-1
- Update to 0.120
- Drop --add-category=X-Fedora in pan.desktop

* Sat Nov 11 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.119-1
- Update to 0.119

* Sat Nov 04 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.118-1
- Update to 0.118

* Sun Oct 22 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.117-1
- Update to 0.117

* Sun Oct 15 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.116-1
- Update to 0.116

* Mon Oct 02 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 1:0.115-1
- Update to 0.115 (last `big change' release before 1.0)
- removed unnecessary Patch0 pan-0.99-gi18n.patch
- spec cleanups

* Sat Jun 03 2006 Michael A. Peters <mpeters@mac.com> - 1:0.99-2
- Patch0 to try and fix devel build

* Tue May 30 2006 Michael A. Peters <mpeters@mac.com> - 1:0.99-1
- Update to 0.99

* Tue May 23 2006 Michael A. Peters <mpeters@mac.com> - 1:0.98-1
- Update to 0.98
- previous patches not needed

* Tue May 16 2006 Michael A. Peters <mpeters@mac.com> - 1:0.97-2
- Added pan-0.97-tree-expanders.patch from upstream

* Sat May 13 2006 Michael A. Peters <mpeters@mac.com> - 1:0.97-1
- Update to 0.97 (previous patches no longer needed)
- Patch pan-0.97-crash-on-shutdown.patch from upstream added

* Mon May 08 2006 Michael A. Peters <mpeters@mac.com> - 1:0.96-2
- Two patches from upstream (pan-0.96-upstream-sort_segfault.patch
- and pan-0.96-upstream-subscribed_group.patch)

* Sat May 06 2006 Michael A. Peters <mpeters@mac.com> - 1:0.96-1
- Update to 0.96 - patch0 no longer needed

* Mon May 01 2006 Michael A. Peters <mpeters@mac.com> - 1:0.95-3
- Apply a patch from upstream for new tree implementation bug
-  (Patch0)

* Sun Apr 30 2006 Michael A. Peters <mpeters@mac.com> - 1:0.95-2
- Fix rpmlint errors on debug package

* Sun Apr 30 2006 Michael A. Peters <mpeters@mac.com> - 1:0.95-1
- Update to 0.95

* Mon Apr 24 2006 Michael A. Peters <mpeters@mac.com> - 1:0.94-1
- Update to 0.94

* Wed Apr 19 2006 Michael A. Peters <mpeters@mac.com> - 1:0.93-1
- Update to 0.93

* Mon Apr 17 2006 Michael A. Peters <mpeters@mac.com> - 1:0.91-1
- New upstream version - using spec file mods submitted by
- Alan C. Sanderson with cleanup - Thanks :)
- Closes bug 187874
-
- #* Tue Apr 04 2006 Alan C. Sanderson <Alan.C.Sanderson@gmail.com> - 1:0.90-1
- Updated to 0.90.
- Added gmime-devel >= 2.1.0 BuildRequires
- Removed patches 7,11,12

* Fri Feb 17 2006 Michael A. Peters <mpeters@mac.com> - 1:0.14.2.91-4
- Devel branch rebuild

* Mon Jan 16 2006 Michael A. Peters <mpeters@mac.com> - 1:0.14.2.91-3.3
- Devel branch rebuild

* Thu Sep 22 2005 Michael A. Peters <mpeters@mac.com> - 1:0.14.2.91-3.2
- forgot to commit patch to cvs in devel branch.

* Sun Sep 11 2005 Michael A. Peters <mpeters@mac.com> - 1:0.14.2.91-3.1
- added patch12 to fix bug 165626

* Tue Jun 21 2005 Michael A. Peters <mpeters@mac.com> - 1:0.14.2.91-2.1
- added gettext BuildRequires

* Tue Jun 21 2005 Michael A. Peters <mpeters@mac.com> - 1:0.14.2.91-2
- bump version
- remove patch 8 - replace w/ gcc4 patch (patch11)
- remove patch 9 - fixed in upstream version bump
- remove patch 10 - fixed in upstream / use desktop-file-install
- remove gnet2 source - use gnet2-devel from Extras
- remove redundant BuildRequires, remove explicit library requires


* Thu May 06 2004 Than Ngo <than@redhat.com> 1:0.14.2-7
- cleanup GNOME/KDE Menu

* Tue Apr 20 2004 Jens Petersen <petersen@redhat.com> - 1:0.14.2-6
- disable pan-0.14.2-gcc34.patch since it seems to break things badly
  (Nathan Grennan,121103)

* Wed Apr 14 2004 Jens Petersen <petersen@redhat.com> - 1:0.14.2-5
- add pan-desktop-rh-119909.patch and use upstream desktop file
  (hayastan132@hotmail.com)
- add pan-0.14.2-gmime-crash-120007.patch to fix crashing
  (confushion@comcast.net)
- add pan-0.14.2-gcc34.patch to fix building with newer gcc (Jeff Law)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Dec  5 2003 Jens Petersen <petersen@redhat.com> - 1:0.14.2-3
- require libxml2 and buildrequire libxml2-devel [Maxim Dzumanenko]

* Wed Sep 17 2003 Jens Petersen <petersen@redhat.com> - 1:0.14.2-2
- build with gtkspell support enabled [suggested by Alan Sanderson]
- require gtkspell and buildrequire gtkspell-devel and aspell-devel

* Wed Sep  3 2003 Jens Petersen <petersen@redhat.com> - 1:0.14.2-1
- update to 0.14.2 bugfix release (fixes a long-standing seldom seen
  config file corruption bug)

* Thu Aug 28 2003 Jens Petersen <petersen@redhat.com> - 1:0.14.1-1
- update to 0.14.1 bugfix release
- build with gnet-2.0.4 and pass PKG_CONFIG_PATH for it to configure

* Fri Jun 27 2003 Jens Petersen <petersen@redhat.com> - 1:0.14.0-2
- build gnet with glib2 (#98060) [reported by suckfish@ihug.co.nz]

* Sun Jun 22 2003 Jens Petersen <petersen@redhat.com> - 1:0.14.0-1
- update to 0.14.0
- drop pan-0.12.1-browser.patch (the default is now mozilla)
- update pan-0.13.3-editor-80839.patch to pan-0.14.0-default-editor-80839.patch
- build gnet-1.1.9 to make libgnet.a for new gnet requirement
- use %%buildroot

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb  6 2003 Jens Petersen <petersen@redhat.com> - 1:0.13.3-3
- change browser patch to default to htmlview instead of gnome-moz-remote
  (#80839) and default editor to [from Louis Garcia]
- change default editor to gedit (#80839) [based on patch from Louis Garcia]
- set startup notification in desktop file

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 31 2002 Jens Petersen <petersen@redhat.com> 1:0.13.3-1
- update to 0.13.3

* Thu Nov 28 2002 Jens Petersen <petersen@redhat.com> 1:0.13.2-1
- update to 0.13.2, fixing #77989
- drop old patches

* Thu Aug 29 2002 Jens Petersen <petersen@redhat.com> 1:0.13.0-2
- 0.13.0
- configure with --disable-gtkspell
- fix type of gmime's message_part_write_to_stream on 64bit archs

* Fri Aug 16 2002 Jens Petersen <petersen@redhat.com> 1:0.12.1-3
- update desktop file so that pan lives in Extras -> Internet

* Thu Aug 8 2002 Jens Petersen <petersen@redhat.com> 1:0.12.1-2
- update url
- update requires and build-requires
- fix desktop file
- update description

* Wed Aug 7 2002 Jens Petersen <petersen@redhat.com> 1:0.12.1-1
- 0.12.1
- build on all archs
- default to gnome-moz-remote, instead of netscape (#70634)

* Wed Jul 10 2002 Bill Huang <bhuang@redhat.com>
- Upgrade to 0.12.0
- Update ja.po to enable Japanese menu.

* Mon Jul 08 2002 Bill Huang <bhuang@redhat.com>
- Upgrade to 0.11.3
- Update "Copyright" to "License"

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 12  2002 Bill Huang <bhuang@redhat.com>
- Update ja.po so that pan can be started up in Japanese locale. 

* Wed Apr  3 2002 Tim Powers <timp@redhat.com>
- update to 0.11.2

* Thu Jan 31 2002 Bill Nottingham <notting@redhat.com>
- build current version in new environment

* Mon Jul  2 2001 Tim Powers <timp@redhat.com>
- updated to 0.9.7, bugfix release
- patched desktop file so that the tooltip isn't considered offensive.

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Mar 19 2001 Tim Powers <timp@redhat.com>
- updated to 0.9.5
- fixes bug #31214 where the years were being displayed as 1979 etc.

* Fri Feb 23 2001 Trond Eivind Glomsr?eg@redhat.com>
- langify

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Mon Nov 13 2000 Tim Powers <timp@redhat.com>
- update to 0.9.1
- no more applnk. Why did we do that in the first place? We have an
  entry for a desktop file in GNOME anyway?

* Wed Sep 13 2000 Tim Powers <timp@redhat.com>
- update to 0.8.1-beta4

* Mon Jul 31 2000 Tim Powers <timp@redhat.com>
- fixed pan's desktop file location to fix bug #14868, was under /etx now fixed to be under /etc
- use predefined  macros from RPM so that this doesn't happen again :)

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Sun Jul 02 2000 Trond Eivind Glomsr?eg@redhat.com>
- updated to 0.8.1beta1
- patch for db breakage

* Tue May 23 2000 Preston Brown <pbrown@redhat.com>
- updated to 0.8.0 final

* Wed May 17 2000 Tim Powers <timp@redhat.com>
- updated to 0.8.0beta8

* Tue Apr 18 2000 Tim Powers <timp@redhat.com>
- updated to 0.8.0beta5

* Thu Feb 10 2000 Matt Wilson <msw@redhat.com>
- updated to 0.7.5

* Tue Jan 11 2000 Tim Powers <timp@redhat.com>
- updated to 0.7.0

* Wed Dec 15 1999 Tim Powers <timp@redhat.com>
- updated to 0.6.7
- general spec file cleanups

* Tue Aug 3 1999 Tim Powers <timp@redhat.com>
- first build of package
