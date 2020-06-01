# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}


Summary: Dans Irix Compatibility Library
Name: libdicl
Version: 0.1.25
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

%build

%{configure}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
rm $RPM_BUILD_ROOT%{_libdir}/libdicl-0.1.la

%files
#%%{!?_licensedir:%%global license %%doc}
#%%license COPYING
#%%doc README ChangeLog NEWS
%{_libdir}/libdicl-0.1.so.*

%files devel
%{_libdir}/libdicl-0.1.a
%{_libdir}/libdicl-0.1.so
%{_libdir}/pkgconfig/libdicl-0.1.pc
%{_includedir}/libdicl-0.1


%changelog
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
