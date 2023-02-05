Name:           libitl
Version:        0.7.0 
Release:        18%{?dist}
Summary:        Libraries for The Islamic Tools and Libraries Project

License:        LGPLv2+
URL:            http://www.arabeyes.org/project.php?proj=ITL
Source0:        http://switch.dl.sourceforge.net/sourceforge/arabeyes/%{name}-%{version}.tar.gz

Patch0: %{name}-makefile-ld.patch
#BuildRequires:  autoconf

BuildRequires:  gcc
%description
The Islamic Tools and Libraries (ITL) is a project 
to provide a plethora of useful Islamic tools and 
applications as well as a comprehensive feature-full 
Islam-centric library. The ITL project currently 
includes Hijri date, Muslim prayer times, and Qibla. 

This package contains the libraries for applications using ITL

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make  %{?_smp_mflags} -j1


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ $RPM_BUILD_ROOT/%{_includedir}/itl
cp build/libitl.so.0.0.7 $RPM_BUILD_ROOT/%{_libdir}/
ln -s libitl.so.0.0.7 $RPM_BUILD_ROOT/%{_libdir}/libitl.so.0
ln -s libitl.so.0.0.7 $RPM_BUILD_ROOT/%{_libdir}/libitl.so
cp prayertime/src/prayer.h hijri/src/hijri.h $RPM_BUILD_ROOT/%{_includedir}/itl/
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc AUTHORS COPYING README
%{_libdir}/libitl.so.*

%files devel
%doc prayertime/doc/method-info.txt
%doc prayertime/README
%doc hijri/README
%{_libdir}/libitl.so
%{_includedir}/itl/


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 23 2009 Mohd Izhar Firdaus Ismail <mohd.izhar.firdaus@gmail.com> 0.7.0-2
- fix libitl.so.0 is not symlink warning
- made libitl to be built using only 1 make thread, as multiple threading randomly
  fail during compile

* Sat Sep 19 2009 Mohd Izhar Firdaus Ismail <mohd.izhar.firdaus@gmail.com> 0.7.0-1
- update to 0.7.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 09 2008 Mohd Izhar Firdaus Ismail <mohd.izhar.firdaus@gmail.com> 0.6.4-5
- fix for FTBFS bug #449622

* Mon Mar 03 2008 Mohd Izhar Firdaus Ismail <mohd.izhar.firdaus@gmail.com> 0.6.4-4
- remove --build-id from makefile

* Fri Feb 15 2008 Mohd Izhar Firdaus Ismail <mohd.izhar.firdaus@gmail.com> 0.6.4-3
- include the configure script as a source instead of as a patch

* Sun Feb 03 2008 Mohd Izhar Firdaus Ismail <mohd.izhar.firdaus@gmail.com> 0.6.4-2
- modified makefile to install .so files to standard path
- moved unversioned .so to devel package
- added requires to ldconfig
- changed license to LGPLv2+
- upstream tarball doesn't include a configure script.
  ran autogen.sh with autoconf-2.61 and created a patch to 
  include a configure script instead of running autogen.sh
  on every compile. autoconf-2.61 works with this tarball but we
  don't know about the other autoconf versions.

* Thu Oct 18 2007 Mohd Izhar Firdaus Ismail <mohd.izhar.firdaus@gmail.com> 0.6.4-1
- Initial package
