%global glib2_version 2.56.1
%global freetype_version 2.1.5
%global fontconfig_version 2.11.91
%global cairo_version 1.12.10
%global libthai_version 0.1.9
%global harfbuzz_version 1.4.2
%global libXft_version 2.0.0
%global fribidi_version 1.0

Name: pango
Version: 1.43.0
Release: 3%{?dist}
Summary: System for layout and rendering of internationalized text

License: LGPLv2+
URL: http://www.pango.org
Source0: https://download.gnome.org/sources/%{name}/1.43/%{name}-%{version}.tar.xz
Patch0: pango-fixes-pkg-config.patch

BuildRequires: pkgconfig(cairo) >= %{cairo_version}
BuildRequires: pkgconfig(freetype2) >= %{freetype_version}
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(fontconfig) >= %{fontconfig_version}
BuildRequires: pkgconfig(harfbuzz) >= %{harfbuzz_version}
#BuildRequires: pkgconfig(libthai) >= %{libthai_version}
BuildRequires: pkgconfig(xft) >= %{libXft_version}
BuildRequires: pkgconfig(fribidi) >= %{fribidi_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: cairo-gobject-devel
#BuildRequires: gtk-doc
BuildRequires: help2man
BuildRequires: meson
BuildRequires: gcc gcc-c++

#Requires: glib2%{?_isa} >= %{glib2_version}
Requires: freetype%{?_isa} >= %{freetype_version}
Requires: fontconfig%{?_isa} >= %{fontconfig_version}
Requires: cairo%{?_isa} >= %{cairo_version}
Requires: harfbuzz%{?_isa} >= %{harfbuzz_version}
#Requires: libthai%{?_isa} >= %{libthai_version}
Requires: libXft%{?_isa} >= %{libXft_version}
Requires: fribidi%{?_isa} >= %{fribidi_version}

%description
Pango is a library for laying out and rendering of text, with an emphasis
on internationalization. Pango can be used anywhere that text layout is needed,
though most of the work on Pango so far has been done in the context of the
GTK+ widget toolkit. Pango forms the core of text and font handling for GTK+.

Pango is designed to be modular; the core Pango layout engine can be used
with different font backends.

The integration of Pango with Cairo provides a complete solution with high
quality text handling and graphics rendering.

%package devel
Summary: Development files for pango
Requires: pango%{?_isa} = %{version}-%{release}
#Requires: glib2-devel%{?_isa} >= %{glib2_version}
Requires: freetype-devel%{?_isa} >= %{freetype_version}
Requires: fontconfig-devel%{?_isa} >= %{fontconfig_version}
Requires: cairo-devel%{?_isa} >= %{cairo_version}

%description devel
The pango-devel package includes the header files and developer documentation
for the pango package.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.


%prep
%setup -q -n pango-%{version}
%patch0 -p1 -b .pc

%build
export LD_LIBRARYN32_PATH=%{_builddir}/pango-1.43.0/mips-sgug-irix/pango/:$LD_LIBRARYN32_PATH

%meson -Denable_docs=false
%meson_build


%install
%meson_install

PANGOXFT_SO=$RPM_BUILD_ROOT%{_libdir}/libpangoxft-1.0.so
if ! test -e $PANGOXFT_SO; then
        echo "$PANGOXFT_SO not found; did not build with Xft support?"
        ls $RPM_BUILD_ROOT%{_libdir}
        exit 1
fi

rm -f $RPM_BUILD_ROOT/usr/sgug/share/man/man1/pan*

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libpango*-*.so.*
%{_bindir}/pango-list
%{_bindir}/pango-view
#%%{_mandir}/man1/pango-view.1*
%{_libdir}/girepository-1.0/Pango-1.0.typelib
%{_libdir}/girepository-1.0/PangoCairo-1.0.typelib
%{_libdir}/girepository-1.0/PangoFT2-1.0.typelib
%{_libdir}/girepository-1.0/PangoXft-1.0.typelib


%files devel
%{_libdir}/libpango*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
#%%doc %{_datadir}/gtk-doc/html/pango
%{_datadir}/gir-1.0/Pango-1.0.gir
%{_datadir}/gir-1.0/PangoCairo-1.0.gir
%{_datadir}/gir-1.0/PangoFT2-1.0.gir
%{_datadir}/gir-1.0/PangoXft-1.0.gir


%files tests
%{_libexecdir}/installed-tests/%{name}
%{_datadir}/installed-tests


%changelog
* Mon May 1 2020 HAL <hal@null.not> - 1.16.0-6
- removed the docs so it will compile nicely on Irix 6.5 without gtk-doc

* Mon Feb 11 2019 Peng Wu <pwu@redhat.com> - 1.43.0-3
- Fixes pkg-config issue

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 1.43.0-1
- Update to 1.43.0

* Fri Jan 18 2019 Peng Wu <pwu@redhat.com> - 1.42.4-2
- Fixes crash in pango_fc_font_key_get_variations when key is null

* Mon Aug 20 2018 David King <amigadave@amigadave.com> - 1.42.4-1
- Update to 1.42.4

* Mon Aug 20 2018 David King <amigadave@amigadave.com> - 1.42.3-2
- Include a fix for invalid Unicode sequence handling

* Mon Jul 30 2018 Kalev Lember <klember@redhat.com> - 1.42.3-1
- Update to 1.42.3

* Wed Jul 25 2018 Kalev Lember <klember@redhat.com> - 1.42.2-1
- Update to 1.42.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Kalev Lember <klember@redhat.com> - 1.42.1-2
- Rebuild against fribidi 1.0 (#1574861)

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 1.42.1-1
- Update to 1.42.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 1.42.0-1
- Update to 1.42.0

* Wed Mar 07 2018 Akira TAGOH <tagoh@redhat.com> - 1.41.1-2
- Add BR: gcc-c++

* Thu Mar 01 2018 Akira TAGOH <tagoh@redhat.com> - 1.41.1-1
- New upstream release. (#1550390)
- Add BR: pkgconfig(fribidi)

* Mon Feb 19 2018 Akira TAGOH <tagoh@redhat.com>
- Add BR: gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.40.14-1
- Update to 1.40.14
- Remove unused patch

* Thu Nov 02 2017 Kalev Lember <klember@redhat.com> - 1.40.13-2
- Backport a patch to fix wrapping long filenames in Nautilus

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 1.40.13-1
- Update to 1.40.13

* Tue Sep 05 2017 Kalev Lember <klember@redhat.com> - 1.40.12-1
- Update to 1.40.12

* Tue Aug 29 2017 Akira TAGOH <tagoh@redhat.com> - 1.40.11-3
- Fix multilib issue (#1485076)

* Sat Aug 19 2017 Kalev Lember <klember@redhat.com> - 1.40.11-1
- Update to 1.40.11

* Sat Aug 19 2017 Kalev Lember <klember@redhat.com> - 1.40.10-2
- Switch to the meson build system

* Wed Aug 16 2017 Kalev Lember <klember@redhat.com> - 1.40.10-1
- Update to 1.40.10

* Wed Aug 09 2017 Kalev Lember <klember@redhat.com> - 1.40.9-1
- Update to 1.40.9

* Tue Aug 08 2017 Kalev Lember <klember@redhat.com> - 1.40.8-1
- Update to 1.40.8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 1.40.7-1
- Update to 1.40.7

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 1.40.6-1
- Update to 1.40.6

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 1.40.5-1
- Update to 1.40.5

* Mon Feb 27 2017 Richard Hughes <rhughes@redhat.com> - 1.40.4-1
- Update to 1.40.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Kalev Lember <klember@redhat.com> - 1.40.3-1
- Update to 1.40.3

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 1.40.2-1
- Update to 1.40.2
- Don't set group tags

* Tue Apr 12 2016 Kalev Lember <klember@redhat.com> - 1.40.1-1
- Update to 1.40.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 1.40.0-1
- Update to 1.40.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 1.39.0-1
- Update to 1.39.0

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 1.38.1-1
- Update to 1.38.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 1.38.0-1
- Update to 1.38.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 1.37.5-1
- Update to 1.37.5

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 1.37.4-1
- Update to 1.37.4

* Sat Aug 15 2015 Kalev Lember <klember@redhat.com> - 1.37.3-1
- Update to 1.37.3
- Use make_install macro

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 1.37.2-1
- Update to 1.37.2

* Tue Jun 23 2015 David King <amigadave@amigadave.com> - 1.37.1-1
- Update to 1.37.1
- Use pkgconfig for BuildRequires
- Update man page glob in files section

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 1.37.0-1
- Update to 1.37.0
- Remove modules support from packaging as it's gone upstream
- Use license macro for the COPYING file

* Thu May 14 2015 Matthias Clasen <mclasen@redhat.com> - 1.36.8-5
- Regenerate man page for pango-view

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.36.8-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.36.8-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Jan 26 2015 Akira TAGOH <tagoh@redhat.com> - 1.36.8-2
- Add Requires(post): libXft deps. (#1155261)

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.36.8-1
- Update to 1.36.8

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 1.36.7-1
- Update to 1.36.7
- Tighten deps with the _isa macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 16 2014 Kalev Lember <kalevlember@gmail.com> - 1.36.6-1
- Update to 1.36.6

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.36.5-2
- Rebuilt for gobject-introspection 1.41.4

* Wed Jun 25 2014 Richard Hughes <rhughes@redhat.com> - 1.36.5-1
- Update to 1.36.5

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 1.36.4-1
- Update to 1.36.4

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 1.36.3-1
- Update to 1.36.3

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 1.36.2-1
- Update to 1.36.2

* Wed Jan 22 2014 Akira TAGOH <tagoh@redhat.com> - 1.36.1-2
- Backport a patch to fix SIGFPE in pango_layout_iter_get_char_extents() (#1036351)

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 1.36.1-1
- Update to 1.36.1

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 1.36.0-1
- Update to 1.36.0

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 1.35.3-1
- Update to 1.35.3

* Thu Aug 22 2013 Akira TAGOH <tagoh@redhat.com> - 1.35.2-2
- Fix duplicate file list for modules.cache
- s/%%define/%%global/g
- Fix bogus date in %%changelog
- Do not suppress the detailed build log.

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 1.35.2-1
- Update to 1.35.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 1.35.0-1
- Update to 1.35.0
- Add a tests subpackage

* Mon May 13 2013 Richard Hughes <rhughes@redhat.com> - 1.34.1-1
- Update to 1.34.1

* Wed May  8 2013 Matthias Clasen <mclasen@redhat.com> - 1.34.0-2
- Make man pango-query-modules-64 work

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1.34.0-1
- Update to 1.34.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 1.33.9-1
- Update to 1.33.9

* Tue Mar  5 2013 Matthias Clasen <mclasen@redhat.com> - 1.33.8-1
- Update to 1.33.8

* Tue Feb 05 2013 Kalev Lember <kalevlember@gmail.com> - 1.33.7-1
- Update to 1.33.7

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 1.32.6-1
- Update to 1.32.6

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 1.32.5-1
- Update to 1.32.5

* Wed Nov 21 2012 Richard Hughes <hughsient@gmail.com> - 1.32.3-1
- Update to 1.32.3

* Wed Nov 14 2012 Kalev Lember <kalevlember@gmail.com> - 1.32.2-1
- Update to 1.32.2

* Thu Sep 27 2012 Matthias Clasen <mclasen@redhat.com> - 1.32.1-1
- Update to 1.32.1
- Move module cache file to /usr/lib64/pango/1.8.0/modules.cache
- No more /etc/pango

* Sat Aug 25 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.31.0-3
- Fix %%postun error on multilib erase (#684729).

* Wed Aug 22 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 1.31.0-2
- Add missing BR:harfbuzz-devel
- Remove file pangox.aliases as pangox support is now removed

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 1.31.0-1
- Update to 1.31.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 1.30.1-1
- Update to 1.30.1

* Sat May 19 2012 Matthias Clasen <mclasen@redhat.com> - 1.30.0-2
- Fix up scriptlet dependencies (#684729)

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 1.30.0-1
- Update to 1.30.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Matthias Clasen <mclasen@redhat.com> - 1.29.5-1
- Update to 1.29.5

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 1.29.4-1
- Update to 1.29.4

* Wed Aug 17 2011 Kalev Lember <kalevlember@gmail.com> - 1.29.3-2
- Fix a crash in the fallback engine

* Fri Jun 17 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.29.3-1
- Update to 1.29.3

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.28.4-2
- Stop using G_CONST_RETURN

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 1.28.4-1
- Update to 1.28.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 1.28.3-1
- Update 1.28.3

* Tue Sep 21 2010 Matthias Clasen <mclasen@redhat.com> - 1.28.1-6
- Rebuild against newer gobject-introspection

* Fri Sep 03 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.28.1-5
- Merge Review cleanup (rh#226229)

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 1.28.1-4
- Rebuild for new gobject-introspection

* Tue Jun 29 2010 Colin Walters <walters@verbum.org> - 1.28.1-3
- Remove usage of chrpath, should no longer be needed

* Tue Jun 29 2010 Colin Walters <walters@verbum.org> - 1.28.1-2
- Support builds from snapshots

* Tue Jun 15 2010 Matthias Clasen <mclasen@redhat.com> - 1.28.1-1
- Update to 1.28.1

* Thu May 27 2010 Matthias Clasen <mclasen@redhat.com> - 1.28.0-2
- Enable introspection

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> - 1.28.0-1
- Update to 1.28.0

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 1.27.1-1
- Update to 1.27.1

* Wed Dec 16 2009 Matthias Clasen <mclasen@redhat.com> - 1.26.2-1
- Update to 1.26.2
- See http://download.gnome.org/sources/pango/1.26/pango-1.26.2.news

* Thu Dec  3 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.26.1-1
- 1.26.1

* Mon Sep 21 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.26.0-1
- 1.26.0

* Tue Sep  8 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.6-1
- 1.25.6

* Mon Aug 24 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.5-1
- 1.25.5

* Thu Aug 20 2009 Karsten Hopp <karsten@redhat.com> 1.25.4-2
- fix autoconf host on s390x

* Mon Aug 17 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.4-1
- 1.25.4

* Tue Aug 11 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.3-1
- 1.25.3

* Tue Aug 11 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.2-1
- 1.25.2

* Mon Aug 10 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.1-7
- Yes, I am stupid.

* Mon Aug 10 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.1-6
- One more try

* Mon Aug 10 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.1-5
- Remove -fexceptions from CXXFLAGS actually
- Hopefully builds this time

* Mon Aug 10 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.1-4
- Remove -fexceptions from RPM_OPT_FLAGS
- Hopefully builds this time

* Mon Aug 10 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.1-3
- Remove pango-1.25.1-no-hb-main.patch
- Add pango-1.25.1-cxx.patch
- Hopefully builds this time

* Mon Aug 10 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.1-2
- Add pango-1.25.1-no-hb-main.patch to fix build on x86-64

* Mon Aug 10 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.25.1-1
- Update to 1.25.1

* Wed Jul 22 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.24.5-1
- Update to 1.24.5

* Tue Jun 30 2009 Matthias Clasen <mclasen@redhat.com> - 1.24.4-1
- Update to 1.24.4

* Wed Jun 24 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.24.3-1
- Update to 1.24.3

* Fri May 15 2009 Karsten Hopp <karsten@redhat.com> 1.24.2-1
- Update to 1.24.2
- See http://download.gnome.org/sources/pango/1.24/pango-1.24.2.news

* Sat Apr 18 2009 Karsten Hopp <karsten@redhat.com> 1.24.1-1.1
- autoconf uses ibm-linux not redhat-linux (s390x)

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 1.24.1-1
- Update to 1.24.1
- See http://download.gnome.org/sources/pango/1.24/pango-1.24.1.news

* Thu Mar 26 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.24.0-2
- Remove weird Requires(pre).
- Resolves #486641

* Mon Mar 16 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.24.0-1
- Update to 1.24.0
- Package pango-view.1.gz

* Wed Mar 11 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.23.0-4.g5317893
- Push changes from git

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb  4 2009 Behdad Esfahbod <besfahbo@redhat.com> - 1.23.0-2
- Move pango-view from pango-devel to pango

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 1.23.0-1
- Update to 1.23.0

* Tue Dec 16 2008 Matthias Clasen <mclasen@redhat.com> - 1.22.4-1
- Update to 1.22.4

* Sun Dec  7 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.22.3-2
- Rebuild for pkgconfig provides

* Mon Nov 24 2008 Matthias Clasen <mclasen@redhat.com> - 1.22.3-1
- Update to 1.22.3

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 1.22.2-1
- Update to 1.22.2

* Mon Oct 20 2008 Matthias Clasen <mclasen@redhat.com> - 1.22.1-1
- Update to 1.22.1

* Mon Sep 22 2008 Behdad Esfahbod <besfahbo@redhat.com> - 1.22.0-1.1
- Rebuild against cairo 1.7.6
- Update cairo and glib required versions

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 1.22.0-1
- Update to 1.22.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.6-1
- Update to 1.21.6

* Tue Aug 26 2008 Behdad Esfahbod <besfahbo@redhat.com> - 1.21.5-1
- Update to 1.21.5

* Mon Aug 11 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.4-1
- Update to 1.21.4

* Tue Jun 17 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.3-1
- Update to 1.21.3

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.2-1
- Update to 1.21.2

* Mon May 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.21.1-2
- add sparc64 to multilib handling

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.1-1
- Update to 1.21.1

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.0-1
- Update to 1.21.0

* Tue Apr  8 2008 Matthias Clasen <mclasen@redhat.com> - 1.20.1-1
- Update to 1.20.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 1.20.0-1
- Update to 1.20.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 1.19.4-1
- Update to 1.19.4

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.19.3-3
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Behdad Esfahbod <besfahbo@redhat.com> - 1.19.3-2
- Bump libthai requirement.

* Mon Jan 21 2008 Behdad Esfahbod <besfahbo@redhat.com> - 1.19.3-1
- Update to 1.19.3

* Tue Dec 18 2007 Matthias Clasen <mclasne@redhat.com> - 1.19.2-1
- Update to 1.19.2

* Thu Dec  6 2007 Matthias Clasen <mclasne@redhat.com> - 1.19.1-1
- Update to 1.19.1

* Wed Oct 31 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.19.0-1
- Update to 1.19.0

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 1.18.3-1
- Update to 1.18.3 (make Nafees Nastaliq font work)

* Tue Sep 18 2007 Matthias Clasen <mclasen@redhat.com> - 1.18.2-1
- Update to 1.18.2

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 1.18.1-1
- Update to 1.18.1

* Thu Aug 23 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.18.0-1
- Update to 1.18.0

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.17.5-3
- Rebuild for PPC toolchain bug

* Thu Aug  2 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.5-2
- Update license field
- Don't install ChangeLog

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.5-1
- Update to 1.17.5

* Tue Jul 03 2007 Behdad Esfahbod <besfahbo@redhat.com>
- Distribute NEWS

* Mon Jul  2 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.4-1
- Update to 1.17.4

* Mon Jul  2 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.3-1
- Update to 1.17.3
- Drop ancient Obsoletes

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.2-1
- Update to 1.17.2

* Mon May 28 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.1-1
- Update to 1.17.1

* Sat May 19 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.0-1
- Update to 1.17.0

* Fri Apr 27 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.16.4-1
- Update to 1.16.4.
- Enable doc rebuilding to get cross-references right.

* Tue Apr 10 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.16.2-1
- Update to 1.16.2.

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 1.16.1-1
- Update to 1.16.1

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 1.16.0-1
- Update to 1.16.0

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 1.15.6-1
- Update to 1.15.6

* Mon Jan 22 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.5-1
- Update to 1.15.5.
- Drop upstreamed pango-1.15.4-slighthint.patch

* Thu Jan 18 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.4-5
- Again... HELLO.txt is moved.

* Thu Jan 18 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.4-4
- Bump again.  I accidentally tagged 1.15.3-4 as 1.15.4-3 previously :(.

* Thu Jan 18 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.4-3
- s/HELLO.utf8/HELLO.txt/ to match upstream.

* Wed Jan 17 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.4-2
- Update slighthint patch to apply.

* Wed Jan 17 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.4-1
- Update to 1.15.4
- [Build]Require libthai[-devel]
- Require pkgconfig in -devel
- Remove "static libs" from -devel description, since we don't ship them.

* Fri Jan 12 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.3-5
- Require pango = %%{version}-%%{release} in devel (previously didn't have
  releaes).

* Thu Jan 11 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.3-4
- Undo the posttrans change.  That's a no no.  We now regenerate the module
  file in postun if there are any other pango versions left.  This should
  take care of the problem in the future.

* Thu Jan 11 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.3-3
- Move pango.modules generation to posttrans, to make sure modules available
  in an older version but not this one are removed.
- Resolves #222217

* Tue Jan 09 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.3-2
- Update sources

* Tue Jan 09 2007 Behdad Esfahbod <besfahbo@redhat.com> - 1.15.3-1
- Update to 1.15.3
- Pass --with-included-modules=basic-fc.  Saves one page of memory per process.

* Thu Dec 21 2006 Matthias Clasen <mclasen@redhat.com> - 1.15.2-1
- Update to 1.15.2

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 1.15.1-1
- Update to 1.15.1

* Fri Oct 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.15.0-1
- Update to 1.15.0

* Thu Oct 12 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.14.6-1
- Update to 1.14.6

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.14.4-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.14.4-2
- Remove illegal g_object_unref().

* Fri Sep 15 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.14.4-1
- Update to 1.14.4
- Fixes bugs 198136, 306388, 206390
- Remove upstreamed patch

* Tue Sep 12 2006 Matthias Clasen <mclasen@redhat.com> - 1.14.3-2
- Fix Hangul decomposition issues (#206044)

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 1.14.3-1
- Update to 1.14.3

* Tue Aug 22 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.14.2-1
- Update to 1.14.2

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 1.14.1-1.fc6
- Update to 1.14.1

* Thu Aug 17 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.14.0-3
- Bump glib requirement to 2.12.0. (bug #201586)

* Mon Aug 07 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.14.0-2
- Incorrect sources in last update.  Fix.

* Mon Aug 07 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.14.0-1
- Update to 1.14.0

* Wed Aug 02 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.13.5-1
- Update to 1.13.5

* Thu Jul 27 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.13.4-2
- Add umask 022 to post (#185419)

* Tue Jul 25 2006 Matthias Clasen <mclasen@redhat.com> - 1.13.4-1
- Update to 1.13.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.13.3-1.1
- rebuild

* Mon Jul 10 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.13.3-1
- Update to 1.13.3

* Thu Jun 15 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.13.2-1
- Update to 1.13.2

* Sun May 21 2006 Matthias Clasen <mclasen@redhat.com> - 1.13.1-3
- Add missing BuildRequires (#191958)

* Tue May 16 2006 Matthias Clasen <mclasen@redhat.com> - 1.13.1-2
- Update to 1.13.1

* Mon May  8 2006 Matthias Clasen <mclasen@redhat.com> - 1.13.0-1
- Update to 1.13.0

* Fri Apr  7 2006 Matthias Clasen <mclasen@redhat.com> - 1.12.1-2
- Update to 1.12.1

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Sun Feb 26 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.99-1
- Update to 1.11.99

* Tue Feb 21 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.6-1
- Upate to 1.11.6
- Drop upstreamed patches

* Fri Feb 17 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.5-2
- Fix a crash in pango_split
- Hide some private API

* Mon Feb 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.5-1
- Update to 1.11.5

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.11.4-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.11.4-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb  6 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.4-1
- Update to 1.11.4

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.3-1
- Update to 1.11.3

* Mon Jan 16 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.2-1
- Update to 1.11.2

* Mon Dec 19 2005 Matthias Clasen <mclasen@redhat.com> - 1.11.1-2
- BuildRequire cairo-devel

* Wed Dec 14 2005 Matthias Clasen <mclasen@redhat.com> - 1.11.1-1
- Update to 1.11.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Matthias Clasen <mclasen@redhat.com> - 1.11.0-1
- Update to 1.11.0

* Tue Nov 29 2005 Matthias Clasen <mclasen@redhat.com> - 1.10.2-1
- Update to 1.10.2

* Sun Nov 13 2005 Jeremy Katz <katzj@redhat.com> - 1.10.1-6
- switch prereqs to modular X

* Fri Nov  4 2005 Matthias Clasen <mclasen@redhat.com> - 1.10.1-5
- Switch buildrequires to modular X.
- Don't install .la files for modules.

* Thu Oct 27 2005 Matthias Clasen <mclasen@redhat.com> - 1.10.1-2
- Bump the requirement for glib (#165928)

* Mon Oct  3 2005 Matthias Clasen <mclasen@redhat.com> - 1.10.1-1
- Newer upstream version
- Use the docs which are included in the tarball

* Wed Aug 17 2005 Owen Taylor <otaylor@redhat.com> - 1.10.0-1
- Upgrade to 1.10.0

* Mon Aug 15 2005 Kristian Høgsberg <krh@redhat.com> 1.9.1-2
- Patch out libpixman dependency.

* Thu Jul 28 2005 Owen Taylor <otaylor@redhat.com> 1.9.1-1
- Update to 1.9.1

* Tue Jun 21 2005 Matthias Clasen <mclasen@redhat.com> 
- Add a missing requires

* Tue Jun 21 2005 Matthias Clasen <mclasen@redhat.com> 1.9.0-1
- Update to 1.9.0
- Require cairo

* Fri Mar  4 2005 Owen Taylor <otaylor@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Tue Dec 21 2004 Matthias Clasen <mclasen@redhat.com> - 1.8.0-1
- Version 1.8.0
- Drop unneeded patches and hacks

* Wed Oct 20 2004 Owen Taylor <otaylor@redhat.com> - 1.6.0-7
- Fix problem with pango_layout_get_attributes returning one too few items
  (Needed to fix problems mentioned in #135656, 
  http://bugzilla.gnome.org/show_bug.cgi?id=155912)

* Tue Oct 19 2004 Owen Taylor <otaylor@redhat.com> - 1.6.0-6
- Make Hangul and Kana not backspace-deletes-char (#135356)

* Tue Oct 19 2004 Owen Taylor <otaylor@redhat.com> - 1.6.0-5
- Fix problem in the last patch where we weren't getting the metrics from the 
  right font description (#136428, Steven Lawrance)

* Mon Oct 18 2004 Owen Taylor <otaylor@redhat.com> - 1.6.0-4
- Move place where we compute fontset metrics to fix problems with line 
  height in CJK locales (#131218)

* Mon Oct 11 2004 Colin Walters <walters@redhat.com> - 1.6.0-3
- BR xorg-x11-devel instead of XFree86-devel

* Mon Sep 20 2004 Owen Taylor <otaylor@redhat.com> - 1.6.0-2
- Add patch from CVS to fix display of U+3000 (#132203,  
  reported upstream by Suresh Chandrasekharan, Federic Zhang)

* Mon Sep 20 2004 Owen Taylor <otaylor@redhat.com> - 1.6.0-1
- Version 1.6.0
- Add patch from CVS to fix bitmap-fonts/no-hint problem (#129246)

* Wed Sep  8 2004 Jeremy Katz <katzj@redhat.com> - 1.5.2-3
- fix running of pango-query-modules to have necessary libraries available
  (#132052)

* Mon Aug 16 2004 Owen Taylor <otaylor@redhat.com> - 1.5.2-2
- Fix crashes with left-matra fixups (#129982, Jatin Nansi)

* Mon Aug  2 2004 Owen Taylor <otaylor@redhat.com> - 1.5.2-1
- Update to 1.5.2
- Fix ppc/powerpc confusion when creating query-modules binary (#128645)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 17 2004 Owen Taylor <otaylor@redhat.com> 1.4.0-2
- Fix location for modules file on ppc/ppc64 (#114399)
- Make the spec file check to avoid further mismatches

* Wed Mar 17 2004 Alex Larsson <alexl@redhat.com> 1.4.0-1
- update to 1.4.0

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com> 1.3.6-1
- Update to 1.3.6
- Bump required glib2 to 2.3.1

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Mark McLoughlin <markmc@redhat.com> 1.3.5-1
- Update to 1.3.5

* Wed Feb 25 2004 Mark McLoughlin <markmc@redhat.com> 1.3.3-1
- Update to 1.3.3

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 23 2004 Jonathan Blandford <jrb@redhat.com> 1.3.2-1
- new version
- add man page

* Thu Dec 18 2003 Owen Taylor <otaylor@redhat.com> 1.2.5-4
- Deal with autoconf changing -linux to -linux-gnu (#112387)

* Mon Dec  8 2003 Owen Taylor <otaylor@redhat.com> 1.2.5-3.0
- Package pango-querymodules as pango-querymodules-{32,64}; look for 
  pango.modules in an architecture-specific directory.
  (Fixes #111511, Justin M. Forbes)

* Mon Sep  8 2003 Owen Taylor <otaylor@redhat.com> 1.2.5-2.0
- Fix problem with corrupt Thai shaper

* Wed Aug 27 2003 Owen Taylor <otaylor@redhat.com> 1.2.5-1.1
- Version 1.2.5

* Tue Aug 26 2003 Owen Taylor <otaylor@redhat.com> 1.2.4-1.1
- Version 1.2.4

* Tue Jul  8 2003 Owen Taylor <otaylor@redhat.com> 1.2.3-2.0
- Bump for rebuild

* Mon Jun  9 2003 Owen Taylor <otaylor@redhat.com>
- Version 1.2.3

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun  2 2003 Owen Taylor <otaylor@redhat.com>
- Use the right version-1.2.2 tarball

* Thu May 29 2003 Owen Taylor <otaylor@redhat.com>
- Version 1.2.2

* Thu Feb 13 2003 Tim Powers <timp@redhat.com> 1.2.1-3
- remove deps on Xft and Xft-devel since XFree86 no longer has the
  virtual prvodes. Instead, require XFree86-devel > 4.2.99

* Tue Feb 11 2003 Owen Taylor <otaylor@redhat.com>
- Fix problem where language tag wasn't causing relookup of font (#84034)

* Sun Feb  2 2003 Owen Taylor <otaylor@redhat.com>
- Version 1.2.1

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 14 2003 Owen Taylor <otaylor@redhat.com>
- Patch from CVS to synthesize GDEF tables for fonts
  without them, like the Kacst fonts in fonts-arabic

* Thu Jan  9 2003 Owen Taylor <otaylor@redhat.com>
- Make requires freetype, not freetype-devel (#81423)

* Tue Jan  7 2003 Owen Taylor <otaylor@redhat.com>
- Update slighthint patch for freetype-2.1.3 (#81125)

* Fri Dec 20 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.2.0

* Mon Dec 16 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.1.6

* Wed Dec 11 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.1.5

* Tue Dec  3 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.1.4

* Thu Nov 21 2002 Havoc Pennington <hp@redhat.com>
- change PKG_CONFIG_PATH hack to also search /usr/X11R6/lib64/pkgconfig

* Wed Nov 20 2002 Havoc Pennington <hp@redhat.com>
- explicitly require pangoxft to be built, so we catch situations such
  as xft.pc moving to /usr/X11R6
- also add /usr/X11R6/lib/pkgconfig to PKG_CONFIG_PATH as a temporary 
  hack

* Thu Nov  7 2002 Havoc Pennington <hp@redhat.com>
- 1.1.3

* Thu Oct 31 2002 Owen Taylor <otaylor@redhat.com> 1.1.1-5
- Require the necessary freetype version, don't just
  BuildRequires it (#74744)

* Thu Oct 31 2002 Owen Taylor <otaylor@redhat.com> 1.1.1-4
- Own /etc/pango (#73962, Enrico Scholz)
- Remove .la files from the build root

* Mon Oct  7 2002 Havoc Pennington <hp@redhat.com>
- require glib 2.0.6-3, try rebuild on more arches

* Wed Aug 21 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.1.1 (main change, fixes font selection for FT2 backend, 
  as in gdmgreeter)

* Thu Aug 15 2002 Owen Taylor <otaylor@redhat.com>
- Fix linked list manipulation problem that was causing hang for anaconda
- Fix warning from loading mini-fonts with context == NULL

* Wed Aug 14 2002 Owen Taylor <otaylor@redhat.com>
- Fix major memory leak in the last patch

* Tue Aug 13 2002 Owen Taylor <otaylor@redhat.com>
- Actually use language tags at the rendering layer (should fix #68211)

* Mon Jul 15 2002 Owen Taylor <otaylor@redhat.com>
- Remove fixed-ltmain.sh, relibtoolize; to fix relink problems without 
- Fix bug causing hex boxes to be misrendered
  leaving RPATH (#66005)
- For FT2 backend, supply FT_LOAD_NO_BITMAP to avoid problems with 
  fonts with embedded bitmaps (#67851)

* Mon Jul  8 2002 Owen Taylor <otaylor@redhat.com>
- Make basic-x shaper work with our big-5 fonts

* Wed Jul  3 2002 Owen Taylor <otaylor@redhat.com>
- New upstream tarball with hooks for change-on-the fly font rendering

* Tue Jun 25 2002 Owen Taylor <otaylor@redhat.com>
- Up FreeType version to deal with FreeType-2.0.x / 2.1.x \
  ABI changes for pango's OpenType code.

* Mon Jun 24 2002 Owen Taylor <otaylor@redhat.com>
- Add some Korean aliases that the installer wants

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jun  8 2002 Havoc Pennington <hp@redhat.com>
- devel package requires fontconfig/Xft devel packages

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Jun  6 2002 Owen Taylor <otaylor@redhat.com>
- Snapshot with Xft2/fontconfig support

* Wed May 29 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.0.2
- Patch for charmaps problem

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed May 22 2002 Havoc Pennington <hp@redhat.com>
- add patch to adjust to newer version of freetype

* Wed Apr  3 2002 Alex Larsson <alexl@redhat.com>
- Update to version 1.0.1, remove patch

* Tue Mar 19 2002 Owen Taylor <otaylor@redhat.com>
- Patch from CVS for big speedup with FreeType-2.0.9

* Mon Mar 11 2002 Owen Taylor <otaylor@redhat.com>
- Rebuild

* Fri Mar  8 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.0.0

* Mon Feb 25 2002 Alex Larsson <alexl@redhat.com>
- Update to 0.26

* Thu Feb 21 2002 Alex Larsson <alexl@redhat.com>
- Bump for rebuild

* Mon Feb 18 2002 Alex Larsson <alexl@redhat.com>
- Update to 0.25

* Fri Feb 15 2002 Havoc Pennington <hp@redhat.com>
- add horrible buildrequires hack

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 0.24.90 cvs snap

* Tue Jan 29 2002 Owen Taylor <otaylor@redhat.com>
- Version 0.24

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- new snap 0.23.90

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- rebuild with 64-bit-fixed glib

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- Version 0.22
- add explicit check for required glib2 version before we do the build,
  so we don't end up with bad RPMs on --nodeps builds
- PreReq the glib2_version version, instead of 1.3.8 hardcoded that 
  no one had updated recently

* Thu Oct 25 2001 Owen Taylor <otaylor@redhat.com>
- Version 0.21

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- cvs snap
- new cvs snap with a bugfix

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- sync with Owen's changes, fix up dependency versions

* Wed Sep 19 2001 Havoc Pennington <hp@redhat.com>
- 0.19

* Mon Sep 10 2001 Havoc Pennington <hp@redhat.com>
- build CVS snap

* Wed Sep 05 2001 Havoc Pennington <hp@redhat.com>
- no relinking junk

* Tue Sep  4 2001 root <root@dhcpd37.meridian.redhat.com>
- Version 0.18

* Fri Jul 20 2001 Owen Taylor <otaylor@redhat.com>
- Configure --disable-gtk-doc
- BuildRequires freetype-devel, XFree86-devel

* Tue Jun 12 2001 Havoc Pennington <hp@redhat.com>
- 0.17
- libtool hackarounds

* Fri May 04 2001 Owen Taylor <otaylor@redhat.com>
- 0.16, rename back to pango from pango-gtkbeta

* Fri Feb 16 2001 Owen Taylor <otaylor@redhat.com>
- Obsolete fribidi-gtkbeta

* Mon Dec 11 2000 Havoc Pennington <hp@redhat.com>
- Remove that patch I just put in

* Mon Dec 11 2000 Havoc Pennington <hp@redhat.com>
- Patch pangox.pc.in to include -Iincludedir

* Fri Nov 17 2000 Owen Taylor <otaylor@redhat.com>
- final 0.13

* Tue Nov 14 2000 Owen Taylor <otaylor@redhat.com>
- New 0.13 tarball

* Mon Nov 13 2000 Owen Taylor <otaylor@redhat.com>
- 0.13pre1

* Sun Aug 13 2000 Owen Taylor <otaylor@redhat.com>
- Rename to 0.12b to avoid versioning problems

* Thu Aug 10 2000 Havoc Pennington <hp@redhat.com>
- Move to a CVS snapshot

* Fri Jul 07 2000 Owen Taylor <otaylor@redhat.com>
- Move back to /usr
- Version 0.12

* Mon Jun 19 2000  Owen Taylor <otaylor@redhat.com>
- Add missing %%defattr

* Thu Jun 8 2000  Owen Taylor <otaylor@redhat.com>
- Rebuild with a prefix of /opt/gtk-beta

* Wed May 31 2000 Owen Taylor <otaylor@redhat.com>
- version 0.11
- add --without-qt

* Wed Apr 26 2000 Owen Taylor <otaylor@redhat.com>
- Make the devel package require *-gtkbeta-* not the normal packages.

* Tue Apr 25 2000 Owen Taylor <otaylor@redhat.com>
- GTK+ snapshot version installing in /opt/gtk-beta

* Fri Feb 11 2000 Owen Taylor <otaylor@redhat.com>
- Created spec file
