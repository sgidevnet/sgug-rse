Summary: The GNU Debugger
Name: gdb
Version: 7.6.2
Release: 1%{?dist}
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL
URL: http://ftp.gnu.org/gnu/gdb/
Source: http://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.gz

Patch0: gdb762.sgifixups.patch

BuildRequires: gcc, binutils
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: zlib-devel, readline-devel, ncurses-devel
BuildRequires: texinfo, gettext, flex, bison, expat-devel, xz-devel

Requires: zlib, readline, ncurses

%description
The gnu debugger.

%prep
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
%setup
%patch0 -p1 -b .sgifixups

%build
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
%{configure} --enable-werror=no --disable-nls --disable-iconv \
    --disable-gprof --with-system-zlib --with-system-readline \
    --with-curses=ncurses                                     \
    --prefix=%{_prefix}					      \
    --libdir=%{_libdir}					      \
    --sysconfdir=%{_sysconfdir}				      \
    --mandir=%{_mandir}					      \
    --infodir=%{_infodir}
    
make %{?_smp_mflags}

%check
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
make check

%install
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

rm -rf $RPM_BUILD_ROOT%{_libdir}/charset.alias
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{_includedir}/*.h
# Sorry not worked out how to install the docs yet
rm -rf $RPM_BUILD_ROOT%{_docdir}
rm $RPM_BUILD_ROOT%{_infodir}/annotate*
rm $RPM_BUILD_ROOT%{_infodir}/bfd*
rm $RPM_BUILD_ROOT%{_infodir}/configure*
rm $RPM_BUILD_ROOT%{_infodir}/stabs*
rm $RPM_BUILD_ROOT%{_infodir}/standards*

# And don't install the python bits
rm -rf $RPM_BUILD_ROOT%{_prefix}/share/gdb/python

# We are not cross-target
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/syscalls/*

%files
%{_bindir}/*

%{_includedir}/gdb

%{_mandir}/*

%{_infodir}/gdb*.gz

%changelog
* Thu Jan 16 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
