%global __strip /bin/true

%global libsolv_version 0.7.7
%global libmodulemd_version 2.5.0
%global librepo_version 1.12.0
%global dnf_conflict 4.2.23
%global swig_version 3.0.12
%global libdnf_major_version 0
%global libdnf_minor_version 48
%global libdnf_micro_version 0

# set sphinx package name according to distro
%global requires_python2_sphinx python2-sphinx
%global requires_python3_sphinx python3-sphinx
%if 0%{?rhel} == 7
    %global requires_python2_sphinx python-sphinx
%endif
%if 0%{?suse_version}
    %global requires_python2_sphinx python2-Sphinx
    %global requires_python3_sphinx python3-Sphinx
%endif

%bcond_with valgrind

# Do not build bindings for python3 for RHEL <= 7
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

#%%if 0%%{?rhel} > 7 || 0%%{?fedora} > 29
# Disable python2 build by default
%bcond_with python2
#%%else
#%%bcond_without python2
#%%endif

%if 0%{?rhel} && ! 0%{?centos}
%bcond_without rhsm
%else
%bcond_with rhsm
%endif

%if 0%{?rhel}
%bcond_with zchunk
%else
%bcond_without zchunk
%endif

%bcond_with sanitizers

%global _cmake_opts \\\
    -DENABLE_RHSM_SUPPORT=%{?with_rhsm:ON}%{!?with_rhsm:OFF} \\\
    %{nil}

Name:           libdnf
Version:        %{libdnf_major_version}.%{libdnf_minor_version}.%{libdnf_micro_version}
Release:        1%{?dist}
Summary:        Library providing simplified C and Python API to libsolv
License:        LGPLv2+
URL:            https://github.com/rpm-software-management/libdnf
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch100:       libdnf.sgifixes.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsolv-devel >= %{libsolv_version}
BuildRequires:  pkgconfig(librepo) >= %{librepo_version}
BuildRequires:  pkgconfig(check)
%if %{with valgrind}
BuildRequires:  valgrind
%endif
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.46.0
#BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  rpm-devel >= 4.11.0
%if %{with rhsm}
BuildRequires:  pkgconfig(librhsm) >= 0.0.3
%endif
%if %{with zchunk}
BuildRequires:  pkgconfig(zck) >= 0.9.11
%endif
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
#BuildRequires:  pkgconfig(smartcols)
BuildRequires:  gettext
BuildRequires:  gpgme-devel

%if %{with sanitizers}
BuildRequires:  libasan-static
BuildRequires:  liblsan-static
BuildRequires:  libubsan-static
%endif

Requires:       libmodulemd%{?_isa} >= %{libmodulemd_version}
Requires:       libsolv%{?_isa} >= %{libsolv_version}
Requires:       librepo%{?_isa} >= %{librepo_version}

%if %{without python2}
# Obsoleted from here so we can track the fast growing version easily.
# We intentionally only obsolete and not provide, this is a broken upgrade
# prevention, not providing the removed functionality.
Obsoletes:      python2-%{name} < %{version}-%{release}
Obsoletes:      python2-hawkey < %{version}-%{release}
Obsoletes:      python2-hawkey-debuginfo < %{version}-%{release}
Obsoletes:      python2-libdnf-debuginfo < %{version}-%{release}
%endif

%description
A Library providing simplified C and Python API to libsolv.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libsolv-devel%{?_isa} >= %{libsolv_version}

%description devel
Development files for %{name}.

%if %{with python2}
%package -n python2-%{name}
%{?python_provide:%python_provide python2-%{name}}
Summary:        Python 2 bindings for the libdnf library.
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python2-devel
%if !0%{?mageia}
BuildRequires:  %{requires_python2_sphinx}
%endif
%if 0%{?rhel} == 7
BuildRequires:  swig3 >= %{swig_version}
%else
BuildRequires:  swig >= %{swig_version}
%endif

%description -n python2-%{name}
Python 2 bindings for the libdnf library.
%endif
# endif with python2

%if %{with python3}
%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary:        Python 3 bindings for the libdnf library.
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  %{requires_python3_sphinx}
BuildRequires:  swig >= %{swig_version}

%description -n python3-%{name}
Python 3 bindings for the libdnf library.
%endif

%if %{with python2}
%package -n python2-hawkey
Summary:        Python 2 bindings for the hawkey library
%{?python_provide:%python_provide python2-hawkey}
BuildRequires:  python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-nose
%else
BuildRequires:  python2-nose
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python2-%{name} = %{version}-%{release}
# Fix problem with hawkey - dnf version incompatibility
# Can be deleted for distros where only python2-dnf >= 2.0.0
Conflicts:      python2-dnf < %{dnf_conflict}
Conflicts:      python-dnf < %{dnf_conflict}

%description -n python2-hawkey
Python 2 bindings for the hawkey library.
%endif
# endif with python2

%if %{with python3}
%package -n python3-hawkey
Summary:        Python 3 bindings for the hawkey library
%{?python_provide:%python_provide python3-hawkey}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-%{name} = %{version}-%{release}
# Fix problem with hawkey - dnf version incompatibility
# Can be deleted for distros where only python3-dnf >= 2.0.0
Conflicts:      python3-dnf < %{dnf_conflict}
# Obsoletes F27 packages
Obsoletes:      platform-python-hawkey < %{version}-%{release}

%description -n python3-hawkey
Python 3 bindings for the hawkey library.
%endif

%prep
%autosetup -p1
%if %{with python2}
mkdir build-py2
%endif
%if %{with python3}
mkdir build-py3
%endif

#exit 1

# A place to generate sgug patch
#%%patch100 -p1

#exit 1

%build
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
#export CFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS -g -O0"
export CFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_FUNOPEN -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS -g -O0"
#export CFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_FUNOPEN -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
#export LDFLAGS="-ldicl-0.1"
export LDFLAGS="-ldicl-0.1 -ldiclfunopen-0.1"
#export LDFLAGS="-ldicl-0.1 -ldiclfunopen-0.1 $RPM_LD_FLAGS"
%if %{with python2}
export PREV_WD=`pwd`
cd build-py2
  %if 0%{?mageia} || 0%{?suse_version}
    cd ..
    %define _cmake_builddir build-py2
    %define __builddir build-py2
  %endif
  %cmake -DPYTHON_DESIRED:FILEPATH=%{__python2} -DWITH_MAN=OFF ../ %{!?with_zchunk:-DWITH_ZCHUNK=OFF} %{!?with_valgrind:-DDISABLE_VALGRIND=1} %{_cmake_opts} -DLIBDNF_MAJOR_VERSION=%{libdnf_major_version} -DLIBDNF_MINOR_VERSION=%{libdnf_minor_version} -DLIBDNF_MICRO_VERSION=%{libdnf_micro_version} \
    -DWITH_SANITIZERS=%{?with_sanitizers:ON}%{!?with_sanitizers:OFF} \
    -DWITH_GTKDOC=OFF
  %make_build
cd $PREV_WD
%endif
# endif with python2

%if %{with python3}
export PREV_WD=`pwd`
cd build-py3
  %if 0%{?mageia} || 0%{?suse_version}
    cd ..
    %define _cmake_builddir build-py3
    %define __builddir build-py3
  %endif
  %cmake -DPYTHON_DESIRED:FILEPATH=%{__python3} -DWITH_GIR=0 -DWITH_MAN=0 -Dgtkdoc=0 ../ %{!?with_zchunk:-DWITH_ZCHUNK=OFF} %{!?with_valgrind:-DDISABLE_VALGRIND=1} %{_cmake_opts} -DLIBDNF_MAJOR_VERSION=%{libdnf_major_version} -DLIBDNF_MINOR_VERSION=%{libdnf_minor_version} -DLIBDNF_MICRO_VERSION=%{libdnf_micro_version} \
    -DWITH_SANITIZERS=%{?with_sanitizers:ON}%{!?with_sanitizers:OFF} \
    -DWITH_GTKDOC=OFF
  %make_build
cd $PREV_WD
%endif

%check
export PREV_WD=`pwd`
%if %{with python2}
cd build-py2
  make ARGS="-V" test
cd
%endif
%if %{with python3}
# If we didn't run the general tests yet, do it now.
%if %{without python2}
cd build-py3
  make ARGS="-V" test
cd $PREV_WD
%else
# Otherwise, run just the Python tests, not all of
# them, since we have coverage of the core from the
# first build
cd build-py3/python/hawkey/tests
  make ARGS="-V" test
cd $PREV_WD
%endif
%endif

%install
export PREV_WD=`pwd`
%if %{with python2}
cd build-py2
  %make_install
cd $PREV_WD
%endif
%if %{with python3}
cd build-py3
  %make_install
cd $PREV_WD
%endif

%find_lang %{name}

#%if (0%{?rhel} && 0%{?rhel} <= 7) || 0%{?suse_version}
#%post -p /sbin/ldconfig
#%postun -p /sbin/ldconfig
#%else
#%ldconfig_scriptlets
#%endif

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS
%{_libdir}/%{name}.so.*
%dir %{_libdir}/libdnf/
%dir %{_libdir}/libdnf/plugins/
%{_libdir}/libdnf/plugins/README

%files devel
#%%doc %%{_datadir}/gtk-doc/html/%%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%if %{with python2}
%files -n python2-%{name}
%{python2_sitearch}/%{name}/
%endif

%if %{with python3}
%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%endif

%if %{with python2}
%files -n python2-hawkey
%{python2_sitearch}/hawkey/
%endif

%if %{with python3}
%files -n python3-hawkey
%{python3_sitearch}/hawkey/
%endif

%changelog
* Tue Jun 02 2020 Nicola Sella <nsella@redhat.com> - 0.48.0-1
- Update to 0.48.0
- swdb: Catch only SQLite3 exceptions and simplify the messages
- MergedTransaction list multiple comments (RhBug:1773679)
- Modify CMake to pull *.po files from weblate
- Optimize DependencyContainer creation from an existing queue
- fix a memory leak in dnf_package_get_requires()
- Fix memory leaks on g_build_filename()
- Fix memory leak in dnf_context_setup()
- Add `hy_goal_favor` and `hy_goal_disfavor`
- Define a cleanup function for `DnfPackageSet`
- dnf-repo: fix dnf_repo_get_public_keys double-free
- Do not cache RPMDB
- Use single-quotes around string literals used in SQL statements
- SQLite3: Do not close the database if it wasn't opened (RhBug:1761976)
- Don't create a new history DB connection for in-memory DB
- transaction/Swdb: Use a single logger variable in constructor
- utils: Add a safe version of pathExists()
- swdb: Handle the case when pathExists() fails on e.g. permission
- Repo: prepend "file://" if a local path is used as baseurl
- Move urlEncode() to utils
- utils: Add 'exclude' argument to urlEncode()
- Encode package URL for downloading through librepo (RhBug:1817130)
- Replace std::runtime_error with libdnf::RepoError
- Fixes and error handling improvements of the File class
- [context] Use ConfigRepo for gpgkey and baseurl (RhBug:1807864)
- [context] support "priority" option in .repo config file (RhBug:1797265)

* Wed Apr 01 2020 Ales Matej <amatej@redhat.com> - 0.47.0-1
- Update to 0.47.0
- Add prereq_ignoreinst & regular_requires properties for pkg (RhBug:1543449)
- Reset active modules when no module enabled or default (RhBug:1767351)
- Add comment option to transaction (RhBug:1773679)
- Failing to get module defauls is a recoverable error
- Baseurl is not exclusive with mirrorlist/metalink (RhBug: 1775184)
- Add new function to reset all modules in C API (dnf_context_reset_all_modules)
- [context] Fix to preserve additionalMetadata content (RhBug:1808677)
- Fix filtering of DepSolvables with source rpms (RhBug:1812596)
- Add setter for running kernel protection setting
- Handle situation when an unprivileged user cannot create history database (RhBug:1634385)
- Add query filter: latest by priority
- Add DNF_NO_PROTECTED flag to allow empty list of protected packages
- Remove 'dim' option from terminal colors to make them more readable (RhBug:1807774,1814563)
- [context] Error when main config file can't be opened (RhBug:1794864)
- [context] Add function function dnf_context_is_set_config_file_path
- Config options: only first empty value clears existing (RhBug:1788154)
- Make parsing of reldeps more strict (RhBug:1788107)
- [context] Support repositories defined in main configuration file
- Fix filtering packages by advisory when more versions and arches are available (RhBug:1770125)
- Add expanding solvable provides for dependency matching (RhBug:1534123)
- DnfRepo: fix module_hotfixes keyfile priority level
- Add custom exceptions to libdnf interface
- [conf] Set useful default colors when color is enabled
- Port to libmodulemd-2 API (RhBug:1693683)
- [context] Create new repo instead of reusing old one (RhBug:1795004)

* Thu Mar 12 2020 Stephen Gallagher <sgallagh@redhat.com> - 0.43.1-5
- Backport new API for resetting all modules

* Fri Mar 06 2020 Ales Matej <amatej@redhat.com> - 0.43.1-3
- Backport patch to reset active modules when no module enabled or default (1767351)

* Tue Feb 04 2020 Adam Williamson <adamwill@fedoraproject.org> - 0.43.1-2
- [context] Create new repo instead of reusing old one (RhBug:1795004)

* Wed Jan 15 2020 Ales Matej <amatej@redhat.com> - 0.43.1-1
- Allow excluding packages with "excludepkgs" and globs
- Add two new query filters: obsoletes_by_priority, upgrades_by_priority
- [context] Use installonly_limit from global config (RhBug:1256108)
- [context] Add API to get/set "install_weak_deps"
- [context] Add wildcard support for repo_id in dnf_context_repo_enable/disable (RhBug:1781420)
- [context] Adds support for includepkgs in repository configuration.
- [context] Adds support for excludepkgs, exclude, includepkgs, and disable_excludes in main configuration.
- [context] Added function dnf_transaction_set_dont_solve_goal
- [context] Added functions dnf_context_get/set_config_file_path
- [context] Respect "plugins" global conf value
- [context] Add API to disable/enable plugins

* Fri Nov 29 2019 Ales Matej <amatej@redhat.com> - 0.39.1-1
- Update to 0.39.1
- Report reason how package was excluded (RhBug:1649754)
- Additional Arm detection improvements (RhBug:1691430)
- Set skip_if_unavailable for media repos to skip their update (RhBug:1716067)
- Add support of xml:base for remote and local url in context (RhBug:1734350, 1717865)
- Handle NoModuleException in dnf_context_reset_modules (RhBug:1767453)
- Add missing C function hy_nevra_free() for HyNevra deallocation
- Context part of libdnf now uses metadata_expire from global configuration 

* Mon Nov 11 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.37.2-2
- Fix accidental code removal from hy_subject_get_best_solution()

* Wed Nov 06 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.37.2-1
- Update to 0.37.2
- Fix crash in PackageKit (RhBug:1636803)
- Do not create @System.solv files (RhBug:1707995)
- Set LRO_CACHEDIR so zchunk works again (RhBug:1739867)
- Don't reinstall modified packages with the same NEVRA (RhBug:1644241)
- Fix bug when moving temporary repository metadata after download (RhBug:1700341)
- Improve detection of extras packages by comparing (name, arch) pair instead of full NEVRA (RhBuh:1684517)
- Improve handling multilib packages in the history command (RhBug:1728637)
- Repo download: use full error description into the exception text (RhBug:1741442)
- Properly close hawkey.log (RhBug:1594016)
- Fix dnf updateinfo --update to not list advisories for packages updatable only from non-enabled modules
- Apply modular filtering by package name (RhBug:1702729)
- Fully enable the modular fail safe mechanism (RhBug:1616167)
- Use more descriptive message when failed to retrieve GPG key (RhBug:1605117)
- Add removeMetadataTypeFromDownload function to the API
- Context part of libdnf can now read vars (urlvars) from dirs and environment
- Throw exception immediately if file cannot be opened
- Add test when there is no primary metadata in compatible format (RhBug:1744960)
- Various improvements to countme features
- Don't abort on rpmdb checksum calculation failure
- Enable module dependency trees when using set_modules_enabled_by_pkgset() (RhBug:1762314)
- Resolve problem with --best and search in provides (RhBug:1737469)
- New method "Query::filterSubject()", replaces Solution::getBestSolution()
- The Solution class was removed
- Add query argument into get_best_query and get_best_solution
- Add module reset function into dnf_context
- Add method to get all repository metadata locations
- Catch NoModuleException in case of not existent value was used in persistor (RhBug:1761773)

* Mon Oct 21 2019 Ales Matej <amatej@gmail.com> - 0.35.3-6
- Fixes for some issues on Arm platforms (RhBug:1691430) 

* Sat Sep 14 2019 Jonathan Dieter <jdieter@gmail.com> - 0.35.3-5
- Set LRO_CACHEDIR so zchunk works again

* Wed Sep 11 2019 Jaroslav Mracek <jmracek@redhat.com> - 0.35.3-4
- Backport patch to fix reinstalling packages with a different buildtime - part II

* Tue Sep 10 2019 Jaroslav Mracek <jmracek@redhat.com> - 0.35.3-3
- Backport patch to fix reinstalling packages with a different buildtime

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.35.3-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.35.3-1
- Update to 0.35.3
- Make libdnf own its plugin directory (RhBug:1714265)
- Don't disable nonexistent but required repositories (RhBug:1689331)
- Set priority of dnf.conf.d drop-ins
- Fix toString() to not insert [] (RhBug:1584442)
- Ignore trailing blank lines in config (RhBug:1722493)
- Fix handling large number of filenames on input (RhBug:1690915)
- Detect armv7 with crypto extension only on arm version >= 8
- A new standardized User-Agent field consisting of the libdnf and OS version
  (including the variant) (RhBug:1156007)
- Add basic countme support (RhBug:1647454)

* Mon Jul 29 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.35.1-4
- Rebuilt for librepo 1.10.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.35.1-2
- Backport patch to fix attaching and detaching of libsolvRepo and
  repo_internalize_trigger() (RhBug:1727343,1727424)

* Thu Jul 04 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.35.1-1
- Update to 0.35.1
- Enhance logging handling
- Do not log DEBUG messages by default
- Also add subkeys when adding GPG keys
- [module] Fix swig binding for getModuleDependencies()
- Skip invalid key files in "/etc/pki/rpm-gpg" with warning (RhBug:1644040)
- Enable timestamp preserving for downloaded data (RhBug:1688537)
- Set default to skip_if_unavailable=false (RhBug:1679509)
- Add configuration option skip_if_unavailable (RhBug:1689931)
- Fix 'database is locked' error (RhBug:1631533)
- Replace the 'Failed to synchronize cache' message (RhBug:1712055)
- Fix 'no such table: main.trans_cmdline' error (RhBug:1596540)
- Add support of modular FailSafe (RhBug:1623128) (temporarily with warnings
  instead of errors when installing modular RPMs without modular metadata)
- Add support of DNF main config file in context; used by PackageKit and
  microdnf (RhBug:1689331)
- Exit gpg-agent after repokey import (RhBug:1650266)

* Mon Jun 10 22:13:19 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.31.0-5
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:02 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.31.0-4
- Rebuild for RPM 4.15

* Fri May 03 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.31.0-3
- Backport patches to reintroduce hawkeyRepo

* Thu Apr 25 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.31.0-1
- Update to 0.31.0
- Installroot now requires absolute path
- Support "_none_" value for repo option "proxy" (RhBug:1680272)
- Add support for Module advisories
- Add support for xml:base attribute from primary.xml (RhBug:1691315)
- Improve detection of Platform ID (RhBug:1688462)

* Wed Mar 27 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.28.1-1
- Update to 0.28.1
- Return empty query if incorrect reldep (RhBug:1687135)
- ConfigParser: Improve compatibility with Python ConfigParser and dnf-plugin-spacewalk (RhBug:1692044)
- ConfigParser: Unify default set of string represenation of boolean values
- Fix segfault when interrupting dnf process (RhBug:1610456)

* Mon Mar 11 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.28.0-1
- Update to 0.28.0
- Exclude module pkgs that have conflict
- Enhance config parser to preserve order of data, and keep comments and format
- Improve ARM detection
- Add support for SHA-384

* Tue Feb 19 2019 Jaroslav Mracek <jmracek@redhat.com> - 0.26.0-2
- Backport patches for zchunk

* Wed Feb 13 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 0.26.0-1
- Update to 0.26.0-1
- Enhance modular solver to handle enabled and default module streams differently (RhBug:1648839)
- Add support of wild cards for modules (RhBug:1644588)
- Revert commit that adds best as default behavior

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.24.1-1
- Update to 0.24.1
- Add support for zchunk
- Enhance LIBDNF plugins support
- Enhance sorting for module list (RhBug:1590358)
- [repo] Check whether metadata cache is expired (RhBug:1539620,1648274)
- [DnfRepo] Add methods for alternative repository metadata type and download (RhBug:1656314)
- Remove installed profile on module  enable or disable (RhBug:1653623)
- [sack] Implement dnf_sack_get_rpmdb_version()

* Thu Nov 22 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.3-1
- Permanently disable Python2 build for Fedora 30+
- Update to 0.22.3
- Modify solver_describe_decision to report cleaned (RhBug:1486749)
- [swdb] create persistent WAL files (RhBug:1640235)
- Relocate ModuleContainer save hook (RhBug:1632518)
- [transaction] Fix transaction item lookup for obsoleted packages (RhBug: 1642796)
- Fix memory leaks and memory allocations
- [repo] Possibility to extend downloaded repository metadata

* Wed Nov 07 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.0-8
- Backport fixes for RHBZ#1642796 from upstream master

* Tue Oct 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-7
- Rebuild for libsolv 0.7

* Tue Oct 23 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.0-6
- Add patch Relocate-ModuleContainer-save-hook-RhBug1632518
- Add patch Test-if-sack-is-present-and-run-save-module-persistor-RhBug1632518

* Sat Oct 20 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.0-5
- remove problematic patch Relocate-ModuleContainer-save-hook-RhBug1632518

* Fri Oct 19 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.0-4
- backport Relocate-ModuleContainer-save-hook-RhBug1632518

* Thu Oct 18 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.0-3
- bacport swdb-create-persistent-WAL-files-RhBug1640235

* Wed Oct 17 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.0-2
- backport Modify-solver_describe_decision-to-report-cleaned-RhBug1486749
- backport history-Fix-crash-in-TransactionItemaddReplacedBy

* Mon Oct 15 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.22.0-1
- Update to 0.22.0
- Fix segfault in repo_internalize_trigger (RhBug:1375895)
- Change sorting of installonly packages (RhBug:1627685)
- [swdb] Fixed pattern searching in history db (RhBug:1635542)
- Check correctly gpg for repomd when refresh is used (RhBug:1636743)
- [conf] Provide additional VectorString methods for compatibility with Python list.
- [plugins] add plugin loading and hooks into libdnf

* Sat Sep 29 2018 Kevin Fenzi <kevin@scrye.com> - 0.20.0-2
- Temp re-enable python2 subpackages to get rawhide composing again.

* Tue Sep 25 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.20.0-1
- [module] Report module solver errors
- [module] Enhance module commands and errors
- [transaction] Fixed several problems with SWDB
- Remove unneeded regex URL tests (RhBug:1598336)
- Allow quoted values in ini files (RhBug:1624056)
- Filter out not unique set of solver problems (RhBug:1564369)
- Disable python2 build for Fedora 30+

* Tue Sep 18 2018 Adam Williamson <awilliam@redhat.com> - 0.19.1-3
- Backport PR #585 for an update crash bug (#1629340)

* Fri Sep 14 2018 Kalev Lember <klember@redhat.com> - 0.19.1-2
- Backport a fix for a packagekit crasher / F29 Beta blocker (#1626851)

* Mon Sep 10 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.19.1-1
- Fix compilation errors on gcc-4.8.5
- [module] Allow module queries on disabled modules

* Fri Sep 07 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.19.0-1
- [query] Reldeps can contain a space char (RhBug:1612462)
- [transaction] Avoid adding duplicates via Transaction::addItem()
- Fix compilation errors on gcc-4.8.5
- [module] Make available ModuleProfile using SWIG
- [module] Redesign module disable and reset

* Mon Aug 13 2018 Daniel Mach <dmach@redhat.com> - 0.17.2-1
- [sqlite3] Change db locking mode to DEFAULT.
- [doc] Add libsmartcols-devel to devel deps.

* Mon Aug 13 2018 Daniel Mach <dmach@redhat.com> - 0.17.1-1
- [module] Solve a problem in python constructor of NSVCAP if no version.
- [translations] Update translations from zanata.
- [transaction] Fix crash after using dnf.comps.CompsQuery and forking the process in Anaconda.
- [module] Support for resetting module state.
- [output] Introduce wrapper for smartcols.

* Fri Aug 10 2018 Adam Williamson <awilliam@redhat.com> - 0.17.0-2
- Backport fix that prevented anaconda running dnf in a subprocess (#546)

* Tue Aug 07 2018 Daniel Mach <dmach@redhat.com> - 0.17.0-1
- [conf] Add module_platform_id option.
- [module] Add ModulePackageContainer class.
- [module] Add ModulePersistor class.
- [sack] Module filtering made available in python API
- [sack] Module auto-enabling according to installed packages

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.1-3
- Rebuild for new binutils

* Fri Jul 27 2018 Daniel Mach <dmach@redhat.com> - 0.16.1-2
- [module] Implement 'module_hotfixes' conf option to skip filtering RPMs from hotfix repos.
- [goal] Fix distupgrade filter, allow downgrades.
- [context] Allow to set module platform in context.
- [module] Introduce proper modular dependency solving.
- [module] Platform pseudo-module based on /etc/os-release.
- [goal] Add Goal::listSuggested().
- [l10n] Support for translations, add gettext build dependency.

* Sun Jul 22 2018 Daniel Mach <dmach@redhat.com> - 0.16.0-1
- Fix RHSM plugin
- Add support for logging
- Bump minimal libmodulemd version to 1.6.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.15.2-1
- Update to 0.15.1
- Resolves: rhbz#1595487

* Fri Jun 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.1-2
- Restore proper ldconfig_scriptlets

* Tue Jun 26 2018 Jaroslav Mracek <jmracek@redhat.com> - 0.15.1-1
- Update to 0.15.1

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.11.1-4
- Switch to %%ldconfig_scriptlets

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.1-3
- Use better Obsoletes for platform-python

* Fri Nov 03 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.11.1-2
- Remove platform-python subpackage

* Mon Oct 16 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.11.1-1
- Rerelease of 0.11.1-1
- Improvement query performance
- Run file query in hy_subject_get_best_solution only for files (arguments that start with ``/`` or
  ``*/``)
- Resolves: rhbz#1498207 - DNF crash during upgrade installation F26 -> F27

* Tue Oct 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Mon Oct 02 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.10.1-2
- Rerelease of 0.10.1-1

* Wed Sep 27 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.10.1-1
- Update to 0.10.1
- It improves query performance with name and arch filters. Also nevra filter will now
  handle string with or without epoch.
- Additionally for python bindings it renames NEVRA._has_just_name() to NEVRA.has_just_name() due
  to movement of code into c part of library.
- Resolves: rhbz#1260242 - --exclude does not affect dnf remove's removal of requirements
- Resolves: rhbz#1485881 - DNF claims it cannot install package, which have been already installed
- Resolves: rhbz#1361187 - [abrt] python-ipython-console: filter_updown(): python3.5 killed by SIGABRT

* Fri Sep 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.3-8
- Disable platform python on old releases

* Tue Aug 15 2017 Lumír Balhar <lbalhar@redhat.com> - 0.9.3-7
- Add platform-python subpackage

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.3-6
- Rebuilt after RPM update (№ 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.3-5
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.3-4
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.9.3-1
- Update to 0.9.3

* Sat Jul 01 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Mon Jun 12 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Mon May 22 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Tue May 02 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Fri Mar 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Tue Mar 21 2017 Jaroslav Mracek <jmracek@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Mon Feb 20 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.4-1
- Update to 0.7.4

* Fri Feb 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.3-1
- Update to 0.7.3

* Wed Feb 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.2-1
- 0.7.2

* Fri Jan 06 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.1-1
- 0.7.1

* Wed Dec 21 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.0-0.7gitf9b798c
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.0-0.6gitf9b798c
- Use new upstream URL

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.7.0-0.5gitf9b798c
- Rebuild for Python 3.6

* Tue Dec 06 2016 Martin Hatina <mhatina@redhat.com> - 0.7.0-0.4gitf9b798c
- Increase conflict version of dnf

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.0-0.3gitf9b798c
- Update to latest snapshot

* Fri Nov 04 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.7.0-0.2git8bd77f8
- Update to latest snapshot

* Thu Sep 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.7.0-0.1git179c0a6
- Initial package
