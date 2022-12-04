%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        dnf/yum equivalent using C libs
Name:           tdnf
Version:        3.1.5
Release:        3%{?dist}
Vendor:         VMware, Inc.
Distribution:   Photon
License:        LGPLv2.1,GPLv2
URL:            https://github.com/vmware/%{name}
Group:          Applications/RPM
Source0:        %{name}-%{version}.tar.gz
%define sha1    %{name}=48bc98b57a50a580a56d00988bf3955be5d749a4

# Patch0:         pool_flag_noinstalledobsoletes.patch
Patch100:		cmakelist-paths.sgifixes.patch
Patch101:		client-defines.sgifixes.patch
Patch102: 	    tdnf-conf.sgifixes.patch
Patch103:		tdnf-pool.sgifixes.patch
Patch104:		tdnf-client.sgifixes.patch
Patch105:		tdnf-common-utils.sgifixes.patch
Patch106:       cli-termios.sgifixes.patch
# mach's crappy interpolation patch
# Patch106:		tdnf-client-rpmtrans.sgifixes.patch
# Patch107:		tdnf-printfprecision.sgifixes.patch
Patch108:		tdnf-no-dlclose-plugins.patch

Requires:       rpm-libs
Requires:       libcurl
Requires:       tdnf-cli-libs = %{version}-%{release}
Requires:       libsolv
Requires:       libmetalink

BuildRequires:  popt-devel
BuildRequires:  rpm-devel
BuildRequires:  openssl-devel >= 1.1.1
BuildRequires:  libsolv-devel >= 0.7.14
# this definitely won't do anything bad at all
# BuildRequires:  libsolv-devel >= 0.7.19
BuildRequires:  curl-devel
BuildRequires:  libmetalink-devel
# BuildRequires:  systemd
#plugin repogpgcheck
BuildRequires:  gpgme-devel
BuildRequires:  cmake
BuildRequires:  python3-devel

# %if %{with_check}
# BuildRequires:  createrepo_c
# BuildRequires:  glib
# BuildRequires:  libxml2
# %endif

# Obsoletes:      yum
Provides:       yum

%description
tdnf is a yum/dnf equivalent which uses libsolv and libcurl

%define _tdnfpluginsdir %{_libdir}/tdnf-plugins

%package    devel
Summary:    A Library providing C API for tdnf
Group:      Development/Libraries
Requires:   tdnf = %{version}-%{release}
Requires:   libsolv-devel

%description devel
Development files for tdnf

%package	cli-libs
Summary:	Library providing cli libs for tdnf like clients
Group:		Development/Libraries

%description cli-libs
Library providing cli libs for tdnf like clients.

%package    plugin-repogpgcheck
Summary:    tdnf plugin providign gpg verification for repository metadata
Group:      Development/Libraries
Requires:   gpgme

%description plugin-repogpgcheck
tdnf plugin providign gpg verification for repository metadata

%package    python
Summary:    python bindings for tdnf
Group:      Development/Libraries
Requires:   python3

%description python
python bindings for tdnf

%package automatic
Summary:   %{name} - automated upgrades
Group:     Development/Libraries
Requires:  %{name} = %{version}-%{release}
%{?systemd_requires}

%description automatic
Systemd units that can periodically download package upgrades and apply them.

%prep
%autosetup -p1 -n %{name}-%{version}

# Rewrite some hardcoded paths (just in case used in tests etc)
perl -pi -e "s|/var/cache/tdnf|%{_prefix}/var/cache/tdnf|g" etc/motdgen.d/02-tdnf-updateinfo.sh

perl -pi -e "s|/etc/tdnf/|%{_prefix}/etc/tdnf/|g" bin/tdnf-automatic.in
perl -pi -e "s|/usr/bin/env bash|%{_bindir}/bash|g" bin/tdnf-automatic.in

perl -pi -e "s|/usr/bin/env bash|%{_bindir}/bash|g" bin/tdnf-cache-updateinfo.in
perl -pi -e "s|/var/cache/tdnf|%{_prefix}/var/cache/tdnf|g" bin/tdnf-cache-updateinfo.in

# Remove openssl finder that doesn't work for RSE
rm cmake/FindOpenSSL.cmake

%build
mkdir build && cd build
export CFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT $RPM_OPT_FLAGS -g"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
cmake \
-DCMAKE_INSTALL_PREFIX=%{_prefix} \
-DCMAKE_INSTALL_FULL_SYSCONDIR=%{_sysconfdir} \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_C_FLAGS_RELEASE="$CFLAGS" \
-DMOTGEN_DIR=%{_sysconfdir}/motdgen.d \
-DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
-DSYSTEMD_DIR=%{_prefix}/lib/systemd/system \
..

VERBOSE=1 make %{?_smp_mflags} && make python

%check
cd build && make %{?_smp_mflags} check

%install
cd build && make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.a' -delete
mkdir -p %{buildroot}%{_prefix}/var/cache/tdnf
mkdir -p %{buildroot}/%{_libdir}/systemd/system/
ln -sf %{_bindir}/tdnf %{buildroot}%{_bindir}/tyum
ln -sf %{_bindir}/tdnf %{buildroot}%{_bindir}/yum
mv %{buildroot}%{_libdir}/pkgconfig/tdnfcli.pc %{buildroot}%{_libdir}/pkgconfig/tdnf-cli-libs.pc
mkdir -p %{buildroot}/%{_tdnfpluginsdir}/tdnfrepogpgcheck
mv %{buildroot}/%{_tdnfpluginsdir}/libtdnfrepogpgcheck.so %{buildroot}/%{_tdnfpluginsdir}/tdnfrepogpgcheck/libtdnfrepogpgcheck.so
rm -rf %{buildroot}%{_prefix}/lib/systemd/system/

cd python
python3 setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}
cd ..
find %{buildroot} -name '*.pyc' -delete

%files
    %defattr(-,root,root,0755)
    %{_bindir}/tdnf
    %{_bindir}/tyum
    %{_bindir}/yum
    %{_bindir}/tdnf-cache-updateinfo
    %{_libdir}/libtdnf.so.*
    %config(noreplace) %{_sysconfdir}/tdnf/tdnf.conf
    %config %{_sysconfdir}/motdgen.d/02-tdnf-updateinfo.sh
    %dir %{_prefix}/var/cache/tdnf
    %{_datadir}/bash-completion/completions/tdnf

%files devel
    %defattr(-,root,root)
    %{_includedir}/tdnf/*.h
    %{_libdir}/libtdnf.so
    %{_libdir}/libtdnfcli.so
    %{_libdir}/pkgconfig/tdnf.pc
    %{_libdir}/pkgconfig/tdnf-cli-libs.pc

%files cli-libs
    %defattr(-,root,root)
    %{_libdir}/libtdnfcli.so.*

%files plugin-repogpgcheck
    %defattr(-,root,root)
    %dir %{_sysconfdir}/tdnf/pluginconf.d
    %config(noreplace) %{_sysconfdir}/tdnf/pluginconf.d/tdnfrepogpgcheck.conf
    %{_tdnfpluginsdir}/tdnfrepogpgcheck/libtdnfrepogpgcheck.so

%files python
    %defattr(-,root,root)
    %{python3_sitelib}/*

%files automatic
    %defattr(-,root,root,0755)
    %{_bindir}/%{name}-automatic
    %config(noreplace) %{_sysconfdir}/%{name}/automatic.conf

%changelog
*   Wed Nov 17 2021 David Stancu <dstancu@nyu.edu> - 3.1.5-3
-   rse update to 3.1.5
*   Wed Oct 06 2021 Oliver Kurth <okurth@vmware.com> 3.1.5-1
-   update to 3.1.5
-   add minversions config option
-   make pytests arch independent (does not affect functionality)
*   Mon Aug 2 2021 Oliver Kurth <okurth@vmware.com> 3.1.4-1
-   update to 3.1.4
-   fix configreader key reading logic
*   Tue Jun 29 2021 Oliver Kurth <okurth@vmware.com> 3.1.3-1
-   update to 3.1.3
*   Wed Jun 23 2021 Oliver Kurth <okurth@vmware.com> 3.1.2-1
-   update to 3.1.2
*   Fri Jun 11 2021 Oliver Kurth <okurth@vmware.com> 3.1.0-3
-   rebuild with libsolv 0.7.19
*   Thu Jun 03 2021 Shreenidhi Shedi <sshedi@vmware.com> 3.1.0-2
-   fix segfaulting when gpgcheck is enabled & no key configured
*   Tue Jun 01 2021 Oliver Kurth <okurth@vmware.com> 3.1.0-1
-   update to 3.1.0
*   Tue Apr 06 2021 Oliver Kurth <okurth@vmware.com> 3.0.2-1
-   update to 3.0.2
*   Sun Dec 20 2020 Daniel Hams <daniel.hams@gmail.com> 3.0.0-5
-   Little cleanups (paths, RPATH, printf precision, bad SSL discovery, use RSE OPT flags)
*  	Sat Dec 19 2020 David Stancu <dstancu@nyu.edu> 3.0.0-4
-	  Make TDNFNormalizePath a no-op (since it is only used with the cache dir, which is already normalized)
-   Expand $releasever and $basearch in GPG urls
*   Thu Dec 03 2020 David Stancu <dstancu@nyu.edu> 3.0.0-3
-	  Built for sgug-rse!
*   Thu Oct 29 2020 Keerthana K <keerthanak@vmware.com> 3.0.0-2
-   Fix coverity scan issues and fedora pytest issue.
*   Tue Oct 27 2020 Keerthana K <keerthanak@vmware.com> 3.0.0-1
-   Update to v3.0.0-beta
*   Sun Sep 06 2020 Satya Naga Vasamsetty <svasamsetty@vmware.com> 2.1.1-3
-   Rebuild with openssl 1.1.1
*   Sat Aug 15 2020 Shreenidhi Shedi <sshedi@vmware.com> 2.1.1-2
-   Cherry-pick some critical fixes from vmware/tdnf:dev
*   Thu Jun 04 2020 Tapas Kundu <tkundu@vmware.com> 2.1.1-1
-   Update to 2.1.1
*   Tue Mar 24 2020 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.1.0-2
-   Fix distroverpkg search to look for provides instead of name
*   Thu Feb 20 2020 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.1.0-1
-   Update to 2.1.0
*   Sun Sep 08 2019 Ankit Jain <ankitja@vmware.com> 2.0.0-11
-   Added more rules for skipconflicts and skipobsoletes to check command.
*   Fri Mar 15 2019 Ankit Jain <ankitja@vmware.com> 2.0.0-10
-   Added skipconflicts and skipobsoletes to check command.
*   Thu Mar 14 2019 Keerthana K <keerthanak@vmware.com> 2.0.0-9
-   GPGCheck fix on RPM version 4.14.2
*   Mon Mar 04 2019 Keerthana K <keerthanak@vmware.com> 2.0.0-8
-   makecache and refresh command updates.
*   Thu Feb 14 2019 Keerthana K <keerthanak@vmware.com> 2.0.0-7
-   Fix to address issues when no repos are enabled.
*   Wed Jan 23 2019 Keerthana K <keerthanak@vmware.com> 2.0.0-6
-   Fix Memory leak and curl status type.
*   Wed Jan 02 2019 Keerthana K <keerthanak@vmware.com> 2.0.0-5
-   Added make check.
*   Tue Dec 04 2018 Keerthana K <keerthanak@vmware.com> 2.0.0-4
-   Add support for libsolv caching.
-   Fix bug in tdnf updateinfo command.
-   Fix bug on list available command.
*   Wed Nov 21 2018 Keerthana K <keerthanak@vmware.com> 2.0.0-3
-   Update to 2.0.0 beta release.
*   Mon Oct 08 2018 Keerthana K <keerthanak@vmware.com> 2.0.0-2
-   Fix bug on tdnf crash when photon-iso repo only enabled without mounting cdrom.
*   Fri Feb 09 2018 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.0.0-1
-   update to 2.0.0
*   Tue Jan 30 2018 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.2-3
-   patch to error out early for permission issues.
*   Tue Oct 10 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.2-2
-   Fix bug in obsolete protected packages.
*   Wed Oct 4 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.2-1
-   update to v1.2.2
*   Sat Sep 30 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.1-5
-   Output problems while resolving to stderr (instead of stdout)
*   Wed Sep 27 2017 Bo Gan <ganb@vmware.com> 1.2.1-4
-   Improve suggestion in motd message
*   Thu Sep 14 2017 Bo Gan <ganb@vmware.com> 1.2.1-3
-   Add suggestion in motd message
*   Fri Jul 21 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.1-2
-   Modify quiet patch.
*   Tue Jul 18 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.1-1
-   Update to v1.2.1
*   Tue May 30 2017 Bo Gan <ganb@vmware.com> 1.2.0-5
-   Fix cache-updateinfo script again
*   Fri May 12 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.0-4
-   Patch repo refresh to allow quiet flags
*   Wed May 10 2017 Bo Gan <ganb@vmware.com> 1.2.0-3
-   Fix cache-updateinfo script
*   Fri May 05 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.0-2
-   Fix Requires for cli-libs
*   Wed May 03 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.0-1
-   update to v1.2.0
*   Sun Apr 30 2017 Bo Gan <ganb@vmware.com> 1.1.0-5
-   Do not write to stdout in motd triggers
*   Thu Apr 20 2017 Bo Gan <ganb@vmware.com> 1.1.0-4
-   motd hooks/triggers for updateinfo notification
*   Fri Apr 14 2017 Dheerajs Shetty <dheerajs@vmware.com> 1.1.0-3
-   Adding a patch to compile with latest hawkey version
*   Mon Dec 19 2016 Xiaolin Li <xiaolinl@vmware.com> 1.1.0-2
-   BuildRequires libsolv-devel.
*   Thu Dec 08 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.1.0-1
-   update to v1.1.0
*   Thu Nov 17 2016 Alexey Makhalov <amakhalov@vmware.com> 1.0.9-3
-   Use rpm-libs at runtime
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.9-2
-   GA - Bump release of all rpms
*   Fri May 20 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.9-1
-   Update to 1.0.9. Contains fixes for updateinfo.
*   Wed May 4 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.8-3
-   Fix link installs, fix devel header dir
*   Fri Apr 1 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.8-2
-   Update version which was missed with 1.0.8-1, apply string limits
*   Fri Apr 1 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.8-1
-   Code scan fixes, autotest path fix, support --releasever
*   Thu Jan 14 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.7
-   Fix return codes on install and check-update
-   Add tests for install existing and update
*   Wed Jan 13 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.6
-   Support distroverpkg and add tests to work with make check
*   Mon Dec 14 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.5
-   Support for multiple packages in alter commands
-   Support url vars for releasever and basearch
*   Fri Oct 2 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.4
-   Fix upgrade to work without args, Engage distro-sync
-   Fix install to resolve to latest available
-   Fix formats, fix refresh on download output
*   Tue Sep 8 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.3
-   Fix metadata creation issues. Engage refresh flag.
-   Do not check gpgkey when gpgcheck is turned off in repo.
*   Thu Jul 23 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.2
-   Support reinstalls in transaction. Handle non-existent packages correctly.
*   Mon Jul 13 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.1-2
-   Create -debuginfo package. Use parallel make.
*   Tue Jun 30 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.1
-   Proxy support, keepcache fix, valgrind leaks fix
*   Fri Jan 23 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0
-   Initial build.  First version
