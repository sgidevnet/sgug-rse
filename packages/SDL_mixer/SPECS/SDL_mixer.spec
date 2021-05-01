Name:		SDL_mixer
Version:	1.2.12
Release: 	18%{?dist}
Summary:	Simple DirectMedia Layer - Sample Mixer Library

License:	LGPLv2
URL:		http://www.libsdl.org/projects/SDL_mixer/
Source0:	http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz

# MikMod-related fixes from trunk
Patch0:         SDL_mixer-MikMod-1.patch
Patch1:         SDL_mixer-MikMod-2.patch

BuildRequires:  gcc
BuildRequires:	SDL-devel >= 1.2.10 
BuildRequires:	libvorbis-devel
BuildRequires:	flac-devel
BuildRequires:	mikmod-devel >= 3.1.10
#BuildRequires:	fluidsynth-devel
# Require libvorbis since we build it with dynamically load support.
Requires:	libvorbis
Requires:	libmikmod
#Requires:	fluidsynth

%description
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD, Timidity MIDI and Ogg Vorbis libraries.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.10
Requires:	libvorbis-devel
Requires:	libmikmod-devel
#Requires:	fluidsynth-devel
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --disable-dependency-tracking	\
	   --disable-static 			\
	   --enable-music-libmikmod

# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Upstream bug for proper fixing of the lack of -lm:
# http://bugzilla.libsdl.org/show_bug.cgi?id=1010
make %{?_smp_mflags} LDFLAGS=-lm


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall install-bin

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

#%%ldconfig_scriptlets

%files
%doc README CHANGES COPYING
%{_bindir}/playmus
%{_bindir}/playwave
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/SDL

%changelog
* Sun Feb 14 2021  HAL <notes2@gmx.de> - 1.2.12-18
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 03 2015 Jon Ciesla <limburgher@gmail.com> - 1.2.12-10
- Fix -devel BR.

* Thu Sep 03 2015 Jon Ciesla <limburgher@gmail.com> - 1.2.12-9
- Enable fluidsynth support, BZ 1218776.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012 Jan Dvorak <mordae@anilinux.org> - 1.2.12-3
- Apply MikMod-related fixes from trunk to prevent crashes.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.12-1
- New upstream.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 24 2010 Hans de Goede <hdegoede@redhat.com> 1.2.11-4
- link SDL_mixer with -lm (#607357)

* Thu Jun 17 2010 Thomas Janssen <thomasj@fedorapeople.org> 1.2.11-3
- added R libmikmod
- #571177 #584211

* Sat May 01 2010 Thomas Janssen <thomasj@fedorapeople.org> 1.2.11-2
- added flac support

* Mon Jan 18 2010 Brian Pepple <bpepple@fedoraproject.org> - 1.2.11-1
- Update to 1.2.11.
- Drop timidity path patch.  Fixed upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr  5 2009 Peter Robinson <pbrobinson@gmail.com> - 1.2.8-12
- Remove dependency on timidity++-patches

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Peter Robinson <pbrobinson@gmail.com> - 1.2.8-10
- Add Provides: SDL_mixer-midi in prep for moving samples to sub-package

* Sun Aug 10 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-9
- Add requires on libvorbis.

* Sun Feb 17 2008 Jesse Keating <jkeating@redhat.com> - 1.2.8-8
- Rebuild for new mikmod.

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-7
- Rebuild for gcc-4.3.

* Tue Jan  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-6
- Pulseaudio hack has been moved to SDL. (#427865) 

* Mon Nov 12 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-5
- link against system libmikmod. (#355991)

* Tue Oct 30 2007 Warren Togami <wtogami@redhat.com> - 1.2.8-4
- SDL_AUDIODRIVER=esd temporary hack until SDL supports pulseaudio directly
  avoids applications from locking up. (#358341)

* Mon Oct 15 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-3
- Change requires to timidity++-patches. (#331431)

* Tue Aug 28 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-2
- Rebuild.

* Mon Jul 30 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8.
- Drop requires on SDL, since the devel soname will pull it in.
- Drop volume patch.  fixed upstream.
- Drop reopen patch.  fixed upstream.
- Drop bad-code patch.  fixed upstream.
- Bump min version of SDL needed.
- Bump min version of mikmod needed.

* Sat Jul 14 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.7-3
- Add patch fix eopening issue. (#248253)

* Thu Aug 31 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.2.7-2
- Rebuild for FC6.

* Fri Aug 25 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7.
- Update bad-code & timidity patches.
- Simplify description & summary for devel package.
- Use disable-static configure flag.
- Drop 64bit patch, fixed upstream.
- Drop libmikmod.patch, fixed upstream.
- Add patch to allow control volume w/playmus. Bug #203210.

* Sun Apr 23 2006 Brian Pepple <bdpepple@ameritech.net> - 1.2.6-8
- Add patch to fix sound on x86_64. Bug #175672.

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 1.2.6-6
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Nov 16 2005 Brian Pepple <bdpepple@ameritech.net> - 1.2.6-5
- Add requires for timidity++ to fix bug #173393.

* Tue Nov  8 2005 Brian Pepple <bdpepple@ameritech.net> - 1.2.6-4
- Add libmikmod patch to fix Bug #171562. (Thanks, Ville)

* Tue Sep 27 2005 Brian Pepple <bdpepple@ameritech.net> - 1.2.6-3
- Cleanup up spec formatting.

* Sat Jun 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.6-2
- Rebuild.

* Sun Jun 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.6-1
- 1.2.6, use system libmikmod.
- Drop obsolete patches, *.la and over-eager cleanup from %%clean.
- Build with dependency tracking disabled.

* Thu Jun 16 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2.5-10.1
- Make -devel package require exact release of main package (this
  is particularly important for API changes such as in 1.2.5-9).

* Thu Jun  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.5-9
- Bring back Ogg support (BuildRequire libvorbis-devel).
- Add SDL-devel dependency to -devel.
- Improve description.

* Thu May 26 2005 Bill Nottingham <notting@redhat.com> 1.2.5-7
- rebuild

* Wed Feb  9 2005 Thomas Woerner <twoerner@redhat.com> 1.2.5-5
- rebuild

* Thu Sep 30 2004 Thomas Woerner <twoerner@redhat.com> 1.2.5-4
- moved to new autofoo utils

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr 22 2004 Thomas Woerner <twoerner@redhat.com> 1.2.5-2
- fixed bad code in effect_position.c
- cleaned up build

* Tue Mar  9 2004 Thomas Woerner <twoerner@redhat.com> 1.2.5-1
- new version 1.2.5
- cleaned up spec file
- installing playmus and playwave by hand (not installed automatically anymore)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 17 2003 Elliot Lee <sopwith@redhat.com> 1.2.4-8
- ppc64 fix

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Tim Powers <timp@redhat.com>
- bump and rebuild
- use pushd and popd instead of cd'ing into the buildroot

* Sat Oct 12 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add 64bit patch

* Wed Aug 28 2002 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jul 18 2002 Bill Nottingham <notting@redhat.com> 1.2.4-4
- build against current libvorbis

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Bernhard Rosenkraeenzer <bero@redhat.com> 1.2.4-1
- 1.2.4
- clean up spec file

* Fri Mar  1 2002 Than Ngo <than@redhat.com> 1.2.1-4
- rebuild in new env

* Thu Jan 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-3
- Rebuild to get rid of superfluous dependencies
  [dependencies removed from SDL-1.2.3-5]

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jan  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-1
- Require arts-devel rather than the obsolete kdelibs-sound-devel
- Update to 1.2.1
- Fix build with current auto* tools

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add more build dependencies (#49828)

* Tue Jul 10 2001 Elliot Lee <sopwith@redhat.com>
- Rebuild

* Fri Jun 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- do not delete acinclude.m4 in spec file

* Sun Apr 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.2.0

* Tue Jan 16 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Require arts, not kdelibs-sound

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.1.0
- Fix %%post, %%postun
- Fix summary line for -devel

* Wed Nov 29 2000 Than Ngo <than@redhat.com>
- added ftp site

* Mon Nov 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.0.6
- Requires: smpeg
- BuildRequires: SDL-devel
- Look for timidity.cfg in the right place

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt lkto fix bad dir perms

* Tue Nov 14 2000 Tim Powers <timp@redhat.com>
- updated to 1.0.6

* Wed Aug 02 2000 Than Ngo <than@redhat.de>
- move libSDL_mixer.so in SDL_mixer-devel

* Tue Aug 1 2000 Tim Powers <timp@redhat.com>
- added post and postun sections with /sbin/ldconfig

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt
- use RPM macros

* Mon Jun 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial build for Red Hat Powertools
- fix build with current libtool

* Wed Jan 19 2000 Sam Lantinga 
- converted to get package information from configure

* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file

