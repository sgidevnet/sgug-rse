# IRIX This is necessary as vim configure will fail with --as-needed
%global build_ldflags -Wl,-z,relro -Wl,-z,now -Wl,-rpath -Wl,%{_libdir}

%global perl_version    5.30.0
%global perl_epoch      4
%global perl_arch_stem -thread-multi
%global perl_archname %{_arch}-%{_os}%{perl_arch_stem}

#DH
#%global multilib_64_archs aarch64 %{power64} s390x sparc64 x86_64 
%global parallel_tests 1
%global tapsetdir   %{_datadir}/systemtap/tapset

%global dual_life 0
%global rebuild_from_scratch %{defined perl_bootstrap}

# This overrides filters from build root (/usr/lib/rpm/macros.d/macros.perl)
# intentionally (unversioned perl(DB) is removed and versioned one is kept).
# Filter provides from *.pl files, bug #924938
%global __provides_exclude_from .*%{_docdir}|.*%{perl_archlib}/.*\\.pl$|.*%{perl_privlib}/.*\\.pl$
%global __requires_exclude_from %{_docdir}
%global __provides_exclude perl\\((VMS|Win32|BSD::|DB\\)$)
%global __requires_exclude perl\\((VMS|BSD::|Win32|Tk|Mac::|Your::Module::Here)
# same as we provide in /usr/lib/rpm/macros.d/macros.perl
%global perl5_testdir   %{_libexecdir}/perl5-tests

# Optional features
# Run C++ tests
%bcond_without perl_enables_cplusplus_test
# We can bootstrap without gdbm
%bcond_without gdbm
# Support for groff, bug #135101
%bcond_without perl_enables_groff
# Run Turkish locale tests
%bcond_without perl_enables_turkish_test
# Run syslog tests
%bcond_with perl_enables_syslog_test
# SystemTap support
#%bcond_without perl_enables_systemtap
# <> operator uses File::Glob nowadays. CSH is not needed.
%bcond_with perl_enables_tcsh
# We can skip %%check phase
%bcond_without test

Name:           perl
# These are all found licenses. They are distributed among various
# subpackages.
# dist/Tie-File/lib/Tie/File.pm:        GPLv2+ or Artistic
# cpan/Getopt-Long/lib/Getopt/Long.pm:  GPLv2+ or Artistic
# cpan/Compress-Raw-Zlib/Zlib.xs:       (GPL+ or Artistic) and zlib
# cpan/Digest-MD5/MD5.xs:               (GPL+ or Artistic) and BSD
# cpan/Time-Piece/Piece.xs:             (GPL+ or Artistic) and BSD
# dist/PathTools/Cwd.xs:                (GPL+ or Artistic) and BSD
# util.c:                               (GPL+ or Artistic) and BSD
# cpan/perlfaq/lib/perlfaq4.pod:        (GPL+ or Artistic) and Public Domain
# cpan/Test-Simple/lib/Test/Tutorial.pod:   (GPL+ or Artistic) and
#                                           Public Domain
# cpan/MIME-Base64/Base64.xs:           (GPL+ or Artistic) and MIT
# cpan/Test-Simple/lib/ok.pm:           CC0
# cpan/Text-Tabs/lib/Text/Wrap.pm:      TTWL
# cpan/Encode/bin/encguess:             Artistic 2.0
# cpan/libnet/lib/Net/libnetFAQ.pod:    Artistic    (CPAN RT#117888)
# cpan/Unicode-Collate/Collate/allkeys.txt:     Unicode
# lib/unicore:                          UCD
# ext/SDBM_File/sdbm.{c,h}:             Public domain
# regexec.c, regcomp.c:                 HSRL
# cpan/Locale-Maketext-Simple/lib/Locale/Maketext/Simple.pm:    MIT (with
#                                       exception for Perl)
# time64.c:                             MIT
# pod/perlpodstyle.pod:                 MIT
# pod/perlunicook.pod:                  (GPL+ or Artistic) and Public Domain
# pod/perlgpl.pod:                      GPL text
# pod/perlartistic.pod:                 Artistic text
# ext/File-Glob/bsd_glob.{c,h}:         BSD
# Other files:                          GPL+ or Artistic
## Not is a binary package
# cpan/podlators/t/style/minimum-version.t          MIT
# cpan/Term-ANSIColor/t/lib/Test/RRA/Config.pm:     MIT
## Unbundled
# cpan/Compress-Raw-Bzip2/bzip2-src:    BSD
# cpan/Compress-Raw-Zlib/zlib-src:      zlib
## perl sub-package notice
# perluniprops.pod is generated from lib/unicore sources:   UCD
#
# This sub-subpackage doesn't contain any copyrightable material.
# Nevertheless, it needs a License tag, so we'll use the generic
# "perl" license.
License:        GPL+ or Artistic
Epoch:          %{perl_epoch}
Version:        %{perl_version}
# release number must be even higher, because dual-lived modules will be broken otherwise
Release:        446%{?dist}
Summary:        Practical Extraction and Report Language
Url:            https://www.perl.org/
Source0:        https://www.cpan.org/src/5.0/perl-%{perl_version}.tar.gz
Source3:        macros.perl
#Systemtap tapset and example that make use of systemtap-sdt-devel
# build requirement. Written by lberk; Not yet upstream.
Source4:        perl.stp
Source5:        perl-example.stp
# Tom Christiansen confirms Pod::Html uses the same license as perl
Source6:        Pod-Html-license-clarification

# Pregenerated dependencies for bootstrap.
# If your RPM tool fails on including the source file, then you forgot to
# define _sourcedir macro to point to the directory with the sources.
Source7:        gendep.macros
%if %{defined perl_bootstrap}
%include %{SOURCE7}
%endif

Source8:        perl.irix6_gcc_config.sh

# Removes date check, Fedora/RHEL specific
Patch1:         perl-perlbug-tag.patch

# Fedora/RHEL only (64bit only)
Patch2:         perl-5.8.0-libdir64.patch

# Fedora/RHEL specific (use libresolv instead of libbind), bug #151127
Patch3:         perl-5.10.0-libresolv.patch

# FIXME: May need the "Fedora" references removed before upstreaming
# patches ExtUtils-MakeMaker
Patch4:         perl-USE_MM_LD_RUN_PATH.patch

# Provide maybe_command independently, bug #1129443
Patch5:         perl-5.22.1-Provide-ExtUtils-MM-methods-as-standalone-ExtUtils-M.patch

# The Fedora builders started randomly failing this futime test
# only on x86_64, so we just don't run it. Works fine on normal
# systems.
Patch6:         perl-5.10.0-x86_64-io-test-failure.patch

# switch off test, which is failing only on koji (fork)
Patch7:         perl-5.14.1-offtest.patch

# Define SONAME for libperl.so
Patch8:         perl-5.16.3-create_libperl_soname.patch

# Install libperl.so to -Dshrpdir value
Patch9:         perl-5.22.0-Install-libperl.so-to-shrpdir-on-Linux.patch

# Make *DBM_File desctructors thread-safe, bug #1107543, RT#61912
Patch10:        perl-5.18.2-Destroy-GDBM-NDBM-ODBM-SDBM-_File-objects-only-from-.patch

# Replace ExtUtils::MakeMaker dependency with ExtUtils::MM::Utils.
# This allows not to require perl-devel. Bug #1129443
Patch11:        perl-5.22.1-Replace-EU-MM-dependnecy-with-EU-MM-Utils-in-IPC-Cmd.patch

# Link XS modules to pthread library to fix linking with -z defs,
# <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/3RHZEHLRUHJFF2XGHI5RB6YPDNLDR4HG/>
Patch12:        perl-5.27.8-hints-linux-Add-lphtread-to-lddlflags.patch

# Pass the correct CFLAGS to dtrace
Patch13:        perl-5.28.0-Pass-CFLAGS-to-dtrace.patch

# Fix an out-of-buffer read while parsing a Unicode property name, RT#134134,
# fixed after 5.31.0
Patch14:        perl-5.31.0-PATCH-perl-134134-read-beyond-end-of-buffer.patch

# Do not panic when outputting a warning, RT#134059, fixed after 5.31.0
Patch15:        perl-5.31.0-PATCH-perl-134059-panic-outputting-a-warning.patch

# Fix memory handling when parsing string literals, fixed after 5.31.0
Patch16:        perl-5.31.0-S_scan_const-Properly-test-if-need-to-grow.patch

# Fix an undefined behavior in shifting IV variables, fixed after 5.31.0
Patch17:        perl-5.31.0-Create-fcn-for-lossless-conversion-of-NV-to-IV.patch
Patch18:        perl-5.30.0-pp.c-Add-two-UNLIKELY-s.patch
Patch19:        perl-5.30.0-Remove-undefined-behavior-from-IV-shifting.patch

# Fix stacking file test operators, CPAN RT#127073, fixed after 5.31.0
Patch20:        perl-5.31.0-Don-t-use-PL_check-op_type-to-check-for-filetets-ops.patch

# Fix a crash in SIGALARM handler when waiting on a child process to be closed,
# RT#122112, fixed after 5.31.0
Patch21:        perl-5.31.0-perl-122112-test-for-signal-handler-death-in-pclose.patch
Patch22:        perl-5.31.0-perl-122112-a-simpler-fix-for-pclose-aborted-by-a-si.patch
Patch23:        perl-5.31.0-perl-122112-remove-some-interfering-debug-output.patch

# Fix a crash with a negative precision in sprintf function, RT#134008,
# fixed after 5.31.0
Patch24:        perl-5.31.0-134008-More-carefully-ignore-negative-precision-in-s.patch
Patch25:        perl-5.31.0-perl-134008-an-alternative-test.patch

# Fix an erroneous assertion on OP_SCALAR, RT#134048, fixed after 5.31.0
Patch26:        perl-5.31.0-perl-134048-prevent-an-erroneous-assertion-on-OP_SCA.patch

# Prevent from wrapping a width in a numeric format string, RT#133913,
# fixed after 5.31.0
Patch27:        perl-5.31.0-perl-133913-limit-numeric-format-results-to-INT_MAX.patch

# Fix subroutine protypes to track reference aliases, RT#134072,
# fixed after 5.31.0
Patch28:        perl-5.31.0-perl-134072-allow-foo-bar-to-work-in-main.patch

# Improve retrieving a scalar value of a variable modified in a signal
# handler, RT#134035, fixed after 5.31.0
Patch29:        perl-5.31.0-perl-134035-ensure-sv_gets-handles-a-signal-handler-.patch

# Fix changing packet destination sent from a UDP IO::Socket object,
# RT#133936, fixed after 5.31.0
Patch30:        perl-5.31.0-perl-133936-ensure-TO-is-honoured-for-UDP-sock-send.patch
Patch31:        perl-5.31.0-perl-133936-document-differences-between-IO-Socket-a.patch
Patch32:        perl-5.31.0-perl-133936-make-send-a-bit-saner.patch

# Fix a stack underflow in readline() if passed an empty array as an argument,
# RT133989, fixed after 5.31.0
Patch33:        perl-5.31.0-perl-133989-scalar-the-argument-to-readline-if-any.patch

# Fix setting supplementar group IDs, RT#134169, fixed after 5.31.0
Patch34:        perl-5.31.0-perl-134169-mg.c-reset-endptr-after-use.patch
Patch35:        perl-5.31.0-Add-test-for-perl-134169.patch
Patch36:        perl-5.31.0-Manuel-Mausz-is-now-a-perl-author.patch

# Fix %%{^CAPTURE_ALL} to be an alias for %%- variable, RT#131867,
# fixed after 5.31.0
Patch37:        perl-5.31.0-CAPTURE_ALL-was-intended-to-be-an-alias-for-make-it-.patch

# Fix %%{^CAPTURE} value when used after @{^CAPTURE}, RT#134193,
# fixed after 5.31.0
Patch38:        perl-5.31.0-perl-134193-allow-CAPTURE-to-work-when-CAPTURE-comes.patch
Patch39:        perl-5.31.0-perl-134193-make-the-varname-match-the-names.patch

# Fix a test for a crash in SIGALARM handler when waiting on a child process to
# be closed, RT#122112, fixed after 5.31.1
Patch40:        perl-5.31.1-perl-122112-make-sure-SIGPIPE-is-delivered-if-we-tes.patch

# Fix a crash on an uninitialized warning when processing a multideref node,
# RT#134275, fixed after 5.31.1
Patch41:        perl-5.31.1-avoid-SEGV-with-uninit-warning-with-multideref.patch

# Preserve append mode when opening anonymous files, RT#134221,
# fixed after 5.31.1
Patch42:        perl-5.30.0-perl-134221-support-append-mode-for-open-.-undef.patch
Patch43:        perl-5.31.1-perl-134221-support-append-mode-temp-files-on-Win32-.patch
Patch44:        perl-5.31.1-perl-134221-support-O_APPEND-for-open-.-undef-on-VMS.patch

# Fix propagating non-string variables in an exception value, RT#134291,
# fixed after 5.31.2
Patch45:        perl-5.31.2-perl-134291-propagate-non-PVs-in-in-bare-die.patch

# Include trailing zero in scalars holding trie data, RT#134207,
# fixed after 5.31.2
Patch46:        perl-5.31.2-include-a-trailing-0-in-SVs-holding-trie-info.patch

# Fix a use after free in /(?{...})/, RT#134208, fixed after 5.31.2
Patch47:        perl-5.31.2-avoid-use-after-free-in.patch

# Fix a use after free in debugging output of a collation,
# in upstream after 5.31.2
Patch48:        perl-5.31.2-locale.c-Stop-Coverity-warning.patch

# Fix a NULL pointer dereference in PerlIOVia_pushed(), fixed after 5.31.2
Patch49:        perl-5.31.2-PerlIO-Via-check-arg-is-non-NULL-before-using-it.patch

# Fix a crash when setting $@ on unwinding a call stack, RT#134266,
# fixed after 5.31.2
Patch50:        perl-5.30.0-perl-134266-make-sure-is-writable-when-we-write-to-i.patch

# Fix parsing a denominator when parsing a Unicode property name,
# fixed after 5.31.2
Patch51:        perl-5.31.2-regcomp.c-Don-t-read-off-the-end-of-buffer.patch

# Fix a documentation about a future API change, fixed after 5.31.2
Patch52:        perl-5.31.2-perlapi-5.30-promise-not-met-change-to-5.32.patch

# Do not run File-Find tests in parallel, fixed after 5.31.2
Patch53:        perl-5.31.2-Run-tests-in-ext-File-Find-t-in-series.patch

# Fix parsing a Unicode property name when compiling a regular expression,
# fixed after 5.31.3
Patch54:        perl-5.31.3-regcomp.c-Fix-wrong-limit-test.patch

# Fix a buffer overread when parsing a Unicode property while compiling
# a regular expression, RT#134133, fixed after 5.31.3
Patch55:        perl-5.31.3-PATCH-perl-134133-read-beyond-end-of-buffer.patch

# Do not interpret 0x and 0b prefixes when numifying strings, RT#134230,
# fixed after 5.31.3
Patch56:        perl-5.31.3-perl-134230-don-t-interpret-0x-0b-when-numifying-str.patch

# Fix a buffer overread when compiling a regular expression with many escapes,
# RT#134325, fixed after 5.31.3
Patch57:        perl-5.31.3-PATCH-perl-134325-Heap-buffer-overflow.patch

# Fix a buffer overflow when compiling a regular expression with many
# branches, RT#134329, fixed after 5.31.3
# This is a binary patch and requires git.
Patch58:        perl-5.30.0-PATCH-perl-134329-Use-after-free-in-regcomp.c.patch

# Correct a misspelling in perlrebackslash documentation, RT#134395,
# fixed after 5.31.3
Patch59:        perl-5.31.3-Supply-missing-right-brace-in-regex-example.patch

# Fix a memory leak when matching a UTF-8 regular expression, RT#134329,
# fixed after 5.31.3
Patch60:        perl-5.31.3-perl-134390-don-t-leak-the-SV-we-just-created-on-an-.patch

# Fix a detection for futimes, RT#134432, fixed after 5.31.3
Patch61:        perl-5.31.3-Configure-Include-stdlib.h-in-futimes-check.patch
Patch62:        perl-5.31.3-Florian-Weimer-is-now-a-perl-author.patch

# Link XS modules to libperl.so with EU::CBuilder on Linux, bug #960048
Patch200:       perl-5.16.3-Link-XS-modules-to-libperl.so-with-EU-CBuilder-on-Li.patch

# Link XS modules to libperl.so with EU::MM on Linux, bug #960048
Patch201:       perl-5.16.3-Link-XS-modules-to-libperl.so-with-EU-MM-on-Linux.patch

Patch300:         perl5_30_0_fixes.patch

# Update some of the bundled modules
# see http://fedoraproject.org/wiki/Perl/perl.spec for instructions

#BuildRequires:  bash
#BuildRequires:  bzip2-devel
#BuildRequires:  coreutils
#BuildRequires:  findutils
#BuildRequires:  gcc
%if %{with gdbm}
#BuildRequires:  gdbm-devel
%endif
# git for PATCH-perl-134329-Use-after-free-in-regcomp.c.patch
#BuildRequires:  git-core
# glibc-common for iconv
#BuildRequires:  glibc-common
%if %{with perl_enables_groff}
# Build-require groff tools for populating %%Config correctly, bug #135101
#BuildRequires:  groff-base
%endif
#BuildRequires:  libdb-devel
#BuildRequires:  make
%if !%{defined perl_bootstrap}
#BuildRequires:  perl-interpreter
#BuildRequires:  perl-generators
%endif
#BuildRequires:  sed
%if %{with perl_enables_systemtap}
#BuildRequires:  systemtap-sdt-devel
%endif
#BuildRequires:  tar
%if %{with perl_enables_tcsh}
#BuildRequires:  tcsh
%endif
#BuildRequires:  zlib-devel

# For tests
%if %{with test}
%if %{with perl_enables_cplusplus_test}
# An optional ExtUtils-CBuilder's test
#BuildRequires:  gcc-c++
%endif
#BuildRequires:  procps
%if %{with perl_enables_turkish_test}
# An optional t/re/fold_grind_T.t test
#BuildRequires:  glibc-langpack-tr
%endif
%if %{with perl_enables_syslog_test}
#BuildRequires:  rsyslog
%endif
%endif


# compat macro needed for rebuild
%global perl_compat perl(:MODULE_COMPAT_5.30.0)

Requires:       %perl_compat
Requires:       perl-interpreter%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-devel%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-macros
Requires:       perl-utils
%if %{defined perl_bootstrap}
%gendep_perl
%endif

Requires:       perl-Archive-Tar, perl-Attribute-Handlers, perl-autodie,
Requires:       perl-bignum
Requires:       perl-Compress-Raw-Bzip2,
Requires:       perl-Carp, perl-Compress-Raw-Zlib, perl-Config-Perl-V,
Requires:       perl-constant,
Requires:       perl-CPAN, perl-CPAN-Meta, perl-CPAN-Meta-Requirements,
Requires:       perl-CPAN-Meta-YAML
Requires:       perl-Data-Dumper, perl-DB_File,
Requires:       perl-Devel-Peek, perl-Devel-PPPort, perl-Devel-SelfStubber,
Requires:       perl-Digest, perl-Digest-MD5,
Requires:       perl-Digest-SHA,
Requires:       perl-Encode, perl-Encode-devel, perl-encoding
Requires:       perl-Env, perl-Errno, perl-Exporter, perl-experimental
Requires:       perl-ExtUtils-CBuilder, perl-ExtUtils-Command,
Requires:       perl-ExtUtils-Embed,
Requires:       perl-ExtUtils-Install, perl-ExtUtils-MakeMaker
Requires:       perl-ExtUtils-Manifest, perl-ExtUtils-Miniperl
Requires:       perl-ExtUtils-ParseXS, perl-File-Fetch
Requires:       perl-File-Path, perl-File-Temp, perl-Filter,
Requires:       perl-Filter-Simple, perl-Getopt-Long
Requires:       perl-HTTP-Tiny,
Requires:       perl-IO, perl-IO-Compress, perl-IO-Socket-IP
Requires:       perl-IO-Zlib, perl-IPC-Cmd, perl-IPC-SysV, perl-JSON-PP
Requires:       perl-libnet, perl-libnetcfg,
Requires:       perl-Locale-Maketext,
Requires:       perl-Locale-Maketext-Simple
Requires:       perl-Math-BigInt, perl-Math-BigInt-FastCalc, perl-Math-BigRat,
Requires:       perl-Math-Complex, perl-Memoize,
Requires:       perl-MIME-Base64,
Requires:       perl-Module-CoreList,
Requires:       perl-Module-CoreList-tools, perl-Module-Load
Requires:       perl-Module-Load-Conditional, perl-Module-Loaded,
Requires:       perl-Module-Metadata, perl-Net-Ping,
Requires:       perl-open, perl-PathTools
Requires:       perl-Params-Check
Requires:       perl-perlfaq,
Requires:       perl-PerlIO-via-QuotedPrint, perl-Perl-OSType
Requires:       perl-Pod-Checker, perl-Pod-Escapes, perl-Pod-Html,
Requires:       perl-Pod-Parser, perl-Pod-Perldoc, perl-Pod-Usage
Requires:       perl-podlators, perl-Pod-Simple, perl-Scalar-List-Utils
Requires:       perl-SelfLoader, perl-Socket, perl-Storable, perl-Sys-Syslog,
Requires:       perl-Term-ANSIColor, perl-Term-Cap,
Requires:       perl-Test, perl-Test-Harness, perl-Test-Simple
Requires:       perl-Text-Balanced, perl-Text-ParseWords, perl-Text-Tabs+Wrap,
Requires:       perl-Thread-Queue
Requires:       perl-Time-HiRes
Requires:       perl-Time-Local, perl-Time-Piece
Requires:       perl-Unicode-Collate, perl-Unicode-Normalize,
Requires:       perl-version, perl-threads, perl-threads-shared, perl-parent

# Full EVR is for compatibility with systems that swapped perl and perl-core
# <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>,
# bug #1464903.
Provides:       perl-core = %{perl_version}-%{release}
Provides:       perl-core%{?_isa} = %{perl_version}-%{release}
# perl was renamed to perl-interpreter and perl-core renamed to perl
Obsoletes:      perl-core < 5.26.0-395


%description
Perl is a high-level programming language with roots in C, sed, awk and shell
scripting. Perl is good at handling processes and files, and is especially
good at handling text. Perl's hallmarks are practicality and efficiency.
While it is used to do a lot of different things, Perl's most common
applications are system administration utilities and web programming.

This is a metapackage with all the Perl bits and core modules that can be
found in the upstream tarball from perl.org.

If you need only a specific feature, you can install a specific package
instead. E.g. to handle Perl scripts with %{_bindir}/perl interpreter,
install perl-interpreter package. See perl-interpreter description for more
details on the Perl decomposition into packages.


%package interpreter
Summary:        Standalone executable Perl interpreter
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic) and BSD and Public Domain and UCD
# perl-interpreter denotes a package with the perl executable.
# Full EVR is for compatibility with systems that swapped perl and perl-core
# <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>,
# bug #1464903.
Version:        %{perl_version}
Epoch:          %{perl_epoch}

Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
# Require this till perl-interpreter sub-package provides any modules
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_interpreter
%endif

# We need this to break the dependency loop, and ensure that perl-libs 
# gets installed before perl-interpreter.
Requires(post): perl-libs
# Same as perl-libs. We need macros in basic buildroot, where Perl is only
# because of git.
Requires(post): perl-macros

# File provides
Provides:       perl(bytes_heavy.pl)
Provides:       perl(dumpvar.pl)
Provides:       perl(perl5db.pl)

# suidperl isn't created by upstream since 5.12.0
Obsoletes:      perl-suidperl <= 4:5.12.2
# perl was renamed to perl-interpreter and perl-core renamed to perl
# <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>,
# bug #1464903.
Obsoletes:      perl < 4:5.26.0-395


%description interpreter
This is a Perl interpreter as a standalone executable %{_bindir}/perl
required for handling Perl scripts. It does not provide all the other Perl
modules or tools.

Install this package if you want to program in Perl or enable your system to
handle Perl scripts with %{_bindir}/perl interpreter.

If your script requires some Perl modules, you can install them with
"perl(MODULE)" where "MODULE" is a name of required module. E.g. install
"perl(Test::More)" to make Test::More Perl module available.

If you need all the Perl modules that come with upstream Perl sources, so
called core modules, install perl package.

If you only need perl run-time as a shared library, i.e. Perl interpreter
embedded into another application, the only essential package is perl-libs.

Perl header files can be found in perl-devel package.

Perl utils like "splain" or "perlbug" can be found in perl-utils package.


%package libs
Summary:        The libraries for the perl run-time
License:        (GPL+ or Artistic) and HSRL and MIT and UCD
# Compat provides
Provides:       %perl_compat
# Interpreter version to fulfil required genersted from "require 5.006;"
Provides:       perl(:VERSION) = %{perl_version}
# Integeres are 64-bit on all platforms
Provides:       perl(:WITH_64BIT)
# Threading provides
Provides:       perl(:WITH_ITHREADS)
Provides:       perl(:WITH_THREADS)
# Largefile provides
Provides:       perl(:WITH_LARGEFILES)
# PerlIO provides
Provides:       perl(:WITH_PERLIO)
# Loaded by charnames, unicore/Name.pm does not declare unicore::Name module
Provides:       perl(unicore::Name)
# Keep utf8 modules in perl-libs because a sole regular expression like /\pN/
# causes loading utf8 and unicore/Heave.pl and unicore/lib files.
Provides:       perl(utf8_heavy.pl)
# utf8 and utf8_heavy.pl require Carp, re, strict, warnings, XSLoader
Requires:       perl(Carp)
Requires:       perl(Exporter)
# Term::Cap is optional
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
%gendep_perl_libs
%endif

# Remove private redefinitions
# XSLoader redefines DynaLoader name space for compatibility, but does not
# load the DynaLoader.pm (though the DynaLoader.xs is compiled into libperl).
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((charnames|DynaLoader)\\)$

%description libs
The is a perl run-time (interpreter as a shared library and include
directories).


%package devel
Summary:        Header #files for use in perl development
# l1_char_class_tab.h is generated from lib/unicore sources:    UCD
License:        (GPL+ or Artistic) and UCD
%if %{with perl_enables_systemtap}
#Requires:       systemtap-sdt-devel
%endif
Requires:       perl(ExtUtils::ParseXS)
Requires:       %perl_compat
# Match library and header files when downgrading releases
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
# Devel::PPPort for h2xs script
Requires:       perl(Devel::PPPort)
# Compiler and linker options stored into perl and used when building XS
# modules refer to hardering profiles like
# /usr/lib/rpm/redhat/redhat-hardened-cc1 that are delivered by
# redhat-rpm-config. Bug #1557667.
#Requires:       redhat-rpm-config
# ExtUtils::Embed -e ldopts include libcrypt, bug #1666098
#Requires:       libxcrypt-devel%{?_isa}

%if %{defined perl_bootstrap}
%gendep_perl_devel
%endif

%description devel
This package contains header files and development modules.
Most perl packages will need to install perl-devel to build.


%package macros
Summary:        Macros for rpmbuild
License:        GPL+ or Artistic
Requires:       %perl_compat
Requires:       perl-interpreter
%if %{defined perl_bootstrap}
%gendep_perl_macros
%endif

%description macros
RPM macros that are handy when building binary RPM packages.


%package tests
Summary:        The Perl test suite
License:        GPL+ or Artistic
# right?
AutoReqProv:    0
Requires:       %perl_compat
# FIXME - note this will need to change when doing the core/minimal swizzle
Requires:       perl
%if %{defined perl_bootstrap}
%gendep_perl_tests
%endif

%description tests
This package contains the test suite included with Perl %{perl_version}.

Install this if you want to test your Perl installation (binary and core
modules).


%package utils
Summary:        Utilities packaged with the Perl distribution
License:        GPL+ or Artistic
Epoch:          0
Version:        %{perl_version}
BuildArch:      noarch
# Match library exactly for splain messages
Requires:       perl-libs = %{perl_epoch}:%{perl_version}-%{release}
# Keep /usr/sbin/sendmail and Module::CoreList optional for the perlbug tool
%if %{defined perl_bootstrap}
%gendep_perl_utils
%endif
Conflicts:      perl < 4:5.22.0-351

%description utils
Several utilities which come with Perl distribution like h2ph, perlbug,
perlthanks, pl2pm, and splain. Some utilities are provided by more specific
packages like perldoc by perl-Pod-Perldoc.


%if %{dual_life} || %{rebuild_from_scratch}
%package Archive-Tar
Summary:        A module for Perl manipulation of .tar files
License:        GPL+ or Artistic
Epoch:          0
Version:        2.32
BuildArch:      noarch
Requires:       %perl_compat
Requires:       perl(IO::Zlib) >= 1.01
# Optional run-time:
Requires:       perl(IO::Compress::Bzip2) >= 2.015
# IO::String not used if perl supports useperlio which is true
# Use Compress::Zlib's version for IO::Uncompress::Bunzip2
Requires:       perl(IO::Uncompress::Bunzip2) >= 2.015
%if !%{defined perl_bootstrap}
Requires:       perl(Text::Diff)
%endif
%if %{defined perl_bootstrap}
%gendep_perl_Archive_Tar
%endif

%description Archive-Tar
Archive::Tar provides an object oriented mechanism for handling tar files.  It
provides class methods for quick and easy files handling while also allowing
for the creation of tar file objects for custom manipulation.  If you have the
IO::Zlib module installed, Archive::Tar will also support compressed or
gzipped tar files.
%endif

%package Attribute-Handlers
Summary:        Simpler definition of attribute handlers
License:        GPL+ or Artistic
Epoch:          0
Version:        1.01
BuildArch:      noarch
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Attribute_Handlers
%endif
Conflicts:      perl < 4:5.22.0-351

%description Attribute-Handlers
This Perl module, when inherited by a package, allows that package's class to
define attribute handler subroutines for specific attributes. Variables and
subroutines subsequently defined in that package, or in packages derived from
that package may be given attributes with the same names as the attribute
handler subroutines, which will then be called in one of the compilation
phases (i.e. in a "BEGIN", "CHECK", "INIT", or "END" block).

%if %{dual_life} || %{rebuild_from_scratch}
%package autodie
Summary:        Replace functions with ones that succeed or die
License:        GPL+ or Artistic
Epoch:          0
Version:        2.29
Requires:       %perl_compat
BuildArch:      noarch
Requires:       perl(B)
Requires:       perl(Fcntl)
Requires:       perl(overload)
Requires:       perl(POSIX)
%if %{defined perl_bootstrap}
%gendep_perl_autodie
%endif
Conflicts:      perl < 4:5.16.2-259

%description autodie
The "autodie" and "Fatal" pragma provides a convenient way to replace
functions that normally return false on failure with equivalents that throw an
exception on failure.

However "Fatal" has been obsoleted by the new autodie pragma. Please use
autodie in preference to "Fatal".
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package bignum
Summary:        Transparent big number support for Perl
License:        GPL+ or Artistic
Epoch:          0
Version:        0.51
Requires:       %perl_compat
Requires:       perl(Carp)
# Math::BigInt::Lite is optional
Requires:       perl(Math::BigRat)
Requires:       perl(warnings)
BuildArch:      noarch
%if %{defined perl_bootstrap}
%gendep_perl_bignum
%endif
Conflicts:      perl < 4:5.22.0-348

%description bignum
This package attempts to make it easier to write scripts that use BigInts and
BigFloats in a transparent way.

%package Carp
Summary:        Alternative warn and die for modules
Epoch:          0
# Real version 1.50
Version:        1.50
License:        GPL+ or Artistic
Requires:       %perl_compat
Provides:       perl(Carp::Heavy) = %{version}
%if %{defined perl_bootstrap}
%gendep_perl_Carp
%endif
BuildArch:      noarch

# Do not export unversioned module
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Carp\\)\\s*$

%description Carp
The Carp routines are useful in your own modules because they act like
die() or warn(), but with a message which is more likely to be useful to a
user of your module. In the case of cluck, confess, and longmess that
context is a summary of every call in the call-stack. For a shorter message
you can use carp or croak which report the error as being from where your
module was called. There is no guarantee that that is where the error was,
but it is a good educated guess.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Compress-Raw-Bzip2
Summary:        Low-Level Interface to bzip2 compression library
License:        GPL+ or Artistic
Epoch:          0
Version:        2.084
Requires:       perl(Exporter), perl(File::Temp)
%if %{defined perl_bootstrap}
%gendep_perl_Compress_Raw_Bzip2
%endif

%description Compress-Raw-Bzip2
This module provides a Perl interface to the bzip2 compression library.
It is used by IO::Compress::Bzip2.

%package Compress-Raw-Zlib
Summary:        Low-Level Interface to the zlib compression library
License:        (GPL+ or Artistic) and zlib
Epoch:          0
Version:        2.084
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Compress_Raw_Zlib
%endif

%description Compress-Raw-Zlib
This module provides a Perl interface to the zlib compression library.
It is used by IO::Compress::Zlib.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Config-Perl-V
Summary:        Structured data retrieval of perl -V output
License:        GPL+ or Artistic
Epoch:          0
Version:        0.32
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Config_Perl_V
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347

%description Config-Perl-V
The command "perl -V" will return you an excerpt from the %%Config::Config
hash combined with the output of "perl -V" that is not stored inside the hash,
but only available to the perl binary itself. This package provides Perl
module that will return you the output of "perl -V" in a structure.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package constant
Summary:        Perl pragma to declare constants
License:        GPL+ or Artistic
Epoch:          0
Version:        1.33
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_constant
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-264

%description constant
This pragma allows you to declare constants at compile-time:

use constant PI => 4 * atan2(1, 1);

When you declare a constant such as "PI" using the method shown above,
each machine your script runs upon can have as many digits of accuracy
as it can use. Also, your program will be easier to read, more likely
to be maintained (and maintained correctly), and far less likely to
send a space probe to the wrong planet because nobody noticed the one
equation in which you wrote 3.14195.

When a constant is used in an expression, Perl replaces it with its
value at compile time, and may then optimize the expression further.
In particular, any code in an "if (CONSTANT)" block will be optimized
away if the constant is false.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN
Summary:        Query, download and build perl modules from CPAN sites
License:        GPL+ or Artistic
Epoch:          0
Version:        2.22
Requires:       make
# Prefer Archive::Tar and Compress::Zlib over tar and gzip
Requires:       perl(Archive::Tar) >= 1.50
Requires:       perl(base)
Requires:       perl(Data::Dumper)
%if !%{defined perl_bootstrap}
Requires:       perl(Devel::Size)
%endif
Requires:       perl(ExtUtils::Manifest)
%if !%{defined perl_bootstrap}
Requires:       perl(File::HomeDir) >= 0.65
%endif
Requires:       perl(File::Temp) >= 0.16
Requires:       perl(lib)
Requires:       perl(Net::Config)
Requires:       perl(Net::FTP)
Requires:       perl(POSIX)
Requires:       perl(Term::ReadLine)
%if !%{defined perl_bootstrap}
Requires:       perl(URI)
Requires:       perl(URI::Escape)
%endif
Requires:       perl(User::pwent)
# Optional but higly recommended:
%if !%{defined perl_bootstrap}
Requires:       perl(Archive::Zip)
Requires:       perl(Compress::Bzip2)
Requires:       perl(CPAN::Meta) >= 2.110350
%endif
Requires:       perl(Compress::Zlib)
Requires:       perl(Digest::MD5)
# CPAN encourages Digest::SHA strongly because of integrity checks
Requires:       perl(Digest::SHA)
Requires:       perl(Dumpvalue)
Requires:       perl(ExtUtils::CBuilder)
%if ! %{defined perl_bootstrap}
# Avoid circular deps local::lib -> Module::Install -> CPAN when bootstraping
# local::lib recommended by CPAN::FirstTime default choice, bug #1122498
Requires:       perl(local::lib)
%endif
#Requires:       perl(Module::Build)
%if ! %{defined perl_bootstrap}
Requires:       perl(Text::Glob)
%endif
Requires:       %perl_compat
Provides:       cpan = %{version}
%if %{defined perl_bootstrap}
%gendep_perl_CPAN
%endif
BuildArch:      noarch

%description CPAN
The CPAN module automates or at least simplifies the make and install of
perl modules and extensions. It includes some primitive searching
capabilities and knows how to use LWP, HTTP::Tiny, Net::FTP and certain
external download clients to fetch distributions from the net.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN-Meta
Summary:        Distribution metadata for a CPAN dist
Epoch:          0
Version:        2.150010
License:        GPL+ or Artistic
Requires:       %perl_compat
Requires:       perl(CPAN::Meta::YAML) >= 0.011
Requires:       perl(Encode)
Requires:       perl(JSON::PP) >= 2.27300
%if %{defined perl_bootstrap}
%gendep_perl_CPAN_Meta
%endif
BuildArch:      noarch

%description CPAN-Meta
Software distributions released to the CPAN include a META.json or, for
older distributions, META.yml, which describes the distribution, its
contents, and the requirements for building and installing the
distribution. The data structure stored in the META.json file is described
in CPAN::Meta::Spec.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN-Meta-Requirements
Summary:        Set of version requirements for a CPAN dist
Epoch:          0
# Real version 2.140
Version:        2.140
License:        GPL+ or Artistic
Requires:       %perl_compat
BuildArch:      noarch
# CPAN-Meta-Requirements used to have six decimal places
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(CPAN::Meta::Requirements\\)
Provides:       perl(CPAN::Meta::Requirements) = %{version}000
%if %{defined perl_bootstrap}
%gendep_perl_CPAN_Meta_Requirements
%endif

%description CPAN-Meta-Requirements
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN-Meta-YAML
Version:        0.018
Epoch:          0
Summary:        Read and write a subset of YAML for CPAN Meta files
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_CPAN_Meta_YAML
%endif

%description CPAN-Meta-YAML
This module implements a subset of the YAML specification for use in reading
and writing CPAN metadata files like META.yml and MYMETA.yml. It should not be
used for any other general YAML parsing or generation task.
%endif


%if %{dual_life} || %{rebuild_from_scratch}
%package Data-Dumper
Summary:        Stringify perl data structures, suitable for printing and eval
License:        GPL+ or Artistic
Epoch:          0
Version:        2.174
Requires:       %perl_compat
Requires:       perl(Scalar::Util)
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
%gendep_perl_Data_Dumper
%endif

%description Data-Dumper
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The content of each
variable is output in a single Perl statement. Handles self-referential
structures correctly.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package DB_File
Summary:        Perl5 access to Berkeley DB version 1.x
License:        GPL+ or Artistic
Epoch:          0
Version:        1.843
Requires:       %perl_compat
Requires:       perl(Fcntl)
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
%gendep_perl_DB_File
%endif
Conflicts:      perl < 4:5.16.3-264

%description DB_File
DB_File is a module which allows Perl programs to make use of the facilities
provided by Berkeley DB version 1.x (if you have a newer version of DB, you
will be limited to functionality provided by interface of version 1.x). The
interface defined here mirrors the Berkeley DB interface closely.
%endif

%package Devel-Peek
Summary:        A data debugging tool for the XS programmer
License:        GPL+ or Artistic
Epoch:          0
Version:        1.28
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Devel_Peek
%endif
Conflicts:      perl < 4:5.22.0-351

%description Devel-Peek
Devel::Peek contains functions which allows raw Perl data types to be
manipulated from a Perl script. This is used by those who do XS programming to
check that the data they are sending from C to Perl looks as they think it
should look.

%if %{dual_life} || %{rebuild_from_scratch}
%package Devel-PPPort
Summary:        Perl Pollution Portability header generator
License:        GPL+ or Artistic
Epoch:          0
Version:        3.52
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Devel_PPPort
%endif
Conflicts:      perl < 4:5.20.1-310

%description Devel-PPPort
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C name space
environment (reduced pollution). The header file written by this module,
typically ppport.h, attempts to bring some of the newer Perl API features
to older versions of Perl, so that you can worry less about keeping track
of old releases, but users can still reap the benefit.
%endif

%package Devel-SelfStubber
Summary:        Generate stubs for a SelfLoading module
License:        GPL+ or Artistic
Epoch:          0
Version:        1.06
BuildArch:      noarch
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Devel_SelfStubber
%endif
Conflicts:      perl < 4:5.22.0-351

%description Devel-SelfStubber
Devel::SelfStubber prints the stubs you need to put in the module before the
__DATA__ token (or you can get it to print the entire module with stubs
correctly placed). The stubs ensure that if a method is called, it will get
loaded. They are needed specifically for inherited autoloaded methods.

%if %{dual_life} || %{rebuild_from_scratch}
%package Digest
Summary:        Modules that calculate message digests
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          0
Version:        1.17
BuildArch:      noarch
Requires:       %perl_compat
Requires:       perl(MIME::Base64)
%if %{defined perl_bootstrap}
%gendep_perl_Digest
%endif

%description Digest
The Digest:: modules calculate digests, also called "fingerprints" or
"hashes", of some data, called a message. The digest is (usually)
some small/fixed size string. The actual size of the digest depend of
the algorithm used. The message is simply a sequence of arbitrary
bytes or bits.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Digest-MD5
Summary:        Perl interface to the MD5 Algorithm
License:        (GPL+ or Artistic) and BSD
# Epoch bump for clean upgrade over old standalone package
Epoch:          0
Version:        2.55
Requires:       %perl_compat
Requires:       perl(XSLoader)
# Recommended
Requires:       perl(Digest::base) >= 1.00
%if %{defined perl_bootstrap}
%gendep_perl_Digest_MD5
%endif

%description Digest-MD5
The Digest::MD5 module allows you to use the RSA Data Security Inc. MD5
Message Digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 128-bit
"fingerprint" or "message digest" of the input.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Digest-SHA
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        6.02
Requires:       %perl_compat
Requires:       perl(Carp)
# Recommended
Requires:       perl(Digest::base)
%if %{defined perl_bootstrap}
%gendep_perl_Digest_SHA
%endif

%description Digest-SHA
Digest::SHA is a complete implementation of the NIST Secure Hash
Standard.  It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests.  The
module can handle all types of input, including partial-byte data.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Encode
Summary:        Character encodings in Perl
License:        (GPL+ or Artistic) and Artistic 2.0 and UCD
Epoch:          4
Version:        3.01
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Encode
%endif
Conflicts:      perl < 4:5.16.2-256

%description Encode
The Encode module provides the interface between Perl strings and the rest
of the system. Perl strings are sequences of characters.

%package encoding
Summary:        Write your Perl script in non-ASCII or non-UTF-8
License:        GPL+ or Artistic
Epoch:          4
Version:        2.22
# Keeping this sub-package arch-specific because it installs files into
# arch-specific directories.
Requires:       %perl_compat
Requires:       perl(Carp)
# Config not needed on perl ≥ 5.008
# Consider Filter::Util::Call as mandatory, bug #1165183, CPAN RT#100427
Requires:       perl(Filter::Util::Call)
# I18N::Langinfo is optional
# PerlIO::encoding is optional
Requires:       perl(utf8)
%if %{defined perl_bootstrap}
%gendep_perl_encoding
%endif
Conflicts:      perl-Encode < 2:2.60-314

%description encoding
With the encoding pragma, you can write your Perl script in any encoding you
like (so long as the Encode module supports it) and still enjoy Unicode
support.

However, this encoding module is deprecated under perl 5.18. It uses
a mechanism provided by perl that is deprecated under 5.18 and higher, and may
be removed in a future version.

The easiest and the best alternative is to write your script in UTF-8.

%package Encode-devel
Summary:        Character encodings in Perl
License:        (GPL+ or Artistic) and UCD
Epoch:          4
Version:        3.01
Requires:       %perl_compat
Requires:       %{name}-Encode = %{epoch}:%{version}-%{release}
Recommends:     perl-devel
%if %{defined perl_bootstrap}
%gendep_perl_Encode_devel
%endif
BuildArch:      noarch

%description Encode-devel
enc2xs builds a Perl extension for use by Encode from either Unicode Character
Mapping files (.ucm) or Tcl Encoding Files (.enc). You can use enc2xs to add
your own encoding to perl. No knowledge of XS is necessary.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Env
Summary:        Perl module that imports environment variables as scalars or arrays
License:        GPL+ or Artistic
Epoch:          0
Version:        1.04
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Env
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-265

%description Env
Perl maintains environment variables in a special hash named %%ENV. For when
this access method is inconvenient, the Perl module Env allows environment
variables to be treated as scalar or array variables.
%endif

%package Errno
Summary:        System errno constants
License:        GPL+ or Artistic
Epoch:          0
Version:        1.30
Requires:       %perl_compat
# Errno.pm bakes in kernel version at build time and compares it against
# $Config{osvers} at run time. Match exact interpreter build. Bug #1393421.
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_Errno
%endif
Conflicts:      perl < 4:5.22.0-351

%description Errno
"Errno" defines and conditionally exports all the error constants defined in
your system "errno.h" include file. It has a single export tag, ":POSIX",
which will export all POSIX defined error numbers.

%if %{dual_life} || %{rebuild_from_scratch}
%package experimental
Summary:        Experimental features made easy
License:        GPL+ or Artistic
Epoch:          0
Version:        0.020
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_experimental
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.20.0-303

%description experimental
This pragma provides an easy and convenient way to enable or disable
experimental features.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Exporter
Summary:        Implements default import method for modules
License:        GPL+ or Artistic
Epoch:          0
Version:        5.73
Requires:       %perl_compat
Requires:       perl(Carp) >= 1.05
%if %{defined perl_bootstrap}
%gendep_perl_Exporter
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-265

%description Exporter
The Exporter module implements an import method which allows a module to
export functions and variables to its users' name spaces. Many modules use
Exporter rather than implementing their own import method because Exporter
provides a highly flexible interface, with an implementation optimized for
the common case.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-CBuilder
Summary:        Compile and link C code for Perl modules
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.280231
BuildArch:      noarch
# C and C++ compilers are highly recommended because compiling code is the
# purpose of ExtUtils::CBuilder, bug #1547165
#Requires:       gcc
#Requires:       gcc-c++
Requires:       perl-devel
Requires:       %perl_compat
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Mksymlists)
Requires:       perl(File::Spec) >= 3.13
Requires:       perl(Perl::OSType) >= 1
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_CBuilder
%endif

%description ExtUtils-CBuilder
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-Command
Summary:        Perl routines to replace common UNIX commands in Makefiles
License:        GPL+ or Artistic
Epoch:          1
Version:        7.34
BuildArch:      noarch
Requires:       %perl_compat
Conflicts:      perl < 4:5.20.1-312
Requires:       perl(File::Find)
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_Command
%endif

%description ExtUtils-Command
This Perl module is used to replace common UNIX commands. In all cases the
functions work with @ARGV rather than taking arguments. This makes them
easier to deal with in Makefiles.
%endif

%package ExtUtils-Embed
Summary:        Utilities for embedding Perl in C/C++ applications
License:        GPL+ or Artistic
Epoch:          0
Version:        1.35
Requires:       perl-devel
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_Embed
%endif
BuildArch:      noarch

%description ExtUtils-Embed
Utilities for embedding Perl in C/C++ applications.


%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-Install
Summary:        Install files from here to there
License:        GPL+ or Artistic
Epoch:          0
Version:        2.14
BuildArch:      noarch
Requires:       %perl_compat
Requires:       perl(Data::Dumper)
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_Install
%endif

%description ExtUtils-Install
Handles the installing and uninstalling of perl modules, scripts, man
pages, etc.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-MakeMaker
Summary:        Create a module Makefile
License:        GPL+ or Artistic
Epoch:          2
Version:        7.34
# These dependencies are weak in order to relieve building noarch
# packages from perl-devel and gcc. See bug #1547165.
# If an XS module is built, the generated Makefile executes gcc.
Recommends:     gcc
# If an XS module is built, code generated from XS will be compiled and it
# includes Perl header files.
Recommends:     perl-devel
Requires:       %perl_compat
Requires:       perl(Data::Dumper)
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Command)
Requires:       perl(ExtUtils::Install)
Requires:       perl(ExtUtils::Manifest)
Requires:       perl(File::Find)
Requires:       perl(Getopt::Long)
# Optional Pod::Man is needed for generating manual pages from POD
Requires:       perl(Pod::Man)
Requires:       perl(POSIX)
Requires:       perl(Test::Harness)
Requires:       perl(version)
# If an XS module is compiled, xsubpp(1) is needed
Requires:       perl-ExtUtils-ParseXS
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_MakeMaker
%endif
BuildArch:      noarch

# Filter false DynaLoader provides. Versioned perl(DynaLoader) keeps
# unfiltered on perl package, no need to reinject it.
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader\\)\\s*$
%global __provides_exclude %__provides_exclude|^perl\\(ExtUtils::MakeMaker::_version\\)

%description ExtUtils-MakeMaker
Create a module Makefile.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-Manifest
Summary:        Utilities to write and check a MANIFEST file
License:        GPL+ or Artistic
Epoch:          1
Version:        1.72
Requires:       %perl_compat
Requires:       perl(File::Path)
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_Manifest
%endif
BuildArch:      noarch

%description ExtUtils-Manifest
%{summary}.
%endif

%package ExtUtils-Miniperl
Summary:        Write the C code for perlmain.c
License:        GPL+ or Artistic
Epoch:          0
Version:        1.09
Requires:       perl-devel
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_Miniperl
%endif
BuildArch:      noarch

%description ExtUtils-Miniperl
writemain() takes an argument list of directories containing archive libraries
that relate to perl modules and should be linked into a new perl binary. It
writes a corresponding perlmain.c file that is a plain C file containing all
the bootstrap code to make the If the first argument to writemain() is a
reference to a scalar it is used as the file name to open for output. Any other
reference is used as the file handle to write to. Otherwise output defaults to
STDOUT.

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-MM-Utils
Summary:        ExtUtils::MM methods without dependency on ExtUtils::MakeMaker
License:        GPL+ or Artistic
Epoch:          1
# Real version 7.11
# Dual-life ExtUtils-MakeMaker generate it with its version
Version:        7.34
BuildArch:      noarch
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_MM_Utils
%endif

%description ExtUtils-MM-Utils
This is a collection of ExtUtils::MM subroutines that are used by many
other modules but that do not need full-featured ExtUtils::MakeMaker. The
issue with ExtUtils::MakeMaker is it pulls in Perl header files and that
is an overkill for small subroutines.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-ParseXS
Summary:        Module and a script for converting Perl XS code into C code
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        3.40
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_ExtUtils_ParseXS
%endif
BuildArch:      noarch

%description ExtUtils-ParseXS
ExtUtils::ParseXS will compile XS code into C code by embedding the constructs
necessary to let C functions manipulate Perl values and creates the glue
necessary to let Perl access those functions.
%endif


%if %{dual_life} || %{rebuild_from_scratch}
%package File-Fetch
Summary:        Generic file fetching mechanism
License:        GPL+ or Artistic
Epoch:          0
Version:        0.56
Requires:       perl(IPC::Cmd) >= 0.36
Requires:       perl(Module::Load::Conditional) >= 0.04
Requires:       perl(Params::Check) >= 0.07
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_File_Fetch
%endif
BuildArch:      noarch

%description File-Fetch
File::Fetch is a generic file fetching mechanism.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package File-Path
Summary:        Create or remove directory trees
License:        GPL+ or Artistic
Epoch:          0
Version:        2.16
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_File_Path
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-265

%description File-Path
This module provides a convenient way to create directories of arbitrary
depth and to delete an entire directory subtree from the file system.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package File-Temp
Summary:        Return name and handle of a temporary file safely
License:        GPL+ or Artistic
Epoch:          1
# Normalized version
Version:        0.230.900
Requires:       %perl_compat
BuildArch:      noarch
Requires:       perl(File::Path) >= 2.06
Requires:       perl(POSIX)
%if %{defined perl_bootstrap}
%gendep_perl_File_Temp
%endif
Conflicts:      perl < 4:5.16.2-265

%description File-Temp
File::Temp can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface. The
File::Temp constructor or the tempfile() function can be used to return the
name and the open file handle of a temporary file. The tempdir() function
can be used to create a temporary directory.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
# FIXME Filter-Simple? version?
%package Filter
Summary:        Perl source filters
License:        GPL+ or Artistic
Epoch:          2
Version:        1.59
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Filter
%endif

%description Filter
Source filters alter the program text of a module before Perl sees it, much as
a C preprocessor alters the source text of a C program before the compiler
sees it.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Filter-Simple
Summary:        Simplified Perl source filtering
License:        GPL+ or Artistic
Epoch:          0
Version:        0.95
BuildArch:      noarch
Requires:       %perl_compat
Conflicts:      perl < 4:5.20.1-312
Requires:       perl(Text::Balanced) >= 1.97
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
%gendep_perl_Filter_Simple
%endif

%description Filter-Simple
The Filter::Simple Perl module provides a simplified interface to
Filter::Util::Call; one that is sufficient for most common cases.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Getopt-Long
Summary:        Extended processing of command line options
License:        GPLv2+ or Artistic
Epoch:          1
Version:        2.50
Requires:       %perl_compat
Requires:       perl(overload)
Requires:       perl(Text::ParseWords)
# Recommended:
Requires:       perl(Pod::Usage) >= 1.14
%if %{defined perl_bootstrap}
%gendep_perl_Getopt_Long
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-268

%description Getopt-Long
The Getopt::Long module implements an extended getopt function called
GetOptions(). It parses the command line from @ARGV, recognizing and removing
specified options and their possible values.  It adheres to the POSIX syntax
for command line options, with GNU extensions. In general, this means that
options have long names instead of single letters, and are introduced with
a double dash "--". Support for bundling of command line options, as was the
case with the more traditional single-letter approach, is provided but not
enabled by default.
%endif

%package IO
Summary:        Perl input/output modules
License:        GPL+ or Artistic
Epoch:          0
Version:        1.40
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_IO
%endif
Conflicts:      perl < 4:5.22.0-351

%description IO
This is a collection of Perl input/output modules.

%if %{dual_life} || %{rebuild_from_scratch}
%package IO-Compress
Summary:        IO::Compress wrapper for modules
License:        GPL+ or Artistic
Epoch:          0
Version:        2.084
Requires:       %perl_compat
Obsoletes:      perl-Compress-Zlib <= 2.020
Provides:       perl(IO::Uncompress::Bunzip2)
%if %{defined perl_bootstrap}
%gendep_perl_IO_Compress
%endif
BuildArch:      noarch

%description IO-Compress
This module is the base class for all IO::Compress and IO::Uncompress modules.
This module is not intended for direct use in application code. Its sole
purpose is to to be sub-classed by IO::Compress modules.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package IO-Socket-IP
Summary:        Drop-in replacement for IO::Socket::INET supporting both IPv4 and IPv6
License:        GPL+ or Artistic
Epoch:          0
Version:        0.39
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_IO_Socket_IP
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.20.0-303

%description IO-Socket-IP
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, as a drop-in replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way.
%endif

%package IO-Zlib
Summary:        Perl IO:: style interface to Compress::Zlib
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        1.10
Requires:       perl(Compress::Zlib)
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_IO_Zlib
%endif
BuildArch:      noarch

%description IO-Zlib
This modules provides an IO:: style interface to the Compress::Zlib package.
The main advantage is that you can use an IO::Zlib object in much the same way
as an IO::File object so you can have common code that doesn't know which sort
of file it is using.


%if %{dual_life} || %{rebuild_from_scratch}
%package IPC-Cmd
Summary:        Finding and running system commands made easy
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          2
Version:        1.02
Requires:       perl(ExtUtils::MM::Utils)
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_IPC_Cmd
%endif
BuildArch:      noarch

%description IPC-Cmd
IPC::Cmd allows you to run commands, interactively if desired, in a platform
independent way, but have them still work.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package IPC-SysV
Summary:        Object interface to System V IPC
License:        GPL+ or Artistic
Epoch:          0
Version:        2.07
Requires:       %perl_compat
Requires:       perl(DynaLoader)
%if %{defined perl_bootstrap}
%gendep_perl_IPC_SysV
%endif
Conflicts:      perl < 4:5.22.0-351

%description IPC-SysV
This is an object interface for System V messages, semaphores, and
inter-process calls.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package HTTP-Tiny
Summary:        A small, simple, correct HTTP/1.1 client
License:        GPL+ or Artistic
Epoch:          0
Version:        0.076
Requires:       perl(bytes)
Requires:       perl(Carp)
Requires:       perl(IO::Socket)
Requires:       perl(Time::Local)
%if %{defined perl_bootstrap}
%gendep_perl_HTTP_Tiny
%endif
BuildArch:      noarch

%description HTTP-Tiny
This is a very simple HTTP/1.1 client, designed primarily for doing simple GET 
requests without the overhead of a large framework like LWP::UserAgent.
It is more correct and more complete than HTTP::Lite. It supports proxies 
(currently only non-authenticating ones) and redirection. It also correctly 
resumes after EINTR.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package JSON-PP
Summary:        JSON::XS compatible pure-Perl module
Epoch:          1
Version:        4.02
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       %perl_compat 
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Requires:       perl(Scalar::Util)
Requires:       perl(subs)
%if %{defined perl_bootstrap}
%gendep_perl_JSON_PP
%endif
Conflicts:      perl-JSON < 2.50

%description JSON-PP
JSON::XS is the fastest and most proper JSON module on CPAN. It is written by
Marc Lehmann in C, so must be compiled and installed in the used environment.
JSON::PP is a pure-Perl module and is compatible with JSON::XS.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package libnet
Summary:        Perl clients for various network protocols
License:        (GPL+ or Artistic) and Artistic
Epoch:          0
Version:        3.11
Requires:       %perl_compat
Requires:       perl(File::Basename)
Requires:       perl(IO::Socket) >= 1.05
# Prefer IO::Socket::IP over IO::Socket::INET6 and IO::Socket::INET
Requires:       perl(IO::Socket::IP) >= 0.20
Requires:       perl(POSIX)
Requires:       perl(Socket) >= 2.016
Requires:       perl(utf8)
%if %{defined perl_bootstrap}
%gendep_perl_libnet
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347

%description libnet
This is a collection of Perl modules which provides a simple and
consistent programming interface (API) to the client side of various
protocols used in the internet community.
%endif

%package libnetcfg
Summary:        Configure libnet
License:        GPL+ or Artistic
Epoch:          %perl_epoch
Version:        %perl_version
# Net::Config is optional
BuildArch:      noarch
%if %{defined perl_bootstrap}
%gendep_perl_libnetcfg
%endif
Conflicts:      perl-devel < 4:5.22.0-347

%description libnetcfg
The libnetcfg utility can be used to configure the libnet.

%if %{dual_life} || %{rebuild_from_scratch}
%package Locale-Maketext
Summary:        Framework for localization
License:        GPL+ or Artistic
Epoch:          0
Version:        1.29
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Locale_Maketext
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-268

%description Locale-Maketext
It is a common feature of applications (whether run directly, or via the Web)
for them to be "localized" -- i.e., for them to present an English interface
to an English-speaker, a German interface to a German-speaker, and so on for
all languages it's programmed with. Locale::Maketext is a framework for
software localization; it provides you with the tools for organizing and
accessing the bits of text and text-processing code that you need for
producing localized applications.
%endif

%package Locale-Maketext-Simple
Summary:        Simple interface to Locale::Maketext::Lexicon
License:        MIT
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.21
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Locale_Maketext_Simple
%endif
BuildArch:      noarch

%description Locale-Maketext-Simple
This module is a simple wrapper around Locale::Maketext::Lexicon, designed
to alleviate the need of creating Language Classes for module authors.

%if %{dual_life} || %{rebuild_from_scratch}
%package Math-BigInt
Summary:        Arbitrary-size integer and float mathematics
License:        GPL+ or Artistic
Epoch:          1
# Real version 1.999816
Version:        1.9998.16
Requires:       %perl_compat
Requires:       perl(Carp)
# File::Spec not used on recent perl
%if %{defined perl_bootstrap}
%gendep_perl_Math_BigInt
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347

# Do not export unversioned module
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::BigInt\\)\\s*$

%description Math-BigInt
This provides Perl modules for arbitrary-size integer and float mathematics.

%package Math-BigInt-FastCalc
Summary:        Math::BigInt::Calc XS implementation
License:        GPL+ or Artistic
Epoch:          0
# Version normalized to dot format
# Real version 0.5008
Version:        0.500.800
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Math_BigInt_FastCalc
%endif
Conflicts:      perl < 4:5.22.0-348

%description Math-BigInt-FastCalc
This package provides support for faster big integer calculations.

%package Math-BigRat
Summary:        Arbitrary big rational numbers
License:        GPL+ or Artistic
Epoch:          0
# Real version 0.2614
Version:        0.2614
Requires:       %perl_compat
Requires:       perl(Math::BigInt)
%if %{defined perl_bootstrap}
%gendep_perl_Math_BigRat
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-348

%description Math-BigRat
Math::BigRat complements Math::BigInt and Math::BigFloat by providing support
for arbitrary big rational numbers.
%endif

%package Math-Complex
Summary:        Complex numbers and trigonometric functions
License:        GPL+ or Artistic
Epoch:          0
Version:        1.59
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Math_Complex
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-348

%description Math-Complex
This package lets you create and manipulate complex numbers. By default, Perl
limits itself to real numbers, but an extra "use" statement brings full
complex support, along with a full set of mathematical functions typically
associated with and/or extended to complex numbers.

%package Memoize
Summary:        Transparently speed up functions by caching return values
License:        GPL+ or Artistic
Epoch:          0
Version:        1.03
Requires:       %perl_compat
# Keep Time::HiRes optional
%if %{defined perl_bootstrap}
%gendep_perl_Memoize
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-350

%description Memoize
Memoizing a function makes it faster by trading space for time. It does
this by caching the return values of the function in a table. If you call
the function again with the same arguments, memoize jumps in and gives
you the value out of the table, instead of letting the function compute
the value all over again.

%if %{dual_life} || %{rebuild_from_scratch}
%package MIME-Base64
Summary:        Encoding and decoding of Base64 and quoted-printable strings
# cpan/MIME-Base64/Base64.xs:   (GPL+ or Artistic) and MIT (Bellcore's part)
# Other files:                  GPL+ or Artistic
License:        (GPL+ or Artistic) and MIT
Epoch:          0
Version:        3.15
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_MIME_Base64
%endif
Conflicts:      perl < 4:5.22.0-347

%description MIME-Base64
This package contains a Base64 encoder/decoder and a quoted-printable
encoder/decoder. These encoding methods are specified in RFC 2045 - MIME
(Multipurpose Internet Mail Extensions).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Module-CoreList
Summary:        What modules are shipped with versions of perl
License:        GPL+ or Artistic
Epoch:          1
Version:        5.20190522
Requires:       %perl_compat
Requires:       perl(List::Util)
Requires:       perl(version) >= 0.88
%if %{defined perl_bootstrap}
%gendep_perl_Module_CoreList
%endif
BuildArch:      noarch

%description Module-CoreList
Module::CoreList provides information on which core and dual-life modules
are shipped with each version of perl.


%package Module-CoreList-tools
Summary:        Tool for listing modules shipped with perl
License:        GPL+ or Artistic
Epoch:          1
Version:        5.20190522
Requires:       %perl_compat
Requires:       perl(feature)
Requires:       perl(version) >= 0.88
Requires:       perl-Module-CoreList = %{epoch}:%{version}-%{release}
%if %{defined perl_bootstrap}
%gendep_perl_Module_CoreList_tools
%endif
# The files were distributed with perl.spec's subpackage
# perl-Module-CoreList <= 1:5.020001-309
Conflicts:      perl-Module-CoreList < 1:5.020001-310
BuildArch:      noarch

%description Module-CoreList-tools
This package provides a corelist(1) tool which can be used to query what
modules were shipped with given perl version.
%endif


%if %{dual_life} || %{rebuild_from_scratch}
%package Module-Load
Summary:        Runtime require of both modules and files
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.34
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Module_Load
%endif
BuildArch:      noarch

%description Module-Load
Module::Load eliminates the need to know whether you are trying to require
either a file or a module.
%endif


%if %{dual_life} || %{rebuild_from_scratch}
%package Module-Load-Conditional
Summary:        Looking up module information / loading at runtime
License:        GPL+ or Artistic
Epoch:          0
Version:        0.68
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Module_Load_Conditional
%endif
BuildArch:      noarch

%description Module-Load-Conditional
Module::Load::Conditional provides simple ways to query and possibly load any
of the modules you have installed on your system during runtime.
%endif


%package Module-Loaded
Summary:        Mark modules as loaded or unloaded
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.08
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Module_Loaded
%endif
BuildArch:      noarch

%description Module-Loaded
When testing applications, often you find yourself needing to provide
functionality in your test environment that would usually be provided by
external modules. Rather than munging the %%INC by hand to mark these external
modules as loaded, so they are not attempted to be loaded by perl, this module
offers you a very simple way to mark modules as loaded and/or unloaded.


%if %{dual_life} || %{rebuild_from_scratch}
%package Module-Metadata
Summary:        Gather package and POD information from perl module files
Epoch:          0
Version:        1.000036
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Module_Metadata
%endif

%description Module-Metadata
Gather package and POD information from perl module files
%endif

%package Net-Ping
Summary:        Check a remote host for reachability
License:        GPL+ or Artistic
Epoch:          0
Version:        2.71
Requires:       %perl_compat
# Keep Net::Ping::External optional
%if %{defined perl_bootstrap}
%gendep_perl_Net_Ping
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-350

%description Net-Ping
Net::Ping module contains methods to test the reachability of remote hosts on
a network.

%package open
Summary:        Perl pragma to set default PerlIO layers for input and output
License:        GPL+ or Artistic
Epoch:          0
Version:        1.11
Requires:       %perl_compat
Requires:       perl(Carp)
Requires:       perl(Encode)
Requires:       perl(encoding)
%if %{defined perl_bootstrap}
%gendep_perl_open
%endif
Conflicts:      perl < 4:5.20.2-326
BuildArch:      noarch

%description open
The "open" pragma serves as one of the interfaces to declare default "layers"
(also known as "disciplines") for all I/O.

%if %{dual_life} || %{rebuild_from_scratch}
%package parent
Summary:        Establish an ISA relationship with base classes at compile time
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.237
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_parent
%endif
BuildArch:      noarch

%description parent
parent allows you to both load one or more modules, while setting up
inheritance from those modules at the same time. Mostly similar in effect to:

    package Baz;

    BEGIN {
        require Foo;
        require Bar;

        push @ISA, qw(Foo Bar);
    }
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Params-Check
Summary:        Generic input parsing/checking mechanism
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.38
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Params_Check
%endif
BuildArch:      noarch

%description Params-Check
Params::Check is a generic input parsing/checking mechanism.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package PathTools
Summary:        PathTools Perl module (Cwd, File::Spec)
License:        (GPL+ or Artistic) and BSD
Epoch:          0
Version:        3.78
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_PathTools
%endif

%description PathTools
PathTools Perl module (Cwd, File::Spec).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package perlfaq
Summary:        Frequently asked questions about Perl
# Code examples are Public Domain
License:        (GPL+ or Artistic) and Public Domain
Epoch:          0
Version:        5.20190126
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_perlfaq
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347

%description perlfaq
The perlfaq comprises several documents that answer the most commonly asked
questions about Perl and Perl programming.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package PerlIO-via-QuotedPrint
Summary:        PerlIO layer for quoted-printable strings
License:        GPL+ or Artistic
Epoch:          0
Version:        0.08
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_PerlIO_via_QuotedPrint
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347

%description PerlIO-via-QuotedPrint
This module implements a PerlIO layer that works on files encoded in the
quoted-printable format. It will decode from quoted-printable while
reading from a handle, and it will encode as quoted-printable while
writing to a handle.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Perl-OSType
Summary:        Map Perl operating system names to generic types
Version:        1.010
Epoch:          0
License:        GPL+ or Artistic
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Perl_OSType
%endif
BuildArch:      noarch

%description Perl-OSType
Modules that provide OS-specific behaviors often need to know if the current
operating system matches a more generic type of operating systems. For example,
'linux' is a type of 'Unix' operating system and so is 'freebsd'.
This module provides a mapping between an operating system name as given by $^O
and a more generic type. The initial version is based on the OS type mappings
provided in Module::Build and ExtUtils::CBuilder (thus, Microsoft operating
systems are given the type 'Windows' rather than 'Win32').
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Checker
Summary:        Check POD documents for syntax errors
Epoch:          4
Version:        1.73
License:        GPL+ or Artistic
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Pod_Checker
%endif
BuildArch:      noarch

%description Pod-Checker
Module and tools to verify POD documentation contents for compliance with the
Plain Old Documentation format specifications.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Escapes
Summary:        Resolve POD escape sequences
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        1.07
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Pod_Escapes
%endif
BuildArch:      noarch

%description Pod-Escapes
This module provides things that are useful in decoding Pod E<...> sequences.
%endif

%package Pod-Html
Summary:        Convert POD files to HTML
License:        GPL+ or Artistic
Epoch:          0
Version:        1.24
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Pod_Html
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-350

%description Pod-Html
This package converts files from POD format (see perlpod) to HTML format. It
can automatically generate indexes and cross-references, and it keeps a cache
of things it knows how to cross-reference.

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Parser
Summary:        Basic perl modules for handling Plain Old Documentation (POD)
License:        GPL+ or Artistic
Epoch:          0
Version:        1.63
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Pod_Parser
%endif
BuildArch:      noarch

%description Pod-Parser
This software distribution contains the packages for using Perl5 POD (Plain
Old Documentation). See the "perlpod" and "perlsyn" manual pages from your
Perl5 distribution for more information about POD.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Perldoc
Summary:        Look up Perl documentation in Pod format
License:        GPL+ or Artistic
Epoch:          0
# Real version 3.2801
Version:        3.28.01
%if %{with perl_enables_groff}
# Pod::Perldoc::ToMan executes roff
#Requires:       groff-base
%endif
Requires:       %perl_compat
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(HTTP::Tiny)
Requires:       perl(IO::Handle)
Requires:       perl(IPC::Open3)
# POD2::Base is optional
# Pod::Checker is not needed if Pod::Simple::Checker is available
Requires:       perl(Pod::Simple::Checker)
Requires:       perl(Pod::Simple::RTF) >= 3.16
Requires:       perl(Pod::Simple::XMLOutStream) >= 3.16
Requires:       perl(Text::ParseWords)
# Tk is optional
Requires:       perl(Symbol)
%if %{defined perl_bootstrap}
%gendep_perl_Pod_Perldoc
%endif
BuildArch:      noarch

%description Pod-Perldoc
perldoc looks up a piece of documentation in .pod format that is embedded
in the perl installation tree or in a perl script, and displays it via
"groff -man | $PAGER". This is primarily used for the documentation for
the perl library modules.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Simple
Summary:        Framework for parsing POD documentation
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        3.35
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Pod_Simple
%endif
BuildArch:      noarch

%description Pod-Simple
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Usage
Summary:        Print a usage message from embedded pod documentation
License:        GPL+ or Artistic
Epoch:          4
Version:        1.69
Requires:       %perl_compat
# Pod::Usage executes perldoc from perl-Pod-Perldoc by default
Requires:       perl-Pod-Perldoc
Requires:       perl(Pod::Text)
%if %{defined perl_bootstrap}
%gendep_perl_Pod_Usage
%endif
BuildArch:      noarch

%description Pod-Usage
pod2usage will print a usage message for the invoking script (using its
embedded POD documentation) and then exit the script with the desired exit
status. The usage message printed may have any one of three levels of
"verboseness": If the verbose level is 0, then only a synopsis is printed.
If the verbose level is 1, then the synopsis is printed along with a
description (if present) of the command line options and arguments. If the
verbose level is 2, then the entire manual page is printed.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package podlators
Summary:        Format POD source into various output formats
License:        (GPL+ or Artistic) and MIT
Epoch:          1
Version:        4.11
BuildArch:      noarch
Requires:       %perl_compat
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Pod::Simple) >= 3.06
%if %{defined perl_bootstrap}
%gendep_perl_podlators
%endif
Conflicts:      perl < 4:5.16.1-234

%description podlators
This package contains Pod::Man and Pod::Text modules which convert POD input
to *roff source output, suitable for man pages, or plain text.  It also
includes several sub-classes of Pod::Text for formatted output to terminals
with various capabilities.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Scalar-List-Utils
Summary:        A selection of general-utility scalar and list subroutines
License:        GPL+ or Artistic
Epoch:          3
Version:        1.50
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Scalar_List_Utils
%endif

%description Scalar-List-Utils
Scalar::Util and List::Util contain a selection of subroutines that people have
expressed would be nice to have in the perl core, but the usage would not
really be high enough to warrant the use of a keyword, and the size so small
such that being individual extensions would be wasteful.
%endif

%package SelfLoader
Summary:        Load functions only on demand
License:        GPL+ or Artistic
Epoch:          0
Version:        1.25
BuildArch:      noarch
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_SelfLoader
%endif
Conflicts:      perl < 4:5.22.0-351

%description SelfLoader
This Perl module tells its users that functions in a package are to be
autoloaded from after the "__DATA__" token. See also "Autoloading" in
perlsub.

%if %{dual_life} || %{rebuild_from_scratch}
%package Socket
Summary:        C socket.h defines and structure manipulators
License:        GPL+ or Artistic
Epoch:          4
Version:        2.027
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Socket
%endif

%description Socket
This module is just a translation of the C socket.h file.  Unlike the old
mechanism of requiring a translated socket.ph file, this uses the h2xs program
(see the Perl source distribution) and your native C compiler.  This means
that it has a far more likely chance of getting the numbers right.  This
includes all of the commonly used pound-defines like AF_INET, SOCK_STREAM, etc.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Storable
Summary:        Persistence for Perl data structures
License:        GPL+ or Artistic
Epoch:          1
Version:        3.15
Requires:       %perl_compat
# Carp substitutes missing Log::Agent
Requires:       perl(Carp)
Requires:       perl(Config)
# Fcntl is optional, but locking is good
Requires:       perl(Fcntl)
Requires:       perl(IO::File)
%if %{defined perl_bootstrap}
%gendep_perl_Storable
%endif
Conflicts:      perl < 4:5.16.3-274

%description Storable
The Storable package brings persistence to your Perl data structures
containing scalar, array, hash or reference objects, i.e. anything that
can be conveniently stored to disk and retrieved at a later time.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Sys-Syslog
Summary:        Perl interface to the UNIX syslog(3) calls
License:        GPL+ or Artistic
Epoch:          0
Version:        0.35
Requires:       %perl_compat
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
%gendep_perl_Sys_Syslog
%endif
Conflicts:      perl < 4:5.16.3-269

%description Sys-Syslog
Sys::Syslog is an interface to the UNIX syslog(3) function. Call syslog() with
a string priority and a list of printf() arguments just like at syslog(3).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Term-ANSIColor
Summary:        Color screen output using ANSI escape sequences
License:        GPL+ or Artistic
Epoch:          0
Version:        4.06
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_Term_ANSIColor
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.18.2-302

%description Term-ANSIColor
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility functions uncolor(),
colorstrip(), colorvalid(), and coloralias(), which have to be explicitly
imported to be used.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Term-Cap
Summary:        Perl termcap interface
License:        GPL+ or Artistic
Epoch:          0
Version:        1.17
Requires:       %perl_compat
# ncurses for infocmp tool
#Requires:       ncurses
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_Term_Cap
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347

%description Term-Cap
These are low-level functions to extract and use capabilities from a terminal
capability (termcap) database.
%endif

%package Test
Summary:        Simple framework for writing test scripts
License:        GPL+ or Artistic
Epoch:          0
Version:        1.31
Requires:       %perl_compat
# Algorithm::Diff 1.15 is optional
Requires:       perl(File::Temp)
%if %{defined perl_bootstrap}
%gendep_perl_Test
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-351

%description Test
The Test Perl module simplifies the task of writing test files for Perl modules,
such that their output is in the format that Test::Harness expects to see.

%if %{dual_life} || %{rebuild_from_scratch}
%package Test-Harness
Summary:        Run Perl standard test scripts with statistics
License:        GPL+ or Artistic
Epoch:          1
Version:        3.42
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Test_Harness
%endif
BuildArch:      noarch

%description Test-Harness
Run Perl standard test scripts with statistics.
Use TAP::Parser, Test::Harness package was whole rewritten.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Test-Simple
Summary:        Basic utilities for writing tests
License:        (GPL+ or Artistic) and CC0 and Public Domain
Epoch:          3
Version:        1.302162
Requires:       %perl_compat
Requires:       perl(Data::Dumper)
%if %{defined perl_bootstrap}
%gendep_perl_Test_Simple
%endif
BuildArch:      noarch

%description Test-Simple
Basic utilities for writing tests.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Text-Balanced
Summary:        Extract delimited text sequences from strings
License:        GPL+ or Artistic
Epoch:          0
Version:        2.03
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Text_Balanced
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347

%description Text-Balanced
These Perl subroutines may be used to extract a delimited substring, possibly
after skipping a specified prefix string.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Text-ParseWords
Summary:        Parse text into an array of tokens or array of arrays
License:        GPL+ or Artistic
Epoch:          0
Version:        3.30
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_Text_ParseWords
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-256

%description Text-ParseWords
Parse text into an array of tokens or array of arrays.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Text-Tabs+Wrap
Summary:        Expand tabs and do simple line wrapping
License:        TTWL
Epoch:          0
Version:        2013.0523
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Text_Tabs_Wrap
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.20.2-325

%description Text-Tabs+Wrap
Text::Tabs performs the same job that the UNIX expand(1) and unexpand(1)
commands do: adding or removing tabs from a document.

Text::Wrap::wrap() will reformat lines into paragraphs. All it does is break
up long lines, it will not join short lines together.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Thread-Queue
Summary:        Thread-safe queues
License:        GPL+ or Artistic
Epoch:          0
Version:        3.13
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_Thread_Queue
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-257

%description Thread-Queue
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Time-HiRes
Summary:        High resolution alarm, sleep, gettimeofday, interval timers
License:        GPL+ or Artistic
Epoch:          0
Version:        1.9760
Requires:       %perl_compat
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
%gendep_perl_Time_HiRes
%endif
Conflicts:      perl < 4:5.16.3-271

%description Time-HiRes
The Time::HiRes module implements a Perl interface to the usleep, nanosleep,
ualarm, gettimeofday, and setitimer/getitimer system calls, in other words,
high resolution time and timers.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Time-Local
Summary:        Efficiently compute time from local and GMT time
License:        GPL+ or Artistic
Epoch:          2
# Real version 1.28
Version:        1.280
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Time_Local
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-262

%description Time-Local
This module provides functions that are the inverse of built-in perl functions
localtime() and gmtime(). They accept a date as a six-element array, and
return the corresponding time(2) value in seconds since the system epoch
(Midnight, January 1, 1970 GMT on Unix, for example). This value can be
positive or negative, though POSIX only requires support for positive values,
so dates before the system's epoch may not work on all operating systems.
%endif

# Here's a terminator

%package Time-Piece
Summary:        Time objects from localtime and gmtime
License:        (GPL+ or Artistic) and BSD
Epoch:          0
Version:        1.33
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_Time_Piece
%endif

%description Time-Piece
The Time::Piece module replaces the standard localtime and gmtime functions
with implementations that return objects.  It does so in a backwards compatible
manner, so that using localtime or gmtime as documented in perlfunc still
behave as expected.

%if %{dual_life} || %{rebuild_from_scratch}
%package threads
Summary:        Perl interpreter-based threads
License:        GPL+ or Artistic
Epoch:          1
Version:        2.22
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_threads
%endif

%description threads
Since Perl 5.8, thread programming has been available using a model called
interpreter threads  which provides a new Perl interpreter for each thread,
and, by default, results in no data or state information being shared between
threads.

(Prior to Perl 5.8, 5005threads was available through the Thread.pm API. This
threading model has been deprecated, and was removed as of Perl 5.10.0.)

As just mentioned, all variables are, by default, thread local. To use shared
variables, you need to also load threads::shared.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package threads-shared
Summary:        Perl extension for sharing data structures between threads
License:        GPL+ or Artistic
Epoch:          0
Version:        1.60
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_threads_shared
%endif

%description threads-shared
By default, variables are private to each thread, and each newly created thread
gets a private copy of each existing variable. This module allows you to share
variables across different threads (and pseudo-forks on Win32). It is used
together with the threads module.  This module supports the sharing of the
following data types only: scalars and scalar refs, arrays and array refs, and
hashes and hash refs.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Unicode-Collate
Summary:        Unicode Collation Algorithm
License:        (GPL+ or Artistic) and Unicode
Epoch:          0
Version:        1.27
Requires:       %perl_compat
Requires:       perl(Unicode::Normalize)
%if %{defined perl_bootstrap}
%gendep_perl_Unicode_Collate
%endif
Conflicts:      perl < 4:5.22.0-347

%description Unicode-Collate
This package is Perl implementation of Unicode Technical Standard #10 (Unicode
Collation Algorithm).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Unicode-Normalize
Summary:        Unicode Normalization Forms
License:        GPL+ or Artistic
Epoch:          0
Version:        1.26
Requires:       %perl_compat
# unicore/CombiningClass.pl and unicore/Decomposition.pl from perl, perl is
# auto-detected.
%if %{defined perl_bootstrap}
%gendep_perl_Unicode_Normalize
%endif
Conflicts:      perl < 4:5.22.0-347

%description Unicode-Normalize
This package provides Perl functions that can convert strings into various
Unicode normalization forms as defined in Unicode Standard Annex #15.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package version
Summary:        Perl extension for Version Objects
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          7
# real version 0.9924
Version:        0.99.24
Requires:       %perl_compat
%if %{defined perl_bootstrap}
%gendep_perl_version
%endif
BuildArch:      noarch

%description version
Perl extension for Version Objects
%endif

%prep
%setup -q -n perl-%{perl_version}

%patch1 -p1
%ifarch %{multilib_64_archs}
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
# PATCH-perl-134329-Use-after-free-in-regcomp.c.patch is a binary patch
git init-db .
git config --replace-all gc.auto 0 # Prevent from racing with "rm -rf .git"
git config --replace-all user.email '<nobody@localhost>'
git config --replace-all user.name 'Nobody'
git add .
git commit --message 'Import'
git am < %{PATCH58}
rm -rf .git # Perl tests examine a git repository
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch200 -p1
%patch201 -p1

%patch300 -p1

%if !%{defined perl_bootstrap}
# Local patch tracking
perl -x patchlevel.h \
    'Didbs Patch1: irix changes for 5.30.0' \
    %{nil}
%endif

#copy the example script
install -m 0644 %{SOURCE5} .

#copy Pod-Html license clarification
cp %{SOURCE6} .

#
# Candidates for doc recoding (need case by case review):
# find . -name "*.pod" -o -name "README*" -o -name "*.pm" | xargs file -i | grep charset= | grep -v '\(us-ascii\|utf-8\)'
recode()
{
        iconv -f "${2:-iso-8859-1}" -t utf-8 < "$1" > "${1}_"
        touch -r "$1" "${1}_"
        mv -f "${1}_" "$1"
}
# TODO iconv fail on this one
##recode README.tw big5
#recode pod/perlebcdic.pod
#recode pod/perlhack.pod
#recode pod/perlhist.pod
#recode pod/perlthrtut.pod
#recode AUTHORS

find . -name \*.orig -exec rm -fv {} \;

# Configure Compress::Zlib to use system zlib
sed -i 's|BUILD_ZLIB      = True|BUILD_ZLIB      = False|
    s|INCLUDE         = ./zlib-src|INCLUDE         = %{_includedir}|
    s|LIB             = ./zlib-src|LIB             = %{_libdir}|' \
    cpan/Compress-Raw-Zlib/config.in

# Ensure that we never accidentally bundle zlib or bzip2
rm -rf cpan/Compress-Raw-Zlib/zlib-src
rm -rf cpan/Compress-Raw-Bzip2/bzip2-src
sed -i '/\(bzip2\|zlib\)-src/d' MANIFEST

#%if !%{with gdbm}
# Do not install anything requiring NDBM_File if NDBM is not available.
rm -rf 'cpan/Memoize/Memoize/NDBM_File.pm'
sed -i '\|cpan/Memoize/Memoize/NDBM_File.pm|d' MANIFEST
#%endif


%build
echo "RPM Build arch: %{_arch}"

# use "lib", not %%{_lib}, for privlib, sitelib, and vendorlib
# To build production version, we would need -DDEBUGGING=-g

# Perl INC path (perl -V) in search order:
# - /usr/local/share/perl5            -- for CPAN     (site lib)
# - /usr/local/lib[64]/perl5          -- for CPAN     (site arch)
# - /usr/share/perl5/vendor_perl      -- 3rd party    (vendor lib)
# - /usr/lib[64]/perl5/vendor_perl    -- 3rd party    (vendor arch)
# - /usr/share/perl5                  -- Fedora       (priv lib)
# - /usr/lib[64]/perl5                -- Fedora       (arch lib)

%global privlib     %{_prefix}/share/perl5
%global archlib     %{_libdir}/perl5

%global perl_vendorlib  %{privlib}/vendor_perl
%global perl_vendorarch %{archlib}/vendor_perl

%global perl_abi    %(echo '%{perl_version}' | sed 's/^\\([^.]*\\.[^.]*\\).*/\\1/')

# ldflags is not used when linking XS modules.
# Only ldflags is used when linking miniperl.
# Only ccflags and ldflags are used for Configure's compiler checks.
# Set optimize=none to prevent from injecting upstream's value.
cp %{_topdir}/SOURCES/perl.irix6_gcc_config.sh config.sh
perl -pi -e "s|DIDBSINSTALLPREFIX|%{_prefix}|g" config.sh
LIBDIR_REGEXP="s|%{_prefix}/lib/|%{_prefix}/%{_lib}/|g"
perl -pi -e "$LIBDIR_REGEXP" config.sh
CCFLAGS_REGEXP="s|^ccflags=.*$|ccflags='$RPM_OPT_FLAGS'|g"
perl -pi -e "$CCFLAGS_REGEXP" config.sh
LDFLAGS_REGEXP="s|^ldflags=.*$|ldflags='$RPM_LD_FLAGS -L%{_libdir}'|g"
perl -pi -e "$LDFLAGS_REGEXP" config.sh
CCDLFLAGS_REGEXP="s|^ccdlflags=.*$|ccdlflags='-Wl,--enable-new-dtags $RPM_LD_FLAGS'|g"
perl -pi -e "$CCDLFLAGS_REGEXP" config.sh
LDDLFLAGS_REGEXP="s|^lddlflags=.*$|lddlflags='-shared $RPM_LD_FLAGS -L%{_libdir}'|g"
perl -pi -e "$LDDLFLAGS_REGEXP" config.sh
OPTFLAGS_REGEXP="s|^optimize=.*$|optimize='%{optflags}'|g"
perl -pi -e "$OPTFLAGS_REGEXP" config.sh
/usr/bin/env sh Configure -S \
        -Doptimize=" " \
        -Dccflags="$RPM_OPT_FLAGS" \
        -Dldflags="$RPM_LD_FLAGS" \
        -Dccdlflags="-Wl,--enable-new-dtags $RPM_LD_FLAGS" \
        -Dlddlflags="-shared $RPM_LD_FLAGS" \
        -Dshrpdir="%{_libdir}" \
        -DDEBUGGING=-g \
        -Dversion=%{perl_version} \
        -Dmyhostname=localhost \
        -Dperladmin=root@localhost \
        -Dcc='%{__cc}' \
        -Dcf_by='SGUG' \
        -Dprefix=%{_prefix} \
%if %{without perl_enables_groff}
        -Dman1dir="%{_mandir}/man1" \
        -Dman3dir="%{_mandir}/man3" \
%endif
        -Dvendorprefix=%{_prefix} \
        -Dsiteprefix=%{_prefix}/local \
        -Dsitelib="%{_prefix}/share/perl5/%{perl_abi}" \
        -Dsitearch="%{_prefix}/%{_lib}/perl5/%{perl_abi}" \
        -Dprivlib="%{privlib}" \
        -Dvendorlib="%{perl_vendorlib}" \
        -Darchlib="%{archlib}" \
        -Dvendorarch="%{perl_vendorarch}" \
        -Darchname=%{perl_archname} \
        -Duselargefiles \
        -Dman3ext=3pm


#        -Duseshrplib \
#        -Duselargefiles \
#        -Dman3ext=3pm \
#        -Duseperlio \
#        -Ubincompat5005 \
#        -Uversiononly \
#        -Dscriptdir='%{_bindir}' \
#        -Dusesitecustomize \
#        -Duse64bitint

# Force regen
#touch config.sh
#chmod u+x config.sh
#./config_h.SH
make depend

# -Duseshrplib creates libperl.so, -Ubincompat5005 help create DSO -> libperl.so

BUILD_BZIP2=0
BZIP2_LIB=%{_libdir}
export BUILD_BZIP2 BZIP2_LIB

# Prepapre a symlink from proper DSO name to libperl.so now so that new perl
# can be executed from make.
%global soname libperl.so.%{perl_abi}
test -L %soname || ln -s libperl.so %soname

LD_LIBRARYN32_PATH=%{_libdir}:$LD_LIBRARYN32_PATH make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%global build_archlib $RPM_BUILD_ROOT%{archlib}
%global build_privlib $RPM_BUILD_ROOT%{privlib}
%global build_bindir  $RPM_BUILD_ROOT%{_bindir}
%global new_perl LD_PRELOAD="%{build_archlib}/CORE/libperl.so" \\\
    LD_LIBRARYN32_PATH="%{build_archlib}/CORE" \\\
    PERL5LIB="%{build_archlib}:%{build_privlib}" \\\
    %{build_bindir}/perl

## Make proper DSO names, move libperl to standard path.
mv "%{build_archlib}/CORE/libperl.so" \
    "$RPM_BUILD_ROOT%{_libdir}/libperl.so.%{perl_version}"
ln -s "libperl.so.%{perl_version}" "$RPM_BUILD_ROOT%{_libdir}/%{soname}"
ln -s "libperl.so.%{perl_version}" "$RPM_BUILD_ROOT%{_libdir}/libperl.so"
# XXX: Keep symlink from original location because various code glues
# $archlib/CORE/$libperl to get the DSO.
ln -s "../../libperl.so.%{perl_version}" "%{build_archlib}/CORE/libperl.so"
# XXX: Remove the soname named file from CORE directory that was created as
# a symlink in build section and installed as a regular file by perl build
# system.
rm -f "%{build_archlib}/CORE/%{soname}"

install -p -m 755 utils/pl2pm %{build_bindir}/pl2pm

for i in asm/termios.h syscall.h syslimits.h syslog.h \
    sys/ioctl.h sys/socket.h sys/time.h wait.h
do
    %{new_perl} %{build_bindir}/h2ph -a -d %{build_archlib} $i || true
done

# vendor directories (in this case for third party rpms)
# perl doesn't create the auto subdirectory, but modules put things in it,
# so we need to own it.

mkdir -p $RPM_BUILD_ROOT%{perl_vendorarch}/auto
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}

#
# perl RPM macros
#
mkdir -p ${RPM_BUILD_ROOT}%{_rpmmacrodir}
install -p -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_rpmmacrodir}

#
# Core modules removal
#
# Dual-living binaries clashes on debuginfo files between perl and standalone
# packages. Excluding is not enough, we need to remove them. This is
# a work-around for rpmbuild bug #878863.
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
chmod -R u+w $RPM_BUILD_ROOT/*

# miniperl? As an interpreter? How odd. Anyway, a symlink does it:
rm %{build_privlib}/ExtUtils/xsubpp
ln -s ../../../bin/xsubpp %{build_privlib}/ExtUtils/

# Don't need the .packlist
rm %{build_archlib}/.packlist

# Do not distribute File::Spec::VMS as it works on VMS only (bug #973713)
# We cannot remove it in %%prep because dist/Cwd/t/Spec.t test needs it.
rm %{build_archlib}/File/Spec/VMS.pm
rm $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::VMS.3*

# Fix some manpages to be UTF-8
#mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
#pushd $RPM_BUILD_ROOT%{_mandir}/man1/
#  for i in perl588delta.1 perldelta.1 ; do
#    iconv -f MS-ANSI -t UTF-8 $i --output new-$i
#    rm $i
#    mv new-$i $i
#  done
#popd

# for now, remove Bzip2:
# Why? Now is missing Bzip2 files and provides
##find $RPM_BUILD_ROOT -name Bzip2 | xargs rm -r
##find $RPM_BUILD_ROOT -name '*B*zip2*'| xargs rm

# tests -- FIXME need to validate that this all works as expected
mkdir -p %{buildroot}%{perl5_testdir}/perl-tests

# "core"
tar -cf - t/ | ( cd %{buildroot}%{perl5_testdir}/perl-tests && tar -xf - )

# "dual-lifed"
for dir in `find ext/ -type d -name t -maxdepth 2` ; do

    tar -cf - $dir | ( cd %{buildroot}%{perl5_testdir}/perl-tests/t && tar -xf - )
done

# Normalize shell bangs in tests.
# brp-mangle-shebangs executed by rpm-build chokes on t/TEST.
%{new_perl} -MConfig -i -pn \
    -e 's"\A#!(?:perl|\./perl|/usr/bin/perl|/usr/bin/env perl)\b"$Config{startperl}"' \
    $(find %{buildroot}%{perl5_testdir}/perl-tests -type f)

%if %{with perl_enables_systemtap}
# Systemtap tapset install
mkdir -p %{buildroot}%{tapsetdir}
%ifarch %{multilib_64_archs}
%global libperl_stp libperl%{perl_version}-64.stp
%else
%global libperl_stp libperl%{perl_version}-32.stp
%endif

sed \
  -e "s|LIBRARY_PATH|%{_libdir}/%{soname}|" \
  %{SOURCE4} \
  > %{buildroot}%{tapsetdir}/%{libperl_stp}
%endif

# TODO: Canonicalize test files (rewrite intrerpreter path, fix permissions)
# XXX: We cannot rewrite ./perl before %%check phase. Otherwise the test
# would run against system perl at build-time.
# See __spec_check_pre global macro in macros.perl.
#T_FILES=`find %%{buildroot}%%{perl5_testdir} -type f -name '*.t'`
#%%fix_shbang_line $T_FILES
#%%{__chmod} +x $T_FILES
#%%{_fixperms} %%{buildroot}%%{perl5_testdir}
#
# lib/perl5db.t will fail if Term::ReadLine::Gnu is available
%check
%if %{with test}
%{new_perl} -I/lib regen/lib_cleanup.pl
pushd t
%{new_perl} -I../lib porting/customized.t --regen
popd
%if %{parallel_tests}
    JOBS=$(printf '%%s' "%{?_smp_mflags}" | sed 's/.*-j\([0-9][0-9]*\).*/\1/')
    LC_ALL=C TEST_JOBS=$JOBS make test_harness
%else
    LC_ALL=C make test
%endif
%endif

%ldconfig_scriptlets libs

%files
# We sub-package modules from perl-interpreter subpackage. Main perl package
# is a meta package.

%files interpreter
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_bindir}/*
%{archlib}/*
%{privlib}/*


# libs
%exclude %dir %{archlib}
%exclude %dir %{archlib}/auto
%exclude %{archlib}/auto/re
%exclude %dir %{archlib}/CORE
%exclude %{archlib}/CORE/libperl.so
%exclude %{archlib}/re.pm
%exclude %{_libdir}/libperl.so.*
%exclude %dir %{perl_vendorarch}
%exclude %dir %{perl_vendorarch}/auto
%exclude %dir %{privlib}
%exclude %{privlib}/integer.pm
%exclude %{privlib}/strict.pm
%exclude %{privlib}/unicore
%exclude %{privlib}/utf8.pm
%exclude %{privlib}/utf8_heavy.pl
%exclude %{privlib}/warnings.pm
%exclude %{privlib}/XSLoader.pm
%exclude %dir %{perl_vendorlib}
%exclude %{_mandir}/man3/integer.*
%exclude %{_mandir}/man3/re.*
%exclude %{_mandir}/man3/strict.*
%exclude %{_mandir}/man3/utf8.*
%exclude %{_mandir}/man3/warnings.*
%exclude %{_mandir}/man3/XSLoader.*

# devel
%exclude %{_bindir}/h2xs
%exclude %{_mandir}/man1/h2xs*
%exclude %{_bindir}/perlivp
%exclude %{_mandir}/man1/perlivp*
%exclude %{archlib}/CORE/*.h
%exclude %{_libdir}/libperl.so
%exclude %{_mandir}/man1/perlxs*
%if %{with perl_enables_systemtap}
%exclude %dir %{_datadir}/systemtap
%exclude %dir %{_datadir}/systemtap/tapset
%endif

# utils
%exclude %{_bindir}/h2ph
%exclude %{_bindir}/perlbug
%exclude %{_bindir}/perlthanks
%exclude %{_bindir}/pl2pm
%exclude %{_bindir}/splain
%exclude %{privlib}/pod/perlutil.pod
%exclude %{_mandir}/man1/h2ph.*
%exclude %{_mandir}/man1/perlbug.*
%exclude %{_mandir}/man1/perlthanks.*
%exclude %{_mandir}/man1/perlutil.*
%exclude %{_mandir}/man1/pl2pm.*
%exclude %{_mandir}/man1/splain.*

# Archive-Tar
%exclude %{_bindir}/ptar
%exclude %{_bindir}/ptardiff
%exclude %{_bindir}/ptargrep
%exclude %dir %{privlib}/Archive
%exclude %{privlib}/Archive/Tar
%exclude %{privlib}/Archive/Tar.pm
%exclude %{_mandir}/man1/ptar.1*
%exclude %{_mandir}/man1/ptardiff.1*
%exclude %{_mandir}/man1/ptargrep.1*
%exclude %{_mandir}/man3/Archive::Tar*

# Attribute-Handlers
%exclude %{privlib}/Attribute
%exclude %{_mandir}/man3/Attribute::Handlers.*

# autodie
%exclude %{privlib}/autodie/
%exclude %{privlib}/autodie.pm
%exclude %{privlib}/Fatal.pm
%exclude %{_mandir}/man3/autodie.3*
%exclude %{_mandir}/man3/autodie::*
%exclude %{_mandir}/man3/Fatal.3*

# bignum
%exclude %{privlib}/bigint.pm
%exclude %{privlib}/bignum.pm
%exclude %{privlib}/bigrat.pm
%exclude %{privlib}/Math/BigFloat
%exclude %{privlib}/Math/BigInt/Trace.pm
%exclude %{_mandir}/man3/bigint.*
%exclude %{_mandir}/man3/bignum.*
%exclude %{_mandir}/man3/bigrat.*

# Carp
%exclude %{privlib}/Carp
%exclude %{privlib}/Carp.*
%exclude %{_mandir}/man3/Carp.*

# Config-Perl-V
%exclude %{privlib}/Config/Perl
%exclude %{_mandir}/man3/Config::Perl::V.*

# constant
%exclude %{privlib}/constant.pm
%exclude %{_mandir}/man3/constant.3*

# CPAN
%exclude %{_bindir}/cpan
%exclude %dir %{privlib}/App
%exclude %{privlib}/App/Cpan.pm
%exclude %{privlib}/CPAN
%exclude %{privlib}/CPAN.pm
%exclude %{_mandir}/man1/cpan.1*
%exclude %{_mandir}/man3/App::Cpan.*
%exclude %{_mandir}/man3/CPAN.*
%exclude %{_mandir}/man3/CPAN:*

# CPAN-Meta
%exclude %dir %{privlib}/CPAN
%exclude %{privlib}/CPAN/Meta.pm
%exclude %dir %{privlib}/CPAN/Meta
%exclude %{privlib}/CPAN/Meta/Converter.pm
%exclude %{privlib}/CPAN/Meta/Feature.pm
%exclude %dir %{privlib}/CPAN/Meta/History
%exclude %{privlib}/CPAN/Meta/History.pm
%exclude %{privlib}/CPAN/Meta/Merge.pm
%exclude %{privlib}/CPAN/Meta/Prereqs.pm
%exclude %{privlib}/CPAN/Meta/Spec.pm
%exclude %{privlib}/CPAN/Meta/Validator.pm
%exclude %dir %{privlib}/Parse
%exclude %dir %{privlib}/Parse/CPAN
%exclude %{privlib}/Parse/CPAN/Meta.pm
%exclude %{_mandir}/man3/CPAN::Meta*
%exclude %{_mandir}/man3/Parse::CPAN::Meta.3*

# CPAN-Meta-Requirements
%exclude %dir %{privlib}/CPAN
%exclude %dir %{privlib}/CPAN/Meta
%exclude %{privlib}/CPAN/Meta/Requirements.pm
%exclude %{_mandir}/man3/CPAN::Meta::Requirements.3*

# CPAN-Meta-YAML
%exclude %dir %{privlib}/CPAN
%exclude %dir %{privlib}/CPAN/Meta
%exclude %{privlib}/CPAN/Meta/YAML.pm
%exclude %{_mandir}/man3/CPAN::Meta::YAML*

# Compress-Raw-Bzip2
%exclude %dir %{archlib}/Compress
%exclude %dir %{archlib}/Compress/Raw
%exclude %{archlib}/Compress/Raw/Bzip2.pm
%exclude %dir %{archlib}/auto/Compress
%exclude %dir %{archlib}/auto/Compress/Raw
%exclude %{archlib}/auto/Compress/Raw/Bzip2
%exclude %{_mandir}/man3/Compress::Raw::Bzip2*

# Compress-Raw-Zlib
%exclude %dir %{archlib}/Compress
%exclude %dir %{archlib}/Compress/Raw
%exclude %{archlib}/Compress/Raw/Zlib.pm
%exclude %dir %{archlib}/auto/Compress
%exclude %dir %{archlib}/auto/Compress/Raw
%exclude %{archlib}/auto/Compress/Raw/Zlib
%exclude %{_mandir}/man3/Compress::Raw::Zlib*

# Data-Dumper
%exclude %dir %{archlib}/auto/Data
%exclude %dir %{archlib}/auto/Data/Dumper
%exclude %{archlib}/auto/Data/Dumper/Dumper.so
%exclude %dir %{archlib}/Data
%exclude %{archlib}/Data/Dumper.pm
%exclude %{_mandir}/man3/Data::Dumper.3*

# DB_File
%exclude %{archlib}/DB_File.pm
%exclude %dir %{archlib}/auto/DB_File
%exclude %{archlib}/auto/DB_File/DB_File.so
%exclude %{_mandir}/man3/DB_File*

# Devel-Peek
%dir %exclude %{archlib}/Devel
%exclude %{archlib}/Devel/Peek.pm
%dir %exclude %{archlib}/auto/Devel
%exclude %{archlib}/auto/Devel/Peek
%exclude %{_mandir}/man3/Devel::Peek.*

# Devel-PPPort
%exclude %{archlib}/Devel/PPPort.pm
%exclude %{_mandir}/man3/Devel::PPPort.3*

# Devel-SelfStubber
%exclude %dir %{privlib}/Devel
%exclude %{privlib}/Devel/SelfStubber.pm
%exclude %{_mandir}/man3/Devel::SelfStubber.*

# Digest
%exclude %{privlib}/Digest.pm
%exclude %dir %{privlib}/Digest
%exclude %{privlib}/Digest/base.pm
%exclude %{privlib}/Digest/file.pm
%exclude %{_mandir}/man3/Digest.3*
%exclude %{_mandir}/man3/Digest::base.3*
%exclude %{_mandir}/man3/Digest::file.3*

# Digest-MD5
%exclude %dir %{archlib}/Digest
%exclude %{archlib}/Digest/MD5.pm
%exclude %dir %{archlib}/auto/Digest
%exclude %{archlib}/auto/Digest/MD5
%exclude %{_mandir}/man3/Digest::MD5.3*

# Digest-SHA
%exclude %{_bindir}/shasum
%exclude %dir %{archlib}/Digest
%exclude %{archlib}/Digest/SHA.pm
%exclude %dir %{archlib}/auto/Digest
%exclude %{archlib}/auto/Digest/SHA
%exclude %{_mandir}/man1/shasum.1*
%exclude %{_mandir}/man3/Digest::SHA.3*

# Encode
%exclude %{_bindir}/encguess
%exclude %{_bindir}/piconv
%exclude %{archlib}/Encode*
%exclude %{archlib}/auto/Encode*
%exclude %{privlib}/Encode
%exclude %{_mandir}/man1/encguess.1*
%exclude %{_mandir}/man1/piconv.1*
%exclude %{_mandir}/man3/Encode*.3*

# encoding
%exclude %{archlib}/encoding.pm
%exclude %{_mandir}/man3/encoding.3*

# Encode-devel
%exclude %{_bindir}/enc2xs
%exclude %dir %{privlib}/Encode
%exclude %{privlib}/Encode/*.e2x
%exclude %{privlib}/Encode/encode.h
%exclude %{_mandir}/man1/enc2xs.1*

# Env
%exclude %{privlib}/Env.pm
%exclude %{_mandir}/man3/Env.3*

# Errno
%exclude %{archlib}/Errno.pm
%exclude %{_mandir}/man3/Errno.*

# Exporter
%exclude %{privlib}/Exporter*
%exclude %{_mandir}/man3/Exporter*

# experimental
%exclude %{privlib}/experimental*
%exclude %{_mandir}/man3/experimental*

# ExtUtils-CBuilder
%exclude %{privlib}/ExtUtils/CBuilder
%exclude %{privlib}/ExtUtils/CBuilder.pm
%exclude %{_mandir}/man3/ExtUtils::CBuilder*

# ExtUtils-Command
%exclude %{privlib}/ExtUtils/Command.pm
%exclude %{_mandir}/man3/ExtUtils::Command.*

# ExtUtils-Embed
%exclude %{privlib}/ExtUtils/Embed.pm
%exclude %{_mandir}/man3/ExtUtils::Embed*

# ExtUtils-Install
%exclude %{privlib}/ExtUtils/Install.pm
%exclude %{privlib}/ExtUtils/Installed.pm
%exclude %{privlib}/ExtUtils/Packlist.pm
%exclude %{_mandir}/man3/ExtUtils::Install.3*
%exclude %{_mandir}/man3/ExtUtils::Installed.3*
%exclude %{_mandir}/man3/ExtUtils::Packlist.3*

# ExtUtils-Manifest
%exclude %{privlib}/ExtUtils/Manifest.pm
%exclude %{privlib}/ExtUtils/MANIFEST.SKIP
%exclude %{_mandir}/man3/ExtUtils::Manifest.3*

# ExtUtils-MakeMaker
%exclude %{_bindir}/instmodsh
%exclude %{privlib}/ExtUtils/Command
%exclude %{privlib}/ExtUtils/Liblist
%exclude %{privlib}/ExtUtils/Liblist.pm
%exclude %{privlib}/ExtUtils/MakeMaker
%exclude %{privlib}/ExtUtils/MakeMaker.pm
%exclude %{privlib}/ExtUtils/MM.pm
%exclude %{privlib}/ExtUtils/MM_*.pm
%exclude %{privlib}/ExtUtils/MY.pm
%exclude %{privlib}/ExtUtils/Mkbootstrap.pm
%exclude %{privlib}/ExtUtils/Mksymlists.pm
%exclude %{privlib}/ExtUtils/testlib.pm
%exclude %{_mandir}/man1/instmodsh.1*
%exclude %{_mandir}/man3/ExtUtils::Command::MM*
%exclude %{_mandir}/man3/ExtUtils::Liblist.3*
%exclude %{_mandir}/man3/ExtUtils::MM.3*
%exclude %{_mandir}/man3/ExtUtils::MM_*
%exclude %{_mandir}/man3/ExtUtils::MY.3*
%exclude %{_mandir}/man3/ExtUtils::MakeMaker*
%exclude %{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%exclude %{_mandir}/man3/ExtUtils::Mksymlists.3*
%exclude %{_mandir}/man3/ExtUtils::testlib.3*

# ExtUtils-Miniperl
%exclude %{privlib}/ExtUtils/Miniperl.pm
%exclude %{_mandir}/man3/ExtUtils::Miniperl.3*

# ExtUtils-MM-Utils
%exclude %dir %{privlib}/ExtUtils/MM
%exclude %{privlib}/ExtUtils/MM/Utils.pm
%exclude %{_mandir}/man3/ExtUtils::MM::Utils.*

# ExtUtils-ParseXS
%exclude %dir %{privlib}/ExtUtils/ParseXS
%exclude %{privlib}/ExtUtils/ParseXS.pm
%exclude %{privlib}/ExtUtils/ParseXS.pod
%exclude %{privlib}/ExtUtils/ParseXS/Constants.pm
%exclude %{privlib}/ExtUtils/ParseXS/CountLines.pm
%exclude %{privlib}/ExtUtils/ParseXS/Eval.pm
%exclude %{privlib}/ExtUtils/ParseXS/Utilities.pm
%exclude %dir %{privlib}/ExtUtils/Typemaps
%exclude %{privlib}/ExtUtils/Typemaps.pm
%exclude %{privlib}/ExtUtils/Typemaps/Cmd.pm
%exclude %{privlib}/ExtUtils/Typemaps/InputMap.pm
%exclude %{privlib}/ExtUtils/Typemaps/OutputMap.pm
%exclude %{privlib}/ExtUtils/Typemaps/Type.pm
%exclude %{privlib}/ExtUtils/xsubpp
%exclude %{_bindir}/xsubpp
%exclude %{_mandir}/man1/xsubpp*
%exclude %{_mandir}/man3/ExtUtils::ParseXS.3*
%exclude %{_mandir}/man3/ExtUtils::ParseXS::Constants.3*
%exclude %{_mandir}/man3/ExtUtils::ParseXS::Eval.3*
%exclude %{_mandir}/man3/ExtUtils::ParseXS::Utilities.3*
%exclude %{_mandir}/man3/ExtUtils::Typemaps.3*
%exclude %{_mandir}/man3/ExtUtils::Typemaps::Cmd.3*
%exclude %{_mandir}/man3/ExtUtils::Typemaps::InputMap.3*
%exclude %{_mandir}/man3/ExtUtils::Typemaps::OutputMap.3*
%exclude %{_mandir}/man3/ExtUtils::Typemaps::Type.3*

# File-Fetch
%exclude %{privlib}/File/Fetch.pm
%exclude %{_mandir}/man3/File::Fetch.3*

# File-Path
%exclude %{privlib}/File/Path.pm
%exclude %{_mandir}/man3/File::Path.3*

# File-Temp
%exclude %{privlib}/File/Temp.pm
%exclude %{_mandir}/man3/File::Temp.3*

# Filter
%exclude %dir %{archlib}/auto/Filter
%exclude %{archlib}/auto/Filter/Util
%exclude %dir %{archlib}/Filter
%exclude %{archlib}/Filter/Util
%exclude %{privlib}/pod/perlfilter.pod
%exclude %{_mandir}/man1/perlfilter.*
%exclude %{_mandir}/man3/Filter::Util::*

# Filter-Simple
%exclude %dir %{privlib}/Filter
%exclude %{privlib}/Filter/Simple.pm
%exclude %{_mandir}/man3/Filter::Simple.3*

# Getopt-Long
%exclude %{privlib}/Getopt/Long.pm
%exclude %{_mandir}/man3/Getopt::Long.3*

# IO
%exclude %dir %{archlib}/IO
%exclude %{archlib}/IO.pm
%exclude %{archlib}/IO/Dir.pm
%exclude %{archlib}/IO/File.pm
%exclude %{archlib}/IO/Handle.pm
%exclude %{archlib}/IO/Pipe.pm
%exclude %{archlib}/IO/Poll.pm
%exclude %{archlib}/IO/Seekable.pm
%exclude %{archlib}/IO/Select.pm
%exclude %dir %{archlib}/IO/Socket
%exclude %{archlib}/IO/Socket/INET.pm
%exclude %{archlib}/IO/Socket/UNIX.pm
%exclude %{archlib}/IO/Socket.pm
%exclude %dir %{archlib}/auto/IO
%exclude %{archlib}/auto/IO/IO.so
%exclude %{_mandir}/man3/IO.*
%exclude %{_mandir}/man3/IO::Dir.*
%exclude %{_mandir}/man3/IO::File.*
%exclude %{_mandir}/man3/IO::Handle.*
%exclude %{_mandir}/man3/IO::Pipe.*
%exclude %{_mandir}/man3/IO::Poll.*
%exclude %{_mandir}/man3/IO::Seekable.*
%exclude %{_mandir}/man3/IO::Select.*
%exclude %{_mandir}/man3/IO::Socket::INET.*
%exclude %{_mandir}/man3/IO::Socket::UNIX.*
%exclude %{_mandir}/man3/IO::Socket.*

# IO-Compress
%exclude %{_bindir}/zipdetails
%exclude %dir %{privlib}/IO
%exclude %dir %{privlib}/IO/Compress
%exclude %{privlib}/IO/Compress/FAQ.pod
%exclude %{_mandir}/man1/zipdetails.*
%exclude %{_mandir}/man3/IO::Compress::FAQ.*
# Compress-Zlib
%exclude %dir %{privlib}/Compress
%exclude %{privlib}/Compress/Zlib.pm
%exclude %{_mandir}/man3/Compress::Zlib*
# IO-Compress-Base
%exclude %{privlib}/File/GlobMapper.pm
%exclude %dir %{privlib}/IO
%exclude %dir %{privlib}/IO/Compress
%exclude %{privlib}/IO/Compress/Base
%exclude %{privlib}/IO/Compress/Base.pm
%exclude %dir %{privlib}/IO/Uncompress
%exclude %{privlib}/IO/Uncompress/AnyUncompress.pm
%exclude %{privlib}/IO/Uncompress/Base.pm
%exclude %{_mandir}/man3/File::GlobMapper.*
%exclude %{_mandir}/man3/IO::Compress::Base.*
%exclude %{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%exclude %{_mandir}/man3/IO::Uncompress::Base.*
# IO-Compress-Zlib
%exclude %dir %{privlib}/IO
%exclude %dir %{privlib}/IO/Compress
%exclude %{privlib}/IO/Compress/Adapter
%exclude %{privlib}/IO/Compress/Deflate.pm
%exclude %{privlib}/IO/Compress/Gzip
%exclude %{privlib}/IO/Compress/Gzip.pm
%exclude %{privlib}/IO/Compress/RawDeflate.pm
%exclude %{privlib}/IO/Compress/Bzip2.pm
%exclude %{privlib}/IO/Compress/Zip
%exclude %{privlib}/IO/Compress/Zip.pm
%exclude %{privlib}/IO/Compress/Zlib
%exclude %dir %{privlib}/IO/Uncompress
%exclude %{privlib}/IO/Uncompress/Adapter
%exclude %{privlib}/IO/Uncompress/AnyInflate.pm
%exclude %{privlib}/IO/Uncompress/Bunzip2.pm
%exclude %{privlib}/IO/Uncompress/Gunzip.pm
%exclude %{privlib}/IO/Uncompress/Inflate.pm
%exclude %{privlib}/IO/Uncompress/RawInflate.pm
%exclude %{privlib}/IO/Uncompress/Unzip.pm
%exclude %{_mandir}/man3/IO::Compress::Deflate*
%exclude %{_mandir}/man3/IO::Compress::Bzip2*
%exclude %{_mandir}/man3/IO::Compress::Gzip*
%exclude %{_mandir}/man3/IO::Compress::RawDeflate*
%exclude %{_mandir}/man3/IO::Compress::Zip*
%exclude %{_mandir}/man3/IO::Uncompress::AnyInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Bunzip2*
%exclude %{_mandir}/man3/IO::Uncompress::Gunzip*
%exclude %{_mandir}/man3/IO::Uncompress::Inflate*
%exclude %{_mandir}/man3/IO::Uncompress::RawInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Unzip*

# IO-Socket-IP
%exclude %dir %{privlib}/IO
%exclude %dir %{privlib}/IO/Socket
%exclude %{privlib}/IO/Socket/IP.pm
%exclude %{_mandir}/man3/IO::Socket::IP.*

# IO-Zlib
%exclude %dir %{privlib}/IO
%exclude %{privlib}/IO/Zlib.pm
%exclude %{_mandir}/man3/IO::Zlib.*

# HTTP-Tiny
%exclude %dir %{privlib}/HTTP
%exclude %{privlib}/HTTP/Tiny.pm
%exclude %{_mandir}/man3/HTTP::Tiny*

# IPC-Cmd
%exclude %{privlib}/IPC/Cmd.pm
%exclude %{_mandir}/man3/IPC::Cmd.3*

# IPC-SysV
%exclude %{archlib}/auto/IPC
%exclude %{archlib}/IPC/Msg.pm
%exclude %{archlib}/IPC/Semaphore.pm
%exclude %{archlib}/IPC/SharedMem.pm
%exclude %{archlib}/IPC/SysV.pm
%exclude %{_mandir}/man3/IPC::Msg.*
%exclude %{_mandir}/man3/IPC::Semaphore.*
%exclude %{_mandir}/man3/IPC::SharedMem.*
%exclude %{_mandir}/man3/IPC::SysV.*

# JSON-PP
%exclude %{_bindir}/json_pp
%exclude %dir %{privlib}/JSON
%exclude %{privlib}/JSON/PP
%exclude %{privlib}/JSON/PP.pm
%exclude %{_mandir}/man1/json_pp.1*
%exclude %{_mandir}/man3/JSON::PP.3*
%exclude %{_mandir}/man3/JSON::PP::Boolean.3pm*

# libnet
%exclude %{privlib}/Net/Cmd.pm
%exclude %{privlib}/Net/Config.pm
%exclude %{privlib}/Net/Domain.pm
%exclude %{privlib}/Net/FTP
%exclude %{privlib}/Net/FTP.pm
%exclude %{privlib}/Net/libnetFAQ.pod
%exclude %{privlib}/Net/NNTP.pm
%exclude %{privlib}/Net/Netrc.pm
%exclude %{privlib}/Net/POP3.pm
%exclude %{privlib}/Net/SMTP.pm
%exclude %{privlib}/Net/Time.pm
%exclude %{_mandir}/man3/Net::Cmd.*
%exclude %{_mandir}/man3/Net::Config.*
%exclude %{_mandir}/man3/Net::Domain.*
%exclude %{_mandir}/man3/Net::FTP.*
%exclude %{_mandir}/man3/Net::libnetFAQ.*
%exclude %{_mandir}/man3/Net::NNTP.*
%exclude %{_mandir}/man3/Net::Netrc.*
%exclude %{_mandir}/man3/Net::POP3.*
%exclude %{_mandir}/man3/Net::SMTP.*
%exclude %{_mandir}/man3/Net::Time.*

# libnetcfg
%exclude %{_bindir}/libnetcfg
%exclude %{_mandir}/man1/libnetcfg*

# Locale-Maketext
%exclude %dir %{privlib}/Locale
%exclude %dir %{privlib}/Locale/Maketext
%exclude %{privlib}/Locale/Maketext.*
%exclude %{privlib}/Locale/Maketext/Cookbook.*
%exclude %{privlib}/Locale/Maketext/Guts.*
%exclude %{privlib}/Locale/Maketext/GutsLoader.*
%exclude %{privlib}/Locale/Maketext/TPJ13.*
%exclude %{_mandir}/man3/Locale::Maketext.*
%exclude %{_mandir}/man3/Locale::Maketext::Cookbook.*
%exclude %{_mandir}/man3/Locale::Maketext::Guts.*
%exclude %{_mandir}/man3/Locale::Maketext::GutsLoader.*
%exclude %{_mandir}/man3/Locale::Maketext::TPJ13.*

# Locale-Maketext-Simple
%exclude %dir %{privlib}/Locale
%exclude %dir %{privlib}/Locale/Maketext
%exclude %{privlib}/Locale/Maketext/Simple.pm
%exclude %{_mandir}/man3/Locale::Maketext::Simple.*

# Math-BigInt
%exclude %{privlib}/Math/BigFloat.pm
%exclude %{privlib}/Math/BigInt.pm
%exclude %dir %exclude %{privlib}/Math/BigInt
%exclude %{privlib}/Math/BigInt/Calc.pm
%exclude %{privlib}/Math/BigInt/Lib.pm
%exclude %{_mandir}/man3/Math::BigFloat.*
%exclude %{_mandir}/man3/Math::BigInt.*
%exclude %{_mandir}/man3/Math::BigInt::Calc.*
%exclude %{_mandir}/man3/Math::BigInt::Lib.*

# Math-BigInt-FastCalc
%exclude %{archlib}/Math
%exclude %{archlib}/auto/Math
%exclude %{_mandir}/man3/Math::BigInt::FastCalc.*

# Math-BigRat
%exclude %{privlib}/Math/BigRat.pm
%exclude %{_mandir}/man3/Math::BigRat.*

# Math-Complex
%dir %exclude %{privlib}/Math
%exclude %{privlib}/Math/Complex.pm
%exclude %{privlib}/Math/Trig.pm
%exclude %{_mandir}/man3/Math::Complex.*
%exclude %{_mandir}/man3/Math::Trig.*

# Memoize
%exclude %{privlib}/Memoize
%exclude %{privlib}/Memoize.pm
%exclude %{_mandir}/man3/Memoize::*
%exclude %{_mandir}/man3/Memoize.*

# MIME-Base64
%exclude %{archlib}/auto/MIME
%exclude %{archlib}/MIME
%exclude %{_mandir}/man3/MIME::*

# Module-CoreList
%exclude %dir %{privlib}/Module
%exclude %{privlib}/Module/CoreList
%exclude %{privlib}/Module/CoreList.pm
%exclude %{privlib}/Module/CoreList.pod
%exclude %{_mandir}/man3/Module::CoreList*

# Module-CoreList-tools
%exclude %{_bindir}/corelist
%exclude %{_mandir}/man1/corelist*

# Module-Load
%exclude %dir %{privlib}/Module
%exclude %{privlib}/Module/Load.pm
%exclude %{_mandir}/man3/Module::Load.*

# Module-Load-Conditional
%exclude %dir %{privlib}/Module
%exclude %{privlib}/Module/Load
%exclude %{_mandir}/man3/Module::Load::Conditional*

# Module-Loaded
%exclude %dir %{privlib}/Module
%exclude %{privlib}/Module/Loaded.pm
%exclude %{_mandir}/man3/Module::Loaded*

# Module-Metadata
%exclude %dir %{privlib}/Module
%exclude %{privlib}/Module/Metadata.pm
%exclude %{_mandir}/man3/Module::Metadata.3pm*

# Net-Ping
%exclude %{privlib}/Net/Ping.pm
%exclude %{_mandir}/man3/Net::Ping.*

# PathTools
%exclude %{archlib}/Cwd.pm
%exclude %{archlib}/File/Spec*
%exclude %{archlib}/auto/Cwd/
%exclude %{_mandir}/man3/Cwd*
%exclude %{_mandir}/man3/File::Spec*

# Params-Check
%exclude %{privlib}/Params/
%exclude %{_mandir}/man3/Params::Check*

# perlfaq
%exclude %{privlib}/perlfaq.pm
%exclude %{privlib}/pod/perlfaq*
%exclude %{privlib}/pod/perlglossary.pod
%exclude %{_mandir}/man1/perlfaq*
%exclude %{_mandir}/man1/perlglossary.*

# PerlIO-via-QuotedPrint
%exclude %{privlib}/PerlIO
%exclude %{_mandir}/man3/PerlIO::via::QuotedPrint.*

# Perl-OSType
%exclude %dir %{privlib}/Perl
%exclude %{privlib}/Perl/OSType.pm
%exclude %{_mandir}/man3/Perl::OSType.3pm*

# open
%exclude %{privlib}/open.pm
%exclude %{_mandir}/man3/open.3*

# parent
%exclude %{privlib}/parent.pm
%exclude %{_mandir}/man3/parent.3*

# Pod-Checker
%exclude %{_bindir}/podchecker
%exclude %{privlib}/Pod/Checker.pm
%exclude %{_mandir}/man1/podchecker.*
%exclude %{_mandir}/man3/Pod::Checker.*

# Pod-Escapes
%exclude %{privlib}/Pod/Escapes.pm
%exclude %{_mandir}/man3/Pod::Escapes.*

# Pod-Html
%exclude %{_bindir}/pod2html
%exclude %{privlib}/Pod/Html.pm
%exclude %{_mandir}/man1/pod2html.1*
%exclude %{_mandir}/man3/Pod::Html.*

# Pod-Parser
%exclude %{_bindir}/podselect
%exclude %{privlib}/Pod/Find.pm
%exclude %{privlib}/Pod/InputObjects.pm
%exclude %{privlib}/Pod/ParseUtils.pm
%exclude %{privlib}/Pod/Parser.pm
%exclude %{privlib}/Pod/PlainText.pm
%exclude %{privlib}/Pod/Select.pm
%exclude %{_mandir}/man1/podselect.1*
%exclude %{_mandir}/man3/Pod::Find.*
%exclude %{_mandir}/man3/Pod::InputObjects.*
%exclude %{_mandir}/man3/Pod::ParseUtils.*
%exclude %{_mandir}/man3/Pod::Parser.*
%exclude %{_mandir}/man3/Pod::PlainText.*
%exclude %{_mandir}/man3/Pod::Select.*

# Pod-Perldoc
%exclude %{_bindir}/perldoc
%exclude %{privlib}/pod/perldoc.pod
%exclude %{privlib}/Pod/Perldoc.pm
%exclude %{privlib}/Pod/Perldoc/
%exclude %{_mandir}/man1/perldoc.1*
%exclude %{_mandir}/man3/Pod::Perldoc*

# Pod-Usage
%exclude %{_bindir}/pod2usage
%exclude %{privlib}/Pod/Usage.pm
%exclude %{_mandir}/man1/pod2usage.*
%exclude %{_mandir}/man3/Pod::Usage.*

# podlators
%exclude %{_bindir}/pod2man
%exclude %{_bindir}/pod2text
%exclude %{privlib}/pod/perlpodstyle.pod
%exclude %{privlib}/Pod/Man.pm
%exclude %{privlib}/Pod/ParseLink.pm
%exclude %{privlib}/Pod/Text
%exclude %{privlib}/Pod/Text.pm
%exclude %{_mandir}/man1/pod2man.1*
%exclude %{_mandir}/man1/pod2text.1*
%exclude %{_mandir}/man1/perlpodstyle.1*
%exclude %{_mandir}/man3/Pod::Man*
%exclude %{_mandir}/man3/Pod::ParseLink*
%exclude %{_mandir}/man3/Pod::Text*

# Pod-Simple
%exclude %{privlib}/Pod/Simple/
%exclude %{privlib}/Pod/Simple.pm
%exclude %{privlib}/Pod/Simple.pod
%exclude %{_mandir}/man3/Pod::Simple*

# Scalar-List-Utils
%exclude %{archlib}/List/
%exclude %{archlib}/Scalar/
%exclude %{archlib}/Sub/
%exclude %{archlib}/auto/List/
%exclude %{_mandir}/man3/List::Util*
%exclude %{_mandir}/man3/Scalar::Util*
%exclude %{_mandir}/man3/Sub::Util*

# SelfLoader
%exclude %{privlib}/SelfLoader.pm
%exclude %{_mandir}/man3/SelfLoader*

# Storable
%exclude %{archlib}/Storable.pm
%exclude %{archlib}/auto/Storable/
%exclude %{_mandir}/man3/Storable.*

# Sys-Syslog
%exclude %{archlib}/Sys/Syslog.pm
%exclude %{archlib}/auto/Sys/Syslog/
%exclude %{_mandir}/man3/Sys::Syslog.*

# Term-ANSIColor
%exclude %{privlib}/Term/ANSIColor.pm
%exclude %{_mandir}/man3/Term::ANSIColor*

# Term-Cap
%exclude %{privlib}/Term/Cap.pm
%exclude %{_mandir}/man3/Term::Cap.*

# Test
%exclude %{privlib}/Test.pm
%exclude %{_mandir}/man3/Test.*

# Test-Harness
%exclude %{_bindir}/prove
%exclude %dir %{privlib}/App
%exclude %{privlib}/App/Prove*
%exclude %{privlib}/TAP*
%exclude %dir %{privlib}/Test
%exclude %{privlib}/Test/Harness*
%exclude %{_mandir}/man1/prove.1*
%exclude %{_mandir}/man3/App::Prove*
%exclude %{_mandir}/man3/TAP*
%exclude %{_mandir}/man3/Test::Harness*

# Test-Simple
%exclude %{privlib}/ok*
%exclude %dir %{privlib}/Test
%exclude %{privlib}/Test/More*
%exclude %{privlib}/Test/Builder*
%exclude %{privlib}/Test/Tester*
%exclude %{privlib}/Test/Simple*
%exclude %{privlib}/Test/Tutorial*
%exclude %{privlib}/Test/use
%exclude %{privlib}/Test2*
%exclude %{_mandir}/man3/ok*
%exclude %{_mandir}/man3/Test::More*
%exclude %{_mandir}/man3/Test::Builder*
%exclude %{_mandir}/man3/Test::Tester*
%exclude %{_mandir}/man3/Test::Simple*
%exclude %{_mandir}/man3/Test::Tutorial*
%exclude %{_mandir}/man3/Test::use::*
%exclude %{_mandir}/man3/Test2*

# Text-Balanced
%exclude %{privlib}/Text/Balanced.pm
%exclude %{_mandir}/man3/Text::Balanced.*

# Text-ParseWords
%exclude %{privlib}/Text/ParseWords.pm
%exclude %{_mandir}/man3/Text::ParseWords.*

# Text-Tabs+Wrap
%exclude %{privlib}/Text/Tabs.pm
%exclude %{privlib}/Text/Wrap.pm
%exclude %{_mandir}/man3/Text::Tabs.*
%exclude %{_mandir}/man3/Text::Wrap.*

# Thread-Queue
%exclude %{privlib}/Thread/Queue.pm
%exclude %{_mandir}/man3/Thread::Queue.*

# Time-HiRes
%exclude %dir %{archlib}/Time
%exclude %{archlib}/Time/HiRes.pm
%exclude %dir %{archlib}/auto/Time
%exclude %{archlib}/auto/Time/HiRes
%exclude %{_mandir}/man3/Time::HiRes.*

# Time-Local
%exclude %{privlib}/Time/Local.pm
%exclude %{_mandir}/man3/Time::Local.*

# Time-Piece
%exclude %dir %{archlib}/Time
%exclude %{archlib}/Time/Piece.pm
%exclude %{archlib}/Time/Seconds.pm
%exclude %dir %{archlib}/auto/Time
%exclude %{archlib}/auto/Time/Piece
%exclude %{_mandir}/man3/Time::Piece.3*
%exclude %{_mandir}/man3/Time::Seconds.3*

# Socket
%exclude %dir %{archlib}/auto/Socket
%exclude %{archlib}/auto/Socket/Socket.*
%exclude %{archlib}/Socket.pm
%exclude %{_mandir}/man3/Socket.3*

# threads
%dir %exclude %{archlib}/auto/threads
%exclude %{archlib}/auto/threads/threads*
%exclude %{archlib}/threads.pm
%exclude %{_mandir}/man3/threads.3*

# threads-shared
%exclude %{archlib}/auto/threads/shared*
%exclude %dir %{archlib}/threads
%exclude %{archlib}/threads/shared*
%exclude %{_mandir}/man3/threads::shared*

# Unicode-Collate
%dir %exclude %{archlib}/auto/Unicode
%exclude %{archlib}/auto/Unicode/Collate
%dir %exclude %{archlib}/Unicode
%exclude %{archlib}/Unicode/Collate
%exclude %{archlib}/Unicode/Collate.pm
%exclude %{privlib}/Unicode/Collate
%exclude %{_mandir}/man3/Unicode::Collate.*
%exclude %{_mandir}/man3/Unicode::Collate::*

# Unicode-Normalize
%exclude %{archlib}/auto/Unicode/Normalize
%exclude %{archlib}/Unicode/Normalize.pm
%exclude %{_mandir}/man3/Unicode::Normalize.*

# version
%exclude %{privlib}/version.pm
%exclude %{privlib}/version.pod
%exclude %{privlib}/version/
%exclude %{_mandir}/man3/version.3*
%exclude %{_mandir}/man3/version::Internals.3*

%files libs
%license Artistic Copying
%doc AUTHORS README Changes
%dir %{archlib}
%dir %{archlib}/auto
%{archlib}/auto/re
%dir %{archlib}/CORE
%{archlib}/CORE/libperl.so
%{archlib}/re.pm
%{_libdir}/libperl.so.*
%dir %{perl_vendorarch}
%dir %{perl_vendorarch}/auto
%dir %{privlib}
%{privlib}/integer.pm
%{privlib}/strict.pm
%{privlib}/unicore
%{privlib}/utf8.pm
%{privlib}/utf8_heavy.pl
%{privlib}/warnings.pm
%{privlib}/XSLoader.pm
%dir %{perl_vendorlib}
%{_mandir}/man3/integer.*
%{_mandir}/man3/re.*
%{_mandir}/man3/strict.*
%{_mandir}/man3/utf8.*
%{_mandir}/man3/warnings.*
%{_mandir}/man3/XSLoader.*

%files devel
%{_bindir}/h2xs
%{_mandir}/man1/h2xs*
%{_bindir}/perlivp
%{_mandir}/man1/perlivp*
%{archlib}/CORE/*.h
%{_libdir}/libperl.so
%{_mandir}/man1/perlxs*
%if %{with perl_enables_systemtap}
%dir %{_datadir}/systemtap
%dir %{_datadir}/systemtap/tapset
%{tapsetdir}/%{libperl_stp}
%doc perl-example.stp
%endif

%files macros
%{_rpmmacrodir}/macros.perl

%files tests
%{perl5_testdir}/

%files utils
%{_bindir}/h2ph
%{_bindir}/perlbug
%{_bindir}/perlthanks
%{_bindir}/pl2pm
%{_bindir}/splain
%dir %{privlib}/pod
%{privlib}/pod/perlutil.pod
%{_mandir}/man1/h2ph.*
%{_mandir}/man1/perlbug.*
%{_mandir}/man1/perlthanks.*
%{_mandir}/man1/perlutil.*
%{_mandir}/man1/pl2pm.*
%{_mandir}/man1/splain.*

%if %{dual_life} || %{rebuild_from_scratch}
%files Archive-Tar
%{_bindir}/ptar
%{_bindir}/ptardiff
%{_bindir}/ptargrep
%dir %{privlib}/Archive
%{privlib}/Archive/Tar 
%{privlib}/Archive/Tar.pm
%{_mandir}/man1/ptar.1*
%{_mandir}/man1/ptardiff.1*
%{_mandir}/man1/ptargrep.1*
%{_mandir}/man3/Archive::Tar* 
%endif

%files Attribute-Handlers
%{privlib}/Attribute
%{_mandir}/man3/Attribute::Handlers.*

%if %{dual_life} || %{rebuild_from_scratch}
%files autodie
%{privlib}/autodie/
%{privlib}/autodie.pm
%{privlib}/Fatal.pm
%{_mandir}/man3/autodie.3*
%{_mandir}/man3/autodie::*
%{_mandir}/man3/Fatal.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files bignum
%{privlib}/bigint.pm
%{privlib}/bignum.pm
%{privlib}/bigrat.pm
%dir %{privlib}/Math
%{privlib}/Math/BigFloat
%dir %{privlib}/Math/BigInt
%{privlib}/Math/BigInt/Trace.pm
%{_mandir}/man3/bigint.*
%{_mandir}/man3/bignum.*
%{_mandir}/man3/bigrat.*

%files Carp
%{privlib}/Carp
%{privlib}/Carp.*
%{_mandir}/man3/Carp.*

%files Compress-Raw-Bzip2
%dir %{archlib}/Compress
%dir %{archlib}/Compress/Raw
%{archlib}/Compress/Raw/Bzip2.pm
%dir %{archlib}/auto/Compress
%dir %{archlib}/auto/Compress/Raw
%{archlib}/auto/Compress/Raw/Bzip2
%{_mandir}/man3/Compress::Raw::Bzip2*

%files Compress-Raw-Zlib
%dir %{archlib}/Compress
%dir %{archlib}/Compress/Raw
%{archlib}/Compress/Raw/Zlib.pm
%dir %{archlib}/auto/Compress
%dir %{archlib}/auto/Compress/Raw
%{archlib}/auto/Compress/Raw/Zlib
%{_mandir}/man3/Compress::Raw::Zlib*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Config-Perl-V
%dir %{privlib}/Config
%{privlib}/Config/Perl
%{_mandir}/man3/Config::Perl::V.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files constant
%{privlib}/constant.pm
%{_mandir}/man3/constant.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files CPAN
%{_bindir}/cpan
%dir %{privlib}/App
%{privlib}/App/Cpan.pm
%{privlib}/CPAN
%{privlib}/CPAN.pm
%{_mandir}/man1/cpan.1*
%{_mandir}/man3/App::Cpan.*
%{_mandir}/man3/CPAN.*
%{_mandir}/man3/CPAN:*
%exclude %{privlib}/CPAN/Meta/
%exclude %{privlib}/CPAN/Meta.pm
%exclude %{_mandir}/man3/CPAN::Meta*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files CPAN-Meta
%dir %{privlib}/CPAN/Meta
%{privlib}/CPAN/Meta.pm
%{privlib}/CPAN/Meta/Converter.pm
%{privlib}/CPAN/Meta/Feature.pm
%dir %{privlib}/CPAN/Meta/History
%{privlib}/CPAN/Meta/History/Meta*
%{privlib}/CPAN/Meta/History.pm
%{privlib}/CPAN/Meta/Merge.pm
%{privlib}/CPAN/Meta/Prereqs.pm
%{privlib}/CPAN/Meta/Spec.pm
%{privlib}/CPAN/Meta/Validator.pm
%dir %{privlib}/Parse/
%dir %{privlib}/Parse/CPAN/
%{privlib}/Parse/CPAN/Meta.pm
%{_mandir}/man3/CPAN::Meta*
%{_mandir}/man3/Parse::CPAN::Meta.3*
%exclude %{_mandir}/man3/CPAN::Meta::YAML*
%exclude %{_mandir}/man3/CPAN::Meta::Requirements*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files CPAN-Meta-Requirements
%dir %{privlib}/CPAN
%dir %{privlib}/CPAN/Meta
%{privlib}/CPAN/Meta/Requirements.pm
%{_mandir}/man3/CPAN::Meta::Requirements.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files CPAN-Meta-YAML
%dir %{privlib}/CPAN
%dir %{privlib}/CPAN/Meta
%{privlib}/CPAN/Meta/YAML.pm
%{_mandir}/man3/CPAN::Meta::YAML*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Data-Dumper
%dir %{archlib}/auto/Data
%dir %{archlib}/auto/Data/Dumper
%{archlib}/auto/Data/Dumper/Dumper.so
%dir %{archlib}/Data
%{archlib}/Data/Dumper.pm
%{_mandir}/man3/Data::Dumper.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files DB_File
%{archlib}/DB_File.pm
%dir %{archlib}/auto/DB_File
%{archlib}/auto/DB_File/DB_File.so
%{_mandir}/man3/DB_File*
%endif

%files Devel-Peek
%dir %{archlib}/Devel
%{archlib}/Devel/Peek.pm
%dir %{archlib}/auto/Devel
%{archlib}/auto/Devel/Peek
%{_mandir}/man3/Devel::Peek.*

%if %{dual_life} || %{rebuild_from_scratch}
%files Devel-PPPort
%dir %{archlib}/Devel
%{archlib}/Devel/PPPort.pm
%{_mandir}/man3/Devel::PPPort.3*
%endif

%files Devel-SelfStubber
%dir %{privlib}/Devel
%{privlib}/Devel/SelfStubber.pm
%{_mandir}/man3/Devel::SelfStubber.*

%if %{dual_life} || %{rebuild_from_scratch}
%files Digest
%{privlib}/Digest.pm
%dir %{privlib}/Digest
%{privlib}/Digest/base.pm
%{privlib}/Digest/file.pm
%{_mandir}/man3/Digest.3*
%{_mandir}/man3/Digest::base.3*
%{_mandir}/man3/Digest::file.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Digest-MD5
%dir %{archlib}/Digest
%{archlib}/Digest/MD5.pm
%dir %{archlib}/auto/Digest
%{archlib}/auto/Digest/MD5
%{_mandir}/man3/Digest::MD5.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Digest-SHA
%{_bindir}/shasum
%dir %{archlib}/Digest
%{archlib}/Digest/SHA.pm
%dir %{archlib}/auto/Digest
%{archlib}/auto/Digest/SHA
%{_mandir}/man1/shasum.1*
%{_mandir}/man3/Digest::SHA.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Encode
%{_bindir}/encguess
%{_bindir}/piconv
%{archlib}/Encode*
%{archlib}/auto/Encode*
%{privlib}/Encode
%exclude %{privlib}/Encode/*.e2x
%exclude %{privlib}/Encode/encode.h
%{_mandir}/man1/encguess.1*
%{_mandir}/man1/piconv.1*
%{_mandir}/man3/Encode*.3*

%files encoding
%{archlib}/encoding.pm
%{_mandir}/man3/encoding.3*

%files Encode-devel
%{_bindir}/enc2xs
%dir %{privlib}/Encode
%{privlib}/Encode/*.e2x
%{privlib}/Encode/encode.h
%{_mandir}/man1/enc2xs.1*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Env
%{privlib}/Env.pm
%{_mandir}/man3/Env.3*
%endif

%files Errno
%{archlib}/Errno.pm
%{_mandir}/man3/Errno.*

%if %{dual_life} || %{rebuild_from_scratch}
%files Exporter
%{privlib}/Exporter*
%{_mandir}/man3/Exporter*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files experimental
%{privlib}/experimental*
%{_mandir}/man3/experimental*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files ExtUtils-CBuilder
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/CBuilder
%{privlib}/ExtUtils/CBuilder.pm
%{_mandir}/man3/ExtUtils::CBuilder*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files ExtUtils-Command
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/Command.pm
%{_mandir}/man3/ExtUtils::Command.*
%endif

%files ExtUtils-Embed
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/Embed.pm
%{_mandir}/man3/ExtUtils::Embed*

%if %{dual_life} || %{rebuild_from_scratch}
%files ExtUtils-Install
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/Install.pm
%{privlib}/ExtUtils/Installed.pm
%{privlib}/ExtUtils/Packlist.pm
%{_mandir}/man3/ExtUtils::Install.3*
%{_mandir}/man3/ExtUtils::Installed.3*
%{_mandir}/man3/ExtUtils::Packlist.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files ExtUtils-Manifest
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/Manifest.pm
%{privlib}/ExtUtils/MANIFEST.SKIP
%{_mandir}/man3/ExtUtils::Manifest.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files ExtUtils-MakeMaker
%{_bindir}/instmodsh
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/Command/
%{privlib}/ExtUtils/Liblist
%{privlib}/ExtUtils/Liblist.pm
%{privlib}/ExtUtils/MakeMaker
%{privlib}/ExtUtils/MakeMaker.pm
%{privlib}/ExtUtils/MM.pm
%{privlib}/ExtUtils/MM_*.pm
%{privlib}/ExtUtils/MY.pm
%{privlib}/ExtUtils/Mkbootstrap.pm
%{privlib}/ExtUtils/Mksymlists.pm
%{privlib}/ExtUtils/testlib.pm
%{_mandir}/man1/instmodsh.1*
%{_mandir}/man3/ExtUtils::Command::MM*
%{_mandir}/man3/ExtUtils::Liblist.3*
%{_mandir}/man3/ExtUtils::MM.3*
%{_mandir}/man3/ExtUtils::MM_*
%{_mandir}/man3/ExtUtils::MY.3*
%{_mandir}/man3/ExtUtils::MakeMaker*
%{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%{_mandir}/man3/ExtUtils::Mksymlists.3*
%{_mandir}/man3/ExtUtils::testlib.3*
%endif

%files ExtUtils-Miniperl
%dir %{privlib}/ExtUtils
%{privlib}/ExtUtils/Miniperl.pm
%{_mandir}/man3/ExtUtils::Miniperl.3*

%if %{dual_life} || %{rebuild_from_scratch}
%files ExtUtils-MM-Utils
%dir %{privlib}/ExtUtils
%dir %{privlib}/ExtUtils/MM
%{privlib}/ExtUtils/MM/Utils.pm
%{_mandir}/man3/ExtUtils::MM::Utils.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files ExtUtils-ParseXS
%dir %{privlib}/ExtUtils
%dir %{privlib}/ExtUtils/ParseXS
%{privlib}/ExtUtils/ParseXS.pm
%{privlib}/ExtUtils/ParseXS.pod
%{privlib}/ExtUtils/ParseXS/Constants.pm
%{privlib}/ExtUtils/ParseXS/CountLines.pm
%{privlib}/ExtUtils/ParseXS/Eval.pm
%{privlib}/ExtUtils/ParseXS/Utilities.pm
%dir %{privlib}/ExtUtils/Typemaps
%{privlib}/ExtUtils/Typemaps.pm
%{privlib}/ExtUtils/Typemaps/Cmd.pm
%{privlib}/ExtUtils/Typemaps/InputMap.pm
%{privlib}/ExtUtils/Typemaps/OutputMap.pm
%{privlib}/ExtUtils/Typemaps/Type.pm
%{privlib}/ExtUtils/xsubpp
%{_bindir}/xsubpp
%{_mandir}/man1/xsubpp*
%{_mandir}/man3/ExtUtils::ParseXS.3*
%{_mandir}/man3/ExtUtils::ParseXS::Constants.3*
%{_mandir}/man3/ExtUtils::ParseXS::Eval.3*
%{_mandir}/man3/ExtUtils::ParseXS::Utilities.3*
%{_mandir}/man3/ExtUtils::Typemaps.3*
%{_mandir}/man3/ExtUtils::Typemaps::Cmd.3*
%{_mandir}/man3/ExtUtils::Typemaps::InputMap.3*
%{_mandir}/man3/ExtUtils::Typemaps::OutputMap.3*
%{_mandir}/man3/ExtUtils::Typemaps::Type.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files File-Fetch
%dir %{privlib}/File
%{privlib}/File/Fetch.pm
%{_mandir}/man3/File::Fetch.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files File-Path
%dir %{privlib}/File
%{privlib}/File/Path.pm
%{_mandir}/man3/File::Path.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files File-Temp
%dir %{privlib}/File
%{privlib}/File/Temp.pm
%{_mandir}/man3/File::Temp.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Filter
%dir %{archlib}/auto/Filter
%{archlib}/auto/Filter/Util
%dir %{archlib}/Filter
%{archlib}/Filter/Util
%{privlib}/pod/perlfilter.pod
%{_mandir}/man1/perlfilter.*
%{_mandir}/man3/Filter::Util::*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Filter-Simple
%dir %{privlib}/Filter
%{privlib}/Filter/Simple.pm
%{_mandir}/man3/Filter::Simple.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Getopt-Long
%dir %{privlib}/Getopt
%{privlib}/Getopt/Long.pm
%{_mandir}/man3/Getopt::Long.3*
%endif

%files IO
%dir %{archlib}/IO
%{archlib}/IO.pm
%{archlib}/IO/Dir.pm
%{archlib}/IO/File.pm
%{archlib}/IO/Handle.pm
%{archlib}/IO/Pipe.pm
%{archlib}/IO/Poll.pm
%{archlib}/IO/Seekable.pm
%{archlib}/IO/Select.pm
%dir %{archlib}/IO/Socket
%{archlib}/IO/Socket/INET.pm
%{archlib}/IO/Socket/UNIX.pm
%{archlib}/IO/Socket.pm
%dir %{archlib}/auto/IO
%{archlib}/auto/IO/IO.so
%{_mandir}/man3/IO.*
%{_mandir}/man3/IO::Dir.*
%{_mandir}/man3/IO::File.*
%{_mandir}/man3/IO::Handle.*
%{_mandir}/man3/IO::Pipe.*
%{_mandir}/man3/IO::Poll.*
%{_mandir}/man3/IO::Seekable.*
%{_mandir}/man3/IO::Select.*
%{_mandir}/man3/IO::Socket::INET.*
%{_mandir}/man3/IO::Socket::UNIX.*
%{_mandir}/man3/IO::Socket.*

%if %{dual_life} || %{rebuild_from_scratch}
%files IO-Compress
# IO-Compress
%{_bindir}/zipdetails
%dir %{privlib}/IO
%dir %{privlib}/IO/Compress
%{privlib}/IO/Compress/FAQ.pod
%{_mandir}/man1/zipdetails.*
%{_mandir}/man3/IO::Compress::FAQ.*
# Compress-Zlib
%dir %{privlib}/Compress
%{privlib}/Compress/Zlib.pm
%{_mandir}/man3/Compress::Zlib*
#IO-Compress-Base
%dir %{privlib}/File
%{privlib}/File/GlobMapper.pm
%dir %{privlib}/IO
%dir %{privlib}/IO/Compress
%{privlib}/IO/Compress/Base
%{privlib}/IO/Compress/Base.pm
%dir %{privlib}/IO/Uncompress
%{privlib}/IO/Uncompress/AnyUncompress.pm
%{privlib}/IO/Uncompress/Base.pm
%{_mandir}/man3/File::GlobMapper.*
%{_mandir}/man3/IO::Compress::Base.*
%{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%{_mandir}/man3/IO::Uncompress::Base.*
# IO-Compress-Zlib
%dir %{privlib}/IO
%dir %{privlib}/IO/Compress
%{privlib}/IO/Compress/Adapter
%{privlib}/IO/Compress/Deflate.pm
%{privlib}/IO/Compress/Bzip2.pm
%{privlib}/IO/Compress/Gzip
%{privlib}/IO/Compress/Gzip.pm
%{privlib}/IO/Compress/RawDeflate.pm
%{privlib}/IO/Compress/Zip
%{privlib}/IO/Compress/Zip.pm
%{privlib}/IO/Compress/Zlib
%dir %{privlib}/IO/Uncompress
%{privlib}/IO/Uncompress/Adapter/
%{privlib}/IO/Uncompress/AnyInflate.pm
%{privlib}/IO/Uncompress/Bunzip2.pm
%{privlib}/IO/Uncompress/Gunzip.pm
%{privlib}/IO/Uncompress/Inflate.pm
%{privlib}/IO/Uncompress/RawInflate.pm
%{privlib}/IO/Uncompress/Unzip.pm
%{_mandir}/man3/IO::Compress::Deflate*
%{_mandir}/man3/IO::Compress::Gzip*
%{_mandir}/man3/IO::Compress::Bzip2*
%{_mandir}/man3/IO::Compress::RawDeflate*
%{_mandir}/man3/IO::Compress::Zip*
%{_mandir}/man3/IO::Uncompress::AnyInflate*
%{_mandir}/man3/IO::Uncompress::Bunzip2*
%{_mandir}/man3/IO::Uncompress::Gunzip*
%{_mandir}/man3/IO::Uncompress::Inflate*
%{_mandir}/man3/IO::Uncompress::RawInflate*
%{_mandir}/man3/IO::Uncompress::Unzip*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files IO-Socket-IP
%dir %{privlib}/IO
%dir %{privlib}/IO/Socket
%{privlib}/IO/Socket/IP.pm
%{_mandir}/man3/IO::Socket::IP.*
%endif

%files IO-Zlib
%dir %{privlib}/IO
%{privlib}/IO/Zlib.pm
%{_mandir}/man3/IO::Zlib.*

%if %{dual_life} || %{rebuild_from_scratch}
%files HTTP-Tiny
%dir %{privlib}/HTTP
%{privlib}/HTTP/Tiny.pm
%{_mandir}/man3/HTTP::Tiny*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files IPC-Cmd
%dir %{privlib}/IPC
%{privlib}/IPC/Cmd.pm
%{_mandir}/man3/IPC::Cmd.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files IPC-SysV
%{archlib}/auto/IPC
%dir %{archlib}/IPC
%{archlib}/IPC/Msg.pm
%{archlib}/IPC/Semaphore.pm
%{archlib}/IPC/SharedMem.pm
%{archlib}/IPC/SysV.pm
%{_mandir}/man3/IPC::Msg.*
%{_mandir}/man3/IPC::Semaphore.*
%{_mandir}/man3/IPC::SharedMem.*
%{_mandir}/man3/IPC::SysV.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files JSON-PP
%{_bindir}/json_pp
%dir %{privlib}/JSON
%{privlib}/JSON/PP
%{privlib}/JSON/PP.pm
%{_mandir}/man1/json_pp.1*
%{_mandir}/man3/JSON::PP.3*
%{_mandir}/man3/JSON::PP::Boolean.3pm*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files libnet
%dir %{privlib}/Net
%{privlib}/Net/Cmd.pm
%{privlib}/Net/Config.pm
%{privlib}/Net/Domain.pm
%{privlib}/Net/FTP
%{privlib}/Net/FTP.pm
%{privlib}/Net/libnetFAQ.pod
%{privlib}/Net/NNTP.pm
%{privlib}/Net/Netrc.pm
%{privlib}/Net/POP3.pm
%{privlib}/Net/SMTP.pm
%{privlib}/Net/Time.pm
%{_mandir}/man3/Net::Cmd.*
%{_mandir}/man3/Net::Config.*
%{_mandir}/man3/Net::Domain.*
%{_mandir}/man3/Net::FTP.*
%{_mandir}/man3/Net::libnetFAQ.*
%{_mandir}/man3/Net::NNTP.*
%{_mandir}/man3/Net::Netrc.*
%{_mandir}/man3/Net::POP3.*
%{_mandir}/man3/Net::SMTP.*
%{_mandir}/man3/Net::Time.*
%endif

%files libnetcfg
%{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg*

%if %{dual_life} || %{rebuild_from_scratch}
%files Locale-Maketext
%dir %{privlib}/Locale
%dir %{privlib}/Locale/Maketext
%{privlib}/Locale/Maketext.*
%{privlib}/Locale/Maketext/Cookbook.*
%{privlib}/Locale/Maketext/Guts.*
%{privlib}/Locale/Maketext/GutsLoader.*
%{privlib}/Locale/Maketext/TPJ13.*
%{_mandir}/man3/Locale::Maketext.*
%{_mandir}/man3/Locale::Maketext::Cookbook.*
%{_mandir}/man3/Locale::Maketext::Guts.*
%{_mandir}/man3/Locale::Maketext::GutsLoader.*
%{_mandir}/man3/Locale::Maketext::TPJ13.*
%endif

%files Locale-Maketext-Simple
%dir %{privlib}/Locale
%dir %{privlib}/Locale/Maketext
%{privlib}/Locale/Maketext/Simple.pm
%{_mandir}/man3/Locale::Maketext::Simple.*

%if %{dual_life} || %{rebuild_from_scratch}
%files Math-BigInt
%dir %{privlib}/Math
%{privlib}/Math/BigFloat.pm
%{privlib}/Math/BigInt.pm
%dir %{privlib}/Math/BigInt
%{privlib}/Math/BigInt/Calc.pm
%{privlib}/Math/BigInt/Lib.pm
%{_mandir}/man3/Math::BigFloat.*
%{_mandir}/man3/Math::BigInt.*
%{_mandir}/man3/Math::BigInt::Calc.*
%{_mandir}/man3/Math::BigInt::Lib.*

%files Math-BigInt-FastCalc
%{archlib}/Math
%{archlib}/auto/Math
%{_mandir}/man3/Math::BigInt::FastCalc.*

%files Math-BigRat
%dir %{privlib}/Math
%{privlib}/Math/BigRat.pm
%{_mandir}/man3/Math::BigRat.*
%endif

%files Math-Complex
%dir %{privlib}/Math
%{privlib}/Math/Complex.pm
%{privlib}/Math/Trig.pm
%{_mandir}/man3/Math::Complex.*
%{_mandir}/man3/Math::Trig.*

%files Memoize
%{privlib}/Memoize
%{privlib}/Memoize.pm
%{_mandir}/man3/Memoize::*
%{_mandir}/man3/Memoize.*

%if %{dual_life} || %{rebuild_from_scratch}
%files MIME-Base64
%{archlib}/auto/MIME
%{archlib}/MIME
%{_mandir}/man3/MIME::*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Module-CoreList
%dir %{privlib}/Module
%{privlib}/Module/CoreList
%{privlib}/Module/CoreList.pm
%{privlib}/Module/CoreList.pod
%{_mandir}/man3/Module::CoreList*

%files Module-CoreList-tools
%{_bindir}/corelist
%{_mandir}/man1/corelist*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Module-Load
%dir %{privlib}/Module
%{privlib}/Module/Load.pm
%{_mandir}/man3/Module::Load.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Module-Load-Conditional
%dir %{privlib}/Module
%{privlib}/Module/Load
%{_mandir}/man3/Module::Load::Conditional* 
%endif

%files Module-Loaded
%dir %{privlib}/Module
%{privlib}/Module/Loaded.pm
%{_mandir}/man3/Module::Loaded*

%if %{dual_life} || %{rebuild_from_scratch}
%files Module-Metadata
%dir %{privlib}/Module
%{privlib}/Module/Metadata.pm
%{_mandir}/man3/Module::Metadata.3pm*
%endif

%files Net-Ping
%dir %{privlib}/Net
%{privlib}/Net/Ping.pm
%{_mandir}/man3/Net::Ping.*

%if %{dual_life} || %{rebuild_from_scratch}
%files PathTools
%{archlib}/Cwd.pm
%dir %{archlib}/File
%{archlib}/File/Spec*
%{archlib}/auto/Cwd
%{_mandir}/man3/Cwd*
%{_mandir}/man3/File::Spec*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Params-Check
%{privlib}/Params/
%{_mandir}/man3/Params::Check*
%endif

%files open
%{privlib}/open.pm
%{_mandir}/man3/open.3*

%if %{dual_life} || %{rebuild_from_scratch}
%files parent
%{privlib}/parent.pm
%{_mandir}/man3/parent.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files perlfaq
%{privlib}/perlfaq.pm
%dir %{privlib}/pod
%{privlib}/pod/perlfaq*
%{privlib}/pod/perlglossary.pod
%{_mandir}/man1/perlfaq*
%{_mandir}/man1/perlglossary.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files PerlIO-via-QuotedPrint
%{privlib}/PerlIO
%{_mandir}/man3/PerlIO::via::QuotedPrint.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Perl-OSType
%dir %{privlib}/Perl
%{privlib}/Perl/OSType.pm
%{_mandir}/man3/Perl::OSType.3pm*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Pod-Checker
%{_bindir}/podchecker
%dir %{privlib}/Pod
%{privlib}/Pod/Checker.pm
%{_mandir}/man1/podchecker.*
%{_mandir}/man3/Pod::Checker.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Pod-Escapes
%dir %{privlib}/Pod
%{privlib}/Pod/Escapes.pm
%{_mandir}/man3/Pod::Escapes.*
%endif

%files Pod-Html
%license Pod-Html-license-clarification
%dir %{privlib}/Pod
%{_bindir}/pod2html
%{privlib}/Pod/Html.pm
%{_mandir}/man1/pod2html.1*
%{_mandir}/man3/Pod::Html.*

%if %{dual_life} || %{rebuild_from_scratch}
%files Pod-Parser
%{_bindir}/podselect
%dir %{privlib}/Pod
%{privlib}/Pod/Find.pm
%{privlib}/Pod/InputObjects.pm
%{privlib}/Pod/ParseUtils.pm
%{privlib}/Pod/Parser.pm
%{privlib}/Pod/PlainText.pm
%{privlib}/Pod/Select.pm
%{_mandir}/man1/podselect.1*
%{_mandir}/man3/Pod::Find.*
%{_mandir}/man3/Pod::InputObjects.*
%{_mandir}/man3/Pod::ParseUtils.*
%{_mandir}/man3/Pod::Parser.*
%{_mandir}/man3/Pod::PlainText.*
%{_mandir}/man3/Pod::Select.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Pod-Perldoc
%{_bindir}/perldoc
%{privlib}/pod/perldoc.pod
%dir %{privlib}/Pod
%{privlib}/Pod/Perldoc
%{privlib}/Pod/Perldoc.pm
%{_mandir}/man1/perldoc.1*
%{_mandir}/man3/Pod::Perldoc*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Pod-Usage
%{_bindir}/pod2usage
%dir %{privlib}/Pod
%{privlib}/Pod/Usage.pm
%{_mandir}/man1/pod2usage.*
%{_mandir}/man3/Pod::Usage.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files podlators
%{_bindir}/pod2man
%{_bindir}/pod2text
%{privlib}/pod/perlpodstyle.pod
%dir %{privlib}/Pod
%{privlib}/Pod/Man.pm
%{privlib}/Pod/ParseLink.pm
%{privlib}/Pod/Text
%{privlib}/Pod/Text.pm
%{_mandir}/man1/pod2man.1*
%{_mandir}/man1/pod2text.1*
%{_mandir}/man1/perlpodstyle.1*
%{_mandir}/man3/Pod::Man*
%{_mandir}/man3/Pod::ParseLink*
%{_mandir}/man3/Pod::Text*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Pod-Simple
%dir %{privlib}/Pod
%{privlib}/Pod/Simple
%{privlib}/Pod/Simple.pm
%{privlib}/Pod/Simple.pod
%{_mandir}/man3/Pod::Simple*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Scalar-List-Utils
%{archlib}/List
%{archlib}/Scalar
%{archlib}/Sub
%{archlib}/auto/List
%{_mandir}/man3/List::Util*
%{_mandir}/man3/Scalar::Util*
%{_mandir}/man3/Sub::Util*
%endif

%files SelfLoader
%{privlib}/SelfLoader.pm
%{_mandir}/man3/SelfLoader*

%if %{dual_life} || %{rebuild_from_scratch}
%files Sys-Syslog
%dir %{archlib}/Sys
%{archlib}/Sys/Syslog.pm
%dir %{archlib}/auto/Sys
%{archlib}/auto/Sys/Syslog
%{_mandir}/man3/Sys::Syslog.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Socket
%dir %{archlib}/auto/Socket
%{archlib}/auto/Socket/Socket.*
%{archlib}/Socket.pm
%{_mandir}/man3/Socket.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Storable
%{archlib}/Storable.pm
%{archlib}/auto/Storable
%{_mandir}/man3/Storable.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Term-ANSIColor
%dir %{privlib}/Term
%{privlib}/Term/ANSIColor.pm
%{_mandir}/man3/Term::ANSIColor*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Term-Cap
%dir %{privlib}/Term
%{privlib}/Term/Cap.pm
%{_mandir}/man3/Term::Cap.*
%endif

%files Test
%{privlib}/Test.pm
%{_mandir}/man3/Test.*

%if %{dual_life} || %{rebuild_from_scratch}
%files Test-Harness
%{_bindir}/prove
%dir %{privlib}/App
%{privlib}/App/Prove*
%{privlib}/TAP*
%dir %{privlib}/Test
%{privlib}/Test/Harness*
%{_mandir}/man1/prove.1*
%{_mandir}/man3/App::Prove*
%{_mandir}/man3/TAP*
%{_mandir}/man3/Test::Harness*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Test-Simple
%{privlib}/ok*
%dir %{privlib}/Test
%{privlib}/Test/More*
%{privlib}/Test/Builder*
%{privlib}/Test/Tester*
%{privlib}/Test/Simple*
%{privlib}/Test/Tutorial*
%{privlib}/Test/use
%{privlib}/Test2*
%{_mandir}/man3/ok*
%{_mandir}/man3/Test::More*
%{_mandir}/man3/Test::Builder*
%{_mandir}/man3/Test::Tester*
%{_mandir}/man3/Test::Simple*
%{_mandir}/man3/Test::Tutorial*
%{_mandir}/man3/Test::use::*
%{_mandir}/man3/Test2*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Text-Balanced
%dir %{privlib}/Text
%{privlib}/Text/Balanced.pm
%{_mandir}/man3/Text::Balanced.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Text-ParseWords
%dir %{privlib}/Text
%{privlib}/Text/ParseWords.pm
%{_mandir}/man3/Text::ParseWords.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Text-Tabs+Wrap
%dir %{privlib}/Text
%{privlib}/Text/Tabs.pm
%{privlib}/Text/Wrap.pm
%{_mandir}/man3/Text::Tabs.*
%{_mandir}/man3/Text::Wrap.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Thread-Queue
%dir %{privlib}/Thread
%{privlib}/Thread/Queue.pm
%{_mandir}/man3/Thread::Queue.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Time-HiRes
%dir %{archlib}/Time
%{archlib}/Time/HiRes.pm
%dir %{archlib}/auto/Time
%{archlib}/auto/Time/HiRes
%{_mandir}/man3/Time::HiRes.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Time-Local
%dir %{privlib}/Time
%{privlib}/Time/Local.pm
%{_mandir}/man3/Time::Local.*
%endif

%files Time-Piece
%dir %{archlib}/Time
%{archlib}/Time/Piece.pm 
%{archlib}/Time/Seconds.pm
%dir %{archlib}/auto/Time
%{archlib}/auto/Time/Piece
%{_mandir}/man3/Time::Piece.3*
%{_mandir}/man3/Time::Seconds.3*

%if %{dual_life} || %{rebuild_from_scratch}
%files threads
%dir %{archlib}/auto/threads
%{archlib}/auto/threads/threads*
%{archlib}/threads.pm
%{_mandir}/man3/threads.3*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files threads-shared
%dir %{archlib}/auto/threads
%{archlib}/auto/threads/shared*
%dir %{archlib}/threads
%{archlib}/threads/shared*
%{_mandir}/man3/threads::shared*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Unicode-Collate
%dir %{archlib}/auto/Unicode
%{archlib}/auto/Unicode/Collate
%dir %{archlib}/Unicode
%{archlib}/Unicode/Collate
%{archlib}/Unicode/Collate.pm
%dir %{privlib}/Unicode
%{privlib}/Unicode/Collate
%{_mandir}/man3/Unicode::Collate.*
%{_mandir}/man3/Unicode::Collate::*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files Unicode-Normalize
%dir %{archlib}/auto/Unicode
%{archlib}/auto/Unicode/Normalize
%dir %{archlib}/Unicode
%{archlib}/Unicode/Normalize.pm
%{_mandir}/man3/Unicode::Normalize.*
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%files version
%{privlib}/version.pm
%{privlib}/version.pod
%{privlib}/version/
%{_mandir}/man3/version.3*
%{_mandir}/man3/version::Internals.3*
%endif

# Old changelog entries are preserved in CVS.
%changelog
* Mon Nov 11 2019 Daniel Hams <daniel.hams@gmail.com> - 4:5.30.0-1
- First copy/pasta from fedora success in compilation
