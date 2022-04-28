# i get problems with references to eg Console.bnd on wrong paths
%global debug_package %{nil}

Name:           netsurf
Version:        3.10
Release:        3%{?dist}
Summary:        Lightweight Web Browser with its own layout and rendering engine
License:        GPL-2.0 and MIT
Group:          Productivity/Networking/Web/Browsers
Source0:        http://download.netsurf-browser.org/netsurf/releases/source-full/netsurf-all-%{version}.tar.gz
Source1:        nsmotiffe.tar.gz

Patch100: 		netsurf-all-3.10.sgifixes.patch
Patch101: 		netsurf-motif.patch
URL:            http://www.netsurf-browser.org/
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  openssl-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  zlib-devel
BuildRequires:  gperf
BuildRequires:  vim-common
BuildRequires:  check-devel
BuildRequires:  libidn-devel
BuildRequires:  perl-HTML-Parser
BuildRequires:  perl-Digest-MD5
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel


%description
NetSurf is a lightweight browser with its own layout and rendering engine 
entirely written from scratch. It is small and capable of handling many 
of the web standards in use today.

%prep
%setup -q -n netsurf-all-%{version}
%patch100 -p1 -b .sgifixes
%patch101 -p1 -b .motiffixes
tar xzf ../../SOURCES/nsmotiffe.tar.gz

%global common_make_opts \\\
        V=1 \\\
        VARIANT=debug \\\
        PREFIX=%{_prefix} \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=YES \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO \\\
        NETSURF_USE_RSVG=NO \\\
        NETSURF_USE_IPV6=NO \\\
        NETSURF_USE_LIBICONV_PLUG=NO \\\
        NETSURF_USE_DUKTAPE=YES

%global motif_make_opts %{common_make_opts} TARGET=motif V=1 \\\
        NETSURF_USE_RSVG=NO \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=YES \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO \\\
        NETSURF_USE_IPV6=NO \\\
        NETSURF_USE_LIBICONV_PLUG=NO \\\
        NETSURF_USE_DUKTAPE=YES
#
%build
export CFLAGS="-Wno-error -I/usr/sgug/include/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -liconv"
make %{?_smp_mflags} %{motif_make_opts} 

%install
export CFLAGS="-Wno-error -I/usr/sgug/include/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -liconv"
export PATH="$PATH:/usr/sgug/bin:/usr/sgug/sbin:/usr/bin/X11:/usr/bin:/bin:/usr/sbin:/usr/bsd"
%make_install PREFIX=%{_prefix} %{motif_make_opts}
install -D -m0644 netsurf/frontends/gtk/res/netsurf.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/netsurf.xpm

%files
%{_bindir}/%{name}-motif
%{_datadir}/%{name}
%{_datadir}/pixmaps/netsurf.xpm

%changelog
* Sat Apr 27 2022 drmadison 3.10-3
- fix MOTIF version with GL output

* Sun Jul 04 2021 jenna16bit - 3.10-2
- Minor log removal on SGUG version

* Mon Nov 02 2020 josef radinger <cheese@nosuchhost.net> - 3.10-2
- BuildRequires on expat-devel

* Tue May 26 2020 josef radinger <cheese@nosuchhost.net> - 3.10-1
- bump version
- http://www.nosuchhost.net/bugzilla/show_bug.cgi?id=143
  thanks sincorazon9@gmail.com

* Sat Apr 25 2020 josef radinger <cheese@nosuchhost.net> - 3.9-3
- fix .desktop
- remove dependency on lcms-devel (fixes http://www.nosuchhost.net/bugzilla/show_bug.cgi?id=137)

* Sun Jul 28 2019 josef radinger <cheese@nosuchhost.net> - 3.9-2
- use gtk3

* Sat Jul 27 2019 josef radinger <cheese@nosuchhost.net> - 3.9-1
- bump version
- add BuildRequires on vim-common

* Sat Sep 08 2018 josef radinger <cheese@nosuchhost.net> - 3.8-1
- bump version
- remove patch1

* Tue Oct 24 2017 josef radinger <cheese@nosuchhost.net> - 3.7-1
- bump version

* Sun May 14 2017 josef radinger <cheese@nosuchhost.net> - 3.6-4
- fix fallthrough

* Fri Jan 06 2017 josef radinger <cheese@nosuchhost.net> - 3.6-3
- and fix the desktop-file

* Thu Jan 05 2017 josef radinger <cheese@nosuchhost.net> - 3.6-2
- fix desktop-file-install

* Thu Jan 05 2017 josef radinger <cheese@nosuchhost.net> - 3.6-1
- bump version
- add bison+flex+hostname to buildrequires
- add gdk-pixbuf2-devel ynd perl-Digest-MD5 to buildrequires
- add gdk-pixbuf-query-loaders-%{__isa_bits} to setup-section
- correct path to xpm
#- add libharu-devel to buildrequires
#- fix wrong path (haru.patch)

* Mon Jun 13 2016 Huaren Zhong <huaren.zhong@gmail.com> 3.5
- Rebuild for Fedora

* Sun May 13 2012 andreas.stieger@gmx.de
- update to upstream 2.9
  For a full list of changes, see:
  http://www.netsurf-browser.org/downloads/releases/ChangeLog.txt
- switch to full upstream source tarball with in-tree libraries
- move changelog to .changes file
- remove start script and use binary names as per upstream
- license is GPL-2.0 and MIT
- reformat spec file and add in-tree dependency libraries
- update patches to compile with flags
- add backported upstream netsurf-2.9-libcss-enum-compare.patch
  to compile without -Wno-error=enum-compare
- update .desktop file

* Fri Jun 19 2009 pascal.bleser@opensuse.org
- update to 2.1

* Fri May  1 2009 pascal.bleser@opensuse.org
- update to 2.0
- use latest lempar.c and lemon.c from sqlite

* Sun Mar 23 2008 guru@unixtech.be
- new package
