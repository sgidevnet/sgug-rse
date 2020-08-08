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
#%%if 0%%{?rhel} && 0%%{?rhel} < 8
#%%bcond_with python3
#%%else
%bcond_without python3
#%%endif

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
Release:        6%{?relsuf}%{?dist}
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

Source100:      cmake.sgifixbinsh.filelist

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

# For patch creation (I prefer not to have all the /bin/sh changes in the patch)
#exit 1

# Fix up all the references to /bin/sh (and point them to %{_bindir}/sh)
for filetofix in `cat %{SOURCE100}`; do
    perl -pi -e "s|/bin/sh|%{_bindir}/bash|g" ${filetofix}
done

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

# To ensure we pick up the right compiler
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
# Yes, we don't have this
export FC=mips-sgi-irix6.5-gcf
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export CFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS $CFLAGS"
export CXXFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS $CXXFLAGS"
export LDFLAGS="-ldicl-0.1 $LDFLAGS"
export NUM_PARALLEL=`echo -- "%{_smp_mflags}" |perl -pe "s|.*\-j(\\\\d+).*|\\\$1|g"`

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
* Wed Jun 17 2020 Daniel Hams <daniel.hams@gmail.com> - 3.17.2-6
- Update FindZLIB module to hunt first for sgug libz

* Fri May 22 2020 Daniel Hams <daniel.hams@gmail.com> - 3.17.2-5
- Fix minor path issue in __cmake macro (was overriden anyway, but..)

* Sat May 16 2020 Daniel Hams <daniel.hams@gmail.com> - 3.17.2-4
- Avoid using select in ProcessUNIX which causes SIGCHL to fall on the floor and ctest will lock up. Rewrite hardcoded references to /bin/sh to /usr/sgug/bin/bash and link in libdicl for "correctness" of printf.

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
