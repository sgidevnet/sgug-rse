%global debug_package %{nil}

# When releasing a xorg-x11-proto-devel version with updated keysyms,
# rebuild libX11

Summary: X.Org X11 Protocol headers
Name: xorg-x11-proto-devel
Version: 2019.1
Release: 4%{?dist}
License: MIT
URL: https://www.x.org
BuildArch: noarch

Source0:  https://www.x.org/pub/individual/proto/xorgproto-%{version}.tar.bz2

Source40: make-git-snapshot.sh

Patch100: xorgproto.irixfixes.patch

BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.0.2-1
BuildRequires: autoconf automake libtool

%description
X.Org X11 Protocol headers


%prep
%autosetup -n xorgproto-%{version} -p1

# place to make patches
#exit 1

%build
autoreconf -f -i -v
%configure --disable-specs
make %{?_smp_mflags}


%install
%make_install

# remove conflicting glxtokens
rm -f $RPM_BUILD_ROOT%{_includedir}/GL/glxtokens.h

# trim some fat
for i in apple windows trap ; do
    rm -f $RPM_BUILD_ROOT%{_includedir}/X11/extensions/*${i}*
    rm -f $RPM_BUILD_ROOT%{_datadir}/pkgconfig/*${i}*
done

# keep things building even if you have the html doc tools for xmlto installed
rm -f $RPM_BUILD_ROOT%{_docdir}/*/*.{html,svg}

%files
%doc COPYING-*
%doc *.txt
%dir %{_includedir}/GL
%{_includedir}/GL/glxint.h
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxproto.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%dir %{_includedir}/X11
%{_includedir}/X11/DECkeysym.h
%{_includedir}/X11/HPkeysym.h
%{_includedir}/X11/Sunkeysym.h
%{_includedir}/X11/X.h
%{_includedir}/X11/XF86keysym.h
%{_includedir}/X11/XWDFile.h
%{_includedir}/X11/Xalloca.h
%{_includedir}/X11/Xarch.h
%{_includedir}/X11/Xatom.h
%{_includedir}/X11/Xdefs.h
%{_includedir}/X11/Xfuncproto.h
%{_includedir}/X11/Xfuncs.h
%{_includedir}/X11/Xmd.h
%{_includedir}/X11/Xos.h
%{_includedir}/X11/Xos_r.h
%{_includedir}/X11/Xosdefs.h
%{_includedir}/X11/Xpoll.h
%{_includedir}/X11/Xproto.h
%{_includedir}/X11/Xprotostr.h
%{_includedir}/X11/Xthreads.h
%{_includedir}/X11/Xw32defs.h
%{_includedir}/X11/Xwindows.h
%{_includedir}/X11/Xwinsock.h
%{_includedir}/X11/ap_keysym.h
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/xf86dri.h
%{_includedir}/X11/dri/xf86driproto.h
%{_includedir}/X11/dri/xf86dristr.h
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/EVI.h
%{_includedir}/X11/extensions/EVIproto.h
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XI2.h
%{_includedir}/X11/extensions/XI2proto.h
%{_includedir}/X11/extensions/XIproto.h
%{_includedir}/X11/extensions/XKB.h
%{_includedir}/X11/extensions/XKBgeom.h
%{_includedir}/X11/extensions/XKBproto.h
%{_includedir}/X11/extensions/XKBsrv.h
%{_includedir}/X11/extensions/XKBstr.h
%{_includedir}/X11/extensions/XResproto.h
%{_includedir}/X11/extensions/Xv.h
%{_includedir}/X11/extensions/XvMC.h
%{_includedir}/X11/extensions/XvMCproto.h
%{_includedir}/X11/extensions/Xvproto.h
%{_includedir}/X11/extensions/ag.h
%{_includedir}/X11/extensions/agproto.h
%{_includedir}/X11/extensions/bigreqsproto.h
%{_includedir}/X11/extensions/bigreqstr.h
%{_includedir}/X11/extensions/composite.h
%{_includedir}/X11/extensions/compositeproto.h
%{_includedir}/X11/extensions/cup.h
%{_includedir}/X11/extensions/cupproto.h
%{_includedir}/X11/extensions/damageproto.h
%{_includedir}/X11/extensions/damagewire.h
%{_includedir}/X11/extensions/dbe.h
%{_includedir}/X11/extensions/dbeproto.h
%{_includedir}/X11/extensions/dmx.h
%{_includedir}/X11/extensions/dmxproto.h
%{_includedir}/X11/extensions/dpmsconst.h
%{_includedir}/X11/extensions/dpmsproto.h
%{_includedir}/X11/extensions/dri2proto.h
%{_includedir}/X11/extensions/dri2tokens.h
%{_includedir}/X11/extensions/dri3proto.h
%{_includedir}/X11/extensions/ge.h
%{_includedir}/X11/extensions/geproto.h
%{_includedir}/X11/extensions/lbx.h
%{_includedir}/X11/extensions/lbxproto.h
%{_includedir}/X11/extensions/mitmiscconst.h
%{_includedir}/X11/extensions/mitmiscproto.h
%{_includedir}/X11/extensions/multibufconst.h
%{_includedir}/X11/extensions/multibufproto.h
%{_includedir}/X11/extensions/panoramiXproto.h
%{_includedir}/X11/extensions/presentproto.h
%{_includedir}/X11/extensions/presenttokens.h
%{_includedir}/X11/extensions/randr.h
%{_includedir}/X11/extensions/randrproto.h
%{_includedir}/X11/extensions/recordconst.h
%{_includedir}/X11/extensions/recordproto.h
%{_includedir}/X11/extensions/recordstr.h
%{_includedir}/X11/extensions/render.h
%{_includedir}/X11/extensions/renderproto.h
%{_includedir}/X11/extensions/saver.h
%{_includedir}/X11/extensions/saverproto.h
%{_includedir}/X11/extensions/secur.h
%{_includedir}/X11/extensions/securproto.h
%{_includedir}/X11/extensions/shapeconst.h
%{_includedir}/X11/extensions/shapeproto.h
%{_includedir}/X11/extensions/shapestr.h
%{_includedir}/X11/extensions/shm.h
%{_includedir}/X11/extensions/shmproto.h
%{_includedir}/X11/extensions/shmstr.h
%{_includedir}/X11/extensions/syncconst.h
%{_includedir}/X11/extensions/syncproto.h
%{_includedir}/X11/extensions/syncstr.h
%{_includedir}/X11/extensions/vldXvMC.h
%{_includedir}/X11/extensions/xcmiscproto.h
%{_includedir}/X11/extensions/xcmiscstr.h
%{_includedir}/X11/extensions/xf86bigfont.h
%{_includedir}/X11/extensions/xf86bigfproto.h
%{_includedir}/X11/extensions/xf86bigfstr.h
%{_includedir}/X11/extensions/xf86dga.h
%{_includedir}/X11/extensions/xf86dga1const.h
%{_includedir}/X11/extensions/xf86dga1proto.h
%{_includedir}/X11/extensions/xf86dga1str.h
%{_includedir}/X11/extensions/xf86dgaconst.h
%{_includedir}/X11/extensions/xf86dgaproto.h
%{_includedir}/X11/extensions/xf86dgastr.h
%{_includedir}/X11/extensions/xf86vm.h
%{_includedir}/X11/extensions/xf86vmproto.h
%{_includedir}/X11/extensions/xf86vmstr.h
%{_includedir}/X11/extensions/xfixesproto.h
%{_includedir}/X11/extensions/xfixeswire.h
%{_includedir}/X11/extensions/xtestconst.h
%{_includedir}/X11/extensions/xtestext1const.h
%{_includedir}/X11/extensions/xtestext1proto.h
%{_includedir}/X11/extensions/xtestproto.h
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/FS.h
%{_includedir}/X11/fonts/FSproto.h
%{_includedir}/X11/fonts/font.h
%{_includedir}/X11/fonts/fontproto.h
%{_includedir}/X11/fonts/fontstruct.h
%{_includedir}/X11/fonts/fsmasks.h
%{_includedir}/X11/keysym.h
%{_includedir}/X11/keysymdef.h
%{_datadir}/pkgconfig/bigreqsproto.pc
%{_datadir}/pkgconfig/compositeproto.pc
%{_datadir}/pkgconfig/damageproto.pc
%{_datadir}/pkgconfig/dmxproto.pc
%{_datadir}/pkgconfig/dri2proto.pc
%{_datadir}/pkgconfig/dri3proto.pc
%{_datadir}/pkgconfig/fixesproto.pc
%{_datadir}/pkgconfig/fontsproto.pc
%{_datadir}/pkgconfig/glproto.pc
%{_datadir}/pkgconfig/inputproto.pc
%{_datadir}/pkgconfig/kbproto.pc
%{_datadir}/pkgconfig/presentproto.pc
%{_datadir}/pkgconfig/randrproto.pc
%{_datadir}/pkgconfig/recordproto.pc
%{_datadir}/pkgconfig/renderproto.pc
%{_datadir}/pkgconfig/resourceproto.pc
%{_datadir}/pkgconfig/scrnsaverproto.pc
%{_datadir}/pkgconfig/videoproto.pc
%{_datadir}/pkgconfig/xcmiscproto.pc
%{_datadir}/pkgconfig/xextproto.pc
%{_datadir}/pkgconfig/xf86bigfontproto.pc
%{_datadir}/pkgconfig/xf86dgaproto.pc
%{_datadir}/pkgconfig/xf86driproto.pc
%{_datadir}/pkgconfig/xf86vidmodeproto.pc
%{_datadir}/pkgconfig/xineramaproto.pc
%{_datadir}/pkgconfig/xproto.pc
%{_docdir}/xorgproto/*

%changelog
* Wed Dec 30 2020 Julien Maerten <julien@3dw.org> - 2019.1-4
- Remove conflicting glxtokens.h

* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2019.1-3
- Rebuild for jpegturbo + fix bzero issue

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
