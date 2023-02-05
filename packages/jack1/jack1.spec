# This package is able to use optimised linker flags.
#%%global build_ldflags %{sgug_optimised_ldflags}

#%%global __strip /bin/true

%if 0%{?fedora}
%ifnarch s390 s390x
%define _enable_freebob --enable-freebob
%endif
%endif

Summary: The Jack Audio Connection Kit
Name: jack1
Version: 0.125.0
Release: 1%{?dist}
License: GPLv2 and LGPLv2
Group: System Environment/Daemons
Source0: http://www.jackaudio.org/downloads/jack-audio-connection-kit-%{version}.tar.gz
#Source1: %{name}-README.Fedora
#Source2: %{name}-script.pa
#Source3: %{name}-no_date_footer.html
#Source4: %{name}-limits.conf

# For 0.125.0
#Patch100: jack1.sgifixes00.patch
#Patch101: jack1.sgifixes01.patch
#Patch102: jack1.sgifixes02.patch
#Patch103: jack1.sgifixes03.patch

#Patch104: jack1.sgidebugging.patch

Patch1000: jack1.sgifixesnew.patch

URL: http://www.jackaudio.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel >= 1.0.0
BuildRequires: pkgconfig
#BuildRequires: doxygen
BuildRequires: readline-devel, ncurses-devel
BuildRequires: autoconf >= 2.59, automake >= 1.9.3, libtool
%if 0%{?_enable_freebob:1}
BuildRequires: libfreebob-devel >= 1.0.0
%endif

%define groupname jackuser
%define pagroup   pulse-rt

#Requires(pre): shadow-utils
#Requires(post): /sbin/ldconfig
#Requires: pam

# To fix multilib conflicts take a basepoint as following
%define doxyfile	doc/reference.doxygen.in

%description
JACK is a low-latency audio server, written primarily for the Linux
operating system. It can connect a number of different applications to
an audio device, as well as allowing them to share audio between
themselves. Its clients can run in their own processes (ie. as a
normal application), or can they can run within a JACK server (ie. a
"plugin").

JACK is different from other audio server efforts in that it has been
designed from the ground up to be suitable for professional audio
work. This means that it focuses on two key areas: synchronous
execution of all clients, and low latency operation.

%package devel
Summary: Header files for Jack
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
Header files for the Jack Audio Connection Kit.

%package example-clients
Summary: Example clients that use Jack 
Group: Applications/Multimedia
Requires: %{name} = %{version}

%description example-clients
Small example clients that use the Jack Audio Connection Kit.

%prep
# For 0.121.3
#%%setup -q -n jack-audio-connection-kit-%{version}
# For 0.125.0
%setup -q -n jack-audio-connection-kit-%{version}

#%patch100 -p1 -b .sgifixes00
#%patch101 -p1 -b .sgifixes01
#%patch102 -p1 -b .sgifixes02
#%patch103 -p1 -b .sgifixes03
#%patch104 -p1 -b .sgidebugging

%patch1000 -p1 -b .sgifixesnew

#exit 1

# Put custom HTML_FOOTER to avoid timestamp inside
# (recipe was taken from http://fedoraproject.org/wiki/PackagingDrafts/MultilibTricks)
#cp %{SOURCE3} doc/no_date_footer.html

# Fix Doxyfile:
#  - apply custom html footer (#477718, #341621)
#  - avoid font packaging (workaround for #477402, fix will come with #478747)
sed -e 's,^HTML_FOOTER[ \t]*=.*,HTML_FOOTER = no_date_footer.html,;
        s,^GENERATE_LATEX[ \t]*=.*,GENERATE_LATEX = NO,;' %{doxyfile} > %{doxyfile}.new
touch -r %{doxyfile} %{doxyfile}.new
mv -f %{doxyfile}.new %{doxyfile}

%build
export CPPFLAGS="-D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS -I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1"
export LDFLAGS="-ldicl-0.1 -lpthread -ltinfo $RPM_LD_FLAGS"
export ac_cv_func_getopt_long=yes
# x86_64 issue reported by Rudolf Kastl (not checked, but not bad).
# For 0.121.3
autoreconf --force --install
#$SHELL ./autogen.sh

#   --with-default-tmpdir=/dev/shm #
%configure \
    --with-html-dir=%{_docdir} \
    %{?_enable_freebob}%{!?_enable_freebob:--disable-freebob} \
    --disable-oss \
    --disable-portaudio \
    --disable-alsa \
    --with-default-tmpdir=%{_tmppath}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

# can't use the makeinstall macro, jack needs DESTDIR and prefix gets
# added to it and messes up part of the install
make install DESTDIR=$RPM_BUILD_ROOT

# install our limits to the /etc/security/limits.d
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d
#sed -e 's,@groupname@,%groupname,g; s,@pagroup@,%pagroup,g;' \
#    %{SOURCE4} > $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/99-jack.conf

# prepare README.Fedora for documentation including
#install -p -m644 %{SOURCE1} README.Fedora

# install pulseaudio script for jack (as documentation part)
#install -p -m644 %{SOURCE2} jack.pa

# remove extra install of the documentation
rm -fr $RPM_BUILD_ROOT%{_docdir}

# remove *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/jack/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Fix timestamps to avoid multiarch conflicts
find doc/reference -type f | xargs touch -r %{doxyfile}

%clean
rm -rf $RPM_BUILD_ROOT

#%%pre
#getent group %groupname > /dev/null || groupadd -r %groupname
#exit 0

#%%post -p /sbin/ldconfig

#%%postun -p /sbin/ldconfig

%files 
%doc AUTHORS TODO COPYING*
#%%doc README.Fedora
#%%doc jack.pa
%{_bindir}/jackd
%{_bindir}/jack_load
%{_bindir}/jack_unload
%{_bindir}/jack_freewheel
%{_libdir}/jack/
%{_mandir}/man1/jack*.1*
%{_libdir}/libjack.so.*
%{_libdir}/libjackserver.so.*
#%%{_sysconfdir}/security/limits.d/*.conf

%files devel
%doc doc/reference
%{_includedir}/jack/
%{_libdir}/libjack.so
%{_libdir}/libjackserver.so
%{_libdir}/pkgconfig/jack.pc

%files example-clients
%{_bindir}/jack_alias
%{_bindir}/jack_bufsize
%{_bindir}/jack_connect
%{_bindir}/jack_disconnect
%{_bindir}/jack_evmon
%{_bindir}/jack_impulse_grabber
%{_bindir}/jack_iodelay
%{_bindir}/jack_latent_client
%{_bindir}/jack_load_test
%{_bindir}/jack_lsp
%{_bindir}/jack_metro
%{_bindir}/jack_midi_dump
%{_bindir}/jack_midiseq
%{_bindir}/jack_midisine
%{_bindir}/jack_monitor_client
%{_bindir}/jack_netsource
%{_bindir}/jack_property
%{_bindir}/jack_rec
%{_bindir}/jack_samplerate
%{_bindir}/jack_server_control
%{_bindir}/jack_session_notify
%{_bindir}/jack_showtime
%{_bindir}/jack_simple_client
%{_bindir}/jack_simple_session_client
%{_bindir}/jack_transport
%{_bindir}/jack_transport_client
%{_bindir}/jack_wait

%changelog
* Sun Mar 11 2012 Dominik Mierzejewski <rpm@greysector.net> - 0.121.3-1
- update to 0.121.3 (0.120.1 is required audacious-plugins)
- append new binaries to -example-clients subpackage

* Sat Nov 21 2009 Andy Shevchenko <andy@smile.org.ua> - 0.118.0-1
- update to 0.118.0 (should fix #533419)
- remove upstreamed patch
- append new binaries to -example-clients subpackage

* Wed Nov  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.116.2-8
- update to 0.116.2
- make sure we cleanup threads that we open, fixes segfaults (thanks to Ray Strode)

* Tue Oct 27 2009 Dennis Gilmore <dennis@ausil.us> - 0.116.1-7
- dont build libfreebob support on s390 arches

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.116.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Andy Shevchenko <andy@smile.org.ua> - 0.116.1-5
- create file under /etc/security/limits.d instead of limits.conf hack (#506583)
- rename jack-audio-connection-kit.pa to jack.pa in the documentation part

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.116.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 04 2009 Andy Shevchenko <andy@smile.org.ua> - 0.116.1-3
- avoid creation of the LaTeX documentation (temporary fix for #477402)

* Mon Dec 29 2008 Andy Shevchenko <andy@smile.org.ua> - 0.116.1-2
- fix multiarch conflict again (#477718, #341621)

* Sun Dec 14 2008 Andy Shevchenko <andy@smile.org.ua> - 0.116.1-1
- update to last official release
- update URL tag
- update file list accordingly

* Mon Jul 28 2008 Andy Shevchenko <andy@smile.org.ua> 0.109.2-3
- add a new requirement to be ensure we have /etc/security for postinstall
  script (#359291, #456830)
- provide a pulseaudio start script from README.Fedora
- append values for pulse-rt group to the limits.conf
- update README.Fedora regarding to the recent changes

* Sun Jul 20 2008 Andy Shevchenko <andy@smile.org.ua> 0.109.2-2
- apply patch to be work on ppc64 (#451531)
- update README.Fedora to describe integration jack with pulseaudio (#455193)

* Wed Feb 13 2008 Andy Shevchenko <andy@smile.org.ua> 0.109.2-1.1
- update to the last official release

* Mon Jan 21 2008 Andy Shevchenko <andy@smile.org.ua> 0.109.0-1
- update to the last official release (#429162)
- shut up the postinstall script (#359291)

* Sat Oct 20 2007 Andy Shevchenko <andy@smile.org.ua> 0.103.0-5
- fix timestamps to avoid multiarch conflicts (#341621)

* Tue Sep 04 2007 Andy Shevchenko <andy@smile.org.ua> 0.103.0-4
- fix Source Forge's URL scheme

* Thu Aug 16 2007 Andy Shevchenko <andy@smile.org.ua> 0.103.0-3
- fix according to new guidelines:
  - License tag
  - group creation

* Wed May 23 2007 Andy Shevchenko <andy@smile.org.ua> 0.103.0-1
- update to the last official release
- append defaults to the limits.conf (#221785, #235624)

* Wed Mar 07 2007 Andy Shevchenko <andy@smile.org.ua> 0.102.20-4
- drop libtermcap-devel build requirement (#231203)
- create special jackuser group (#221785)

* Sat Oct 28 2006 Andy Shevchenko <andy@smile.org.ua> 0.102.20-3
- fix BuildRequires: libfreebob -> libfreebob-devel

* Tue Oct 24 2006 Andy Shevchenko <andy@smile.org.ua> 0.102.20-2.1
- rebuild with libfreebob (should closed #211751)

* Wed Oct 11 2006 Andy Shevchenko <andy@smile.org.ua> 0.102.20-2.0
- update to 0.102.20
- drop patch0 (already in mainstream)
- no pack jack_transport (build error)
- pack new JACK MIDI files

* Tue Aug 29 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-13
- http://fedoraproject.org/wiki/Extras/Schedule/FC6MassRebuild

* Tue Aug 01 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-12
- use install instead of cp (#200835)

* Tue Jul 04 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-11
- update URL
- add BR: libtool

* Tue Jun 20 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-10
- add BRs: autoconf, automake
  (http://fedoraproject.org/wiki/QA/FixBuildRequires)

* Sat May 27 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-9
- remove --enable-stripped-jackd and --enable-optimize (use default flags)

* Fri May 19 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-8
- uniform directories items at %files section

* Wed May 17 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-7
- change License tag to GPL/LGPL
- remove --enable-shared (it should be default)
- add a -p flag to the line that copies README.Fedora

* Wed May 10 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-6
- apply clock fix for AMD X2 CPUs (please, refer to
  http://sourceforge.net/mailarchive/forum.php?thread_id=8085535&forum_id=3040)

* Wed May 03 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-5
- adjust spec after reviewing

* Thu Apr 27 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-4
- reformatting README.Fedora to 72 symbols width

* Wed Apr 26 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-3
- add README.Fedora
- remove useless BRs

* Mon Apr 24 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-2
- disable oss and portaudio engines
- use /dev/shm as jack tmpdir
- remove capabilities stuff

* Tue Apr 04 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.101.1-1
- update to 0.101.1

* Mon Mar 27 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- update to 0.100.7 (#183912)
- adjust BR (add versions)
- replace files between examples and main packages
- own jack tmpdir

* Fri Mar 17 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- no libs subpackage
- From Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>:
  - added configuration variable to build with/without capabilities
  - added --enable-optimize flag to configure script
  - disabled sse/mmx instructions in i386 build
  - create temporary directory as /var/lib/jack/tmp
  - create and erase tmp directory at install or uninstall
  - try to umount the temporary directory before uninstalling the package

* Fri Mar 03 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- fix spec for extras injection

* Fri Nov 18 2005 Andy Shevchenko <andriy@asplinux.ru>
- exclude *.la files
- use dist tag

* Fri Oct 14 2005 Andy Shevchenko <andriy@asplinux.ru>
- 0.100.0
- no optimization

* Tue Sep 28 2004 Andy Shevchenko <andriy@asplinux.ru>
- 0.99.1

* Fri Aug 20 2004 Andy Shevchenko <andriy@asplinux.ru>
- rebuild from Mandrake
