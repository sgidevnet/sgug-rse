%if 0%{?fedora}
%global xapian_core_support ON
%else
%global xapian_core_support OFF
%endif

Summary: A documentation system for C/C++
Name:    doxygen
Epoch:   1
Version: 1.8.15
Release: 10%{?dist}

# No version is specified.
License: GPL+
Url: http://www.doxygen.nl
Source0: http://doxygen.nl/files/%{name}-%{version}.src.tar.gz
# this icon is part of kdesdk
Source1: doxywizard.png
Source2: doxywizard.desktop

# upstream patches
Patch0: doxygen-1.8.15-handle_empty_TOC_in_XML_output.patch
Patch1: doxygen-1.8.15-test_for_XML_output_with_an_empty_TOC.patch
Patch2: doxygen-1.8.15-inconsistent_whitespace_removal_for_operators.patch
Patch3: doxygen-1.8.15-crash.patch
Patch4: doxygen-1.8.15-multilib.patch
Patch5: https://github.com/doxygen/doxygen/pull/6893.patch

BuildRequires: %{_bindir}/python3

BuildRequires: gcc-c++ gcc
BuildRequires: perl-interpreter
%if ! 0%{?_module_build}
BuildRequires: tex(dvips)
BuildRequires: tex(latex)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(sectsty.sty)
BuildRequires: tex(tocloft.sty)
BuildRequires: tex(xtab.sty)
BuildRequires: tex(import.sty)
BuildRequires: tex(tabu.sty)
BuildRequires: tex(appendix.sty)
BuildRequires: tex(adjustbox.sty)
BuildRequires: /usr/bin/epstopdf
BuildRequires: texlive-epstopdf
BuildRequires: ghostscript
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: graphviz
%else
BuildRequires: zlib-devel
%endif
BuildRequires: flex
BuildRequires: bison
BuildRequires: cmake
%if %{xapian_core_support} == "ON"
BuildRequires: xapian-core-devel
BuildRequires: zlib-devel
%endif
Requires: perl-interpreter
Requires: graphviz

%description
Doxygen can generate an online class browser (in HTML) and/or a
reference manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen can
also be configured to extract the code structure from undocumented
source files.

%if ! 0%{?_module_build}
%package doxywizard
Summary: A GUI for creating and editing configuration files
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildRequires: qt5-qtbase-devel

%description doxywizard
Doxywizard is a GUI for creating and editing configuration files that
are used by doxygen.

%package latex
Summary: Support for producing latex/pdf output from doxygen
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: tex(latex)
%if 0%{?fedora} > 17 || 0%{?rhel} > 6
Requires: tex(multirow.sty)
Requires: tex(sectsty.sty)
Requires: tex(tocloft.sty)
Requires: tex(xtab.sty)
Requires: tex(import.sty)
Requires: tex(tabu.sty)
Requires: tex(appendix.sty)
Requires: tex(newunicodechar.sty)
Requires: texlive-epstopdf-bin
%endif

%description latex
%{summary}.
%endif


%prep
%autosetup -p1

# convert into utf-8
#iconv --from=ISO-8859-1 --to=UTF-8 LANGUAGE.HOWTO > LANGUAGE.HOWTO.new
#touch -r LANGUAGE.HOWTO LANGUAGE.HOWTO.new
#mv LANGUAGE.HOWTO.new LANGUAGE.HOWTO


%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LDFLAGS="$LDFLAGS -ldicl-0.1 -liconv"

mkdir -p %{_target_platform}
_dir=$PWD
cd %{_target_platform}
%if ! 0%{?_module_build}
%cmake \
      -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
      -Dbuild_doc=OFF \
      -Dbuild_wizard=ON \
      -Dbuild_xmlparser=ON \
      -Dbuild_search=%{xapian_core_support} \
      -DMAN_INSTALL_DIR=%{_mandir}/man1 \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DBUILD_SHARED_LIBS=OFF \
      ..
%else
%cmake \
      -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
      -Dbuild_doc=OFF \
      -Dbuild_wizard=OFF \
      -Dbuild_xmlparser=ON \
      -Dbuild_search=OFF \
      -DMAN_INSTALL_DIR=%{_mandir}/man1 \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DBUILD_SHARED_LIBS=OFF \
      -DSOURCE_DIR="${_dir}" \
      -DBUILD_DIR="${_dir}/build" \
      ..
%endif
cd $_dir

make %{?_smp_mflags} -C %{_target_platform}

%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

install -m644 -p -D %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/doxywizard.png

# install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
cp doc/*.1 %{buildroot}/%{_mandir}/man1/
%if 0%{?_module_build}
rm -f %{buildroot}/%{_mandir}/man1/doxywizard.1*
%endif

%if %{xapian_core_support} == "OFF"
rm -f %{buildroot}/%{_mandir}/man1/doxyindexer.1* %{buildroot}/%{_mandir}/man1/doxysearch.1*
%endif

# remove duplicate
rm -rf %{buildroot}/%{_docdir}/packages

%if ! 0%{?_module_build}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
%endif

%check
make tests -C %{_target_platform}

%files
%doc LANGUAGE.HOWTO README.md
%license LICENSE
%if ! 0%{?_module_build}
%if %{xapian_core_support} == "ON"
%{_bindir}/doxyindexer
%{_bindir}/doxysearch*
%endif
%endif
%{_bindir}/doxygen
%{_mandir}/man1/doxygen.1*
%if %{xapian_core_support} == "ON"
%{_mandir}/man1/doxyindexer.1*
%{_mandir}/man1/doxysearch.1*
%endif
%if ! 0%{?_module_build}
%files doxywizard
%{_bindir}/doxywizard
%{_mandir}/man1/doxywizard*
%{_datadir}/applications/doxywizard.desktop
%endif
%{_datadir}/pixmaps/doxywizard.png

%if ! 0%{?_module_build}
%files latex
# intentionally left blank
%endif

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Christoph Junghans <junghans@votca.org> - 1:1.8.15-9
- Incl. xml fix for c++11

* Sat Mar 16 2019 Than Ngo <than@redhat.com> - 1:1.8.15-8
- added license file

* Wed Mar 13 2019 Than Ngo <than@redhat.com> - 1:1.8.15-7
- added Requirement on dot

* Thu Feb 14 2019 Than Ngo <than@redhat.com> - 1:1.8.15-6
- fixed bz#1677000, fixed multilib issue

* Tue Feb 12 2019 Than Ngo <than@redhat.com> - 1:1.8.15-5
- fixed bz#1675288, doxygen 1.8.15 segfault

* Fri Feb 08 2019 Than Ngo <than@redhat.com> - 1:1.8.15-4
- fixed bz#673228 - operator whitespace changes cause wxpython FTBFS
- fixed bz#1673230 - BR on tex(newunicodechar.sty) in doxygen-latex 

* Tue Feb 05 2019 Than Ngo <than@redhat.com> - 1:1.8.15-3
- fixed bz#1671999, backported from upstream
- added test for XML output with an empty TOC

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Than Ngo <than@redhat.com> - 1:1.8.15-1
- update to 1.8.15

* Thu Dec 06 2018 Than Ngo <than@redhat.com> - 1:1.8.14-8
- enable testing 

* Mon Jul 23 2018 Than Ngo <than@redhat.com> - 1:1.8.14-7
- add BR: gcc-c++ gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Than Ngo <than@redhat.com> - 1:1.8.14-5
- support Qt5

* Wed Jun 20 2018 Than Ngo <than@redhat.com> - 1.8.14-4
- enble search addon on fedora

* Mon Apr 30 2018 Than Ngo <than@redhat.com> - 1.8.14-3
- added missing BR on adjustbox.sty for refman

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Than Ngo <than@redhat.com> - 1:1.8.14-1
- update to 1.8.14

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1:1.8.13-10
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Tue Jul 04 2017 Than Ngo <than@redhat.com> - 1:1.8.13-9
- backport to fix C# property initializer parsing 
- backport to fix non reachable links and redirected links in documentation

* Tue May 30 2017 Than Ngo <than@redhat.com> - 1:1.8.13-8
- backport to fix problem where automatic line breaking caused
  missing vertical bars in the parameter table for Latex output

* Sat Apr 22 2017 Karsten Hopp <karsten@redhat.com> - 1.8.13-7
- fix _module_build macro

* Fri Apr 21 2017 Karsten Hopp <karsten@redhat.com> - 1.8.13-6
- use new _module_build macro to limit dependencies for Modularity

* Mon Mar 13 2017 Than Ngo <than@redhat.com> - 1:1.8.13-5
- backport to fix behavior of @ref const matching (#776988)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Than Ngo <than@redhat.com> - 1:1.8.13-3
- Bug 775493 - Usage of underscore's in parameter names

* Tue Jan 17 2017 Björn Esser <besser82@fedoraproject.org> - 1:1.8.13-2
- Add upstream patch to fix regression (rhbz#1413296)

* Thu Dec 29 2016 Orion Poplawski <orion@cora.nwra.com> - 1:1.8.13-1
- Update to 1.8.13
- Drop upstream patches

* Thu Dec 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1:1.8.12-7
- Rebuild for xapian soname bump
- Add patch to build with python rc

* Mon Dec 12 2016 Than Ngo <than@redhat.com> - 1:1.8.12-6
- backport upstream patch to fix
    Bug 707266 - C++/CLI indexed property not documented
    Bug 774949 - Unknown reference in manual
    Bug 775245 - referencing Python files via tagfile broken

* Thu Dec 08 2016 Than Ngo <than@redhat.com> - 1:1.8.12-5
- fixed bz#1402043 - runtime dependency on perl
- backport upstream patch to fix Bug 774138 . add HTML classes to "Definition at..." & "Referenced by..." for CSS

* Fri Nov 25 2016 Than Ngo <than@redhat.com> - - 1:1.8.12-4
- Bug 774273 - INLINE_SIMPLE_STRUCTS with enums in classes does not work

* Tue Nov 15 2016 Than Ngo <than@redhat.com> - 1:1.8.12-3
- bz#1394456, add missing docs
- fix build issue when build_doc=ON

* Thu Oct 20 2016 Than Ngo <than@redhat.com> - 1:1.8.12-2
- backport upstream fixes
  Bug 771310 - French description for "Namespace Members" is wrong and causes fatal javascript error
  Bug 771344 - Class name 'internal' breaks class hierarchy in C++

* Tue Sep 06 2016 Than Ngo <than@redhat.com> - 1:1.8.12-1
- 1.8.12
- fixed bz#1373167 - doxygen ships bogus man pages 

* Sun Mar 06 2016 Than Ngo <than@redhat.com> - 1:1.8.11-4
- bz#1305739, Unescaped percent sign in doxygen

* Mon Feb 22 2016 Than Ngo <than@redhat.com> - 1:1.8.11-3
- fix bz#1305739, Unescaped percent sign in doxygen

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Than Ngo <than@redhat.com> - 1:1.8.11-1
- 1.8.11

* Fri Dec 04 2015 Than Ngo <than@redhat.com> - 1:1.8.10-7
- backport to fix a couple of small memory leaks

* Tue Nov 10 2015 Than Ngo <than@redhat.com> - 1:1.8.10-6
- backport patches to fix follow issues:
   angle brackets (< and >) not escaped in HTML formula alt text
   don't support longer key in bibtex
   math does not work in LaTeX with custom header and footer
   writeMemberNavIndex template calls static fixSpaces
   XML empty <argsstring/> in python
   XML not documenting a class in python
   add option to build latex without timestamps

* Mon Nov 09 2015 Than Ngo <than@redhat.com> - 1:1.8.10-5
- fix install issue

* Thu Oct 08 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1:1.8.10-4
- Fix patch to apply

* Thu Oct 08 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1:1.8.10-3
- drop QT_ARCH_X86_64 hardcoded definition to get doxygen built on aarch64
  (it built by pure luck on other architectures)

* Wed Sep 23 2015 Than Ngo <than@redhat.com> - 1.8.10-2
- fix broken deps

* Fri Aug 28 2015 Than Ngo <than@redhat.com> - 1.8.10-1
- update to 1.8.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Than Ngo <than@redhat.com> - 1:1.8.9.1-3
- rebuild

* Wed Apr 29 2015 Than Ngo <than@redhat.com> - 1:1.8.9.1-2
- Resolves: bz#1198355, doxygen generates \backmatter in article class

* Wed Jan 21 2015 Than Ngo <than@redhat.com> 1:1.8.9.1-1
- update to 1.8.9.1

* Mon Aug 25 2014 Than Ngo <than@redhat.com> - 1:1.8.8-1
- 1.8.8

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Than Ngo <than@redhat.com> - 1:1.8.7-1
- 1.8.7

* Thu Dec 26 2013 Orion Poplawski <orion@cora.nwra.com> - 1:1.8.6-1
- 1.8.6

* Tue Oct 08 2013 Than Ngo <than@redhat.com> - 1:1.8.5-2
- add exlive-epstopdf-bin in requirement

* Mon Aug 26 2013 Than Ngo <than@redhat.com> - 1:1.8.5-1
- 1.8.5

* Sat Aug 03 2013 Robert Scheck <robert@fedoraproject.org> - 1:1.8.4-4
- Work around strange dependencies in epstopdf packages (#991699)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Than Ngo <than@redhat.com> - 1:1.8.4-2
- backport upstream patch to fix endless loop

* Tue May 21 2013 Than Ngo <than@redhat.com> - 1:1.8.4-1
- 1.8.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Than Ngo <than@redhat.com> - 1.8.3.1-1
- 1.8.3.1
- fedora/rhel condition

* Tue Jan 08 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:1.8.3-3
- -latex subpkg (#892288)
- .spec cleanup

* Thu Jan 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:1.8.3-2
- doxygen is missing dependencies for texlive update (#891452)
- doxywizard: tighten dep on main pkg

* Wed Jan 02 2013 Than Ngo <than@redhat.com> - 1:1.8.3-1
- 1.8.3

* Mon Aug 13 2012 Than Ngo <than@redhat.com> - 1:1.8.2-1
- 1.8.2

* Mon Jul 30 2012 Than Ngo <than@redhat.com> - 1:1.8.1.2-1
- 1.8.1.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Than Ngo <than@redhat.com> - 1:1.8.1.1-3
- bz#832525, fix multilib issue

* Wed Jun 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1:1.8.1.1-2
- make HTML_TIMESTAMP default FALSE

* Mon Jun 11 2012 Than Ngo <than@redhat.com> - 1:1.8.1.1-1
- 1.8.1.1

* Wed Jun 06 2012 Than Ngo <than@redhat.com> - 1:1.8.1-1
- 1.8.1

* Mon Feb 27 2012 Than Ngo <than@redhat.com> - 1:1.8.0-1
- 1.8.0

* Wed Jan 18 2012 Than Ngo <than@redhat.com> - 1:1.7.6.1-2
- bz#772523, add desktop file

* Fri Dec 16 2011 Than Ngo <than@redhat.com> - 1:1.7.6.1-1
- 1.7.6.1

* Tue Dec 06 2011 Than Ngo <than@redhat.com> - 1:1.7.6-1
- 1.7.6

* Tue Nov 08 2011 Than Ngo <than@redhat.com> - 1:1.7.5.1-1
- 1.7.5.1

* Tue Aug 23 2011 Than Ngo <than@redhat.com> - 1:1.7.5-1
- 1.7.5

* Mon Jun 27 2011 Than Ngo <than@redhat.com> - 1:1.7.4-2
- bz#688684, apply patch to fix crash when not generating man format

* Tue Mar 29 2011 Than Ngo <than@redhat.com> - 1.7.4-1
- 1.7.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Than Ngo <than@redhat.com> - 1.7.3-1
- 1.7.3
- bz#661107

* Fri Nov 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.7.2-2
- Wrong Buildrequire to qt-devel (#651064)

* Mon Oct 11 2010 Than Ngo <than@redhat.com> - 1.7.2-1
- 1.7.2

* Wed Sep 08 2010 Than Ngo <than@redhat.com> - 1:1.7.1-2
- bz#629286, apply patch to fix broken thread handling
- bz#627553, #define in included file in different directory not handled properly
- Inherited documentation doesn't work in case of multiple inheritance

* Mon Jul 19 2010 Than Ngo <than@redhat.com> - 1.7.1-1
- 1.7.1

* Fri Feb 12 2010 Than Ngo <than@redhat.com> - 1.6.2-1.svn20100208
- fix #555526, snapshot 1.6.2-20100208

* Mon Jan 04 2010 Than Ngo <than@redhat.com> - 1:1.6.2-1
- 1.6.2

* Fri Dec 18 2009 Than Ngo <than@redhat.com> - 1:1.6.1-4
- drop _default_patch_fuzz

* Fri Dec 18 2009 Than Ngo <than@redhat.com> - 1:1.6.1-3
- bz#225709, merged review

* Fri Dec 11 2009 Than Ngo <than@redhat.com> - 1:1.6.1-2
- bz#225709, merged review 

* Tue Aug 25 2009 Than Ngo <than@redhat.com> - 1.6.1-1
- 1.6.1

* Mon Aug 24 2009 Than Ngo <than@redhat.com> - 1.6.0-2
- fix #516339, allow to enable/disable timstamp to avoid the multilib issue
  HTMP_TIMESTAMP is disable by default

* Fri Aug 21 2009 Than Ngo <than@redhat.com> - 1.6.0-1
- 1.6.0

* Mon Aug 10 2009 Ville Skyttä <ville.skytta at iki.fi> - 1:1.5.9-3
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Than Ngo <than@redhat.com> - 1.5.9-1
- 1.5.9

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Than Ngo <than@redhat.com> 1.5.8-1
- 1.5.8

* Mon Oct 06 2008 Than Ngo <than@redhat.com> 1.5.7.1-1
- 1.5.7.1

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5.6-3
- fix license tag

* Wed May 21 2008 Than Ngo <than@redhat.com> 1.5.6-2
- rebuild

* Mon May 19 2008 Than Ngo <than@redhat.com> 1.5.6-1
- 1.5.6

* Fri Mar 14 2008 Than Ngo <than@redhat.com> 1.5.5-3
- apply patch to not break partial include paths, thanks to Tim Niemueller

* Wed Feb 20 2008 Than Ngo <than@redhat.com> 1.5.5-2
- apply patch to make doxygen using system libpng/zlib

* Fri Feb 15 2008 Than Ngo <than@redhat.com> 1.5.5-1
- 1.5.5

* Wed Nov 28 2007 Than Ngo <than@redhat.com> 1.5.4-1
- 1.5.4

* Fri Aug 10 2007 Than Ngo <than@redhat.com> - 1:1.5.3-1
- 1.5.3

* Thu Apr 12 2007 Than Ngo <than@redhat.com> - 1:1.5.2-1
- 1.5.2

* Fri Nov 03 2006 Than Ngo <than@redhat.com> 1:1.5.1-2
- 1.5.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.4.7-1.1
- rebuild

* Mon Jun 12 2006 Than Ngo <than@redhat.com> 1:1.4.7-1
- update to 1.4.7

* Thu Jun 08 2006 Than Ngo <than@redhat.com> 1:1.4.6-5
- fix build problem in mock #193358 

* Fri May 12 2006 Than Ngo <than@redhat.com> 1:1.4.6-4
- apply patch to fix Doxygen crash on empty file #191392 
- html docs #187177 

* Wed Mar 08 2006 Than Ngo <than@redhat.com> 1:1.4.6-3
- fix typo bug #184400

* Mon Mar 06 2006 Than Ngo <than@redhat.com> 1:1.4.6-2
- fix build problem #184042

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:1.4.6-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:1.4.6-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Than Ngo <than@redhat.com> 1.4.6-1
- 1.4.6

* Mon Dec 19 2005 Than Ngo <than@redhat.com> 1.4.5-3
- apply patch to fix build problem with gcc-4.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 18 2005 Bill Nottingham <notting@redhat.com>
- fix references to /usr/X11R6

* Sat Oct 15 2005 Florian La Roche <laroche@redhat.com>
- 1.4.5

* Mon Sep 19 2005 Than Ngo <than@redhat.com> 1:1.4.4-2
- move doxywizard man page to subpackge doxywizard

* Thu Jul 21 2005 Than Ngo <than@redhat.com> 1:1.4.4-1
- update to 1.4.4

* Tue Jun 14 2005 Than Ngo <than@redhat.com> 1.4.3-1
- 1.4.3

* Thu Mar 31 2005 Than Ngo <than@redhat.com> 1:1.4.2-1
- 1.4.2

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 1:1.4.1-2
- rebuilt against gcc-4

* Wed Jan 19 2005 Than Ngo <than@redhat.com> 1:1.4.1-1
- update to 1.4.1

* Sun Oct 10 2004 Than Ngo <than@redhat.com> 1:1.3.9.1-1
- update to 1.3.9.1

* Wed Oct 06 2004 Than Ngo <than@redhat.com> 1:1.3.9-1
- update to 1.3.9

* Sun Jul 25 2004 Than Ngo <than@redhat.com> 1:1.3.8-1
- update to 1.3.8

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 11 2004 Than Ngo <than@redhat.com> 1.3.7-1
- update to 1.3.7, bug #119340

* Sun Apr 04 2004 Than Ngo <than@redhat.com> 1:1.3.6-2
- fix qt-mt linking problem

* Thu Feb 26 2004 Than Ngo <than@redhat.com> 1:1.3.6-1
- update to 1.3.6
- added more buildrequires, #110752

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Dec 17 2003 Than Ngo <than@redhat.com> 1:1.3.5-1
- 1.3.5 release

* Fri Sep 26 2003 Harald Hoyer <harald@redhat.de> 1:1.3.4-1
- update to 1.3.4
- doxsearch was removed

* Tue Sep 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- allow compiling without qt/doxywizard

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Tue May  6 2003 Than Ngo <than@redhat.com> 1.3-1
- 1.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 27 2002 Than Ngo <than@redhat.com> 1.2.18-2
- use gnu install

* Sat Nov  9 2002 Than Ngo <than@redhat.com> 1.2.18-1.2
- fix some build problem

* Tue Oct 15 2002 Than Ngo <than@redhat.com> 1.2.18-1
- 1.2.18

* Wed Aug 28 2002 Than Ngo <than@redhat.com> 1.2.17-1
- 1.2.17 fixes many major bugs

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com>
- rebuilt with gcc-3.2 (we hope)

* Mon Jul 22 2002 Tim Powers <timp@redhat.com>
- rebuild using gcc-3.2-0.1

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr 16 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.13-5
- rebuild against qt 3.0.3-10

* Fri Mar  8 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.13-4
- rebuild against qt 3.0.2

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 1.2.14-2
- rebuild against qt 2.3.2

* Tue Feb 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.14-1
- 1.2.14

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jan 06 2002 Than Ngo <than@redhat.com> 1.2.13.1-1
- update to 1.2.13.1
- fixed build doxywizard with qt3

* Sun Dec 30 2001 Jeff Johnson <jbj@redhat.com> 1.2.13-1
- update to 1.2.13

* Sun Nov 18 2001 Than Ngo <than@redhat.com> 1.2.12-1
- update to 1.2.12
- s/Copyright/License

* Wed Sep 12 2001 Tim Powers <timp@redhat.com>
- rebuild with new gcc and binutils

* Wed Jun 13 2001 Than Ngo <than@redhat.com>
- update tp 1.2.8.1
- make doxywizard as separat package
- fix to use install as default

* Tue Jun 05 2001 Than Ngo <than@redhat.com>
- update to 1.2.8

* Tue May 01 2001 Than Ngo <than@redhat.com>
- update to 1.2.7
- clean up specfile
- patch to use RPM_OPT_FLAG

* Wed Mar 14 2001 Jeff Johnson <jbj@redhat.com>
- update to 1.2.6

* Wed Feb 28 2001 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Tue Dec 26 2000 Than Ngo <than@redhat.com>
- update to 1.2.4
- remove excludearch ia64
- bzip2 sources

* Mon Dec 11 2000 Than Ngo <than@redhat.com>
- rebuild with the fixed fileutils

* Mon Oct 30 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.2.3.

* Sun Oct  8 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.2.2.
- enable doxywizard.

* Sat Aug 19 2000 Preston Brown <pbrown@redhat.com>
- 1.2.1 is latest stable, so we upgrade before Winston is released.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul  4 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Fri Jun 30 2000 Florian La Roche <laroche@redhat.de>
- fix QTDIR detection

* Fri Jun 09 2000 Preston Brown <pbrown@redhat.com>
- compile on x86 w/o optimization, revert when compiler fixed!!

* Wed Jun 07 2000 Preston Brown <pbrown@redhat.com>
- use newer RPM macros

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- add to distro.

* Tue May  9 2000 Tim Powers <timp@redhat.com>
- rebuilt for 7.0

* Wed Feb  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- recompile with current Qt (2.1.0/1.45)

* Wed Jan  5 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.0.0.
- recompile with qt-2.0.1 if available.
- relocatable package.

* Mon Nov  8 1999 Tim Powers <timp@redhat.com>
-updated to 0.49-991106

* Tue Jul 13 1999 Tim Powers <timp@redhat.com>
- updated source
- cleaned up some stuff in the spec file

* Thu Apr 22 1999 Jeff Johnson <jbj@redhat.com>
- Create Power Tools 6.0 package.
