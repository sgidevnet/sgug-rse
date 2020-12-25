%global debug 0

%if 0%{debug}
%global __strip /bin/true
%else
# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}
%endif

Summary: A collection of programs for manipulating patch files
Name: patchutils
Version: 0.3.4
Release: 15%{?dist}
License: GPLv2+
URL: http://cyberelk.net/tim/patchutils/
Source0: http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.xz
Patch1: patchutils-bz1226985.patch
Patch2: patchutils-format-str.patch
Obsoletes: interdiff <= 0.0.10
Provides: interdiff = 0.0.11
Requires: patch
BuildRequires:  gcc
BuildRequires: perl-generators
BuildRequires: xmlto
BuildRequires: automake, autoconf
BuildRequires: libdicl-devel

%description
This is a collection of programs that can manipulate patch files in
a variety of ways, such as interpolating between two pre-patches, 
combining two incremental patches, fixing line numbers in hand-edited 
patches, and simply listing the files modified by a patch.

%prep
%setup -q

# Fixed handling of delete-file diffs from git (bug #1226985).
%patch1 -p1 -b .bz1226985

# Don't use regerror() result as format string.
%patch2 -p1 -b .format-str

autoreconf

# Rewrite some hardcoded paths prevent tests executing
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" test-driver
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" scripts/dehtmldiff.in
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" scripts/dehtmldiff
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/*/run-test
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" scripts/move-to-front
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" scripts/espdiff.in
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" scripts/editdiff.in
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" tests/combine2/run-test
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" tests/combine3/run-test

# Replace use of /bin/echo
perl -pi -e "s|/bin/echo|%{_bindir}/echo|g" tests/*/run-test

%build
touch doc/patchutils.xml

# Use libdicl so we have access to getopt_long
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -O0"
export LDFLAGS="-ldicl-0.1"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif
# autoconf won't detect our replacement functions in libdicl without hints...
export ac_cv_func_getopt_long=yes
export ac_cv_func_getline=yes

%configure
# Dont use parallel make, this package is a bit broken
#make %%{?_smp_mflags}
make

%check
make check

%install
make DESTDIR=%{buildroot} install

%files
%{!?_licensedir:%global license %doc}
%doc AUTHORS ChangeLog README BUGS NEWS
%license COPYING
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Tue Oct 06 2020 Daniel Hams <daniel.hams@gmail.com> - 0.3.4-15
- Get all tests passing (broken paths + bad internal getline implementation)

* Mon Sep 28 2020  HAL <notes2@gmx.de> - 0.3.4-14
- initial commit, many tests fail (-build with --nocheck)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Tim Waugh <twaugh@redhat.com> - 0.3.4-12
- Requires patch (bug #1609946).
