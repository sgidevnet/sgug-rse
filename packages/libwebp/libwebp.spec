%global _hardened_build 1

Name:          libwebp
Version:       1.0.3
Release:       4%{?dist}
URL:           http://webmproject.org/
Summary:       Library and tools for the WebP graphics format
# Additional IPR is licensed as well. See PATENTS file for details
License:       BSD
Source0:       http://downloads.webmproject.org/releases/webp/%{name}-%{version}.tar.gz
Source1:       libwebp_jni_example.java

BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: giflib-devel
BuildRequires: libtiff-devel
#BuildRequires: java-devel
#BuildRequires: jpackage-utils
BuildRequires: swig
BuildRequires: autoconf automake libtool
#BuildRequires: freeglut-devel

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.


%package tools
Summary:       The WebP command line tools

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.


%package devel
Summary:       Development files for libwebp, a library for the WebP format
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.


#%%package java
#Summary:       Java bindings for libwebp, a library for the WebP format
#Requires:      #%%{name}#%%{?_isa} = #%%{version}-#%%{release}
#Requires:      java-headless
#Requires:      jpackage-utils

#%%description java
#Java bindings for libwebp.


%prep
%autosetup -p1


%build
autoreconf -vif
%ifarch aarch64
export CFLAGS="%{optflags} -frename-registers"
%endif
# Neon disabled due to resulting CFLAGS conflict resulting in
# inlining failed in call to always_inline '[...]': target specific option mismatch
#%%configure --disable-static
export CFLAGS="$RPM_OPT_FLAGS -mfp64 -mload-store-pairs -fPIE"
export LDFLAGS="$RPM_LD_FLAGS -mfp64 -pie"
%configure --disable-static --enable-libwebpmux \
           --enable-libwebpdemux --enable-libwebpdecoder \
           --disable-neon
%make_build V=1

# swig generated Java bindings
#cp %{SOURCE1} .
#cd swig
#rm -rf libwebp.jar libwebp_java_wrap.c
#mkdir -p java/com/google/webp
#swig -ignoremissing -I../src -java \
#    -package com.google.webp  \
#    -outdir java/com/google/webp \
#    -o libwebp_java_wrap.c libwebp.swig

#gcc %{__global_ldflags} %{optflags} -shared \
#    -I/usr/lib/jvm/java/include \
#    -I/usr/lib/jvm/java/include/linux \
#    -I../src \
#    -L../src/.libs -lwebp libwebp_java_wrap.c \
#    -o libwebp_jni.so

#cd java
#javac com/google/webp/libwebp.java
#jar cvf ../libwebp.jar com/google/webp/*.class


%install
%make_install
find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete

# swig generated Java bindings
#mkdir -p %{buildroot}/%{_libdir}/%{name}-java
#cp swig/*.jar swig/*.so %{buildroot}/%{_libdir}/%{name}-java/


#%%ldconfig_scriptlets


%files tools
%{_bindir}/cwebp
%{_bindir}/dwebp
%{_bindir}/gif2webp
%{_bindir}/img2webp
%{_bindir}/webpinfo
%{_bindir}/webpmux
#%%{_bindir}/vwebp
%{_mandir}/man*/*

%files -n %{name}
%doc README PATENTS NEWS AUTHORS
%license COPYING
%{_libdir}/%{name}.so.7*
%{_libdir}/%{name}decoder.so.3*
%{_libdir}/%{name}demux.so.2*
%{_libdir}/%{name}mux.so.3*

%files devel
%{_libdir}/%{name}*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

#%%files java
#%%doc libwebp_jni_example.java
#%%{_libdir}/%%{name}-java/


%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 1.0.3-4
- Rebuild for jpegturbo

* Sun Sep 27 2020  HAL <notes2@gmx.de> - 1.0.3-3
- Tweak to possible recommended flags from the README

* Sun Aug 30 2020  HAL <notes2@gmx.de> - 1.0.3-2
- compiles on Irix 6.5 with sgug-rse gcc 9.2. I dropped Java support.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
