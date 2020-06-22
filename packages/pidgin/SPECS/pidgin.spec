Name:           pidgin
Version:        2.13.0
Release:        15%{?dist}
License:        BSD and GPLv2+ and GPLv2 and LGPLv2+ and MIT
# GPLv2+ - libpurple, gnt, finch, pidgin, most prpls
# GPLv2 - novell prpls
# MIT - Zephyr prpl
URL:            http://pidgin.im/
Source0:        http://downloads.sourceforge.net/pidgin/pidgin-%{version}.tar.bz2
Obsoletes:      gaim < 999:1
Provides:       gaim = 999:1


## Fedora pidgin defaults
# Only needs regenerating if Pidgin breaks backwards compatibility with prefs.xml
# 1) uninstall any non-default pidgin or libpurple plugins
# 2) run pidgin as new user 3) edit preferences 4) close 5) copy .purple/prefs.xml
# OR 1) edit manually
# - enable ExtPlacement plugin
# - enable History plugin
# - enable Message Notification plugin
#   Insert count of new messages into window title
#   Set window manager "URGENT" hint
# - disable buddy icon in buddy list
# - enable Logging (in HTML)
# - Browser "GNOME Default"
# - Smiley Theme "Default"
Source1:        purple-fedora-prefs.xml

Summary:        A Gtk+ based multiprotocol instant messaging client

# Require Binary Compatible glib
# returns bogus value if glib2-devel is not installed in order for parsing to succeed
# bogus value wont make it into a real package
%global glib_ver %([ -a %{_libdir}/pkgconfig/glib-2.0.pc ] && pkg-config --modversion glib-2.0 | cut -d. -f 1,2 || echo -n "999")

%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols including AIM, MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu,
ICQ, IRC, Novell Groupwise, QQ, Lotus Sametime, Simple and Zephyr.
These protocols are implemented using a modular, easy to use design.
To use a protocol, just add an account using the account editor.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting, TCL scripting and C plugins.

Pidgin is not affiliated with or endorsed by America Online, Inc.,
Microsoft Corporation, Yahoo! Inc., or ICQ Inc.


%package devel
Summary:    Development headers and libraries for pidgin
Requires:   %{name} = %{version}-%{release}
Requires:   libpurple-devel = %{version}-%{release}
Requires:   pkgconfig
Requires:   gtk2-devel
Obsoletes:  gaim-devel
Provides:   gaim-devel = %{version}-%{release}


%description devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

#%package perl
#Summary:    Perl scripting support for Pidgin
#Requires:   libpurple = %{version}-%{release}
#Requires:   libpurple-perl = %{version}-%{release}

#%description perl
#Perl plugin loader for Pidgin. This package will allow you to write or
#use Pidgin plugins written in the Perl programming language.


%package -n libpurple
Summary:    libpurple library for IM clients like Pidgin and Finch

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, Simple and Zephyr.


%package -n libpurple-devel
Summary:    Development headers, documentation, and libraries for libpurple
Requires:   libpurple = %{version}-%{release}
Requires:   pkgconfig

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

#%package -n libpurple-perl
#Summary:    Perl scripting support for libpurple
#Requires:   libpurple = %{version}-%{release}
#Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

#%description -n libpurple-perl
#Perl plugin loader for libpurple. This package will allow you to write or
#use libpurple plugins written in the Perl programming language.


%package -n libpurple-tcl
Summary:    Tcl scripting support for libpurple
Requires:   libpurple = %{version}-%{release}

%description -n libpurple-tcl
Tcl plugin loader for libpurple. This package will allow you to write or
use libpurple plugins written in the Tcl programming language.


%package -n finch
Summary:    A text-based user interface for Pidgin
Requires:   glib2 >= %{glib_ver}
Requires:   libpurple = %{version}-%{release}

%description -n finch
A text-based user interface for using libpurple.  This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.


%package -n finch-devel
Summary:    Headers etc. for finch stuffs
Requires:   finch = %{version}-%{release}
Requires:   libpurple-devel = %{version}-%{release}
Requires:   pkgconfig
Requires:   ncurses-devel

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.


%prep
%setup -q

# Our preferences
cp %{SOURCE1} prefs.xml


# Bug #528796: Get rid of #!/usr/bin/env python
# Upstream refuses to use ./configure --python-path= in these scripts.
#for file in finch/plugins/pietray.py libpurple/purple-remote libpurple/plugins/dbus-buddyicons-example.py \
#            libpurple/plugins/startup.py libpurple/purple-url-handler libpurple/purple-notifications-example; do
#    sed -i 's/env python/python3/' $file
#done

# Bug #1141477
#%if 0%{?has_valgrind}
#rm -f libpurple/valgrind.h
#sed -ie 's/include "valgrind.h"/include <valgrind\/valgrind.h>/' libpurple/plugin.c
#%endif

%build

# remove after irc-sasl patch has been merged upstream
#autoreconf --force --install
autoconf

# gnutls is buggy so use mozilla-nss on all distributions
%configure --enable-tcl --enable-tk \
           --disable-schemas-install \
            --disable-nls \
            --disable-missing-dependencies \
            --disable-screensaver \
            --disable-sm \
            --disable-startup-notification \
            --disable-gtkspell \
            --disable-gestures \
            --disable-gstreamer \
            --disable-gstreamer-video \
            --disable-gstreamer-interfaces \
            --disable-farstream \
            --disable-vv \
            --disable-idn \
            --disable-meanwhile \
            --disable-avahi \
            -disable-fortify \
            --disable-dbus \
            --disable-nm \
            --disable-doxygen \
            --disable-devhelp \
            --with-x

make %{?_smp_mflags} V=1 LIBTOOL=/usr/sgug/bin/libtool

# one_time_password plugin, included upstream but not built by default
cd libpurple/plugins/
make one_time_password.so V=1 LIBTOOL=/usr/sgug/bin/libtool
cd -

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install LIBTOOL=/usr/sgug/bin/libtool

install -m 0755 libpurple/plugins/one_time_password.so $RPM_BUILD_ROOT%{_libdir}/purple-2/


# remove libtool libraries and static libraries
find $RPM_BUILD_ROOT \( -name "*.la" -o -name "*.a" \) -exec rm -f {} ';'
# remove the perllocal.pod file and other unrequired perl bits
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
# remove relnot.so plugin since it is unusable for our package
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/relnot.so
# remove dummy nullclient
rm -f $RPM_BUILD_ROOT%{_bindir}/nullclient
# install Fedora pidgin default prefs.xml
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/purple/
install -m 644 prefs.xml $RPM_BUILD_ROOT%{_sysconfdir}/purple/prefs.xml

# remove non-plugin unrequired library symlinks
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/liboscar.so
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/libjabber.so
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/libymsg.so

# make sure that we can write to all the files we've installed
# so that they are properly stripped
chmod -R u+w $RPM_BUILD_ROOT/*

#%find_lang pidgin


# Create list of plugins for __requires_exclude
find %{buildroot}/%{_libdir}/purple-2 -name \*.so\* -printf '%f|' | sed -e 's/|$//' > plugins.list

%files
%doc NEWS COPYING AUTHORS README ChangeLog doc/PERL-HOWTO.dox
%{_bindir}/pidgin
%{_libdir}/pidgin/
%{_mandir}/man1/pidgin.*
%{_mandir}/man3/
%{_datadir}/pixmaps/pidgin/
%{_datadir}/icons/hicolor/*/apps/pidgin.*

%files devel
%{_includedir}/pidgin/
%{_libdir}/pkgconfig/pidgin.pc

%files -n libpurple
%{_libdir}/purple-2/
%{_libdir}/libpurple.so.*
%{_datadir}/sounds/purple/
%dir %{_sysconfdir}/purple
%config(noreplace) %{_sysconfdir}/purple/prefs.xml
%{_datadir}/purple/ca-certs/


%files -n libpurple-devel
%{_datadir}/aclocal/purple.m4
%{_libdir}/libpurple.so
%{_includedir}/libpurple/
%{_libdir}/pkgconfig/purple.pc



%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Stefan Becker <chemobejk@gmail.com> - 2.13.0-14
- add support for NetworkManager-libnm integration (#1726938)

* Fri Jun 07 2019 Debarshi Ray <rishi@fedoraproject.org> - 2.13.0-13
- Drop AIM support

* Tue Jun 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.0-12
- Perl 5.30 re-rebuild updated packages

* Tue Jun  4 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.13.0-11
- Fixed FTBFS with python-3.8
  Resolves: rhbz#1716480
- Made build more verbose (V=1)
- De-fuzzified patches

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.0-10
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.13.0-8
- Rebuilt for libcrypt.so.2 (#1666033)

* Tue Oct 09 2018 Debarshi Ray <rishi@fedoraproject.org> - 2.13.0-7
- Honor %%{valgrind_arches}

* Tue Jul 31 2018 Debarshi Ray <rishi@fedoraproject.org> - 2.13.0-6
- Update License

* Mon Jul 30 2018 Debarshi Ray <rishi@fedoraproject.org> - 2.13.0-5
- Make python3-config available during the build

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.0-3
- Perl 5.28 rebuild

* Fri May 25 2018 Adam Jackson <ajax@redhat.com> - 2.13.0-2
- Rebuild for new libidn

* Mon Apr 16 2018 Björn Esser <besser82@fedoraproject.org> - 2.13.0-1
- Update to 2.13.0 (#1553811)
- Drop nm-glib on Fedora 29+ (#1530657)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.12.0-7
- Rebuilt for switch to libxcrypt

* Thu Dec 21 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.12.0-6
- Cleanup spec file conditionals

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12.0-3
- Perl 5.26 rebuild

* Wed Apr 26 2017 Debarshi Ray <rishi@fedoraproject.org> - 2.12.0-2
- Avoid a use-after-free in an error path (#1445915)

* Mon Mar 13 2017 Jan Synáček <jsynacek@redhat.com> - 2.12.0-1
- Update to 2.12.0 (#1431113 #1431225)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.11.0-2
- Rebuild for Python 3.6

* Thu Jun 23 2016 Jan Synáček <jsynacek@redhat.com> - 2.11.0-1
- Update to 2.11.0 (#1348545)

* Fri Jun 10 2016 David Woodhouse <dwmw2@infradead.org> - 2.10.12-5
- Include media fixes from upstream (and soon to be upstream)

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.12-4
- Perl 5.24 rebuild

* Mon May  9 2016 Jan Synáček <jsynacek@redhat.com> - 2.10.12-3
- Disable SILC support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Jan Synáček <jsynacek@redhat.com> - 2.10.12-1
- Update to 2.10.12 (#1295097)

* Thu Nov 12 2015 David Woodhouse <dwmw2@infradead.org> - 2.10.11-15
- Add two upstream appdata fixes

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.11-13
- Perl 5.22 rebuild

* Wed Jun  3 2015 Jan Synáček <jsynacek@redhat.com> - 2.10.11-12
- Refix purple-remote when running in python3 (#1226468)
- Add python3-dbus to Requires (needed by purple-remote from libpurple)

* Mon Jun  1 2015 Jan Synáček <jsynacek@redhat.com> - 2.10.11-11
- Fix purple-remote when running in python3 (#1226468)

* Tue Mar 17 2015 David Woodhouse <dwmw2@infradead.org> - 2.10.11-10
- Import all Lync-collab patches now that they are upstream.

* Fri Mar 13 2015 David Woodhouse <dwmw2@infradead.org> - 2.10.11-9
- Add TCP and media encryption support

* Thu Mar 12 2015 David Woodhouse <dwmw2@infradead.org> - 2.10.11-8
- Update to final upstream version of GStreamer 1.0 patch

* Thu Mar 12 2015 David Woodhouse <dwmw2@infradead.org> - 2.10.11-7
- Update BuildRequires for farstream
- Add GConf2 to BuildRequires

* Thu Mar 12 2015 David Woodhouse <dwmw2@infradead.org> - 2.10.11-6
- Build against GStreamer 1.x (#962028)

* Mon Mar  9 2015 Jan Synáček <jsynacek@redhat.com> - 2.10.11-5
- Add In-call DTMF support (#1199771)

* Tue Mar  3 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.10.11-4
- Removed CFLAGS hacks
- Fixed building with gcc-5 (by do-not-disable-wall patch)
  Resolves: rhbz#1197698

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.10.11-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Feb 13 2015 Jan Synáček <jsynacek@redhat.com> - 2.10.11-2
- Switch to Python 3 (#1192115)

* Tue Nov 25 2014 Jan Synáček <jsynacek@redhat.com> - 2.10.11-1
- Update to 2.10.11 (#1157503)

* Thu Nov 20 2014 Jan Synáček <jsynacek@redhat.com> - 2.10.10-4
- Fix: Bump MSN ApplicationID again (#1165066)

* Tue Nov 18 2014 Jan Synáček <jsynacek@redhat.com> - 2.10.10-3
- Fix: Pidgin 2.10.10 can't connect to MSN (#1165066)

* Fri Oct 31 2014 Dan Horák <dan[at]danny.cz> - 2.10.10-2
- valgrind available only on selected arches

* Wed Oct 29 2014 Jan Synáček <jsynacek@redhat.com> - 2.10.10-1
- Update to 2.10.10, includes security fixes for CVE-2014-3694,
  CVE-2014-3695, CVE-2014-3696, CVE-2014-3697 and CVE-2014-3698

* Mon Sep 15 2014 Jan Synacek <jsynacek@redhat.com> - 2.10.9-6
- Use system valgrind.h, BZ 1141477

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.9-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.9-4.el6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.10.9-2
- Rebuilt for tcl/tk8.6

* Mon Feb 03 2014 Dan Mashal <dan.mashal@fedoraproject.org> 2.10.9-1
- Update to 2.10.9

* Thu Sep 26 2013 Rex Dieter <rdieter@fedoraproject.org> 2.10.7-9
- add explicit avahi build deps

* Thu Aug  8 2013 Jan Synáček <jsynacek@redhat.com> - 2.10.7-8
- Remove versioned docdirs, BZ 994039

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 2.10.7-6
- Perl 5.18 rebuild

* Fri Jul 19 2013 Orion Poplawski <orion@cora.nwra.com> - 2.10.7-5
- Fix setting -fstack-protector on F20+, use -fstack-protector-strong there
- Filter out provides from plugins

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.10.7-4
- Perl 5.18 rebuild

* Mon Jul 01 2013 Jan Synáček <jsynacek@redhat.com> - 2.10.7-3
- Require cyrus-sasl-scram, BZ 979052

* Mon Feb 25 2013 Jan Synáček <jsynacek@redhat.com> - 2.10.7-2
- Fix IRC support, BZ 914794

* Wed Feb 20 2013 Jan Synáček <jsynacek@redhat.com> - 2.10.7-1
- Update to 2.10.7, BZ 911088

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Jan Synáček <jsynacek@redhat.com> - 2.10.6-4
- Correctly obsolete pidgin-evolution if evolution integration is disabled,
  BZ 860285

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Petr Pisar <ppisar@redhat.com> - 2.10.6-2
- Perl 5.16 rebuild

* Wed Jul 11 2012 Jan Synáček <jsynacek@redhat.com> - 2.10.6-1
- Update to 2.10.6, BZ 838311

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2.10.5-3
- Perl 5.16 rebuild

* Fri Jul 06 2012 Stu Tomlinson <stu@nosnilmot.com> 2.10.5-2
- Disable evolution integration on F18+ due to API changes in
  evolution-data-server 3.6

* Thu Jul 05 2012 Stu Tomlinson <stu@nosnilmot.com> 2.10.5-1
- Update to 2.10.5, CVE-2012-3374
- Allow building only libraries (#831364)
- Revive FT crash prevention patch

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.10.4-2
- Perl 5.16 rebuild

* Wed May 30 2012 Jon Ciesla <limburgher@gmail.com> - 2.10.4-1
- Update to 2.10.4, CVE-2012-2214, CVE-2012-2318, BZ 806839, 819454.
- Port to farstream patch upstreamed.

* Wed May 02 2012 Milan Crha <mcrha@redhat.com> - 2.10.2-2
- Rebuild against newer evolution-data-server

* Fri Mar 23 2012 Jon Ciesla <limburgher@gmail.com> - 2.10.2-1
- Update to 2.10.2, BZ 803293, 803299.
- Dropping MSN patches.  Protocol patch not needed, won't connect
- to 16 by default.  Crash patch was upstreamed.
- Dropped nm09 patch, upstreamed.

* Fri Mar  9 2012 Tom Callaway <spot@fedoraproject.org> - 2.10.1-4
- fedora 17+ uses farstream now instead of farsight2

* Wed Jan 18 2012 Matthew Barnes <mbarnes@redhat.com> - 2.10.1-3
- Map RHEL 7 to Fedora 16 (for now).

* Wed Jan 18 2012 Matthew Barnes <mbarnes@redhat.com> - 2.10.1-2
- Map RHEL 7 to Fedora 16 (for now).

* Thu Dec 29 2011 Stu Tomlinson <stu@nosnilmot.com> 2.10.1-1
- 2.10.1, includes security fixes for CVE-2011-3594, CVE-2011-4601,
  CVE-2011-4602, CVE-2011-4603

* Mon Nov 28 2011 Milan Crha <mcrha@redhat.com> 2.10.0-5
- Rebuild against newer evolution-data-server

* Sun Oct 30 2011 Bruno Wolff III <bruno@wolff.to> 2.10.0-4
- Rebuild against newer evolution-data-server

* Tue Aug 30 2011 Milan Crha <mcrha@redhat.com> 2.10.0-3
- Sync version with f16 branch

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> 2.10.0-2
- Rebuild against newer evolution-data-server

* Sun Aug 21 2011 Stu Tomlinson <stu@nosnilmot.com> 2.10.0-1
- 2.10.0
- Link against system libgadu instead of using internal copy (#713888)

* Tue Aug 16 2011 Milan Crha <mcrha@redhat.com> 2.9.0-3
- Rebuild against newer evolution-data-server

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.9.0-2
- Perl mass rebuild

* Thu Jun 30 2011 Stu Tomlinson <stu@nosnilmot.com> 2.8.0-3
- 2.9.0, includes security/DoS fix to work around gdk-pixbuf issue
  CVE-2011-2485

* Mon Jun 20 2011 Milan Crha <mcrha@redhat.com> 2.8.0-3
- Rebuild against new evolution-data-server

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.8.0-2
- Perl mass rebuild

* Mon Jun 13 2011 Stu Tomlinson <stu@nosnilmot.com> 2.8.0-1
- 2.8.0

* Fri May 20 2011 Kalev Lember <kalev@smartlink.ee> 2.7.11-4
- Rebuilt for libcamel soname bump

* Tue Apr 26 2011 Dan Williams <dcbw@redhat.com> 2.7.11-3
- A few more NetworkManager 0.9 fixes

* Fri Mar 25 2011 Dan Williams <dcbw@redhat.com> 2.7.11-2
- Rebuild for NetworkManager 0.9

* Fri Mar 11 2011 Stu Tomlinson <stu@nosnilmot.com> 2.7.11-1
- 2.7.11, includes security/DoS fixes in Yahoo protocol
  CVE-2011-1091 (#683031)

* Thu Mar 10 2011 Dan Williams <dcbw@redhat.com> 2.7.10-2
- Update for NetworkManager 0.9

* Tue Feb 22 2011 Stu Tomlinson <stu@nosnilmot.com> 2.7.10-1
- 2.7.10

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 01 2011 Milan Crha <mcrha@redhat.com> 2.7.9-3
- Rebuild against newer evolution-data-server

* Wed Jan 12 2011 Milan Crha <mcrha@redhat.com> 2.7.9-2
- Rebuild against newer evolution-data-server

* Mon Dec 27 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.9-1
- 2.7.9, includes security/DoS fix in the MSN protocol (#665856)

* Mon Nov 29 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.7-1
- 2.7.7
- Disable MSNP16 due to regressions interacting with official client

* Fri Nov 19 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.5-2
- Add additional intermediate CA certificates to fix MSN

* Mon Nov 01 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.5-1
- 2.7.5

* Fri Oct 22 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.4-1
- 2.7.4, includes security fix for CVE-2010-3711

* Tue Oct 12 2010 Milan Crha <mcrha@redhat.com> - 2.7.3-6
- Rebuild against newer evolution-data-server

* Wed Sep 29 2010 jkeating - 2.7.3-5
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.3-4
- Rebuild against newer libedataserver

* Mon Sep 13 2010 Dan Horák <dan[at]danny.cz> 2.7.3-3
- drop the s390(x) ifarchs

* Mon Aug 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.7.3-2
- use _isa in explicit Requires on libpurple to prevent yum from trying to 
  jump architectures to resolve dependency

* Wed Aug 11 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.3-1
- 2.7.3

* Wed Jul 21 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.2-1
- 2.7.2 with a security fix (CVE-2010-2528) and a couple of bug fixes (#601650)

* Thu Jul 15 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.1-5
- Rebuild against newer libedataserver
- spec file cleanup:
    replace %%define with %%global
    replace tabs with spaces for consistency
    mark prefs.xml as a config file

* Wed Jul 07 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.1-4
- Include license in libpurple subpackage

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.7.1-3
- Mass rebuild with perl-5.12.0

* Sun May 30 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.1-2
- Add Obsoletes to pull in pidgin-evolution during update

* Sun May 30 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.1-1
- 2.7.1
- Adds Direct Connection support for MSN
- Numerous bug fixes
- Evolution support moved to pidgin-evolution for F13+ (#581144)

* Thu May 20 2010 Stu Tomlinson <stu@nosnilmot.com> 2.7.0-2
- Upstream backports:
    3c30f64efedafc379b6536852bbb3b6ef5f1f6c9 - fix for receiving HTML on ICQ
    13fbe0815f84d5b3c001947559f5818c10275f4c - prevent null deref on disconnecting account (#592750)
    c4a874926d07b8597db4b78a181a89cf720a8418 - fix blinking tray icon on new message (#592691)
    cfe0e649dda34d9252d40d8f67e445336a247998 - prevent race condition on Yahoo! login
    e3dd36706068f3b8eabd630ff71d270c145cce42 - fix crash in Oscar (#548128)
    13fbe0815f84d5b3c001947559f5818c10275f4c - fix crash during network disconnect (#592750)

* Thu May 13 2010 Stu Tomlinson <stu@nosnilmot.com> - 2.7.0-1
- 2.7.0 with features, bug fixes and a security fix: CVE-2010-1624 (#591806)
- Use System SSL Certificates (#576721)
- Add additional dependencies for Voice + Video (#581343)
- Upstream backport:
    87ada76abf90c44e615679efc5f8128bb941bba1 Reduce MSN traffic

* Thu Mar 04 2010 Warren Togami <wtogami@redhat.com> - 2.6.6-2
- Upstream backports:
    0e3079d15adeb12c1e57ceaf5bf037f9b71c8abd Fix AIM SSL clientLogin
    b14ee507e932a395a0e1f29298af162c8614ca0f Fix AIM clientLogin with proxy

* Tue Feb 16 2010 Warren Togami <wtogami@redhat.com> - 2.6.6-1
- 2.6.6 with security and numerous minor bug fixes
  CVE-2010-0277 CVE-2010-0420 CVE-2010-0423
- Bug #528796: Get rid of #!/usr/bin/env python

* Fri Jan  8 2010 Warren Togami <wtogami@redhat.com> - 2.6.5-2
- 2.6.5
- CVE-2010-0013
- Other bug fixes
- Fix build with old gcc versions (RHEL4)

* Tue Dec  8 2009 Warren Togami <wtogami@redhat.com> - 2.6.4-4
- temporarily disable evolution integration in F13 until it is fixed

* Wed Dec 02 2009 Warren Togami <wtogami@redhat.com> 2.6.4-2
- disable SILC in EL6 builds

* Mon Nov 30 2009 Warren Togami <wtogami@redhat.com> 2.6.4-1
- 2.6.4

* Mon Oct 19 2009 Warren Togami <wtogami@redhat.com> 2.6.3-2
- Upstream backport:
    3abad7606f4a2dfd1903df796f33924b12509a56 msn_servconn_disconnect-crash

* Fri Oct 16 2009 Warren Togami <wtogami@redhat.com> 2.6.3-1
- 2.6.3 CVE-2009-3615

* Wed Sep 09 2009 Warren Togami <wtogami@redhat.com> 2.6.2-2
- Upstream backports:
    97e003ed2bc2bafbb993693c9ae9c6d667731cc1 aim-buddy-status-grab
    37aa00d044431100d37466517568640cb082680c yahoo-buddy-idle-time
    40005b889ee276fbcd0a4e886a68d8a8cce45698 yahoo-status-change-away
    cb46b045aa6e927a3814d9053c2b1c0f08d6fa62 crash-validate-jid

* Sun Sep 06 2009 Stu Tomlinson <stu@nosnilmot.com> 2.6.2-1.1
- VV support needs to be explicitly disabled on F10

* Sun Sep 06 2009 Stu Tomlinson <stu@nosnilmot.com> 2.6.2-1
- 2.6.2 Fixes a number of crashes
- CVE-2009-2703, CVE-2009-3083, CVE-2009-3084, CVE-2009-3085

* Wed Aug 19 2009 Warren Togami <wtogami@redhat.com> 2.6.1-1
- 2.6.1: Fix a crash when some users send you a link in a Yahoo IM

* Tue Aug 18 2009 Warren Togami <wtogami@redhat.com> 2.6.0-1
- CVE-2009-2694
- Voice and Video support via farsight2 (Fedora 11+)
- Numerous other bug fixes

* Thu Aug 06 2009 Warren Togami <wtogami@redhat.com> 2.6.0-0.11.20090812
- new snapshot at the request of maiku

* Thu Aug 06 2009 Warren Togami <wtogami@redhat.com> 2.6.0-0.10.20090806
- new snapshot - theoretically better sound quality in voice chat

* Tue Aug 04 2009 Warren Togami <wtogami@redhat.com> 2.6.0-0.9.20090804
- new snapshot

* Mon Jul 27 2009 Warren Togami <wtogami@redhat.com> 2.6.0-0.8.20090727
- new snapshot

* Mon Jul 27 2009 Stu Tomlinson <stu@nosnilmot.com> 2.6.0-0.6.20090721
- Prevent main libpurple & pidgin packages depending on perl (#513902)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-0.5.20090721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Warren Togami <wtogami@redhat.com> 2.6.0-0.4.20090721
- rebuild

* Tue Jul 21 2009 Warren Togami <wtogami@redhat.com> 2.6.0-0.3.20090721
- prevent crash with no camera when closing vv window

* Tue Jul 21 2009 Warren Togami <wtogami@redhat.com> 2.6.0-0.1.20090721
- 2.6.0 snapshot with voice and video support via farsight2

* Sat Jul 11 2009 Stu Tomlison <stu@nosnilmot.com> 2.5.8-2
- Backport patch from upstream to enable NSS to recognize root CA
  certificates that use MD2 & MD4 algorithms in their signature, as
  used by some MSN and XMPP servers

* Sun Jun 28 2009 Warren Togami <wtogami@redat.com> 2.5.8-1
- 2.5.8 with several important bug fixes

* Mon Jun 22 2009 Warren Togami <wtogami@redhat.com> 2.5.7-2
- glib2 compat with RHEL-4

* Sat Jun 20 2009 Warren Togami <wtogami@redhat.com> 2.5.7-1
- 2.5.7 with Yahoo Protocol 16 support

* Wed May 20 2009 Stu Tomlinson <stu@nosnilmot.com> 2.5.6-1
- 2.5.6

* Mon Apr 20 2009 Warren Togami <wtogami@redhat.com> 2.5.5-3
- F12+ removed krb4

* Tue Mar 03 2009 Stu Tomlinson <stu@nosnilmot.com> 2.5.5-1
- 2.5.5

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Warren Togami <wtogami@redhat.com> 2.5.4-2
- one_time_password plugin
- Eliminate RPATH

* Mon Jan 12 2009 Stu Tomlinson <stu@nosnilmot.com> 2.5.4-1
- 2.5.4

* Fri Dec 26 2008 Warren Togami <wtogami@redhat.com> 2.5.3-1
- 2.5.3

* Sat Nov 22 2008 Warren Togami <wtogami@redhat.com> 2.5.2-6
- Automatically detect booleans to enable build features from dist tag
- Unify RHEL4 and RHEL5 spec with Fedora to make both easier to maintain

* Fri Nov 21 2008 Warren Togami <wtogami@redhat.com> 2.5.2-2
- Upstream backports:
  100: sametime-redirect-null crash
  101: NetworkManager-improvement
  102: no-password-in-dialog-if-not-remembering
  103: temporarily-remember-password-during-auto-reconnect
  104: smilie-theme-change-crash
  105: url_fetch_connect_cb-double-free crash
  106: GtkIMHtmlSmileys-remove-crash
  107: remove-dialog-from-open-dialog-list

* Mon Oct 20 2008 Stu Tomlinson <stu@nosnilmot.com> 2.5.2-1
- 2.5.2
- Generate doxygen API documentation (#466693)

* Tue Sep 16 2008 Stu Tomlinson <stu@nosnilmot.com> 2.5.1-3
- Backport fixes from upstream:
  Add "Has You:" back to MSN tooltips
  Fix crash during removal of your own buddy icon
  Fix crash when handling self signed certificate with NSS SSL

* Tue Sep 16 2008 Stu Tomlinson <stu@nosnilmot.com> 2.5.1-2
- Fix a crash with GNOME proxy enabled (#461951)

* Sun Aug 31 2008 Stu Tomlinson <stu@nosnilmot.com> 2.5.1-1
- 2.5.1

* Sat Aug 23 2008 Stu Tomlinson <stu@nosnilmot.com> 2.5.0-1
- 2.5.0

* Tue Jul 01 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.3-1.1
- Add a patch to build with latest rawhide tcl

* Tue Jul 01 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.3-1
- 2.4.3

* Sat May 17 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.2-1
- 2.4.2

* Tue May 13 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.1-3
- Rebuild for new evolution-data-server
- Clean up default prefs.xml
- Enable nautilus integration plugin by default in prefs.xml (#242289)

* Mon Mar 31 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.1-2
- nss-devel no longer provides mozilla-nss-devel

* Mon Mar 31 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.1-1
- 2.4.1

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.4.0-4
- add Requires for versioned perl (libperl.so)

* Fri Mar 14 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.0-3
- BuildRequire perl(ExtUtils::Embed) for perl 5.10

* Fri Mar 14 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.0-2
- Fix download URL
- Use xdg-open instead of gnome-open (#388521, Ville Skyttä)

* Fri Feb 29 2008 Stu Tomlinson <stu@nosnilmot.com> 2.4.0-1
- 2.4.0

* Mon Feb 11 2008 Stu Tomlinson <stu@nosnilmot.com> 2.3.1-3
- %%{_datadir}/purple should be owned by libpurple (#427807)
- Rebuild for gcc 4.3

* Fri Jan 04 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.3.1-2
- Bump to rebuild against new tcl.

* Fri Dec 07 2007 Stu Tomlinson <stu@nosnilmot.com> 2.3.1-1
- 2.3.1 Many bugfixes

* Tue Nov 27 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.3.0-1
- Fix MSN local display name bug

* Mon Nov 26 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.3.0-1
- 2.3.0

* Wed Oct 24 2007 Warren Togami <wtogami@redhat.com> - 2.2.2-1
- 2.2.2 CVE-2007-4999

* Sun Oct 7 2007 Michel Salim <michel.sylvan@gmail.com> - 2.2.1-2
- BR on avahi-glib-devel to supply complete set of Avahi headers

* Mon Oct 1 2007 Warren Togami <wtogami@redhat.com> - 2.2.1-1
- 2.2.1 with many bug fixes and CVE-2007-4996 DOS fix

* Sat Sep 29 2007 Michel Salim <michel.sylvan@gmail.com> - 2.2.0-3
- Build against avahi proper instead of its HOWL compatibility layer

* Tue Sep 18 2007 Warren Togami <wtogami@redhat.com> - 2.2.0-2
- License clarification
- Backport patches to fix memory leaks
- Backport patches to fix proxy settings & status scores

* Tue Sep 18 2007 Warren Togami <wtogami@redhat.com> - 2.2.0-1
- 2.2.0

* Mon Aug 20 2007 Warren Togami <wtogami@redhat.com> - 2.1.1-1
- 2.1.1

* Wed Aug 15 2007 Warren Togami <wtogami@redhat.com> - 2.1.0-2
- Upstream fix backports
  115: gmail-notification-crash #2323
  117: drag-and-drop-mouse-click-group-header #2333
  118: jabber-confirm-authentication-unencrypted-crash #2493

* Mon Aug 6 2007 Warren Togami <wtogami@redhat.com>
- require exact version of libpurple (#250720)

* Mon Jul 30 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.1.0-1
- 2.1.0
- Only include translations in libpurple instead of duplicating them in
  packages that depend on libpurple anyway

* Tue Jun 19 2007 Warren Togami <wtogami@redhat.com> - 2.0.2-3
- libpurple obsoletes and provides gaim
  This smoothens multilib the upgrade path.

* Fri Jun 15 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.2-1
- 2.0.2

* Wed Jun 6 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-5
- Enable Bonjour support (#242949)
- Fix building against latest evolution-data-server

* Tue Jun 5 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-4
- Fix purple-remote for AIM & ICQ accounts (#240589)
- Add missing Requires to -devel packages
- Add missing BuildRequires for libxml2-devel

* Fri Jun 1 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-2
- Call g_thread_init early (#241883)
- Fix purple-remote syntax error (#241905)

* Mon May 28 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.1-1
- 2.0.1

* Wed May 9 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-3
- Split out Perl plugin support into subpackages
- Add Tcl plugin support in a subpackage

* Sun May 6 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-2
- Silence errors when gconfd-2 is not running

* Sat May 5 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-1.1
- Add perl-devel to BuildRequires

* Fri May 4 2007 Stu Tomlinson <stu@nosnilmot.com> - 2.0.0-1
- 2.0.0
- Add scriptlets to install & uninstall GConf schemas
- Move schema file from libpurple to Pidgin to avoid GConf
  dependencies in libpurple
- rename gaim-fedora-prefs.xml to purple-fedora-prefs.xml

* Tue May 1 2007 Stu Tomlinson <stu@nosnilmot.com>
- Update Gtk icon cache when installing or uninstalling (#238621)
- Don't own all directories we put icons in

* Mon Apr 30 2007 Warren Togami <wtogami@redhat.com> - 2.0.0-0.36.beta7
- pidgin-2.0.0beta7, bug fixes and pref migration handling

* Sat Apr 21 2007 Warren Togami <wtogami@redhat.com> - 2.0.0-0.35.beta7devel
- upstream insists that we remove the Epoch
  rawhide users might need to use --oldpackage once to upgrade
- remove mono and howl cruft

* Wed Apr 18 2007 Stu Tomlinson <stu@nosnilmot.com> - 2:2.0.0-0.34.beta7devel
- Split into pidgin, finch & libpurple, along with corresponding -devel RPMs
- Remove ldconfig for plugin directories
- Fix non-UTF8 %%changelog

* Tue Apr 17 2007 Warren Togami <wtogami@redhat.com> 
- -devel req pkgconfig (#222488)

* Mon Apr 16 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.33.beta7devel
- pidgin-2.0.0 snapshot prior to beta7
- rename gaim to pidgin/purple/finch in various places of spec (not complete)
- ExcludeArch s390, s390x.  It never did work there.
- Include meanwhile plugin by moving to Extras

* Fri Mar 23 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.31.beta6
- Removed debian-02_gnthistory-in-gtk
  Removed debian-03_gconf-gstreamer.patch
  Upstream recommended removing these patches.
- Add fix-buggy-fetch-url
- Enable type_chat and type_chat_nick in default prefs.xml

* Sat Jan 20 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.30.beta6
- 2.0.0 beta6

* Thu Jan 18 2007 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.29.beta5
- Debian patch 17_upnp_crash
- Debian patch 18_jabber-roster-crash

* Mon Dec 11 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.28.beta5
- Debian patch 13_yahoo_webauth_disable
  temporarily disable the broken yahoo web auth fallback

* Wed Dec 06 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.27.beta5
- Debian patch 12_gstreamer-cleanup, hopefully fixes #218070

* Tue Dec 05 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.26.beta5
- Jabber SASL Authentication Crash (#217335)

* Wed Nov 29 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.25.beta5
- GTK File dialog blanked fix (#217768)

* Tue Nov 28 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.24.beta5
- Debian patch 10_text-arrow-keys
- Debian patch 11_reread-resolvconf

* Sun Nov 26 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.23.beta5
- Debian patch 08_jabber-info-crash

* Tue Nov 21 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.22.beta5
- 2.0.0 beta5
- Debian patches
    02_gnthistory-in-gtk
    03_gconf-gstreamer
    04_blist-memleak
    05_url-handler-xmpp
    06_jabber-registration-srv
    07_msn-custom-smiley-crash
- SILC Account Edit Crash

* Tue Nov 21 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.21.beta4
- #212817 Jabber needs cyrus-sasl plugins for authentication

* Wed Nov 15 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.20.beta4
- #215704 Revert Yahoo protocol version identifier

* Wed Nov 8 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.19.beta4
- buildreq NetworkManager-glib-devel FC5+ (katzj)
- #213800 debug window freeze fix
- #212818 IRC SIGPIPE crash fix

* Wed Oct 25 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.17.beta4
- temporary workaround for gstreamer build bug in beta4
  --enable-gstreamer prevented it from working =)
  NOTE: beta4 removed libao support entirely.  Distros that lack gstreamer-0.10+
  will need to use command line sound output from now on.
- Gadu Gadu is re-included in beta4 without requirement of external library

* Mon Oct 23 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.16.beta4
- 2.0.0 beta4
- gaim-text ncurses interface!
- gstreamer integration with FC5+

* Thu Oct 05 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.15.beta3
- delete config.h correctly (rvokal)

* Thu Oct 05 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.14.beta3
- Fix multilib conflict in -devel (#205206)

* Sat Sep 30 2006 Matthias Clasen <mclasen@redhat.com> - 2:2.0.0-0.13.beta3
- Make the tray icon work with transparent panels (#208706)

* Mon Jul 31 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.11.beta3
- rebuild for new libebook

* Tue Jul 25 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.9.beta3
- fix crash with certain UTF-8 names in buddy list (#199590)

* Sat Jul 22 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.8.beta3
- move gaim.pc to -devel (#199761)

* Wed Jul 19 2006 Warren Togami <wtogami@redhat.com> - 2:2.0.0-0.7.beta3
- cleanup spec and update default pref

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2:2.0.0-0.6.beta3.2
- Add BR for dbus-glib-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:2.0.0-0.6.beta3.1
- rebuild

* Wed Jul 05 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.6.beta3
- SILC blank realname failure fix (#173076)

* Thu Jun 29 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.5.beta3
- buildreq libSM-devel (#197241)

* Wed Jun 28 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.4.beta3
- rebuild against libsilc-1.0.2

* Tue Jun 27 2006 Warren Togami <wtogami@redhat.com> 2.0.0-0.3.beta3
- more spec cleanups
- buildreq libXScrnSaver-devel, gettext, intltool, desktop-file-utils
- disable mono for now due to #196877

* Mon Jun 26 2006 Tom "spot" Callaway <tcallawa@redhat.com>
- split out -devel package to meet guidelines

* Mon Jan 23 2006 Tom "spot" Callaway <tcallawa@redhat.com>
- gaim2 version of the spec

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-9
- Ensure that security opt flags are used (#165795)
- Many bug fixes from Peter Lawler (#171350)
  156: Fix Yahoo chatroom ignore on join
  157: Fix Italian yahoo profiles
  158: Strip HTML from status
  159: xmlnode cleanup
  160: Fix crash on non-terminated strings
  161: silc-close-gaim_request-window-prpl-disconnect-p1
  162: silc-close-gaim_request-window-prpl-disconnect-p2
  163: silc-close-gaim_request-window-prpl-disconnect-p3
  164: silc-close-gaim_request-window-prpl-disconnect-p4
  165: silc-close-gaim_request-window-prpl-disconnect-p5
  166: silc-close-gaim_request-window-prpl-disconnect-p6
  167: MSN data corruption fix
  168: msn-kill-convo-close-timeout-notices-p1
  169: msn-kill-convo-close-timeout-notices-p2
  170: msn-kill-convo-close-timeout-notices-p3
  171: forceful-connection_disconnect-not-wipe-password
  172: Clipboard leak and history scrolling fix
  173: smileys-logtype-p1
  174: smileys-logtype-p2
  175: Allow Italics in IRC
  176: Add more authors
  177: Update copyright
  178: Update HACKING doc
  179: Fix doc creation
  180: Fix AIM/ICQ Rate Limiting issue

* Thu Oct 13 2005 Ray Strode <rstrode@redhat.com> - 1:1.5.0-7
- use upstream desktop file (except use generic name, because 
  this is our default instant messaging client)

* Tue Sep 27 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-6
- remove -Wno-pointer-sign, not sure why it was needed earlier
- fix FORTIFY_SOURCE on FC3

* Thu Sep 15 2005 Jeremy Katz <katzj@redhat.com> - 1:1.5.0-5
- rebuild for new e-d-s

* Sun Aug 21 2005 Peter Jones <pjones@redhat.cm> - 1:1.5.0-4
- rebuild for new cairo, add -Wno-pointer-sign
- add -Wno-pointer-sign until somebody maintaining this package makes it build
  without it.

* Sun Aug 14 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-2
- always use -z relro and FORTIFY_SOURCE opt flags for FC3+ and RHEL4+ 
  (compiler simply ignores these flags if they are unsupported)

* Thu Aug 11 2005 Warren Togami <wtogami@redhat.com> - 1:1.5.0-1
- 1.5.0 security and bug fixes
  CAN-2005-2370 Gadu-Gadu memory alignment bug
  CAN-2005-2102 AIM/ICQ non-UTF-8 Filename Crash
  CAN-2005-2103 AIM/ICQ away message buffer overflow

* Tue Aug  9 2005 Jeremy Katz <katzj@redhat.com> - 1:1.4.0-7
- rebuild for new evolution-data-server

* Mon Aug  1 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-6
- FC5+ bash regex replace for -fstack-protector-all (mharris)

* Sun Jul 31 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-5
- FC5+ automatic -fstack-protector-all switch
- 150: MSN buddy names with space disconnect and profile corruption
       (supercedes patch 149)
- 151: Gadu Gadu memory alignment crash
- 152: Rename Group Merge crash
- 153: mailto: parse crash (util.c)
- 154: mailto: parse crash (MSN)
- 155: mailto: parse crash (Zephyr)

* Mon Jul 11 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-4
- 149: MSN username with space disconnect fix
- Do not own perl dir, remove empty files (#162994 jpo)

* Sun Jul 10 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-2
- 148: AIM login crash fix

* Thu Jul 07 2005 Warren Togami <wtogami@redhat.com> 1:1.4.0-1
- 1.4.0

* Thu Jun 09 2005 Warren Togami <wtogami@redhat.com> 1:1.3.1-0
- 1.3.1 more bug fixes
  CAN-2005-1269 CAN-2005-1934
- enable Message Notification plugin by default

* Tue May 10 2005 Warren Togami <wtogami@redhat.com> 1:1.3.0-1
- 1.3.0 many bug fixes and two security fixes
  long URL crash fix (#157017) CAN-2005-1261
  MSN bad messages crash fix (#157202) CAN-2005-1262

* Thu Apr 07 2005 Warren Togami <wtogami@redhat.com> 1:1.2.1-4
- use mozilla-nss everywhere because gnutls is buggy (#135778)

* Wed Apr 06 2005 Warren Togami <wtogami@redhat.com> 1:1.2.1-2
- 147: drag-n-drop URL crash fix

* Sun Apr 03 2005 Warren Togami <wtogami@redhat.com> 1:1.2.1-1
- update to 1.2.1 CAN-2005-0965 CAN-2005-0966 CAN-2005-0967

* Fri Mar 18 2005 Warren Togami <wtogami@redhat.com> 1:1.2.0-1
- update to 1.2.0 (minor bug fixes)

* Mon Mar 07 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-5
- Copy before modifying prefs.xml

* Sun Mar 06 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-4
- 144: POSIX functions became macros, build fix (#150429)
- 145: Fix non-proxy yahoo file transfer
- 146: Fix non-proxy yahoo buddy icons

* Fri Mar 04 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-3
- 143: Gadu Gadu protocol crash fix (#149984)

* Mon Feb 28 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-2
- remove gcc4 conditional since FC4 is gcc4 default

* Thu Feb 24 2005 Warren Togami <wtogami@redhat.com> 1:1.1.4-1
- 1.1.4 with MSN crash fix, g_stat() crash workaround
  CAN-2005-0208 Gaim HTML parsing DoS (another one)

* Tue Feb 22 2005 Warren Togami <wtogami@redhat.com> 1:1.1.3-4
- Test fixes for #149190 and #149304

* Mon Feb 21 2005 Dan Williams <dcbw@redhat.com> 1:1.1.3-3
- Work around #149190 gaim-1.1.3-2 segfaults when calling g_stat()

* Fri Feb 18 2005 Warren Togami <wtogami@redhat.com> 1:1.1.3-2
- 1.1.3 including two security fixes
  CAN-2005-0472 Client freezes when receiving certain invalid messages
  CAN-2005-0473 Client crashes when receiving specific malformed HTML

* Fri Jan 28 2005 Florian La Roche <laroche@redhat.com>
- rebuild

* Thu Jan 20 2005 Warren Togami <wtogami@redhat.com> 1:1.1.2-1
- 1.1.2 with more bugfixes

* Tue Jan 18 2005 Chip Turner <cturner@redhat.com> 1:1.1.1-3
- rebuild for new perl

* Mon Jan 03 2005 Warren Togami <wtogami@redhat.com> 1.1.1-2
- force required glib2 version

* Tue Dec 28 2004 Warren Togami <wtogami@redhat.com> 1.1.1-1
- 1.1.1 (minor bugfixes)

* Thu Dec 2 2004 Warren Togami <wtogami@redhat.com> 1.1.0-1
- upgrade 1.1.0 (mostly bugfixes)
- fix PIE patch

* Sat Nov 20 2004 Warren Togami <wtogami@redhat.com> 1.0.3-3
- make gcc4 conditional

* Sat Nov 20 2004 Daniel Reed <djr@redhat.com> 1.0.3-2
- Rebuild using gcc4
  - To revert, remove "BuildRequires: gcc4" and "CC=gcc4"

* Fri Nov 12 2004 Warren Togami <wtogami@redhat.com> 1.0.3-1
- 1.0.3 another bugfix release

* Tue Oct 19 2004 Warren Togami <wtogami@redhat.com> 1.0.2-1
- 1.0.2 fixes many crashes, endian and other issues

* Tue Oct 19 2004 Warren Togami <wtogami@redhat.com> 1.0.1-3
- nosnilmot: zephyr krb build was broken by thinko

* Wed Oct 13 2004 Warren Togami <wtogami@redhat.com> 1.0.1-2
- CAN-2004-0891

* Thu Oct 07 2004 Warren Togami <wtogami@redhat.com> 1.0.1-1
- update to 1.0.1
- disable naive GNOME session check
- switch to gnutls default (FC3+)

* Mon Sep 27 2004 Warren Togami <wtogami@redhat.com> 1.0.0-5
- djr fixed PIE
- added gnutls option, disabled and favoring mozilla-nss

* Sat Sep 25 2004 Warren Togami <wtogami@redhat.com> 1.0.0-4
- PIE

* Mon Sep 20 2004 Warren Togami <wtogami@redhat.com> 1.0.0-3
- 141: Jabber chat room list fix

* Mon Sep 20 2004 Daniel Reed <djr@redhat.com> 1.0.0-2
- #132967 Remove GenericName

* Sat Sep 18 2004 Warren Togami <wtogami@redhat.com> 1.0.0-1
- 1.0.0

* Wed Sep 01 2004 Warren Togami <wtogami@redhat.com> 0.82.1-2
- enable SILC protocol

* Thu Aug 26 2004 Warren Togami <wtogami@redhat.com> 0.82.1-1
- new upstream point release with crash fix and added translation

* Wed Aug 25 2004 Warren Togami <wtogami@redhat.com> 0.82-2
- 140: Buddy icon pref changing crash fix

* Wed Aug 25 2004 Warren Togami <wtogami@redhat.com> 0.82-1
- Update to 0.82 resolves several security issues and bugs
  CAN-2004-0500, CAN-2004-0754, CAN-2004-0784, CAN-2004-0785
  More details at http://gaim.sourceforge.net/security/

* Mon Aug 16 2004 Warren Togami <wtogami@redhat.com> 0.81-7
- CVS backport 138: GTK Prefs bug fix

* Sun Aug 15 2004 Warren Togami <wtogami@redhat.com> 0.81-6
- CVS backport 137: System Log viewer fd leak

* Sun Aug 15 2004 Warren Togami <wtogami@redhat.com> 0.81-5
- fix substitution for browser back compat
- req fix for htmlview back compat
- update prefs.xml

* Fri Aug 13 2004 Warren Togami <wtogami@redhat.com> 0.81-4
- conditionalize features for alternate target distributions
- remove unnecessary ExclusiveArch
- other cleanups

* Wed Aug 11 2004 Warren Togami <wtogami@redhat.com> 0.81-3
- CVS backport 133: CAN-2004-0500 MSNLP buffer overflow
               134: Select buddy icon in new account crash
               135: Jabber join crash
               136: Jabber tooltip fake self crash

* Mon Aug  9 2004 Daniel Reed <djr@redhat.com> 0.81-2
- #125847 Change gaim.desktop names to "IM"

* Thu Aug 05 2004 Warren Togami <wtogami@redhat.com> 0.81-1
- 0.81
- krb5-devel for Zephyr
- evolution-data-server-devel integration
  plugin disabled by default because it seems very unstable

* Sun Jul 18 2004 Warren Togami <wtogami@redhat.com> 0.80-3
- CVS backport 130, 131: MSN buddy scaling issue fix
               132: Drag and Drop crash fix

* Sat Jul 17 2004 Warren Togami <wtogami@redhat.com> 0.80-2
- CVS backport 129: IRC buddy list flood disconnect fix

* Fri Jul 16 2004 Warren Togami <wtogami@redhat.com> 0.80-1
- update to 0.80
- enable ExtPlacement plugin by default
- Smiley Theme "Default" by default (bug fix)
- Insertions -> Control-{B/I/U} by default

* Mon Jun 28 2004 Warren Togami <wtogami@redhat.com> 0.79-2
- remove tray icon patch temporarily because it seems to cause more
  problems than it solves.
- provide gaim-devel
- CVS backport 128: Cached buddy icons fix

* Fri Jun 25 2004 Warren Togami <wtogami@redhat.com> 0.79-1
- update to 0.79
- update desktop patch
- update header and pkgconfig locations
- update default prefs
- FC3 sed behavior workaround
- temporarily disable evolution integration

* Tue Jun 22 2004 Warren Togami <wtogami@redhat.com> 0.78-8
- rebuilt

* Mon Jun 07 2004 Warren Togami <wtogami@redhat.com> 0.78-7
- CVS backport 125: MSN disconnect on non-fatal error fix
               126: Paste html with img crash fix
               127: Misplaced free fix

* Sat Jun 05 2004 Warren Togami <wtogami@redhat.com> 0.78-4
- CVS backport 123: jabber disconnect fix
               124: log find click fix

* Sun May 30 2004 Warren Togami <wtogami@redhat.com> 0.78-2
- update to 0.78 (without SILC support for now)

* Sun May 09 2004 Warren Togami <wtogami@redhat.com> 0.77-7
- CVS backport 121: byte order badness and crashing copy & paste fix
               122: history.so scroll to bottom in new tabs fix

* Tue May 04 2004 Warren Togami <wtogami@redhat.com> 0.77-6
- CVS backport 118: x86-64 yahoo auth fix
               119: Copy/paste fixes for UCS-2 encoded selection
               120: IRC reconnect segfault fix
- remove relnot.so plugin because it is unusable in FC
- Default enable logging and history.so plugin
          enable autoreconnect plugin
- Fix Gnome Default url handler

* Thu Apr 29 2004 Warren Togami <wtogami@redhat.com> 0.77-3
- remove gnome-open manual, since 0.77 has "GNOME Default" as default.
- update default prefs.xml, disable buddy icons in buddy list
- CVS backport 114: plugin prefs saving fix
               115: autoreconn-suppress-dialogs
               116: fix smileys in dialogs
               117: gtk+ 2.0 compat

* Sun Apr 25 2004 Warren Togami <wtogami@redhat.com> 0.77-1
- 0.77, remove cvs backports

* Thu Apr 15 2004 Warren Togami <wtogami@redhat.com> 0.76-6
- CVS backports:
  111 Prevent Crash during password change if blank fields
  112 Prevent Crash if remote sends invalid characters
  113 Enable /etc/gaim/prefs.xml defaults for new profiles
- Tray Icon enabled by default
- Relabel internal version with V-R

* Wed Apr 14 2004 Warren Togami <wtogami@redhat.com> 0.76-5
- CVS backports: 
  102 Fix ^F keybinding when gtkrc is set to emacs mode
  103 Add Missing File: evolution-1.5.x buildability
  104 When MSN server intermittently has problems accessing buddy list, MSN will crash with 0.76
  105, 106, 107 MSN Error reporting fixes
  108 History plugin causes unnecessary horizontal scrollbars
  109 Fix the text replace plugin 
  110 Prevent message sending while offline

* Fri Apr 09 2004 Warren Togami <wtogami@redhat.com> 0.76-3
- CVS backport: Fix oscar tooltip misbehavior
                Fix yahoo more

* Thu Apr 01 2004 Warren Togami <wtogami@redhat.com> 0.76-2
- 0.76

* Sun Mar 28 2004 Warren Togami <wtogami@redhat.com>
- CVS snapshot
- more spec cleanups

* Tue Mar 16 2004 Warren Togami <wtogami@redhat.com>
- CVS snapshot, generated with automake-1.7.9
- update #4
- update #2 but disable
- #5 no longer needed
- default to gnome-open #6
- some spec cleanup

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 23 2004 Christopher Blizzard <blizzard@redhat.com> 1:0.75-1.1.0
- Include patch that fixes a bunch of buffer-related problems, mostly
  from nectar@freebsd.org and some of my own changes.

* Wed Jan 14 2004 Christopher Blizzard <blizzard@redhat.com> 1:0.75-0
- Update to 0.75.
- Remove mem leak patch that is already included in 0.75.
- Clean up a lot of old unused patches and old source tarballs.

* Fri Dec 12 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.74-10
- Add patch that fixes a large memory leak.

* Thu Dec 04 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.74-9
- Bump release to rebuild for fc2.

* Wed Nov 26 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.74-0
- Upgrade to 0.74
- Include libao-devel and startup-notification-devel to the
  buildreq list

* Mon Nov 03 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.71-2
- Add gtk2-devel to the buildreq list.

* Fri Oct 24 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.71-2
- Include patch that should fix some input problems for ja_JP users

* Fri Oct 17 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.71-1
- Include patch that updates the tray icon to a more recent version

* Mon Sep 29 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.70-0
- Update to 0.70

* Thu Sep 04 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.68-0
- Update to 0.68

* Tue Aug 26 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.66-2
- Change Instant Messenger to Messaging Client

* Wed Jul 23 2003 Jeremy Katz <katzj@redhat.com> 1:0.66-1
- 0.66

* Thu Jul 17 2003 Matt Wilson <msw@redhat.com> 1:0.65-1
- 0.65
- don't include .a or .la files

* Tue Jul 15 2003 Matt Wilson <msw@redhat.com> 1:0.64-2
- rebuild against gtkspell

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Christopher Blizzard <blizzard@redhat.com> 1:0.64-0
- 0.64

* Mon Apr 14 2003 Matt Wilson <msw@redhat.com> 1:0.61-1
- 0.61
- remove prefs patch, no longer needed

* Wed Apr  9 2003 Matt Wilson <msw@redhat.com> 1:0.59.8-1
- use system libtool (#88340)

* Wed Jan 29 2003 Christopher Blizzard <blizzard@redhat.com> 0.59.8-0
- Update to 0.59.8

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 18 2002 Elliot Lee <sopwith@redhat.com> 0.59-11
- Add libtoolize etc. steps

* Tue Dec 17 2002 Elliot Lee <sopwith@redhat.com> 0.59-10
- Rebuild

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- build on all arches

* Fri Aug 09 2002 Christopher Blizzard <blizzard@redhat.com> 0.59-7
- Include patch that uses htmlview instead of calling Netscape
  directly
- Include patch that turns off the buddy ticker and changes the button
  look to the (sane) default.

* Thu Aug 01 2002 Christopher Blizzard <blizzard@redhat.com>
- Fix .desktop file, and put it in the right place.
- More .desktop file fixes

* Tue Jun 25 2002 Christopher Blizzard <blizzard@redhat.com>
- Update to 0.59.
- Disable perl for now.

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 24 2002 Matt Wilson <msw@redhat.com> 0.58-1
- 0.58
- remove applet

* Fri Mar 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.53-1
- Langify

* Wed Mar 13 2002 Christopher Blizzard <blizzard@redhat.com>
- update 0.53

* Thu Feb 21 2002 Christopher Blizzard <blizzard@redhat.com>
- update to 0.52

* Tue Jan 29 2002 Christopher Blizzard <blizzard@redhat.com>
- update to 0.51

* Fri Sep 14 2001 Matt Wilson <msw@redhat.com>
- update to 0.43

* Fri Aug 03 2001 Christopher Blizzard <blizzard@redhat.com>
- Add BuildRequires for gnome-libs-devel (bug #44739)

* Mon Jul 02 2001 Christopher Blizzard <blizzard@redhat.com>
- Add BuildRequires for gnome-core-devel (bug #44739)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Feb 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- make it compile

* Sun Feb 11 2001 Tim Powers <timp@redhat.com>
- updated to 0.11.0pre4 (bug fixes)
- applied Bero's konqueror patch to fix kfm->konq

* Tue Dec  5 2000 Tim Powers <timp@redhat.com>
- updated to 0.11.0pre2
- enable gnome support
- updated ispell to aspell patch
- cleaned up file list

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- updated to 0.10.3

* Fri Nov 10 2000 Tim Powers <timp@redhat.com> 
- update to 0.10.2

* Mon Sep 11 2000 Tim Powers <timp@redhat.com>
- some ideas taken from the package available at the gaim website, mainly to install the applet stuff too.

* Wed Aug 9 2000 Tim Powers <timp@redhat.com>
- added Serial so that we can upgrade from Helix packages from 6.2

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Tue Jul 18 2000 Tim Powers <timp@redhat.com>
- changed default spell checker to aspell from ispell, patched.
- requires aspell

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jun 22 2000 Tim Powers <timp@redhat.com>
- fixed problems with ldconfig PreReq, shouls have been /sbin/ldconfig

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- 0.9.19
- fix ldconfig stuff

* Thu Jun 1 2000 Tim Powers <timp@redhat.com>
- cleaned up spec for use with RPM 4.0 (al la _sysconfdir _datadir etc)
- update to 0.9.17
- yay! a man page!

* Thu May 25 2000 Tim Powers <timp@redhat.com>
- we left a bunch of stuff out, pixmaps, plugins. Fixed
- added applnk entry

* Wed May 10 2000 Tim Powers <timp@redhat.com>
- updated to 0.9.15

* Mon Apr 24 2000 Matt Wilson <msw@redhat.com>
- updated to 0.9.14

* Mon Apr 24 2000 Matt Wilson <msw@redhat.com>
- updated to 0.9.13

* Thu Feb 10 2000 Matt Wilson <msw@redhat.com>
- added patch to prevent floating point errors in lag-o-meter update
  code

* Wed Nov 10 1999 Tim Powers <timp@redhat.com>
- updated to 0.9.10

* Tue Jul 13 1999 Tim Powers <timp@redhat.com>
- rebuilt and put into Powertools 6.1

* Mon Jul 12 1999 Dale Lovelace <dale@redhat.com>
- First RPM Build
