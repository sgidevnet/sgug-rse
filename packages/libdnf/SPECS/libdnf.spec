%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

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
Release:        3%{?dist}
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
BuildRequires:  pkgconfig(gtk-doc)
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
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  gettext
BuildRequires:  gpgme-devel
BuildRequires:  gnupg2 >= 2.2.20-4

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

# Rewrite some hardcoded paths
perl -pi -e "s|/etc/os-release|%{_sysconfdir}/os-release|g" libdnf/utils/os-release.cpp
perl -pi -e "s|/usr/lib/os-release|%{_prefix}/lib/os-release|g" libdnf/utils/os-release.cpp

perl -pi -e "s|/var/lib/dnf|/usr/sgug/var/lib/dnf|g" libdnf/conf/Const.hpp
perl -pi -e "s|/var/cache/dnf|/usr/sgug/var/cache/dnf|g" libdnf/conf/Const.hpp
perl -pi -e "s|/etc/dnf/|%{_sysconfdir}/dnf/|g" libdnf/conf/Const.hpp
perl -pi -e "s|/etc/yum/|%{_sysconfdir}/yum/|g" libdnf/conf/Const.hpp
perl -pi -e "s|/var/lib/rpm|/usr/sgug/var/lib/rpm|g" libdnf/conf/Const.hpp
perl -pi -e "s|/etc/dnf/|%{_sysconfdir}/dnf/|g" libdnf/module/ModulePackageContainer.cpp
perl -pi -e "s|usr/etc/os-release|usr/sgug/etc/os-release|g" libdnf/dnf-context.cpp
perl -pi -e "s|var/lib/rpm|usr/sgug/var/lib/rpm|g" libdnf/dnf-context.cpp

perl -pi -e "s|/etc/yum.repos.d|/usr/sgug/etc/yum.repos.d|g" libdnf/conf/ConfigMain.cpp
perl -pi -e "s|/etc/yum/protected.d|/usr/sgug/etc/yum/protected.d|g" libdnf/conf/ConfigMain.cpp
perl -pi -e "s|/var/cache/|/usr/sgug/var/cache/|g" libdnf/dnf-sack.cpp
perl -pi -e "s|/var/tmp/|/usr/sgug/var/tmp/|g" libdnf/dnf-sack.cpp
perl -pi -e "s|/etc/pki/|/usr/sgug/etc/pki/|g" libdnf/dnf-keyring.cpp
perl -pi -e "s|/run/user/|/usr/sgug/var/run/user/|g" libdnf/repo/Repo.cpp

perl -pi -e "s|/var/lib/dnf/history|%{_prefix}/var/lib/dnf/history|g" libdnf/transaction/Swdb.hpp

# Don't do this rewrite - some of the tests rely on /usr/bin paths
# to correctly execute
#perl -pi -e "s|/usr/bin/|/usr/sgug/bin/|g" tests/hawkey/test_sack.cpp

perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" data/tests/hawkey/yum/recreate
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" data/tests/modules/specs/build.sh

#exit 1

%build
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++

%if 0%{debug}
export CFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_FUNOPEN -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS -g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -ldiclfunopen-0.1"
%else
export CFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_FUNOPEN -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -ldiclfunopen-0.1 $RPM_LD_FLAGS"
%endif

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

#%%if (0%%{?rhel} && 0%%{?rhel} <= 7) || 0%%{?suse_version}
#%%post -p /sbin/ldconfig
#%%postun -p /sbin/ldconfig
#%%else
#%%ldconfig_scriptlets
#%%endif

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
* Wed Dec 02 2020 Daniel Hams <daniel.hams@gmail.com> - 0.48.0-3
- More fixups / debugging, use new gnupg unix socket dir.

* Wed Nov 11 2020 Daniel Hams <daniel.hams@gmail.com> - 0.48.0-2
- More fixups / debugging

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
