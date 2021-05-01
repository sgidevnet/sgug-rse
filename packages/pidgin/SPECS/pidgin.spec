Name:           pidgin
Version:        2.13.0
Release:        18%{?dist}
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

BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel

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

#%%package perl
#Summary:    Perl scripting support for Pidgin
#Requires:   libpurple = %%{version}-%%{release}
#Requires:   libpurple-perl = %%{version}-%%{release}

#%%description perl
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

#$%package -n libpurple-perl
#Summary:    Perl scripting support for libpurple
#Requires:   libpurple = %%{version}-%%{release}
#Requires:   perl(:MODULE_COMPAT_%%(eval "`%%{__perl} -V:version`"; echo $version))

#%%description -n libpurple-perl
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
#%%if 0%%{?has_valgrind}
#rm -f libpurple/valgrind.h
#sed -ie 's/include "valgrind.h"/include <valgrind\/valgrind.h>/' libpurple/plugin.c
#%%endif

%build

# remove after irc-sasl patch has been merged upstream
autoreconf --force --install

# gnutls is buggy so use mozilla-nss on all distributions
%configure --enable-tcl --enable-tk \
           --disable-schemas-install \
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
            --disable-fortify \
            --disable-dbus \
            --disable-nm \
            --disable-doxygen \
            --disable-devhelp \
            --with-x \
            --enable-gnutls=yes \
            --with-gnutls-includes=%{_prefix} \
            --with-gnutls-libs=%{_prefix}

#            --disable-nls \
#

make %{?_smp_mflags} V=1 LIBTOOL=/usr/sgug/bin/libtool

# one_time_password plugin, included upstream but not built by default
cd libpurple/plugins/
make one_time_password.so V=1 LIBTOOL=/usr/sgug/bin/libtool
cd -

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install LIBTOOL=/usr/sgug/bin/libtool

install -m 0755 libpurple/plugins/one_time_password.so $RPM_BUILD_ROOT%{_libdir}/purple-2/

desktop-file-install --vendor pidgin --delete-original              \
                     --add-category X-Red-Hat-Base                  \
                     --dir $RPM_BUILD_ROOT%{_datadir}/applications  \
                     $RPM_BUILD_ROOT%{_datadir}/applications/pidgin.desktop

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

%find_lang pidgin

# Create list of plugins for __requires_exclude
find %{buildroot}/%{_libdir}/purple-2 -name \*.so\* -printf '%f|' | sed -e 's/|$//' > plugins.list

%files
%doc NEWS COPYING AUTHORS README ChangeLog doc/PERL-HOWTO.dox
%{_bindir}/pidgin
%{_libdir}/pidgin/
%{_mandir}/man1/pidgin.*
%{_mandir}/man3/
%{_datadir}/applications/pidgin.desktop
%{_datadir}/pixmaps/pidgin/
%{_datadir}/icons/hicolor/*/apps/pidgin.*
%{_datadir}/appdata/pidgin.appdata.xml

%files devel
%{_includedir}/pidgin/
%{_libdir}/pkgconfig/pidgin.pc

%files -f pidgin.lang -n libpurple
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
* Fri Dec 18 2020 Daniel Hams <daniel.hams@gmail.com> - 2.13.0.18
- Enable desktop file generation so we appear in icon catalog

* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2.13.0.17
- Rebuild for jpegturbo

* Fri Jul 10 2020 Daniel Hams <daniel.hams@gmail.com> - 2.13.0.16
- Fix up params passed to configure

* Sat Jun 20 2020 Unxy <unxy@dontknow.com> - 2.13.0.15
- Import to wip

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
