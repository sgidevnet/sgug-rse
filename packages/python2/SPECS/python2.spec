# ======================================================
# Conditionals and other variables controlling the build
# ======================================================

# Note that the bcond macros are named for the CLI option they create.
# "%%bcond_without" means "ENABLE by default and create a --without option"

# Whether to use RPM build wheels from the python-{pip,setuptools}-wheel package
# Uses upstream bundled prebuilt wheels otherwise
%bcond_with rpmwheels

# Extra build for debugging the interpreter or C-API extensions
# (the -debug subpackages)
%bcond_with debug_build

# Only use this when bootstrapping python3
# Needed to build setuptools for the first time
%bcond_with python3_bootstrap

%global unicode ucs4

%global python python2

%global pybasever 2.7
%global pylibdir %{_libdir}/python%{pybasever}
%global tools_dir %{pylibdir}/Tools
%global demo_dir %{pylibdir}/Demo
%global doc_tools_dir %{pylibdir}/Doc/tools
%global dynload_dir %{pylibdir}/lib-dynload
%global site_packages %{pylibdir}/site-packages

# Python's configure script defines SOVERSION, and this is used in the Makefile
# to determine INSTSONAME, the name of the libpython DSO:
#   LDLIBRARY='libpython$(VERSION).so'
#   INSTSONAME="$LDLIBRARY".$SOVERSION
# We mirror this here in order to make it easier to add the -gdb.py hooks.
# (if these get out of sync, the payload of the libs subpackage will fail
# and halt the build)
%global py_SOVERSION 1.0
%global py_INSTSONAME_optimized libpython%{pybasever}.so.%{py_SOVERSION}
%global py_INSTSONAME_debug     libpython%{pybasever}_d.so.%{py_SOVERSION}

# Disabled for now:
%global with_huntrleaks 0

%global with_gdb_hooks 0

%global with_systemtap 0

# some arches don't have valgrind so we need to disable its support on them
#%%ifnarch s390 %%{mips} riscv64
#%%global with_valgrind 1
#%%else
%global with_valgrind 0
#%%endif

%global with_gdbm 1

%if 0%{?_module_build}
%global with_valgrind 0
%global with_systemtap 0

# (Don't) Run the test suite in %%check
%bcond_with tests
%else
# Run the test suite in %%check
%bcond_without tests
%endif

# Disable automatic bytecompilation. The python2.7 binary is not yet
# available in /usr/bin when Python is built. Also, the bytecompilation fails
# on files that test invalid syntax.
%global __brp_python_bytecompile %{nil}

# We need to get a newer configure generated out of configure.in for the following
# patches:
#   patch 4 (CFLAGS)
#   patch 52 (valgrind)
#   patch 55 (systemtap)
#   patch 145 (linux2)
#
# For patch 55 (systemtap), we need to get a new header for configure to use
#
# configure.in requires autoconf-2.65, but the version in Fedora is currently
# autoconf-2.66
#
# For now, we'll generate a patch to the generated configure script and
# pyconfig.h.in on a machine that has a local copy of autoconf 2.65
#
# Instructions on obtaining such a copy can be seen at
#   http://bugs.python.org/issue7997
#
# To make it easy to regenerate the patch, this specfile can be run in two
# ways:
# (i) regenerate_autotooling_patch  0 : the normal approach: prep the
# source tree using a pre-generated patch to the "configure" script, and do a
# full build
# (ii) regenerate_autotooling_patch 1 : intended to be run on a developer's
# workstation: prep the source tree without patching configure, then rerun a
# local copy of autoconf-2.65, regenerate the patch, then exit, without doing
# the rest of the build
%global regenerate_autotooling_patch 0

# Python 2 is deprecated in Fedora 30+, see:
#   https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
# This means that new packages MUST NOT depend on python2, even transitively
#   see: https://fedoraproject.org/wiki/Packaging:Deprecating_Packages
# Python 2 will not be supported after 2019. Use the python3 package instead
# if possible.
#%%if 0%%{fedora} >= 30
#%%global deprecated Provides: deprecated()
#%%endif


# ==================
# Top-level metadata
# ==================
Summary: An interpreted, interactive, object-oriented programming language
Name: %{python}
URL: https://www.python.org/

# Remember to also rebase python2-docs when changing this:
%global general_version %{pybasever}.18
#global prerel ...
%global upstream_version %{general_version}%{?prerel}
Version: %{general_version}%{?prerel:~%{prerel}}
Release: 3%{?dist}
License: Python
Requires: %{python}-libs%{?_isa} = %{version}-%{release}
Provides: python(abi) = %{pybasever}

%?deprecated

# People might want to dnf install pythonX.Y instead of pythonXY
Provides: python%{pybasever} = %{version}-%{release}


# =======================
# Build-time requirements
# =======================

# (keep this list alphabetized)

BuildRequires: autoconf
#%%if ! 0%%{?_module_build}
#BuildRequires: bluez-libs-devel
#%%endif
BuildRequires: bzip2
BuildRequires: bzip2-devel
#BuildRequires: glibc-all-langpacks
#BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: libdb-devel
BuildRequires: libffi-devel >= 3.2.1-26
BuildRequires: ncurses-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: sqlite-devel
BuildRequires: tcl-devel

BuildRequires: openssl-devel

# For the nis module
#BuildRequires: libnsl2-devel
#BuildRequires: libtirpc-devel

# expat 2.1.0 added the symbol XML_SetHashSalt without bumping SONAME.  We use
# it (in pyexpat) in order to enable the fix in Python-2.7.3 for CVE-2012-0876:
BuildRequires: expat-devel >= 2.1.0

BuildRequires: findutils
BuildRequires: gcc-c++
%if %{with_gdbm}
# ABI change without soname bump, reverted
BuildRequires: gdbm-devel >= 1:1.13
%endif
#%%if ! 0%%{?_module_build}
#BuildRequires: libGL-devel
#BuildRequires: libX11-devel
#%%endif

%if 0%{?with_systemtap}
BuildRequires: systemtap-sdt-devel
# (this introduces a circular dependency, in that systemtap-sdt-devel's
# /usr/bin/dtrace is a python script)
%global tapsetdir      /usr/share/systemtap/tapset
%endif # with_systemtap

BuildRequires: tar
#%%if ! 0%%{?_module_build}
#BuildRequires: tix-devel
#BuildRequires: tk-devel
#%%endif

%if 0%{?with_valgrind}
BuildRequires: valgrind-devel
%endif

BuildRequires: zlib-devel
#BuildRequires: gnupg2

# For %%python_provide
BuildRequires: python-rpm-macros

%if %{with rpmwheels}
BuildRequires: python-setuptools-wheel
BuildRequires: python-pip-wheel
%endif

# Providing python27 as now multiple interpreters exist in Fedora
# alongside the system one e.g. python26, python33 etc
Provides:   python27 = %{version}-%{release}

# Previously, this was required for our rewheel patch to work.
# This is technically no longer needed, but we keep it recommended
# for the developer experience.
Recommends: python2-setuptools
Recommends: python2-pip


# =======================
# Source code and patches
# =======================

Source0: %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz
Source1: %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz.asc
Source2: %{url}static/files/pubkeys.txt

# Systemtap tapset to make it easier to use the systemtap static probes
# (actually a template; LIBRARY_PATH will get fixed up during install)
# Written by dmalcolm; not yet sent upstream
Source3: libpython.stp


# Example systemtap script using the tapset
# Written by wcohen, mjw, dmalcolm; not yet sent upstream
Source4: systemtap-example.stp

# Another example systemtap script that uses the tapset
# Written by dmalcolm; not yet sent upstream
Source5: pyfuntop.stp

Source7: pynche

# Modules/Setup.dist is ultimately used by the "makesetup" script to construct
# the Makefile and config.c
#
# Upstream leaves many things disabled by default, to try to make it easy as
# possible to build the code on as many platforms as possible.
#
# TODO: many modules can also now be built by setup.py after the python binary
# has been built; need to assess if we should instead build things there
#
# We patch it downstream as follows:
#   - various modules are built by default by upstream as static libraries;
#   we built them as shared libraries
#   - build the "readline" module (appears to also be handled by setup.py now)
#   - build the nis module (which needs the tirpc library since glibc 2.26)
#   - enable the build of the following modules:
#     - array arraymodule.c	# array objects
#     - cmath cmathmodule.c # -lm # complex math library functions
#     - math mathmodule.c # -lm # math library functions, e.g. sin()
#     - _struct _struct.c	# binary structure packing/unpacking
#     - time timemodule.c # -lm # time operations and variables
#     - operator operator.c	# operator.add() and similar goodies
#     - _weakref _weakref.c	# basic weak reference support
#     - _testcapi _testcapimodule.c    # Python C API test module
#     - _random _randommodule.c	# Random number generator
#     - _collections _collectionsmodule.c # Container types
#     - itertools itertoolsmodule.c
#     - strop stropmodule.c
#     - _functools _functoolsmodule.c
#     - _bisect _bisectmodule.c	# Bisection algorithms
#     - unicodedata unicodedata.c    # static Unicode character database
#     - _locale _localemodule.c
#     - fcntl fcntlmodule.c	# fcntl(2) and ioctl(2)
#     - spwd spwdmodule.c		# spwd(3)
#     - grp grpmodule.c		# grp(3)
#     - select selectmodule.c	# select(2); not on ancient System V
#     - mmap mmapmodule.c  # Memory-mapped files
#     - _csv _csv.c  # CSV file helper
#     - _socket socketmodule.c  # Socket module helper for socket(2)
#     - _ssl _ssl.c
#     - crypt cryptmodule.c -lcrypt	# crypt(3)
#     - termios termios.c	# Steen Lumholt's termios module
#     - resource resource.c	# Jeremy Hylton's rlimit interface
#     - audioop audioop.c	# Operations on audio samples
#     - imageop imageop.c	# Operations on images
#     - _md5 md5module.c md5.c
#     - _sha shamodule.c
#     - _sha256 sha256module.c
#     - _sha512 sha512module.c
#     - linuxaudiodev linuxaudiodev.c
#     - timing timingmodule.c
#     - _tkinter _tkinter.c tkappinit.c
#     - dl dlmodule.c
#     - gdbm gdbmmodule.c
#     - _bsddb _bsddb.c
#     - binascii binascii.c
#     - parser parsermodule.c
#     - cStringIO cStringIO.c
#     - cPickle cPickle.c
#     - zlib zlibmodule.c
#     - _multibytecodec cjkcodecs/multibytecodec.c
#     - _codecs_cn cjkcodecs/_codecs_cn.c
#     - _codecs_hk cjkcodecs/_codecs_hk.c
#     - _codecs_iso2022 cjkcodecs/_codecs_iso2022.c
#     - _codecs_jp cjkcodecs/_codecs_jp.c
#     - _codecs_kr cjkcodecs/_codecs_kr.c
#     - _codecs_tw cjkcodecs/_codecs_tw.c
Patch0: python-2.7.1-config.patch

# Removes the "-g" option from "pydoc", for some reason; I believe
# (dmalcolm 2010-01-29) that this was introduced in this change:
# - fix pydoc (#68082)
# in 2.2.1-12 as a response to the -g option needing TkInter installed
# (Red Hat Linux 8)
# Not upstream
Patch1: 00001-pydocnogui.patch

# Add $(CFLAGS) to the linker arguments when linking the "python" binary
# since some architectures (sparc64) need this (rhbz:199373).
# Not yet filed upstream
Patch4: python-2.5-cflags.patch

# Work around a bug in Python' gettext module relating to the "Plural-Forms"
# header (rhbz:252136)
# Related to upstream issues:
#   http://bugs.python.org/issue1448060 and http://bugs.python.org/issue1475523
# though the proposed upstream patches are, alas, different
Patch6: python-2.5.1-plural-fix.patch

# This patch was listed in the changelog as:
#  * Fri Sep 14 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-11
#  - fix encoding of sqlite .py files to work around weird encoding problem
#  in Turkish (#283331)
# A traceback attached to rhbz 244016 shows the problem most clearly: a
# traceback on attempting to import the sqlite module, with:
#   "SyntaxError: encoding problem: with BOM (__init__.py, line 1)"
# This seems to come from Parser/tokenizer.c:check_coding_spec
# Our patch changes two source files within sqlite3, removing the
# "coding: ISO-8859-1" specs and character E4 = U+00E4 =
# LATIN SMALL LETTER A WITH DIAERESIS from in ghaering's surname.
#
# It may be that the conversion of "ISO-8859-1" to "iso-8859-1" is thwarted
# by the implementation of "tolower" in the Turkish locale; see:
#   https://bugzilla.redhat.com/show_bug.cgi?id=191096#c9
#
# TODO: Not yet sent upstream, and appears to me (dmalcolm 2010-01-29) that
# it may be papering over a symptom
Patch7: python-2.5.1-sqlite-encoding.patch

# FIXME: Lib/ctypes/util.py posix implementation defines a function
# _get_soname(f).  Upstreams's implementation of this uses objdump to read the
# SONAME from a library; we avoid this, apparently to minimize space
# requirements on the live CD:
# (rhbz:307221)
Patch10: 00010-2.7.13-binutils-no-dep.patch

# Upstream as of Python 2.7.3:
#  Patch11: python-2.7rc1-codec-ascii-tolower.patch

# Add various constants to the socketmodule (rhbz#436560):
# TODO: these patches were added in 2.5.1-22 and 2.5.1-24 but appear not to
# have been sent upstream yet:
Patch13: python-2.7rc1-socketmodule-constants.patch
Patch14: python-2.7rc1-socketmodule-constants2.patch

# Remove an "-rpath $(LIBDIR)" argument from the linkage args in configure.in:
# FIXME: is this for OSF, not Linux?
#Patch16: python-2.6-rpath.patch

# Fixup distutils/unixccompiler.py to remove standard library path from rpath:
# Adapted from Patch0 in ivazquez' python3000 specfile, removing usage of
# super() as it's an old-style class
#Patch17: python-2.6.4-distutils-rpath.patch

# 00055 #
# Systemtap support: add statically-defined probe points
# Patch based on upstream bug: http://bugs.python.org/issue4111
# fixed up by mjw and wcohen for 2.6.2, then fixed up by dmalcolm for 2.6.4
# then rewritten by mjw (attachment 390110 of rhbz 545179), then reformatted
# for 2.7rc1 by dmalcolm:
#Patch55: 00055-systemtap.patch

# Only used when "%%{_lib}" == "lib64"
# Fixup various paths throughout the build and in distutils from "lib" to "lib64",
# and add the /usr/lib64/pythonMAJOR.MINOR/site-packages to sitedirs, in front of
# /usr/lib/pythonMAJOR.MINOR/site-packages
# Not upstream
# DH
#Patch102: 00102-2.7.13-lib64.patch

# Python 2.7 split out much of the path-handling from distutils/sysconfig.py to
# a new sysconfig.py (in r77704).
# We need to make equivalent changes to that new file to ensure that the stdlib
# and platform-specific code go to /usr/lib64 not /usr/lib, on 64-bit archs:
# DH
#Patch103: python-2.7-lib64-sysconfig.patch

# 00104 #
# Only used when "%%{_lib}" == "lib64"
# Another lib64 fix, for distutils/tests/test_install.py; not upstream:
#DH
#Patch104: 00104-lib64-fix-for-test_install.patch

# 00111 #
# Patch the Makefile.pre.in so that the generated Makefile doesn't try to build
# a libpythonMAJOR.MINOR.a (bug 550692):
# Downstream only: not appropriate for upstream
Patch111: 00111-no-static-lib.patch

# 00112 #
# Patch to support building both optimized vs debug stacks DSO ABIs, sharing
# the same .py and .pyc files, using "_d.so" to signify a debug build of an
# extension module.
#
# Based on Debian's patch for the same,
#  http://patch-tracker.debian.org/patch/series/view/python2.6/2.6.5-2/debug-build.dpatch
#
# (which was itself based on the upstream Windows build), but with some
# changes:
#
#   * Debian's patch to dynload_shlib.c looks for module_d.so, then module.so,
# but this can potentially find a module built against the wrong DSO ABI.  We
# instead search for just module_d.so in a debug build
#
#   * We remove this change from configure.in's build of the Makefile:
#   SO=$DEBUG_EXT.so
# so that sysconfig.py:customize_compiler stays with shared_lib_extension='.so'
# on debug builds, so that UnixCCompiler.find_library_file can find system
# libraries (otherwise "make sharedlibs" fails to find system libraries,
# erroneously looking e.g. for "libffi_d.so" rather than "libffi.so")
#
#   * We change Lib/distutils/command/build_ext.py:build_ext.get_ext_filename
# to add the _d there, when building an extension.  This way, "make sharedlibs"
# can build ctypes, by finding the sysmtem libffi.so (rather than failing to
# find "libffi_d.so"), and builds the module as _ctypes_d.so
#
#   * Similarly, update build_ext:get_libraries handling of Py_ENABLE_SHARED by
# appending "_d" to the python library's name for the debug configuration
#
#   * We modify Modules/makesetup to add the "_d" to the generated Makefile
# rules for the various Modules/*.so targets
#
# This may introduce issues when building an extension that links directly
# against another extension (e.g. users of NumPy?), but seems more robust when
# searching for external libraries
#
#   * We don't change Lib/distutils/command/build.py: build.build_purelib to
# embed plat_specifier, leaving it as is, as pure python builds should be
# unaffected by these differences (we'll be sharing the .py and .pyc files)
#
#   * We introduce DEBUG_SUFFIX as well as DEBUG_EXT:
#     - DEBUG_EXT is used by ELF files (names and SONAMEs); it will be "_d" for
# a debug build
#     - DEBUG_SUFFIX is used by filesystem paths; it will be "-debug" for a
# debug build
#
#   Both will be empty in an optimized build.  "_d" contains characters that
# are valid ELF metadata, but this leads to various ugly filesystem paths (such
# as the include path), and DEBUG_SUFFIX allows these paths to have more natural
# names.  Changing this requires changes elsewhere in the distutils code.
#
#   * We add DEBUG_SUFFIX to PYTHON in the Makefile, so that the two
# configurations build parallel-installable binaries with different names
# ("python-debug" vs "python").
#
#   * Similarly, we add DEBUG_SUFFIX within python-config and
#  python$(VERSION)-config, so that the two configuration get different paths
#  for these.
#
#  See also patch 130 below
#
Patch112: 00112-2.7.13-debug-build.patch


# 00113 #
# Add configure-time support for the COUNT_ALLOCS and CALL_PROFILE options
# described at http://svn.python.org/projects/python/trunk/Misc/SpecialBuilds.txt
# so that if they are enabled, they will be in that build's pyconfig.h, so that
# extension modules will reliably use them
# Not yet sent upstream
Patch113: 00113-more-configuration-flags.patch

# 00114 #
# Add flags for statvfs.f_flag to the constant list in posixmodule (i.e. "os")
# (rhbz:553020); partially upstream as http://bugs.python.org/issue7647
# Not yet sent upstream
Patch114: 00114-statvfs-f_flag-constants.patch

# Upstream r79310 removed the "Modules" directory from sys.path when Python is
# running from the build directory on POSIX to fix a unit test (issue #8205).
# This seems to have broken the compileall.py done in "make install": it cannot
# find shared library extension modules at this point in the build (sys.path
# does not contain DESTDIR/usr/lib(64)/python-2.7/lib-dynload for some reason),
# leading to the build failing with:
# Traceback (most recent call last):
#   File "/home/david/rpmbuild/BUILDROOT/python-2.7-0.1.rc2.fc14.x86_64/usr/lib64/python2.7/compileall.py", line 17, in <module>
#     import struct
#   File "/home/david/rpmbuild/BUILDROOT/python-2.7-0.1.rc2.fc14.x86_64/usr/lib64/python2.7/struct.py", line 1, in <module>
#    from _struct import *
# ImportError: No module named _struct
# This patch adds the build Modules directory to build path.
Patch121: 00121-add-Modules-to-build-path.patch

# 2.7.1 (in r84230) added a test to test_abc which fails if python is
# configured with COUNT_ALLOCS, which is the case for our debug build
# (the COUNT_ALLOCS instrumentation keeps "C" alive).
# Not yet sent upstream
Patch128: python-2.7.1-fix_test_abc_with_COUNT_ALLOCS.patch

# 00130 #
# Add "--extension-suffix" option to python-config and python-debug-config
# (rhbz#732808)
#
# This is adapted from 3.2's PEP-3149 support.
#
# Fedora's debug build has some non-standard features (see also patch 112
# above), though largely shared with Debian/Ubuntu and Windows
#
# In particular, SO in the Makefile is currently always just ".so" for our
# python 2 optimized builds, but for python 2 debug it should be '_d.so', to
# distinguish the debug vs optimized ABI, following the pattern in the above
# patch.
#
# Not yet sent upstream
Patch130: python-2.7.2-add-extension-suffix-to-python-config.patch

# 00131 #
# The four tests in test_io built on top of check_interrupted_write_retry
# fail when built in Koji, for ppc and ppc64; for some reason, the SIGALRM
# handlers are never called, and the call to write runs to completion
# (rhbz#732998)
Patch131: 00131-disable-tests-in-test_io.patch

# 00132 #
# Add non-standard hooks to unittest for use in the "check" phase below, when
# running selftests within the build:
#   @unittest._skipInRpmBuild(reason)
# for tests that hang or fail intermittently within the build environment, and:
#   @unittest._expectedFailureInRpmBuild
# for tests that always fail within the build environment
#
# The hooks only take effect if WITHIN_PYTHON_RPM_BUILD is set in the
# environment, which we set manually in the appropriate portion of the "check"
# phase below (and which potentially other python-* rpms could set, to reuse
# these unittest hooks in their own "check" phases)
Patch132: 00132-add-rpmbuild-hooks-to-unittest.patch

# 00133 #
# "dl" is deprecated, and test_dl doesn't work on 64-bit builds:
Patch133: 00133-skip-test_dl.patch

# 00136 #
# Some tests try to seek on sys.stdin, but don't work as expected when run
# within Koji/mock; skip them within the rpm build:
Patch136: 00136-skip-tests-of-seeking-stdin-in-rpmbuild.patch

# 00137 #
# Some tests within distutils fail when run in an rpmbuild:
Patch137: 00137-skip-distutils-tests-that-fail-in-rpmbuild.patch

# 00138 #
# Fixup some tests within distutils to work with how debug builds are set up:
Patch138: 00138-fix-distutils-tests-in-debug-build.patch

# 00139 #
# ARM-specific: skip known failure in test_float:
#  http://bugs.python.org/issue8265 (rhbz#706253)
Patch139: 00139-skip-test_float-known-failure-on-arm.patch

# 00140 #
# Sparc-specific: skip known failure in test_ctypes:
#  http://bugs.python.org/issue8314 (rhbz#711584)
# which appears to be a libffi bug
Patch140: 00140-skip-test_ctypes-known-failure-on-sparc.patch

# 00142 #
# Some pty tests fail when run in mock (rhbz#714627):
Patch142: 00142-skip-failing-pty-tests-in-rpmbuild.patch

# 00143 #
# Fix the --with-tsc option on ppc64, and rework it on 32-bit ppc to avoid
# aliasing violations (rhbz#698726)
# Sent upstream as http://bugs.python.org/issue12872
Patch143: 00143-tsc-on-ppc.patch

# 00144 #
# (Optionally) disable the gdbm module:
Patch144: 00144-no-gdbm.patch

# 00146 #
# Support OpenSSL FIPS mode (e.g. when OPENSSL_FORCE_FIPS_MODE=1 is set)
# - handle failures from OpenSSL (e.g. on attempts to use MD5 in a
#   FIPS-enforcing environment)
# - add a new "usedforsecurity" keyword argument to the various digest
#   algorithms in hashlib so that you can whitelist a callsite with
#   "usedforsecurity=False"
# (sent upstream for python 3 as http://bugs.python.org/issue9216; this is a
# backport to python 2.7; see RHEL6 patch 119)
# - enforce usage of the _hashlib implementation: don't fall back to the _md5
#   and _sha* modules (leading to clearer error messages if fips selftests
#   fail)
# - don't build the _md5 and _sha* modules; rely on the _hashlib implementation
#   of hashlib (for example, md5.py will use _hashlib's implementation of MD5,
#   if permitted by the FIPS setting)
# (rhbz#563986)
Patch146: 00146-hashlib-fips.patch

# 00147 #
# Add a sys._debugmallocstats() function
# Based on patch 202 from RHEL 5's python.spec, with updates from rhbz#737198
# Sent upstream as http://bugs.python.org/issue14785
Patch147: 00147-add-debug-malloc-stats.patch

# 00155 #
# Avoid allocating thunks in ctypes unless absolutely necessary, to avoid
# generating SELinux denials on "import ctypes" and "import uuid" when
# embedding Python within httpd (rhbz#814391)
Patch155: 00155-avoid-ctypes-thunks.patch

# 00156 #
# Recent builds of gdb will only auto-load scripts from certain safe
# locations.  Turn off this protection when running test_gdb in the selftest
# suite to ensure that it can load our -gdb.py script (rhbz#817072):
# Not yet sent upstream
Patch156: 00156-gdb-autoload-safepath.patch

# 00165 #
# Backport to Python 2 from Python 3.3 of improvements to the "crypt" module
# adding precanned ways of salting a password (rhbz#835021)
# Based on r88500 patch to py3k from Python 3.3
# plus 6482dd1c11ed, 0586c699d467, 62994662676a, 74a1110a3b50, plus edits
# to docstrings to note that this additional functionality is not standard
# within 2.7
Patch165: 00165-crypt-module-salt-backport.patch

# 00167 #
# Don't run any of the stack navigation tests in test_gdb when Python is
# optimized, since there appear to be many different ways in which gdb can
# fail to read the PyFrameObject* for arbitrary places in the callstack,
# presumably due to compiler optimization (rhbz#912025)
#
# Not yet sent upstream
Patch167: 00167-disable-stack-navigation-tests-when-optimized-in-test_gdb.patch

# 00169 #
# Use SHA-256 rather than implicitly using MD5 within the challenge handling
# in multiprocessing.connection
#
# Sent upstream as http://bugs.python.org/issue17258
# (rhbz#879695)
Patch169: 00169-avoid-implicit-usage-of-md5-in-multiprocessing.patch

# 00170 #
# In debug builds, try to print repr() when a C-level assert fails in the
# garbage collector (typically indicating a reference-counting error
# somewhere else e.g in an extension module)
# Backported to 2.7 from a patch I sent upstream for py3k
#   http://bugs.python.org/issue9263  (rhbz#614680)
# hiding the proposed new macros/functions within gcmodule.c to avoid exposing
# them within the extension API.
# (rhbz#850013)
Patch170: 00170-gc-assertions.patch

# 00174 #
# Workaround for failure to set up prefix/exec_prefix when running
# an embededed libpython that sets Py_SetProgramName() to a name not
# on $PATH when run from the root directory due to
#   https://fedoraproject.org/wiki/Features/UsrMove
# e.g. cmpi-bindings under systemd (rhbz#817554):
Patch174: 00174-fix-for-usr-move.patch

# 00180 #
# Enable building on ppc64p7
# Not appropriate for upstream, Fedora-specific naming
Patch180: 00180-python-add-support-for-ppc64p7.patch

# 00181 #
# Allow arbitrary timeout for Condition.wait, as reported in
# https://bugzilla.redhat.com/show_bug.cgi?id=917709
# Upstream doesn't want this: http://bugs.python.org/issue17748
# But we have no better solution downstream yet, and since there is
# no API breakage, we apply this patch.
# Doesn't apply to Python 3, where this is fixed otherwise and works.
Patch181: 00181-allow-arbitrary-timeout-in-condition-wait.patch

# 00185 #
# Makes urllib2 honor "no_proxy" enviroment variable for "ftp:" URLs
# when ftp_proxy is set
Patch185: 00185-urllib2-honors-noproxy-for-ftp.patch

# 00187 #
# Add an explicit RPATH to pyexpat.so pointing at the directory
# containing the system expat (which has the extra XML_SetHashSalt
# symbol), to avoid an ImportError with a link error if there's an
# LD_LIBRARY_PATH containing a "vanilla" build of expat (without the
# symbol)
#Patch187: 00187-add-RPATH-to-pyexpat.patch

# 00189 #
# Instead of bundled wheels, use our RPM packaged wheels from
# /usr/share/python-wheels
Patch189: 00189-use-rpm-wheels.patch

# 00191 #
# Disabling NOOP test as it fails without internet connection
Patch191: 00191-disable-NOOP.patch

# 00193 #
# Enable loading sqlite extensions. This patch isn't needed for
# python3.spec, since Python 3 has a configuration option for this.
# rhbz#1066708
# Patch provided by John C. Peterson
Patch193: 00193-enable-loading-sqlite-extensions.patch

# 00289 #
# Disable automatic detection for the nis module
# (we handle it it in Setup.dist, see Patch0)
Patch289: 00289-disable-nis-detection.patch

# (New patches go here ^^^)
#
# When adding new patches to "python2" and "python3" in Fedora, EL, etc.,
# please try to keep the patch numbers in-sync between all specfiles.
#
# More information, and a patch number catalog, is at:
#
#     https://fedoraproject.org/wiki/SIGs/Python/PythonPatches

# This is the generated patch to "configure"; see the description of
#   %%{regenerate_autotooling_patch}
# above:

# Disable tk for modularity builds to break up build dependencies
Patch04000: 04000-modularity-disable-tk.patch

Patch5000: 05000-autotool-intermediates.patch

Patch9000: python2.sgifixes.patch
#Patch9000: python2.sgifixes2.patch

# ======================================================
# Additional metadata, and subpackages
# ======================================================

%description
Python 2 is an old version of the language that is incompatible with the 3.x
line of releases. The language is mostly the same, but many details, especially
how built-in objects like dictionaries and strings work, have changed
considerably, and a lot of deprecated features have finally been removed in the
3.x line.

Note that documentation for Python 2 is provided in the python2-docs
package.

This package provides the "python2" executable; most of the actual
implementation is within the "python2-libs" package.


%package libs
Summary: Runtime libraries for Python 2
%?deprecated

# Needed for ctypes, to load libraries, worked around for Live CDs size
# Requires: binutils

# expat 2.1.0 added the symbol XML_SetHashSalt without bumping SONAME.  We use
# this symbol (in pyexpat), so we must explicitly state this dependency to
# prevent "import pyexpat" from failing with a linker error if someone hasn't
# yet upgraded expat:
Requires: expat >= 2.1.0

# Python built with glibc >= 2.24.90-26 needs to require it (rhbz#1410644).
#Requires: glibc%%{?_isa} >= 2.24.90-26

%if %{with_gdbm}
# ABI change without soname bump, reverted
Requires: gdbm%{?_isa} >= 1:1.13
%endif

%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python2-pip) = 19.2.3
Provides: bundled(python2-setuptools) = 41.2.0
%endif

%{?python_provide:%python_provide python2-libs}
%{?python_provide:%python_provide python2-libs%{?_isa}}

%description libs
This package contains files used to embed Python 2 into applications.

%package devel
Summary: Libraries and header files needed for Python 2 development
%?deprecated

Requires: %{python}%{?_isa} = %{version}-%{release}
Requires: python-rpm-macros
Requires: python2-rpm-macros
Requires: pkgconfig

%if %{without python3_bootstrap}
# When bootstrapping python3, we need to build setuptools
# But setuptools BR python2-devel and that brings in python3-rpm-generators
# python3-rpm-generators needs python3-setuptools, so we cannot have it yet
BuildRequires: python3-rpm-generators
Requires: python3-rpm-generators
%endif

# This is not "API" (packages that need setuptools should still BuildRequire it)
# However some packages apparently can build both with and without setuptools
# producing egg-info as file or directory (depending on setuptools presence).
# Directory-to-file updates are problematic in RPM, so we ensure setuptools is
# installed when -devel is required.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1623922
# See https://fedoraproject.org/wiki/Packaging:Directory_Replacement
Requires: python2-setuptools

# https://bugzilla.redhat.com/show_bug.cgi?id=1217376
# https://bugzilla.redhat.com/show_bug.cgi?id=1496757
# https://bugzilla.redhat.com/show_bug.cgi?id=1218294
# TODO change to a specific subpackage once available (#1218294)
Requires: sgug-rpm-config

# Needed here because of the migration of Makefile from -devel to the main
# package
Conflicts: %{python} < %{version}-%{release}

%{?python_provide:%python_provide python2-devel}
%{?python_provide:%python_provide python2-devel%{?_isa}}

%description devel
This package contains libraries and header files used to build applications
with and native libraries for Python 2

%package tools
Summary: A collection of development tools included with Python 2
%?deprecated

Requires: %{name} = %{version}-%{release}
Requires: %{python}-tkinter = %{version}-%{release}

%{?python_provide:%python_provide python2-tools}
%{?python_provide:%python_provide python2-tools%{?_isa}}

%description tools
This package includes several tools to help with the development of Python 2
programs, including IDLE (an IDE with editing and debugging facilities), a
color editor (pynche), and a python gettext program (pygettext.py).

%package tkinter
Summary: A graphical user interface for the Python 2 scripting language
%?deprecated

Requires: %{name} = %{version}-%{release}

%if 0%{?fedora} < 31
Provides: tkinter = %{version}-%{release}
Provides: tkinter%{?_isa} = %{version}-%{release}
Provides: tkinter2 = %{version}-%{release}
Provides: tkinter2%{?_isa} = %{version}-%{release}
%endif
%{?python_provide:%python_provide python2-tkinter}
%{?python_provide:%python_provide python2-tkinter%{?_isa}}

%description tkinter

The Tkinter (Tk interface) program is an graphical user interface for
the Python 2 scripting language.

You should install the python2tkinter package if you'd like to use a graphical
user interface for Python 2 programming.

%package test
Summary: The test modules from the main python2 package
%?deprecated

Requires: %{name} = %{version}-%{release}

%{?python_provide:%python_provide python2-test}
%{?python_provide:%python_provide python2-test%{?_isa}}

%description test

The test modules from the main python2 package: %{name}
These have been removed to save space, as they are never or almost
never used in production.

You might want to install the python2-test package if you're developing python 2
code that uses more than just unittest and/or test.support.

%if %{with debug_build}
%package debug
Summary: Debug version of the Python 2 runtime
%?deprecated

# The debug build is an all-in-one package version of the regular build, and
# shares the same .py/.pyc files and directories as the regular build.  Hence
# we depend on all of the subpackages of the regular build:
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-test%{?_isa} = %{version}-%{release}
Requires: %{python}-tkinter%{?_isa} = %{version}-%{release}
Requires: %{name}-tools%{?_isa} = %{version}-%{release}

%{?python_provide:%python_provide python2-debug}
%{?python_provide:%python_provide python2-debug%{?_isa}}

%description debug
python2-debug provides a version of the Python 2 runtime with numerous debugging
features enabled, aimed at advanced Python users, such as developers of Python
extension modules.

This version uses more memory and will be slower than the regular Python 2 build,
but is useful for tracking down reference-counting issues, and other bugs.

The bytecodes are unchanged, so that .pyc files are compatible between the two
version of Python 2, but the debugging features mean that C/C++ extension modules
are ABI-incompatible with those built for the standard runtime.

It shares installation directories with the standard Python 2 runtime, so that
.py and .pyc files can be shared.  All compiled extension modules gain a "_d"
suffix ("foo_d.so" rather than "foo.so") so that each Python 2 implementation can
load its own extensions.
%endif # with debug_build


# ======================================================
# The prep phase of the build:
# ======================================================

%prep
#%%gpgverify -k2 -s1 -d0
%setup -q -n Python-%{upstream_version}

%if 0%{?with_systemtap}
# Provide an example of usage of the tapset:
cp -a %{SOURCE4} .
cp -a %{SOURCE5} .
%endif # with_systemtap

# Ensure that we're using the system copy of various libraries, rather than
# copies shipped by upstream in the tarball:
#   Remove embedded copy of expat:
rm -r Modules/expat || exit 1

#   Remove embedded copy of libffi:
for SUBDIR in darwin libffi libffi_arm_wince libffi_msvc libffi_osx ; do
  rm -r Modules/_ctypes/$SUBDIR || exit 1 ;
done

#   Remove embedded copy of zlib:
rm -r Modules/zlib || exit 1

## Disabling hashlib patch for now as it needs to be reimplemented
## for OpenSSL 1.1.0.
# Don't build upstream Python's implementation of these crypto algorithms;
# instead rely on _hashlib and OpenSSL.
#
# For example, in our builds md5.py uses always uses hashlib.md5 (rather than
# falling back to _md5 when hashlib.md5 is not available); hashlib.md5 is
# implemented within _hashlib via OpenSSL (and thus respects FIPS mode)
#for f in md5module.c md5.c shamodule.c sha256module.c sha512module.c; do
#    rm Modules/$f
#done

#
# Apply patches:
#
%patch0 -p1 -b .rhconfig
%patch1 -p1 -b .no_gui
%patch4 -p1 -b .cflags
%patch6 -p1 -b .plural
%patch7 -p1

#if "%{_lib}" == "lib32"
#patch102 -p1 -b .lib64
#patch103 -p1 -b .lib64-sysconfig
#patch104 -p1
#endif

%patch10 -p1 -b .binutils-no-dep
%patch13 -p1 -b .socketmodule
%patch14 -p1 -b .socketmodule2
#patch16 -p1 -b .rpath
#patch17 -p1 -b .distutils-rpath

%if 0%{?with_systemtap}
%patch55 -p1 -b .systemtap
%endif

%patch111 -p1 -b .no-static-lib

%patch112 -p1 -b .debug-build

%patch113 -p1 -b .more-configuration-flags

%patch114 -p1 -b .statvfs-f-flag-constants


%patch121 -p1
%patch128 -p1

%patch130 -p1

%ifarch ppc %{power64}
%patch131 -p1
%endif

%patch132 -p1
%patch133 -p1
%patch136 -p1 -b .stdin-test
%patch137 -p1
%patch138 -p1
%ifarch %{arm}
%patch139 -p1
%endif
%ifarch %{sparc}
%patch140 -p1
%endif
%patch142 -p1 -b .tty-fail
%patch143 -p1 -b .tsc-on-ppc
%if !%{with_gdbm}
%patch144 -p1
%endif
#patch146 -p1
%patch147 -p1
%patch155 -p1
%patch156 -p1
%patch165 -p1
mv Modules/cryptmodule.c Modules/_cryptmodule.c
%patch167 -p1
%patch169 -p1
%patch170 -p1
%patch174 -p1 -b .fix-for-usr-move
%patch180 -p1
%patch181 -p1
%patch185 -p1
#patch187 -p1

%if %{with rpmwheels}
%patch189 -p1
rm Lib/ensurepip/_bundled/*.whl
%endif

%patch191 -p1
%patch193 -p1
%patch289 -p1

%if 0%{?_module_build}
%patch4000 -p1
%endif

%patch9000 -p1

# For sgug patch regeneration
#exit 1

# This shouldn't be necesarry, but is right now (2.2a3)
find -name "*~" |xargs rm -f

#%%if ! 0%{regenerate_autotooling_patch}
## Normally we apply the patch to "configure"
## We don't apply the patch if we're working towards regenerating it
#%%patch5000 -p0 -b .autotool-intermediates
#%%endif


# ======================================================
# Configuring and building the code:
# ======================================================

%build
topdir=$(pwd)
#export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
#export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CFLAGS="$RPM_OPT_FLAGS -D_SGI_SOURCE -fPIC -fwrapv"
export CXXFLAGS="$RPM_OPT_FLAGS -D_SGI_SOURCE -fPIC -fwrapv"
export CPPFLAGS="$(pkg-config --cflags-only-I libffi)"
#export OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export OPT="$RPM_OPT_FLAGS -D_SGI_SOURCE -fPIC -fwrapv"
#export LINKCC="gcc"
export LINKCC="mips-sgi-irix6.5-gcc"
export LDFLAGS="$RPM_LD_FLAGS"
if pkg-config openssl ; then
  export CFLAGS="$CFLAGS $(pkg-config --cflags openssl)"
  export LDFLAGS="$LDFLAGS $(pkg-config --libs-only-L openssl)"
fi
# Force CC
#export CC=gcc
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++

#exit 1

%if 0%{regenerate_autotooling_patch}
# If enabled, this code regenerates the patch to "configure", using a
# local copy of autoconf-2.65, then exits the build
#
# The following assumes that the copy is installed to ~/autoconf-2.65/bin
# as per these instructions:
#   http://bugs.python.org/issue7997

for f in pyconfig.h.in configure ; do
    cp $f $f.autotool-intermediates ;
done

# Rerun the autotools:
PATH=~/autoconf-2.65/bin:$PATH autoconf
autoheader

# Regenerate the patch:
gendiff . .autotool-intermediates > %{PATCH5000}


# Exit the build
exit 1
%endif

# DH 
autoreconf -fi
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" configure

# Define a function, for how to perform a "build" of python for a given
# configuration:
BuildPython() {
  ConfName=$1
  BinaryName=$2
  SymlinkName=$3
  ExtraConfigArgs=$4
  PathFixWithThisBinary=$5

  ConfDir=build/$ConfName

  echo STARTING: BUILD OF PYTHON FOR CONFIGURATION: $ConfName - %{_bindir}/$BinaryName
  mkdir -p $ConfDir

  export PREV_WD=`pwd`
  cd $ConfDir

  # Use the freshly created "configure" script, but in the directory two above:
  %global _configure $topdir/configure

%configure \
  --enable-shared \
  --enable-unicode=%{unicode} \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-system-expat \
  --with-system-ffi \
%if 0%{?with_systemtap}
  --with-dtrace \
  --with-tapset-install-dir=%{tapsetdir} \
%endif
%if 0%{?with_valgrind}
  --with-valgrind \
%endif
  $ExtraConfigArgs \
  %{nil}

#  --enable-ipv6 \
#

make EXTRA_CFLAGS="$CFLAGS" %{?_smp_mflags}

# We need to fix shebang lines across the full source tree.
#
# We do this using the pathfix.py script, which requires one of the
# freshly-built Python binaries.
#
# We use the optimized python binary, and make the shebangs point at that same
# optimized python binary:
if $PathFixWithThisBinary
then
  # pathfix.py currently only works with files matching ^[a-zA-Z0-9_]+\.py$
  # when crawling through directories, so we handle the special cases manually
  LD_LIBRARYN32_PATH="$topdir/$ConfDir" ./$BinaryName \
    $topdir/Tools/scripts/pathfix.py \
      -i "%{_bindir}/python%{pybasever}" \
      $topdir \
      $topdir/Tools/pynche/pynche \
      $topdir/Demo/pdist/{rcvs,rcsbump,rrcs} \
      $topdir/Demo/scripts/find-uname.py \
      $topdir/Tools/scripts/reindent-rst.py
fi

# Rebuild with new python
# We need a link to a versioned python in the build directory
ln -s $BinaryName $SymlinkName
LD_LIBRARYN32_PATH="$topdir/$ConfDir" PATH=$PATH:$topdir/$ConfDir make -s EXTRA_CFLAGS="$CFLAGS" %{?_smp_mflags}

  cd $PREV_WD
  echo FINISHED: BUILD OF PYTHON FOR CONFIGURATION: $ConfDir
}

# Use "BuildPython" to support building with different configurations:

%if %{with debug_build}
BuildPython debug \
  python-debug \
  python%{pybasever}-debug \
%ifarch %{ix86} x86_64 ppc %{power64}
  "--with-pydebug --with-tsc --with-count-allocs --with-call-profile" \
%else
  "--with-pydebug --with-count-allocs --with-call-profile" \
%endif
  false
%endif # with debug_build

BuildPython optimized \
  python \
  python%{pybasever} \
%ifarch %{ix86} x86_64
  "--enable-optimizations" \
%else
  "" \
%endif
  true


# ======================================================
# Installing the built code:
# ======================================================

%install
topdir=$(pwd)
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix} %{buildroot}%{_mandir}

# Clean up patched .py files that are saved as .lib64
for f in distutils/command/install distutils/sysconfig; do
    rm -f Lib/$f.py.lib64
done

InstallPython() {

  ConfName=$1
  BinaryName=$2
  PyInstSoName=$3

  ConfDir=build/$ConfName

  echo STARTING: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName - %{_bindir}/$BinaryName
  mkdir -p $ConfDir

  export PREV_WD=`pwd`
  cd $ConfDir

make install DESTDIR=%{buildroot}

# We install a collection of hooks for gdb that make it easier to debug
# executables linked against libpython (such as /usr/lib/python itself)
#
# These hooks are implemented in Python itself
#
# gdb-archer looks for them in the same path as the ELF file, with a -gdb.py suffix.
# We put them in the debuginfo package by installing them to e.g.:
#  /usr/lib/debug/usr/lib/libpython2.6.so.1.0.debug-gdb.py
# (note that the debug path is /usr/lib/debug for both 32/64 bit)
#
# See https://fedoraproject.org/wiki/Features/EasierPythonDebugging for more
# information
#
# Initially I tried:
#  /usr/lib/libpython2.6.so.1.0-gdb.py
# but doing so generated noise when ldconfig was rerun (rhbz:562980)
#
%if 0%{?with_gdb_hooks}
DirHoldingGdbPy=%{_usr}/lib/debug/%{_libdir}
PathOfGdbPy=$DirHoldingGdbPy/$PyInstSoName-%{version}-%{release}.%{_arch}.debug-gdb.py

mkdir -p %{buildroot}$DirHoldingGdbPy
cp $topdir/Tools/gdb/libpython.py %{buildroot}$PathOfGdbPy

# Manually byte-compile the file, in case find-debuginfo.sh is run before
# brp-python-bytecompile, so that the .pyc/.pyo files are properly listed in
# the debuginfo manifest:
LD_LIBRARYN32_PATH="$topdir/$ConfDir" $topdir/$ConfDir/$BinaryName \
  -c "import compileall; import sys; compileall.compile_dir('%{buildroot}$DirHoldingGdbPy', ddir='$DirHoldingGdbPy')"

LD_LIBRARYN32_PATH="$topdir/$ConfDir" $topdir/$ConfDir/$BinaryName -O \
  -c "import compileall; import sys; compileall.compile_dir('%{buildroot}$DirHoldingGdbPy', ddir='$DirHoldingGdbPy')"
%endif # with_gdb_hooks

  cd $PREV_WD

  echo FINISHED: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName
}

# Use "InstallPython" to support building with different configurations:

# Install the "debug" build first, so that we can move some files aside
%if %{with debug_build}
InstallPython debug \
  python%{pybasever}-debug \
  %{py_INSTSONAME_debug}
%endif # with debug_build

# Now the optimized build:
InstallPython optimized \
  python%{pybasever} \
  %{py_INSTSONAME_optimized}


# Fix the interpreter path in binaries installed by distutils
# (which changes them by itself)
# Make sure we preserve the file permissions
for fixed in %{buildroot}%{_bindir}/pydoc; do
    sed 's,#!.*/python$,#!/usr/bin/env python%{pybasever},' $fixed > $fixed- \
        && cat $fixed- > $fixed && rm -f $fixed-
done

# Junk, no point in putting in -test sub-pkg
rm -f %{buildroot}/%{pylibdir}/idlelib/testcode.py*

# don't include tests that are run at build time in the package
# This is documented, and used: rhbz#387401
if /bin/false; then
 # Move this to -test subpackage.
mkdir save_bits_of_test
for i in test_support.py __init__.py; do
  cp -a %{buildroot}/%{pylibdir}/test/$i save_bits_of_test
done
rm -rf %{buildroot}/%{pylibdir}/test
mkdir %{buildroot}/%{pylibdir}/test
cp -a save_bits_of_test/* %{buildroot}/%{pylibdir}/test
fi

# tools

mkdir -p ${RPM_BUILD_ROOT}%{site_packages}

#pynche
install -p -m755 %{SOURCE7} ${RPM_BUILD_ROOT}%{_bindir}/pynche
chmod 755 ${RPM_BUILD_ROOT}%{_bindir}/pynche
rm -f Tools/pynche/*.pyw
cp -rp Tools/pynche \
  ${RPM_BUILD_ROOT}%{site_packages}/

cp Tools/pynche/README Tools/pynche/README.pynche

#gettext
install -m755  Tools/i18n/pygettext.py %{buildroot}%{_bindir}/
install -m755  Tools/i18n/msgfmt.py %{buildroot}%{_bindir}/

# Useful development tools
install -m755 -d %{buildroot}%{tools_dir}/scripts
install Tools/README %{buildroot}%{tools_dir}/
install Tools/scripts/*py %{buildroot}%{tools_dir}/scripts/

# Documentation tools
install -m755 -d %{buildroot}%{doc_tools_dir}
#install -m755 Doc/tools/mkhowto %{buildroot}%{doc_tools_dir}

# Useful demo scripts
install -m755 -d %{buildroot}%{demo_dir}
cp -ar Demo/* %{buildroot}%{demo_dir}

# Get rid of crap
find %{buildroot}/ -name "*~"|xargs rm -f
find %{buildroot}/ -name ".cvsignore"|xargs rm -f
find %{buildroot}/ -name "*.bat"|xargs rm -f
find . -name "*~"|xargs rm -f
find . -name ".cvsignore"|xargs rm -f


# Provide binaries in the form of bin2 and bin2.7, thus implementing
# (and expanding) the recommendations of PEP 394.
# Do NOT provide unversioned binaries
# https://fedoraproject.org/wiki/Changes/Python_means_Python3
mv %{buildroot}%{_bindir}/idle %{buildroot}%{_bindir}/idle%{pybasever}
ln -s ./idle%{pybasever} %{buildroot}%{_bindir}/idle2

mv %{buildroot}%{_bindir}/pynche %{buildroot}%{_bindir}/pynche%{pybasever}
ln -s ./pynche%{pybasever} %{buildroot}%{_bindir}/pynche2

mv %{buildroot}%{_bindir}/pydoc %{buildroot}%{_bindir}/pydoc%{pybasever}
ln -s ./pydoc%{pybasever} %{buildroot}%{_bindir}/pydoc2

mv %{buildroot}%{_bindir}/pygettext.py %{buildroot}%{_bindir}/pygettext%{pybasever}.py
ln -s ./pygettext%{pybasever}.py %{buildroot}%{_bindir}/pygettext2.py

mv %{buildroot}%{_bindir}/msgfmt.py %{buildroot}%{_bindir}/msgfmt%{pybasever}.py
ln -s ./msgfmt%{pybasever}.py %{buildroot}%{_bindir}/msgfmt2.py

mv %{buildroot}%{_bindir}/smtpd.py %{buildroot}%{_bindir}/smtpd%{pybasever}.py
ln -s ./smtpd%{pybasever}.py %{buildroot}%{_bindir}/smtpd2.py

# Fix for bug #136654
rm -f %{buildroot}%{pylibdir}/email/test/data/audiotest.au %{buildroot}%{pylibdir}/test/audiotest.au

# Fix bug #143667: python should own /usr/lib/python2.x on 64-bit machines
%if "%{_lib}" == "lib32"
install -d %{buildroot}/%{_prefix}/%{_lib}/python%{pybasever}/site-packages
%endif

# Don't do this multilib dance for irix
## Make python-devel multilib-ready (bug #192747, #139911)
# %%global _pyconfig32_h pyconfig-32.h
# %%global _pyconfig64_h pyconfig-64.h
#
# %%ifarch %%{power64} s390x x86_64 ia64 alpha sparc64 aarch64 %%{mips64} riscv64
# %%global _pyconfig_h %%{_pyconfig64_h}
# %%else
# %%global _pyconfig_h %%{_pyconfig32_h}
# %%endif
#
# %%if %%{with debug_build}
# %%global PyIncludeDirs python%%{pybasever} python%%{pybasever}-debug
# %%else
# %%global PyIncludeDirs python%%{pybasever}
# %%endif
#
# for PyIncludeDir in %{PyIncludeDirs} ; do
#   mv %%{buildroot}%%{_includedir}/$PyIncludeDir/pyconfig.h \
#      %%{buildroot}%%{_includedir}/$PyIncludeDir/%%{_pyconfig_h}
#   cat > %%{buildroot}%%{_includedir}/$PyIncludeDir/pyconfig.h << EOF
# #include <bits/wordsize.h>
#
# #if __WORDSIZE == 32
# #include "%%{_pyconfig32_h}"
# #elif __WORDSIZE == 64
# #include "%%{_pyconfig64_h}"
# #else
# #error "Unknown word size"
# #endif
# EOF
# done
%global _pyconfig_h pyconfig.h

ln -s ../../libpython%{pybasever}.so %{buildroot}%{pylibdir}/config/libpython%{pybasever}.so

# Fix for bug 201434: make sure distutils looks at the right pyconfig.h file
# Similar for sysconfig: sysconfig.get_config_h_filename tries to locate
# pyconfig.h so it can be parsed, and needs to do this at runtime in site.py
# when python starts up.
#
# Split this out so it goes directly to the pyconfig-32.h/pyconfig-64.h
# variants:
#sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" \
#  %{buildroot}%{pylibdir}/distutils/sysconfig.py \
#  %{buildroot}%{pylibdir}/sysconfig.py

# Ensure that the curses module was linked against libncursesw.so, rather than
# libncurses.so (bug 539917)
ldd %{buildroot}/%{dynload_dir}/_curses*.so \
    | grep curses \
    | grep libncurses.so && (echo "_curses.so linked against libncurses.so" ; exit 1)

# Ensure that the debug modules are linked against the debug libpython, and
# likewise for the optimized modules and libpython:
for Module in %{buildroot}/%{dynload_dir}/*.so ; do
    case $Module in
    *_d.so)
        ldd $Module | grep %{py_INSTSONAME_optimized} &&
            (echo Debug module $Module linked against optimized %{py_INSTSONAME_optimized} ; exit 1)

        ;;
    *)
        ldd $Module | grep %{py_INSTSONAME_debug} &&
            (echo Optimized module $Module linked against debug %{py_INSTSONAME_optimized} ; exit 1)
        ;;
    esac
done

#
# Systemtap hooks:
#
%if 0%{?with_systemtap}
# Install a tapset for this libpython into tapsetdir, fixing up the path to the
# library:
mkdir -p %{buildroot}%{tapsetdir}
%ifarch %{power64} s390x x86_64 ia64 alpha sparc64 aarch64 %{mips64}
%global libpython_stp_optimized libpython%{pybasever}-64.stp
%global libpython_stp_debug     libpython%{pybasever}-debug-64.stp
%else
%global libpython_stp_optimized libpython%{pybasever}-32.stp
%global libpython_stp_debug     libpython%{pybasever}-debug-32.stp
%endif

sed \
   -e "s|LIBRARY_PATH|%{_libdir}/%{py_INSTSONAME_optimized}|" \
   %{SOURCE3} \
   > %{buildroot}%{tapsetdir}/%{libpython_stp_optimized}

%if %{with debug_build}
sed \
   -e "s|LIBRARY_PATH|%{_libdir}/%{py_INSTSONAME_debug}|" \
   %{SOURCE3} \
   > %{buildroot}%{tapsetdir}/%{libpython_stp_debug}
%endif # with debug_build
%endif # with_systemtap

# Do bytecompilation with the newly installed interpreter.
# compile *.pyo
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARYN32_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2]) for f in sys.argv[1:]]' || :
# compile *.pyc
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARYN32_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2]) for f in sys.argv[1:]]' || :


# Make library-files user writable
/usr/bin/chmod 755 %{buildroot}%{dynload_dir}/*.so
/usr/bin/chmod 755 %{buildroot}%{_libdir}/libpython%{pybasever}.so.1.0
%if %{with debug_build}
/usr/bin/chmod 755 %{buildroot}%{_libdir}/libpython%{pybasever}_d.so.1.0
%endif

# Remove pyc/pyo files from /usr/bin
# They are not needed, and due to them, the resulting RPM is not multilib-clean
# https://bugzilla.redhat.com/show_bug.cgi?id=1703575
rm %{buildroot}%{_bindir}/*.py{c,o}

# Remove all remaining unversioned commands
# https://fedoraproject.org/wiki/Changes/Python_means_Python3
rm %{buildroot}%{_bindir}/python
rm %{buildroot}%{_bindir}/python-config
rm %{buildroot}%{_mandir}/*/python.1*
rm %{buildroot}%{_libdir}/pkgconfig/python.pc
%if %{with debug_build}
rm %{buildroot}%{_bindir}/python-debug
rm %{buildroot}%{_bindir}/python-debug-config
rm %{buildroot}%{_libdir}/pkgconfig/python-debug.pc
%endif


# ======================================================
# Running the upstream test suite
# ======================================================

%check
topdir=$(pwd)
CheckPython() {
  ConfName=$1
  BinaryName=$2
  ConfDir=$(pwd)/build/$ConfName

  export OPENSSL_CONF=/non-existing-file

  echo STARTING: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName

  # Note that we're running the tests using the version of the code in the
  # builddir, not in the buildroot.

  export PREV_PWD=`pwd`
  cd $ConfDir

  EXTRATESTOPTS="--verbose"

%ifarch s390 s390x %{power64} %{arm} aarch64 %{mips}
    EXTRATESTOPTS="$EXTRATESTOPTS -x test_gdb"
%endif
%ifarch %{mips64}
    EXTRATESTOPTS="$EXTRATESTOPTS -x test_ctypes"
%endif

%if 0%{?with_huntrleaks}
  # Try to detect reference leaks on debug builds.  By default this means
  # running every test 10 times (6 to stabilize, then 4 to watch):
  if [ "$ConfName" = "debug"  ] ; then
    EXTRATESTOPTS="$EXTRATESTOPTS --huntrleaks : "
  fi
%endif

  # Run the upstream test suite, setting "WITHIN_PYTHON_RPM_BUILD" so that the
  # our non-standard decorators take effect on the relevant tests:
  #   @unittest._skipInRpmBuild(reason)
  #   @unittest._expectedFailureInRpmBuild
  WITHIN_PYTHON_RPM_BUILD= EXTRATESTOPTS="$EXTRATESTOPTS" make test

  cd $PREV_WD

  echo FINISHED: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName

}

%if %{with tests}

# no locale coercion in python2
# test_ssl:test_load_dh_params shutil.copies into unicode filename
export LC_ALL=C.utf-8

# Check each of the configurations:
%if %{with debug_build}
CheckPython \
  debug \
  python%{pybasever}-debug
%endif # with debug_build
CheckPython \
  optimized \
  python%{pybasever}

%endif # with tests


# ======================================================
# Cleaning up
# ======================================================


%files
%doc README
%{_bindir}/pydoc2*
%{_bindir}/%{python}
%{_bindir}/python%{pybasever}
%{_mandir}/*/python2*

%files libs
%doc README
%license %{pylibdir}/LICENSE.txt
%dir %{pylibdir}
%dir %{dynload_dir}

%{dynload_dir}/_md5module.so
%{dynload_dir}/_sha256module.so
%{dynload_dir}/_sha512module.so
%{dynload_dir}/_shamodule.so

%{dynload_dir}/Python-%{upstream_version}-py%{pybasever}.egg-info
%{dynload_dir}/_bisectmodule.so
%{dynload_dir}/_bsddb.so
%{dynload_dir}/_codecs_cn.so
%{dynload_dir}/_codecs_hk.so
%{dynload_dir}/_codecs_iso2022.so
%{dynload_dir}/_codecs_jp.so
%{dynload_dir}/_codecs_kr.so
%{dynload_dir}/_codecs_tw.so
%{dynload_dir}/_collectionsmodule.so
%{dynload_dir}/_csv.so
%{dynload_dir}/_ctypes.so
%{dynload_dir}/_curses.so
%{dynload_dir}/_curses_panel.so
%{dynload_dir}/_elementtree.so
%{dynload_dir}/_functoolsmodule.so
%{dynload_dir}/_hashlib.so
%{dynload_dir}/_heapq.so
%{dynload_dir}/_hotshot.so
%{dynload_dir}/_io.so
%{dynload_dir}/_json.so
%{dynload_dir}/_localemodule.so
%{dynload_dir}/_lsprof.so
%{dynload_dir}/_multibytecodecmodule.so
%{dynload_dir}/_multiprocessing.so
%{dynload_dir}/_randommodule.so
%{dynload_dir}/_socketmodule.so
%{dynload_dir}/_sqlite3.so
%{dynload_dir}/_ssl.so
%{dynload_dir}/_struct.so
%{dynload_dir}/arraymodule.so
%{dynload_dir}/audioop.so
%{dynload_dir}/binascii.so
%{dynload_dir}/bz2.so
%{dynload_dir}/cPickle.so
%{dynload_dir}/cStringIO.so
%{dynload_dir}/cmathmodule.so
%{dynload_dir}/_cryptmodule.so
%{dynload_dir}/datetime.so
%{dynload_dir}/dbm.so
%{dynload_dir}/dlmodule.so
%{dynload_dir}/fcntlmodule.so
%{dynload_dir}/future_builtins.so
%if %{with_gdbm}
%{dynload_dir}/gdbmmodule.so
%endif
%{dynload_dir}/grpmodule.so
%{dynload_dir}/imageop.so
%{dynload_dir}/itertoolsmodule.so
#%%{dynload_dir}/linuxaudiodev.so
%{dynload_dir}/math.so
%{dynload_dir}/mmapmodule.so
#%%{dynload_dir}/nismodule.so
%{dynload_dir}/operator.so
#%%{dynload_dir}/ossaudiodev.so
%{dynload_dir}/parsermodule.so
%{dynload_dir}/pyexpat.so
%{dynload_dir}/readline.so
%{dynload_dir}/resource.so
%{dynload_dir}/selectmodule.so
%{dynload_dir}/spwdmodule.so
%{dynload_dir}/stropmodule.so
%{dynload_dir}/syslog.so
%{dynload_dir}/termios.so
%{dynload_dir}/timemodule.so
%{dynload_dir}/timingmodule.so
%{dynload_dir}/unicodedata.so
%{dynload_dir}/xxsubtype.so
%{dynload_dir}/zlibmodule.so

%dir %{site_packages}
%{site_packages}/README
%{pylibdir}/*.py*
%{pylibdir}/*.doc
%{pylibdir}/wsgiref.egg-info
%dir %{pylibdir}/bsddb
%{pylibdir}/bsddb/*.py*
%{pylibdir}/compiler
%dir %{pylibdir}/ctypes
%{pylibdir}/ctypes/*.py*
%{pylibdir}/ctypes/macholib
%{pylibdir}/curses
%dir %{pylibdir}/distutils
%{pylibdir}/distutils/*.py*
%{pylibdir}/distutils/README
%{pylibdir}/distutils/command
%exclude %{pylibdir}/distutils/command/wininst-*.exe
%dir %{pylibdir}/email
%{pylibdir}/email/*.py*
%{pylibdir}/email/mime
%{pylibdir}/encodings
%{pylibdir}/hotshot
%{pylibdir}/idlelib
%{pylibdir}/importlib
%dir %{pylibdir}/json
%{pylibdir}/json/*.py*
%{pylibdir}/lib2to3
%exclude %{pylibdir}/lib2to3/tests
%{pylibdir}/logging
%{pylibdir}/multiprocessing
#%%{pylibdir}/plat-linux2
%{pylibdir}/plat-irix6
%{pylibdir}/pydoc_data
%dir %{pylibdir}/sqlite3
%{pylibdir}/sqlite3/*.py*

# Some bits of test are used for actual testing of stuff, not just python itself:
# See also https://bugzilla.redhat.com/show_bug.cgi?id=1528899
%dir %{pylibdir}/test
%{pylibdir}/test/__init__.py*
%{pylibdir}/test/support/
%{pylibdir}/test/script_helper.py*
%{pylibdir}/test/test_support.py*

%{pylibdir}/unittest
%{pylibdir}/wsgiref
%{pylibdir}/xml
%if "%{_lib}" == "lib32"
%attr(0755,root,root) %dir %{_prefix}/%{_lib}/python%{pybasever}
%attr(0755,root,root) %dir %{_prefix}/%{_lib}/python%{pybasever}/site-packages
%endif

# "Makefile" and the config-32/64.h file are needed by
# distutils/sysconfig.py:_init_posix(), so we include them in the libs
# package, along with their parent directories (bug 531901):
%dir %{pylibdir}/config
%{pylibdir}/config/Makefile
%dir %{_includedir}/python%{pybasever}
%{_includedir}/python%{pybasever}/%{_pyconfig_h}

%{_libdir}/%{py_INSTSONAME_optimized}
%if 0%{?with_systemtap}
%dir %(dirname %{tapsetdir})
%dir %{tapsetdir}
%{tapsetdir}/%{libpython_stp_optimized}
%doc systemtap-example.stp pyfuntop.stp
%endif

%dir %{pylibdir}/ensurepip/
%{pylibdir}/ensurepip/*.py*
%if %{with rpmwheels}
%exclude %{pylibdir}/ensurepip/_bundled
%else
%dir %{pylibdir}/ensurepip/_bundled
%{pylibdir}/ensurepip/_bundled/*.whl
%endif


%files devel
%{_libdir}/pkgconfig/python-%{pybasever}.pc
%{_libdir}/pkgconfig/python2.pc
%{pylibdir}/config/*
%exclude %{pylibdir}/config/Makefile
%{pylibdir}/distutils/command/wininst-*.exe
%{_includedir}/python%{pybasever}/*.h
%exclude %{_includedir}/python%{pybasever}/%{_pyconfig_h}
%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit
%{_bindir}/python2-config
%{_bindir}/python%{pybasever}-config
%{_libdir}/libpython%{pybasever}.so

%files tools
%doc Tools/pynche/README.pynche
%{site_packages}/pynche
%{_bindir}/smtpd2*.py

# https://bugzilla.redhat.com/show_bug.cgi?id=1111275
%exclude %{_bindir}/2to3*

%{_bindir}/idle2*
%{_bindir}/pynche2*
%{_bindir}/pygettext2*.py
%{_bindir}/msgfmt2*.py
%{tools_dir}
%{demo_dir}
%{pylibdir}/Doc

%files tkinter
%{pylibdir}/lib-tk
%if ! 0%{?_module_build}
%{dynload_dir}/_tkinter.so
%endif

%files test
%{pylibdir}/bsddb/test
%{pylibdir}/ctypes/test
%{pylibdir}/distutils/tests
%{pylibdir}/email/test
%{pylibdir}/json/tests
%{pylibdir}/lib2to3/tests
%{pylibdir}/sqlite3/test
%{pylibdir}/test/*

# Some bits of test are used for actual testing of stuff, not just python itself:
# See also https://bugzilla.redhat.com/show_bug.cgi?id=1528899
%exclude %{pylibdir}/test/__init__.py*
%exclude %{pylibdir}/test/support/
%exclude %{pylibdir}/test/script_helper.py*
%exclude %{pylibdir}/test/test_support.py*

%{dynload_dir}/_ctypes_test.so
%{dynload_dir}/_testcapimodule.so


# We don't bother splitting the debug build out into further subpackages:
# if you need it, you're probably a developer.

# Hence the manifest is the combination of analogous files in the manifests of
# all of the other subpackages

%if %{with debug_build}
%files debug

# Analog of the core subpackage's files:
%{_bindir}/%{python}-debug
%{_bindir}/python%{pybasever}-debug

# Analog of the -libs subpackage's files, with debug builds of the built-in
# "extension" modules:

%{dynload_dir}/_md5module_d.so
%{dynload_dir}/_sha256module_d.so
%{dynload_dir}/_sha512module_d.so
%{dynload_dir}/_shamodule_d.so

%{dynload_dir}/_bisectmodule_d.so
%{dynload_dir}/_bsddb_d.so
%{dynload_dir}/_codecs_cn_d.so
%{dynload_dir}/_codecs_hk_d.so
%{dynload_dir}/_codecs_iso2022_d.so
%{dynload_dir}/_codecs_jp_d.so
%{dynload_dir}/_codecs_kr_d.so
%{dynload_dir}/_codecs_tw_d.so
%{dynload_dir}/_collectionsmodule_d.so
%{dynload_dir}/_csv_d.so
%{dynload_dir}/_ctypes_d.so
%{dynload_dir}/_curses_d.so
%{dynload_dir}/_curses_panel_d.so
%{dynload_dir}/_elementtree_d.so
%{dynload_dir}/_functoolsmodule_d.so
%{dynload_dir}/_hashlib_d.so
%{dynload_dir}/_heapq_d.so
%{dynload_dir}/_hotshot_d.so
%{dynload_dir}/_io_d.so
%{dynload_dir}/_json_d.so
%{dynload_dir}/_localemodule_d.so
%{dynload_dir}/_lsprof_d.so
%{dynload_dir}/_multibytecodecmodule_d.so
%{dynload_dir}/_multiprocessing_d.so
%{dynload_dir}/_randommodule_d.so
%{dynload_dir}/_socketmodule_d.so
%{dynload_dir}/_sqlite3_d.so
%{dynload_dir}/_ssl_d.so
%{dynload_dir}/_struct_d.so
%{dynload_dir}/arraymodule_d.so
%{dynload_dir}/audioop_d.so
%{dynload_dir}/binascii_d.so
%{dynload_dir}/bz2_d.so
%{dynload_dir}/cPickle_d.so
%{dynload_dir}/cStringIO_d.so
%{dynload_dir}/cmathmodule_d.so
%{dynload_dir}/_cryptmodule_d.so
%{dynload_dir}/datetime_d.so
%{dynload_dir}/dbm_d.so
%{dynload_dir}/dlmodule_d.so
%{dynload_dir}/fcntlmodule_d.so
%{dynload_dir}/future_builtins_d.so
%if %{with_gdbm}
%{dynload_dir}/gdbmmodule_d.so
%endif
%{dynload_dir}/grpmodule_d.so
%{dynload_dir}/imageop_d.so
%{dynload_dir}/itertoolsmodule_d.so
#%%{dynload_dir}/linuxaudiodev_d.so
%{dynload_dir}/math_d.so
%{dynload_dir}/mmapmodule_d.so
#%%{dynload_dir}/nismodule_d.so
%{dynload_dir}/operator_d.so
#%%{dynload_dir}/ossaudiodev_d.so
%{dynload_dir}/parsermodule_d.so
%{dynload_dir}/pyexpat_d.so
%{dynload_dir}/readline_d.so
%{dynload_dir}/resource_d.so
%{dynload_dir}/selectmodule_d.so
%{dynload_dir}/spwdmodule_d.so
%{dynload_dir}/stropmodule_d.so
%{dynload_dir}/syslog_d.so
%{dynload_dir}/termios_d.so
%{dynload_dir}/timemodule_d.so
%{dynload_dir}/timingmodule_d.so
%{dynload_dir}/unicodedata_d.so
%{dynload_dir}/xxsubtype_d.so
%{dynload_dir}/zlibmodule_d.so

# No need to split things out the "Makefile" and the config-32/64.h file as we
# do for the regular build above (bug 531901), since they're all in one package
# now; they're listed below, under "-devel":

%{_libdir}/%{py_INSTSONAME_debug}
%if 0%{?with_systemtap}
%dir %(dirname %{tapsetdir})
%dir %{tapsetdir}
%{tapsetdir}/%{libpython_stp_debug}
%endif

# Analog of the -devel subpackage's files:
%dir %{pylibdir}/config-debug
%{_libdir}/pkgconfig/python-%{pybasever}-debug.pc
%{_libdir}/pkgconfig/python2-debug.pc
%{pylibdir}/config-debug/*
%{_includedir}/python%{pybasever}-debug/*.h
%{_bindir}/python2-debug-config
%{_bindir}/python%{pybasever}-debug-config
%{_libdir}/libpython%{pybasever}_d.so

# Analog of the -tools subpackage's files:
#  None for now; we could build precanned versions that have the appropriate
# shebang if needed

%if ! 0%{?_module_build}
# Analog  of the tkinter subpackage's files:
%{dynload_dir}/_tkinter_d.so
%endif

# Analog  of the -test subpackage's files:
%{dynload_dir}/_ctypes_test_d.so
%{dynload_dir}/_testcapimodule_d.so

%endif # with debug_build

# We put the debug-gdb.py file inside /usr/lib/debug to avoid noise from
# ldconfig (rhbz:562980).
#
# The /usr/lib/rpm/redhat/macros defines the __debug_package macro to use
# debugfiles.list, and it appears that everything below /usr/lib/debug and
# (/usr/src/debug) gets added to this file (via LISTFILES) in
# /usr/lib/rpm/find-debuginfo.sh
#
# Hence by installing it below /usr/lib/debug we ensure it is added to the
# -debuginfo subpackage
# (if it doesn't, then the rpmbuild ought to fail since the debug-gdb.py
# payload file would be unpackaged)

# Workaround for rhbz#1476593
%undefine _debuginfo_subpackages

# ======================================================
# Finally, the changelog:
# ======================================================

%changelog
* Sat Nov 21 2020 Daniel Hams <daniel.hams@gmail.com> - 2.7.18-3
- Depend on bug-fixed libffi

* Sat Aug 22 2020 Daniel Hams <daniel.hams@gmail.com> - 2.7.18-2
- Depend on sgug-rpm-config not redhat-rpm-config

* Mon Apr 20 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-1
- Update to 2.7.18
- This is is the last Python 2.7 release and therefore the last Python 2 release

* Thu Apr 09 2020 Marcel Plch <mplch@redhat.com> - 2.7.18~rc1-1
- Update to 2.7.18rc1

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.17-1
- Update to 2.7.17

* Wed Oct 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.17~rc1-1
- Rebase to 2.7.17rc1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
