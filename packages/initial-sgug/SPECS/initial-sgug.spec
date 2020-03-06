Summary: Bootstrap vpkg for sgug
Name: initial-sgug
Epoch: 1
Version: 0.2.0
Release: 2%{?dist}
License: GPLv3+

Provides: /bin/sh
Provides: /bin/ksh
Provides: /bin/env
Provides: /usr/bin/env
Provides: /sbin/cpio
Provides: cpio
Provides: /usr/sgug/sbin/install-info

# Base platform shared libraries
Provides: libc.so.1
Provides: libm.so
Provides: libmx.so
Provides: libpthread.so
Provides: libdl.so
Provides: libgen.so
Provides: libnsl.so
Provides: libcrypt.so
Provides: librpcsvc.so
Provides: libgssapi_krb5.so.2
Provides: libsocket.so

# X11 libraries that are used
Provides: libX11.so.1
Provides: libXt.so
Provides: libXaw.so.2
Provides: libXext.so

# Motif
Provides: libXm.so.1
Provides: libXm.so.2
Provides: libXmu.so

# Audio
Provides: libaudio.so

# Hacks while working on getting everything rebuilt
#Provides: libgcc_s.so.1

%description
This is a virtual RPM package.  It contains no actual files.

%prep
# nothing to do
%build
# nothing to do
%install
# nothing to do
%clean
# nothing to do
%files
# no files in a virtual package
