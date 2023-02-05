Name:     icecream
Version:  1.3
Release:  4%{?dist}
Summary:  Distributed compiler
License:  GPLv2+
URL:      https://github.com/icecc/icecream
Source0:  https://github.com/icecc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:  fedora-sysconfig.icecream
Source2:  icecream.module.in
Source3:  icecream.fc
Source4:  icecream.te
Source5:  icecream.if
Source6:  iceccd.service
Source7:  icecc-scheduler.service
Source11: icecream-tmpfiles.conf
Source12: icecream.xml
Source13: icecream-scheduler.xml
Patch1:   0001-Revert-chmod-chown-envs-dir-when-preparing-this.patch
Patch2:   0002-daemon-main-do-not-create-run-icecc-by-ourselves.patch
Patch3:   0003-Ignore-the-suse-directory.patch
Patch4:   0004-do-not-use-usr-bin-env.patch
Patch5:	  icecream.sgifixes.patch

BuildRequires: gcc-c++
#BuildRequires: libcap-ng-devel
BuildRequires: lzo-devel libzstd-devel libarchive-devel
#BuildRequires: docbook2X
BuildRequires: autoconf automake libtool
BuildRequires: make
Requires(post):   findutils

%define _tmpfilesdir /tmp

# description copied from Debian icecc package
%description
Icecream is a distributed compile system. It allows parallel compiling by
distributing the compile jobs to several nodes of a compile network running the
icecc daemon. The icecc scheduler routes the jobs and provides status and
statistics information to the icecc monitor. Each compile node can accept one
or more compile jobs depending on the number of processors and the settings of
the daemon. Link jobs and other jobs which cannot be distributed are executed
locally on the node where the compilation is started.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
#Requires: libcap-ng-devel%{?_isa}
Requires: lzo-devel%{?_isa}
Requires: libzstd-devel%{?_isa}
Requires: libarchive-devel%{?_isa}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

mkdir fedora
cp -p %{SOURCE6} %{SOURCE7} %{SOURCE11} fedora

%build
export CFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"

sed -ie 's,/usr/bin/,/usr/sgug/bin/,g' client/icecc-create-env.in
sed -ie 's,/usr/bin/,/usr/sgug/bin/,g' client/icecc-test-env.in

./autogen.sh

%configure \
    --disable-static \
    --enable-shared \
    --enable-clang-rewrite-includes \
    --enable-clang-wrappers \
	--without-man 

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# TODO: revisit why autoconf doesn't do this
echo "#undef HAVE_GETLOADAVG" >> config.h
echo "#undef HAVE_SYS_VFS_H" >> config.h
echo "#undef USE_SYSCTL" >> config.h

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/libicecc.la

# install config file and initscripts
#install -d -m 755 %{buildroot}/%{_unitdir}
#mkdir -p %{buildroot}%{_tmpfilesdir}
#install -p -m 644 fedora/icecream-tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/icecream.conf
#install -D -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/icecream

# create default working dir
mkdir -p %{buildroot}/%{_localstatedir}/cache/icecream
mkdir -p %{buildroot}/run/icecc/

# Make the environment-modules file
#mkdir -p %{buildroot}%{_modulesdir}/icecream
#sed  's#@LIBEXECDIR@#%{_libexecdir}#' < %{SOURCE2} > %{buildroot}%{_modulesdir}/icecream/icecc

%post
# Remove files owned by the user 'icecream' (used by older versions).
find %{_localstatedir}/cache/icecream/ -user icecream -delete 2>/dev/null
exit 0

%files
%license COPYING
%doc README NEWS TODO
%{_bindir}/icecc
%{_bindir}/icecc-create-env
%{_bindir}/icecc-test-env
%{_bindir}/icerun
%{_libexecdir}/icecc/
%{_libdir}/libicecc.so.*
%{_sbindir}/iceccd
%{_sbindir}/icecc-scheduler
%attr(0775, root, icecc) %{_localstatedir}/cache/icecream
%attr(0775, root, icecc) /run/icecc
##%{_mandir}/man*/*
##%{_tmpfilesdir}/icecream.conf

%files devel
%dir %{_includedir}/icecc/
%{_includedir}/icecc/*.h
%{_libdir}/libicecc.so
%{_libdir}/pkgconfig/icecc.pc

%changelog
* Thu Dec 31 2020 David Stancu <dstancu@nyu.edu> - 1.3-4
- Rebuild + patch for sgug-rse 

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Michal Schmidt <mschmidt@redhat.com> - 1.3-1
- Upstream release 1.3.

* Thu Aug 01 2019 Michal Schmidt <mschmidt@redhat.com> - 1.2-4
- Fix FTBFS, rely on PATH to run hardlink.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Michal Schmidt <mschmidt@redhat.com> - 1.2-1
- Upstream release 1.2.
- selinux: allow symlinks in foreign environment

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Michal Schmidt <mschmidt@redhat.com> - 1.1-4
- BuildRequire gcc-c++.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Michal Schmidt <mschmidt@redhat.com> - 1.1-2
- selinux: allow scheduler to perform connection checks

* Wed Aug 09 2017 Michal Schmidt <mschmidt@redhat.com> - 1.1-1
- Upstream release 1.1.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.10.rc3.g22fcc39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.9.rc3.g22fcc39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Michal Schmidt <mschmidt@redhat.com> - 1.1-0.8.rc3.g22fcc39
- Update to upstream rc3 plus latest commits.

* Mon Jul 03 2017 Michal Schmidt <mschmidt@redhat.com> - 1.1-0.7.rc2.g1c15f6b
- Current git snapshot.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.6.rc2.ga79f70f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Michal Schmidt <mschmidt@redhat.com> - 1.1-0.5.rc2.ga79f70f
- In scriptlets split the semanage calls for robustness. (#1391871)

* Fri Nov 11 2016 Michal Schmidt <mschmidt@redhat.com> - 1.1-0.4.rc2.ga79f70f
- Fix FTBFS on s390x. (#1393742)
- Do not use #!/usr/bin/env.

* Fri Nov 04 2016 Michal Schmidt <mschmidt@redhat.com> - 1.1-0.3.rc2.ga79f70f
- One more SELinux fix. (#1389570)

* Fri Nov 04 2016 Michal Schmidt <mschmidt@redhat.com> - 1.1-0.2.rc2.ga79f70f
- Fix fallout from 'icecream'->'icecc' user name change.
- Drop Group tag.

* Thu Nov 03 2016 Michal Schmidt <mschmidt@redhat.com> - 1.1-0.1.rc2.ga79f70f
- Update to current git snapshot.
- SELinux policy fixes. (#1389570, #1391871)
- Drop PATH_MAX patch of no obvious benefit.
- Prod firewalld in %%post.
- Move environment module file from under /etc to /usr.
- Do not ship /var/log/icecream.
- spec file cleanups.

* Wed Mar 16 2016 Helio Chissini de Castro <helio@kde.org> - 1.0.98-4
- Default user is icecc, not icecream

* Tue Mar 08 2016 Helio Chissini de Castro <helio@kde.org> - 1.0.98-3
- Re-apply config cleanup patch
- Remove libexec from configure since is already on macro
- Remove logrotate as not be a good idea
- Add github pull requests from Pino Toscano ( RedHat )

* Wed Mar 02 2016 Helio Chissini de Castro <helio@kde.org> - 1.0.98-2
- Add log entries and log dir
- Remove profile entries. We shouldn't be in the path, since tools rely on icecc binary
and this break the process since it relies on recursive call due to be in path.

* Thu Feb 25 2016 Helio Chissini de Castro <helio@kde.org> - 1.0.98-1
- Update for most recent version available by Suse
- Icecream is now in github

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14.20140822git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-13.20140822git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-12.20140822git
- Rebuilt for GCC 5 C++11 ABI change

* Fri Dec 12 2014 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-11.20140822git
- selinux: allow icecc_scheduler_t to read /proc/meminfo

* Fri Dec 12 2014 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-10.20140822git
- selinux: fix daemons running as unconfined_service_t
- selinux: fix label of icecc-create-env
- Fixes: rhbz#1173477

* Thu Nov 27 2014 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-9.20140822git
- selinux: allow the scheduler to read state via netlink route sockets
- Fixes: rhbz#1162321

* Fri Sep 05 2014 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-8.20140822git
- Update to current upstream git.
- Drops bundled minilzo, use system lzo library. (#1131794, CVE-2014-4607)
- Fix build of manpages (use docbook2X).
- Enable clang wrappers.
- Remove no longer necessary restorecon /var/log/icecc.
- Drop merged patches.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-5
- Drop the permissions to log to the old files from the SELinux policy.

* Mon Sep 02 2013 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-4
- Fix dropping of capabilities.
- Log everything to journal/syslog, not the custom log files.

* Fri Aug 30 2013 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-3
- Disable building with librsync. The upstream code to use it is unfinished
  and the only thing it does is leak memory.

* Fri Aug 30 2013 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-2
- Update the SELinux policy module and build it.
- Use tmpfiles.d to create /run/icecc instead of letting the daemon write to
  var_run_t directly.
- Add a patch to stop icecc-create-env from reading /etc/passwd.
- Batch semenage calls in scriptlets.

* Mon Aug 26 2013 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-1
- Rebase to current upstream release. (#888183, #914087, #925572, #992557)
- Build with librsync and libcap-ng support.
- Build manpages from included DocBook sources.
- Disable the SELinux module, it's out of date.
- Enable PIE. (#955456)
- Modernize spec file. (#850154)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for c++ ABI breakage

* Tue Feb 07 2012 Michal Schmidt <mschmidt@redhat.com> - 0.9.7-2
- systemd conversion

* Mon Feb 06 2012 Michal Schmidt <mschmidt@redhat.com> - 0.9.7-1
- Upstream release 0.9.7.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 03 2011 Michal Schmidt <mschmidt@redhat.com> - 0.9.6-4
- Add lto plugin for -fuse-linker-plugin (patch from dtardon)
- Fixes: BZ#675663

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.6-2
- Fix spaces instead of ':' separator for $PATH in icecream.csh.

* Tue Aug 03 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.6-1
- New upstream release. With an official tarball this time.
- Dropped icecream-fix-createenv-when-ldconfig-fails.patch
  It was never accepted upstream and it is not necessary with working ldconfig.
- Refreshed icecream-rename-scheduler.patch

* Thu Jul 08 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.5-7
- Build without SELinux only on RHEL 5.

* Thu Jul 08 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.5-6
- Moved away from fedora-usermgmt in favor of plain shadow-utils.

* Sun Jun 13 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.5-5
- Mark UDP port 8765 as icecc_scheduler_port_t.

* Sat Jun 12 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.5-4
- Require /usr/sbin/semanage for scriptlets. (BZ#581272)

* Sat Jun 12 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.5-3
- Fix incorrect handling of SELinux in the scriptlets.
- Avoid recursive rpm invocation (fixfiles -R).
- Fixes: BZ#581272

* Thu Mar 25 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.5-2
- SELinux policy fix (current selinux-policy assigns port 8765 to LIRC).

* Thu Mar 25 2010 Michal Schmidt <mschmidt@redhat.com> 0.9.5-1
- Upstream release 0.9.5.
  - new command 'icerun': serialize possibly resource-intensive tasks
  - minor bugfixes
- Refreshed icecream-rename-scheduler.patch.

* Mon Oct 12 2009 Michal Schmidt <mschmidt@redhat.com> 0.9.4-5
- Fix failure to build native environment in SELinux enforcing mode.
- 'cvs rm ...' unused patches.

* Mon Aug 17 2009 Michal Schmidt <mschmidt@redhat.com> 0.9.4-4
- SELinux policy: Allow untrusted binaries to getattr all filesystems.
  (BSD process accounting does vfs_getattr() to check disk space.)

* Fri Aug 14 2009 Michal Schmidt <mschmidt@redhat.com> 0.9.4-3
- Create the logfile for the scheduler in the initscript.
- Allow the scheduler to write to the log in the SELinux policy (BZ#517251).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 30 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.4-1
- Upstream release 0.9.4.
- Dropped merged patches.

* Mon Apr 06 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.3-6
- Fix wrong permissions on the cache dir preventing the jobs from being
  distributed.
- SELinux policy update based on review comments on refpolicy ML.

* Mon Mar 02 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.3-5
- Fix a fd leak from iceccd + avoid using system().
- Allows tighter SELinux policy.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.3-3
- Do not use --disable-rpath, icecream's configure script does not understand
  it and warns about it. We still remove rpath using the sed tricks.
- One more SELinux policy tweak.

* Mon Feb 16 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.3-2
- Updated and re-enabled the SELinux policy. The scheduler is now confined too.

* Mon Feb 16 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.3-1
- new upstream release
- Dropped merged patches.
- Added an upstream patch to fix compilation with gcc 4.4.

* Sat Feb 07 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.2-4
- one more fix for gcc 4.4.
- updated the scheduler renaming patch.

* Sat Feb 07 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.2-3
- add an upstream patch to fix FTBFS with gcc 4.4

* Wed Jan 28 2009 Michal Schmidt <mschmidt@redhat.com> - 0.9.2-2
- Fix the create-env script not to crash on relative paths in ld.so.conf.
- No need to build the native environment as root anymore.
- Disable the SELinux policy for now, it needs more work.

* Thu Nov 13 2008 Michal Schmidt <mschmidt@redhat.com> - 0.9.2-1
- Update to upstream release 0.9.2.
- The license is GPLv2+.
- Add manpages from SUSE src package.
- Add patch to run icecc --build-native as root.

* Tue Sep  2 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.0-12.20080117svn
- Include unowned icecc directories.
- Add defattr in devel pkg.

* Thu Mar 13 2008 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-11.20080117svn
- Minor SELinux policy fix.

* Sun Feb 10 2008 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-10.20080117svn
- Compile fix (added missing #includes).
- Conditional building of SELinux policy and documentation.
- Fix build on RHEL5.

* Tue Jan 29 2008 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-9.20080117svn
- SELinux policy fixes.

* Thu Jan 17 2008 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-8.20080117svn
- Update to current icecream-make-it-cool branch.

* Tue Jan  8 2008 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-7.20071101svn
- Build fix. meinproc is now in kdelibs3. BuildRequire that instead of kdelibs.

* Thu Nov 29 2007 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-6.20071101svn
- Rewritten the profile scripts to make icecream work together with ccache.

* Tue Nov 27 2007 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-5.20071101svn
- SELinux: Allow iceccd to contact the scheduler via UDP.
- Don't add icecream to PATH in the profile scripts if ccache is installed
  to avoid recursive invocations (bz #377761).

* Tue Nov 20 2007 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-4.20071101svn
- Add a SELinux policy for iceccd
- Initscripts as sources instead of patches in the .spec file
- Don't touch /var/log/iceccd in the initscript. Let iceccd create it.

* Mon Nov 12 2007 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-3.20071101svn
- Add icecc to $PATH using scripts in profile.d

* Tue Nov  6 2007 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-2.20071101svn
- Use the _datadir macro instead of hardcoded /usr/share

* Thu Nov 01 2007 Michal Schmidt <mschmidt@redhat.com> - 0.8.0-1.20071101svn
- Initial package for Fedora.
