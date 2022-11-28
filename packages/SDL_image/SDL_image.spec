%global _hardened_build 1
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro -Wl,-z,now}

Name:		SDL_image
Version:	1.2.12
Release:	22%{?dist}
Summary:	Image loading library for SDL

License:	LGPLv2+
URL:		http://www.libsdl.org/projects/SDL_image/
Source0:	http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
Patch0:         SDL_image-1.2.12-interlaced-png-warning-fix.patch

BuildRequires:  gcc
BuildRequires: 	SDL-devel >= 1.2.10
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL surfaces.


%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.10
Requires:	pkgconfig


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
# XCF support is crashy in 1.2.4
%configure --disable-dependency-tracking	\
	--enable-tif				\
	--enable-jpg-shared			\
	--enable-png-shared			\
	--disable-static
make %{?_smp_mflags}

#        --enable-tif-shared                     \

%install
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_bindir}
./libtool --mode=install /usr/sgug/bin/install showimage $RPM_BUILD_ROOT%{_bindir}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


#%%ldconfig_scriptlets


%files
%doc README CHANGES COPYING
%{_bindir}/showimage
%{_libdir}/lib*.so.*


%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Feb 14 2021  HAL <notes2@gmx.de> - 1.2.12-22
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.12-19
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Hans de Goede <hdegoede@redhat.com> - 1.2.12-13
- Fix runtime warnings when loading interlaced pngs (rhbz#829419)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 Moez Roy <moez.roy@gmail.com> - 1.2.12-11
- Add global harderning flags

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.2.12-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.2.12-4
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.12-2
- Rebuild for new libtiff.

* Tue Jan 31 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.12-1
- New upstream.
- libpng15 patch upstreamed.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 06 2011 Jon Ciesla <limb@jcomserv.net> - 1.2.10-3
- Rebuilt for libpng 1.5.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 18 2010 Brian Pepple <bpepple@fedoraproject.org> - 1.2.10-1
- Update to 1.2.10.

* Sun Aug  9 2009 Brian Pepple <bpepple@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7.
- Drop IMG_lbm patch.  Fixed upstream.
- Drop buffer overflow patch.  Fixed upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.6-6
- Rebuild for gcc-4.3.

* Tue Jan 29 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.6-5
- Add patch to fix ILBM image buffer overflow. (#430693)

* Thu Jan 24 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.6-4
- Add patch to fix buffer-overflow. (#430100)

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.6-3
- Rebuild.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.6-2
- Update license tag.

* Mon Jul 30 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6.
- remove IMG_xpm patch.  fixed upstream.

* Tue Dec 19 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.2.5-4
- Disable run-time loading of libs. (#219902)

* Tue Oct 31 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.2.5-3
- Add patch to fix IMG_ReadXPMFromArray crash. (#213282)

* Thu Aug 31 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.2.5-2
- Rebuild for FC6.

* Sat Aug 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5.
- Simplify description & summary for devel package.
- Update SDL version required.
- Use disable-static configure flag.

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 1.2.4-5
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Sep 27 2005 Brian Pepple <bdpepple@ameritech.net> - 1.2.4-4
- Bump release so it upgrades from FC4.
- General spec formatting cleanup.

* Sat Jun 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.4-2
- Rebuild.

* Sun Jun 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.4-1
- 1.2.4, patches obsolete.
- Bring back TIFF support (BuildRequire libtiff-devel).
- Build with dependency tracking disabled.
- Require exact EVR of main package in -devel.

* Thu May 26 2005 Bill Nottingham <notting@redhat.com> 1.2.3-9
- rebuild

* Wed Feb  9 2005 Thomas Woerner <twoerner@redhat.com> 1.2.3-7
- rebuild

* Thu Sep 30 2004 Thomas Woerner <twoerner@redhat.com> 1.2.3-6
- moved to new autofoo utils

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 18 2003 Thomas Woerner <twoerner@redhat.com> 1.2.3-3
- fixed build with automake-1.7

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May  6 2003 Thomas Woerner <twoerner@redhat.com> 1.2.3-1
- new version 1.2.3

* Mon Feb 17 2003 Elliot Lee <sopwith@redhat.com>
- ppc64 fix

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sun Dec 01 2002 Elliot Lee <sopwith@redhat.com>
- Remove unpackaged files

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-1
- 1.2.2

* Fri Mar  1 2002 Than Ngo <than@redhat.com> 1.2.1-4
- rebuild in new env

* Thu Jan 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-3
- Rebuild to get rid of superfluous dependencies
- Clean up spec file

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jan  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-1
- 1.2.1
- Require arts-devel rather than the obsolete kdelibs-sound-devel

* Fri Oct 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.0-4
- Rebuild with new libpng

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add build requirements (#49827)

* Tue Jul 10 2001 Elliot Lee <sopwith@redhat.com>
- Rebuild

* Sun Apr 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.2.0

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.1.0
- Use %%post -p, %%postun -p
- devel requires %%{name} = %%{version} rather than just %%{name}
- enable tiff support

* Tue Dec 19 2000 Than Ngo <than@redhat.com>
- added missing %%post and %%postun

* Wed Nov 29 2000 Than Ngo <than@redhat.com>
- first build for 7.1
