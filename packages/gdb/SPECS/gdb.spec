%global debug 0

%if 0%{debug}
%global __strip /bin/true
%else
# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}
%endif


Summary: The GNU Debugger
Name: gdb
Version: 7.6.2
Release: 7%{?dist}
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL
URL: http://ftp.gnu.org/gnu/gdb/
Source: http://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.gz

Patch0: gdb762.sgifixups.patch

BuildRequires: gcc, binutils
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: zlib-devel, readline-devel, ncurses-devel
BuildRequires: texinfo, gettext, flex, bison, expat-devel, xz-devel
BuildRequires: python3-devel

Requires: zlib, readline, ncurses

%description
The gnu debugger.

%prep
%setup

%patch0 -p1 -b .sgifixups

# A place to generate our patch
#exit 1

%build
# Be explicit about compilers
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
%if 0%{debug}
export CFLAGS="-g -Og"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%endif

%{configure} --enable-werror=no --disable-nls --disable-iconv \
    --disable-gprof --with-system-zlib --with-system-readline \
    --with-curses=ncurses                                     \
    --prefix=%{_prefix}					      \
    --libdir=%{_libdir}					      \
    --sysconfdir=%{_sysconfdir}				      \
    --mandir=%{_mandir}					      \
    --infodir=%{_infodir}                                     \
    --with-python

make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

rm -rf $RPM_BUILD_ROOT%{_libdir}/charset.alias
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{_includedir}/*.h
# Sorry not worked out how to install the docs yet
rm -rf $RPM_BUILD_ROOT%{_docdir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
rm $RPM_BUILD_ROOT%{_infodir}/annotate*
rm $RPM_BUILD_ROOT%{_infodir}/bfd*
rm $RPM_BUILD_ROOT%{_infodir}/configure*
rm $RPM_BUILD_ROOT%{_infodir}/stabs*
rm $RPM_BUILD_ROOT%{_infodir}/standards*

# We are not cross-target
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/syscalls/*

%files
%{_bindir}/*

%{_includedir}/gdb

%{_datadir}/gdb/python

%{_mandir}/*

%{_infodir}/gdb*.gz

%changelog
* Sat Oct 24 2020 Daniel Hams <daniel.hams@gmail.com> - 7.6.2-7
- Clean up of dynamically loaded library symbol support, fix issue on first load.

* Sun Oct 18 2020 Daniel Hams <daniel.hams@gmail.com> - 7.6.2-6
- Implement breakpoint trap on load of .so files (dlopened libraries) so gdb notices and loads their symbols

* Sat Oct 03 2020 Daniel Hams <daniel.hams@gmail.com> - 7.6.2-5
- Activate and fix the python bindings/extension

* Sat Sep 26 2020 Daniel Hams <daniel.hams@gmail.com> - 7.6.2-4
- Teach gdb about the extra IRIX signals and the pthread ones that can be
  safely ignored.

* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 7.6.2-3
- Avoid picking up python

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 7.6.2-2
- Remove hard coded shell paths

* Thu Jan 16 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
