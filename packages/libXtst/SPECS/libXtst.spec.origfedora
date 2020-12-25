%global tarball libXtst
#global gitdate 20130524
%global gitversion e7e04b7be

Summary: X.Org X11 libXtst runtime library
Name: libXtst
Version: 1.2.3
Release: 10%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel >= 1.5.99.902
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: xmlto

%description
X.Org X11 libXtst runtime library

%package devel
Summary: X.Org X11 libXtst development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libXi-devel%{?_isa}

%description devel
X.Org X11 libXtst development package

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING
%{_libdir}/libXtst.so.6
%{_libdir}/libXtst.so.6.1.0

%files devel
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/record.h
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_mandir}/man3/XTest*.3*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 1.2.3-7
- Drop useless %%defattr

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 1.2.3-6
- Use ldconfig scriptlet macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.2.3-1%{?gitdate:.git}%{?dist}
- libXtst 1.2.3
- fixes CVE-2016-7951, CVE-2016-7952

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.2.2-1
- libXtst 1.2.2
