Summary:	Enables programs to look inside archived/compressed files, access remote files
Name:		avfs
Version:	1.1.4
Release:	2
License:	GPLv2 and LGPLv2
Group:		Applications/Archiving
URL:		http://sourceforge.net/projects/avf
Source0:	http://ncu.dl.sourceforge.net/project/avf/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch100:	avfs.sgifixes.patch

%description
AVFS is a system which enables all programs to look inside archived
or compressed files, or access remote files without recompiling the
programs or changing the kernel.

At the moment it supports floppies, tar and gzip files, zip, bzip2, ar
and rar files, ftp sessions, http, webdav, rsh/rcp, ssh/scp. Quite a
few other handlers are implemented with the Midnight Commander's
external FS.

AVFS is (C) under the GNU GPL (see the file COPYING). The shared
library supporting AVFS with LD_PRELOAD is (C) under the GNU LGPL (see
the file COPYING.LIB).

AVFS comes with ABSOLUTELY NO WARRANTY, for details see the file COPYING. 

%package devel
Summary:   Development libraries and header files for %{name}
Group:     Development/Libraries
Requires:  %{name} = %{version}-%{release}

%description devel
Development libraries and header files for %{name}

%prep
%setup -q
%patch100 -p1


%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export CFLAGS="$CPPFLAGS"
export LDFLAGS="$RPM_LD_FLAGS -ldicl-0.1"
%ifarch aarch64
autoreconf -ifv
%endif
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf doc/Makefil*
sed -i 's| /bin/perl| /usr/bin/perl|' $RPM_BUILD_ROOT%{_libdir}/%{name}/extfs/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/*.so.*
%doc AUTHORS COPYING COPYING.LIB ChangeLog INSTALL NEWS README TODO doc/

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/avfs.pc

%changelog
* Fri Dec 24 2021 SGI User Group - 1.1.4-2
- Rebuilt for Irix
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.4
- Rebuilt for Fedora
* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.8-2
- Added libdir to configure for build under x86_64.
* Sat Nov 10 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9.8-1
- Initial build.
