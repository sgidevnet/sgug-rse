# This package is NOT able to use optimised linker flags.
#%%global build_ldflags %%{sgug_optimised_ldflags}

%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

Summary: Dans Irix Compatibility Library
Name: libdicl
Version: 0.1.36
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/danielhams/dicl
Source: https://github.com/danielhams/dicl/releases/download/%{version}/libdicl-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool

%description
libdicl is a library to provide / patch some of the missing / broken
posix functionality in IRIX libc.

%package devel
Summary: Header files and libraries for the libdicl library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
libdicl-devel contains the header files and libraries needed
to develop programs that use libdicl library.

%prep
%setup -q

# A place to generate a patch
#exit 1


%build

export CPPFLAGS="-D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="-g -Og"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%endif
%configure

make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
rm $RPM_BUILD_ROOT%{_libdir}/libdicl*.la

%files
#%%{!?_licensedir:%%global license %%doc}
#%%license COPYING
#%%doc README ChangeLog NEWS
%{_libdir}/libdicl*.so.*

%files devel
%{_libdir}/libdicl*.a
%{_libdir}/libdicl*.so
%{_libdir}/pkgconfig/libdicl*.pc
%{_includedir}/libdicl*


%changelog
* Fri Nov 27 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.36-1
- Upgrade to 0.1.36 with C++ stubs for strto* functions

* Wed Sep 23 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.35-1
- Upgrade to 0.1.25 with memrchr + fopendir implementations

* Sat Sep 05 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.33-1
- Bug to posix spawn to avoid attempting to sigaction for the IRIX internal signal 65.

* Sat Aug 22 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.32-1
- libdicl unhappy with optimised linker flags (test fails to build), switch to non-optimised linker flags

* Sun Aug 16 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.31-1
- Fix longstanding issue with rpl_select causing uknown fd_set compilation problems

* Sat Aug 15 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.30-1
- Bug fix and little optimisation to funopen bits.

* Sat Aug 15 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.29-1
- Add dprintf, vdprintf, funopen impl/lib for libsolv

* Thu Jun 18 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.28-1
- Add strptime and strftime, switch to lgpl2.1

* Sat Jun 06 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.27-1
- Add gnu format style attributes to reduce warnings

* Sun May 31 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.25-1
- Fix up test launching + correct glaring endian header mistake

* Thu May 21 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.24-1
- More posix spawnattr funcs + timegm

* Thu May 21 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.23-1
- Upgrade to libdicl exposing more posix spawn functionality

* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.22-1
- Upgrade to libdicl exposing strnlen, removing pselect proto

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.20-1
- Update to 0.1.20 with gnulib regexp

* Thu Feb 20 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.19-1
- Upgrade to 0.1.19 needed for pcre test passing / bug fixes.

* Fri Nov 29 2019 Daniel Hams <daniel.hams@gmail.com> - 0.1.15
- First build
