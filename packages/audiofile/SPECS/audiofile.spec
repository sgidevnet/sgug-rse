Summary: A library for accessing various audio file formats
Name: audiofile
Version: 0.2.7
Release: 4%{?dist}
Epoch: 1
License: LGPLv2+
Group: System Environment/Libraries
Source: https://ftp.gnome.org/pub/gnome/sources/audiofile/0.2/audiofile-%{version}.tar.gz
URL: http://www.68k.org/~michael/audiofile/
#Patch2: audiofile-multilib.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
BuildRequires: libtool

%description
The Audio File library is an implementation of the Audio File Library
from SGI, which provides an API for accessing audio file formats like
AIFF/AIFF-C, WAVE, and NeXT/Sun .snd/.au files. This library is used
by the EsounD daemon.

Install audiofile if you are installing EsounD or you need an API for
any of the sound file formats it can handle.

%package devel
Summary: Development files for Audio File applications
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: pkgconfig >= 1:0.8

%description devel
The audiofile-devel package contains libraries, include files, and
other resources you can use to develop Audio File applications.

%prep
%setup -q
#%%patch2 -p1 -b .multilib

%build
%configure --disable-static
make %{?_smp_mflags} LIBTOOL="/usr/sgug/bin/libtool"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f docs/Makefile*

#%%post -p /sbin/ldconfig

#%%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING TODO README ChangeLog docs
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/audiofile-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/aclocal/*

%changelog
* Thu Jul 09 2020  HAL <notes2@gmx.de> - 1:0.2.7-4
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 22 2010 Bastien Nocera <bnocera@redhat.com> 0.2.7-1
- Update to 0.2.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.2.6-9
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.2.6-8
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 1:0.2.6-7
- Rebuild for build ID

* Sat Feb  3 2007 Matthias Clasen <mclasen@redhat.com> - 1:0.2.6-6
- Corrections from package review
 
* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 1:0.2.6-5
- Fix multilib conflicts
- Don't ship static libraries

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:0.2.6-4.1
- rebuild

* Mon Apr 17 2006 John (J5) Palmieri <johnp@redhat.com> - 1:0.2.6-4
- Remove Makefile* from docs so they are not installed

* Fri Mar 24 2006 Matthias Clasen <mclasen@redhat.com> - 1:0.2.6-3
- Reduce memory consumption by making data tables const

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:0.2.6-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:0.2.6-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> - 0.2.6-2.1
- rebuilt

* Thu Mar 17 2005 John (J5) Palmieri <johnp@redhat.com> - 0.2.6-2
- rebuild for gcc 4.0

* Fri Jul 30 2004 Colin Walters  <walters@redhat.com>
- Update to 0.2.6
- Rework description to not contain apostrophe that
  makes emacs unhappy

* Thu Jul 15 2004 Tim Waugh <twaugh@redhat.com>
- Fixed warnings in shipped m4 file.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Alexander Larsson <alexl@redhat.com> 1:0.2.5-1
- update to 0.2.5

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Jun  8 2003 Tim Powers <timp@redhat.com> 1:0.2.3-7.1
- rebuild for RHEL

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Mon Feb 10 2003 Bill Nottingham <notting@redhat.com>
- fix URL (#71010)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com>
- Remove unpackaged files

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jan  8 2002 Owen Taylor <otaylor@redhat.com>
- Update to 0.2.3, update URLs

* Mon Jun 25 2001 Preston Brown <pbrown@redhat.com>
- explicit requirement of -devel package on main package (#45205)

* Tue Apr 17 2001 Jonathan Blandford <jrb@redhat.com>
- Bumped version to 0.2.1

* Mon Dec 11 2000 Preston Brown <pbrown@redhat.com>
- upgrade to 0.1.11.

* Mon Aug 14 2000 Than Ngo <than@redhat.com>
- add ldconfig to %post and %postun (Bug #15413)

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- use FHS macros

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- strip library, use configure macro.

* Tue Sep 14 1999 Elliot Lee <sopwith@redhat.com>
- 0.1.8pre (take whatever is in CVS).

* Fri Aug 13 1999 Michael Fulbrght <drmike@redhat.com>
- version 1.7.0

* Sun Apr 18 1999 Matt Wilson <msw@redhat.com>
- updated patch from DaveM

* Fri Apr 16 1999 Matt Wilson <msw@redhat.com>
- added patch from Dave Miller to disable byte swapping in decoding

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries before packaging

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- Version 0.1.6

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- Removed libtoolize from %build

* Wed Feb 3 1999 Jonathan Blandfor <jrb@redhat.com>
- Newer version with bug fix.  Upped release.

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- integrating into rawhide release at GNOME freeze

* Fri Nov 20 1998 Michael Fulbright <drmike@redhat.com>
- First try at a spec file
