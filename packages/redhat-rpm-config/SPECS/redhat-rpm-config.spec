#                        TO WHOM IT MAY CONCERN
#
# 1) Don't add patches, dist-git is the upstream repository for this package.
# 2) When making changes, update version by +1, leave release alone.
#

Summary: Red Hat specific rpm configuration files
Name: redhat-rpm-config
Version: 143
Release: 4%{?dist}
# No version specified.
License: GPL+
URL: https://src.fedoraproject.org/rpms/redhat-rpm-config

# Core rpm settings
Source0: macros
Source1: rpmrc

# gcc specs files for hardened builds
Source50: redhat-hardened-cc1
Source51: redhat-hardened-ld

# gcc specs files for annobin builds
Source52: redhat-annobin-cc1

# The macros defined by these files are for things that need to be defined
# at srpm creation time when it is not feasible to require the base packages
# that would otherwise be providing the macros. other language/arch specific
# macros should not be defined here but instead in the base packages that can
# be pulled in at rpm build time, this is specific for srpm creation.
Source100: macros.fedora-misc-srpm
#Source102: macros.mono-srpm
Source103: macros.nodejs-srpm
#Source104: macros.ldc-srpm
#Source105: macros.valgrind-srpm

# Other misc macros
#Source150: macros.dwz
#Source151: macros.kmp
Source152: macros.vpath
Source153: macros.forge
#Source154: macros.ldconfig
Source155: macros.fedora-misc

# Build policy scripts
# this comes from https://github.com/rpm-software-management/rpm/pull/344
# added a python -> python2 conversion for fedora with warning
# and an echo when the mangling happens
Source201: brp-mangle-shebangs

# this comes from rpm itself
# however, now we can do Fedora changes within
Source202: brp-python-bytecompile

# Dependency generator scripts (deprecated)
Source300: find-provides
#Source301: find-provides.ksyms
Source304: find-requires
#Source305: find-requires.ksyms
#Source308: firmware.prov
#Source309: modalias.prov

# Misc helper scripts
Source400: dist.sh
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

%description
Red Hat specific rpm configuration files.

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
#install -p -m 755 -t %%{buildroot}%%{rrcdir} gpgverify
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

mkdir -p %{buildroot}%{_rpmluadir}/fedora/{rpm,srpm}
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora common.lua
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora/srpm forge.lua

%files
%dir %{rrcdir}
%{rrcdir}/macros
#%%{rrcdir}/rpmrc
%{rrcdir}/brp-*
#%%{rrcdir}/dist.sh
#%%{rrcdir}/gpgverify
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
#%%{_rpmconfigdir}/macros.d/macros.ldconfig
%{_rpmconfigdir}/macros.d/macros.vpath
%{_rpmconfigdir}/macros.d/macros.fedora-misc
%dir %{_rpmluadir}/fedora
%dir %{_rpmluadir}/fedora/srpm
%dir %{_rpmluadir}/fedora/rpm
%{_rpmluadir}/fedora/*.lua
%{_rpmluadir}/fedora/srpm/*lua

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
* Sat Jun 06 2020 Daniel Hams <daniel.hams@gmail.com> - 143-3
- Activate and customise some more macros (python compile, shebang mangle)

* Mon May 25 2020 Daniel Hams <daniel.hams@gmail.com> - 143-3
- Activate some more macros + python compilation macros

* Sun Apr 12 2020 Daniel Hams <daniel.hams@gmail.com> - 143-2
- First import with fixups

* Fri Feb 21 2020 Jason L Tibbitts III <tibbs@math.uh.edu> - 143-1
- Add dependency on fonts-srpm-macros, as those have now been approved by FPC.

* Fri Nov 01 2019 Miro Hrončok <mhroncok@redhat.com> - 142-1
- Fix the simple API of %%gpgverify.

* Thu Aug 22 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 141-2
- Simplify the API of %%gpgverify.

* Thu Jul 25 2019 Richard W.M. Jones <rjones@redhat.com> - 140-2
- Bump version and rebuild.

* Sat Jul 20 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 140-1
- Fixup python-srpm-macros version

* Wed Jul 17 2019 Lumír Balhar <lbalhar@redhat.com> - 139-1
- Use compileall2 Python module for byte-compilation in brp-python-bytecompile
