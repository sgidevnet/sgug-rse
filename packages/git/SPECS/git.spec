# Pass --without tests to rpmbuild if you don't want to run the tests
%bcond_without tests

%global gitexecdir          %{_libexecdir}/git-core

%global gitweb_httpd_conf   gitweb.conf

%global bashcomp_pkgconfig  1
%global bashcompdir         %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot        %(dirname %{bashcompdir} 2>/dev/null)
%global emacs_filesystem    0
%global libsecret           0
%global use_new_rpm_filters 0
%global use_systemd         0

# Allow cvs subpackage to be toggled via --with/--without
# Disable cvs subpackage by default on EL > 7
#%if 0%{?rhel} > 7
#%bcond_with                 cvs
#%else
#%bcond_without              cvs
#%endif

# Allow p4 subpackage to be toggled via --with/--without
# Disable by default if we lack python2 support
#%if %{without python2}
#%bcond_with                 p4
#%else
#%bcond_without              p4
#%endif

# Hardening flags for EL-7
%if 0%{?rhel} == 7
%global _hardened_build     1
%endif

# Hardening flags for EL-6
#if 0%{?rhel} == 6
#global build_cflags        %{build_cflags} -fPIC -pie
#global build_ldflags       -Wl,-z,relro -Wl,-z,now
#endif

# Define for release candidates
#global rcrev   .rc0

Name:           git
Version:        2.22.0
Release:        1%{?rcrev}%{?dist}
Summary:        Fast Version Control System
License:        GPLv2
URL:            https://git-scm.com/
Source0:        https://www.kernel.org/pub/software/scm/git/%{?rcrev:testing/}%{name}-%{version}%{?rcrev}.tar.gz
#Source1:        https://www.kernel.org/pub/software/scm/git/%{?rcrev:testing/}%{name}-%{version}%{?rcrev}.tar.sign

# Junio C Hamano's key is used to sign git releases, it can be found in the
# junio-gpg-pub tag within git.
#
# (Note that the tagged blob in git contains a version of the key with an
# expired signing subkey.  The subkey expiration has been extended on the
# public keyservers, but the blob in git has not been updated.)
#
# https://git.kernel.org/cgit/git/git.git/tag/?h=junio-gpg-pub
# https://git.kernel.org/cgit/git/git.git/blob/?h=junio-gpg-pub&id=7214aea37915ee2c4f6369eb9dea520aec7d855b
Source9:        gpgkey-junio.asc

# Local sources begin at 10 to allow for additional future upstream sources
Source11:       git.xinetd.in
Source12:       git-gui.desktop
Source13:       gitweb-httpd.conf
Source14:       gitweb.conf.in
Source15:       git@.service.in
Source16:       git.socket

# Script to print test failure output (used in %%check)
Source99:       print-failed-test-output

Patch1:         git.sgifixes01.patch

#BuildRequires:  desktop-file-utils
#BuildRequires:  emacs
#BuildRequires:  expat-devel
#BuildRequires:  findutils
#BuildRequires:  gawk
#BuildRequires:  gcc
#BuildRequires:  gettext
#BuildRequires:  gnupg2
#BuildRequires:  libcurl-devel
#BuildRequires:  make
#BuildRequires:  openssl-devel
#BuildRequires:  pcre2-devel
#BuildRequires:  perl(Error)
#BuildRequires:  perl(Test)
#BuildRequires:  perl-generators
BuildRequires:  perl
#BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  sed

#BuildRequires:  tcl
#BuildRequires:  tk
#BuildRequires:  zlib-devel >= 1.2

%if %{with tests}
# Test suite requirements
#BuildRequires:  acl
# endif fedora >= 27
BuildRequires:  bash
# endif fedora, el-6, or el7-ppc64
#BuildRequires:  httpd
# endif fedora (except i386 and s390x)
#BuildRequires:  mod_dav_svn
#BuildRequires:  perl(App::Prove)
#BuildRequires:  perl(CGI)
#BuildRequires:  perl(CGI::Carp)
#BuildRequires:  perl(CGI::Util)
#BuildRequires:  perl(DBD::SQLite)
#BuildRequires:  perl(Digest::MD5)
#BuildRequires:  perl(HTTP::Date)
#BuildRequires:  perl(IO::Pty)
#BuildRequires:  perl(JSON)
#BuildRequires:  perl(JSON::PP)
#BuildRequires:  perl(Mail::Address)
#BuildRequires:  perl(Memoize)
#BuildRequires:  perl(Test::More)
#BuildRequires:  perl(Time::HiRes)
#%if %{with python2}
#BuildRequires:  python2-devel
#%endif
## endif with python2
#%if %{with python3}
#BuildRequires:  python3-devel
#%endif
## endif with python3
#BuildRequires:  subversion
#BuildRequires:  subversion-perl
#BuildRequires:  time
%endif
# endif with tests

Requires:       git-core = %{version}-%{release}

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git rpm installs common set of tools which are usually using with
small amount of dependencies. To install all git packages, including
tools for integrating with other SCMs, install the git-all meta-package.

%package all
Summary:        Meta-package to pull in all git tools
BuildArch:      noarch
Requires:       git = %{version}-%{release}

%description all
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This is a dummy package which brings in all subpackages.

%package core
Summary:        Core package of git with minimal functionality
Requires:       less
Requires:       openssh-clients
Requires:       zlib >= 1.2
Requires:       tk >= 8.4
%description core
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git-core rpm installs really the core tools with minimal
dependencies. Install git package for common set of tools.
To install all git packages, including tools for integrating with
other SCMs, install the git-all meta-package.

%prep

# Ensure a blank line follows autosetup, el6 chokes otherwise
# https://bugzilla.redhat.com/1310704
export SHELL=%{_bindir}/bash
export CONFIG_SHELL="$SHELL"
export SHELL_PATH="$SHELL"
export PERL_PATH=%{_bindir}/perl
export TCLTK_PATH=%{_bindir}/wish
export CC=gcc
export CXX=g++

%autosetup -p1 -n %{name}-%{version}%{?rcrev}

%configure ac_cv_prog_DIFF=diff ac_cv_func_getdelim=no ac_cv_func_getline=no ac_cv_func_get_current_dir_name=no ac_cv_func_strsignal=no ac_cv_func_vfork=no ac_cv_func_euidaccess=no ac_cv_func_getloadavg=no

%build
# Improve build reproducibility
export TZ=UTC
export SOURCE_DATE_EPOCH=$(date -r version +%%s 2>/dev/null)
export SHELL=%{_bindir}/bash
export CONFIG_SHELL="$SHELL"
export SHELL_PATH="$SHELL"
export PERL_PATH=%{_bindir}/perl
export TCLTK_PATH=%{_bindir}/wish
export CC=gcc
export CXX=g++

%make_build all

%install
export TZ=UTC
export SOURCE_DATE_EPOCH=$(date -r version +%%s 2>/dev/null)
export SHELL=%{_bindir}/bash
export CONFIG_SHELL="$SHELL"
export SHELL_PATH="$SHELL"
export PERL_PATH=%{_bindir}/perl
export TCLTK_PATH=%{_bindir}/wish
export CC=gcc
export CXX=g++

%make_install

# Unnecessary bits for now
rm -rf %{buildroot}%{_datadir}/gitweb
rm -rf %{buildroot}%{_datadir}/perl5

# Some stuff we don't want included
rm -rf %{buildroot}%{_datadir}/git-core/templates/hooks/fsmonitor-watchman.sample
rm -rf %{buildroot}%{gitexecdir}/git-p4
rm -rf %{buildroot}%{gitexecdir}/git-add--interactive
rm -rf %{buildroot}%{gitexecdir}/git-send-email
rm -rf %{buildroot}%{gitexecdir}/git-svn
rm -rf %{buildroot}%{gitexecdir}/git-cvs*
rm -rf %{buildroot}%{_bindir}/git-cvs*

%check
%if %{without tests}
echo "*** Skipping tests"
exit 0
%endif
# endif without tests

# Actual make check would go here.

%files
#%{_datadir}/git-core/contrib/diff-highlight
#%{_datadir}/git-core/contrib/hooks/multimail
#%{_datadir}/git-core/contrib/hooks/update-paranoid
#%{_datadir}/git-core/contrib/hooks/setgitperms.perl
#%{_datadir}/git-core/templates/hooks/fsmonitor-watchman.sample
%{_datadir}/git-core/templates/hooks/pre-rebase.sample
%{_datadir}/git-core/templates/hooks/prepare-commit-msg.sample

%files all
# No files for you!

%files core 
#NOTE: this is only use of the %%doc macro in this spec file and should not
#      be used elsewhere
%{!?_licensedir:%global license %doc}
%license COPYING
%{_bindir}/git*
#%{bashcomproot}
%{_datadir}/git-core/
%exclude %{_datadir}/git-core/templates/hooks/pre-rebase.sample
%exclude %{_datadir}/git-core/templates/hooks/prepare-commit-msg.sample
%{gitexecdir}/*

%{_datadir}/gitk/

%{_datadir}/git-gui/

%{_datadir}/locale

%changelog
* Wed Dec 18 2019 Daniel Hams <daniel.hams@gmail.com> - 2.22.0-1
- Custom build, fedora too complex
