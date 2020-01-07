Name:		xloadimage
Summary: 	Image viewer and processor
Version:	4.1
Release:	27%{?dist}
License:	MIT
Source0:	ftp://ftp.x.org/R5contrib/%{name}.%{version}.tar.gz
# Patches 0-18 come from Debian 4.1-16.1
# Many thanks to all those who have done work on this package over the years
Patch0:		01_libjpeg-support.dpatch
Patch1:		02_png-support.dpatch
Patch2:		03_security-strfoo.dpatch
Patch3:		04_previous-image.dpatch
Patch4:		05_idelay-manpage.dpatch
Patch5:		06_-Wall-cleanup.dpatch
Patch6:		07_SYSPATHFILE.dpatch
Patch7:		08_manpage-config-path.dpatch
Patch8:		09_xloadimagerc-path.dpatch
Patch9:		10_config.c-HOME-fix.dpatch
Patch10:	11_fork-implies-quiet.dpatch
Patch11:	12_fix-tile.dpatch
Patch12:	13_varargs-is-obsolete.dpatch
Patch13:	14_errno-not-extern.dpatch
Patch14:	15_CAN-2005-0638.dpatch
Patch15:	16_CAN-2005-0639.dpatch
Patch16:	17_security-sprintf.dpatch
Patch17:	18_manpage_fixes.dpatch
Patch18:	19_fix_root_c_resource_leak.dpatch
Patch19:	xloadimage-4.1-ignore-dummy-copyright-variables.patch
Patch20:	xloadimage-4.1-bracketfix.patch
Patch21:	xloadimage-4.1-png-pkg-config.patch
Patch22:	xloadimage-4.1-libtiff4.patch
Patch23:	xloadimage-4.1-png-1.5.patch
Patch24:	xloadimage-4.1-fix-mem-leak.patch
Patch25:	xloadimage-4.1-sub-second-delay.patch
URL:		http://www.frostbytes.com/~jimf/xloadimage.html
#BuildRequires:  gcc
#BuildRequires:	libtiff-devel >= 4.0
#BuildRequires:	libX11-devel, libpng-devel, libjpeg-devel
#BuildRequires:	libICE-devel

%description
Xloadimage is a utility which will view many different types of images 
under X11, load images onto the root window, or dump processed images 
into one of several image file formats. The current version can read 
many different image file types.

A variety of options are available to modify images prior to viewing. 
These options include clipping, dithering, depth reduction, zoom (either 
X or Y axis independently or both at once), brightening or darkening, 
and image merging. When applicable, these options are done automatically 
(eg a color image to be displayed on a monochrome screen will be 
dithered automatically). 

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1 -b .png-pkg-config
%patch22 -p1 -b .tiff4
%patch23 -p1 -b .png15
%patch24 -p1 -b .fix-mem-leak
%patch25 -p1 -b .sub-second-delay

chmod +x configure

%build
%configure
make %{?_smp_mflags}

%install
# First, the binaries:
mkdir -p %{buildroot}%{_bindir}
install -m 0755 uufilter %{buildroot}%{_bindir}
install -m 0755 xloadimage %{buildroot}%{_bindir}
# Next, the symlinks
pushd %{buildroot}%{_bindir}
ln -s xloadimage xsetbg
ln -s xloadimage xview
popd
# The configuration file
mkdir -p %{buildroot}%{_sysconfdir}/X11/
install -m 0644 xloadimagerc %{buildroot}%{_sysconfdir}/X11/Xloadimage
# Now, the man pages
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 0644 xloadimage.man %{buildroot}%{_mandir}/man1/xloadimage.1x
install	-m 0644 uufilter.man %{buildroot}%{_mandir}/man1/uufilter.1x
# And some copies for the symlinks (we can't really make symlinks here because of how rpm 
# compresses man pages)
cp -a %{buildroot}%{_mandir}/man1/xloadimage.1x %{buildroot}%{_mandir}/man1/xsetbg.1x
cp -a %{buildroot}%{_mandir}/man1/xloadimage.1x %{buildroot}%{_mandir}/man1/xview.1x

%files
%doc README mit.cpyrght
%{_bindir}/uufilter
%{_bindir}/xloadimage
%{_bindir}/xsetbg
%{_bindir}/xview
%config(noreplace) %{_sysconfdir}/X11/Xloadimage
%{_mandir}/man1/*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 4.1-14
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan  2 2013 Tom Callaway <spot@fedoraproject.org> - 4.1-13
- fix memory leak caused by opening a lot of files at once then cycling through them with "N"
- enable support for sub-second-delay values
- thanks to Roger Heflin for both patches

* Tue Nov 27 2012 Tom Callaway <spot@fedoraproject.org> - 4.1-12
- fix png 1.5 support

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Tom Callaway <spot@fedoraproject.org> - 4.1-10
- build against libtiff 4 (on Fedora 18+)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Tom Callaway <spot@fedoraproject.org> - 4.1-8
- fix configure and Makefile.in to use pkg-config info on libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.1-7
- Rebuild for new libpng

* Tue Jun 28 2011 Tom Callaway <spot@fedoraproject.org> - 4.1-6
- comment out unused copyright variables
- add missing bracket in C_ARITH_CODING_SUPPORTED conditional in jpeg.c

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.1-2
- drop unnecessary BR: zlib-devel (dragged in by libpng-devel)

* Thu Dec 4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.1-1
- Initial package for Fedora
