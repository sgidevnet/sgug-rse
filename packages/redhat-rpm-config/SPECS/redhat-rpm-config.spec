#                        TO WHOM IT MAY CONCERN
#
# 1) Don't add patches, dist-git is the upstream repository for this package.
# 2) When making changes, update version by +1, leave release alone.
#

Summary: Red Hat specific rpm configuration files
Name: redhat-rpm-config
Version: 143
Release: 2%{?dist}
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

# We don't use kernel modules macros
#%%global rrcdir /usr/lib/rpm/redhat

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
#mkdir -p %{buildroot}%{rrcdir}
#install -p -m 644 -t %{buildroot}%{rrcdir} macros rpmrc
#install -p -m 444 -t %{buildroot}%{rrcdir} redhat-hardened-*
#install -p -m 444 -t %{buildroot}%{rrcdir} redhat-annobin-*
#install -p -m 755 -t %{buildroot}%{rrcdir} config.*
#install -p -m 755 -t %{buildroot}%{rrcdir} dist.sh rpmsort symset-table kmodtool
#install -p -m 755 -t %{buildroot}%{rrcdir} dist.sh
#install -p -m 755 -t %{buildroot}%{rrcdir} gpgverify
#install -p -m 755 -t %{buildroot}%{rrcdir} brp-*

#install -p -m 755 -t %{buildroot}%{rrcdir} find-*
#mkdir -p %{buildroot}%{rrcdir}/find-provides.d
#install -p -m 644 -t %{buildroot}%{rrcdir}/find-provides.d firmware.prov modalias.prov

#install -p -m 755 -t %{buildroot}%{rrcdir} brp-*

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*

mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 644 -t %{buildroot}%{_fileattrsdir} *.attr
#install -p -m 755 -t %{buildroot}%{_rpmconfigdir} kmod.prov

mkdir -p %{buildroot}%{_rpmluadir}/fedora/{rpm,srpm}
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora common.lua
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora/srpm forge.lua

%files
#%dir %{rrcdir}
#%{rrcdir}/macros
#%{rrcdir}/rpmrc
#%{rrcdir}/brp-*
#%{rrcdir}/dist.sh
#%{rrcdir}/gpgverify
#%{rrcdir}/redhat-hardened-*
#%{rrcdir}/redhat-annobin-*
#%{rrcdir}/config.*
#%{rrcdir}/find-provides
#%{rrcdir}/find-requires
#%{rrcdir}/brp-ldconfig
%{_fileattrsdir}/*.attr
#%{_rpmconfigdir}/kmod.prov
%{_rpmconfigdir}/macros.d/macros.*-srpm
#%{_rpmconfigdir}/macros.d/macros.dwz
%{_rpmconfigdir}/macros.d/macros.forge
#%{_rpmconfigdir}/macros.d/macros.ldconfig
%{_rpmconfigdir}/macros.d/macros.vpath
%{_rpmconfigdir}/macros.d/macros.fedora-misc
%dir %{_rpmluadir}/fedora
%dir %{_rpmluadir}/fedora/srpm
%dir %{_rpmluadir}/fedora/rpm
%{_rpmluadir}/fedora/*.lua
%{_rpmluadir}/fedora/srpm/*lua

%doc buildflags.md

#%files -n kernel-rpm-macros
#%dir %{rrcdir}/find-provides.d
#%{rrcdir}/kmodtool
#%{rrcdir}/rpmsort
#%{rrcdir}/symset-table
#%{rrcdir}/find-provides.ksyms
#%{rrcdir}/find-requires.ksyms
#%{rrcdir}/find-provides.d/firmware.prov
#%{rrcdir}/find-provides.d/modalias.prov
#%{_rpmconfigdir}/macros.d/macros.kmp

%changelog
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

* Tue Jul 09 2019 Miro Hrončok <mhroncok@redhat.com> - 138-1
- Move brp-python-bytecompile from rpm, so we can easily adapt it

* Mon Jul 08 2019 Nicolas Mailhot <nim@fedoraproject.org> - 137-1
- listfiles: make it robust against all kinds of “interesting” inputs
- wordwrap: make list indenting smarter, to produce something with enough
  structure that it can be converted into AppStream metadata

* Mon Jul 08 2019 Robert-André Mauchin <zebob.m@gmail.com> - 136-1
- Revert "Fix expansion in listfiles_exclude/listfiles_include"

* Mon Jul 08 2019 Nicolas Mailhot <nim@fedoraproject.org> - 135-1
- Fix expansion in listfiles_exclude/listfiles_include

* Mon Jul 01 2019 Florian Festi <ffesti@redhat.com> - 134-1
- Switch binary payload compression to Zstandard level 19

* Thu Jun 27 2019 Vít Ondruch <vondruch@redhat.com> - 133-2
- Enable RPM to set SOURCE_DATE_EPOCH environment variable.

* Tue Jun 25 08:13:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 133-1
- Expand listfiles_exclude/listfiles_include

* Tue Jun 11 2019 Jitka Plesnikova <jplesnik@redhat.com> - 132-1
- Remove perl macro refugees

* Mon Jun 10 2019 Panu Matilainen <pmatilai@redhat.com> - 131-1
- Provide temporary shelter for rpm 4.15 perl macro refugees

* Tue Jun 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 130-1
- New macro for wrapping text — %%wordwrap
- Smal fix for %%listfiles with no arguments

* Thu May 30 2019 Björn Persson <Bjorn@Rombobjörn.se> - 129-1
- Added gpgverify.

* Tue Jan 15 2019 Panu Matilainen <pmatilai@redhat.com> - 128-1
- Drop redundant _smp_mflag re-definition, use the one from rpm instead

* Thu Dec 20 2018 Florian Weimer <fweimer@redhat.com> - 127-1
- Build flags: Add support for extension builders (#1543394)

* Mon Dec 17 2018 Panu Matilainen <pmatilai@redhat.com> - 126-1
- Silence the annoying warning from ldconfig brp-script (#1540971)

* Thu Nov 15 2018 Miro Hrončok <mhroncok@redhat.com> - 125-1
- Make automagic Python bytecompilation optional
  https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2

* Thu Nov 08 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 124-1
- forge: add more distprefix cleaning (bz1646724)

* Mon Oct 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 123-1
- Add -q option to %%forgesetup

* Sat Oct 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 122-1
- Allow multiple calls to forge macros

* Thu Oct 11 2018 Jan Pazdziora <jpazdziora@redhat.com> - 121-1
- Add %_swidtagdir for directory for SWID tag files describing the
  installation.

* Mon Sep 10 2018 Miro Hrončok <mhroncok@redhat.com> - 120-1
- Make ambiguous python shebangs error
  https://fedoraproject.org/wiki/Changes/Make_ambiguous_python_shebangs_error

* Mon Aug 20 2018 Kalev Lember <klember@redhat.com> - 119-1
- Add aarch64 to ldc arches

* Wed Aug 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 118-1
- Enable --as-needed by default

* Mon Jul 16 2018 Miro Hrončok <mhroncok@redhat.com> - 117-1
- Mangle /bin shebnags to /usr/bin ones (#1581757)

* Tue Jul 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 116-1
- Add option to add -Wl,--as-needed into LDFLAGS

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 115-1
- Disable non-functional ppc64 support for ldc packages

* Tue Jun 26 2018 Panu Matilainen <pmatilai@redhat.com> - 114-1
- Fix kernel ABI related strings (Peter Oros, #26)
- Automatically trim changelog to two years (Zbigniew Jędrzejewski-Szmek, #22)
- Cosmetics cleanups (Zbigniew Jędrzejewski-Szmek, #22)

* Mon Jun 18 2018 Florian Weimer <fweimer@redhat.com> - 113-1
- Build flags: Require SSE2 on i686 (#1592212)

* Mon May 28 2018 Miro Hrončok <mhroncok@redhat.com> - 112-1
- Add a possibility to opt-out form automagic Python bytecompilation
  https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation

* Wed May 02 2018 Peter Jones <pjones@redhat.com> - 111-1
- brp-mangle-shebangs: add %%{__brp_mangle_shebangs_exclude_file} and
  %%{__brp_mangle_shebangs_exclude_from_file} to allow you to specify files
  containing the shebangs to be ignore and files to be ignored regexps,
  respectively, so that they can be generated during the package build.

* Wed May  2 2018 Florian Weimer <fweimer@redhat.com> - 110-1
- Reflect -fasynchronous-unwind-tables GCC default on POWER (#1550914)

* Wed May  2 2018 Florian Weimer <fweimer@redhat.com> - 109-1
- Use plain -fcf-protection compiler flag, without -mcet (#1570823)

* Tue May 01 2018 Peter Jones <pjones@redhat.com> - 108-1
- Add Requires: efi-srpm-macros for %%{efi}

* Fri Apr 20 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 107-1
- Add %%_metainfodir macro.
- %%forgeautosetup tweak to fix patch application.

* Mon Mar 05 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 106-1
- Update forge macros.

* Wed Feb 28 2018 Florian Weimer <fweimer@redhat.com> - 105-1
- Make -fasynchronous-unwind-tables explicit on aarch64 (#1536431)

* Wed Feb 28 2018 Florian Weimer <fweimer@redhat.com> - 104-1
- Use -funwind-tables on POWER (#1536431, #1548847)

* Sun Feb 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 103-1
- Make %%ldconfig_post/%%ldconfig_postun parameterized

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 102-1
- Second step of -z now move: removal from GCC specs file (#1548397)

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 101-1
- First step of moving -z now to the gcc command line (#1548397)

* Thu Feb 22 2018 Miro Hrončok <mhroncok@redhat.com> - 100-1
- Don't mangle shebangs with whitespace only changes (#1546993)

* Thu Feb 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 99-1
- Move %%end to %%ldconfig_scriptlets

* Sat Feb 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 98-1
- Explicitly close scriptlets with %%end (ldconfig)

* Wed Feb 14 2018 Miro Hrončok <mhroncok@redhat.com> - 97-1
- Allow to opt-out from shebang mangling for specific paths/shebangs

* Thu Feb 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 96-1
- Simplify/Fix check for shebang starting with "/"

* Wed Feb 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 95-1
- Fix mangling env shebangs with absolute paths

* Sun Feb  4 2018 Florian Weimer <fweimer@redhat.com> - 94-1
- Add RPM macros for compiler/linker flags

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 93-1
- Use newly available /usr/bin/grep

* Wed Jan 31 2018 Peter Robinson <pbrobinson@fedoraproject.org> 92-1
- Use generic tuning for ARMv7

* Tue Jan 30 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 91-1
- The grep package only provides /bin/grep, not /usr/bin/grep.

* Mon Jan 29 2018 Miro Hrončok <mhroncok@redhat.com> - 90-1
- Add brp-mangle-shebangs

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 89-1
- Add macros.ldconfig

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 88-1
- Create DSO symlinks automatically

* Mon Jan 29 2018 Florian Weimer <fweimer@redhat.com> - 87-1
- Build flags: Disable -z defs again (#1535422)

* Mon Jan 29 2018 Florian Weimer <fweimer@redhat.com> - 86-1
- Build flags: Enable CET on i686, x86_64 (#1538725)

* Thu Jan 25 2018 Florian Weimer <fweimer@redhat.com> - 85-1
- Build flags: Switch to generic tuning on i686 (#1538693)

* Mon Jan 22 2018 Florian Weimer <fweimer@redhat.com> - 84-1
- Link with -z defs by default (#1535422)

* Mon Jan 22 2018 Florian Weimer <fweimer@redhat.com> - 83-1
- Make armhfp flags consistent with GCC defaults

* Mon Jan 22 2018 Florian Weimer <fweimer@redhat.com> - 82-1
- Make use of -fasynchronous-unwind-tables more explicit (#1536431)

* Mon Jan 22 2018 Florian Weimer <fweimer@redhat.com> - 81-1
- Remove --param=ssp-buffer-size=4

* Mon Jan 22 2018 Florian Weimer <fweimer@redhat.com> - 80-1
- Document build flags

* Fri Jan 19 2018 Panu Matilainen <pmatilai@redhat.com> - 79-1
- Document how to disable hardened and annotated build (#1211296)

* Wed Jan 17 2018 Panu Matilainen <pmatilai@redhat.com> - 78-1
- Fix the inevitable embarrassing typo in 77, doh

* Wed Jan 17 2018 Panu Matilainen <pmatilai@redhat.com> - 77-1
- Macroize build root policies for consistent disable/override ability

* Wed Jan 17 2018 Florian Weimer <fweimer@redhat.com> - 76-1
- Add -fstack-clash-protection for supported architectures (#1515865)

* Wed Jan 17 2018 Florian Weimer <fweimer@redhat.com> - 75-1
- Add _GLIBCXX_ASSERTIONS to CFLAGS/CXXFLAGS (#1515858)

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 74-1
- Remove Requires: cmake-rpm-macros

* Thu Jan 11 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 73-1
- Add macros.forge for simplifying packaging of forge-hosted packages.  See
  https://fedoraproject.org/wiki/Forge-hosted_projects_packaging_automation and
  https://bugzilla.redhat.com/show_bug.cgi?id=1523779

* Wed Jan 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 72-1
- Add Requires: nim-srpm-macros for %%nim_arches

* Tue Jan 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 71-1
- Require annobin only if gcc is installed

* Thu Dec 21 2017 Björn Esser <besser82@fedoraproject.org> - 70-2
- Add Requires: cmake-rpm-macros for CMake auto-{provides,requires} (#1498894)

* Fri Dec 08 2017 Panu Matilainen <pmatilai@redhat.com> - 70-1
- Update URL to current location at src.fedoraproject.org

* Wed Nov 22 2017 Nick Clifton <nickc@redhat.com> - 69-1
- Enable binary annotations in compiler flags

* Thu Oct 26 2017 Troy Dawson <tdawson@redhat.com> - 68-1
- Remove Requires: fedora-rpm-macros

* Mon Jul 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 67-1
- Define _include_gdb_index (RHBZ #1476722)
- Move _debuginfo_subpackages and _debugsource_packages from rpm (RHBZ #1476735)

* Tue Jul 18 2017 Florian Festi <ffesti@redhat.com> - 66-1
- Honor %%kmodtool_generate_buildreqs (#1472201)

* Thu Jul 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 65-1
- Add Requires: rust-srpm-macros for %%rust_arches

* Wed Mar 15 2017 Orion Poplawski <orion@cora.nwra.com> - 64-1
- Add Requires: openblas-srpm-macros for %%openblas_arches

* Thu Feb 02 2017 Dan Horák <dan[at]danny.cz> - 63-1
- set zEC12 as minimum architecture level for s390(x) (#1404991)

* Thu Dec 15 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 62-1
- Add macros.vpath (https://fedorahosted.org/fpc/attachment/ticket/655)

* Tue Dec 06 2016 Adam Williamson <awilliam@redhat.com> - 61-1
- revert changes from 60, they break far too much stuff (#1401231)

* Wed Nov 30 2016 Panu Matilainen <pmatilai@redhat.com> - 60-1
- Error on implicit function declaration and -return type for C (#1393492)

* Wed Nov 30 2016 Panu Matilainen <pmatilai@redhat.com> - 59-1
- Move global compiler flags to __global_compiler_flags macro
- Introduce separate __global_fooflags for C, C++ and Fortran

* Tue Nov 29 2016 Panu Matilainen <pmatilai@redhat.com> - 58-1
- Drop atom optimization on i686 (#1393492)

* Tue Nov 15 2016 Dan Horák <dan[at]danny.cz> - 57-1
- set z10 as minimum architecture level for s390(x)

* Fri Nov 11 2016 Panu Matilainen <pmatilai@redhat.com> - 56-1
- Fix directory name mismatch in kernel_source macro (#648996)

* Tue Nov 08 2016 Michal Toman <mtoman@fedoraproject.org> - 55-1
- Add default compiler flags for various MIPS architectures (#1366735)

* Tue Nov 08 2016 Panu Matilainen <pmatilai@redhat.com> - 54-1
- -pie is incompatible with static linkage (#1343892, #1287743)

* Mon Nov 07 2016 Panu Matilainen <pmatilai@redhat.com> - 53-1
- Drop brp-java-repack-jars by request (#1235770)
- Drop brp-implant-ident-static, unused for 13 years and counting

* Mon Nov 07 2016 Lubomir Rintel <lkundrak@v3.sk> - 52-1
- Add valgrind_arches macro for BuildRequires of valgrind

* Fri Nov 04 2016 Stephen Gallagher <sgallagh@redhat.com> - 51-1
- Add s390x build target for Node.js packages

* Mon Oct 31 2016 Kalev Lember <klember@redhat.com> - 50-1
- Add ldc_arches macro

* Mon Oct 17 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 49-1
- Remove hardcoded limit of 16 CPUs for makefile parallelism.
- See https://bugzilla.redhat.com/show_bug.cgi?id=1384938

* Thu Oct 13 2016 Richard W.M. Jones <rjones@redhat.com> 48-1
- Add support for riscv64.
  This also updates config.sub/config.guess to the latest upstream versions.

* Wed Oct 12 2016 Peter Robinson <pbrobinson@fedoraproject.org> 47-1
- Enable aarch64 for mono arches

* Mon Oct 03 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 46-1
- Allow %%configure to optionally pass --disable-silent-rules.  Define
  %%_configure_disable_silent_rules (defaulting to 0) to control this.

* Wed Sep 14 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 45-1
- Add dependency on qt5-srpm-macros.

* Fri Aug 12 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 44-1
- And somehow I managed to make a typo in that dependency.

* Fri Aug 12 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 43-1
- Add dependency on fedora-rpm-macros.

* Tue Apr 12 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 42-1
- Add dependency on fpc-srpm-macros.

* Mon Apr 11 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 41-1
- Add a file for miscellaneous macros, currently containing just %%rpmmacrodir.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Dan Horák <dan[at]danny.cz> 40-1
- switch to -mcpu=power8 for ppc64le default compiler flags

* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> 39-1
- Add Requires: python-srpm-macros

* Fri Jan  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 38-1
- Add missing ARMv6 optflags

* Wed Dec  2 2015 Peter Robinson <pbrobinson@fedoraproject.org> 37-1
- nodejs 4+ now supports aarch64 and power64

* Fri Jul 17 2015 Florian Festi <ffesti@redhat.com> 36-1
- Add Requires: go-srpm-macros (#1243922)

* Thu Jul 09 2015 Sandro Mani <manisandro@gmail.com> 35-1
- Use %%__libsymlink_path instead of %%__libsymlink_exclude_path in libsymlink.attr

* Wed Jul 08 2015 Adam Jackson <ajax@redhat.com> 34-1
- Fix cc1 specs mishandling of incremental linking

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Dan Horák <dan[at]danny.cz> 33-1
- Mono 4 adds support for ppc64le

* Fri May 29 2015 Florian Festi <ffesti@redhat.com> 32-1
- Support out of source builds for %%_configure_gnuconfig_hack (#1191788)
- Fix typo in %%kernel_module_package (#1159361)

* Tue May 19 2015 Florian Festi <ffesti@redhat.com> 31-1
- Add %%py_auto_byte_compile macro controlling Python bytecompilation
(#976651)

* Wed Apr 29 2015 Florian Festi <ffesti@redhat.com> 30-1
- Fix libsymlink.attr for new magic pattern for symlinks (#1207945)

* Wed Apr 08 2015 Adam Jackson <ajax@redhat.com> 29-1
- Fix ld specs mishandling of incremental linking

* Thu Feb 19 2015 Till Maas <opensource@till.name> - 28-1
- Enable harden flags by default (#1192183)

* Wed Dec 10 2014 Dan Horák <dan[at]danny.cz> - 27-1
- Explicitly set -mcpu/-mtune for ppc64p7 and ppc64le to override rpm defaults

* Mon Sep 22 2014 Panu Matilainen <pmatilai@redhat.com> - 26-1
- Gnat macros are now in a package of their own (#1133632)

* Fri Sep 19 2014 Dan Horák <dan[at]danny.cz> - 25-1
- there is still no properly packaged Mono for ppc64le

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 24-1
- ARMv7 has Ada so add it to GNAT_arches

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 23-2
- Changed ppc64 to power64 macro for mono_archs

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org>
- aarch64 has Ada so add it to GNAT_arches

* Mon May 12 2014 Josh Boyer <jwboyer@fedoraproject.org> - 22-1
- Fix kmod.prov to deal with compressed modules (#1096349)

* Wed Apr 30 2014 Jens Petersen <petersen@redhat.com> - 21-1
- macros.ghc-srpm moved to ghc-rpm-macros package (#1089102)
- add requires ghc-srpm-macros

* Tue Apr 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 20-1
- With gcc 4.9 aarch64 now supports stack-protector

* Sun Apr 27 2014 Ville Skyttä <ville.skytta@iki.fi> - 19-1
- Drop bunch of duplicated-with-rpm macro definitions and brp-* scripts

* Tue Apr 15 2014  Panu Matilainen <pmatilai@redhat.com> - 18-1
- Temporarily bring back find-requires and -provides scripts to rrc-side

* Tue Apr 15 2014  Panu Matilainen <pmatilai@redhat.com> - 17-1
- Let OCaml handle its own arch macros (#1087794)

* Tue Apr 15 2014  Panu Matilainen <pmatilai@redhat.com> - 16-1
- Move kmod and libsymlink dependency generators here from rpm

* Thu Apr 10 2014  Panu Matilainen <pmatilai@redhat.com> - 15-1
- Drop most of the script-based dependency generation bits

* Tue Apr 08 2014  Panu Matilainen <pmatilai@redhat.com> - 14-1
- Add Mono path macros (#1070936)
- Allow opting out of config.{guess,sub} replacement hack (#991613)

* Tue Apr 08 2014  Panu Matilainen <pmatilai@redhat.com> - 13-1
- Move the remaining dependency generator stuff to the kmp macro package
- Stop overriding rpm external dependency generator settings by default

* Mon Apr 07 2014  Panu Matilainen <pmatilai@redhat.com> - 12-1
- Be more explicit about the package contents
- Split kernel module macros to a separate file
- Split kernel module scripts and macros to a separate package

* Wed Apr 02 2014  Panu Matilainen <pmatilai@redhat.com> - 11-1
- Stop pretending this package is relocatable, its not
- Require rpm >= 4.11 for /usr/lib/rpm/macros.d support etc
- Move our macros out of from /etc, they're not configuration

* Wed Apr 02 2014  Panu Matilainen <pmatilai@redhat.com> - 10-1
- Make fedora dist-git the upstream of this package and its sources
- Add maintainer comments to spec wrt versioning and changes

* Mon Mar 24 2014 Dan Horák <dan[at]danny.cz> - 9.1.0-58
- enable ppc64le otherwise default rpm cflags will be used

* Fri Feb 07 2014 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-57
- config.guess/sub don't need to be group-writable (#1061762)

* Sun Jan 12 2014 Kevin Fenzi <kevin@scrye.com> 9.1.0-56
- Update libtool hardening hack and re-enable (#978949)

* Wed Dec 18 2013 Dhiru Kholia <dhiru@openwall.com> - 9.1.0-55
- Enable "-Werror=format-security" by default (#1043495)

* Wed Sep 04 2013 Karsten Hopp <karsten@redhat.com> 9.1.0-54
- update config.sub with ppc64p7 support (from Fedora automake)

* Fri Aug 16 2013 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-53
- updated config.guess/sub from upstream for little-endian ppc archs

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 9.1.0-52
- Perl 5.18 rebuild

* Thu Jul 25 2013 Tomas Mraz <tmraz@redhat.com> 9.1.0-51
- Disable the libtool hack as it is breaking builds

* Wed Jul 24 2013 Kevin Fenzi <kevin@scrye.com> 9.1.0-50
- Make docdirs unversioned on Fedora 20+ (#986871)
- Hack around libtool issue for hardened build for now (#978949)

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 9.1.0-49
- Perl 5.18 rebuild

* Fri Jul 05 2013 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-48
- fix brp-java-repack-jars failing on strange permissions (#905573)

* Thu Jul 04 2013 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-47
- switch from -fstack-protector to -fstack-protector-strong (#978763)

* Thu Jun 27 2013 Panu Matilainen <pmatilai@redhat.com> - - 9.1.0-46
- make cpu limit for building configurable through _smp_ncpus_max macro

* Tue May 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 9.1.0-45
- add nodejs_arches macro for ExclusiveArch for Node.js packages

* Mon May 13 2013 Adam Jackson <ajax@redhat.com> 9.1.0-44
- redhat-config-*: Use + to append rather than %%rename, to protect against
  multiple -specs= ending up in the command line. (#892837)

* Tue Apr 23 2013 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-43
- Add optflags stack protector override for AArch64 (#909788)
- Also set FCFLAGS from %%configure (#914831)

* Mon Apr 22 2013 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-42
- Switch back to manual config.guess/sub copies for reproducability
- Replace config.guess/sub from %%configure again (#951442)

* Mon Apr 22 2013 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-41
- Add -grecord-gcc-switches to global CFLAGS (#951669)

* Mon Mar 25 2013 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-40
- Add virtual system-rpm-config provide

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 9.1.0-38
- add ARM to ghc_arches_with_ghci for ghc-7.4.2 ghci support
  (NB this change should not be backported before ghc-7.4.2)

* Fri Nov  9 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 9.1.0-37
- Patch to fix spaces in java jar files
  https://bugzilla.redhat.com/show_bug.cgi?id=872737

* Fri Nov  9 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 9.1.0-36
- Patch to fix spaces in files used in filtering macros
  https://bugzilla.redhat.com/show_bug.cgi?id=783932

* Wed Oct  3 2012 Ville Skyttä <ville.skytta@iki.fi> - 9.1.0-35
- Drop (un)setting LANG and DISPLAY in build stages, require rpm >= 4.8.0.

* Wed Oct  3 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 9.1.0-34
- Add patch from https://bugzilla.redhat.com/show_bug.cgi?id=783433
  to fix spaces in files and directories that are fed to the
  brp-python-hardlink script
- Require zip since java repack jars requires it
  https://bugzilla.redhat.com/show_bug.cgi?id=857479
- Java jars need the MANIFEST.MF file to be first in the archive
  https://bugzilla.redhat.com/show_bug.cgi?id=465664
- Fix kernel_source macro to match the directory that kernel sources are installed in
  https://bugzilla.redhat.com/show_bug.cgi?id=648996
- Patch _mandir, _infodir, and _defaultocdir to use _prefix
  https://bugzilla.redhat.com/show_bug.cgi?id=853216

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-32
- enable minidebuginfo generation (#834073)

* Mon Jun 25 2012 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-31
- revert back to plain -g, -g3 seems to cancel dwz size improvements

* Mon Jun 25 2012 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-30
- require dwz, enable dwarf compression for debuginfo packages (#833311)

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 9.1.0-29
- Pull in dependency with macros specific for building Perl source packages

* Sat Mar  3 2012 Jens Petersen <petersen@redhat.com> - 9.1.0-28
- add s390 and s390x to ghc_arches

* Wed Feb 22 2012 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-27
- add GNAT arch definitions

* Sun Jan 15 2012 Dennis Gilmore <dennis@ausil.us> - 9.1.0-26
- per ppc team request drop -mminimal-toc on ppc64

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 27 2011 Jens Petersen <petersen@redhat.com> - 9.1.0-24
- add ghc_arches_with_ghci

* Wed Nov 09 2011 Dennis Gilmore <dennis@ausil.us> - 9.1.0-23
- remove patch that forces --disable-silent-rules to configure
- it breaks anything set to not ignore unknown configure options

* Tue Oct 18 2011 Jens Petersen <petersen@redhat.com> - 9.1.0-22
- add armv5tel to ghc_arches

* Wed Sep 28 2011 Dennis Gilmore <dennis@ausil.us> - 9.1.0-21
- build armv5tel on armv7l since they are the same abi armv7hl is
  an incompatible ABI

* Wed Sep 28 2011 Jens Petersen <petersen@redhat.com> - 9.1.0-20
- add armv7hl to ghc_arches

* Sun Sep 25 2011 Ville Skyttä <ville.skytta@iki.fi> - 9.1.0-19
- Fix URL.

* Thu Sep 22 2011 Adam Jackson <ajax@redhat.com> 9.1.0-18
- redhat-hardened-cc1: Inject -fPIE, not -fPIC.
  cf. http://lists.fedoraproject.org/pipermail/devel/2011-September/157365.html

* Fri Sep 16 2011 Adam Jackson <ajax@redhat.com> 9.1.0-17
- Expose %%_hardening_{c,ld}flags independently to make it easier for
  packages to apply them to selected components

* Wed Aug 10 2011 Colin Walters <walters@verbum.org> - 9.1.0-16
- Globally disable silent rules

* Wed Aug 03 2011 Adam Jackson <ajax@redhat.com> 9.1.0-15
- redhat-hardened-{cc1,ld}: Move some of the rewrite magic to gcc specs so
  we don't end up with both -fPIC and -fPIE on the command line

* Mon Aug 01 2011 Adam Jackson <ajax@redhat.com> 9.1.0-14
- redhat-rpm-config-9.1.0-hardened.patch: Add macro magic for %%_hardened_build

* Thu Jul 07 2011 Adam Jackson <ajax@redhat.com> 9.1.0-13
- redhat-rpm-config-9.1.0-relro.patch: LDFLAGS, not CFLAGS.

* Sat Jul 02 2011 Jon Masters <jcm@jonmasters.org> - 9.1.0-12
- redhat-rpm-config-9.1.0-arm.patch: Make armv7hl default on all v7 ARM

* Mon Jun 27 2011 Adam Jackson <ajax@redhat.com> - 9.1.0-11
- redhat-rpm-config-9.1.0-relro.patch: Add -Wl,-z,relro to __global_cflags

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 9.1.0-10
- revert last build since releng prefers exclusivearch here

* Sat Jun 18 2011 Jens Petersen <petersen@redhat.com> - 9.1.0-9
- replace ghc_archs with ghc_excluded_archs

* Mon Jun 13 2011 Dennis Gilmore <dennis@ausil.us> - 9.1.0-8
- add arm hardware float macros, fix up armv7l

* Mon May 30 2011 Dennis Gilmore <dennis@ausil.us> - 9.1.0-7
- add -srpm to the arches files so that the base language macros can
  be parallel installable with these

* Fri May 27 2011 Dennis Gilmore <dennis@ausil.us> - 9.1.0-6
- add some specific macros needed at srpm creation time

* Thu May 27 2010 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-5
- adjust to new pkg-config behavior wrt private dependencies (#596433)

* Mon Mar 01 2010 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-4
- avoid unnecessarily running brp-strip-comment-note (#568924)

* Mon Feb 15 2010 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-3
- unbreak find-requires again, doh (#564527)

* Wed Feb 3 2010 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-2
- python byte-compilation errors abort the build by default

* Tue Feb 2 2010 Panu Matilainen <pmatilai@redhat.com> - 9.1.0-1
- new version, lose merged patches (fixes #521141, #455279, #496522, #458648)
- require rpm for parent dir, version >= 4.6.0 for sane keyserver behavior
- buildrequire libtool to grab copies of config.guess and config.sub
- add URL to the git repo and upstream changelog as documentation

* Mon Nov 23 2009 Orion Poplawski <orion@cora.nwra.com> - 9.0.3-19
- Change configure macro to use _configure to allow override (bug #489942)

* Mon Sep 28 2009 Bill Nottingham <notting@redhat.com>
- Drop xz compression level to 2

* Thu Sep 03 2009 Adam Jackson <ajax@redhat.com>
- Delete *.orig in %%install

* Thu Sep 03 2009 Paul Howarth <paul@city-fan.org> 9.0.3-17
- redhat-rpm-config-9.0.3-filtering-macros.patch: Rediff so we don't ship a .orig file
- add (empty) %%build section
- fix unescaped macros in changelog

* Tue Aug 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 9.0.3-16
- add the filtering framework approved by the FPC/FESCo. (#516240)

* Thu Aug 13 2009 Adam Jackson <ajax@redhat.com> 9.0.3-15
- redhat-rpm-config-9.0.4-brpssa-speedup.patch: When looking for static
  archives, only run file(1) on files named *.a. (#517101)

* Wed Aug 12 2009 Adam Jackson <ajax@redhat.com> 9.0.3-14
- redhat-rpm-config-9.0.3-jars-with-spaces.patch: Handle repacking jars
  whose filenames contain spaces. (#461854)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Bill Nottingham <notting@redhat.com> 9.0.3-12
- use XZ payload compression for binary packages

* Tue Jul 21 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 9.0.3-10
- always delete %%buildroot as first step of %%install (as long as %%buildroot is not /)

* Fri Jul 17 2009 Bill Nottingham <notting@redhat.com> 9.0.3-10
- apply fedora 12 default buildflags

* Wed Jun 03 2009 Adam Jackson <ajax@redhat.com> 9.0.3-9
- limit-smp-16-threads.patch: Rediff so we don't ship a .orig file (#500316)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Jon Masters <jcm@redhat.com> - 9.0.3-7
- Change default hashing algorithm in file digests to SHA-256
- Resolves: #485826.

* Tue Feb 17 2009 Dennis Gilmore <dennis@ausil.us> - 9.0.3-6
- add missing armv7l arch
- set the default build arch to match fedora arm build target

* Mon Feb 16 2009 Dennis Gilmore <dennis@ausil.us> - 9.0.3-5
- apply fedora 11 default buildflags
- set 32 bit intel build arch to i586 on compatible hardware
- set 32 bit sparc build arch to sparcv9 on compatible hardware

* Mon Feb 16 2009 Dennis Gilmore <dennis@ausil.us> - 9.0.3-4
- limit _smp_flags to -j16

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 9.0.3-3
- fix license tag
- nuke ancient conflicts

* Mon Aug 11 2008 Panu Matilainen <pmatilai@redhat.com> - 9.0.3-2
- Unbreak find-requires (#443015)

* Tue May 06 2008 Jon Masters <jcm@redhat.com> - 9.0.3-1
- Ensure Java Jar files have readable files within.
- Remove overwritten config.guess|sub files (testing).
- Fix Fortran flags for building using _fmoddir.
- Pull in objdump fix to upstream find-requires.

* Thu Apr 03 2008 Jon Masters <jcm@redhat.com> - 9.0.2-1
- Remove smp dependencies
- Update config.guess|sub files
- Don't call find-requires.ksyms for kmod packages (kernel kABI scripts).

* Thu Jul 05 2007 Jesse Keating <jkeating@redhat.com> - 9.0.1-1
- Remove dist defines, fedora-release does that now
- Enable post-build buildroot checking by default

* Tue Jun 19 2007 Jeremy Katz <katzj@redhat.com> - 9.0.0-1
- use stock find-lang.sh (#213041)
- arm fixes (Lennert Buytenhek, #243523)
- allow jar repacking to be disabled (#219731)
- fix running dist.sh --fc (#223651)
- hardlink identical .pyc and .pyo files to save space (Ville Skyttä)
- fix TMPDIR usage (Matthew Miller, #235614)

* Tue Jun 19 2007 Jeremy Katz <katzj@redhat.com> - 8.1.0-1
- add modalias tags to kmod packages and other kmod changes (jcm)
- recompress jars to avoid multilib conflicts (bkonrath)

* Fri May 18 2007 Jesse Keating <jkeating@redhat.com> 8.0.45-16
- Update macros for F8
- hardcode dist in release string, as we provide it.  chicken/egg.

* Wed Apr 11 2007 Jon Masters <jcm@redhat.com> 8.0.45-15
- Add modalias tags to kernel module packages (kmods) for tracking.
- Further information is available at http://www.kerneldrivers.org/.

* Tue Apr 03 2007 Jon Masters <jcm@redhat.com> 8.0.45-14
- Rebased all previous patches (since java fix introduced offset).
- Added Fedora per-release macros to platforms section of macros.
  Further debate may see these move elsewhere in the ordering.

* Tue Mar 13 2007 Ben Konrath <bkonrath@redhat.com> 8.0.45-13
- Update brp-java-repack-jars to fix issue with tomcat.

* Wed Oct 18 2006 Jon Masters <jcm@redhat.com> 8.0.45-12
- Synced kernel_module_package semantics with SuSE.
- Updated kmodtool.

* Tue Oct 17 2006 Jon Masters <jcm@redhat.com> 8.0.45-10
- Updated kernel_module_package.

* Mon Oct 16 2006 Jon Masters <jcm@redhat.com> 8.0.45-9
- Added kernel_module_package macro. Working on unified packaging.

* Thu Oct 12 2006 Jon Masters <jcm@redhat.com> 8.0.45-8
- Added patch for find-requires. Waiting on write access to public CVS.

* Tue Sep 12 2006 Deepak Bhole <dbhole@redhat.com> 8.0.45-6
- Fix brp-java-repack-jars to work with builddirs that aren't %%name-%%version

* Mon Sep 11 2006 Fernando Nasser <fnasser@redhat.com> - 8.0.45-5
- Fix order of tokens in find command (thanks mikeb@redhat.com)

* Thu Sep  7 2006 Ben Konrath <bkonrath@redhat.com> - 8.0.45-4
- Fix bug in repack jars script.

* Wed Sep  6 2006 Jeremy Katz <katzj@redhat.com> - 8.0.45-3
- path fix

* Tue Sep  5 2006 Jeremy Katz <katzj@redhat.com> - 8.0.45-2
- Add script from Ben Konrath <bkonrath@redhat.com> to repack jars to
  avoid multilib conflicts

* Sun Jul 30 2006 Jon Masters <jcm@redhat.com> - 8.0.45-1
- Fix inverted kernel test.

* Sun Jul 30 2006 Jon Masters <jcm@redhat.com> - 8.0.44-1
- Add a better check for a kernel vs. kmod.

* Thu Jun 15 2006 Jon Masters <jcm@redhat.com> - 8.0.43-1
- Workaround bug in find-requires/find-provides for kmods.

* Thu Jun 15 2006 Jon Masters <jcm@redhat.com> - 8.0.42-1
- Fix a typo in KMP find-requires.

* Tue Jun 13 2006 Jon Masters <jcm@redhat.com> - 8.0.41-1
- Add support for KMP Fedora Extras packaging.

* Fri Feb  3 2006 Jeremy Katz <katzj@redhat.com> - 8.0.40-1
- use -mtune=generic for x86 and x86_64

* Tue Aug 16 2005 Elliot Lee <sopwith@redhat.com> - 8.0.39-1
- Fix #165416

* Mon Aug 01 2005 Elliot Lee <sopwith@redhat.com> - 8.0.38-1
- Add -Wall into cflags

* Mon Aug 01 2005 Elliot Lee <sopwith@redhat.com> - 8.0.37-1
- Patch from Uli: enable stack protector, fix sparc & ppc cflags

* Thu Jun 16 2005 Elliot Lee <sopwith@redhat.com> - 8.0.36-1
- Fix the fix

* Wed Apr  6 2005 Elliot Lee <sopwith@redhat.com> - 8.0.35-1
- Fix #129025 (enable python byte compilation)

* Wed Mar 23 2005 Elliot Lee <sopwith@redhat.com> 8.0.34-1
- Bug fixes
- Cflags change by drepper

* Wed Feb 9 2005 Elliot Lee <sopwith@redhat.com> 8.0.33-1
- Change -D to -Wp,-D to make java happy
- Add -D_FORTIFY_SOURCE=2 to global cflags (as per Jakub & Arjan's request)

* Fri Oct  1 2004 Bill Nottingham <notting@redhat.com> 8.0.32-1
- allow all symbol versioning in find_requires - matches RPM internal
  behavior

* Mon Jun 28 2004 Elliot Lee <sopwith@redhat.com> 8.0.31-1
- Add ppc8[25]60 to rpmrc optflags

* Fri Jun 25 2004 Elliot Lee <sopwith@redhat.com> 8.0.29-1
- rpmrc patch from jakub to change optflags.

* Wed Sep 17 2003 Elliot Lee <sopwith@redhat.com> 8.0.28-1
- Change brp-compress to pass -n flag to gzip (per msw's request)

* Tue Jul 15 2003 Elliot Lee <sopwith@redhat.com> 8.0.27-1
- Fix broken configure macro find for config.guess/config.sub
- Put host/target/build back for now

* Mon Jul  7 2003 Jens Petersen <petersen@redhat.com> - 8.0.26-1
- preserve the vendor field when VENDOR not set
- put VENDOR in the final i386-libc line, not the tentative one

* Mon Jul  7 2003 Jens Petersen <petersen@redhat.com> - 8.0.25-1
- update config.{guess,sub} to 2003-06-17
- define VENDOR to be redhat only when /etc/redhat-release present
  [suggested by jbj]
- put VENDOR in vendor field in our config.guess file for
  ia64, ppc, ppc64, s390, s390x, x86_64 and elf32-i386 Linux
- drop the --host, --build, --target and --program-prefix configure options
  from %%configure, since this causes far too many problems

* Fri May  2 2003 Jens Petersen <petersen@redhat.com> - 8.0.24-3
- make config.{guess,sub} executable

* Thu May  1 2003 Jens Petersen <petersen@redhat.com> - 8.0.22-2
- add config.guess and config.sub (2003-02-22) with s390 patch on config.sub
- make %%configure use them

* Mon Mar 03 2003 Elliot Lee <sopwith@redhat.com>
- Unset $DISPLAY in macros

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com> 8.0.21-1
- Just turn on -g unconditionally for now

* Thu Feb 13 2003 Elliot Lee <sopwith@redhat.com> 8.0.20-1
- Reorganize rpmrc/macros to set cflags in a nicer manner.

* Wed Jan 22 2003 Elliot Lee <sopwith@redhat.com> 8.0.19-1
- Disable brp-implant-ident-static until it works everywhere

* Thu Jan 16 2003 Nalin Dahyabhai <nalin@redhat.com> 8.0.18-1
- add brp-implant-ident-static, which requires mktemp

* Thu Jan  9 2003 Bill Nottingham <notting@redhat.com> 8.0.17-1
- add brp-strip-static-archive from rpm-4.2-0.54

* Tue Dec 17 2002 Bill Nottingham <notting@redhat.com> 8.0.16-1
- make -g in rpmrc conditional on debug_package

* Mon Dec 16 2002 Elliot Lee <sopwith@redhat.com> 8.0.15-1
- Rename -debug subpackages to -debuginfo

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 8.0.14-1
- tweak debug package stuff so that we are overloading %%install
  instead of %%post

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 8.0.13-1
- turn on internal rpm dep generation by default

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 8.0.12-1
- New release with debug packages on

* Tue Dec  3 2002 Bill Nottingham <notting@redhat.com> 8.0.8-1
- turn debug packages off
- override optflags with no -g

* Fri Nov 22 2002 Elliot Lee <sopwith@redhat.com> 8.0.7-1
- turn on debug packages

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 8.0.6-1
- Pass __strip and __objdump macros

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 8.0.5-1
- Update macros to specify find-provides/find-requires

* Thu Oct 31 2002 Elliot Lee <sopwith@redhat.com> 8.0.4-1
- Remove tracking dependency

* Wed Oct 16 2002 Phil Knirsch <pknirsch@redhat.com> 8.0.3-2
- Added fix for outdated config.[sub|guess] files in %%configure section

* Wed Oct 16 2002 Elliot Lee <sopwith@redhat.com> 8.0.3-1
- New release that blows up on unpackaged files and missing doc files.

* Thu Oct  3 2002 Jeremy Katz <katzj@redhat.com> 8.0.2
- don't redefine everything in macros, just what we need to

* Mon Sep 16 2002 Alexander Larsson <alexl@redhat.com> 8.0.1
- Add debug package support to %%__spec_install_post

* Tue Sep  3 2002 Bill Nottingham <notting@redhat.com> 8.0-1
- bump version

* Wed Aug 28 2002 Elliot Lee <sopwith@redhat.com> 7.3.94-1
- Update macrofiles

* Wed Jul 31 2002 Elliot Lee <sopwith@redhat.com> 7.3.93-1
- Add _unpackaged_files_terminate_build and
_missing_doc_files_terminate_build to macros

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-6
- find-lang.sh fix from 67368
- find-requires fix from 67325

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-5
- Add /etc/rpm/macros back to make #67951 go away

* Wed Jun 26 2002 Jens Petersen <petersen@redhat.com> 7.3.92-4
- fix %%configure targeting for autoconf-2.5x (#58468)
- include ~/.rpmmacros in macrofiles file path again

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 7.3.92-3
- automated rebuild

* Fri Jun 21 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-2
- Don't define _arch

* Thu Jun 20 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-1
- find-lang error detection from Havoc

* Wed Jun 12 2002 Elliot Lee <sopwith@redhat.com> 7.3.91-1
- Update

* Sun Jun  9 2002 Jeff Johnson <jbj@redhat.com>
- create.
