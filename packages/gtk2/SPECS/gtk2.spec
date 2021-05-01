%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

%global _changelog_trimtime %(date +%s -d "1 year ago")

%define glib2_base_version 2.28.0
%define glib2_version %{glib2_base_version}-1
%define pango_base_version 1.20.0
%define pango_version %{pango_base_version}-1
%define atk_base_version 1.29.4
%define atk_version %{atk_base_version}-2
%define cairo_base_version 1.6.0
%define cairo_version %{cairo_base_version}-1
%define xrandr_version 1.2.99.4-2
%define gobject_introspection_version 0.9.3
%define gir_repository_version 0.6.5-5

%define bin_version 2.10.0

# Filter provides for private modules
%global __provides_exclude_from ^%{_libdir}/gtk-2.0

Summary: GTK+ graphical user interface library
Name: gtk2
Version: 2.24.32
Release: 8%{?dist}
License: LGPLv2+
URL: http://www.gtk.org
#VCS: git:git://git.gnome.org/gtk+#gtk-2-24
Source: http://download.gnome.org/sources/gtk+/2.24/gtk+-%{version}.tar.xz
Source2: update-gtk-immodules
Source3: im-cedilla.conf
Source4: update-gtk-immodules.1

# Use Python 3 in gtk-builder-convert
# Accepted upstream: https://gitlab.gnome.org/GNOME/gtk/merge_requests/1080
Patch1: python3.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=583273
Patch2: icon-padding.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599618
Patch8: tooltip-positioning.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=611313
Patch15: window-dragging.patch

# Backported from upstream:
Patch20: 0001-calendar-Use-the-new-OB-format-if-supported.patch
Patch21: 0001-Fix-compiler-warnings-with-GCC-8.1.patch

Patch100:   gtk2.sgifixes.patch

BuildRequires: pkgconfig(atk) >= %{atk_version}
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango) >= %{pango_version}
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: gettext
#BuildRequires: cups-devel
# Bootstrap requirements
#BuildRequires: gtk-doc
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: pkgconfig

# Conflicts with packages containing theme engines
# built against the 2.4.0 ABI
Conflicts: gtk2-engines < 2.7.4-7
Conflicts: libgnomeui < 2.15.1cvs20060505-2
Conflicts: redhat-artwork < 0.243-1

Provides: gail = %{version}-%{release}
Obsoletes: gail < 2.13.0-1

# required for icon theme apis to work
Requires: hicolor-icon-theme
# built as a subpackage of gtk3
#Requires: gtk-update-icon-cache

# required to support all the different image formats
Requires: gdk-pixbuf2-modules%{?_isa}

Requires: glib2 >= %{glib2_version}
Requires: atk >= %{atk_version}
Requires: pango >= %{pango_version}
# We need to prereq these so we can run gdk-pixbuf-query-loaders
Requires(post): libtiff >= 3.6.1
Requires: libXrandr >= %{xrandr_version}

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%package immodules
Summary: Input methods for GTK+
Requires: gtk2 = %{version}-%{release}
# for /etc/X11/xinit/xinput.d
#Requires: imsettings

%description immodules
The gtk2-immodules package contains standalone input methods that are shipped
as part of GTK+.

%package immodule-xim
Summary: XIM support for GTK+
Requires: gtk2 = %{version}-%{release}

%description immodule-xim
The gtk2-immodule-xim package contains XIM support for GTK+.

%package devel
Summary: Development files for GTK+
Requires: gtk2 = %{version}-%{release}
Requires: pango-devel >= %{pango_version}
Requires: atk-devel >= %{atk_version}
Requires: glib2-devel >= %{glib2_version}
Requires: gdk-pixbuf2-devel
Requires: cairo-devel >= %{cairo_version}
Requires: libX11-devel, libXcursor-devel, libXinerama-devel
Requires: libXext-devel, libXi-devel, libXrandr-devel
Requires: libXfixes-devel, libXcomposite-devel
Requires: pkgconfig

Provides: gail-devel = %{version}-%{release}
Obsoletes: gail-devel < 2.13.0-1

%description devel
This package contains the libraries and header files that are needed
for writing applications with the GTK+ widget toolkit. If you plan
to develop applications with GTK+, consider installing the gtk2-devel-docs
package.

%package devel-docs
Summary: Developer documentation for GTK+
Requires: gtk2 = %{version}-%{release}
#BuildArch: noarch

%description devel-docs
This package contains developer documentation for the GTK+ widget toolkit.

%prep
%autosetup -n gtk+-%{version} -p1

# A place to build the sgug patch
#exit 1

%build
export XDG_DATA_DIRS=/usr/sgug/share
export PERL=%{_bindir}/perl
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; CONFIGFLAGS=--disable-gtk-doc; fi;
export CFLAGS="-D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="$CFLAGS -g -Og"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%else
export CFLAGS="$CFLAGS -fno-strict-aliasing $RPM_OPT_FLAGS"
%endif
 %configure $CONFIGFLAGS \
	--enable-man		\
	--with-xinput=xfree	\
        --enable-xinerama       \
        --disable-glibtest      \
        --disable-gtk-doc-html  \
        --disable-cups          \
	--enable-debug		\
        --with-xml-catalog=%{_sysconfdir}/xml/catalog
)

rm libtool
cp /usr/sgug/bin/libtool libtool
# fight unused direct deps
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

make %{?_smp_mflags}

# truncate NEWS
awk '/^Overview of Changes/ { seen+=1 }
{ if (seen < 2) print }
{ if (seen == 2) { print "For older news, see http://git.gnome.org/cgit/gtk+/plain/NEWS"; exit } }' NEWS > tmp; mv tmp NEWS

%install
# Deriving /etc/gtk-2.0/$host location
# NOTE: Duplicated below
#
# autoconf changes linux to linux-gnu
#case "%{_host}" in
#  *linux) host="%{_host}-gnu"
#  ;;
#  *) host="%{_host}"
#  ;;
#esac

# autoconf uses powerpc not ppc
#host=`echo $host | sed "s/^ppc/powerpc/"`
# autoconf uses ibm-linux not redhat-linux (s390x)
#host=`echo $host | sed "s/^s390\(x\)*-redhat/s390\1-ibm/"`

# Make sure that the host value that is passed to the compile
# is the same as the host that we're using in the spec file
#
#compile_host=`grep 'host_triplet =' gtk/Makefile | sed "s/.* = //"`

#if test "x$compile_host" != "x$host" ; then
#  echo 1>&2 "Host mismatch: compile='$compile_host', spec file='$host'" && exit 1
#fi

make install DESTDIR=$RPM_BUILD_ROOT        \
             RUN_QUERY_IMMODULES_TEST=false

#echo ".so man1/gtk-query-immodules-2.0.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gtk-query-immodules-2.0-%{__isa_bits}.1

#gzip -c %{SOURCE4} > $RPM_BUILD_ROOT%{_mandir}/man1/update-gtk-immodules.1.gz

%find_lang gtk20
%find_lang gtk20-properties

#
# Make cleaned-up versions of tutorials, examples, and faq for installation
#
#mkdir -p tmpdocs
#cp -aR docs/tutorial/html tmpdocs/tutorial
#cp -aR docs/faq/html tmpdocs/faq

#for dir in examples/* ; do
#  if [ -d $dir ] ; then
#     mkdir -p tmpdocs/$dir
#     for file in $dir/* ; do
#       install -m 0644 $file tmpdocs/$dir
#     done
#  fi
#done

# We need to have separate 32-bit and 64-bit binaries
# for places where we have two copies of the GTK+ package installed.
# (we might have x86_64 and i686 packages on the same system, for example.)
%if %{__isa_bits} == 64
mv $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0 $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0-64
%else
mv $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0 $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0-32
%endif

# Install wrappers for the binaries
cp %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/update-gtk-immodules

# Input method frameworks want this
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d

# Use python3 shebang instead of ambiguous python
pathfix.py -pn -i %{__python3} $RPM_BUILD_ROOT%{_bindir}/gtk-builder-convert

# Remove unpackaged files
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{bin_version}/*/*.la
rm $RPM_BUILD_ROOT%{_bindir}/gtk-update-icon-cache
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/*.a
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{bin_version}/*/*.a
rm $RPM_BUILD_ROOT%{_mandir}/man1/gtk-update-icon-cache.1*

touch $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{bin_version}/immodules.cache

mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/immodules
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{bin_version}/filesystems

%transfiletriggerin -- %{_libdir}/gtk-2.0/immodules/ %{_libdir}/gtk-2.0/%{bin_version}/immodules/
gtk-query-immodules-2.0-%{__isa_bits} --update-cache

%transfiletriggerpostun -- %{_libdir}/gtk-2.0/immodules/ %{_libdir}/gtk-2.0/%{bin_version}/immodules/
gtk-query-immodules-2.0-%{__isa_bits} --update-cache

%files -f gtk20.lang
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/gtk-query-immodules-2.0-%{__isa_bits}
%{_bindir}/update-gtk-immodules
%{_libdir}/libgtk-x11-2.0.so.*
%{_libdir}/libgdk-x11-2.0.so.*
%{_libdir}/libgailutil.so.*
%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/%{bin_version}
%{_libdir}/gtk-2.0/%{bin_version}/engines
%{_libdir}/gtk-2.0/%{bin_version}/filesystems
%dir %{_libdir}/gtk-2.0/%{bin_version}/immodules
%{_libdir}/gtk-2.0/%{bin_version}/printbackends
%{_libdir}/gtk-2.0/modules
%{_libdir}/gtk-2.0/immodules
%dir %{_datadir}/gtk-2.0
%{_datadir}/themes/Default
%{_datadir}/themes/Emacs
%{_datadir}/themes/Raleigh
%ghost %{_libdir}/gtk-2.0/%{bin_version}/immodules.cache
%{_libdir}/girepository-1.0
%{_mandir}/man1/gtk-query-immodules-2.0*
#%%{_mandir}/man1/update-gtk-immodules.1.gz

%files immodules
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-am-et.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-cedilla.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-cyrillic-translit.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-inuktitut.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-ipa.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-multipress.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-thai.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-ti-er.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-ti-et.so
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-viqr.so
%{_sysconfdir}/X11/xinit/xinput.d/im-cedilla.conf
%dir %{_sysconfdir}/gtk-2.0
%config(noreplace) %{_sysconfdir}/gtk-2.0/im-multipress.conf

%files immodule-xim
%{_libdir}/gtk-2.0/%{bin_version}/immodules/im-xim.so

%files devel -f gtk20-properties.lang
%{_libdir}/lib*.so
%{_libdir}/gtk-2.0/include
%{_includedir}/*
%{_datadir}/aclocal/*
%{_bindir}/gtk-builder-convert
%{_libdir}/pkgconfig/*
%{_bindir}/gtk-demo
%{_datadir}/gtk-2.0/demo
%{_datadir}/gir-1.0
%{_mandir}/man1/gtk-builder-convert.1.gz

%files devel-docs
%{_datadir}/gtk-doc
#%%doc tmpdocs/tutorial
#%%doc tmpdocs/faq
#%%doc tmpdocs/examples

%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2.24.32-8
- Rebuild for jpegturbo

* Mon Jul 20 2020 Daniel Hams <daniel.hams@gmail.com> - 2.24.32-7
- Fix to avoid use of buggy XkbSelecteventDetails call that causes GTK crashes.

* Sun Jun 21 2020 Daniel Hams <daniel.hams@gmail.com> - 2.24.32-6
- Upgrade to latest from fc31, fix up cups, xml-catalog, icon catalog, use python3, fix up compilation bug with IRIX headers

* Mon Jun 15 2020  HAL <notes2@gmx.de> - 2.24.32-5
- compiles on Irix 6.5 with sgug-rse gcc 9.2. Not perfect yet, needs some finetuning. 

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jan 27 2019 Kalev Lember <klember@redhat.com> - 2.24.32-4
- Backport two fixes from upstream (#1669768)
- calendar: Use the new "%OB" format if supported
- Fix compiler warnings with GCC 8.1
