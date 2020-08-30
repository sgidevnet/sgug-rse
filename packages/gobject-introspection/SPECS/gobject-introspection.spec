%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

%global glib2_version 2.58.0

%global __python %{__python3}

Name:           gobject-introspection
Version:        1.62.0
Release:        8%{?dist}
Summary:        Introspection system for GObject-based libraries

License:        GPLv2+, LGPLv2+, MIT
URL:            https://wiki.gnome.org/Projects/GObjectIntrospection
Source0:        https://download.gnome.org/sources/gobject-introspection/1.62/%{name}-%{version}.tar.xz

Patch100:       gobject-introspection.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  cairo-gobject-devel
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel >= %{glib2_version}
#BuildRequires:  gtk-doc
BuildRequires:  libffi-devel
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXft-devel
BuildRequires:  libxml2-devel
#BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-markdown

Requires:       glib2%{?_isa} >= %{glib2_version}

%description
GObject Introspection can scan C header and source files in order to
generate introspection "typelib" files.  It also provides an API to examine
typelib files, useful for creating language bindings among other
things.

%package devel
Summary:        Libraries and headers for gobject-introspection
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Not always, but whatever, it's a tiny dep to pull in
Requires:       libtool
# For g-ir-doctool
Requires:       python3-mako
# This package only works with the Python version it was built with
# https://bugzilla.redhat.com/show_bug.cgi?id=1691064
Requires:       (python(abi) = %{python3_version} if python3)

%description devel
Libraries and headers for gobject-introspection

%prep
%autosetup -p1

# Fix some hardcoded paths
perl -pi -e "s|/usr/share|%{_datadir}|g" giscanner/transformer.py
perl -pi -e "s|/usr/share|%{_datadir}|g" giscanner/utils.py
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" giscanner/dumper.py

%build
export LD_LIBRARYN32_PATH=%{_builddir}/gobject-introspection-1.62.0/mips-sgug-irix/girepository/:$LD_LIBRARYN32_PATH
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++

export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
%if 0%{debug}
export CFLAGS="-g -O0"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif

%meson -Ddoctool=true -Dgtk_doc=false -Dpython=%{__python3}
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/lib*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/gobject-introspection/
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_bindir}/g-ir-*
%{_datadir}/gir-1.0
%{_datadir}/gobject-introspection-1.0/
%{_datadir}/aclocal/introspection.m4
%{_mandir}/man1/*.gz
#%%dir %%{_datadir}/gtk-doc
#%%dir %%{_datadir}/gtk-doc/html
#%%{_datadir}/gtk-doc/html/gi/

%changelog
* Thu Jul 30 2020 Daniel Hams <daniel.hams@gmail.com> - 1.62.0-8
- Be explicit about which compilers to use

* Sat Jun 20 2020 Daniel Hams <daniel.hams@gmail.com> - 1.62.0-7
- Fix some hardcoded paths + reenable deps now we have packaged enough python pieces

* Fri May 1 2020 HAL <hal@null.not> - 1.16.0-6
- some slight changes so it will build on Irix 6.5 and gcc 9.2

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 1.62.0-1
- Update to 1.62.0

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 1.61.2-1
- Update to 1.61.2

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 1.61.1-1
- Update to 1.61.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Miro Hrončok <mhroncok@redhat.com> - 1.60.1-3
- Require the Python version this was built with

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.60.1-2
- Rebuild with Meson fix for #1699099

* Mon Apr 08 2019 Kalev Lember <klember@redhat.com> - 1.60.1-1
- Update to 1.60.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 1.60.0-1
- Update to 1.60.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 1.59.5-1
- Update to 1.59.5

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 1.59.4-1
- Update to 1.59.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.59.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Kalev Lember <klember@redhat.com> - 1.59.3-1
- Update to 1.59.3

* Sat Jan 05 2019 Kalev Lember <klember@redhat.com> - 1.59.2-1
- Update to 1.59.2
- Switch to the meson build system
- Fix gtk-doc directory ownership

* Sun Dec 30 2018 Kalev Lember <klember@redhat.com> - 1.58.3-1
- Update to 1.58.3

* Mon Dec 10 2018 Kalev Lember <klember@redhat.com> - 1.58.2-1
- Update to 1.58.2

* Sat Nov 17 2018 Kalev Lember <klember@redhat.com> - 1.58.1-1
- Update to 1.58.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 1.58.0-2
- Rebuilt against fixed atk (#1626575)

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 1.58.0-1
- Update to 1.58.0

* Sun Aug 12 2018 Kalev Lember <klember@redhat.com> - 1.57.2-1
- Update to 1.57.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.56.1-2
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 1.56.1-1
- Update to 1.56.1

* Tue Mar 13 2018 Kalev Lember <klember@redhat.com> - 1.56.0-1
- Update to 1.56.0

* Sat Mar 03 2018 Kalev Lember <klember@redhat.com> - 1.55.2-1
- Update to 1.55.2
- Drop /usr/bin/env shebang patch as the brp scripts now handle this correctly
- Remove ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.54.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.54.1-5
- Switch to python3
- Cleanup spec

* Sat Feb 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.54.1-4
- Add python2 to configure so shebangs are properly updated by
  brp-mangle-shebangs.

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.54.1-3
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.54.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Oct 06 2017 Kalev Lember <klember@redhat.com> - 1.54.1-1
- Update to 1.54.1

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 1.54.0-1
- Update to 1.54.0

* Tue Sep 05 2017 Kalev Lember <klember@redhat.com> - 1.53.7-1
- Update to 1.53.7

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 1.53.5-1
- Update to 1.53.5

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.53.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.53.4-4
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Florian Müllner <fmuellner@redhat.com> - 1.53.4-3
- Revert a GKeyFile introspection ABI change

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.53.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 1.53.4-1
- Update to 1.53.4

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 1.53.3-1
- Update to 1.53.3

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 1.52.1-1
- Update to 1.52.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 1.52.0-1
- Update to 1.52.0

* Fri Mar 17 2017 Kalev Lember <klember@redhat.com> - 1.51.5-1
- Update to 1.51.5
- Remove lib64 rpaths

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 1.51.3-1
- Update to 1.51.3

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 1.51.2-1
- Update to 1.51.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Kalev Lember <klember@redhat.com> - 1.51.1-1
- Update to 1.51.1

* Tue Sep 20 2016 Florian Müllner <fmuellner@redhat.com> - 1.50.0-1
- Update to 1.50.0

* Tue Sep 13 2016 Florian Müllner <fmuellner@redhat.com> - 1.49.2-1
- Update to 1.49.2

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 1.49.1-2
- Drop old gir-repository obsoletes
- Don't set group tags

* Thu Aug 04 2016 Kalev Lember <klember@redhat.com> - 1.49.1-1
- Update to 1.49.1
- Update source URLs

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 1.48.0-1
- Update to 1.48.0

* Mon Mar 14 2016 Richard Hughes <rhughes@redhat.com> - 1.47.92-1
- Update to 1.47.92

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.47.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Colin Walters <walters@redhat.com> - 1.47.1-2
- Backport revert of upstream patch around setuid apps
  Resolves: #1285991
- Forcibly reautoconf to bypass timestamp issues

* Mon Nov 02 2015 Kalev Lember <klember@redhat.com> - 1.47.1-1
- Update to 1.47.1

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 1.46.0-1
- Update to 1.46.0

* Fri Aug 21 2015 Kalev Lember <klember@redhat.com> - 1.45.4-1
- Update to 1.45.4
- Use make_install macro

* Fri Jul 03 2015 Florian Müllner <fmuellner@redhat.com> - 1.45.3-1
- Update to 1.45.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 1.45.2-1
- Update to 1.45.2
- Set minimum required glib2 version

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 1.44.0-1
- Update to 1.44.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 1.43.92-1
- Update to 1.43.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 1.43.91-1
- Update to 1.43.91
- Use the %%license macro for the COPYING file

* Thu Jan 22 2015 Richard Hughes <rhughes@redhat.com> - 1.43.3-1
- Update to 1.43.3

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 1.42.0-1
- Update to 1.42.0

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 1.41.91-1
- Update to 1.41.91

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.41.4-1
- Update to 1.41.4

* Thu Jun 26 2014 Richard Hughes <rhughes@redhat.com> - 1.41.3-1
- Update to 1.41.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 05 2014 Kalev Lember <kalevlember@gmail.com> - 1.40.0-2
- Tighten -devel deps

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 1.40.0-1
- Update to 1.40.0

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 1.39.90-1
- Update to 1.39.90

* Wed Jan 29 2014 Richard Hughes <rhughes@redhat.com> - 1.39.3-1
- Update to 1.39.3

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 1.39.0-1
- Update to 1.39.0

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 1.38.0-1
- Update to 1.38.0

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 1.37.6-1
- Update to 1.37.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 1.37.4-1
- Update to 1.37.4

* Tue May 28 2013 Colin Walters <walters@verbum.org> - 1.37.1-1
- Update to 1.37.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1.36.0-1
- Update to 1.36.0

* Thu Mar 21 2013 Kalev Lember <kalevlember@gmail.com> - 1.35.9-1
- Update to 1.35.9

* Tue Mar 05 2013 Colin Walters <walters@verbum.org> - 1.35.8-2
- Enable g-ir-doctool
- Resolves: #903782

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 1.35.8-1
- Update to 1.35.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 1.35.4-1
- Update to 1.35.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 1.35.3-1
- Update to 1.35.3

* Tue Nov 20 2012 Richard Hughes <hughsient@gmail.com> - 1.35.2-1
- Update to 1.35.2

* Mon Nov 12 2012 Kalev Lember <kalevlember@gmail.com> - 1.34.2-1
- Update to 1.34.2

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 1.34.1.1-1
- Update to 1.34.1.1

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 1.34.1-1
- Update to 1.34.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 1.34.0-1
- Update to 1.34.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 1.33.14-1
- Update to 1.33.14

* Wed Sep 05 2012 Kalev Lember <kalevlember@gmail.com> - 1.33.10-1
- Update to 1.33.10

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 1.33.9-1
- Update to 1.33.9

* Fri Jul 20 2012 Matthias Clasen <mclasen@redhat.com> - 1.33.4-2
- Fix an unintended api break that broke vpn in gnome-shell

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 1.33.4-1
- Update to 1.33.4

* Wed Jun 27 2012 Richard Hughes <hughsient@gmail.com> - 1.33.3-1
- Update to 1.33.3

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 1.33.2-1
- Update to 1.33.2

* Fri Apr 27 2012 Kalev Lember <kalevlember@gmail.com> - 1.32.1-2
- Move libffi to pkgconfig Requires.private, in order to
  reduce the impact when libffi soname bump lands in rawhide.

* Fri Apr 20 2012 Kalev Lember <kalevlember@gmail.com> - 1.32.1-1
- Update to 1.32.1

* Tue Mar 27 2012 Matthias Clasen <mclasen@redhat.com> 0 1.32.0-1
- Update to 1.32.0

* Wed Mar 21 2012 Matthias Clasen <mclasen@redhat.com> 0 1.31.22-1
- Update to 1.31.22

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> 0 1.31.20-1
- Update to 1.31.20

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> 0 1.31.10-1
- Update to 1.31.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redha.com> - 1.31.6-1
- Update to 1.31.6

* Mon Dec 05 2011 Karsten Hopp <karsten@redhat.com> 1.31.0-2
- add fix for PPC failure, bugzilla 749604

* Wed Nov 16 2011 Colin Walters <walters@verbum.org> - 1.31.0-2
- -devel package requires libtool
  https://bugzilla.redhat.com/show_bug.cgi?id=613466

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 1.31.0-1
- Update to 1.31.0

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 1.30.0-1
- Update to 1.30.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 1.30.0-1
- Update to 1.30.0

* Fri Jun 17 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.29.0-1
- Update to 1.29.0

* Thu Apr 21 2011 John (J5) Palmieri <johnp@redhat.com> - 0.10.8-1
- Update to 0.10.8

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 0.10.7-1
- Update to 0.10.7

* Fri Mar 25 2011 Owen Taylor <otaylor@redhat.com> - 0.10.6-1
- New upstream release to fix missing cairo typelib

* Fri Mar 25 2011 Colin Walters <walters@verbum.org> - 0.10.5-1
- New upstream release, fixes cairo.gir
  Necessary to avoid gnome-shell having a cairo-devel dependency.
- Also add cairo-gobject-devel dependency, since we really want
  the cairo typelib to link to GObject, since anyone using
  introspection has it anyways.

* Thu Mar 10 2011 Colin Walters <walters@verbum.org> - 0.10.4-1
- Update to 0.10.4

* Wed Feb 23 2011 Colin Walters <walters@verbum.org> - 0.10.3-1
- Update to 0.10.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Colin Walters <walters@verbum.org> - 0.10.2-1
- Update to 0.10.2

* Wed Jan 12 2011 Colin Walters <walters@verbum.org> - 0.10.1-1
- Update to 0.10.1

* Mon Jan 10 2011 Owen Taylor <otaylor@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Thu Sep 30 2010 Colin Walters <walters@verbum.org> - 0.9.10-1
- Update to 0.9.10

* Thu Sep 30 2010 Colin Walters <walters@verbum.org> - 0.9.9-1
- Update to 0.9.9

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.9.8-1
- Update to 0.9.8

* Tue Sep 28 2010 Colin Walters <walters@verbum.org> - 0.9.7-1
- Update to 0.9.7

* Tue Sep 21 2010 Owen Taylor <otaylor@redhat.com> - 0.9.6-1
- Update to 0.9.6

* Thu Sep  2 2010 Colin Walters <walters@verbum.org> - 0.9.3-6
- Strip out test libraries; they're gone in upstream git, and
  create a dependency on cairo (which requires libX11, which makes
  server operating system builders freak out).

* Tue Aug  3 2010 Matthias Clasen <mclasen@redhat.com> - 0.9.3-1
- Update to 0.9.3

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.2-5
- Cherrypick patch for python 2.7 compatibility (patch 1; rhbz#617782)

* Wed Jul 14 2010 Colin Walters <walters@verbum.org> - 0.9.2-4
- Backport patch from upstream for better errors

* Mon Jul 12 2010 Colin Walters <walters@verbum.org> - 0.9.2-1
- New upstream (unstable series) release; requires rebuilds

* Tue Jun 29 2010 Colin Walters <walters@verbum.org> - 0.9.0-1.4.20100629gitf0599b0a
- Add gtk-doc to files

* Tue Jun 29 2010 Colin Walters <walters@verbum.org>
- Switch to git snapshot; I forgot to enable gtk-doc in the last
  tarball.

* Tue Jun 29 2010 Colin Walters <walters@verbum.org> - 0.9.0-1
- New upstream development release
- Update to support building git snapshot directly

* Thu Jun 24 2010 Colin Walters <walters@pocket> - 0.6.14-3
- rebuild to pick up new glib changes

* Thu Jun 10 2010 Colin Walters <walters@pocket> - 0.6.14-2
- Obsolete gir-repository{,-devel}

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 0.6.14-1
- Update to 0.6.14

* Mon May 24 2010 Colin Walters <walters@verbum.org> - 0.6.12-1
- Update to latest upstream release 0.6.12

* Thu Mar 25 2010 Colin Walters <walters@verbum.org> - 0.6.9-3
- Move python library back into /usr/lib/gobject-introspection.  I put
  it there upstream for a reason, namely that apps need to avoid
  polluting the global Python site-packages with bits of their internals.
  It's not a public API.
  
  Possibly resolves bug #569885

* Wed Mar 24 2010 Adam Miller <maxamillion@fedoraproject.org> - 0.6.9-2
- Added newly owned files (gobject-introspection-1.0 directory)

* Wed Mar 24 2010 Adam Miller <maxamillion@fedoraproject.org> - 0.6.9-1
- Update to latest upstream release 0.6.9

* Thu Mar 11 2010 Colin Walters <walters@verbum.org> - 0.6.8-0.3.20100311git2cc97351
- rebuilt

* Thu Mar 11 2010 Colin Walters <walters@verbum.org>
- New upstream snapshot
- rm unneeded rm

* Thu Jan 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 0.6.8-0.1.20100128git
- Update to new git snapshot
- Fix Version tag to comply with correct naming use with alphatag

* Fri Jan 15 2010 Adam Miller <maxamillion@fedoraproject.org> - 0.6.7.20100115git-1
- Update to git snapshot for rawhide 

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.6.7-1
- Update to 0.6.7

* Fri Sep 11 2009 Colin Walters <walters@verbum.org> - 0.6.5-1
- New upstream
- Drop libtool dep 

* Fri Aug 28 2009 Colin Walters <walters@verbum.org> - 0.6.4-2
- Add dep on libtool temporarily

* Wed Aug 26 2009 Colin Walters <walters@verbum.org> - 0.6.4-1
- New upstream 0.6.4
- Drop upstreamed build fix patch 

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 Peter Robinson <pbrobinson@gmail.com> - 0.6.3-4
- Add upstream patch to fix a build crash

* Thu Jul  2 2009 Peter Robinson <pbrobinson@gmail.com> - 0.6.3-3
- Add -ggdb temporarily so it compiles on ppc64

* Thu Jul  2 2009 Peter Robinson <pbrobinson@gmail.com> - 0.6.3-2
- Add the new source file

* Thu Jul  2 2009 Peter Robinson <pbrobinson@gmail.com> - 0.6.3-1
- Update to 0.6.3

* Mon Jun  1 2009 Dan Williams <dcbw@redhat.com> - 0.6.2-1
- Update to 0.6.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Colin Walters <walters@verbum.org> - 0.6.1-1
- Update to 0.6.1

* Fri Oct 31 2008 Colin Walters <walters@verbum.org> - 0.6.0-1
- Create spec goo
