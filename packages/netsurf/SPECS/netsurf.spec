# i get problems with references to eg Console.bnd on wrong paths
%global debug_package %{nil}

Name:           netsurf
Version:        3.10
Release:        2%{?dist}
Summary:        Lightweight Web Browser with its own layout and rendering engine
License:        GPL-2.0 and MIT
Group:          Productivity/Networking/Web/Browsers
Source0:        http://download.netsurf-browser.org/netsurf/releases/source-full/netsurf-all-%{version}.tar.gz
Source1:        netsurf.desktop

Patch100: 		netsurf-all-3.10.sgifixes.patch
URL:            http://www.netsurf-browser.org/
BuildRequires:  gcc
#BuildRequires:  glibc-devel
BuildRequires:  gtk3-devel
BuildRequires:  libcurl-devel
#BuildRequires:  libglade2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  openssl-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
#BuildRequires:  hostname
BuildRequires:  zlib-devel
#BuildRequires:  lcms-devel
BuildRequires:  gperf
BuildRequires:  vim-common
BuildRequires:  check-devel
BuildRequires:  libidn-devel
BuildRequires:  perl-HTML-Parser
#BuildRequires:  gdk-pixbuf2-devel
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
#export GDK_PIXBUF_MODULE_FILE=/tmp/loaders.cache
#gdk-pixbuf-query-loaders > $GDK_PIXBUF_MODULE_FILE
#cd libcss
#%patch1 -p1 -b .fallthrough

%global common_make_opts \\\
        V=1 \\\
        VARIANT=debug \\\
        PREFIX=%{_prefix} \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=NO \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO \\\
        NETSURF_USE_RSVG=YES \\\
        NETSURF_USE_IPV6=NO \\\
        NETSURF_USE_DUKTAPE=YES

#%global fb_make_opts %{common_make_opts} TARGET=framebuffer \\\
#        NETSURF_USE_RSVG=NO \\\
#        NETSURF_USE_FREETYPE2=YES \\\
#        NETSURF_FB_FONTLIB=freetype \\\
#        NETSURF_FB_FONT_CURSIVE=DejaVuSerif-Italic.ttf \\\
#        NETSURF_FB_FONTPATH=/usr/share/fonts/dejavu
#
%global gtk_make_opts %{common_make_opts} TARGET=gtk2 V=1 \\\
        NETSURF_USE_RSVG=YES \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=NO \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO \\\
        NETSURF_USE_IPV6=NO \\\
        NETSURF_USE_DUKTAPE=YES
#
%build
#export CC=mips-sgi-irix6.5-gcc
#export CXX=mips-sgi-irix6.5-g++
#export CFLAGS="-D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS -I%{_includedir}/libdicl-0.1 $RPM_OPT_FLAGS"
#export CXXFLAGS="-D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS -I%{_includedir}/libdicl-0.1 $RPM_OPT_FLAGS"
#export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
#export CFLAGS="-Wno-error -I%{_includedir}/libdicl-0.1 $RPM_OPT_FLAGS"
export CFLAGS="-Wno-error -I/usr/sgug/include/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -liconv"
#export LDFLAGS="-ldicl-0.1 -liconv $RPM_LD_FLAGS"
#export GDK_PIXBUF_MODULE_FILE=/tmp/loaders.cache
#export PKG_CONFIG_PATH="/usr/sgug/lib32/pkgconfig"
#make PREFIX=%{_prefix} NETSURF_USE_HARU_PDF=NO NETSURF_GTK_MAJOR=3 %{?_smp_mflags}
#make PREFIX=%{_prefix} NETSURF_USE_HARU_PDF=NO TARGET=gtk3 NETSURF_GTK_MAJOR=3 %{?_smp_mflags}
make %{?_smp_mflags} %{gtk_make_opts} 

%install
export CFLAGS="-Wno-error -I/usr/sgug/include/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -liconv"
export PATH="$PATH:/usr/sgug/bin:/usr/sgug/sbin:/usr/bin/X11:/usr/bin:/bin:/usr/sbin:/usr/bsd"
%make_install PREFIX=%{_prefix} TARGET=gtk2 NETSURF_GTK_MAJOR=2
#export PKG_CONFIG_PATH="/usr/sgug/lib32/pkgconfig"
#%make_install PREFIX=%{_prefix} TARGET=gtk3 NETSURF_GTK_MAJOR=3 LDFLAGS="$LDFLAGS $(pkg-config --libs libcss libwebp  glib gtk+-3.0 glib-2.0 libpng16 libjpeg libmng openssl librsvg-2.0 libxml-2.0 zlib libidn expat) -ldicl-0.1 -liconv $RPM_LD_FLAGS"
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
install -D -m0644 netsurf/frontends/gtk/res/netsurf.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/netsurf.xpm

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/%{name}-gtk2
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/netsurf.xpm

%changelog
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
