# Do we add appdata-files?
# consider conditional on whether %%_metainfodir is defined or not instead -- rex
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without appdata
%else
%bcond_with appdata
%endif

# Set to bcond_without or use --with bootstrap if bootstrapping a new release
# or architecture
%bcond_with bootstrap

# Build with Emacs support
%bcond_without emacs

# Run git tests
%bcond_without git_test

# Set to bcond_with or use --without gui to disable qt4 gui build
%bcond_with gui

# Use ncurses for colorful output
%bcond_without ncurses

# Setting the Python-version used by default
%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_with python3
%else
%bcond_without python3
%endif

# Enable RPM dependency generators for cmake files written in Python
%bcond_without rpm

# Sphinx-build cannot import CMakeLexer on EPEL <= 6
#%%if 0%%{?rhel} && 0%%{?rhel} <= 6
#%%bcond_with sphinx
#%%else
#%%bcond_without sphinx
#%%endif
%bcond_with sphinx

# Run tests
%bcond_without test

# Enable X11 tests
%bcond_without X11_test

# Place rpm-macros into proper location
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Setup _pkgdocdir if not defined already
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Setup _vpath_builddir if not defined already
%{!?_vpath_builddir:%global _vpath_builddir %{_target_platform}}

%global major_version 3
%global minor_version 17
# Set to RC version if building RC, else %%{nil}
#global rcsuf rc3
%{?rcsuf:%global relsuf .%{rcsuf}}
%{?rcsuf:%global versuf -%{rcsuf}}

# Uncomment if building for EPEL
#global name_suffix %%{major_version}
%global orig_name cmake

Name:           %{orig_name}%{?name_suffix}
Version:        %{major_version}.%{minor_version}.2
Release:        3%{?relsuf}%{?dist}
Summary:        Cross-platform make system

# most sources are BSD
# Source/CursesDialog/form/ a bunch is MIT
# Source/kwsys/MD5.c is zlib
# some GPL-licensed bison-generated files, which all include an
# exception granting redistribution under terms of your choice
License:        BSD and MIT and zlib
URL:            http://www.cmake.org
Source0:        http://www.cmake.org/files/v%{major_version}.%{minor_version}/%{orig_name}-%{version}%{?versuf}.tar.gz
Source1:        %{name}-init.el
Source2:        macros.%{name}
# See https://bugzilla.redhat.com/show_bug.cgi?id=1202899
Source3:        %{name}.attr
Source4:        %{name}.prov
Source5:        %{name}.req

# Always start regular patches with numbers >= 100.
# We need lower numbers for patches in compat package.
# And this enables us to use %%autosetup
#
# Patch to fix RindRuby vendor settings
# http://public.kitware.com/Bug/view.php?id=12965
# https://bugzilla.redhat.com/show_bug.cgi?id=822796
Patch100:       %{name}-findruby.patch
# replace release flag -O3 with -O2 for fedora
Patch101:       %{name}-fedora-flag_release.patch
# Add dl to CMAKE_DL_LIBS on MINGW
# https://gitlab.kitware.com/cmake/cmake/issues/17600
Patch102:       %{name}-mingw-dl.patch


# Patch for renaming on EPEL
%if 0%{?name_suffix:1}
Patch1:      %{name}-rename.patch
%if 0%{?rhel} && 0%{?rhel} <= 6
Patch2:      %{name}-libarchive3.patch
%endif
%endif

Patch1000:      cmake.sgifixeslibuv.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
#BuildRequires:  gcc-gfortran
BuildRequires:  sed
%if %{with git_test}
# Tests fail if only git-core is installed, bug #1488830
BuildRequires:  git
%else
BuildConflicts: git-core
%endif
%if %{with X11_test}
BuildRequires:  libX11-devel
%endif
%if %{with ncurses}
BuildRequires:  ncurses-devel
%endif
%if %{with sphinx}
BuildRequires:  %{_bindir}/sphinx-build
%endif
%if %{without bootstrap}
BuildRequires:  bzip2-devel
BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  jsoncpp-devel
#%%if 0%%{?fedora} || 0%%{?rhel} >= 7
BuildRequires:  libarchive-devel
#%%else
#BuildRequires:  libarchive3-devel
#%%endif
BuildRequires:  libuv-devel
BuildRequires:  rhash-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
%endif
%if %{with emacs}
BuildRequires:  emacs
%endif
BuildRequires:  openssl-devel
%if %{with rpm}
%if %{with python3}
%{!?python3_pkgversion: %global python3_pkgversion 3}
BuildRequires:  python%{python3_pkgversion}-devel
%else
BuildRequires:  python2-devel
%endif
%endif
#BuildRequires: xmlrpc-c-devel
%if %{with gui}
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: pkgconfig(Qt5Widgets)
%else
BuildRequires: pkgconfig(QtGui)
%endif
BuildRequires: desktop-file-utils
%endif

%if %{without bootstrap}
# Ensure we have our own rpm-macros in place during build.
BuildRequires:  %{name}-rpm-macros
# Ensure recent enough rpm that has already seen cmake installed
# so it has the right value for the cmake macro
BuildRequires:  rpm >= 4.15.0-11
%endif

Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-rpm-macros = %{version}-%{release}
Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}

# Provide the major version name
Provides: %{orig_name}%{major_version} = %{version}-%{release}

# Source/kwsys/MD5.c
# see https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
Provides: bundled(md5-deutsch)

# https://fedorahosted.org/fpc/ticket/555
Provides: bundled(kwsys)

%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is possible
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.


%package        data
Summary:        Common data-files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-rpm-macros = %{version}-%{release}
%if %{with emacs}
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:       emacs-filesystem%{?_emacs_version: >= %{_emacs_version}}
%endif
%endif

BuildArch:      noarch

%description    data
This package contains common data-files for %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.


%package        filesystem
Summary:        Directories used by CMake modules

%description    filesystem
This package owns all directories used by CMake modules.


%if %{with gui}
%package        gui
Summary:        Qt GUI for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       shared-mime-info%{?_isa}

%description    gui
The %{name}-gui package contains the Qt based GUI for %{name}.
%endif


%package        rpm-macros
Summary:        Common RPM macros for %{name}
Requires:       rpm
# when subpkg introduced
Conflicts:      cmake-data < 3.10.1-2

BuildArch:      noarch

%description    rpm-macros
This package contains common RPM macros for %{name}.


%prep
%autosetup -n %{orig_name}-%{version}%{?versuf} -p 1

%if %{with rpm}
%if %{with python3}
echo '#!%{__python3}' > %{name}.prov
echo '#!%{__python3}' > %{name}.req
%else
echo '#!%{__python2}' > %{name}.prov
echo '#!%{__python2}' > %{name}.req
%endif
tail -n +2 %{SOURCE4} >> %{name}.prov
tail -n +2 %{SOURCE5} >> %{name}.req
%endif

# For patch creation
#exit 1

%build
%if 0%{?set_build_flags:1}
%{set_build_flags}
%else
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;}
%endif
SRCDIR="$(/usr/bin/pwd)"
mkdir %{_vpath_builddir}
export PREV_WD=`pwd`
cd %{_vpath_builddir}

# Temporary for debugging
#export CFLAGS="-g -O0"
#export CXXFLAGS="-g -O0"

# To ensure we pick up the right compiler
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
# Yes, we don't have this
export FC=mips-sgi-irix6.5-gcf
#export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export CFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS $CFLAGS"
export CXXFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS $CXXFLAGS"
#export LDFLAGS="-ldicl-0.1 $LDFLAGS"
export NUM_PARALLEL=`echo -- "%{_smp_mflags}" |perl -pe "s|.*\-j(\\\\d+).*|\\\$1|g"`
# Possibly weirdness with mksh (SIGCHLD propogation / defunct children)
export SHELL=%{_bindir}/bash
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"

$SHELL $SRCDIR/bootstrap --prefix=%{_prefix} --datadir=/share/%{name} \
                  --docdir=/share/doc/%{name} --mandir=/share/man \
                  --%{?with_bootstrap:no-}system-libs \
                  --parallel=$NUM_PARALLEL \
%if %{with sphinx}
                  --sphinx-man --sphinx-html \
%else
                  --sphinx-build=%{_bindir}/false \
%endif
                  --%{!?with_gui:no-}qt-gui \
;
cd $PREV_WD
%make_build -C %{_vpath_builddir} VERBOSE=1


%install
mkdir -p %{buildroot}%{_pkgdocdir}
%make_install -C %{_vpath_builddir} CMAKE_DOC_DIR=%{buildroot}%{_pkgdocdir}
find %{buildroot}%{_datadir}/%{name}/Modules -type f | xargs chmod -x
[ -n "$(find %{buildroot}%{_datadir}/%{name}/Modules -name \*.orig)" ] &&
  echo "Found .orig files in %{_datadir}/%{name}/Modules, rebase patches" &&
  exit 1
# Install major_version name links
%{!?name_suffix:for f in ccmake cmake cpack ctest; do ln -s $f %{buildroot}%{_bindir}/${f}%{major_version}; done}
# Install bash completion symlinks
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
for f in %{buildroot}%{_datadir}/%{name}/completions/*
do
  ln -s ../../%{name}/completions/$(basename $f) %{buildroot}%{_datadir}/bash-completion/completions
done
%if %{with emacs}
# Install emacs cmake mode
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
install -p -m 0644 Auxiliary/cmake-mode.el %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
%{_emacs_bytecompile} %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}
%endif
# RPM macros
install -p -m0644 -D %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.%{name}
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" -e "s|@@CMAKE_MAJOR_VERSION@@|%{major_version}|" %{buildroot}%{rpm_macros_dir}/macros.%{name}
touch -r %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.%{name}
%if %{with rpm} && 0%{?_rpmconfigdir:1}
# RPM auto provides
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_prefix}/lib/rpm/fileattrs/%{name}.attr
install -p -m0755 -D %{name}.prov %{buildroot}%{_prefix}/lib/rpm/%{name}.prov
install -p -m0755 -D %{name}.req %{buildroot}%{_prefix}/lib/rpm/%{name}.req
%endif
mkdir -p %{buildroot}%{_libdir}/%{orig_name}
# Install copyright files for main package
find Source Utilities -type f -iname copy\* | while read f
do
  fname=$(basename $f)
  dir=$(dirname $f)
  dname=$(basename $dir)
  cp -p $f ./${fname}_${dname}
done
# Cleanup pre-installed documentation
%if %{with sphinx}
mv %{buildroot}%{_docdir}/%{name}/html .
%endif
rm -rf %{buildroot}%{_docdir}/%{name}
# Install documentation to _pkgdocdir
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr %{buildroot}%{_datadir}/%{name}/Help %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_pkgdocdir}/Help %{buildroot}%{_pkgdocdir}/rst
%if %{with sphinx}
mv html %{buildroot}%{_pkgdocdir}
%endif

%if %{with gui}
# Desktop file
desktop-file-install --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-gui.desktop

%if %{with appdata}
# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/cmake-gui.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: kitware@kitware.com
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">cmake-gui.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>CMake GUI</name>
  <summary>Create new CMake projects</summary>
  <description>
    <p>
      CMake is an open source, cross platform build system that can build, test,
      and package software. CMake GUI is a graphical user interface that can
      create and edit CMake projects.
    </p>
  </description>
  <url type="homepage">http://www.cmake.org</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/CMake/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
%endif
%endif

# create manifests for splitting files and directories for filesystem-package
find %{buildroot}%{_datadir}/%{name} -type d | \
  sed -e 's!^%{buildroot}!%%dir "!g' -e 's!$!"!g' > data_dirs.mf
find %{buildroot}%{_datadir}/%{name} -type f | \
  sed -e 's!^%{buildroot}!"!g' -e 's!$!"!g' > data_files.mf
find %{buildroot}%{_libdir}/%{orig_name} -type d | \
  sed -e 's!^%{buildroot}!%%dir "!g' -e 's!$!"!g' > lib_dirs.mf
find %{buildroot}%{_libdir}/%{orig_name} -type f | \
  sed -e 's!^%{buildroot}!"!g' -e 's!$!"!g' > lib_files.mf
find %{buildroot}%{_bindir} -type f -or -type l -or -xtype l | \
  sed -e '/.*-gui$/d' -e '/^$/d' -e 's!^%{buildroot}!"!g' -e 's!$!"!g' >> lib_files.mf

# Fix up some badly paths
perl -pi -e "s|/usr/bin/rpm|%{_bindir}/rpm|g" $RPM_BUILD_ROOT%{_prefix}/lib/rpm/%{name}.req
perl -pi -e "s|/usr/lib\(64\)\?|%{_libdir}|g" $RPM_BUILD_ROOT%{_prefix}/lib/rpm/%{name}.req
perl -pi -e "s|/usr/bin/cmake|%{_bindir}/cmake|g" $RPM_BUILD_ROOT%{_prefix}/lib/rpm/macros.d/macros.%{name}

%if %{with test}
%check
%if 0%{?rhel} && 0%{?rhel} <= 6
mv -f Modules/FindLibArchive.cmake Modules/FindLibArchive.disabled
%endif
export PREV_WD=`pwd`
cd %{_vpath_builddir}
# CTestTestUpload require internet access
# CPackComponentsForAll-RPM-IgnoreGroup failing wih rpm 4.15 - https://gitlab.kitware.com/cmake/cmake/issues/19983
NO_TEST="CTestTestUpload|CPackComponentsForAll-RPM-IgnoreGroup"
# kwsys.testProcess-{4,5} are flaky on s390x.
%ifarch s390x
NO_TEST="$NO_TEST|kwsys.testProcess-4|kwsys.testProcess-5"
%endif
bin/ctest%{?name_suffix} %{?_smp_mflags} -V -E "$NO_TEST" --output-on-failure
# Keep an eye on failing tests
bin/ctest%{?name_suffix} %{?_smp_mflags} -V -R "$NO_TEST" --output-on-failure || :
cd $PREV_WD
%if 0%{?rhel} && 0%{?rhel} <= 6
mv -f Modules/FindLibArchive.disabled Modules/FindLibArchive.cmake
%endif
%endif


%files -f lib_files.mf
%doc %dir %{_pkgdocdir}
%license Copyright.txt*
%license COPYING*
%if %{with sphinx}
%{_mandir}/man1/c%{name}.1.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/cpack%{?name_suffix}.1.*
%{_mandir}/man1/ctest%{?name_suffix}.1.*
%{_mandir}/man7/*.7.*
%endif


%files data -f data_files.mf
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/bash-completion
%if %{with emacs}
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_emacs_sitelispdir}/%{name}
%{_emacs_sitestartdir}/%{name}-init.el
%else
%{_emacs_sitelispdir}
%{_emacs_sitestartdir}
%endif
%endif


%files doc
# Pickup license-files from main-pkg's license-dir
# If there's no license-dir they are picked up by %%doc previously
%{?_licensedir:%license %{_datadir}/licenses/%{name}*}
%doc %{_pkgdocdir}


%files filesystem -f data_dirs.mf -f lib_dirs.mf


%if %{with gui}
%files gui
%{_bindir}/%{name}-gui
%if %{with appdata}
%{_metainfodir}/*.appdata.xml
%endif
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/mime/packages
%{_datadir}/icons/hicolor/*/apps/CMake%{?name_suffix}Setup.png
%if %{with sphinx}
%{_mandir}/man1/%{name}-gui.1.*
%endif
%endif


%files rpm-macros
%{rpm_macros_dir}/macros.%{name}
%if %{with rpm} && 0%{?_rpmconfigdir:1}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}.prov
%{_rpmconfigdir}/%{name}.req
%endif


%changelog
* Wed May 13 2020 Daniel Hams <daniel.hams@gmail.com> - 3.17.2-3
- More lib install dir fixes (LIB_SUFFIX) and ensure .so are installed executable (needed to get rpm to detect them)

* Tue May 12 2020 Daniel Hams <daniel.hams@gmail.com> - 3.17.2-2
- Fix lib install dir to be lib32, pull bug fixes + stability fixes from sgug libuv github

* Sat May 9 2020 Daniel Hams <daniel.hams@gmail.com> - 3.17.2-1
- Import from fedora

* Tue Apr 28 2020 Björn Esser <besser82@fedoraproject.org> - 3.17.2-1
- Update to cmake-3.17.2

* Thu Apr 09 2020 Björn Esser <besser82@fedoraproject.org> - 3.17.1-1
- Update to cmake-3.17.1

* Tue Mar 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.17.0-1
- Update to cmake-3.17.0

* Fri Mar 13 2020 Björn Esser <besser82@fedoraproject.org> - 3.17.0-0.4.rc3
- Update to 3.17.0-rc3

* Tue Mar 03 2020 Björn Esser <besser82@fedoraproject.org> - 3.17.0-0.3.rc2
- Update to 3.17.0-rc2

* Thu Feb 27 2020 Orion Poplawski <orion@nwra.com> - 3.17.0-0.2.rc1
- Use python3 for rpm generators
- Use lowercase names for cmake provides in generator (in addition to old names)

* Mon Feb 17 2020 Björn Esser <besser82@fedoraproject.org> - 3.17.0-0.1.rc1
- Update to 3.17.0-rc1

* Wed Feb 05 2020 Björn Esser <besser82@fedoraproject.org> - 3.16.4-1
- Update to 3.16.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Björn Esser <besser82@fedoraproject.org> - 3.16.3-1
- Update to 3.16.3

* Wed Jan 15 2020 Björn Esser <besser82@fedoraproject.org> - 3.16.2-1
- Update to 3.16.2
- Use %%_vpath_builddir for out-of-tree build
- Use %%set_build_flags to export build flags if available
- Use %%set_build_flags inside macros.cmake if available

* Tue Jan 14 2020 Miro Hrončok <mhroncok@redhat.com> - 3.16.1-2
- FindPython: Add support for version 3.9

* Sat Dec 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.16.1-1
- Update to 3.16.1
- Re-enable test "kwsys.testProcess-5" on S390X

* Tue Nov 26 2019 Björn Esser <besser82@fedoraproject.org> - 3.16.0-1
- Update to 3.16.0
- Exclude test "kwsys.testProcess-5" on S390X

* Mon Nov 18 2019 Orion Poplawski <orion@nwra.com> - 3.16.0-0.1.rc4
- Update to 3.16.0-rc4
- Cleanup %%check

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.15.5-2
- Rebuild (jsoncpp)
- Exclude more tests failing on s390x

* Wed Oct 30 2019 Orion Poplawski <orion@nwra.com> - 3.15.5-1
- Update to 3.15.5

* Wed Oct 16 2019 Orion Poplawski <orion@nwra.com> - 3.15.4-1
- Update to 3.15.4

* Mon Sep 30 2019 Orion Poplawski <orion@nwra.com> - 3.15.3-1
- Update to 3.15.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.5-3
- Rebuild (jsoncpp), qt5 enabled

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.5-2
- Rebuild (jsoncpp), bootstrap without qt5
- Ignore a test failing with rpm-4.15

* Fri May 31 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.5-1
- 3.14.5

* Tue May 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.4-1
- 3.14.4

* Mon Apr 22 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.3-1
- 3.14.3

* Fri Apr 12 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.2-1
- 3.14.2

* Fri Mar 29 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.1-1
- 3.14.1

* Thu Mar 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.14.0-2
- pull in upstream fix for conflict with ECM/FindFontConfig

* Fri Mar 15 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.0-1
- 3.14.0

* Sat Feb 2 2019 Orion Poplawski <orion@nwra.com> - 3.13.4-1
- 3.13.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.13.3-1
- 3.13.3

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.13.2-1
- 3.13.2

* Sat Dec 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.13.1-2
- macros.cmake: introduce %%_cmake_shared_libs macro

* Wed Nov 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.13.1-1
- 3.13.1

* Sat Sep 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.12.2-1
- Update to 3.12.2

* Fri Aug 17 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.12.1-1
- Update to 3.12.1 (# 1614572)

* Fri Jul 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.12.0-1
- Update to 3.12.0 (#1584925)
- fixes libuv-related FTBFS (#1603661)
- use %%_metainfodir

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.11.2-2
- Rebuilt for Python 3.7

* Fri May 18 2018 Björn Esser <besser82@fedoraproject.org> - 3.11.2-1
- Update to 3.11.2 (#1568630)

* Thu Mar 29 2018 Björn Esser <besser82@fedoraproject.org> - 3.11.0-1
- Update to 3.11.0 (#1536233)

* Thu Mar 08 2018 Orion Poplawski <orion@nwra.com> - 3.10.2-4
- Add patch to fix autogen with empty files (bug #1551147)

* Thu Mar 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.10.2-3
- better Qt dependencies

* Fri Mar 02 2018 Kalev Lember <klember@redhat.com> - 3.10.2-2
- Fix appdata file to match with desktop file name

* Thu Feb 22 2018 Orion Poplawski <orion@nwra.com> - 3.10.2-1
- Update to 3.10.2
- Add patch to fix test failure with gcc 8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.10.1-12
- Conflicts was the right choice

* Sun Jan 14 2018 Björn Esser <besser82@fedoraproject.org> - 3.10.1-11
- rpm-macros: Keep cmake{,-data} in evr-lock, if they are installed

* Sun Jan 14 2018 Björn Esser <besser82@fedoraproject.org> - 3.10.1-10
- rpm-macros: Use rich boolean Requires instead of Conflicts (#1532293)

* Sat Jan 13 2018 Rex Dieter <rdieter@fedoraproject.org> 3.10.1-9
- -rpm-macros: Conflicts: cmake-data < 3.10.1-2 (#1532293)

* Tue Jan 02 2018 Sandro Mani <manisandro@gmail.com> - 3.10.1-8
- Add dl to CMAKE_DL_LIBS on MINGW

* Sat Dec 30 2017 Richard W.M. Jones <rjones@redhat.com> - 3.10.1-7
- Add small fix for RISC-V support.

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 3.10.1-6
- Rebuilt for jsoncpp.so.20

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 3.10.1-5
- Bootstrapping for jsoncpp-1.8.4

* Thu Dec 21 2017 Björn Esser <besser82@fedoraproject.org> - 3.10.1-4
- Re-add arched requires on filesystem sub-package

* Thu Dec 21 2017 Björn Esser <besser82@fedoraproject.org> - 3.10.1-3
- Ensure we have our own rpm-macros in place during build

* Thu Dec 21 2017 Björn Esser <besser82@fedoraproject.org> - 3.10.1-2
- Move rpm macros to own subpackage (#1498894)

* Sat Dec 16 2017 Björn Esser <besser82@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1 (#1526648)

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0 (#1515793)

* Fri Nov 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.9.6-1
- Update to 3.9.6

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.9.5-1
- Update to 3.9.5 (#1498688)

* Thu Sep 21 2017 Pete Walter <pwalter@fedoraproject.org> - 3.9.3-1
- Update to 3.9.3

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.1-4
- Rebuilt for jsoncpp-1.8.3

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.1-3
- Bootstrapping for jsoncpp-1.8.3

* Sun Aug 13 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.1-2
- Add patch to restore old style debuginfo creation for rpm >= 4.14
  in CPackRPM

* Sat Aug 12 2017 Pete Walter <pwalter@fedoraproject.org> - 3.9.1-1
- Update to 3.9.1

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-9
- RunCMake.File_Generate fails on S390X, skip it temporarily

* Wed Aug 02 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-8
- Fix cmake.attr and cmake.req to work properly

* Wed Aug 02 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-7
- Add cmake.req to autogenerate proper depency on cmake-filesystem

* Wed Aug 02 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-6
- Fix cmake-gui being picked up by main package

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-5
- Optimizations for filesystem-package

* Fri Jul 28 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-4
- Temporarily disable RunCMake.CPack_RPM, because it fails for the new
  way RPM handles debug-stuff

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-2
- Update patch for Fedora RELEASE-builds
- Add patch to fix warnings from Sphinx

* Wed Jul 19 2017 Björn Esser <besser82@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0 final (rhbz#1472503)
- Add filesystem package (rhbz#1471153)

* Thu Jun 01 2017 Björn Esser <besser82@fedoraproject.org> - 3.8.2-1
- Update to 3.8.2 final (rhbz#1447473)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Apr 28 2017 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-3
- Add upstream patch to fix FindGLUT library dependencies (bug #1444563)

* Fri Apr 21 2017 Karsten Hopp <karsten@redhat.com> - 3.8.0-2
- use new _module_build macro to limit dependencies for Modularity

* Mon Apr 10 2017 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-1
- Update to 3.8.0 final

* Mon Mar 27 2017 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-0.2.rc3
- Update to 3.8.0-rc3
- Add upstream patch to support rpm build-id dirs

* Mon Mar 20 2017 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-0.1.rc2
- Update to 3.8.0-rc2

* Mon Feb 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.7.2-4
- Add patch to handle gcc format option changes

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.7.2-3
- Fix ambiguous file lookup in cmake.prov

* Thu Feb 9 2017 Orion Poplawski <orion@cora.nwra.com> - 3.7.2-2
- Fix cmake.prov error

* Fri Jan 13 2017 Orion Poplawski <orion@cora.nwra.com> - 3.7.2-1
- Update to 3.7.2

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 3.7.1-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Orion Poplawski <orion@cora.nwra.com> - 3.7.1-1
- Update to 3.7.1

* Sat Nov 12 2016 Orion Poplawski <orion@cora.nwra.com> - 3.7.0-1
- Update to 3.7.0 final

* Fri Nov 4 2016 Orion Poplawski <orion@cora.nwra.com> - 3.7.0-0.3.rc3
- Update to 3.7.0-rc3

* Wed Oct 19 2016 Orion Poplawski <orion@cora.nwra.com> - 3.7.0-0.2.rc2
- Update to 3.7.0-rc2

* Thu Oct 6 2016 Orion Poplawski <orion@cora.nwra.com> - 3.7.0-0.1.rc1
- Update to 3.7.0-rc1
- Drop gui, findjni, and riscv patches applied upstream

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 3.6.2-6
- Rebuilt with gui enabled

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 3.6.2-5
- Rebuilt for libjsoncpp.so.11
- Bootstrap without gui, due inter-circular dependency in qt5-rpm-macros

* Mon Sep 26 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-4
- Add upstream patch for Qt5 QFileDialog usage

* Mon Sep 26 2016 Than Ngo <than@redhat.com> - 3.6.2-3
- Add aarch32 to libarch for arm platform

* Mon Sep 12 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-2
- Provide the major version cmakeX name

* Thu Sep 8 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-1
- Update to 3.6.2

* Tue Aug 16 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-2
- Ship symlinks to binaries with major version in name
- Provide %%cmakeX macro, where X is cmake major version

* Mon Jul 25 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-1
- Update to 3.6.1

* Fri Jul 8 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6.0-1
- Update to 3.6.0

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6.0-0.1.rc4
- Update to 3.6.0-rc4

* Fri Jun 03 2016 Orion Poplawski <orion@cora.nwra.com> - 3.5.2-3
- Add patch to support libarchive 3.2

* Thu Jun 02 2016 Than Ngo <than@redhat.com> - 3.5.2-3
- drop -O3 and add -O2 for default release

* Thu Apr 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.5.2-2
- Do not own /usr/lib/rpm/fileattrs

* Fri Apr 15 2016 Orion Poplawski <orion@cora.nwra.com> - 3.5.2-1
- Update to 3.5.2 final

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 3.5.1-2
- Rebuilt for libjsoncpp.so.1

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 3.5.1-1
- Update to 3.5.1 (#1321198)

* Thu Mar 10 2016 Björn Esser <fedora@besser82.io> - 3.5.0-2
- keep Help-directory and its contents in %%_datadir/%%name (#1316306)

* Tue Mar 8 2016 Orion Poplawski <orion@cora.nwra.com> - 3.5.0-1
- Update to 3.5.0 final

* Mon Mar 07 2016 Björn Esser <fedora@besser82.io> - 3.5.0-0.3.rc3
- cleanup trailing whitespaces
- remove el5 stuff
- doc-subpkg should be noarch'ed
- doc-subpkg should not require main-pkg
- add %%{?_isa} to the applicable Requires
- replaced %%define with %%global
- handle macrosdir for rpm-macros properly
- fix ownership of directories, add needed Requires
- conditionalize appdata
- handle docdir properly
- generalize glob for man-pages independent of used compression
- generalize for use as EPEL-package, too
- use %%license instead of %%doc for license-files
- split the common data-files into a noarch'ed subpackage
- build html-docs and put them into the doc-subpkg

* Sat Feb 20 2016 Orion Poplawski <orion@cora.nwra.com> - 3.5.0-0.2.rc3
- Update to 3.5.0-rc3

* Wed Feb 17 2016 Orion Poplawski <orion@cora.nwra.com> - 3.5.0-0.1.rc2
- Update to 3.5.0-rc2
- Drop dcmtk patch

* Sun Feb 7 2016 Orion Poplawski <orion@cora.nwra.com> - 3.4.3-3
- Fix build without gui (bug #1305310)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Orion Poplawski <orion@cora.nwra.com> - 3.4.3-1
- Update to 3.4.3

* Tue Jan 19 2016 Orion Poplawski <orion@cora.nwra.com> - 3.4.2-1
- Update to 3.4.2

* Sat Dec 12 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.4.1-4
- Use Python 3 on F-23+

* Tue Dec 8 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.1-3
- Use Qt5 for gui

* Mon Dec 7 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.1-2
- Fixup some conditionals for RHEL7

* Wed Dec 2 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.1-1
- Update to 3.4.1

* Wed Nov 25 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-2
- BR /usr/bin/sphinx-build instead of python-sphinx

* Tue Nov 17 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-1
- Update to 3.4.0 final

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-0.3.rc3
- Update to 3.4.0-rc3

* Wed Oct 21 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-0.2.rc2
- Update to 3.4.0-rc2

* Tue Oct 6 2015 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-0.1.rc1
- Update to 3.4.0-rc1

* Tue Oct 6 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.2-2
- Add upstream patch to find python 3.5 (bug #1269095)

* Thu Sep 17 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.2-1
- Update to 3.3.2
- Use %%{__global_ldflags}
- Fix test exclusion

* Fri Sep 11 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-5
- Apply upstream patch to fix Fortran linker detection with redhat-hardened-ld
  (bug #1260490)

* Wed Sep 9 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-4
- Apply upstream patch to fix trycompile output (bug #1260490)

* Tue Aug 25 2015 Rex Dieter <rdieter@fedoraproject.org> 3.3.1-3
- pull in some upstream fixes (FindPkgConfig,boost-1.59)

* Fri Aug 21 2015 Rex Dieter <rdieter@fedoraproject.org> 3.3.1-2
- Provides: bundled(kwsys)

* Thu Aug 13 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-1
- Update to 3.3.1

* Thu Jul 23 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-1
- Update to 3.3.0

* Thu Jul 9 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.4.rc3
- Update to 3.3.0-rc3
- Fix cmake.attr to handle 32-bit libraries

* Tue Jun 23 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.3.rc2
- Update to 3.3.0-rc2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 8 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.1.rc1
- Update to 3.3.0-rc1

* Mon Jun 8 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.3-1
- Update to 3.2.3

* Wed Apr 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.2-1
- Update to 3.2.2

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.2.1-5
- Add an AppData file for the software center

* Mon Mar 23 2015 Daniel Vrátil <dvratil@redhat.com> - 3.2.1-4
- cmake.prov: handle exceptions

* Wed Mar 18 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.1-3
- cmake.prov: use /usr/bin/python (instead of /bin/python)

* Tue Mar 17 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.1-2
- RFE: CMake automatic RPM provides  (#1202899)

* Wed Mar 11 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-1
- Update to 3.2.1

* Thu Feb 26 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.0-0.2.rc2
- Update to 3.2.0-rc2
- Drop C++11 ABI workaround, fixed in gcc
- Drop strict_aliasing patch fixed upstream long ago
- Drop FindLua52, FindLua should work now for 5.1-5.3

* Sun Feb 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.0-0.1.rc1
- Update to 3.2.0-rc1
- Drop ninja patch fixed upstream
- Upstream now ships icons, add icon-cache scriptlets

* Fri Feb 13 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.3-1
- Update to 3.1.3

* Sat Feb 7 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.2-1
- Update to 3.1.2

* Fri Jan 23 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.1-1
- Update to 3.1.1
- Drop ruby patch applied upstream

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-2
- Fix ruby 2.2.0 teeny (0) detection

* Wed Dec 17 2014 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-1
- Update to 3.1.0 final

* Sat Nov 15 2014 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-0.2.rc2
- Update to 3.1.0-rc2

* Wed Oct 29 2014 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-0.1.rc1
- Update to 3.1.0-rc1

* Mon Sep 15 2014 Dan Horák <dan[at]danny.cz> - 3.0.2-2
- fix FindJNI for ppc64le (#1141782)

* Sun Sep 14 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-1
- Update to 3.0.2

* Mon Aug 25 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-3
- Update wxWidgets patches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 6 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-2
- optimize mimeinfo scriptlet

* Sat Jun 14 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-1
- Update to 3.0.0 final

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.11.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.10.rc6
- Update to 3.0.0-rc6

* Wed May 14 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.9.rc5
- Update to 3.0.0-rc5
- Drop icon patch applied upstream

* Tue Apr 22 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.8.rc4
- Update to 3.0.0-rc4

* Thu Apr 10 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.7.rc3
- Fix doc duplication

* Fri Apr 4 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.6.rc3
- Rebase patches to prevent .orig files in Modules
- Add install check for .orig files

* Wed Mar 26 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.5.rc3
- Update to 3.0.0-rc3
- Add patch to fix FindwxWidgets when cross-compiling for Windows (bug #1081207)

* Wed Mar 5 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.4.rc1
- Add additional FindPythonLibs patch from upstream (bug #1072964)

* Mon Mar 3 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.3.rc1
- Update to upstreams version of FindPythonLibs patch

* Mon Mar 3 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.2.rc1
- Use symlinks for bash completions

* Fri Feb 28 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.1.rc1
- Update to 3.0.0-rc1
- Update qtdeps patch to upstreamed version
- Install bash completions

* Tue Feb 11 2014 Orion Poplawski <orion@cora.nwra.com> - 2.8.12.2-2
- Add upstream patch to find Boost MPI library (bug #756141)

* Tue Jan 28 2014 Orion Poplawski <orion@cora.nwra.com> - 2.8.12.2-1
- Update to 2.8.12.2

* Wed Jan 22 2014 Orion Poplawski <orion@cora.nwra.com> - 2.8.12.1-2
- Fix FindFreetype for 2.5.1+

* Wed Nov 6 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12.1-1
- Update to 2.8.12.1

* Wed Oct 23 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-3
- Remove UseQt4 automatic dependency adding

* Thu Oct 10 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-2
- Autoload cmake-mode in emacs (bug #1017779)

* Tue Oct 8 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-1
- Update to 2.8.12 final

* Tue Oct 1 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-0.6.rc4
- Update to 2.8.12-rc4
- Drop upstreamed FindHD5 patch

* Thu Sep 19 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-0.5.rc3
- Add patch to fix FindHDF5

* Tue Sep 17 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-0.4.rc3
- Update to 2.8.12-rc3

* Wed Sep 4 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-0.3.rc2
- Update to 2.8.12-rc2

* Wed Aug 28 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-0.2.rc1
- Add patch to fix FindPythonLibs issues (bug #876118)
- Split docs into separate -doc sub-package

* Mon Aug 26 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.12-0.1.rc1
- Update to 2.8.12-rc1
- Drop ImageMagick patch - not needed

* Fri Jul 26 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11.2-4
- Use version-less docdir

* Thu Jul 25 2013 Petr Machata <pmachata@redhat.com> - 2.8.11.2-3
- Icon name in desktop file should be sans .png extension.

* Thu Jul 25 2013 Petr Machata <pmachata@redhat.com> - 2.8.11.2-2
- Pass -fno-strict-aliasing to cm_sha2.c to avoid strict aliasing
  problems that GCC warns about.

* Tue Jul 9 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11.2-1
- Update to 2.8.11.2 release

* Mon Jun 10 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11.1-1
- Update to 2.8.11.1 release

* Sat May 18 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11-1
- Update to 2.8.11 release

* Mon May 13 2013 Tom Callaway <spot@fedoraproject.org> - 2.8.11-0.9.rc4
- add FindLua52.cmake

* Thu May 9 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11-0.8.rc4
- Update to 2.8.11-rc4

* Fri Apr 19 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11-0.7.rc3
- Update to 2.8.11-rc3

* Thu Apr 18 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11-0.6.rc2
- Drop -O3 from default release build type flags in cmake rpm macro (bug 875954)

* Wed Apr 17 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11-0.5.rc2
- Update to 2.8.11-rc2
- Rebase ImageMagick patch

* Mon Mar 18 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8.11-0.4.rc1
- respin cmake-2.8.11-rc1-IM_pkgconfig_hints.patch
- drop/omit backup files when applying patches

* Sat Mar 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8.11-0.3.rc1
- Patch FindImageMagick.cmake for newer ImageMagick versions

* Sat Mar 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8.11-0.2.rc1
- use %%{_rpmconfigdir}/macros.d on f19+

* Fri Mar 15 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.11-0.1.rc1
- Update to 2.8.11-rc1
- Drop upstream ccmake and usrmove patches

* Wed Mar 13 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.10.2-5
- Add patch from upstream to fix UsrMove handling (bug #917407)
- Drop %%config from rpm macros
- Define FCFLAGS in cmake macro

* Fri Feb 8 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.10.2-4
- Add patch to use ninja-build (bug #886184)

* Thu Jan 24 2013 Orion Poplawski <orion@cora.nwra.com> - 2.8.10.2-3
- Update FindPostgreSQL patch to use PostgreSQL_LIBRARY (bug #903757)

* Thu Jan 17 2013 Tomas Bzatek <tbzatek@redhat.com> - 2.8.10.2-2
- Rebuilt for new libarchive

* Tue Nov 27 2012 Rex Dieter <rdieter@fedoraproject.org> 2.8.10.2-1
- 2.8.10.2

* Thu Nov 8 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.10.1-1
- Update to 2.8.10.1

* Thu Nov 1 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.10-1
- Update to 2.8.10 final

* Thu Oct 25 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.10-0.2.rc3
- Add patch to fix DEL key in ccmake (bug 869769)

* Wed Oct 24 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.10-0.1.rc3
- Update to 2.8.10 RC 3
- Rebase FindRuby and FindPostgreSQL patches

* Thu Aug 9 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.9-1
- Update to 2.8.9 final

* Fri Jul 27 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.9-0.4.rc3
- Update to 2.8.9 RC 3

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.9-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.9-0.2.rc2
- Update to 2.8.9 RC 2

* Tue Jul 10 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.9-0.1.rc1
- Update to 2.8.9 RC 1
- Drop pkgconfig patch

* Thu Jul 5 2012 Orion Poplawski <orion@cora.nwra.com> 2.8.8-5
- Add patch to fix FindPostgreSQL (bug 828467)

* Mon May 21 2012 Orion Poplawski <orion@cora.nwra.com> 2.8.8-4
- Add patch to fix FindRuby (bug 822796)

* Thu May 10 2012 Rex Dieter <rdieter@fedoraproject.org> 2.8.8-3
- Incorrect license tag in spec file (#820334)

* Thu May 3 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.8-2
- Comply with Emacs packaging guidlines (bug #818658)

* Thu Apr 19 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.8-1
- Update to 2.8.8 final

* Sat Apr 14 2012 Rex Dieter <rdieter@fedoraproject.org> 2.8.8-0.4.rc2
- adjust pkgconfig patch (#812188)

* Fri Apr 13 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.8-0.3.rc2
- Add upstream patch to set PKG_CONFIG_FOUND (bug #812188)

* Mon Apr 9 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.8-0.2.rc2
- Update to 2.8.8 RC 2

* Fri Mar 23 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.8-0.1.rc1
- Update to 2.8.8 RC 1

* Tue Feb 21 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.7-6
- Just strip CMAKE_INSTALL_LIBDIR from %%cmake macro

* Tue Feb 21 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.7-5
- Strip CMAKE_INSTALL_LIBDIR and others from %%cmake macro (bug 795542)

* Thu Jan 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 2.8.7-4
- Rebuilt for new libarchive

* Wed Jan 18 2012 Jaroslav Reznik <jreznik@redhat.com> - 2.8.7-3
- Rebuild for libarchive

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 1 2012 Orion Poplawski <orion@cora.nwra.com> - 2.8.7-1
- Update to 2.8.7 final

* Tue Dec 27 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.7-0.2.rc2
- Update to 2.8.7 RC 2

* Tue Dec 13 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.7-0.1.rc1
- Update to 2.8.7 RC 1

* Tue Nov 15 2011 Daniel Drake <dsd@laptop.org> - 2.8.6-2
- Rebuild for libarchive.so.11

* Wed Oct 5 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.6-1
- Update to 2.8.6 final

* Thu Sep 22 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.6-0.5.rc4
- Update to 2.8.6 RC 4

* Tue Sep 13 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.6-0.4.rc3
- Update to 2.8.6 RC 3

* Sun Sep 11 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.8.6-0.3.rc2
- Sync FFLAGS and LDFLAGS in the %%cmake macro with redhat-rpm-config.

* Tue Sep 6 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.6-0.2.rc2
- Update to 2.8.6 RC 2
- Drop aclocal patch

* Mon Aug 29 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.6-0.1.rc1
- Update to 2.8.6 RC 1
- Update dcmtk patch
- Add upstream patch to fix aclocal install location

* Thu Jul 28 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-3
- Updated patch to find dcmtk in Fedora (Bug #720140)

* Fri Jul 22 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-2
- Add patch to find dcmtk in Fedora (Bug #720140)

* Fri Jul 22 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-1
- Update to 2.8.5 final
- Drop issue 12307 patch

* Thu Jul 21 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-0.3.rc3
- Update to 2.8.5 RC 3
- Drop upstreamed swig patch
- Apply upstream fix for issue 12307 (bug #723652)

* Mon Jun 20 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-0.2.rc2
- Update to 2.8.5 RC 2
- Add patch from upstream to fix FindSWIG

* Tue May 31 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-0.1.rc1
- Update to 2.8.5 RC 1
- Disable CTestTestUpload test, needs internet access

* Thu Feb 17 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.4-1
- Update to 2.8.4 final

* Wed Feb 2 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.4-0.2.rc2
- Update to 2.8.4 RC 2

* Tue Jan 18 2011 Orion Poplawski <orion@cora.nwra.com> - 2.8.4-0.1.rc1
- Update to 2.8.4 RC 1
- Drop qt4 patch

* Thu Dec 16 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.3-2
- Add patch from upstream git to fix bug 652886 (qt3/qt4 detection)

* Thu Nov 4 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.3-1
- Update to 2.8.3 final

* Mon Nov 1 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.3-0.3.rc4
- Update to 2.8.3 RC 4
- Drop python 2.7 patch fixed upstream
- No need to fixup source file permissions anymore

* Fri Oct 22 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.3-0.2.rc3
- Update to 2.8.3 RC 3

* Thu Sep 16 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.3-0.1.rc1
- Update to 2.8.3 RC 1
- Add BR bzip2-devel and libarchive-devel

* Fri Jul 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.8.2-2
- add support for Python 2.7 to FindPythonLibs.cmake (Orcan Ogetbil)

* Tue Jul 6 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.2-1
- Update to 2.8.2 final

* Thu Jun 24 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.2-0.3.rc4
- Update to 2.8.2 RC 4

* Wed Jun 23 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.2-0.2.rc3
- Update to 2.8.2 RC 3

* Mon Jun 21 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.2-0.1.rc2
- Update to 2.8.2 RC 2

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-5
- Upstream published a newer 2.8.1 tar ball

* Wed Jun 2 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-4
- Add BR gcc-gfortran so Fortran support is built

* Wed Apr 21 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-3
- Disable ModuleNotices test, re-enable parallel ctest

* Tue Mar 30 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-2
- Disable parallel ctest checks for now

* Tue Mar 23 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-1
- Update to 2.8.1 final

* Tue Mar 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.8.1-0.3.rc5
- Own /usr/lib(64)/cmake

* Fri Mar 12 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-0.2.rc5
- Update to 2.8.1 RC 5

* Fri Feb 19 2010 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-0.1.rc3
- Update to 2.8.1 RC 3

* Thu Jan 14 2010 Rex Dieter <rdieter@fedorproject.org> - 2.8.0-2
- macros.cmake: drop -DCMAKE_SKIP_RPATH:BOOL=ON from %%cmake

* Wed Nov 18 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-1
- Update to 2.8.0 final

* Wed Nov 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.8.0-0.8.rc7
- rebuild (for qt-4.6.0-rc1)

* Wed Nov 11 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.7.rc7
- Update to 2.8.0 RC 7

* Tue Nov 10 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.7.rc6
- Update to 2.8.0 RC 6

* Wed Nov 4 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.6.rc5
- Update to 2.8.0 RC 5
- Drop patches fixed upstream

* Fri Oct 30 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.5.rc4
- Update to 2.8.0 RC 4
- Add FindJNI patch
- Add test patch from cvs to fix Fedora build test build error

* Tue Oct 13 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.4.rc3
- Update to 2.8.0 RC 3
- Drop vtk64 patch fixed upstream

* Fri Oct 9 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.3.rc2
- Do out of tree build, needed for ExternalProject test

* Thu Oct 8 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.2.rc2
- Update to 2.8.0 RC 2
- Use parallel ctest in %%check

* Tue Sep 29 2009 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-0.1.rc1
- Update to 2.8.0 RC 1

* Thu Sep 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.6.4-4
- macro.cmake: prefixes cmake with the package being builts bindir (#523878)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 3 2009 Orion Poplawski <orion@cora.nwra.com> - 2.6.4-2
- Add patch to find VTK on 64-bit machines (bug #503945)

* Wed Apr 29 2009 Orion Poplawski <orion@cora.nwra.com> - 2.6.4-1
- Update to 2.6.4
- Drop patch for bug #475876 fixed upstream

* Mon Mar 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.6.3-3
- macros.cmake: +%%_cmake_version

* Mon Mar 09 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.6.3-2
- Fix crash during kdepimlibs build (#475876)

* Mon Feb 23 2009 Orion Poplawski <orion@cora.nwra.com> - 2.6.3-1
- Update to 2.6.3 final

* Tue Feb 17 2009 Orion Poplawski <orion@cora.nwra.com> - 2.6.3-0.4.rc13
- Update to 2.6.3-RC-13

* Tue Jan 13 2009 Orion Poplawski <orion@cora.nwra.com> - 2.6.3-0.3.rc8
- Update to 2.6.3-RC-8

* Sun Jan 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.6.3-0.2.rc5
- macros.cmake: add -DCMAKE_SKIP_RPATH:BOOL=ON
- fix Release tag

* Wed Dec 10 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.3-0.rc5.1
- Update to 2.6.3-RC-5

* Tue Dec 2 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.6.2-3
- Add -DCMAKE_VERBOSE_MAKEFILE=ON to %%cmake (#474053)
- preserve timestamp of macros.cmake
- cosmetics

* Tue Oct 21 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.2-2
- Allow conditional build of gui

* Mon Sep 29 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.2-1
- Update to 2.6.2

* Mon Sep 8 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.2-0.rc3.1
- Update to 2.6.2-RC-2
- Drop parens patch fixed upstream

* Tue Sep 2 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-3
- Drop jni patch, applied upstream.

* Tue Aug 26 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.6.1-2
- attempt to patch logic error, crasher

* Tue Aug 5 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-1
- Update to 2.6.1

* Mon Jul 14 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-0.rc8.1
- Update to 2.6.1-RC-8
- Drop xmlrpc patch fixed upstream

* Tue May 6 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-1
- Update to 2.6.0

* Mon May 5 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-0.rc10.1
- Update to 2.6.0-RC-10

* Thu Apr 24 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-0.rc9.1
- Update to 2.6.0-RC-9

* Fri Apr 11 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-0.rc8.1
- Update to 2.6.0-RC-8

* Thu Apr 3 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-0.rc6.1
- Update to 2.6.0-RC-6

* Fri Mar 28 2008 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-0.rc5.1
- Update to 2.6.0-RC-5
- Add gui sub-package for Qt frontend

* Fri Mar 7 2008 Orion Poplawski <orion@cora.nwra.com> - 2.4.8-3
- Add macro for bootstrapping new release/architecture
- Add %%check section

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4.8-2
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Orion Poplawski <orion@cora.nwra.com> - 2.4.8-1
- Update to 2.4.8

* Wed Jan 16 2008 Orion Poplawski <orion@cora.nwra.com> - 2.4.8-0.rc12
- Update to 2.4.8 RC-12

* Fri Dec 14 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.8-0.rc4
- Update to 2.4.8 RC-4

* Mon Nov 12 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.7-4
- No longer set CMAKE_SKIP_RPATH

* Tue Aug 28 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.7-3
- Rebuild for new expat

* Wed Aug 22 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.7-2
- Rebuild for BuildID

* Mon Jul 23 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.7-1
- Update to 2.4.7

* Fri Jun 29 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.7-0.rc11
- Update to 2.4.7 RC-11

* Wed Jun 27 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.6-4
- Update macros.cmake to add CMAKE_INSTALL_LIBDIR, INCLUDE_INSTALL_DIR,
  LIB_INSTALL_DIR, SYSCONF_INSTALL_DIR, and SHARE_INSTALL_PREFIX

* Mon Apr 16 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.6-3
- Apply patch from upstream CVS to fix .so install permissions (bug #235673)

* Fri Apr 06 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.6-2
- Add rpm macros

* Thu Jan 11 2007 Orion Poplawski <orion@cora.nwra.com> - 2.4.6-1
- Update to 2.4.6

* Mon Dec 18 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.5-2
- Use system libraries (bootstrap --system-libs)

* Tue Dec  5 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.5-1
- Update to 2.4.5

* Tue Nov 21 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.4-1
- Update to 2.4.4

* Tue Oct 31 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-4
- Add /usr/lib/jvm/java to FindJNI search paths

* Tue Aug 29 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-3
- Rebuild for FC6

* Wed Aug  2 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-2
- vim 7.0 now ships cmake files, so don't ship ours (bug #201018)
- Add patch to Linux.cmake for Fortran soname support for plplot

* Tue Aug  1 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-1
- Update to 2.4.3

* Mon Jul 31 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-3
- Update for vim 7.0

* Tue Jul 11 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-2
- Patch FindRuby and FindSWIG to work on Fedora (bug #198103)

* Fri Jun 30 2006 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-1
- Update to 2.4.2

* Thu Apr  6 2006 Orion Poplawski <orion@cora.nwra.com> - 2.2.3-4
- Update for vim 7.0c

* Tue Mar 28 2006 Orion Poplawski <orion@cora.nwra.com> - 2.2.3-3
- No subpackages, just own the emacs and vim dirs.

* Tue Mar 21 2006 Orion Poplawski <orion@cora.nwra.com> - 2.2.3-2
- Add emacs and vim support
- Include Example in docs

* Wed Mar  8 2006 Orion Poplawski <orion@cora.nwra.com> - 2.2.3-1
- Fedora Extras version
