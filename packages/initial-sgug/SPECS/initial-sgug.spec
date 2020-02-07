Summary: Bootstrap vpkg for sgug
Name: initial-sgug
Epoch: 1
Version: 0.2.0
Release: 1%{?dist}
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

# X11 libraries that are used

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
