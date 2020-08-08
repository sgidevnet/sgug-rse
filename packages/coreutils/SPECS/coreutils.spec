# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary: A set of basic GNU tools commonly used in shell scripts
Name:    coreutils
Version: 8.30
Release: 6%{?dist}
License: GPLv3+
Url:     https://www.gnu.org/software/coreutils/
Source0: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source50:   supported_utils
# These are copied into this file so it can be parsed without
# installing the SRPM file.
#Source51:   coreutils-provides.inc
Source105:  coreutils-colorls.sh
Source106:  coreutils-colorls.csh

# do not make coreutils-single depend on /usr/bin/coreutils
%global __requires_exclude ^%{_bindir}/coreutils$

# md5sum,b2sum,sha*sum: --help: add note about binary/text mode
Patch1:   coreutils-8.31-sums-man-pages.patch

# disable the test-lock gnulib test prone to deadlock
Patch100: coreutils-8.26-test-lock.patch

# require_selinux_(): use selinuxenabled(8) if available
Patch105: coreutils-8.26-selinuxenable.patch

# downstream changes to default DIR_COLORS
#Patch102: coreutils-8.25-DIR_COLORS.patch
#do display processor type for uname -p/-i based on uname(2) syscall
Patch103: coreutils-8.2-uname-processortype.patch
#df --direct
Patch104: coreutils-df-direct.patch
#add note about mkdir --mode behaviour into info documentation(#610559)
Patch107: coreutils-8.4-mkdir-modenote.patch

# sh-utils
#add info about TZ envvar to date manpage
Patch703: sh-utils-2.0.11-dateman.patch
Patch713: coreutils-4.5.3-langinfo.patch

# (sb) lin18nux/lsb compliance - multibyte functionality patch
#Patch800: coreutils-i18n.patch
# (sb) lin18nux/lsb compliance - expand/unexpand
#Patch801: coreutils-i18n-expand-unexpand.patch
# i18n patch for cut - old version - used
#Patch804: coreutils-i18n-cut-old.patch
# The unexpand patch above is not correct. Sent to the patch authors
#Patch803: coreutils-i18n-fix-unexpand.patch
#(un)expand - allow multiple files on input - broken by patch 801
#Patch805: coreutils-i18n-fix2-expand-unexpand.patch
#(un)expand - test BOM headers
#Patch806: coreutils-i18n-un-expand-BOM.patch
# make 'sort -h' work for arbitrary column even when using UTF-8 locales
#Patch807: coreutils-i18n-sort-human.patch
# fold: preserve new-lines in mutlibyte text (#1418505)
#Patch808: coreutils-i18n-fold-newline.patch

#getgrouplist() patch from Ulrich Drepper.
Patch908: coreutils-getgrouplist.patch

#SELINUX Patch - implements Redhat changes
#(upstream did some SELinux implementation unlike with RedHat patch)
#Patch950: coreutils-selinux.patch

Patch1000: coreutils.sgifixes01.patch

Conflicts: filesystem < 3
# To avoid clobbering installs
Conflicts: coreutils-single

#BuildRequires: attr
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: gmp-devel
#BuildRequires: hostname
#BuildRequires: libacl-devel
#BuildRequires: libattr-devel
#BuildRequires: libcap-devel
#BuildRequires: libselinux-devel
#BuildRequires: libselinux-utils
BuildRequires: openssl-devel
#BuildRequires: strace
BuildRequires: texinfo

%if 23 < 0%{?fedora} || 7 < 0%{?rhel}
# needed by i18n test-cases
BuildRequires: glibc-langpack-en
%endif

Requires: %{name}-common = %{version}-%{release}
Requires: ncurses

Provides: coreutils-full = %{version}-%{release}
# COPY below
#%%include %%{SOURCE51}
Provides: bundled(gnulib)

# make it possible to install the latest available Adobe Reader RPM for Linux
Provides: %{_bindir}/cat
Provides: %{_bindir}/chmod
Provides: %{_bindir}/echo
Provides: %{_bindir}/ln
Provides: %{_bindir}/rm
Provides: %{_bindir}/touch
# END COPY

Obsoletes: %{name} < 8.24-100

%description
These are the GNU core utilities.  This package is the combination of
the old GNU fileutils, sh-utils, and textutils packages.

#%package single
#Summary:  coreutils multicall binary
#Suggests: coreutils-common
#Provides: coreutils = %{version}-%{release}
#Provides: coreutils%{?_isa} = %{version}-%{release}
#%include %{SOURCE51}
## To avoid clobbering installs
#Conflicts: coreutils < 8.24-100
## Note RPM doesn't support separate buildroots for %files
## http://rpm.org/ticket/874 so use RemovePathPostfixes
## (new in rpm 4.13) to support separate file sets.
#RemovePathPostfixes: .single
#%description single
#These are the GNU core utilities,
#packaged as a single multicall binary.


%package common
# yum obsoleting rules explained at:
# https://bugzilla.redhat.com/show_bug.cgi?id=1107973#c7
Obsoletes: %{name} < 8.24-100
Summary:  coreutils common optional components
%description common
Optional though recommended components,
including documentation and translations.

%prep
%autosetup -N

# will be modified by coreutils-8.25-DIR_COLORS.patch
tee DIR_COLORS{,.256color,.lightbgcolor} <src/dircolors.hin >/dev/null
# git add DIR_COLORS{,.256color,.lightbgcolor}
# git commit -m "clone DIR_COLORS before patching"

# apply all patches
%autopatch -p1

(echo ">>> Fixing permissions on tests") 2>/dev/null
find tests -name '*.sh' -perm 0644 -print -exec chmod 0755 '{}' '+'
(echo "<<< done") 2>/dev/null

autoreconf -fiv

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fpic"
%{expand:%%global optflags %{optflags} -D_GNU_SOURCE=1}
#for type in separate single; do
for type in separate; do
  mkdir $type && \
  (cd $type && ln -s ../configure || exit 1
#  if test $type = 'single'; then
#    config_single='--enable-single-binary'
#    config_single="$config_single --without-openssl"  # smaller/slower sha*sum
#    config_single="$config_single --without-gmp"      # expr/factor machine ints
#  else
#    config_single='--with-openssl'  # faster sha*sum
#  fi
    config_single="$config_single --without-openssl"  # smaller/slower sha*sum
    config_single="$config_single --without-gmp"      # expr/factor machine ints
  %configure $config_single \
             --enable-install-program=arch \
             --enable-no-install-program=kill,uptime \
             --with-tty-group \
             DEFAULT_POSIX2_VERSION=200112 alternative=199209 || :
#             --cache-file=../config.cache \ #
  make all %{?_smp_mflags}

  # make sure that parse-datetime.{c,y} ends up in debuginfo (#1555079)
  ln -v ../lib/parse-datetime.{c,y} .
  )
done

# Get the list of supported utilities
cp %SOURCE50 .

%check
#for type in separate single; do
for type in separate; do
  test $type = 'single' && subdirs='SUBDIRS=.' # Only check gnulib once
  (cd $type && make check %{?_smp_mflags} $subdirs)
done

%install
#for type in separate single; do
for type in separate; do
  install=install
  if test $type = 'single'; then
    subdir=%{_libexecdir}/%{name}; install=install-exec
  fi
  (cd $type && make DESTDIR=$RPM_BUILD_ROOT/$subdir $install)

  # chroot was in /usr/sbin :
  mkdir -p $RPM_BUILD_ROOT/$subdir/{%{_bindir},%{_sbindir}}
  mv $RPM_BUILD_ROOT/$subdir/{%_bindir,%_sbindir}/chroot

  # Move multicall variants to *.single.
  # RemovePathPostfixes will strip that later.
  if test $type = 'single'; then
    for dir in %{_bindir} %{_sbindir} %{_libexecdir}/%{name}; do
      for bin in $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/$dir/*; do
        basebin=$(basename $bin)
        mv $bin $RPM_BUILD_ROOT/$dir/$basebin.single
      done
    done
  fi
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -p -c -m644 DIR_COLORS{,.256color,.lightbgcolor} \
    $RPM_BUILD_ROOT%{_sysconfdir}
install -p -c -m644 %SOURCE105 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/colorls.sh
install -p -c -m644 %SOURCE106 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/colorls.csh

%find_lang %name
# Add the %%lang(xyz) ownership for the LC_TIME dirs as well...
grep LC_TIME %name.lang | cut -d'/' -f1-6 | sed -e 's/) /) %%dir /g' >>%name.lang

# (sb) Deal with Installed (but unpackaged) file(s) found
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Remove stty tool which doesn't do what we want under irix
rm -f $RPM_BUILD_ROOT%{_bindir}/stty
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/stty.1.gz

%files -f supported_utils
#exclude %{_bindir}/*.single
%dir %{_libexecdir}/coreutils
%{_libexecdir}/coreutils/*.so

#%files single
#%{_bindir}/*.single
#%{_sbindir}/chroot.single
#%dir %{_libexecdir}/coreutils
#%{_libexecdir}/coreutils/*.so.single
## duplicate the license because coreutils-common does not need to be installed
#%{!?_licensedir:%global license %%doc}
#%license COPYING

%files common -f %{name}.lang
%config(noreplace) %{_sysconfdir}/DIR_COLORS*
%config(noreplace) %{_sysconfdir}/profile.d/*
%{_infodir}/coreutils*
%{_mandir}/man*/*
# The following go to /usr/share/doc/coreutils-common
%doc ABOUT-NLS NEWS README THANKS TODO
%license COPYING

%changelog
* Tue Jul 14 2020 Daniel Hams <daniel.hams@gmail.com> - 8.30-6
- Stop using include which breaks ability to parse the spec with tooling

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 8.30-5
- Remove hard coded shell paths

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Kamil Dudka <kdudka@redhat.com> - 8.31-3
- disable flashing in ls colors for broken symbolic links (#1728986)

* Mon Mar 18 2019 Kamil Dudka <kdudka@redhat.com> - 8.31-2
- fix formatting of sha512sum(1) man page (#1688740)
