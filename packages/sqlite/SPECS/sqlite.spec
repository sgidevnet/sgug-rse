# bcond default logic is nicely backwards...
%bcond_without tcl
%bcond_with static
%bcond_without check

%define realver 3290000
%define docver 3290000
%define rpmver 3.29.0

Summary: Library that implements an embeddable SQL database engine
Name: sqlite
Version: %{rpmver}
Release: 2%{?dist}
License: Public Domain
URL: http://www.sqlite.org/

Source0: http://www.sqlite.org/2019/sqlite-src-%{realver}.zip
Source1: http://www.sqlite.org/2019/sqlite-doc-%{docver}.zip
Source2: http://www.sqlite.org/2019/sqlite-autoconf-%{realver}.tar.gz
# Support a system-wide lemon template
Patch1: sqlite-3.6.23-lemon-system-template.patch
# sqlite >= 3.7.10 is buggy if malloc_usable_size() is detected, disable it:
# https://bugzilla.redhat.com/show_bug.cgi?id=801981
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=665363
Patch3: sqlite-3.12.2-no-malloc-usable-size.patch
# Temporary workaround for failed percentile test, see patch for details
Patch4: sqlite-3.8.0-percentile-test.patch
# Disable test date-2.2c on i686
Patch7: sqlite-3.16-datetest-2.2c.patch
# Modify sync2.test to pass with DIRSYNC turned off
Patch8: sqlite-3.18.0-sync2-dirsync.patch

Patch10: sqlite3.sgifixes.patch

#BuildRequires:  gcc
#BuildRequires: ncurses-devel readline-devel glibc-devel
#BuildRequires: autoconf
%if %{with tcl}
#BuildRequires: /usr/bin/tclsh
#BuildRequires: tcl-devel
%{!?tcl_version: %global tcl_version 8.6}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%endif

Requires: %{name}-libs = %{version}-%{release}

# Ensure updates from pre-split work on multi-lib systems
Obsoletes: %{name} < 3.11.0-1
Conflicts: %{name} < 3.11.0-1

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

%package devel
Summary: Development tools for the sqlite3 embeddable SQL database engine
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files and development documentation 
for %{name}. If you like to develop programs using %{name}, you will need 
to install %{name}-devel.

%package libs
Summary: Shared library for the sqlite3 embeddable SQL database engine.

# Ensure updates from pre-split work on multi-lib systems
Obsoletes: %{name} < 3.11.0-1
Conflicts: %{name} < 3.11.0-1

%description libs
This package contains the shared library for %{name}.

%package doc
Summary: Documentation for sqlite
BuildArch: noarch

%description doc
This package contains most of the static HTML files that comprise the
www.sqlite.org website, including all of the SQL Syntax and the 
C/C++ interface specs and other miscellaneous documentation.

%package -n lemon
Summary: A parser generator

%description -n lemon
Lemon is an LALR(1) parser generator for C or C++. It does the same
job as bison and yacc. But lemon is not another bison or yacc
clone. It uses a different grammar syntax which is designed to reduce
the number of coding errors. Lemon also uses a more sophisticated
parsing engine that is faster than yacc and bison and which is both
reentrant and thread-safe. Furthermore, Lemon implements features
that can be used to eliminate resource leaks, making is suitable for
use in long-running programs such as graphical user interfaces or
embedded controllers.

%if %{with tcl}
%package tcl
Summary: Tcl module for the sqlite3 embeddable SQL database engine
Requires: %{name} = %{version}-%{release}
Requires: tcl(abi) = %{tcl_version}

%description tcl
This package contains the tcl modules for %{name}.

%package analyzer
Summary: An analysis program for sqlite3 database files
Requires: %{name} = %{version}-%{release}
Requires: tcl(abi) = %{tcl_version}

%description analyzer
This package contains the analysis program for %{name}.
%endif

%prep
%setup -q -a1 -n %{name}-src-%{realver}
%patch1 -p1
%patch3 -p1
%patch4 -p1
%ifarch %{ix86}
%patch7 -p1
%endif
%patch8 -p1
%patch10 -p1

# Remove backup-file
rm -f %{name}-doc-%{docver}/sqlite.css~ || :

autoconf # Rerun with new autoconf to add support for aarm64

%build
export CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS -DSQLITE_ENABLE_COLUMN_METADATA=1 \
               -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3 \
               -DSQLITE_ENABLE_RTREE=1 -DSQLITE_SECURE_DELETE=1 \
               -DSQLITE_ENABLE_UNLOCK_NOTIFY=1 -DSQLITE_ENABLE_DBSTAT_VTAB=1 \
               -DSQLITE_ENABLE_FTS3_PARENTHESIS=1 -DSQLITE_ENABLE_JSON1=1 \
               -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS \
               -Wall -fno-strict-aliasing"
%configure %{!?with_tcl:--disable-tcl} \
           --enable-fts5 \
           --enable-threadsafe \
           --enable-threads-override-locks \
           --enable-load-extension \
           %{?with_tcl:TCLLIBDIR=%{tcl_sitearch}/sqlite3}

# rpath removal
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

# Build sqlite3_analyzer
# depends on tcl
%if %{with tcl}
make %{?_smp_mflags} sqlite3_analyzer
%endif

%install
make DESTDIR=${RPM_BUILD_ROOT} install

install -D -m0644 sqlite3.1 $RPM_BUILD_ROOT/%{_mandir}/man1/sqlite3.1
install -D -m0755 lemon $RPM_BUILD_ROOT/%{_bindir}/lemon
install -D -m0644 tool/lempar.c $RPM_BUILD_ROOT/%{_datadir}/lemon/lempar.c

%if %{with tcl}
# fix up permissions to enable dep extraction
chmod 0755 ${RPM_BUILD_ROOT}/%{tcl_sitearch}/sqlite3/*.so
# Install sqlite3_analyzer
install -D -m0755 sqlite3_analyzer $RPM_BUILD_ROOT/%{_bindir}/sqlite3_analyzer
%endif

%if ! %{with static}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.{la,a}
%endif

%if %{with check}
%check
# XXX shell tests are broken due to loading system libsqlite3, work around...
export LD_LIBRARY_PATH=`pwd`/.libs
export MALLOC_CHECK_=3

# csv01 hangs on all non-intel archs i've tried
%ifarch x86_64 %{ix86}
%else
rm test/csv01.test
%endif

%ifarch s390x ppc64
rm test/fts3conf.test
%endif

make test
%endif # with check

#%ldconfig_scriptlets libs

%files
%{_bindir}/sqlite3
%{_mandir}/man?/*

%files libs
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if %{with static}
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%endif

%files doc
%doc %{name}-doc-%{docver}/*

%files -n lemon
%{_bindir}/lemon
%{_datadir}/lemon

%if %{with tcl}
%files tcl
%{tcl_sitearch}/sqlite3

%files analyzer
%{_bindir}/sqlite3_analyzer
%endif

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Petr Kubat <pkubat@redhat.com> - 3.29.0-1
- Updated to version 3.29.0 (https://sqlite.org/releaselog/3_29_0.html)
- Remove stupid-openfiles-test patch as the upstream test should now
  work properly even on systems with larger number of file descriptors
  Related: https://sqlite.org/src/info/a27b0b880d76c683

* Mon May 13 2019 Petr Kubat <pkubat@redhat.com> - 3.28.0-1
- Updated to version 3.28.0 (https://sqlite.org/releaselog/3_28_0.html)

* Thu Feb 28 2019 Petr Kubat <pkubat@redhat.com> - 3.27.2-1
- Updated to version 3.27.2 (https://sqlite.org/releaselog/3_27_2.html)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-3
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Petr Kubat <pkubat@redhat.com> - 3.26.0-1
- Updated to version 3.26.0 (https://sqlite.org/releaselog/3_26_0.html)

* Thu Oct 11 2018 Petr Kubat <pkubat@redhat.com> - 3.25.2-1
- Updated to version 3.25.2 (https://sqlite.org/releaselog/3_25_2.html)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Petr Kubat <pkubat@redhat.com> - 3.24.0-1
- Updated to version 3.24.0 (https://sqlite.org/releaselog/3_24_0.html)

* Wed Apr 11 2018 Petr Kubat <pkubat@redhat.com> - 3.23.1-1
- Updated to version 3.23.1 (https://sqlite.org/releaselog/3_23_1.html)

* Tue Apr 03 2018 Petr Kubat <pkubat@redhat.com> - 3.23.0-1
- Updated to version 3.23.0 (https://sqlite.org/releaselog/3_23_0.html)

* Wed Mar 21 2018 Petr Kubat <pkubat@redhat.com> - 3.22.0-4
- Fixed CVE-2018-8740 (#1558809)

* Fri Feb  9 2018 Florian Weimer <fweimer@redhat.com> - 3.22.0-3
- Use LDFLAGS from redhat-rpm-config for building lemon, too

* Mon Feb 05 2018 Petr Kubat <pkubat@redhat.com> - 3.22.0-2
- Fixed issue with some walro2 tests failing on ppc64

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.22.0-2
- Switch to %%ldconfig_scriptlets

* Thu Jan 25 2018 Petr Kubat <pkubat@redhat.com> - 3.22.0-1
- Fixed issue with some e_expr tests failing i686
- Fixed issue with a fts3rank test failing on big-endian systems

* Tue Jan 23 2018 Petr Kubat <pkubat@redhat.com> - 3.22.0-1
- Updated to version 3.22.0 (https://sqlite.org/releaselog/3_22_0.html)

* Wed Nov 01 2017 Petr Kubat <pkubat@redhat.com> - 3.21.0-1
- Updated to version 3.21.0 (https://sqlite.org/releaselog/3_21_0.html)

* Mon Aug 28 2017 Petr Kubat <pkubat@redhat.com> - 3.20.1-1
- Updated to version 3.20.1 (https://sqlite.org/releaselog/3_20_1.html)

* Tue Aug 22 2017 Kalev Lember <klember@redhat.com> - 3.20.0-2
- Build with --enable-fts5

* Wed Aug 02 2017 Petr Kubat <pkubat@redhat.com> - 3.20.0-1
- Updated to version 3.20.0 (https://sqlite.org/releaselog/3_20_0.html)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Petr Kubat <pkubat@redhat.com> - 3.19.3-1
- Updated to version 3.19.3 (https://sqlite.org/releaselog/3_19_3.html)
- Better detection of CVE-2017-10989 (#1469673)

* Thu May 25 2017 Petr Kubat <pkubat@redhat.com> - 3.19.1-1
- Updated to version 3.19.1 (https://sqlite.org/releaselog/3_19_1.html)

* Mon Apr 03 2017 Petr Kubat <pkubat@redhat.com> - 3.18.0-1
- Updated to version 3.18.0 (https://sqlite.org/releaselog/3_18_0.html)
- Modify sync2.test to pass with DIRSYNC turned off

* Thu Mar 02 2017 Petr Kubat <pkubat@redhat.com> - 3.17.0-2
- Rebuild using newest gcc (#1428286)

* Tue Feb 21 2017 Petr Kubat <pkubat@redhat.com> - 3.17.0-1
- Updated to version 3.17.0 (https://sqlite.org/releaselog/3_17_0.html)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.16.2-2
- Rebuild for readline 7.x

* Sat Jan  7 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 3.16.2-1
- Updated to version 3.16.2 (https://sqlite.org/releaselog/3_16_2.html)

* Wed Jan  4 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 3.16.1-1
- Updated to version 3.16.1 (https://sqlite.org/releaselog/3_16_1.html)

* Tue Jan  3 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 3.16.0-1
- Updated to version 3.16.0 (https://sqlite.org/releaselog/3_16_0.html)

* Wed Sep 21 2016 Jakub Dorňák <jdornak@redhat.com> - 3.14.2-1
- Updated to version 3.14.2 (https://sqlite.org/releaselog/3_14_2.html)

* Mon Aug 15 2016 Jakub Dorňák <jdornak@redhat.com> - 3.14.1-1
- Updated to version 3.14.1 (https://sqlite.org/releaselog/3_14_1.html)

* Tue May 24 2016 Jakub Dorňák <jdornak@redhat.com> - 3.13.0-1
- Updated to version 3.13.0 (https://sqlite.org/releaselog/3_13_0.html)

* Mon Apr 25 2016 Jakub Dorňák <jdornak@redhat.com> - 3.12.2-1
- Updated to version 3.12.2 (https://sqlite.org/releaselog/3_12_2.html)

* Wed Mar 02 2016 Jan Stanek <jstanek@redhat.com> - 3.11.0-3
- Release bump for #1312506

* Tue Feb 23 2016 Nils Philippsen <nils@redhat.com> - 3.11.0-2
- add obsoletes/conflicts to make updates on multi-lib systems work (#1310441)
- make -devel package depend on arch-specific -libs (not main) package

* Wed Feb 17 2016 Jan Stanek <jstanek@redhat.com> - 3.11.0-1
- Updated to version 3.11.0 (https://sqlite.org/releaselog/3_11_0.html)

* Mon Feb 08 2016 Jan Stanek <jstanek@redhat.com> - 3.10.2-3
- Split the shared libraries to standalone subpackage

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Jan Stanek <jstanek@redhat.com> - 3.10.2-1
- Updated to version 3.10.2 (http://sqlite.org/releaselog/3_10_2.html)
- Enabled JSON1 Extension (rhbz#1277387)
- Made test failure nonfatal on MIPS (rhbz#1294888)

* Wed Jan 13 2016 Jan Stanek <jstanek@redhat.com> - 3.10.0-1
- Updated to version 3.10.0 (http://sqlite.org/releaselog/3_10_0.html)

* Mon Dec 21 2015 Jan Stanek <jstanek@redhat.com> - 3.9.2-1
- Updated to version 3.9.2 (http://sqlite.org/releaselog/3_9_2.html)

* Thu Dec 10 2015 Jan Stanek <jstanek@redhat.com> - 3.9.0-2
- Add autoconf amalgamation for stage2 builds.

* Thu Oct 15 2015 Jan Stanek <jstanek@redhat.com> - 3.9.0-1
- Updated to version 3.9.0 (https://sqlite.org/releaselog/3_9_0.html)

* Tue Sep 22 2015 Jan Stanek <jstanek@redhat.com> - 3.8.11.1-1
- Updated to version 3.8.11.1

* Tue Jul 28 2015 Jan Stanek <jstanek@redhat.com> - 3.8.11-1
- Updated to version 3.8.11 (https://sqlite.org/releaselog/3_8_11.html)

* Fri Jun 19 2015 Jan Stanek <jstanek@redhat.com> - 3.8.10.2-3
- Enabled SQLITE_ENABLE_FTS3_PARENTHESIS extension (rhbz#1232301)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Jan Stanek <jstanek@redhat.com> - 3.8.10.2-1
- Updated to version 3.8.10.2 (https://sqlite.org/releaselog/3_8_10_2.html)

* Mon May 18 2015 Jan Stanek <jstanek@redhat.com> - 3.8.10.1-1
- Updated to version 3.8.10.1 (https://www.sqlite.org/releaselog/3_8_10_1.html)

* Tue Apr 14 2015 Jan Stanek <jstanek@redhat.com> - 3.8.9-1
- Updated to version 3.8.9 (https://www.sqlite.org/releaselog/3_8_9.html)

* Thu Feb 26 2015 Jan Stanek <jstanek@redhat.com> - 3.8.8.3-1
- Updated to version 3.8.8.3 (https://sqlite.org/releaselog/3_8_8_3.html)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 3.8.8-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Tue Feb 03 2015 Jan Stanek <jstanek@redhat.com> - 3.8.8-2
- Fixed out-of-date source URLs (rhbz#1188092)

* Tue Jan 20 2015 Jan Stanek <jstanek@redhat.com> - 3.8.8-1
- Updated to version 3.8.8 (https://sqlite.org/releaselog/3_8_8.html)
- Recreated patches to work on current version.

* Fri Dec 12 2014 Jan Stanek <jstanek@redhat.com> - 3.8.7.4-1
- Updated to version 3.8.7.4 (http://www.sqlite.org/releaselog/3_8_7_4.html)

* Tue Nov 25 2014 Jan Stanek <jstanek@redhat.com> - 3.8.7.2-1
- Updated to version 3.8.7.2 (http://sqlite.org/releaselog/3_8_7_2.html)

* Tue Oct 21 2014 Jan Stanek <jstanek@redhat.com> - 3.8.7-1
- Updated to version 3.8.7 (http://sqlite.org/releaselog/3_8_7.html)
- Dropped patch for problem fixed upstream

* Tue Aug 19 2014 Jan Stanek <jstanek@redhat.com> - 3.8.6-2
- Added auto-selection of Tcl version based on Fedora version

* Tue Aug 19 2014 Jan Stanek <jstanek@redhat.com> - 3.8.6-1
- Updated to version 3.8.6 (http://www.sqlite.org/releaselog/3_8_6.html)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.8.5-2
- Re-enable tests on aarch64 now they pass again

* Tue Jun 10 2014 Jan Stanek <jstanek@redhat.com> - 3.8.5-1
- Update to version 3.8.5 (http://www.sqlite.org/releaselog/3_8_5.html)
- Dropped patch already included upstream

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.8.4.3-4
- Don't make tests fail the build on aarch64 like some of the other arches

* Wed May 28 2014 Jan Stanek <jstanek@redhat.com> - 3.8.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86 with correct tcl_version

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue Apr 29 2014 Jan Stanek <jstanek@redhat.com> - 3.8.4.3-1
- Update to version 3.8.4.3 (http://www.sqlite.org/releaselog/3_8_4_3.html)
- Changed patch for rhbz#1075889 to upstream version
  Related: #1075889

* Fri Apr 25 2014 Honza Horak <hhorak@redhat.com> - 3.8.4.2-3
- Revert part of the upstream commit dca1945aeb3fb005, since it causes
  nautilus to crash
  Related: #1075889

* Wed Apr 02 2014 Jan Stanek <jstanek@redhat.com> 3.8.4.2-2
- Added building and shipping of sqlite3_analyzer (#1007159)

* Fri Mar 28 2014 Jan Stanek <jstanek@redhat.com> 3.8.4.2-1
- Update to 3.8.4 (http://www.sqlite.org/releaselog/3_8_4_2.html)

* Tue Mar 11 2014 Jan Stanek <jstanek@redhat.com> 3.8.4-1
- Update to 3.8.4 (http://www.sqlite.org/releaselog/3_8_4.html)

* Sun Feb 23 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.8.3-2
- Re-enable check on ARM/aarch64 as failing test fixed upstream for non x86 arches
- Modernise spec

* Tue Feb 11 2014 Jan Stanek <jstanek@redhat.com> 3.8.3-1
- Update to 3.8.3 (http://www.sqlite.org/releaselog/3_8_3.html)
- Dropped man-page patch - included upstream

* Mon Jan  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.8.2-2
- Add aarch64 to all the other arch excludes for tests

* Tue Dec 10 2013 Jan Stanek <jstanek@redhat.com> - 3.8.2-1
- Update to 3.8.2 (http://www.sqlite.org/releaselog/3_8_2.html)

* Tue Nov 26 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.8.1-2
- Do not use transitive WHERE-clause constraints on LEFT JOINs (#1034714)

* Tue Oct 22 2013 Jan Stanek <jstanek@redhat.com> - 3.8.1-1
- Update to 3.8.1 (http://www.sqlite.org/releaselog/3_8_1.html)

* Thu Sep 26 2013 Jan Stanek <jstanek@redhat.com> - 3.8.0.2-4
- Removed fullversioned provides and start using full version for rpm version

* Mon Sep 23 2013 Jan Stanek <jstanek@redhat.com> - 3.8.0-3
- Added fullversioned Provides to fix broken dependency

* Mon Sep 16 2013 Jan Stanek <jstanek@redhat.com> - 3.8.0-2
- Dropped problematic percentile-2.1.50 test

* Thu Sep 05 2013 Jan Stanek <jstanek@redhat.com> - 3.8.0-1
- Update to 3.8.0.2 (http://sqlite.org/releaselog/3_8_0_2.html)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Jan Stanek <jstanek@redhat.com> - 3.7.17-1
- Update to 3.7.17 (http://www.sqlite.org/releaselog/3_7_17.html)

* Thu May 16 2013 Jan Stanek <jstanek@redhat.com> - 3.7.16.2-2
- Added missing options to man page (#948862)

* Mon Apr 29 2013 Jan Stanek <jstanek@redhat.com> - 3.7.16.2-1
- update to 3.7.16.2 (http://www.sqlite.org/releaselog/3_7_16_2.html)
- add support for aarch64 (rerunning autoconf) (#926568)

* Sun Mar 31 2013 Panu Matilainen <pmatilai@redhat.com> - 3.7.16.1-1
- update to 3.7.16.1 (https://www.sqlite.org/releaselog/3_7_16_1.html)

* Wed Mar 20 2013 Panu Matilainen <pmatilai@redhat.com> - 3.7.16-1
- update to 3.7.16 (http://www.sqlite.org/releaselog/3_7_16.html)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Panu Matilainen <pmatilai@redhat.com> - 3.7.15.2-1
- update to 3.7.15.2 (http://www.sqlite.org/releaselog/3_7_15_2.html)

* Thu Dec 13 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.15-1
- update to 3.7.15 (http://www.sqlite.org/releaselog/3_7_15.html)
- fix an old incorrect date in spec changelog

* Tue Nov 06 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.14.1-1
- update to 3.7.14.1 (http://www.sqlite.org/releaselog/3_7_14_1.html)

* Wed Oct 03 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.14-1
- update to 3.7.14 (http://www.sqlite.org/releaselog/3_7_14.html)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.13-1
- update to 3.7.13 (http://www.sqlite.org/releaselog/3_7_13.html)
- drop no longer needed savepoint relase patch

* Fri Jun 01 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.11-3
- don't abort pending queries on release of nested savepoint (#821642)

* Wed Apr 25 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.11-2
- run test-suite with MALLOC_CHECK_=3
- disable buggy malloc_usable_size code (#801981)

* Mon Mar 26 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.11-1
- update to 3.7.11 (http://www.sqlite.org/releaselog/3_7_11.html)

* Wed Mar 07 2012 Panu Matilainen <pmatilai@redhat.com> - 3.7.10-1
- update to 3.7.10 (http://www.sqlite.org/releaselog/3_7_10.html)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.9-1
- update to 3.7.9 (http://www.sqlite.org/releaselog/3_7_9.html)

* Fri Oct 28 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.8-1
- update to 3.7.8 (http://www.sqlite.org/releaselog/3_7_8.html)

* Wed Jul 13 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.7.1-1
- update to 3.7.7.1 (http://www.sqlite.org/releaselog/3_7_7_1.html)
- autoconf no longer needed for build, libdl check finally upstreamed

* Wed May 25 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.6.3-1
- update to 3.7.6.3 (http://www.sqlite.org/releaselog/3_7_6_3.html)

* Sat May 21 2011 Peter Robinson <pbrobinson@gmail.com> - 3.7.6.2-3
- add arm to the exclude from tests list

* Fri Apr 29 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.6.2-2
- comment out stupid tests causing very bogus build failure on koji

* Thu Apr 21 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.6.2-1
- update to 3.7.6.2 (http://www.sqlite.org/releaselog/3_7_6_2.html)

* Fri Feb 25 2011 Dennis Gilmore <dennis@ausil.us> - 3.7.5-4
- build tests on sparc expecting failures same as the other big endian arches

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 2 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.5-2
- unwanted cgi-script in docs creating broken dependencies, remove it
- make doc sub-package noarch

* Tue Feb 1 2011 Panu Matilainen <pmatilai@redhat.com> - 3.7.5-1
- update to 3.7.5 (http://www.sqlite.org/releaselog/3_7_5.html)

* Thu Dec 9 2010 Panu Matilainen <pmatilai@redhat.com> - 3.7.4-1
- update to 3.7.4 (http://www.sqlite.org/releaselog/3_7_4.html)
- deal with upstream source naming, versioning and format changing
- fixup wal2-test expections wrt SQLITE_DISABLE_DIRSYNC use

* Fri Nov 5 2010 Dan Horák <dan[at]danny.cz> - 3.7.3-2
- expect test failures also on s390x

* Mon Nov 1 2010 Panu Matilainen <pmatilai@redhat.com> - 3.7.3-1
- update to 3.7.3 (http://www.sqlite.org/releaselog/3_7_3.html)

* Thu Sep  2 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 3.7.0.1-2
- enable SQLITE_SECURE_DELETE, SQLITE_ENABLE_UNLOCK_NOTIFY for firefox 4

* Fri Aug 13 2010 Panu Matilainen <pmatilai@redhat.com> - 3.7.0.1-1
- update to 3.7.0.1 (http://www.sqlite.org/releaselog/3_7_0_1.html)

* Sat Jul  3 2010 Dan Horák <dan[at]danny.cz> - 3.6.23.1-2
- some tests are failing on s390 and ppc/ppc64 so don't fail the whole build there

* Mon Apr 19 2010 Panu Matilainen <pmatilai@redhat.com> - 3.6.23.1-1
- update to 3.6.23.1 (http://www.sqlite.org/releaselog/3_6_23_1.html)

* Wed Mar 10 2010 Panu Matilainen <pmatilai@redhat.com> - 3.6.23-1
- update to 3.6.23 (http://www.sqlite.org/releaselog/3_6_23.html)
- drop the lemon sprintf patch, upstream doesn't want it
- make test-suite errors fail build finally

* Mon Jan 18 2010 Panu Matilainen <pmatilai@redhat.com> - 3.6.22-1
- update to 3.6.22 (http://www.sqlite.org/releaselog/3_6_22.html)

* Tue Dec 08 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.21-1
- update to 3.6.21 (http://www.sqlite.org/releaselog/3_6_21.html)

* Tue Nov 17 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.20-1
- update to 3.6.20 (http://www.sqlite.org/releaselog/3_6_20.html)

* Tue Oct 06 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.18-1
- update to 3.6.18 (http://www.sqlite.org/releaselog/3_6_18.html)
- drop no longer needed test-disabler patches

* Fri Aug 21 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.17-1
- update to 3.6.17 (http://www.sqlite.org/releaselog/3_6_17.html)
- disable to failing tests until upstream fixes

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.14.2-1
- update to 3.6.14.2 (#505229)

* Mon May 18 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.14-2
- disable rpath
- add -doc subpackage instead of patching out reference to it

* Thu May 14 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.14-1
- update to 3.6.14 (http://www.sqlite.org/releaselog/3_6_14.html)
- merge-review cosmetics (#226429)
  - drop ancient sqlite3 obsoletes
  - fix tab vs space whitespace issues
  - remove commas from summaries
- fixup io-test fsync expectations wrt SQLITE_DISABLE_DIRSYNC

* Wed Apr 15 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.13-1
- update to 3.6.13

* Thu Apr 09 2009 Dennis Gilmore <dennis@ausil.us> - 3.6.12-3
- apply upstream patch for memory alignment issue (#494906)

* Tue Apr 07 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.12-2
- disable strict aliasing to work around brokenness on 3.6.12 (#494266)
- run test-suite on build but let it fail for now

* Fri Apr 03 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.12-1
- update to 3.6.12 (#492662)
- remove reference to non-existent sqlite-doc from manual (#488883)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.10-3
- enable RTREE and FTS3 extensions (#481417)

* Thu Jan 22 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.10-2
- upstream fix yum breakage caused by new keywords (#481189)

* Thu Jan 22 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.10-1
- update to 3.6.10

* Wed Dec 31 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.7-1
- update to 3.6.7
- avoid lemon ending up in main sqlite package too

* Fri Dec 05 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.6.2-4
- add lemon subpackage

* Thu Dec  4 2008 Matthias Clasen <mclasen@redhat.com> - 3.6.6.2-3
- Rebuild for pkg-config provides 

* Tue Dec 02 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.6.2-2
- require tcl(abi) in sqlite-tcl subpackage (#474034)
- move tcl extensions to arch-specific location
- enable dependency extraction on the tcl dso
- require pkgconfig in sqlite-devel

* Sat Nov 29 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.6.2-1
- update to 3.6.6.2

* Sat Nov 08 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.4-1
- update to 3.6.4
- drop patches already upstream

* Mon Sep 22 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.9-2
- Remove references to temporary registers from cache on release (#463061)
- Enable loading of external extensions (#457433)

* Tue Jun 17 2008 Stepan Kasal <skasal@redhat.com> - 3.5.9-1
- update to 3.5.9

* Wed Apr 23 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.8-1
- update to 3.5.8
- provide full version in pkg-config (#443692)

* Mon Mar 31 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.6-2
- remove reference to static libs from -devel description (#439376)

* Tue Feb 12 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.6-1
- update to 3.5.6
- also fixes #432447

* Fri Jan 25 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.4-3
- enable column metadata API (#430258)

* Tue Jan 08 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.4-2
- avoid packaging CVS directory as documentation (#427755)

* Fri Dec 21 2007 Panu Matilainen <pmatilai@redhat.com> - 3.5.4-1
- Update to 3.5.4 (#413801)

* Fri Sep 28 2007 Panu Matilainen <pmatilai@redhat.com> - 3.4.2-3
- Add another build conditional for enabling %%check

* Fri Sep 28 2007 Panu Matilainen <pmatilai@redhat.com> - 3.4.2-2
- Use bconds for the spec build conditionals
- Enable -tcl subpackage again (#309041)

* Wed Aug 15 2007 Paul Nasrat <pnasrat@redhat.com> - 3.4.2-1
- Update to 3.4.2

* Sat Jul 21 2007 Paul Nasrat <pnasrat@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Sun Jun 24 2007 Paul Nasrat <pnsarat@redhat.com> - 3.4.0-2
- Disable load for now (#245486)

* Tue Jun 19 2007 Paul Nasrat <pnasrat@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Fri Jun 01 2007 Paul Nasrat <pnasrat@redhat.com> - 3.3.17-2
- Enable load 
- Build fts1 and fts2
- Don't sync on dirs (#237427)

* Tue May 29 2007 Paul Nasrat <pnasrat@redhat.com> - 3.3.17-1
- Update to 3.3.17

* Mon Mar 19 2007 Paul Nasrat <pnasrat@redhat.com> - 3.3.13-1
- Update to 3.3.13

* Fri Aug 11 2006 Paul Nasrat <pnasrat@redhat.com> - 3.3.6-2
- Fix conditional typo (patch from Gareth Armstrong)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.3.6-1.1
- rebuild

* Mon Jun 26 2006 Paul Nasrat <pnasrat@redhat.com> - 3.3.6-1
- Update to 3.3.6
- Fix typo  (#189647)
- Enable threading fixes (#181298)
- Conditionalize static library

* Mon Apr 17 2006 Paul Nasrat <pnasrat@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.3.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.3.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Tue Jan 24 2006 Paul Nasrat <pnasrat@redhat.com> - 3.2.8-1
- Add --enable-threadsafe (Nicholas Miell)
- Update to 3.2.8

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Oct  4 2005 Jeremy Katz <katzj@redhat.com> - 3.2.7-2
- no more static file or libtool archive (#169874) 

* Wed Sep 28 2005 Florian La Roche <laroche@redhat.com>
- Upgrade to 3.2.7 release.

* Thu Sep 22 2005 Florian La Roche <laroche@redhat.com>
- Upgrade to 3.2.6 release.

* Sun Sep 11 2005 Florian La Roche <laroche@redhat.com>
- Upgrade to 3.2.5 release.

* Fri Jul  8 2005 Roland McGrath <roland@redhat.com> - 3.2.2-1
- Upgrade to 3.2.2 release.

* Sat Apr  9 2005 Warren Togami <wtogami@redhat.com> - 3.1.2-3
- fix buildreqs (#154298)

* Mon Apr  4 2005 Jeremy Katz <katzj@redhat.com> - 3.1.2-2
- disable tcl subpackage

* Wed Mar  9 2005 Jeff Johnson <jbj@redhat.com> 3.1.2-1
- rename to "sqlite" from "sqlite3" (#149719, #150012).

* Wed Feb 16 2005 Jeff Johnson <jbj@jbj.org> 3.1.2-1
- upgrade to 3.1.2.
- add sqlite3-tcl sub-package.

* Sat Feb  5 2005 Jeff Johnson <jbj@jbj.org> 3.0.8-3
- repackage for fc4.

* Mon Jan 17 2005 R P Herrold <info@owlriver.com> 3.0.8-2orc
- fix a man page nameing conflict when co-installed with sqlite-2, as
  is permissible
