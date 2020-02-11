%global build_ldflags -Wl,-z,relro -Wl,-z,now -Wl,-rpath -Wl,%{_libdir} -Wl,-rpath -Wl,/usr/lib32

%define _hardened_build 1
Summary: GUI for several command-line debuggers
Name: ddd
Version: 3.3.12
Release: 33%{?dist}
License: GPLv2+
URL: http://www.gnu.org/software/ddd/
#Source0: http://dl.sf.net/ddd/ddd-%{version}.tar.gz
#For rc:
Source0: ftp://alpha.gnu.org/gnu/ddd/ddd-3.3.12.tar.gz
#Source1: ddd.desktop
Source2: ddd.png
Patch1: ddd-3.3.11-lang.patch
#Patch2: ddd-3.3.11-xprint.patch
Patch3: ddd-3.3.11-htmlview.patch
Patch4: ddd-3.3.12-rc1-strclass-includes.patch
Patch5: ddd-3.3.12-debuginfo.patch
Patch6: ddd-3.3.12-GDBAgent-fix.patch

Patch100: ddd.sgilooknfeel.patch

#Requires: gdb, xorg-x11-utils, xterm, gnuplot, xdg-utils, xorg-x11-fonts-ISO8859-1-75dpi, xorg-x11-fonts-ISO8859-1-100dpi, xorg-x11-apps
Requires: gdb
BuildRequires:  gcc-c++
#BuildRequires: motif-devel, ncurses-devel, libXaw-devel
BuildRequires: ncurses-devel
#BuildRequires: elfutils-libelf-devel, xterm 
BuildRequires: elfutils-libelf-devel
#BuildRequires: desktop-file-utils, gdb, xorg-x11-utils, readline-devel, texinfo, autoconf, automake, libtool
BuildRequires: gdb, readline-devel, texinfo, autoconf, automake, libtool, libXpm-devel

%description
The Data Display Debugger (DDD) is a popular GUI for command-line
debuggers like GDB, DBX, JDB, WDB, XDB, the Perl debugger, and the
Python debugger. DDD allows you to view source texts and provides an
interactive graphical data display, in which data structures are
displayed as graphs. You can use your mouse to dereference pointers
or view structure contents, which are updated every time the program
stops. DDD can debug programs written in Ada, C, C++, Chill, Fortran,
Java, Modula, Pascal, Perl, and Python. DDD provides machine-level
debugging; hypertext source navigation and lookup; breakpoint,
watchpoint, backtrace, and history editors; array plots; undo and
redo; preferences and settings editors; program execution in the
terminal emulation window, debugging on a remote host, an on-line
manual, extensive help on the Motif user interface, and a command-line
interface with full editing, history and completion capabilities.

%prep
%setup -qn ddd-%{version}
%patch1 -p1 -b .lang
#%patch2 -p1 -b .xprint
%patch3 -p1 -b .htmlview
%patch4 -p0
%patch5 -p1
%patch6 -p1

%patch100 -p1

%build
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export CPPFLAGS="$CPPFLAGS -D_SGI_SOURCES -D_SGI_REENTRANT_FUNCTIONS -I/usr/Motif-2.1/include -I%{_includedir}"
export PATH="/usr/bin/X11:$PATH"
export LDFLAGS="-L/usr/Motif-2.1/lib32 -lXm $RPM_LD_FLAGS"
export LIBS="-lm"
libtoolize --force
aclocal
autoheader
automake --force-missing --add-missing
autoconf
export CXXFLAGS="${RPM_OPT_FLAGS} -fpermissive"
# Ugly workaround to get the correct libXpm linked in (from rse)
export LDFLAGS="-L%{_libdir} -lXpm $RPM_LD_FLAGS -L/usr/Motif-2.1/lib32"
%configure --with-readline --disable-dependency-tracking --x-includes=/usr/include/X11 --x-libraries=/usr/lib32 --with-xpm-includes=%{_includedir} --with-xpm-libraries=%{_libdir} --with-termlib=tinfo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir*

#desktop-file-install \
#        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
#        --add-category X-Fedora \
#        ddd/ddd.desktop

install -D -m 0644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/ddd.png

%files
%doc AUTHORS COPYING COPYING.DOC CREDITS 
%doc INSTALL NEWS PROBLEMS README TIPS doc/ddd-paper.*
%{_bindir}/ddd
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/ddd
%{_datadir}/%{name}-%{version}/COPYING
%{_datadir}/%{name}-%{version}/NEWS
%config(noreplace) %{_datadir}/%{name}-%{version}/ddd/Ddd
%{_datadir}/%{name}-%{version}/themes/
%{_datadir}/%{name}-%{version}/vsllib/
%{_datadir}/icons/hicolor/48x48/apps/ddd.png
%{_infodir}/ddd*
%{_mandir}/man1/ddd.1*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.12-32
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.3.12-30
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.3.12-24
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.3.12-21
- Rebuilt for GCC 5 C++11 ABI change

* Sat Nov 29 2014 Andy Grover <agrover@redhat.com> - 3.3.12-20
- Add Requires for xorg-x11-apps, for rhbz #1169011

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Andy Grover <agrover@redhat.com> - 3.3.12-18
- Add patch ddd-3.3.12-GDBAgent-fix.patch for rhbz #1108862

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Jon Ciesla <limburgher@gmail.com> - 3.3.12-16
- Switch from lesstif to motif, BZ 1042757,

* Fri Aug 09 2013 Jon Ciesla <limburgher@gmail.com> - 3.3.12-15
- Better debuginfo fix.

* Thu Aug 08 2013 Jon Ciesla <limburgher@gmail.com> - 3.3.12-14
- Fix debuginfo, BZ 994166.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 3.3.12-12
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 3.3.12-10
- Add hardened build.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-9
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Jon Ciesla <limb@jcomserv.net> - 3.3.12-7
- Rebuild for new openmotif, BZ 727312.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 17 2009 Jon Ciesla <limb@jcomserv.net> - 3.3.12-5
- Adopt upstream's .desktop file, BZ 517587.

* Mon Aug 10 2009 Jon Ciesla <limb@jcomserv.net> - 3.3.12-4
- Fix source.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Jon Ciesla <limb@jcomserv.net> - 3.3.12-2
- 3.3.12 final.

* Mon Mar 02 2009 Jon Ciesla <limb@jcomserv.net> - 3.3.12-1.rc1.3
- Desktop file fix, BZ 487811.

* Fri Feb 27 2009 Jon Ciesla <limb@jcomserv.net> - 3.3.12-1.rc1.2
- Includes fix.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.12-1.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 08 2009 Jon Ciesla <limb@jcomserv.net> - 3.3.12-1.rc1
- New upstream.
- Updated htmlview patch.
- Dropped xprint patch, applied upstream.

* Mon Dec 15 2008 Jon Ciesla <limb@jcomserv.net> - 3.3.11-19
- Added font requires, BZ 476531.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.3.11-18
- Autorebuild for GCC 4.3

* Tue Nov 20 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-17
- use xdg-utils to open html pages

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-16
- fix license tag

* Sun Apr  1 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-15
- drop BR on libtermcap-devel, bugzilla 231198

* Sat Jan  6 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-14
- fix Requires, bugzilla 218235

* Fri Sep 29 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-13
- readd extra docs needed to files

* Wed Sep 27 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-12
- get rid of libtool BR, no longer needed
- get rid of libXmu-devel/libXpm-devel BR, unnecessary
- no need to include COPYING.LIB
- don't rm extra doc files, needed for runtime

* Wed Sep 27 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-11
- add lots of interesting docs
- get rid of X-Red-Hat-Extra from desktop file
- mark Ddd as a config file
- set BuildRequires for default tools
- use htmlview as default html viewer

* Mon Sep 25 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-10
- Add missing libtool BR
- Fix mixed tabs/spaces

* Mon Sep 25 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-9
- vendor is fedora for d-f-i
- remove unnecessary BR
- use preferred buildroot
- don't need .gz in the install-info snippet

* Fri Sep 22 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.11-8
- clean up the spec a bit for Fedora Extras

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.3.11-7.1
- rebuild

* Wed May 17 2006 Karsten Hopp <karsten@redhat.de> 3.3.11-7
- add buildrequires elfutils-libelf-devel

* Fri May  5 2006 Adam Jackson <ajackson@redhat.com> - 3.3.11-6
- Remove spurious libXp dependency

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.3.11-5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.3.11-5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 12 2005 Than Ngo <than@redhat.com> 3.3.11-5 
- rebuilt against new openmotif-2.3

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Than Ngo <than@redhat.com> 3.3.11-4
- cleanup specfile, thanks to Matthias Saou

* Tue Nov 08 2005 Than Ngo <than@redhat.com> 3.3.11-3
- get rid of xorg-x11-devel, fix for modular X

* Wed Oct 12 2005 Than Ngo <than@redhat.com> 3.3.11-2
- install icon in correct place #170512

* Thu Jun 09 2005 Than Ngo <than@redhat.com> 3.3.11-1
- 3.3.11
- add workaround for utf8

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 3.3.10-2
- rebuilt against gcc-4

* Mon Nov 15 2004 Than Ngo <than@redhat.com> 3.3.10-1
- update to 3.3.10

* Wed Jun 30 2004 Than Ngo <than@redhat.com> 3.3.9-1
- update to 3.3.9
- make ddd menu try GNOME HIG compliant (#125854)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 09 2004 Than Ngo <than@redhat.com> 3.3.8-4
- fix gcc 3.4 build problem

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004 Than Ngo <than@redhat.com> 3.3.8-2
- rebuild in new build enviroment

* Mon Nov 10 2003 Than Ngo <than@redhat.com> 3.3.8-1
- 3.3.8

* Wed Oct 08 2003 Than Ngo <than@redhat.com> 3.3.7-3
- fixed utf-8 issue, bug #84816

* Thu Aug 21 2003 Than Ngo <than@redhat.com> 3.3.7-2
- install icon in correct place (bug #102794)

* Fri Jun 27 2003 Than Ngo <than@redhat.com> 3.3.7-1
- 3.3.7

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Than Ngo <than@redhat.com> 3.3.6-1
- 3.3.6

* Mon May  5 2003 Than Ngo <than@redhat.com> 3.3.5-1.1
- use smp_mflags

* Mon May  5 2003 Than Ngo <than@redhat.com> 3.3.5-1
- 3.3.5 (bug #89523)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan  2 2003 Than Ngo <than@redhat.com> 3.3.1-22
- disable debug_package

* Wed Nov  6 2002 Tim Powers <timp@redhat.com> 3.3.1-20
- rebuilt to drop old libelf dep
- add NEWS and COPYING files to filelist

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com> 3.3.1-19
- rebuilt with gcc-3.2 (we hope)

* Wed Jul 24 2002 Than Ngo <than@redhat.com> 3.3.1-18
- desktop file issue (bug #69381)

* Sat Jul 20 2002 Than Ngo <than@redhat.com> 3.3.1-17
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jun 08 2002 Than Ngo <than@redhat.com> 3.3.1-15
- PHP DBG support (bug #62180)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Mar 22 2002 Tim Powers <timp@redhat.com>
- rebuilt against openmotif-2.2.2

* Mon Mar 18 2002 Than Ngo <than@redhat.com> 3.3.1-12
- fix broken desktop file (bug #53193)

* Fri Feb 22 2002 Than Ngo <than@redhat.com> 3.3.1-11
- clean up patch file (bug #59935)
- rebuild in new enviroment

* Thu Jan 17 2002 Trond Eivind Glomsrod <teg@redhat.com> 3.3.1-10
- Don't include %%{_infodir}/dir

* Thu Jan 17 2002 Than Ngo <than@redhat.com> 3.3.1-9
- fix bug #52954
- fix to build against gcc 3

* Wed Sep 12 2001 Tim Powers <timp@redhat.com>
- rebuild with new gcc and binutils

* Thu Jul 19 2001 Than Ngo <than@redhat.com>
- add some build requires
- Copyright->License

* Fri Jun 29 2001 Karsten Hopp <karsten@redhat.de>
- add desktop icons (gnome-cpu.png isn't always installed)

* Sun Jun 10 2001 Than Ngo <than@redhat.com>
- buildrequires lesstif-devel

* Tue May 22 2001 Tim Powers <timp@redhat.com>
- built for the distro

* Thu May 03 2001 Than Ngo <than@redhat.com>
- update to 3.3.1, it brings a couple of minor bug fixes

* Sat Feb 03 2001 Than Ngo <than@redhat.com>
- updated to 3.3

* Tue Jan 23 2001 Than Ngo <than@redhat.com>
- updated to 3.2.98, a release candidate for DDD 3.3

* Mon Dec 04 2000 Than Ngo <than@redhat.com>
- updated to 2.3.92 (Bug #16254)

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Sat Jul 22 2000 Tim Powers <timp@redhat.com>
- fixed missing BuildPreReq

* Mon Jul 17 2000 Tim Powers <timp@redhat.com>
- added defattr

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt

* Mon Jun 12 2000 Than Ngo <than@redhat.de>
- rebuild with openmotif-2.1.30 for 7.0
- clean up specfile
- FHS fixes

* Mon May 8 2000 Tim Powers <timp@redhat.com>
- updated to 3.2.1
- use applnk

* Fri Feb 11 2000 Tim Powers <timp@redhat.com>
- applied patch for ddd for use with lesstif 0.89 which caused the "view news"
  etc. help items not to uncompress the news and manual properly, resulting in
  an error message. Patch was from Andreas Zeller
  <andreas.zeller@fmi.uni-passau.de>

* Tue Feb 01 2000 Tim Powers <timp@redhat.com>
- bzipped sources to conserve space
- built for 6.2

* Tue Feb 01 2000 Trond Eivind Glomsrod <teg@pvv.ntnu.no>
- includes pdf doc instead of postscript
- upgraded to 3.2
- changed source locations and URLs to point at the new GNU sites
- now does a make strip
- added GNOME desktop entry


* Fri Jan 07 2000 Trond Eivind Glomsrod <teg@pvv.ntnu.no>
- removed ptrace patch
- now installs pydb
- upgraded to 3.1.99
- removed lots of old log entries

* Thu Aug 19 1999 Tim Powers <timp@redhat.com>
- reapplied patch for ptrace problems with sparc

* Thu Aug 19 1999 Dale Lovelace <dale@redhat.com>
- added ddd.wmconfig

* Thu Jul 1 1999 Tim Powers <timp@redhat.com>
- added the --with-motif-includes= and --with-motif-libraries= lines
  so that it would build
- rebuilt package for Powertools

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.1.5.

* Tue Apr 13 1999 Michael Maher <mike@redhat.com>
- built package for 6.0
- updated package
