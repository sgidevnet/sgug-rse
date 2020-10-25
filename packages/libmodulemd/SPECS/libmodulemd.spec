%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

# Python 2 is dead on F31+
#%%if ( 0%%{?fedora} && 0%%{?fedora} <= 30 ) || ( 0%%{?rhel} && 0%%{?rhel} <= 7)
#  %%global meson_python_flags -Dwith_py2=true
#  %%global build_python2 1
#%%else
  %global meson_python_flags -Dwith_py2=false
  %global build_python2 0
#%%endif

%global upstream_name libmodulemd

%if (0%{?rhel} && 0%{?rhel} <= 7)
  %global v2_suffix 2
%endif

Name:           %{upstream_name}%{?v2_suffix}
Version:        2.9.3
Release:        1%{?dist}
Summary:        Module metadata manipulation library

License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
Source0:        %{url}/releases/download/%{upstream_name}-%{version}/modulemd-%{version}.tar.xz

BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
#BuildRequires:  pkgconfig(gtk-doc)
#BuildRequires:  glib2-doc
BuildRequires:  rpm-devel
BuildRequires:  file-devel
%if %{build_python2}
BuildRequires:  python2-devel
BuildRequires:  python-gobject-base
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-gobject-base
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  help2man


# Patches
Patch100:       modulemd.sgifixes.patch


%description
C Library for manipulating module metadata files.
See https://github.com/fedora-modularity/libmodulemd/blob/master/README.md for
more details.


%if %{build_python2}
%package -n python2-%{name}
Summary: Python 2 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python-gobject-base
Requires: python-six

%description -n python2-%{name}
Python 2 bindings for %{name}
%endif


%package -n python%{python3_pkgversion}-%{name}
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python%{python3_pkgversion}-gobject-base

%if (0%{?rhel} && 0%{?rhel} <= 7)
# The py3_dist macro on EPEL 7 doesn't work right at the moment
Requires: python3.6dist(six)
%else
Requires: %{py3_dist six}
%endif

%description -n python%{python3_pkgversion}-%{name}
Python %{python3_pkgversion} bindings for %{name}


%package devel
Summary:        Development files for libmodulemd
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if (0%{?rhel} && 0%{?rhel} <= 7)
Conflicts:      libmodulemd1-devel
Conflicts:      libmodulemd-devel
%endif


%description devel
Development files for libmodulemd.


%prep
%autosetup -p1 -n modulemd-%{version}

# A place to generate the SGUG patch
#exit 1

# Rewrite some hardcoded paths
perl -pi -e "s|/usr/bin/bash|%{_bindir}/bash|g" contrib/release-tools/release.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" modulemd/tests/test-import-headers.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" modulemd/tests/test-version.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" spec_tmpl.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" .make_packit_specfile.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" run_ci_tests.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" .travis/*.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" .travis/*/*.sh
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" .travis/travis-common.inc

perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" modulemd/clang_simple_version.sh

perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" .packit_version.sh
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" contrib/doc-tools/fix-xref.sh

perl -pi -e "s|/usr/bin/sh|%{_bindir}/sh|g" make_rpms.sh.in

perl -pi -e "s|/usr/bin/python|%{_bindir}/bin/python|g" modulemd/tests/*.py
perl -pi -e "s|/usr/bin/python|%{_bindir}/bin/python|g" modulemd/tests/ModulemdTests/*.py

perl -pi -e "s|LD_LIBRARY_PATH|LD_LIBRARYN32_PATH|g" modulemd/meson.build

%build
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCES -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -Wl,-z,relro -Wl,-z,now"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif
export CURWD=`pwd`
export LD_LIBRARYN32_PATH=$CURWD/mips-sgug-irix/modulemd:$LD_LIBRARYN32_PATH
%meson -Ddeveloper_build=false \
       -Dskip_formatters=true \
       -Dwith_docs=false \
       %{meson_python_flags}

%meson_build


%check
export CURWD=`pwd`
export LD_LIBRARYN32_PATH=$CURWD/mips-sgug-irix/modulemd:$LD_LIBRARYN32_PATH
#export LC_CTYPE=C.utf8
export LC_CTYPE=C

%ifarch %{power64} s390x
# Valgrind is broken on ppc64[le] with GCC7:
# https://bugs.kde.org/show_bug.cgi?id=386945
export MMD_SKIP_VALGRIND=1
%endif
%ifnarch %{valgrind_arches}
export MMD_SKIP_VALGRIND=1
%endif

# Don't run tests on ARM for now. There are problems with
# performance on the builders and often these time out.
%ifnarch %{arm} aarch64
# The tests sometimes time out in CI, so give them a little extra time
%{__meson} test -C %{_vpath_builddir} %{?_smp_mesonflags} --print-errorlogs -t 5
%endif


%install
%meson_install

%if ( 0%{?rhel} && 0%{?rhel} <= 7)
# Don't conflict with modulemd-validator from 1.x included in the official
# RHEL 7 repos
mv %{buildroot}%{_bindir}/modulemd-validator \
   %{buildroot}%{_bindir}/modulemd-validator%{?v2_suffix}

mv %{buildroot}%{_mandir}/man1/modulemd-validator.1 \
   %{buildroot}%{_mandir}/man1/modulemd-validator%{?v2_suffix}.1
%endif


#%%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_bindir}/modulemd-validator%{?v2_suffix}
%{_mandir}/man1/modulemd-validator%{?v2_suffix}.1*
%{_libdir}/%{upstream_name}.so.2*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Modulemd-2.0.typelib


%files devel
%{_libdir}/%{upstream_name}.so
%{_libdir}/pkgconfig/modulemd-2.0.pc
%{_includedir}/modulemd-2.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Modulemd-2.0.gir
#%%dir %%{_datadir}/gtk-doc
#%%dir %%{_datadir}/gtk-doc/html
#%%{_datadir}/gtk-doc/html/modulemd-2.0/


%if %{build_python2}
%files -n python2-%{name}
%{python2_sitearch}/gi/overrides/
%endif


%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/gi/overrides/


%changelog
* Wed Apr 08 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.3-1
- new upstream release: 2.9.3

* Wed Apr 01 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.2-4
- Skip rpmdeplint from gating due to https://github.com/fedora-infra/bodhi/issues/3944

* Wed Apr 01 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.2-3
- Fix build against Python 3.9
- Resolves: rhbz#1817665

* Wed Mar 11 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.2-2
- new upstream release: 2.9.2

* Wed Mar 11 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.2-0.20200311.1gitg31bbd4e
- new upstream release: 2.9.2

* Wed Mar 11 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.2-0.20200311.1gitg31bbd4e
- new upstream release: 2.9.2

* Fri Feb 14 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.1-1
- new upstream release: 2.9.1

* Wed Feb 12 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.9.0-1
- new upstream release: 2.9.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.8.3-1
- Update to 2.8.3
- Fix compilation issue with glib >= 2.63.3
- Improved modulemd document validation
- Numerous test enhancements

* Thu Oct 24 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.8.2-1
- Update to 2.8.2
- Use safer version of dup()
- Fix loading of YAML module stream with no module or stream name

* Tue Oct 15 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.8.1-1
- Improve the merge logic to handle third-party repos more sanely

* Wed Sep 18 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.8.0-2
- Improvements to ModuleIndex.update_from_defaults_directory()
  * Import each file in the directory as a merge rather than an overwrite so
    we can detect conflicts.
  * Modify the meaning of the 'strict' argument to fail if the merge would
    result in a conflict in the default stream setting of a module.

* Wed Sep 04 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.8.0-1
- Update to 2.8.0
- API Changes
  * Add Modulemd.Module.get_translation() - Retrieve the translations
    associated with a Modulemd.Module
  * Add ModuleIndex.update_from_defaults_directory() - Import defaults from a
    directory of yaml documents, such as fedora-module-defaults, optionally
    providing a second path containing overrides.
- Enhancements
  * Modulemd.ModuleIndex.update_from_file() now supports reading files
    compressed with gzip, bzip2 or xz. (Issue: #208)
  * Documentation updates
- Bugfixes
  * Assorted minor issues discovered by static analysis tools.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.7.0-1
- Update to 2.7.0
- Drop libmodulemd1 subpackage which is now packaged separately
- Add support for 'buildroot' and 'srpm-buildroot' arguments to components

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.6.0-1
- Update to 2.6.0
- New function ModuleIndexMerger.resolve_ext() allowing for strict merging
- Profile.get_description() now properly returns available translations
- Numerous documentation fixes
- Test improvements

* Wed May 29 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.5.0-2
- Fix memory issue with Module.search_streams() in the python bindings

* Wed May 22 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.5.0-1
- Update to 2.5.0 and 1.8.11
- Ensure that XMD is always emitted in the same order
- Add .clear_*() functions for all .add_*() functions
- Add ModuleStream.equals()
- Add ModuleIndex.get_default_streams()

* Mon May 13 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.4.0-1
- Update to 2.4.0 and 1.8.10
- Add ModuleStreamV2.clear_dependencies() and .remove_dependencies()
- Fix bugs and memory issues with the XMD python bindings
- Assorted documentation enhancements

* Fri May 03 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.3.1-1
- Update to 2.3.1
- Make Modulemd.Component.set_*() functions accept NULL
- Fix segmentation fault in XMD code due to improper memory management
- Fix incompatibility in python2-libmodulemd GObject overrides
- Fix assorted documentation issues

* Mon Apr 22 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.3.0-1
- Add ModuleIndex.update_from_custom()
- Add ModuleIndex.dump_to_custom()
- Add Component.equals()
- Add Module.remove_streams_by_NSVCA()
- Fix bug with emitting lists of scalars in XMD
- Fix bug with deduplication in the ModuleIndexMerger
- Fix serious memory leak

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.2.3-3
- Rebuild with Meson fix for #1699099

* Wed Apr 03 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.2.3-2
- Fix accidental ABI break

* Mon Apr 01 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.2.3-1
- Update to 2.2.3 and 1.8.6
- Fix header issue with ModulemdRpmMapEntry

* Wed Mar 27 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.2.2-2
- Don't run tests on armv7hl/aarch64 since they have timeout problems

* Wed Mar 27 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.2.2-1
- Update to libmodulemd 2.2.2
- Add support for python2 on RHEL and Fedora < 31
- Make python subpackages archful for GObject overrides

* Tue Mar 26 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.2.1-1
- Update to libmodulemd 2.2.1
- Fixes builds on i686
- Fixes an accidental API error

* Tue Mar 26 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.2.0-1
- Update to libmodulemd 2.2.0
- Support for RPM checksums
- Adds a new directive: "buildafter" for specifying build dependencies
- Adds a new directive: "buildonly" to indicate that a component's built
  artifacts should be listed in the "filter" field.
- Deprecate lookup functions by NSVC in favor of NSVCA (including the
  architecture.

* Fri Mar 01 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.1.0-4
- Don't run tests on 32-bit ARM due to performance issues causing timeouts

* Fri Mar 01 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.1.0-3
- Have python3-libmodulemd1 properly Obsolete libmodulemd and
  python3-libmodulemd < 2.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.1.0-1
- Update to libmodulemd 2.1.0 and 1.8.2
- Drop upstreamed patches
- Add new API ModuleStream.depends_on_stream() and
  ModuleStream.build_depends_on_stream() to help support auto-detection of
  when a module stream may need to be rebuilt when its dependencies change.
- Don't fail merges when default streams differ, treat it as "no default for
  this module"
- Fix error message
- Copy modified value when copying Modulemd.Defaults objects
- Fixes discovered by clang and coverity static analysis tools
- Test improvements

* Fri Jan 11 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-3
- Fix ordering issue with dependencies
- Use glib2 suppression file when running valgrind tests

* Fri Jan 11 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-2
- Fix issue reading modified value for defaults from YAML streams

* Thu Dec 13 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-1
- Update to 2.0.0 final
- Assorted fixes for validation
- Add modulemd-validator tool based on v2 code
- Fix a crash when merging defaults

* Tue Dec 11 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-0.beta2
- Update to 2.0.0beta2
- Better validation of stored content during read and write operations
- ModuleIndex now returns FALSE if any subdocument fails
- Fix tests on 32-bit platforms
- Make unknown keys in YAML maps non-fatal for libmodulemd1
- Make unknown keys in YAML maps optionally fatal for libmodulemd 2.x
- Fix RPM version requirements for libmodulemd1

* Mon Dec 10 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-0.beta1
- Update to 2.0.0beta1
- Total rewrite to 2.0 API
- https://sgallagh.fedorapeople.org/docs/libmodulemd/2.0/

* Fri Oct 26 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.7.0-1
- Update to 1.7.0
- Enhance YAML parser for use with `fedmod lint`
- Support running unit tests against installed packages
- Include all NSVCs for ModuleStreams in ImprovedModule

* Tue Sep 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.4-1
- Update to 1.6.4.
- Add Buildopts to the documentation.
- Deduplicate module streams when merging.
- Drop upstreamed patches.

* Thu Sep 06 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.3-2
- Fix generation of module component YAML
- Output NSVC information using decimal version

* Tue Sep 04 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.3-1
- Update to 1.6.3
- Drop upstreamed patch
- Don't return ModuleStream objects from modulemd_module_new_all_from_*_ext()
- Ensure that Component buildorder property is signed
- Work around optimization bug
- Don't crash dumping translation events without summary or desc

* Thu Aug 09 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.2-2
- Fix backwards-incompatible API change
- Resolves: rhbz#1607083

* Tue Aug 07 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.2-1
- Update to 1.6.2
- Make buildorder a signed integer to match modulemd specification

* Mon Jul 23 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.1-2
- Obsolete unsupported pythonX-modulemd packages

* Fri Jul 20 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.1-1
- Update to 1.6.1
- Fix header include ordering
- Suppress empty sections from .dump() ordering

* Wed Jul 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Adds Modulemd.ModuleStream object, deprecating Modulemd.Module
- Adds Modulemd.Translation and Modulemd.TranslationEntry objects
- Adds Modulemd.ImprovedModule object that collects streams, defaults and
  translations together
- Adds new Modulemd.index_from_*() funtions to get a hash table of
  Modulemd.ImprovedModule objects for easier searching
- Moves function documentation to the public headers
- Corrects the license headers to MIT (they were incorrectly listed as MITNFA
  in previous releases)
- Makes the "eol" field optional for Modulemd.ServiceLevel
- Clean up HTML documentation
- Fixes a type error on 32-bit systems

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.2-1
- Update to libdmodulemd 1.5.2
- Don't free uninitialized memory

* Fri Jun 22 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-2
- Fix buildopts property not being initialized

* Tue Jun 19 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-1
- Update to version 1.5.1
- Re-enable build-time tests

* Mon Jun 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-2
- Temporarily disable build-time tests

* Mon Jun 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-1
- Update to version 1.5.0
- Adds support for "intents" in Modulemd.Defaults
- Adds `Modulemd.get_version()`
- Adds support for RPM whitelists in the buildopts
- Adds a new object: Modulemd.Buildopts
- Deprecates Modulemd.Module.get_rpm_buildopts()
- Deprecates Modulemd.Module.set_rpm_buildopts()
- Fixes some missing license blurbs

* Tue May 08 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.4.1-1
- Update to version 1.4.1
- Improve output from modulemd-validator
- Drop upstreamed patches

* Wed Apr 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.4.0-2
- Fix pointer math error
- Fix compilation failure in Fedora build system

* Wed Apr 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.4.0-1
- Update to version 1.4.0
- Adds new API for returning failed YAML subdocuments
- Stop emitting log messages by default (polluting consumer logs)
- Validate RPM artifacts for proper NEVRA format
- Improve the validator tool
- Drop upstreamed patch

* Mon Apr 16 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.3.0-2
- Fix serious error in modulemd-defaults emitter

* Fri Apr 13 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.3.0-1
- Update to version 1.3.0
- New Public Objects:
  * Modulemd.Prioritizer - tool to merge module defaults
- New Public Functions:
  * Modulemd.SimpleSet.is_equal()
  * Modulemd.Defaults.copy()
  * Modulemd.Defaults.merge()

* Wed Apr 04 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.2.0-1
- Update to version 1.2.0
- New Functions:
  * Modulemd.objects_from_file()
  * Modulemd.objects_from_string()
  * Modulemd.dump()
  * Modulemd.dumps()
  * Modulemd.Defaults.new_from_file()
  * Modulemd.Defaults.new_from_string()
- Deprecated Functions:
  * Modulemd.Module.new_all_from_file()
  * Modulemd.Module.new_all_from_file_ext()
  * Modulemd.Module.new_all_from_string()
  * Modulemd.Module.new_all_from_string_ext()
  * Modulemd.Module.dump_all()
  * Modulemd.Module.dumps_all()
- Bugfixes
  * Properly use G_BEGIN_DECLS and G_END_DECLS in headers
  * Assorted fixes for memory ownership in GObject Introspection

* Fri Mar 23 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.3-2
- Fix missing G_END_DECL from public headers

* Mon Mar 19 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.3-1
- Fix numerous memory leaks
- Drop upstreamed patch

* Thu Mar 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.2-1
- Update to version 1.1.2
- Revert backwards-incompatible API change
- Fix version string in pkgconfig file

* Thu Mar 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.1-1
- Update to version 1.1.1
- Make default stream and profiles optional
- Fixes: https://github.com/fedora-modularity/libmodulemd/issues/25
- Fixes: https://github.com/fedora-modularity/libmodulemd/issues/26
- Fixes: https://github.com/fedora-modularity/libmodulemd/issues/27

* Wed Mar 14 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-1
- Update to version 1.1.0
- Adds support for handling modulemd-defaults YAML documents
- Adds peek()/dup() routines to all object properties
- Adds Modulemd.Module.dup_nsvc() to retrieve the canonical form of the unique module identifier.
- Adds support for boolean types in the XMD section
- Revert obsoletion of pythonX-modulemd packages for now

* Tue Mar 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-2
- Obsolete unsupported pythonX-modulemd packages

* Tue Feb 27 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.4-1
- Update to 1.0.4
- Rework version autodetection
- Avoid infinite loop on unparseable YAML

* Sun Feb 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.3-1
- RPM components are properly emitted when no module components exist
- Parser works around late determination of modulemd version

* Fri Feb 16 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.2-1
- Be more strict with certain parser edge-cases
- Replace popt argument processing with glib
- Drop upstreamed patches

* Thu Feb 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-2
- Handle certain unlikely format violations

* Thu Feb 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-1
- Support modulemd v2
- Add tool to do quick validation of modulemd
- Fix memory management
- Warn and ignore unparseable sub-documents in the YAML
- Fix several memory issues detected by Coverity scan

* Tue Feb 06 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.2-1
- Update to libmodulemd 0.2.2
- Fix numerous minor memory leaks
- Fix issues with EOL/SL dates

* Tue Feb 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-3
- Own appropriate directories

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.1-1
- Update to libmodulemd 0.2.1
- Add 'name' property for Profiles

* Thu Oct 05 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.2.0-2
- Add missing BuildRequires for gtk-doc

* Thu Oct 05 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.2.0-1
- Update to libmodulemd 0.2.0
- Adds gtk-doc generated documentation
- (ABI-break) Makes all optional properties accept NULL as a value to clear
  them
- (ABI-break) Modulemd.SimpleSet takes a STRV (char **) instead of a
  GLib.PtrArray
- Fixes a bug where the name was not always set for components
- Adds support for dumping YAML from the introspected API
- Includes add/remove routines for profiles

* Sat Sep 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-5
- Use %%_isa in Requires for main package from devel

* Mon Sep 18 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.1.0-4
- Correct the license to MIT

* Mon Sep 18 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.1.0-3
- Modifications requested during package review

* Fri Sep 15 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.1.0-2
- First public release

