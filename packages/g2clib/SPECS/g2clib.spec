%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           g2clib
Version:        1.6.0
Release:        7%{?dist}
Summary:        GRIB2 encoder/decoder and search/indexing routines in C

License:        Public Domain
URL:            http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/
Source0:        http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/g2clib-%{version}.tar
Source1:        g2clib-msg.txt
#Patch to fix up type detection and printf arguments on 64-bit machines
Patch0:         g2clib-64bit.patch
# Patch to remove multiple definitions of templates
Patch1:         g2clib-templates.patch
# Patch from Wesley Ebisuzaki <wesley.ebisuzaki@noaa.gov> to fix sigfault
# if simunpack() is called with 0 values to unpack
Patch2:         g2clib-simunpack.patch
# Patch from degrib - appears to fix projection issues
Patch3:         g2clib-degrib.patch
# Fix build with Jasper 2
Patch4:         g2clib-jasper2.patch

BuildRequires:  gcc
BuildRequires:  libpng-devel jasper-devel
# static only library - no debuginfo
%global debug_package %{nil}

%if %{lua: print(rpm.vercmp(rpm.expand("%version"),"1.6.0"))} >= 0
%global g2clib g2c_v%{version}
%else
%global g2clib grib2c
%endif

%description
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in ASCII file "grib2c.doc".


%package        devel
Summary:        Development files for %{name}
#Requires:       %%{name} = %%{version}-%%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       libpng-devel jasper-devel

%description    devel
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in file "grib2c.doc".

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .64bit
%patch1 -p1 -b .templates
%patch2 -p1 -b .simunpack
%patch3 -p1 -b .degrib
%patch4 -p1 -b .jasper2
chmod a-x *.h *.c README CHANGES grib2c.doc makefile
cp -p %{SOURCE1} .


%build
CFLAGS="$RPM_OPT_FLAGS -DUSE_PNG -DUSE_JPEG2000"

%ifarch sparc64 s390x %{mips64}
CFLAGS="$CFLAGS -D__64BIT__ -fPIC"
%endif
%ifarch x86_64 ia64 %{power64} aarch64
CFLAGS="$CFLAGS -D__64BIT__ -fpic"
%endif
%ifarch %{ix86} %{arm} %{mips32}
CFLAGS="$CFLAGS -fpic"
%endif

make CFLAGS="$CFLAGS" CC="%{__cc}" ARFLAGS=


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 lib%{g2clib}.a $RPM_BUILD_ROOT%{_libdir}
install -p -m0644 grib2.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 drstemplates.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 gridtemplates.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 pdstemplates.h $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{macrosdir}
echo %%g2clib %g2clib > $RPM_BUILD_ROOT%{macrosdir}/macros.g2clib


%files devel
%doc README CHANGES grib2c.doc g2clib-msg.txt
#%%{_libdir}/libgrib2c.a
%{_libdir}/lib%{g2clib}.a
%{_includedir}/grib2.h
%{_includedir}/drstemplates.h
%{_includedir}/gridtemplates.h
%{_includedir}/pdstemplates.h
%{macrosdir}/macros.g2clib


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Jos de Kloe <josdekloe@gmail.com> 1.6.0-4
- Add explicit BuildRequires for gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Orion Poplawski <orion@nwra.com> - 1.6.0-2
- Define %%g2clib for dependent packages to use

* Sun Aug 13 2017 Jos de Kloe <josdekloe@gmail.com> 1.6.0-1
- Update to new upstream version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 5 2016 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-13
- Add patch to fix build with jasper 2

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 1.4.0-12
- Add support for MIPS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-9
- Fix 64bit detection to be automatic (bug #1203582)
- Add patch from degrib that appears to fix some projection issues

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.0-7
- Build aarch64/ppc64le with -fpic

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-3
- Add patch to fix possible segfault after calling simunpack with 0 values to
  unpack

* Tue Dec 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.0-2
- Build with -fpic on 32 bit too. Use -fpic on supported platforms over -fPIC

* Tue Oct 16 2012 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-1
- Update to 1.4.0
- Rebase templates patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 9 2012 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-4
- Add patch to avoid multiple definitions of templates

* Fri Mar 9 2012 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-3
- Install drstemplates.h, gridtemplates.h, and pdstemplates.h

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1
- Update to 1.2.3

* Mon Oct 10 2011 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-2
- Add -fPIC to 64-bit builds

* Wed Mar 16 2011 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-1
- Update to 1.2.2

* Thu Feb 17 2011 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-3
- Define __64BIT__ when compiling on 64 bit machines (bug #678202)
- Add patch to deal with different format specifiers on 64 bit machines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 2 2010 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-1
- Update to 1.2.1

* Fri Apr 16 2010 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-1
- Update to 1.2.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Orion Poplawski <orion@cora.nwra.com> - 1.1.9-1
- Update to 1.1.9

* Fri Apr 17 2009 Orion Poplawski <orion@cora.nwra.com> - 1.1.8-1
- Update to 1.1.8

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Orion Poplawski <orion@cora.nwra.com> - 1.1.7-1
- Update to 1.1.7
- Add quotes around %%{__cc} as it can be multi-word

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.5-4
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Orion Poplawski <orion@cora.nwra.com> 1.0.5-3
- Remove %%{?_smp_mflags}, makefile is not parallel make safe

* Fri Dec 14 2007 Patrice Dumas <pertusus@free.fr> 1.0.5-2
- Add the mail message precising the license

* Thu Dec 13 2007 Orion Poplawski <orion@cora.nwra.com> 1.0.5-1
- Update to 1.0.5

* Fri Aug 24 2007 Patrice Dumas <pertusus@free.fr> 1.0.4-1
- initial packaging
