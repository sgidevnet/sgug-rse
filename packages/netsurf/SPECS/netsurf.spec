Name:           netsurf
Version:        3.9
Release:        2%{?dist}
Summary:        Compact graphical web browser

# There are MIT licensed bits as well as LGPL-licensed talloc, but most
# files are GPLv2 and that is the computed effective license.
License:        GPLv2
URL:            https://www.netsurf-browser.org/
Source0:        https://download.netsurf-browser.org/netsurf/releases/source-full/netsurf-all-%{version}.tar.gz
Patch100:       netsurf1.irixfixes.patch
Patch101:       netsurf2.irixfixes.patch
Patch102:       netsurf.irixfixes.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gperf
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  openssl-devel
BuildRequires:  gtk3-devel
BuildRequires:  expat-devel
BuildRequires:  curl-devel
BuildRequires:  libpng-devel
#BuildRequires:  /usr/bin/xxd
#BuildRequires:  /usr/bin/hostname
#BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  desktop-file-utils
#BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(sdl)
#BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-util)

%description
NetSurf is a compact graphical web browser which aims for HTML5, CSS and
JavaScript support.

This package ships the version with GTK3 frontend that most users will
want to use.


#%%package fb
#Summary:        Compact graphical web browser (framebuffer frontend)

#%%description fb
#NetSurf is a compact graphical web browser which aims for HTML5, CSS and
#JavaScript support.

#This package ships the version with a special-purpose framebuffer frontend.


%prep
#%%setup -q -n netsurf-all-%{version}
%autosetup -p1 -n netsurf-all-%{version}


%global common_make_opts V=1 PREFIX=%{_prefix} \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=YES \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO

%global fb_make_opts %{common_make_opts} TARGET=framebuffer \\\
        NETSURF_USE_RSVG=NO \\\
        NETSURF_USE_FREETYPE2=YES \\\
        NETSURF_FB_FONTLIB=freetype \\\
        NETSURF_FB_FONT_CURSIVE=DejaVuSerif-Italic.ttf \\\
        NETSURF_FB_FONTPATH=/usr/share/fonts/dejavu

%global gtk_make_opts %{common_make_opts} TARGET=gtk3 \\\
        NETSURF_USE_RSVG=YES \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=NO \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO \\\
        NETSURF_USE_IPV6=NO
 

%build
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
#%make %{?_smp_mflags} %{fb_make_opts}
make %{?_smp_mflags} %{gtk_make_opts}


%install
#%%make_install %{fb_make_opts}
%make_install %{gtk_make_opts}

mkdir -p %{buildroot}%{_datadir}/pixmaps \
        %{buildroot}%{_datadir}/applications
install -pm644 netsurf/frontends/gtk/res/netsurf.xpm \
        %{buildroot}%{_datadir}/pixmaps
sed 's/Exec=netsurf-gtk/Exec=netsurf-gtk3/;s/netsurf.png/netsurf/' \
        <netsurf/frontends/gtk/res/netsurf-gtk.desktop \
        >%{buildroot}%{_datadir}/applications/netsurf-gtk.desktop
desktop-file-validate \
        %{buildroot}%{_datadir}/applications/netsurf-gtk.desktop


%files
%{_bindir}/netsurf-gtk3
%{_datadir}/netsurf
%{_datadir}/applications/netsurf-gtk.desktop
%{_datadir}/pixmaps/netsurf.xpm


#%%files fb
#%%{_bindir}/netsurf-fb
#%%{_datadir}/netsurf


%changelog
* Tue Dec 01 2020  HAL <notes2@gmx.de> - 3.9-2
- compiles on Irix 6.5 with sgug-rse gcc 9.2.
  this is wip and needs debugging since it is very unstable.

* Sat Jan 25 2020 Lubomir Rintel <lkundrak@v3.sk> - 3.9-2
- Add fb subpackage

* Sun Jan 12 2020 Lubomir Rintel <lkundrak@v3.sk> - 3.9-1
- Initial packaging
