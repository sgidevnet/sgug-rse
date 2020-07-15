%global with_devel 0%{?rhel} && 0%{?rhel} <= 8

Summary: X.Org X11 libXxf86misc runtime library
Name: libXxf86misc
Version: 1.0.4
Release: 5%{?dist}
License: MIT
URL: http://www.x.org
Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
# copied out of xorgproto 2018.4
Source1: xf86misc.h
Source2: xf86mscstr.h

BuildRequires: sed
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xproto) pkgconfig(xext)

%if !%{with_devel}
Obsoletes: libXxf86misc-devel <= 1.0.4-4
%endif

%description
X.Org X11 libXxf86misc runtime library

%if %{with_devel}
%package devel
Summary: X.Org X11 libXxf86misc development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXxf86misc development package
%endif

%prep
%setup -q
sed -i s/xf86miscproto// configure.ac
mkdir -p src/X11/extensions/
cp %{SOURCE1} %{SOURCE2} src/X11/extensions/

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%if %{with_devel}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/X11/extensions
install -m 0644 -p %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/X11/extensions
%else
rm -f $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_mandir}/man3/*.3*
%endif

#%%ldconfig_post
#%%ldconfig_postun

%files
%doc README COPYING ChangeLog
%{_libdir}/libXxf86misc.so.1
%{_libdir}/libXxf86misc.so.1.1.0

%if %{with_devel}
%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXxf86misc.so
%{_libdir}/pkgconfig/xxf86misc.pc
%{_mandir}/man3/*.3*
%endif

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Adam Jackson <ajax@redhat.com> - 1.0.4-4
- Fix build with xorgproto >= 2019.1, which dropped the xf86misc headers
- Stop building the devel subpackage in Fedora and RHEL > 8, no new code
  should try to use this library, the X server hasn't implemented it in
  over 10 years

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 1.0.4-1
- libXxf86misc 1.0.4

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 1.0.3-16
- Use ldconfig scriptlet macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.3-6
- autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.3-1
- libXxf86misc 1.0.3
