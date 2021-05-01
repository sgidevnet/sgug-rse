# requested by https://bugzilla.redhat.com/1468338
# this break gdimagefile/gdnametest:
#   gdimagefile/gdnametest.c:122: 255 pixels different on /tmp/gdtest.CrpdIb/img.gif
#   gdimagefile/gdnametest.c:122: 255 pixels different on /tmp/gdtest.CrpdIb/img.GIF
#   FAIL gdimagefile/gdnametest (exit status: 2)
%global  with_liq   0


Summary:       A graphics library for quick creation of PNG or JPEG images
Name:          gd
Version:       2.2.5
Release:       11%{?prever}%{?short}%{?dist}
License:       MIT
URL:           http://libgd.github.io/
%if 0%{?commit:1}
# git clone https://github.com/libgd/libgd.git; cd gd-libgd
# git archive  --format=tgz --output=libgd-%{version}-%{commit}.tgz --prefix=libgd-%{version}/  master
Source0:       libgd-%{version}-%{commit}.tgz
%else
Source0:       https://github.com/libgd/libgd/releases/download/gd-%{version}/libgd-%{version}.tar.xz
%endif

Patch1:        gd-2.1.0-multilib.patch
# CVE-2018-5711 - https://github.com/libgd/libgd/commit/a11f47475e6443b7f32d21f2271f28f417e2ac04
Patch2:        gd-2.2.5-upstream.patch
# CVE-2018-1000222 - https://github.com/libgd/libgd/commit/ac16bdf2d41724b5a65255d4c28fb0ec46bc42f5
Patch3:        gd-2.2.5-gdImageBmpPtr-double-free.patch
Patch100:      libgd.sgifixes.patch

BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: gettext-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
%if %{with_liq}
BuildRequires: libimagequant-devel
%endif
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: perl-interpreter
BuildRequires: perl-generators
# for fontconfig/basic test
#BuildRequires: liberation-sans-fonts
BuildRequires: libimagequant-devel


%description
The gd graphics library allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from
other images, and flood fills, and to write out the result as a PNG or
JPEG file. This is particularly useful in Web applications, where PNG
and JPEG are two of the formats accepted for inline images by most
browsers. Note that gd is not a paint program.


%package progs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Utility programs that use libgd

%description progs
The gd-progs package includes utility programs supplied with gd, a
graphics library for creating PNG and JPEG images.


%package devel
Summary:  The development libraries and header files for gd
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: freetype-devel%{?_isa}
Requires: fontconfig-devel%{?_isa}
Requires: libjpeg-devel%{?_isa}
Requires: libpng-devel%{?_isa}
Requires: libtiff-devel%{?_isa}
Requires: libwebp-devel%{?_isa}
Requires: libX11-devel%{?_isa}
Requires: libXpm-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: libimagequant-devel%{?_isa}

%description devel
The gd-devel package contains the development libraries and header
files for gd, a graphics library for creating PNG and JPEG graphics.


%prep
%setup -q -n libgd-%{version}%{?prever:-%{prever}}
%patch1 -p1 -b .mlib
%patch2 -p1 -b .upstream
%patch3 -p1 -b .gdImageBmpPtr-free
%patch100 -p1 -b libgd.sgifixes
: $(perl config/getver.pl)

: regenerate autotool stuff
if [ -f configure ]; then
# This isnt necessary - autoreconf (the version we have) will do it anyway
#   libtoolize --copy --force
   autoreconf -vif
else
   ./bootstrap.sh
fi


%build
# Provide a correct default font search path
CFLAGS="$RPM_OPT_FLAGS -DDEFAULT_FONTPATH='\"\
/usr/sgug/share/fonts/bitstream-vera:\
/usr/sgug/share/fonts/dejavu:\
/usr/sgug/share/fonts/default/Type1:\
/usr/sgug/share/X11/fonts/Type1:\
/usr/sgug/share/fonts/liberation\"'"

%ifarch %{ix86}
# see https://github.com/libgd/libgd/issues/242
CFLAGS="$CFLAGS -msse -mfpmath=sse"
%endif

%ifarch aarch64 ppc64 ppc64le s390 s390x
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1359680
export CFLAGS="$CFLAGS -ffp-contract=off"
%endif

# To be able to test this package, it needs a "mkdtemp" which can be found
# in libdicl
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"

%configure \
    --with-tiff=%{_prefix} \
    --enable-rpath
make %{?_smp_mflags}


%install
make install INSTALL='install -p' DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libgd.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libgd.a


%check
: Upstream test suite
make check

: Check content of pkgconfig
grep %{version} $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gdlib.pc


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*.so.*

%files progs
%{_bindir}/*
%exclude %{_bindir}/gdlib-config

%files devel
%{_bindir}/gdlib-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gdlib.pc


%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2.2.5-11
- Rebuild for jpegturbo

* Sun Sep 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2.2.5-10
- Include webp dep, use libdicl to enable testing of it

* Mon Jun 22 2020  HAL <notes2@gmx.de> - 2.2.5-9
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 mskalick@redhat.com - 2.2.5-7
- Add missing requires to libimagequent-devel

* Thu Aug 30 2018 mskalick@redhat.com - 2.2.5-6
- Use libimagequant library (RHBZ#1468338)
