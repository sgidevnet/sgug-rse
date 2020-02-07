Summary: Test vpkg with didbs tools
Name: initial-didbsng
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
Provides: /usr/didbsng/sbin/install-info

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
