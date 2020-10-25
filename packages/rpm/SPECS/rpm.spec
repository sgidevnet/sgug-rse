%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

# build against xz?
%bcond_without xz
# just for giggles, option to build with internal Berkeley DB
%bcond_with int_bdb
# run internal testsuite?
%bcond_with check
# build with plugins?
%bcond_without plugins
# build with libarchive? (needed for rpm2archive)
%bcond_without libarchive
# build with libimaevm.so
%bcond_with libimaevm
# build with new db format
%bcond_with ndb
# build with zstd support?
%bcond_with zstd
# build with lmdb support?
%bcond_with lmdb

%define rpmhome %{_prefix}/lib/rpm

%global rpmver 4.15.0
#global snapver rc1
%global rel 18

%global srcver %{version}%{?snapver:-%{snapver}}
%global srcdir %{?snapver:testing}%{!?snapver:%{name}-%(echo %{version} | cut -d'.' -f1-2).x}

%define bdbver 5.3.15

# Build-dependency on systemd for the sake of one macro would be a bit much...
%{!?_tmpfilesdir:%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d}

Summary: The RPM package management system
Name: rpm
Version: %{rpmver}
Release: %{?snapver:0.%{snapver}.}%{rel}%{?dist}
Url: http://www.rpm.org/
Source0: http://ftp.rpm.org/releases/%{srcdir}/%{name}-%{srcver}.tar.bz2
%if %{with int_bdb}
Source1: db-%{bdbver}.tar.gz
%endif

# Disable autoconf config.site processing (#962837)
Patch1: rpm-4.15.x-siteconfig.patch
# In current Fedora, man-pages pkg owns all the localized man directories
Patch3: rpm-4.9.90-no-man-dirs.patch
# Temporary band-aid for rpm2cpio whining on payload size mismatch (#1142949)
Patch5: rpm-4.12.0-rpm2cpio-hack.patch
# https://github.com/rpm-software-management/rpm/pull/473
Patch6: 0001-find-debuginfo.sh-decompress-DWARF-compressed-ELF-se.patch
# systemd-inhibit plugin: don't call dbus_shutdown, it causes problems
# https://bugzilla.redhat.com/show_bug.cgi?id=1750575
Patch7: 0001-Revert-Fully-shutdown-DBUS-on-systemd_inhibit-cleanu.patch

# Patches already upstream:

# These are not yet upstream
Patch906: rpm-4.7.1-geode-i686.patch
# Probably to be upstreamed in slightly different form
Patch907: rpm-4.15.x-ldflags.patch

Patch910: 0001-Remove-problematic-sub-variants-of-armv8-and-related.patch
Patch911: revert-arm64.patch
Patch912: 0001-Revert-Improve-ARM-detection.patch

Patch2000: rpm.sgifixes.patch

BuildRequires: libdicl-devel >= 0.1.28
BuildRequires: python3-rpm-macros >= 3-52
Requires: libdicl >= 0.1.28
# Need to "find" cmake and set the right (__cmake) macro variable
BuildRequires: cmake >= 3.17.2-1

# Ensure we have the sgug macros, too
Requires: sgug-rpm-config

# Partially GPL/LGPL dual-licensed and some bits with BSD
# SourceLicense: (GPLv2+ and LGPLv2+ with exceptions) and BSD
License: GPLv2+

Requires: coreutils
%if %{without int_bdb}
# db recovery tools, rpmdb_util symlinks
Requires: %{_bindir}/db_stat
Requires: libdb
%endif
Requires: popt%{_isa} >= 1.10.2.1
Requires: curl

%if %{without int_bdb}
BuildRequires: libdb-devel
%endif

%if %{with check}
BuildRequires: fakechroot gnupg2
%endif

# XXX generally assumed to be installed but make it explicit as rpm
# is a bit special...
#BuildRequires: redhat-rpm-config >= 94
BuildRequires: gcc make
BuildRequires: gawk
BuildRequires: elfutils-devel >= 0.112
BuildRequires: elfutils-libelf-devel
BuildRequires: readline-devel zlib-devel
BuildRequires: openssl-devel
# The popt version here just documents an older known-good version
BuildRequires: popt-devel >= 1.10.2
BuildRequires: file-devel
BuildRequires: gettext-devel
BuildRequires: ncurses-devel
BuildRequires: bzip2-devel >= 0.9.0c-2
BuildRequires: lua-devel >= 5.1
#BuildRequires: libcap-devel
#BuildRequires: libacl-devel
%if %{with xz}
BuildRequires: xz-devel >= 4.999.8
%endif
%if %{with libarchive}
BuildRequires: libarchive-devel
%endif
%if %{with zstd}
BuildRequires: libzstd-devel
%endif
%if %{with lmdb}
BuildRequires: lmdb-devel
%endif
# Couple of patches change makefiles so, require for now...
BuildRequires: automake libtool

#%%if %%{with plugins}
#BuildRequires: libselinux-devel
#BuildRequires: dbus-devel
#BuildRequires: audit-libs-devel
#%%endif

%if %{with libimaevm}
BuildRequires: ima-evm-utils-devel >= 1.0
%endif

Requires: rpm-libs = %{version}-%{release}
Requires: libdb, zlib, lua, popt, openssl-libs, xz-libs, gettext-libs

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package libs
Summary:  Libraries for manipulating RPM packages
License: GPLv2+ and LGPLv2+ with exceptions
Requires: %{name} = %{version}-%{release}

%description libs
This package contains the RPM shared libraries.

%package build-libs
Summary:  Libraries for building RPM packages
License: GPLv2+ and LGPLv2+ with exceptions
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description build-libs
This package contains the RPM shared libraries for building packages.

%package sign-libs
Summary:  Libraries for signing RPM packages
License: GPLv2+ and LGPLv2+ with exceptions
Requires: rpm-libs%{_isa} = %{version}-%{release}
Requires: %{_bindir}/gpg2

%description sign-libs
This package contains the RPM shared libraries for signing packages.

%package devel
Summary:  Development files for manipulating RPM packages
License: GPLv2+ and LGPLv2+ with exceptions
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs%{_isa} = %{version}-%{release}
Requires: %{name}-build-libs%{_isa} = %{version}-%{release}
Requires: %{name}-sign-libs%{_isa} = %{version}-%{release}
Requires: popt-devel%{_isa}
Requires: libdicl-devel >= 0.1.16

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%package build
Summary: Scripts and executable programs used to build packages
Requires: rpm = %{version}-%{release}
Requires: elfutils >= 0.128 binutils
Requires: findutils sed grep gawk diffutils file patch >= 2.5
Requires: tar unzip gzip bzip2 cpio xz
Requires: rpm-build-libs = %{version}-%{release}
%if %{with zstd}
Requires: zstd
%endif
Requires: pkgconfig >= 1:0.24
#Requires: /usr/bin/gdb-add-index
# https://fedoraproject.org/wiki/Changes/Minimal_GDB_in_buildroot
Suggests: gdb-minimal
# Technically rpmbuild doesn't require any external configuration, but
# creating distro-compatible packages does. To make the common case
# "just work" while allowing for alternatives, depend on a virtual
# provide, typically coming from redhat-rpm-config.
#Requires: system-rpm-config
Requires: perl-macros

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

%package sign
Summary: Package signing support
Requires: rpm-sign-libs%{_isa} = %{version}-%{release}

%description sign
This package contains support for digitally signing RPM packages.

%package -n python2-%{name}
Summary: Python 2 bindings for apps which will manipulate RPM packages
BuildRequires: python2-devel
%{?python_provide:%python_provide python2-%{name}}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}-python = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}

%description -n python2-%{name}
The python2-rpm package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python 2
programs that will manipulate RPM packages and databases.

%package -n python3-%{name}
Summary: Python 3 bindings for apps which will manipulate RPM packages
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{name}}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}-python3 = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
Obsoletes: platform-python-%{name} < %{version}-%{release}

%description -n python3-%{name}
The python3-rpm package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python 3
programs that will manipulate RPM packages and databases.

%package apidocs
Summary: API documentation for RPM libraries
BuildArch: noarch

%description apidocs
This package contains API documentation for developing applications
that will manipulate RPM packages and databases.

#%%package cron
#Summary: Create daily logs of installed packages.
#BuildArch: noarch
#Requires: crontabs logrotate rpm = %%{version}-%%{release}

#%%description cron
#This package contains a cron job which creates daily logs of installed
#packages on a system.

%if %{with plugins}
%package plugin-selinux
Summary: Rpm plugin for SELinux functionality
Requires: rpm-libs%{_isa} = %{version}-%{release}
Requires: selinux-policy-base

%description plugin-selinux
%{summary}.

%package plugin-syslog
Summary: Rpm plugin for syslog functionality
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-syslog
%{summary}.

%package plugin-systemd-inhibit
Summary: Rpm plugin for systemd inhibit functionality
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-systemd-inhibit
This plugin blocks systemd from entering idle, sleep or shutdown while an rpm
transaction is running using the systemd-inhibit mechanism.

%package plugin-ima
Summary: Rpm plugin ima file signatures
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-ima
%{summary}.

%package plugin-prioreset
Summary: Rpm plugin for resetting scriptlet priorities for SysV init
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-prioreset
%{summary}.

Useful on legacy SysV init systems if you run rpm transactions with
nice/ionice priorities. Should not be used on systemd systems.

%package plugin-audit
Summary: Rpm plugin for logging audit events on package operations
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-audit
%{summary}.

# with plugins
%endif

%prep
%autosetup -n %{name}-%{srcver} %{?with_int_bdb:-a 1} -p1

# For patch generation
#exit 1

# Rewrite hardcoded paths to /bin/sh that cause us problems on irix
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" lib/rpmscript.c
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" cliutils.c
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" build/parseScript.c
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" macros.in

# Rewrite /usr/bin/sh paths
perl -pi -e "s|/usr/bin/sh|%{_prefix}/bin/sh|g" config.guess
perl -pi -e "s|/usr/bin/sh|%{_prefix}/bin/sh|g" config.sub
perl -pi -e "s|/usr/bin/sh|%{_prefix}/bin/sh|g" mkinstalldirs

# Rewrite pkgconfigdeps
perl -pi -e "s|/bin/bash|%{_prefix}/bin/bash|g" scripts/pkgconfigdeps.sh
perl -pi -e "s|/usr/bin/pkg-config|%{_prefix}/bin/pkg-config|g" scripts/pkgconfigdeps.sh

# Rewrite some /usr/bin/env bash usages that aren''t fixed by macros (yet)
perl -pi -e "s|/usr/bin/env bash|%{_prefix}/bin/bash|g" scripts/check-prereqs
perl -pi -e "s|/usr/bin/env bash|%{_prefix}/bin/bash|g" scripts/check-rpaths-worker
perl -pi -e "s|/usr/bin/env bash|%{_prefix}/bin/bash|g" scripts/find-lang.sh
perl -pi -e "s|/usr/bin/env bash|%{_prefix}/bin/bash|g" scripts/fontconfig.prov
perl -pi -e "s|/usr/bin/env bash|%{_prefix}/bin/bash|g" scripts/rpmdb_loadcvt
perl -pi -e "s|/usr/bin/env bash|%{_prefix}/bin/bash|g" scripts/find-debuginfo.sh

# Rewrite fontconfig provides
perl -pi -e "s|/usr/bin/fc-query|%{_bindir}/fc-query|g" scripts/fontconfig.prov
perl -pi -e "s|/usr/share/fonts|%{_datadir}/fonts|g" scripts/fontconfig.prov
perl -pi -e "s|--format|-f|g" scripts/fontconfig.prov

%if %{with int_bdb}
ln -s db-%{bdbver} db
%endif

%build
%set_build_flags
export CPPFLAGS="-D_SGI_SOURCES -D_SGI_REENTRANT_FUNCTIONS -I%{_includedir}/libdicl-0.1"
export LIBS="-lgen -ldicl-0.1 -llzma -lintl"
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%endif

autoreconf -i -f

# Hardening hack taken from macro %%configure defined in redhat-rpm-config
for i in $(find . -name ltmain.sh) ; do
     %{__sed} -i.backup -e 's~compiler_flags=$~compiler_flags="%{_hardened_ldflags}"~' $i
done;

export RPM_HOST_TRIPLET="mips-sgi-irix6.5"

# Using configure macro has some unwanted side-effects on rpm platform
# setup, use the old-fashioned way for now only defining minimal paths.
ac_cv_func_getline=yes ./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_localstatedir}/lib \
    --libdir=%{_libdir} \
    --build=$RPM_HOST_TRIPLET \
    --host=$RPM_HOST_TRIPLET \
    --with-vendor=sgug \
    %{!?with_int_bdb: --with-external-db} \
    %{!?with_plugins: --disable-plugins} \
    --with-lua \
    --enable-python \
    %{?with_ndb: --with-ndb} \
    %{?with_libimaevm: --with-imaevm} \
    %{?with_zstd: --enable-zstd} \
    %{?with_lmdb: --enable-lmdb} \
    --with-crypto=openssl \
    --disable-openmp

#    --with-cap \ #
#    --with-acl \ #
#    --with-selinux \ #

%make_build

cd python
%py2_build
%py3_build
cd ..

%install
%make_install

# We need to build with --enable-python for the self-test suite, but we
# actually package the bindings built with setup.py (#531543#c26)
cd python
%py2_install
%py3_install
cd ..


# Save list of packages through cron
#mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily
#install -m 755 scripts/rpm.daily ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/rpm

#mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
#install -m 644 scripts/rpm.log ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/rpm

mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
echo "r %{_localstatedir}/lib/rpm/__db.*" > ${RPM_BUILD_ROOT}%{_tmpfilesdir}/rpm.conf

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
mkdir -p $RPM_BUILD_ROOT%{rpmhome}/macros.d

# init an empty database for %ghost'ing
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/rpm
## Hack - for bootstrapping we must use rpm from the path
rpmdb --rcfile=$RPM_BUILD_ROOT%{_prefix}/lib/rpm/rpmrc --dbpath=$RPM_BUILD_ROOT%{_localstatedir}/lib/rpm --initdb

# plant links to relevant db utils as rpmdb_foo for documention compatibility
%if %{without int_bdb}
for dbutil in dump load recover stat upgrade verify
do
    ln -s ../../bin/db_${dbutil} $RPM_BUILD_ROOT/%{rpmhome}/rpmdb_${dbutil}
done
%endif

# Remove unused systemd thing
rm $RPM_BUILD_ROOT%{_prefix}/share/man/man8/rpm-plugin-systemd*

# Move man pages into appropriate place
#mkdir -p $RPM_BUILD_ROOT%{_mandir}
#mv $RPM_BUILD_ROOT%{_prefix}/share/man/* $RPM_BUILD_ROOT%{_mandir}/
#rmdir $RPM_BUILD_ROOT%{_prefix}/share/man

%find_lang %{name}

find $RPM_BUILD_ROOT -name "*.la"|xargs rm -f

# These live in perl-generators and python-rpm-generators now
rm -f $RPM_BUILD_ROOT/%{rpmhome}/{perldeps.pl,perl.*,pythond*}
rm -f $RPM_BUILD_ROOT/%{_fileattrsdir}/{perl*,python*}

echo "Looking for lock files at: %{_localstatedir}/lib/rpm/.*.lock"

# Set our optimisation level to O3
perl -pi -e "s|mips -O2|mips -O3|g" $RPM_BUILD_ROOT%{rpmhome}/rpmrc

%if %{with check}
%check
# https://github.com/rpm-software-management/rpm/issues/741
make check || (cat tests/rpmtests.log; exit 0)
%endif

%files -f %{name}.lang
%license COPYING
%doc CREDITS doc/manual/[a-z]*

%{_tmpfilesdir}/rpm.conf
%dir %{_sysconfdir}/rpm

%attr(0755, root, root) %dir %{_localstatedir}/lib/rpm
%attr(0644, root, root) %ghost %config(missingok,noreplace) %{_localstatedir}/lib/rpm/*
%attr(0644, root, root) %ghost %{_localstatedir}/lib/rpm/.*.lock

%{_bindir}/rpm
%{_bindir}/rpm2archive
%{_bindir}/rpm2cpio
%{_bindir}/rpmdb
%{_bindir}/rpmkeys
%{_bindir}/rpmquery
%{_bindir}/rpmverify

%{_mandir}/man8/rpm.8*
%{_mandir}/man8/rpmdb.8*
%{_mandir}/man8/rpmkeys.8*
%{_mandir}/man8/rpm2cpio.8*
%{_mandir}/man8/rpm-misc.8*

# XXX this places translated manuals to wrong package wrt eg rpmbuild
%lang(fr) %{_mandir}/fr/man[18]/*.[18]*
%lang(ko) %{_mandir}/ko/man[18]/*.[18]*
%lang(ja) %{_mandir}/ja/man[18]/*.[18]*
%lang(pl) %{_mandir}/pl/man[18]/*.[18]*
%lang(ru) %{_mandir}/ru/man[18]/*.[18]*
%lang(sk) %{_mandir}/sk/man[18]/*.[18]*

%attr(0755, root, root) %dir %{rpmhome}
%{rpmhome}/macros
%{rpmhome}/macros.d
%{rpmhome}/lua
%{rpmhome}/rpmpopt*
%{rpmhome}/rpmrc

%{rpmhome}/rpmdb_*
%{rpmhome}/rpm.daily
%{rpmhome}/rpm.log
%{rpmhome}/rpm.supp
%{rpmhome}/rpm2cpio.sh
%{rpmhome}/tgpg

%{rpmhome}/platform

%dir %{rpmhome}/fileattrs

%files libs
%{_libdir}/librpmio.so.*
%{_libdir}/librpm.so.*
%if %{with plugins}
%dir %{_libdir}/rpm-plugins

%files plugin-syslog
%{_libdir}/rpm-plugins/syslog.so

#%%files plugin-selinux
#%%{_libdir}/rpm-plugins/selinux.so

#%%files plugin-systemd-inhibit
#%%{_libdir}/rpm-plugins/systemd_inhibit.so
#%%{_mandir}/man8/rpm-plugin-systemd-inhibit.8*

#%%files plugin-ima
#%%{_libdir}/rpm-plugins/ima.so

%files plugin-prioreset
%{_libdir}/rpm-plugins/prioreset.so

#%%files plugin-audit
#%%{_libdir}/rpm-plugins/audit.so
# with plugins
%endif

%files build-libs
%{_libdir}/librpmbuild.so.*

%files sign-libs
%{_libdir}/librpmsign.so.*

%files build
%{_bindir}/rpmbuild
%{_bindir}/gendiff
%{_bindir}/rpmspec

%{_mandir}/man1/gendiff.1*
%{_mandir}/man8/rpmbuild.8*
%{_mandir}/man8/rpmdeps.8*
%{_mandir}/man8/rpmspec.8*

%{rpmhome}/brp-*
%{rpmhome}/check-*
%{rpmhome}/debugedit
%{rpmhome}/sepdebugcrcfix
%{rpmhome}/find-debuginfo.sh
%{rpmhome}/find-lang.sh
%{rpmhome}/*provides*
%{rpmhome}/*requires*
%{rpmhome}/*deps*
%{rpmhome}/*.prov
%{rpmhome}/*.req
%{rpmhome}/config.*
%{rpmhome}/mkinstalldirs
%{rpmhome}/fileattrs/*

%files sign
%{_bindir}/rpmsign
%{_mandir}/man8/rpmsign.8*

%files -n python2-%{name}
%{python2_sitearch}/%{name}/
%{python2_sitearch}/%{name}-%{version}*.egg-info

%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}*.egg-info

%files devel
%{_mandir}/man8/rpmgraph.8*
%{_bindir}/rpmgraph
%{_libdir}/librp*[a-z].so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

#%%files cron
#%%{_sysconfdir}/cron.daily/rpm
#%%config(noreplace) %%{_sysconfdir}/logrotate.d/rpm

%files apidocs
%license COPYING
%doc doc/librpm/html/*

%changelog
* Sat Oct 10 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-18
- Fix up fontconfig discovery when building font packages

* Sat Aug 22 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-17
- Include dep on gpg2 now we have it.

* Thu Jul 30 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-16
- Rewrite some /usr/bin/env paths that aren''t fixed by macros (yet)

* Thu Jun 18 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-15
- Depend on newer libdicl

* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-14
- Include python2 bindings generation

* Sat Jun 06 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-13
- Merge patches into a single patch, more fix up of hardcoded paths.

* Mon Jun 01 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-12
- Now with better macros, enable python bindings for rpm

* Sun May 10 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-11
- Rebuild after cmake availability

* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-10
- Correct manpath

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-9
- Remove hard coded shell paths/bashisms, retire cron package, detect IRIX (32bit) as well as IRIX64

* Thu Feb 20 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-7
- Rebuild due to libdicl upgrade to 0.1.19

* Wed Oct 23 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.15.0-6
- Revert armv8 detection improvements
