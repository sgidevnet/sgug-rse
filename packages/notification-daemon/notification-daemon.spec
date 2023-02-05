%define gtk3_version            3.15.2

Summary: Desktop Notification Daemon
Name: notification-daemon
Version: 3.20.0
Release: 8%{?dist}
URL: https://wiki.gnome.org/Projects/GnomeFlashback
License: GPLv2+
Provides: desktop-notification-daemon

BuildRequires: gcc
BuildRequires: gtk3-devel >= %{gtk3_version}
BuildRequires: libcanberra-devel
BuildRequires: intltool

Obsoletes: notify-daemon
Provides: notify-daemon
Obsoletes: notification-daemon-engine-slider < 0.2.0-3
Provides: notification-daemon-engine-slider = %{version}-%{release}

Source0: http://download.gnome.org/sources/notification-daemon/3.20/%{name}-%{version}.tar.xz

%description
notification-daemon is the server implementation of the freedesktop.org
desktop notification specification. Notifications can be used to inform
the user about an event or display some form of information without getting
in the user's way.

%prep
%setup -q

%build
%configure --disable-static
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}


%files -f %{name}.lang
%doc COPYING AUTHORS NEWS

%{_libexecdir}/notification-daemon
%{_datadir}/applications/notification-daemon.desktop


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 04 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.20.0-1
- new version

* Mon Feb 22 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.18.2-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Oct 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.18.0-1
- GNOME Flashback 3.18.0

* Wed Jun 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.17.2-1
- GNOME Flashback 3.17.2

* Wed Jun 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.16.1-1
- Version bump for GNOME Flashback 3.16

* Wed Jun 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.1-1
- Version bump for GNOME Flashback 3.14

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 0.7.5-1
- Update to 0.7.5

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 0.7.3-1
- Update to 0.7.3

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 0.7.2-1
- Update to 0.7.2

* Mon Feb 21 2011 Matthias Clasen <mclasen@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 0.7.0-4
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 0.7.0-2
- Rebuild

* Mon Jan 24 2011 Matthias Clasen <mclasen@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Mon Jun 28 2010 Jon McCann <jmccann@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Sat Feb 13 2010 Matthias Clasen <mclasen@redhat.com> - 0.4.1-1.20090923.5
- Add missing libs

* Fri Oct 23 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.1-1.20090923.4
- Don't abort if gnome-screensaver is not running (#529592)

* Thu Oct 15 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.1-1.20090923.3
- Fix issues with the multi-monitor support
- Make screensaver check work
- Use gvfs-open instead of gnome-open

* Thu Sep 24 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.1-1.20090923.2
- Change default theme to 'slider'

* Wed Sep 23 2009 Jon McCann <jmccann@redhat.com> - 0.4.1-0.20090923.1
- Update to snapshot to fix crashers
- Add internal API to allow themes to stack only

* Sat Aug 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.0-8
- Change location for stacked notifications to top-right

* Tue Aug  4 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.0-7
- Fix the libsexy patch to make markup work again

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.0-5
- Copy nodoka patch from F11

* Tue Jul 21 2009 Adam Tkac <atkac redhat com> - 0.4.0-4
- improve libsexy patch

* Thu Jul  2 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.0-3
- Drop libsexy dependency

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0
- Drop obosolete patches
- Tweak description

* Mon Jul 14 2008 Matthias Clasen <mclasen@redhat.com> - 0.3.7.90-1.svn3009
- Build against libsexy rather than copying part of it in a broken way (#455289)

* Tue Jun 10 2008 Colin Walters <walters@redhat.com> -0.3.7.90-0.svn3009
- Update to SVN snapshot 3009 (patches below are against it)
- BR gnome-common so we can autogen
- Add positioning patch
- Add patch to fix the dist
- Edit libsexy patch to adapt to the fact we're using an SVN export
- Drop upstreamed summary patch
- Add some code in install to delete notification-properties crapplet
- BR libglade2-devel

* Sun Apr  6 2008 Jon McCann <jmccann@redhat.com> - 0.3.7-9
- Don't clip text in message bubbles (#441099)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.7-8
- Autorebuild for GCC 4.3

* Tue Oct 23 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.7-7
- Rebuild against new dbus-glib

* Wed Sep 26 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.7-6
- Make it build with the latest intltool

* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.7-5
- Update the license field

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.7-4
- Rebuild again

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.7-3
- Rebuild with new libwnck

* Mon May 14 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.7-2
- Escape markup in summaries (#239950)

* Fri Mar 23 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.7-1
- Update to 0.3.7, which contains important bug fixes 
  and theming improvements

* Mon Jan 29 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.6-1
- Update to 0.3.6
- Apply a patch by Thorsten Leemhuis to fix some spec issues

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 0.3.5-8
- Fix scripts according to packaging guidelines

* Tue Oct 17 2006 Matthias Clasen <mclasen@redhat.com> - 0.3.5-7
- Tighten up Requires (#203813)

* Thu Jul 20 2006 Jesse Keating <jkeating@redhat.com> - 0.3.5-6
- Remove gconf kills, no longer necessary

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.5-5
- add BR on dbus-glib-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.5-4.1
- rebuild

* Fri Jun 09 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.5-4
- Mark schema as config
- Add libtool BR
- Add intltool BR

* Mon Jun 05 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.5-3
- More spec file cleanups

* Fri May 26 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.5-2
- Spec file cleanup

* Fri May 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.5-1
- Update to upstream 0.3.5
- Rename to notification-daemon to track upstream

* Mon Apr 17 2006 Kristian Høgsberg <krh@redhat.com> 0.3.1-10
- Update name of compositing manager selection to track recent
  metacity changes.

* Wed Mar 08 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.1-9
- Add patch to fix struct handling in the dbus glib binding for dbus 0.61
  so image data works again

* Tue Feb 14 2006 Christopher Aillon <caillon@redhat.com> - 0.3.1-8
- BuildRequires love, for all you lovers out there.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.3.1-7.1
- bump again for double-long bug on ppc(64)

* Thu Feb 09 2006 Florian La Roche <laroche@redhat.com>
- remove empty scripts from .spec file

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.3.1-6.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb  3 2006 Christopher Aillon <caillon@redhat.com> - 0.3.1-6
- Add patch to determine whether a compositing manager is running
  when drawing a new notification bubble, as long as the CM grabs
  the appropriate XSelection.

* Fri Jan 20 2006 Christopher Aillon <caillon@redhat.com> - 0.3.1-5
- Make it so that marked-up messages appear with markup

* Thu Jan 12 2006 Christopher Aillon <caillon@redhat.com> - 0.3.1-4
- Provide desktop-notification-daemon, since libnotify requires a
  notification deamon, but not this specific one.  Other notification
  daemons can exist on the system so long as they meet the provides
  (and the API of course).

* Mon Jan  9 2006 Christopher Aillon <caillon@redhat.com> - 0.3.1-3
- Fix positioning of the notification bubble to not draw off-screen

* Wed Dec 14 2005 John (J5) Palmieri <johnp@redhat.com> - 0.3.1-2
- Actuall release of 0.3.1

* Thu Nov 17 2005 John (J5) Palmieri <johnp@redhat.com> - 0.3.1-1
- Upgrade to upstream 0.3.1 

* Tue Nov 15 2005 John (J5) Palmieri <johnp@redhat.com> - 0.3.0-1
- inital build
