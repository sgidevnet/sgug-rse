Name:           xgalaxy
Version:        2.0.34
Release:        31%{?dist}
Summary:        Arcade game: shoot down the space ships attacking the planet
License:        GPL+
URL:            http://sourceforge.net/projects/xgalaga/
Source0:        http://downloads.sourceforge.net/xgalaga/xgalaga_%{version}.orig.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-hyperspace.desktop
Patch0:         http://ftp.debian.org/debian/pool/main/x/xgalaga/xgalaga_2.0.34-44.diff.gz
Patch1:         %{name}-2.0.34-fullscreen.patch
Patch2:         %{name}-2.0.34-%{name}.patch
Patch3:         %{name}-2.0.34-joy.patch
Patch4:         %{name}-2.0.34-fullscreen-viewport.patch
Patch5:         %{name}-2.0.34-alsa.patch
Patch6:         %{name}-2.0.34-dga-compile-fix.patch
BuildRequires:  libXt-devel libXpm-devel libXmu-devel libXxf86vm-devel
#BuildRequires:  alsa-lib-devel desktop-file-utils ImageMagick gcc
Requires:       hicolor-icon-theme
Obsoletes:      xgalaga <= %{version}
Provides:       xgalaga = %{version}-%{release}

%description
Arcade game for the X Window System where you have to shoot down the space
ships attacking the planet.
 

%prep
%setup -q -n xgalaga-%{version}
# many thanks to Debian for all their excellent work on xgalala
%patch0 -p1 -z .deb
%patch1 -p1 -z .fs
%patch2 -p1 -z .%{name}
%patch3 -p1 -z .joy
%patch4 -p1 -z .viewport
%patch5 -p1 -z .alsa
%patch6 -p1 -z .no-dga
sed -e 's/Debian/Fedora/g' debian/README.Debian > README.fedora
cat >> README.fedora << EOF

The latest Fedora %{name} package also includes fullscreen support, start
%{name} with -window to get the old windowed behavior. You can switch on the
fly between window and fullscreen mode with alt+enter.
EOF

# Change the name everywhere as upstreams name has already been used for a game
# much like this one in the past, upstreams use of this is a legal gray area.
sed -i 's/xgalaga/xgalaxy/g' `grep -rls xgalaga .`
sed -i 's/XGalaga/XGalaxy/g' `grep -rls XGalaga .`


%build
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DXF86VIDMODE"
export LDFLAGS=-lXxf86vm
./configure --libdir=%{_libdir} --exec-prefix=%{_bindir} \
  --prefix=%{_datadir}/%{name}
sed -i s/xgal.sndsrv.oss/xgal.sndsrv.alsa/ Makefile
make %{?_smp_mflags} SOUNDLIBS=-lasound
# convert images/player3.xpm %{name}.png


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# move the sound-server binary out of %{_datadir}
#mv $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa \
#  $RPM_BUILD_ROOT%{_bindir}
#ln -s ../../bin/xgal.sndsrv.alsa \
#  $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa
# fix useless exec bit
chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/*/*
# make install doesn't install the manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 xgal.6x $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install         \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install        \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
#mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps
#install -p -m 644 %{name}.png \
#  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps

%files
%doc CHANGES COPYING README README.fedora
%{_bindir}/%{name}*
#%%{_bindir}/xgal.sndsrv.alsa
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/applications/%{name}*.desktop
#%%{_datadir}/icons/hicolor/22x22/apps/%{name}.png


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.34-27
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.34-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.0.34-18
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov  5 2009 Hans de Goede <hdegoede@redhat.com> 2.0.34-14
- Fix sound not working (replace oss code with alsa code)
- Fix building with latest libXxf86dga headers

* Thu Sep 10 2009 Hans de Goede <hdegoede@redhat.com> 2.0.34-13
- Fix (workaround) viewport issues in fullscreen mode (#522116)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Hans de Goede <hdegoede@redhat.com> 2.0.34-10
- Update description for new trademark guidelines

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 2.0.34-9
- Fix patch fuzz build failure

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.34-8
- Autorebuild for GCC 4.3

* Fri Aug 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.34-7
- Update Debian patch to the 2.0.34-44 version

* Thu Aug 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.34-6
- Update License tag for new Licensing Guidelines compliance
- Add iconcache update scriptlets

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.34-5
- FE6 Rebuild

* Thu Jun  1 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.34-4
- Workaround broken glibc-kernheaders (bz 193747).
- Add Provides and Obsoletes xgalaga in case people have an xgalaga package
  installed from another source.

* Wed May 31 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.34-3
- Fixed ships not being centered when flying in in level 1
- Fixed artifacts (ships not yet on screen showing) in level 2
- Added -winsize widthxheight option, which can be used to specify an
  alternative window size
- Documented the -level, -window, -winsize switch in the manpage.

* Mon May 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.34-2
- Change name to xgalaxy because upstreams name has already been used for a
  game much like this one in the past, upstreams use of this name thus legally
  is a bit dodgy.
- Add missing BR: libXxf86vm-devel
- Stop using %%{__sed} just use sed, to be consistent with the way make, rm,
  etc. are called. 
- Package the included manpage.

* Thu May 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.34-1
- Initial packaging based on spec file by Michael A. Peters <mpeters@mac.com>
