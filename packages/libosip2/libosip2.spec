Name:           libosip2
Version:        3.6.0
Release:        17%{?dist}

Summary:        oSIP is an implementation of SIP

License:        LGPLv2+
URL:            http://www.gnu.org/software/osip/
Source0:        http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
Patch0:         libosip2-aarch64.patch

BuildRequires:  gcc
%description
oSIP is an implementation of SIP.

SIP stands for the Session Initiation Protocol and is described by the rfc3261
(wich deprecates rfc2543). This library aims to provide multimedia and telecom
software developers an easy and powerful interface to initiate and control SIP
based sessions in their applications. SIP is a open standard replacement from
IETF for H.323.

%package        devel
Summary:        Development libraries for oSIP
Requires:       %{name} = %{version}-%{release}

%description    devel
The GNU oSIP library is written in C and get no dependencies except the
standard C library. oSIP is thread safe and will generally be used in a
multi-threaded application. Nevertheless, this is optional.

oSIP is little in size and code and thus could be use to implement IP
soft-phone as well as embedded SIP software. oSIP is not limited to endpoint
agents, and can also be used to implement "SIP proxy".

oSIP does not intend to provide a high layer API for controlling "SIP Session"
at this step. Instead, it currently provides an API for the SIP message parser,
SDP message parser, and library to handle "SIP transactions" as defined by the
SIP document.

%prep
%setup -q
%patch0 -p1 -b .aarch64

%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
mv %{buildroot}%{_mandir}/man1/osip.1 %{buildroot}%{_mandir}/man1/osip2.1


%ldconfig_scriptlets

%files
%doc AUTHORS BUGS COPYING ChangeLog FEATURES HISTORY NEWS README TODO
%{_libdir}/libosip2.so.7*
%{_libdir}/libosipparser2.so.7*

%files devel
%{_includedir}/osip2
%{_includedir}/osipparser2
%{_libdir}/libosip2.so
%{_libdir}/libosipparser2.so
%{_libdir}/pkgconfig/libosip2.pc
%{_mandir}/man1/osip2.1*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-5
- add aarch64 patch (#925852)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-1
- libosip2-3.6.0

* Fri Sep  2 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.0-1
- libosip2-3.5.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.1.0-1
- Update to 3.1.0.

* Fri Jan 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-3
- Update to new patchlevel release.

* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-2
- Bump release.

* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-1
- Update to 3.0.3
- Update license tag.

* Wed Nov 22 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.1-2
- Bump release and rebuild

* Sat Nov 11 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.1-1
- Update to 3.0.1 and remove unnecessary patch.

* Wed Aug 30 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.2-4
- Bump release and rebuild.

* Thu Feb 23 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.2.2-3
- Fix for AMD64

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.2.2-2
- Rebuild for Fedora Extras 5

* Thu Dec 22 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.2.2-1
- Upstream update

* Sat Oct 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.2.1-1
- Upstream update
- Disable static library

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Mar 24 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.2.0-2
- Renamed osip.1 and moved to -devel

* Thu Mar 24 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.2.0-1
- Initial RPM release.
