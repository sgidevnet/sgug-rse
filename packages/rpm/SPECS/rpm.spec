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
%global rel 10

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
Patch2001: rpm.sgifixesldn32path.patch
Patch2002: rpm.sgifixelfdeps.patch
Patch2003: rpm.sgistriplibs.patch
Patch2004: rpm.sgifixesaddshellvars.patch

BuildRequires: libdicl-devel >= 0.1.19
Requires: libdicl >= 0.1.19

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

#%if %{with plugins}
#BuildRequires: libselinux-devel
#BuildRequires: dbus-devel
#BuildRequires: audit-libs-devel
#%endif

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
#Requires: %{_bindir}/gpg2

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

#%package -n python2-%{name}
#Summary: Python 2 bindings for apps which will manipulate RPM packages
#BuildRequires: python2-devel
#%{?python_provide:%python_provide python2-%{name}}
#Requires: %{name}-libs%{?_isa} = %{version}-%{release}
#Provides: %{name}-python = %{version}-%{release}
#Obsoletes: %{name}-python < %{version}-%{release}

#%description -n python2-%{name}
#The python2-rpm package contains a module that permits applications
#written in the Python programming language to use the interface
#supplied by RPM Package Manager libraries.

#This package should be installed if you want to develop Python 2
#programs that will manipulate RPM packages and databases.

#%package -n python3-%{name}
#Summary: Python 3 bindings for apps which will manipulate RPM packages
#BuildRequires: python3-devel
#%{?python_provide:%python_provide python3-%{name}}
#Requires: %{name}-libs%{?_isa} = %{version}-%{release}
#Provides: %{name}-python3 = %{version}-%{release}
#Obsoletes: %{name}-python3 < %{version}-%{release}
#Obsoletes: platform-python-%{name} < %{version}-%{release}

#%description -n python3-%{name}
#The python3-rpm package contains a module that permits applications
#written in the Python programming language to use the interface
#supplied by RPM Package Manager libraries.

#This package should be installed if you want to develop Python 3
#programs that will manipulate RPM packages and databases.

%package apidocs
Summary: API documentation for RPM libraries
BuildArch: noarch

%description apidocs
This package contains API documentation for developing applications
that will manipulate RPM packages and databases.

#%package cron
#Summary: Create daily logs of installed packages.
#BuildArch: noarch
#Requires: crontabs logrotate rpm = %{version}-%{release}

#%description cron
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

# Rewrite hardcoded paths to /bin/sh that cause us problems on irix
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" lib/rpmscript.c
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" cliutils.c
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" build/parseScript.c
perl -pi -e "s|/bin/sh|%{_prefix}/bin/sh|g" macros.in

# Rewrite pkgconfigdeps
perl -pi -e "s|/bin/bash|%{_prefix}/bin/bash|g" scripts/pkgconfigdeps.sh
perl -pi -e "s|/usr/bin/pkg-config|%{_prefix}/bin/pkg-config|g" scripts/pkgconfigdeps.sh

%if %{with int_bdb}
ln -s db-%{bdbver} db
%endif

%build
%set_build_flags
export CPPFLAGS="-D_SGI_SOURCES -D_SGI_REENTRANT_FUNCTIONS -I%{_includedir}/libdicl-0.1"
export LIBS="-lgen -ldicl-0.1 -llzma -lintl"

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
    %{?with_ndb: --with-ndb} \
    %{?with_libimaevm: --with-imaevm} \
    %{?with_zstd: --enable-zstd} \
    %{?with_lmdb: --enable-lmdb} \
    --with-crypto=openssl \
    --disable-openmp

#    --enable-python \ #
#    --with-cap \ #
#    --with-acl \ #
#    --with-selinux \ #

%make_build

#cd python
#py2_build
#py3_build
#cd ..

%install
%make_install

# We need to build with --enable-python for the self-test suite, but we
# actually package the bindings built with setup.py (#531543#c26)
#cd python
#py2_install
#py3_install
#cd ..


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

#%files plugin-selinux
#%{_libdir}/rpm-plugins/selinux.so

#%files plugin-systemd-inhibit
#%{_libdir}/rpm-plugins/systemd_inhibit.so
#%{_mandir}/man8/rpm-plugin-systemd-inhibit.8*

#%files plugin-ima
#%{_libdir}/rpm-plugins/ima.so

%files plugin-prioreset
%{_libdir}/rpm-plugins/prioreset.so

#%files plugin-audit
#%{_libdir}/rpm-plugins/audit.so
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

#%files -n python2-%{name}
#%{python2_sitearch}/%{name}/
#%{python2_sitearch}/%{name}-%{version}*.egg-info

#%files -n python3-%{name}
#%{python3_sitearch}/%{name}/
#%{python3_sitearch}/%{name}-%{version}*.egg-info

%files devel
%{_mandir}/man8/rpmgraph.8*
%{_bindir}/rpmgraph
%{_libdir}/librp*[a-z].so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

#%files cron
#%{_sysconfdir}/cron.daily/rpm
#%config(noreplace) %{_sysconfdir}/logrotate.d/rpm

%files apidocs
%license COPYING
%doc doc/librpm/html/*

%changelog
* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-10
- Correct manpath

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-9
- Remove hard coded shell paths/bashisms, retire cron package, detect IRIX (32bit) as well as IRIX64

* Thu Feb 20 2020 Daniel Hams <daniel.hams@gmail.com> - 4.15.0-7
- Rebuild due to libdicl upgrade to 0.1.19

* Wed Oct 23 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.15.0-6
- Revert armv8 detection improvements

* Mon Oct 21 2019 Stephen Gallagher <sgallagh@redhat.com> - 4.15.0-5
- Revert aliasing arm64 to aarch64
- Resolves: rhbz#1763831

* Fri Oct 18 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-3
- Revert problematic sub-variants of armv8 (#1691430)

* Tue Oct 15 2019 Adam Williamson <awilliam@redhat.com> - 4.15.0-2
- Revert systemd inhibit plugin's calling of dbus_shutdown (#1750575)

* Thu Sep 26 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-1
- Update to 4.15.0 final (https://rpm.org/wiki/Releases/4.15.0)

* Wed Aug 28 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-0.rc1.1
- Update to 4.15.0-rc1

* Tue Aug 27 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-0.beta.6
- Fix some issues in the thread cap logic

* Mon Aug 26 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-0.beta.5
- Re-enable test-suite, temporarily disabled during alpha troubleshooting

* Fri Aug 23 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-0.beta.4
- Cap number of threads on 32bit platforms (#1729382)
- Drop %%_lto_cflags macro (reverted upstream)

* Fri Aug 23 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-0.beta.3
- Restore strict order of build scriptlet stdout/stderr output

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 4.15.0-0.beta.2.3
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Miro Hrončok <mhroncok@redhat.com> - 4.15.0-0.beta.2.2
- Rebuilt for libimaevm.so.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.0-0.beta.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 18:30:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.15.0-0.beta.2
- Backport patch to not set RPMTAG_BUILDTIME to SOURCE_DATE_EPOCH

* Thu Jun 27 2019 Panu Matilainen <pmatilai@redhat.com> - 4.15.0-0.beta.1
- Rebase to 4.15.0 beta

* Thu Jun 20 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.90-0.git14653.18
- Fix excessive TLS use, part II (#1722181)

* Thu Jun 20 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.90-0.git14653.17
- Fix excessive TLS use (#1722181)

* Wed Jun 19 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.90-0.git14653.16
- Drop buildarch again now that python_provide no longer needs it (#1720139)

* Fri Jun 14 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.90-0.git14653.15
- Temporarily re-enable buildarch macro for python_provide macro use (#1720139)

* Thu Jun 13 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.90-0.git14653.14
- Don't fail build trying to kill a non-existent process (#1720143)

* Tue Jun 11 14:59:16 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.90-0.git14653.13
- Fix build of binary packages in parallel

* Tue Jun 11 00:08:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.90-0.git14653.10
- Revert generation of binary packages in parallel

* Mon Jun 10 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.90-0.git14653.1
- Update to 4.15.0 alpha

* Mon Jun 10 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-14
- Drop support for sanitizer build, it never really worked anyway
- Drop leftover build-dependency on binutils-devel
- Truncate changelog to rpm 4.14.x (last two years)

* Mon Jun 10 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-13
- Drop support for Fedora < 28 builds
- Drop leftover BDB-related compiler flag foo

* Fri Jun 07 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-12
- Use pre-determined buildhost in test-suite to avoid DNS usage
- Drop obsolete specspo and gpg2 related patches

* Fri Jun 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.2.1-11
- Use py2/3 macros for building and installing the bindings

* Tue May 21 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-10
- Support build-id generation from compressed ELF files (#1650072)

* Fri May 03 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.2.1-9
- Suggest gdb-minimal

* Thu Apr 25 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-8
- Replace deprecated __global_ldflags uses with build_ldflags macro

* Thu Apr 11 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-7
- Fix excessive reference counting on faked string .decode()

* Wed Apr 10 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-6
- Unbreak Python 3 API by returning string data as surrogate-escaped utf-8
  string objects instead of bytes (#1693751)
- As a temporary crutch,  monkey-patch a .decode() method to returned strings
  to give users time to migrate from the long-standing broken behavior

* Wed Apr 10 2019 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-5
- Generate minidebug for PIE executables on file >= 5.33 too
- Backport find-debuginfo --g-libs option for glibc's benefit (#1661512)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.2.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-4
- Backport the new modularity label tag (#1650286)

* Mon Nov 19 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-3
- Take prefix into account when compressing man pages etc for Flatpak builds

* Wed Oct 24 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-2
- Selinux plugin requires a base policy to work (#1641631)

* Mon Oct 22 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2.1-1
- Rebase to rpm 4.14.2.1 (http://rpm.org/wiki/Releases/4.14.2.1)

* Wed Oct 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.2-9
- Push name/epoch/version/release macro before invoking depgens

* Tue Oct 16 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.2-8
- Resurrect long since broken Lua library path

* Fri Oct 12 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-7
- Actually fail build on test-suite failures again
- Invoke python2 explicitly from test-suite to unbreak build, part II

* Thu Oct 11 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-6
- Drop duplicate BDB buildrequire
- Drop nowadays unnecessary BDB macro foo
- Drop nowadays unnecessary manual libcap dependency

* Thu Oct 11 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-5
- Own all rpmdb files and ensure the list remains up to date
- Drop redundant verify exclusions on rpmdb ghosts
- Fix build when systemd is not installed (duh)

* Thu Oct 11 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-4
- Erm, really use the macro for tmpfiles.d path
- Erm, don't nuke buildroot at beginning of %%install
- Use modern build/install helper macros

* Thu Oct 11 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-3
- Eh, selinux plugin dependency condition was upside down (#1493267)
- Drop no longer necessary condition over imaevm name
- Drop no longer necessary obsolete on compat-librpm3

* Thu Oct 11 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-2
- Fix ancient Python GIL locking bug (#1632488)
- Use the appropriate macro for tmpfiles.d now that one exists

* Tue Aug 21 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-1
- Update to rpm 4.14.2 final (http://rpm.org/wiki/Releases/4.14.2)

* Mon Aug 13 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-0.rc2.2
- Move python-macro-helper to main package where the macros are (#1577860)

* Wed Aug 08 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-0.rc2.1
- Update to rpm 4.14.2-rc2

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.2-0.rc1.2
- Decompress DWARF compressed ELF sections

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.2-0.rc1.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 4.14.2-0.rc1.1.1
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.2-0.rc1.1
- Update to rpm 4.14.2-rc1
- Patching test-suite for python2 too painful, just sed it instead
- Fix premature version increment from previous changelog entries, oops

* Fri Jun 29 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.1-13
- Ehm, need to patch the autogenerated rpmtests script too for python2
- Ehm, it's ldconfig_scriptlets not scripts
- Drop the non-working python envvar magic from obsoleted change

* Fri Jun 29 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.1-12
- Invoke python2 explicitly from test-suite to unbreak build

* Fri Jun 29 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.1-11
- Remove direct ldconfig calls, use compat macros instead

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 4.14.1-10.1
- Rebuilt for Python 3.7

* Mon May 28 2018 Miro Hrončok <mhroncok@redhat.com> - 4.14.1-10
- Backport upstream solution to make brp-python-bytecompile automagic part opt-outable
  https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation

* Tue May 22 2018 Mark Wielaard <mjw@fedoraproject.org> - 4.14.1-9
- find-debuginfo.sh: Handle application/x-pie-executable (#1581224)

* Tue Feb 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.1-8
- Split rpm-build-libs to one more subpackage rpm-sign-libs

* Mon Feb 19 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.1-7
- Explicitly BuildRequire gcc and make

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.1-6.1
- Escape macros in %%changelog

* Wed Jan 31 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.1-6
- Avoid unnecessary macro helper dependency on /usr/bin/python (#1538657)
- Fix release of previous changelog entry

* Tue Jan 30 2018 Tomas Orsava <torsava@redhat.com> - 4.14.1-5
- Add envvar that will be present during RPM build,
  Part of a Fedora Change for F28: "Avoid /usr/bin/python in RPM build"
  https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build

* Tue Jan 30 2018 Petr Viktorin <pviktori@redhat.com> - 4.14.1-4
- Skip automatic Python byte-compilation if *.py files are not present

* Thu Jan 25 2018 Florian Weimer <fweimer@redhat.com> - 4.14.1-3
- Rebuild to work around gcc bug leading to librpm miscompilation (#1538648)

* Thu Jan 18 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.1-2
- Avoid nuking the new python-macro-helper along with dep generators (#1535692)

* Tue Jan 16 2018 Panu Matilainen <pmatilai@redhat.com> - 4.14.1-1
- Rebase to rpm 4.14.1 (http://rpm.org/wiki/Releases/4.14.1)

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.0-5
- Fix typo in Obsoletes

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.14.0-4
- Remove platform-python bits

* Thu Oct 26 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-3
- Move selinux plugin dependency to selinux-policy in Fedora >= 28 (#1493267)

* Thu Oct 12 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-2
- Dump out test-suite log in case of failures again
- Don't assume per-user groups in test-suite

* Thu Oct 12 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-1
- Rebase to rpm 4.14.0 final (http://rpm.org/wiki/Releases/4.14.0)

* Tue Oct 10 2017 Troy Dawson <tdawson@redhat.com> - 4.14.0-0.rc2.6
- Cleanup spec file conditionals

* Tue Oct 03 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc2.5
- Add build conditionals for zstd and lmdb support
- Enable zstd support

* Tue Oct 03 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc2.4
- Spec cleanups

* Fri Sep 29 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc2.3
- BuildRequire gnupg2 for the testsuite

* Fri Sep 29 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc2.2
- ima-evm-utils only has a -devel package in fedora >= 28

* Thu Sep 28 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc2.1
- Rebase to rpm 4.14.0-rc2 (http://rpm.org/wiki/Releases/4.14.0)

* Mon Sep 18 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc1.3
- Fix Ftell() past 2GB on 32bit architectures (#1492587)

* Thu Sep 07 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc1.2
- Actually honor with/without libimaevm option
- ima-evm-utils-devel >= 1.0 is required for rpm >= 4.14.0

* Wed Sep 06 2017 Panu Matilainen <pmatilai@redhat.com> - 4.14.0-0.rc1.1
- Rebase to rpm 4.14.0-rc1 (http://rpm.org/wiki/Releases/4.14.0)
- Re-enable SHA256 header digest generation (see #1480407)

* Mon Aug 28 2017 Panu Matilainen <pmatilai@redhat.com> - 4.13.90-0.git14000.8
- Band-aid for DB_VERSION_MISMATCH errors on glibc updates (#1465809)

* Thu Aug 24 2017 Panu Matilainen <pmatilai@redhat.com> - 4.13.90-0.git14000.7
- Remove ugly kludges from posttrans script, BDB handles this now

* Fri Aug 18 2017 Panu Matilainen <pmatilai@redhat.com> - 4.13.90-0.git14000.6
- Silence harmless but bogus error message on noarch packages (#1482144)

* Thu Aug 17 2017 Miro Hrončok <mhroncok@redhat.com> - 4.13.90-0.git14002.5
- Build with platform_python

* Mon Aug 14 2017 Miro Hrončok <mhroncok@redhat.com> - 4.13.90-0.git14000.4
- Add platform-python bytecompilation patch: platform-python-bytecompile.patch
- Add platform python deps generator patch: platform-python-abi.patch
- Add a platform-python subpackage and remove system python related declarations
- Build rpm without platform_python for bytecompilation
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Mon Aug 14 2017 Panu Matilainen <pmatilai@redhat.com> - 4.13.90-0.git14000.3
- Disable macro argument quoting as a band-aid to #1481025

* Fri Aug 11 2017 Panu Matilainen <pmatilai@redhat.com> - 4.13.90-0.git14000.2
- Disable SHA256 header-only digest generation temporarily (#1480407)

* Thu Aug 10 2017 Panu Matilainen <pmatilai@redhat.com> - 4.13.90-0.git14000.1
- Rebase to rpm 4.13.90 aka 4.14.0-alpha (#1474836)

