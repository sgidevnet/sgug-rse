%global gcc4prefix %{_prefix}/pcgcc4
%global gcc4execprefix %{gcc4prefix}
%global gcc4bindir %{gcc4prefix}/bin
%global gcc4sysconfdir %{gcc4prefix}/etc
%global gcc4includedir %{gcc4prefix}/include
%global gcc4libdir %{gcc4prefix}/%{_lib}
%global build_ldflags -Wl,-rpath -Wl,%{gcc4libdir} %{build_ldflags}

Summary: Period correct gcc4 toolchain - binutils
Name: pc-gcc4-binutils
Version: 0.0.1
Release: 2wip%{?dist}
License: GPLv3+
URL: https://ftp.gnu.org/pub/gnu/binutils/
Source: https://ftp.gnu.org/pub/gnu/binutils/binutils-2.17a.tar.bz2

# Just some standard bits
BuildRequires: pc-gcc4-gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

# Here's where you add parents you need in place
#Requires: parentproject

%description
A work in progress for a period correct gcc4 toolchain - this is the binutils part

%prep
# You can omit the "-n example-wip-%{version}" here as it's the default
# this is just to show how you'd specific a particular extracted package dir
#%setup -q -n example-wip-%{version}
%setup -q -n binutils-2.17

%build

export PATH="%{gcc4bindir}:$PATH"
export LD_LIBRARYN32_PATH="%{gcc4libdir}:$LD_LIBRARYN32_PATH"

export CPPFLAGS="-I%{gcc4includedir} -I%{_includedir}"
export LDFLAGS="-L%{gcc4libdir} -L%{_libdir}"

export CC=%{gcc4bindir}/gcc
export CXX=%{gcc4bindir}/g++
export LD=%{gcc4bindir}/ld
export AS=%{gcc4bindir}/as
export NM=%{gcc4bindir}/nm

# Can't use regular %%configure as that passes the usual sgug prefix etc.
./configure --prefix=%{gcc4prefix} \
--exec-prefix=%{gcc4execprefix} --bindir=%{gcc4bindir} \
--sysconfdir=%{gcc4sysconfdir} --includedir=%{gcc4includedir} \
--libdir=%{gcc4libdir} --enable-werror=no --disable-nls --disable-iconv \
--disable-gprof --with-system-zlib
make %{?_smp_mflags}

%check
# Do the tests by hand
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{gcc4prefix} INSTALL='install -p'

# We're only interested in the binaries, libraries, includes
rm -rf $RPM_BUILD_ROOT/info
rm -rf $RPM_BUILD_ROOT/man

%files
%{gcc4prefix}/*

%changelog
* Thu Mar 5 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.1
- First build
