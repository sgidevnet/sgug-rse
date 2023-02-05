Summary: Bootstrap vpkg for sgug
Name: initial-sgug
Epoch: 1
Version: 0.2.0
Release: 4%{?dist}
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
Provides: librt.so

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

# mipspro C++ library - some irix libs depend on this (notably libfam)
Provides: libC.so.2

# Hacks while working on getting everything rebuilt
#Provides: libgcc_s.so.1

%description
This is a virtual RPM package.  It contains no actual files.

%prep
# nothing to do
%build
# we need to touch the output directory otherwise some of the macros
# that check repository root etc will fail
mkdir -p $RPM_BUILD_ROOT

%install
# nothing to do
%clean
# nothing to do
%files
# no files in a virtual package

%changelog
* Mon Dec 14 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.0-4
- Include provides of IRIX mipspro C++ lib used by libfam

* Mon Jul 13 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.0-3
- Make sure we touch the output directory so that rpm macros don''t fail.

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.0-2
- Include gssapi_krb5, socket and rt system libs
