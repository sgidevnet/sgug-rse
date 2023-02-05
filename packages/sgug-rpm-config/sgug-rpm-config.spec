#                        TO WHOM IT MAY CONCERN
#
# 1) Care futzing with this - easy to break an installation
# 2) Get a 2nd someone to double sanity check ALL changes, please
#

Summary: SGUG specific rpm configuration files
Name: sgug-rpm-config
Version: 3
Release: 3%{?dist}
# No version specified.
License: GPL+
URL: https://github.com/sgidevnet/sgug-rse
Conflicts: redhat-rpm-config

# Core rpm settings
Source0: macros
Source1: rpmrc

# gcc specs files for hardened builds
#Source50: redhat-hardened-cc1
#Source51: redhat-hardened-ld

# gcc specs files for annobin builds
#Source52: redhat-annobin-cc1

# The macros defined by these files are for things that need to be defined
# at srpm creation time when it is not feasible to require the base packages
# that would otherwise be providing the macros. other language/arch specific
# macros should not be defined here but instead in the base packages that can
# be pulled in at rpm build time, this is specific for srpm creation.
Source100: macros.sgugrse-misc-srpm
#Source102: macros.mono-srpm
Source103: macros.nodejs-srpm
#Source104: macros.ldc-srpm
#Source105: macros.valgrind-srpm

# Other misc macros
#Source150: macros.dwz
#Source151: macros.kmp
Source152: macros.vpath
Source153: macros.forge
Source154: macros.ldconfig
Source155: macros.sgugrse-misc

# Build policy scripts
# this comes from https://github.com/rpm-software-management/rpm/pull/344
# added a python -> python2 conversion for fedora with warning
# and an echo when the mangling happens
Source201: brp-mangle-shebangs

# this comes from rpm itself
# however, now we can do Fedora changes within
Source202: brp-python-bytecompile

# Dependency generator scripts (deprecated)
#Source300: find-provides
#Source301: find-provides.ksyms
#Source304: find-requires
#Source305: find-requires.ksyms
#Source308: firmware.prov
#Source309: modalias.prov

# Misc helper scripts
#Source400: dist.sh
#Source401: rpmsort
#Source402: symset-table
#Source403: kmodtool
Source404: gpgverify

# 2016-10-02 snapshots from http://git.savannah.gnu.org/gitweb/?p=config.git
Source500: config.guess
Source501: config.sub

# Dependency generators & their rules
#Source600: kmod.attr
#Source601: kmod.prov
Source602: libsymlink.attr

# BRPs
#Source700: brp-ldconfig

# Convenience lua functions
Source800: common.lua
Source801: forge.lua

# Documentation
Source900: buildflags.md

# SGUG
Source1000: sgug-etc-rpm-macros

BuildArch: noarch
BuildRequires: perl-generators
Requires: coreutils

#Requires: efi-srpm-macros
Requires: fonts-srpm-macros
#Requires: fpc-srpm-macros
#Requires: ghc-srpm-macros
#Requires: gnat-srpm-macros
#Requires: go-srpm-macros
#Requires: nim-srpm-macros
#Requires: ocaml-srpm-macros
#Requires: openblas-srpm-macros
Requires: perl-srpm-macros
# ↓ Provides compileall2 Python module
Requires: python-srpm-macros >= 3-46
#Requires: rust-srpm-macros
#Requires: qt5-srpm-macros

Requires: rpm >= 4.11.0
#Requires: dwz >= 0.4
Requires: zip
# We don't do binary annotation in sgug-rse (yet, anyway)
#Requires: (annobin if gcc)

# for brp-mangle-shebangs
Requires: %{_bindir}/find
Requires: %{_bindir}/file
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
Requires: %{_bindir}/xargs

# -fstack-clash-protection and -fcf-protection require GCC 8.
Conflicts: gcc < 8.0.1-0.22

Provides: system-rpm-config = %{version}-%{release}

%global rrcdir %{_prefix}/lib/rpm/sgug
%global rpmetcdir %{_sysconfdir}/rpm

%description
SGUG specific rpm configuration files.

#%package -n kernel-rpm-macros
#Summary: Macros and scripts for building kernel module packages
#Requires: redhat-rpm-config >= 13
#
#%description -n kernel-rpm-macros
#Macros and scripts for building kernel module packages.

%prep
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .

%install
mkdir -p %{buildroot}%{rrcdir}
#install -p -m 644 -t %{buildroot}%{rrcdir} macros rpmrc
install -p -m 644 -t %{buildroot}%{rrcdir} macros
#install -p -m 444 -t %%{buildroot}%%{rrcdir} redhat-hardened-*
#install -p -m 444 -t %%{buildroot}%%{rrcdir} redhat-annobin-*
#install -p -m 755 -t %%{buildroot}%%{rrcdir} config.*
#install -p -m 755 -t %%{buildroot}%%{rrcdir} dist.sh rpmsort symset-table kmodtool
#install -p -m 755 -t %%{buildroot}%%{rrcdir} dist.sh
install -p -m 755 -t %{buildroot}%{rrcdir} gpgverify
install -p -m 755 -t %{buildroot}%{rrcdir} brp-*

#install -p -m 755 -t %%{buildroot}%%{rrcdir} find-*
#mkdir -p %%{buildroot}%%{rrcdir}/find-provides.d
#install -p -m 644 -t %%{buildroot}%%{rrcdir}/find-provides.d firmware.prov modalias.prov

#install -p -m 755 -t %%{buildroot}%%{rrcdir} brp-*

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*

mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 644 -t %{buildroot}%{_fileattrsdir} *.attr
#install -p -m 755 -t %%{buildroot}%%{_rpmconfigdir} kmod.prov

mkdir -p %{buildroot}%{_rpmluadir}/sgugrse/{rpm,srpm}
install -p -m 644 -t %{buildroot}%{_rpmluadir}/sgugrse common.lua
install -p -m 644 -t %{buildroot}%{_rpmluadir}/sgugrse/srpm forge.lua

mkdir -p %{buildroot}%{rpmetcdir}
install -p -m 644 -T sgug-etc-rpm-macros %{buildroot}%{rpmetcdir}/macros

%files
%dir %{rrcdir}
%{rrcdir}/macros
#%%{rrcdir}/rpmrc
%{rrcdir}/brp-*
#%%{rrcdir}/dist.sh
%{rrcdir}/gpgverify
#%%{rrcdir}/redhat-hardened-*
#%%{rrcdir}/redhat-annobin-*
#%%{rrcdir}/config.*
#%%{rrcdir}/find-provides
#%%{rrcdir}/find-requires
#%%{rrcdir}/brp-ldconfig
%{_fileattrsdir}/*.attr
#%%{_rpmconfigdir}/kmod.prov
%{_rpmconfigdir}/macros.d/macros.*-srpm
#%%{_rpmconfigdir}/macros.d/macros.dwz
%{_rpmconfigdir}/macros.d/macros.forge
%{_rpmconfigdir}/macros.d/macros.ldconfig
%{_rpmconfigdir}/macros.d/macros.vpath
%{_rpmconfigdir}/macros.d/macros.sgugrse-misc
%dir %{_rpmluadir}/sgugrse
%dir %{_rpmluadir}/sgugrse/srpm
%dir %{_rpmluadir}/sgugrse/rpm
%{_rpmluadir}/sgugrse/*.lua
%{_rpmluadir}/sgugrse/srpm/*lua

%dir %{rpmetcdir}
%{rpmetcdir}/macros

%doc buildflags.md

#%%files -n kernel-rpm-macros
#%%dir %%{rrcdir}/find-provides.d
#%%{rrcdir}/kmodtool
#%%{rrcdir}/rpmsort
#%%{rrcdir}/symset-table
#%%{rrcdir}/find-provides.ksyms
#%%{rrcdir}/find-requires.ksyms
#%%{rrcdir}/find-provides.d/firmware.prov
#%%{rrcdir}/find-provides.d/modalias.prov
#%%{_rpmconfigdir}/macros.d/macros.kmp

%changelog
* Sun Dec 27 2020 Daniel Hams <daniel.hams@gmail.com> - 3-3
- Bug fix - stop strip being defined recursively, which lua no likey

* Fri Dec 25 2020 Daniel Hams <daniel.hams@gmail.com> - 3-2
- Add a define (_sgug_debug) that can be passed to rpmbuild to choose debug optimisation, no RPATH linking and no symbol stripping

* Sat Aug 22 2020 Daniel Hams <daniel.hams@gmail.com> - 3-1
- Merge / fix redhat-rpm-config and sgug-rpm-config to have a single corrected package with this stuff

* Tue Jul 28 2020 Daniel Hams <daniel.hams@gmail.com> - 2-1
- Ready for 0.0.6

* Tue Jul 14 2020 Daniel Hams <daniel.hams@gmail.com> - 1-5
- Version bump for prerelease temporary dist

* Fri May 22 2020 Daniel Hams <daniel.hams@gmail.com> - 1-4
- Disable the hardcoded "bootstrap" of perl in the macros

* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 1-3
- Switch over to zstd compression

* Thu Apr 16 2020 Daniel Hams <daniel.hams@gmail.com> - 1-2
- Fix incorrect mandir (/usr/sgug/man -> /usr/sgug/share/man)

* Sun Feb 09 2020 Daniel Hams <daniel.hams@gmail.com> - 1-1
- First try as a package
