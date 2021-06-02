Name:       libeio
Version:    4.19
Release:    13%{?dist}
Summary:    Event-based fully asynchronous I/O library

License:    BSD or GPLv2+
URL:        http://software.schmorp.de/pkg/libeio.html
# cvs -rrel-%%(echo %%{version} | sed s/./_/) -z3 -d :pserver:anonymous@cvs.schmorp.de/schmorpforge co libeio-%%{version}
# tar czf libeio-%%{version}.tar.gz libeio-%%{version}
Source0:    libeio-%{version}.tar.gz
# libeio shared library conflicts with libeio from Enlightenment Eio package.
# There were several tries to fix this issue upstream or using FPC, but the
# only way how to fix the package is to rename the shared library in Fedora.
# Current name in Fedora is libev-eio.so.
# https://fedorahosted.org/fpc/ticket/403
Patch0:     libev-eio-rename.patch
BuildRequires:    autoconf automake libtool

%description
Libeio is a full-featured asynchronous I/O library for C, modeled in
similar style and spirit as libev. Features include: asynchronous read,
write, open, close, stat, unlink, fdatasync, mknod, readdir etc. (basically
the full POSIX API). sendfile (native on Solaris, Linux, HP-UX, FreeBSD,
emulated everywhere else), readahead (emulated where not available).

It is fully event-library agnostic and can easily be integrated into any
event-library (or used standalone, even in polling mode). It is very portable
and relies only on POSIX threads.


%package devel
Summary:        Development headers and libraries for libeio
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for libeio


%prep
%setup -q
%patch0 -p1 -b .rename


%build
[ -e configure ] || ./autogen.sh
%configure
make %{?_smp_mflags} CFLAGS="-D_GNU_SOURCE %{optflags}"


%install
make install DESTDIR=$RPM_BUILD_ROOT


%ldconfig_scriptlets


%files
%{_libdir}/libev-eio.so.*
%exclude %{_libdir}/libev-eio.a
%exclude %{_libdir}/libev-eio.la
%doc LICENSE Changes


%files devel
%{_includedir}/eio.h
%{_libdir}/libev-eio.so


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Jan Kaluza <jkaluza@redhat.com> - 4.19-2
- fix the License field and cleanup the spec file

* Tue May 13 2014 Jan Kaluza <jkaluza@redhat.com> - 4.19-1
- update to version 4.19
- rename libeio.so to libev-eio.so to fix conflict with "eio" package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 4.18-1
- update to version 4.18

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.65-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.65-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 3.65-3
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Lubomir Rintel <lkundrak@v3.sk> - 3.65-2
- Call ldconfig (Peter Lemenkov)
- Fix spelling errors
- Use correct compiler flags

* Fri Sep 17 2010 Lubomir Rintel <lkundrak@v3.sk> - 3.65-1
- Initial packaging
