Name:           mikmod
Version:        3.2.8
Release:        7%{?dist}
Summary:        Console music module player

License:        GPLv2 and LGPLv2+
URL:            http://mikmod.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mikmod/%{name}-%{version}.tar.gz

#BuildRequires:  gcc
#BuildRequires:  ncurses-devel
BuildRequires:  libmikmod-devel

%description
MikMod is one of the best and most well known MOD music file players
for UNIX-like systems.  This particular distribution is intended to
compile fairly painlessly in a Linux environment. MikMod uses the OSS
/dev/dsp driver including all recent kernels for output, and will also
write .wav files. Supported file formats include MOD, STM, S3M, MTM,
XM, ULT, and IT.  The player uses ncurses for console output and
supports transparent loading from gzip/pkzip/zoo archives and the
loading/saving of playlists.

Install the mikmod package if you need a MOD music file player.

%prep
%autosetup

%build
#%configure --with-libmikmod-prefix=/usr/sgug --with-libmikmod-exec-prefix=/usr/sgug --disable-libmikmodtest --libdir=/usr/sgug
#%configure --disable-libmikmodtest --exec-prefix=/usr/sgug
%configure 
%make_build

%install
%make_install INSTALL="install -p"

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.8-1
- Update to 3.2.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.2.7-3
- Cleanups in spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Hans de Goede <hdegoede@redhat.com> - 3.2.7-1
- New upstream release 3.2.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 10 2014 Hans de Goede <hdegoede@redhat.com> - 3.2.6-1
- New upstream release 3.2.6 (rhbz#1139003)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar  8 2014 Hans de Goede <hdegoede@redhat.com> - 3.2.5-1
- New upstream release 3.2.5

* Sun Oct 20 2013 Hans de Goede <hdegoede@redhat.com> - 3.2.4-1
- New upstream and new upstream release 3.2.4
- Drop our last patch

* Mon Oct 14 2013 Hans de Goede <hdegoede@redhat.com> - 3.2.3-1
- New upstream and new upstream release 3.2.3
- Drop a bunch of merged patches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 24 2012 Jindrich Novy <jnovy@redhat.com> 3.2.2-19
- update to 3.2.2 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-18.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 11 2011 Dennis Gilmore <dennis@ausil.us> - 3.2.2-17.beta1
- arm needs the same floor symbol fix as s390(x)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-16.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Dan Horák <dan[at]danny.cz> 3.2.2-15.beta1
- fix build on s390(x), the "floor" symbol in libmikmod must be resolved using libm

* Wed Dec  1 2010 Jindrich Novy <jnovy@redhat.com> 3.2.2-14.beta1
- fix off-by-one in get_command() and add various code sanity fixes
- remove unused macro from spec

* Fri Aug 28 2009 Jindrich Novy <jnovy@redhat.com> 3.2.2-13.beta1
- rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.2.2-12.beta1
- Use bzipped upstream tarball.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-11.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-10.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 14 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 3.2.2-9.beta1
- Fix /usr/share/mikmod directory being unowned (bz 442313)

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 3.2.2-8.beta1
- Fix missing prototype compiler warnings

* Fri Feb 15 2008 Jindrich Novy <jnovy@redhat.com> 3.2.2-7.beta1
- rebuild against new libmikmod

* Fri Dec  7 2007 Jindrich Novy <jnovy@redhat.com> 3.2.2-6.beta1
- merge review fixes (#226142)

* Thu Oct 25 2007 Jindrich Novy <jnovy@redhat.com> 3.2.2-5
- remove useless configure option

* Wed Sep 19 2007 Jindrich Novy <jnovy@redhat.com> 3.2.2-4
- don't hardcode buildroot library paths to binaries/libs
- preserve timestamps
- link against libmikmod, remove mikmod-devel
- remove all libmikmod stuff, it's now packaged separately

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 3.2.2-3
- update License
- rebuild for BuildID

* Sat Apr 21 2007 Jindrich Novy <jnovy@redhat.com> 3.2.2-2
- downgrade libmikmod to avoid dependency problems before F7 release
- minor spec fixes

* Tue Apr 17 2007 Jindrich Novy <jnovy@redhat.com> 3.2.2-1
- update to mikmod-3.2.2-beta1
- drop useless libtool, texinfo BuildRequires
- don't use undefined macros, spec fixes
- fix install-info scriptlet usage (#223711), thanks to Ville Skytta

* Thu Nov  9 2006 Martin Stransky <stransky@redhat.com> - 3.1.6-39
- removed obsoletes on tracker (#214112)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.1.6-38.1
- rebuild

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 3.1.6-38
- put .so symlink in -devel subpackage

* Wed May 31 2006 Martin Stransky <stransky@redhat.com> 3.1.6-37
- fixed multilib issue (#192732), thx. to Radek Biba

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.1.6-36.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.1.6-36.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Martin Stransky <stransky@redhat.com> 3.1.6-36
- remove .la file (#172620)

* Mon Jun  6 2005 Martin Stransky <stransky@redhat.com> 3.1.6-35
- fixed #159290,#159291 - CAN-2003-0427
- fixed playing mod files from tar archive

* Wed Mar  2 2005 Bill Nottingham <notting@redhat.com> 3.1.6-34
- new compiler. old code.

* Tue Dec 21 2004 Martin Stransky <stransky@redhat.com> 3.1.6-33
- strip library (#143258)

* Mon Dec 13 2004 Bill Nottingham <notting@redhat.com> 3.1.6-31
- move mikmod binary back to main package (#142668)

* Fri Oct  8 2004 Bill Nottingham <notting@redhat.com> 3.1.6-30
- add texinfo buildreqs (#135088)

* Wed Oct  6 2004 Bill Nottingham <notting@redhat.com> 3.1.6-29
- install-info scripts go with -devel (#134882)

* Wed Sep 22 2004 Than Ngo <than@redhat.com> 3.1.6-28
- increase release number

* Wed Sep 22 2004 Than Ngo <than@redhat.com> 3.1.6-27
- new devel sub package, multiarch problem
- add /sbin/ldconfig in Prereq
- cleanup specfile

* Wed Aug  4 2004 Miloslav Trmac <mitr@redhat.com> - 3.1.6-26
- Update to libmikmod-3.1.11-a, fixes #116182

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jul 23 2003 Bill Nottingham <notting@redhat.com> 3.1.6-23
- remove URL (#77375)

* Mon Jul 14 2003 Bill Nottingham <notting@redhat.com> 3.1.6-22
- fix build with gcc-3.3 some more

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Bill Nottingham <notting@redhat.com> 3.1.6-21
- fix build with gcc-3.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Jeff Johnson <jbj@redhat.com> 3.1.6-19
- don't include -debuginfo files in package.

* Sat Nov 02 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add further lib64 support, clean up spec file

* Sat Oct 12 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add 64bit patch

* Thu Jul 18 2002 Bill Nottingham <notting@redhat.com>
- don't strip binaries
- fix buffering with esd output (#57154, <stssppnn@yahoo.com>)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jul 20 2001 Bill Nottingham <notting@redhat.com>
- add buildprereq for ncurses-devel (#49524)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Dec  7 2000 Bill Nottingham <notting@redhat.com>
- fix %%doc generation

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- FHS fixes, etc.

* Mon Apr  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with current ncurses
- library 3.1.9
- fix build when libmikmod is not already installed

* Thu Feb  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- gzip info page (Bug #9035)
- Update URL and Source fields to present location

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- get rid of useless defines

* Tue Jan 11 2000 Bill Nottingham <notting@redhat.com>
- update lib to 3.1.8

* Mon Aug  2 1999 Bill Nottingham <notting@redhat.com>
- add more patches

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 3.1.6/3.1.7

* Mon Mar 22 1999 Cristian Gafton <gafton@redhat.com>
- fixed spec file description and group according to sepcspo

* Mon Mar 22 1999 Michael Maher <mike@redhat.com>
- changed spec file, updated package
- added libmikmod to the package

* Mon Feb 15 1999 Miodrag Vallat <miodrag@multimania.com>
- Created for 3.1.5

* Sun Jan 24 1999 Michael Maher <mike@redhat.com>
- changed group
- fixed bug #145

* Fri Sep 04 1998 Michael Maher <mike@redhat.com>
- added patch for alpha

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- built package; obsoletes the ancient tracker program.

