%global gcc4prefix %{_prefix}/pcgcc4
%global gcc4execprefix %{gcc4prefix}
%global gcc4bindir %{gcc4prefix}/bin
%global gcc4sysconfdir %{gcc4prefix}/etc
%global gcc4includedir %{gcc4prefix}/include
%global gcc4libdir %{gcc4prefix}/%{_lib}
%global build_ldflags -Wl,-rpath -Wl,%{gcc4libdir} %{build_ldflags}

%global bsprefix /usr/didbs/0_1_5_n32_mips3_mp
%global bsbindir %{bsprefix}/bin
%global bslibdir %{bsprefix}/%{_lib}
%global bsgcc4prefix /usr/didbs/0_1_5_n32_mips3_mp/gbs4_2
%global bsgcc4bindir %{bsgcc4prefix}/bin
%global bsgcc4libdir %{bsgcc4prefix}/%{_lib}

Summary: Period correct gcc4 toolchain - gcc
Name: pc-gcc4-gcc
Version: 0.0.1
Release: 1wip%{?dist}
License: GPLv3+
URL: https://ftp.gnu.org/pub/gnu/gcc/
Source: https://ftp.gnu.org/pub/gnu/gcc/gcc-4.7.1/gcc-4.7.1.tar.gz

# Just some standard bits
BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

# The binutils specific for this gcc
#BuildRequires: pc-gcc4-binutils

Patch0: pc-gcc4.sgignuldfixes.patch

# Here's where you add parents you need in place
#Requires: parentproject

%description
A work in progress for a period correct gcc4 toolchain - this is the gcc part

%prep
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
# For now we'll use the irix toolchain + bootstrap fully
#export CPPFLAGS="-I%{_includedir}"
#export LDFLAGS="-L%{bslibdir} -L%{bsgcc4libdir} -L%{_libdir}"
#export PATH="%{bsgcc4bindir}:%{bsbindir}:%{gcc4bindir}:$PATH"
#export LD_LIBRARYN32_PATH="%{bsgcc4libdir}:%{bslibdir}:%{gcc4libdir}:$LD_LIBRARYN32_PATH"

export PATH="%{gcc4bindir}:$PATH"
export LD_LIBRARYN32_PATH="%{gcc4libdir}:$LD_LIBRARYN32_PATH"

export CPPFLAGS="-I%{_includedir}"
export LDFLAGS="-L%{_libdir}"

export CC=/usr/bin/c99
export CXX=/usr/bin/CC
export LD=%{gcc4bindir}/ld
export AS=%{gcc4bindir}/as
export NM=%{gcc4bindir}/nm

# You can omit the "-n example-wip-%{version}" here as it's the default
# this is just to show how you'd specific a particular extracted package dir
#%setup -q -n example-wip-%{version}
%setup -q -n gcc-4.7.1

%patch0 -p1 -b .sgignuldfixes

%build
mkdir build
cd build
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
# We can't use our newer makeinfo
export MAKEINFO=missing

# For now we'll use the irix toolchain + bootstrap fully
#export CPPFLAGS="-I%{_includedir}"
#export LDFLAGS="-L%{bslibdir} -L%{bsgcc4libdir} -L%{_libdir}"
#export PATH="%{bsgcc4bindir}:%{bsbindir}:%{gcc4bindir}:$PATH"
#export LD_LIBRARYN32_PATH="%{bsgcc4libdir}:%{bslibdir}:%{gcc4libdir}:$LD_LIBRARYN32_PATH"

export PATH="%{gcc4bindir}:$PATH"
export LD_LIBRARYN32_PATH="%{gcc4libdir}:$LD_LIBRARYN32_PATH"

export CPPFLAGS="-I%{_includedir}"
export LDFLAGS="-L%{_libdir}"

export CC=/usr/bin/c99
export CXX=/usr/bin/CC
export LD=%{gcc4bindir}/ld
export AS=%{gcc4bindir}/as
export NM=%{gcc4bindir}/nm

# Can't use regular %%configure as that passes the usual sgug prefix etc.
#../configure --prefix=%{gcc4prefix} \
#--exec-prefix=%{gcc4execprefix} --bindir=%{gcc4bindir} \
#--sysconfdir=%{gcc4sysconfdir} --includedir=%{gcc4includedir} \
#--libdir=%{gcc4libdir} --enable-werror=no --disable-nls --disable-multilib \
#--enable-obsolete --enable-languages=c,c++ --disable-bootstrap \
#--enable-shared --enable-static --enable-threads=posix --enable-tls=no \
#--disable-lto --with-system-zlib --enable-checking=release \
#--with-gmp=%{gcc4prefix} --with-mpfr=%{gcc4prefix}
../configure --prefix=%{gcc4prefix} \
--exec-prefix=%{gcc4execprefix} --bindir=%{gcc4bindir} \
--sysconfdir=%{gcc4sysconfdir} --includedir=%{gcc4includedir} \
--libdir=%{gcc4libdir} --enable-werror=no --disable-nls --disable-multilib \
--enable-obsolete --enable-languages=c,c++ --disable-bootstrap \
--enable-shared --enable-static --enable-threads=posix --enable-tls=no \
--disable-lto --with-system-zlib --enable-checking=release \
--with-gmp=%{gcc4prefix} --with-mpfr=%{gcc4prefix} \
--with-gnu-ld --with-ld=%{gcc4prefix}/bin/ld \
--with-gnu-as --with-as=%{gcc4prefix}/bin/as
make %{?_smp_mflags}

# For after this is self-hosting
#--with-gnu-ld --with-ld=%{gcc4bindir}/ld \
#--with-gnu-as --with-as=%{gcc4bindir}/as \
#

%check
# Do the tests by hand
#make check

%install
cd build
export PATH="%{bsgcc4bindir}:$PATH"
export LD_LIBRARYN32_PATH="%{bsgcc4libdir}:$LD_LIBRARYN32_PATH"
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{gcc4prefix} INSTALL='install -p'

# We're only interested in the binaries, libraries, includes
rm -rf $RPM_BUILD_ROOT/info
rm -rf $RPM_BUILD_ROOT/man

# Leave the libiberty.a from binutils
rm -f $RPM_BUILD_ROOT%{gcc4libdir}/libiberty.a

%files
%{gcc4prefix}/*

%changelog
* Thu Mar 5 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.1
- First build
