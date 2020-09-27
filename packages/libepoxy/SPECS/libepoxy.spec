Summary: epoxy runtime library
Name: libepoxy
Version: 1.5.3
Release: 5%{?dist}
License: MIT
URL: https://github.com/anholt/libepoxy
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch100:   epoxy.sgifixes.patch

# WORKAROUND: non-upstreamable patch to drop
# Requires.private: gl egl
# since mesa recently droppg egl.pc from packaging.  Works only
# beause fedora installs everything into prefix that's already
# included by default (why it's not upstreamable).
# see also:
# libepoxy: https://bugzilla.redhat.com/show_bug.cgi?id=1744320
# mesa: https://bugzilla.redhat.com/show_bug.cgi?id=1744292
Patch1: libepoxy-1.5.3-pkgconfig_drop_private_gl.patch

BuildRequires:  meson
BuildRequires:  gcc
# Until patch1 is no longer needed, don't rely on pkgconfig
#BuildRequires:  pkgconfig(gl)
#BuildRequires:  pkgconfig(egl)
#BuildRequires: libGL-devel
#BuildRequires: libEGL-devel
#BuildRequires:  pkgconfig(glesv2)
BuildRequires:  python3
#BuildRequires:  xorg-x11-server-Xvfb mesa-dri-drivers

%description
A library for handling OpenGL function pointer management.

%package devel
Summary: Development files for libepoxy
Requires: %{name}%{?_isa} = %{version}-%{release}
# manually add header dependencies instead of relying on pkgconfig deps
# see patch1
#Requires: libGL-devel
#Requires: libEGL-devel

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -Dtests=false -Dx11=true -Dglx=yes -Degl=no
%meson_build

%install
%meson_install

%check
# this should be %%meson_test but the macro expands with a bajillion
# embedded newlines for no obvious reason
#xvfb-run -d -s "-screen 0 640x480x24" ninja -C %{_vpath_builddir} test || \
#    (cat %{_vpath_builddir}/meson-logs/testlog.txt ; exit 1)

#%%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/libepoxy.so.0*

%files devel
%{_includedir}/epoxy/
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc

%changelog
* Mon Sep 21 2020  HAL <notes2@gmx.de> - 1.5.3-5
- changed option -Dglx from false to true since this gives us epoxy/glx.h which is required for gtk3

* Sat Sep 19 2020  HAL <notes2@gmx.de> - 1.5.3-4
- compiles on Irix 6.5 with sgug-rse gcc 9.2. Very stripped down epoxy.RTLD_NOLOAD is defined x10. 

* Thu Aug 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.5.3-4
- epoxy.pc: -Requires.private: gl egl (#1744320)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Kalev Lember <klember@redhat.com> - 1.5.3-1
- Update to 1.5.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Kalev Lember <klember@redhat.com> - 1.5.2-1
- Update to 1.5.2

* Wed Apr 25 2018 Adam Jackson <ajax@redhat.com> - 1.5.1-2
- Enable tests for all arches
- Run tests against Xvfb so we get plausible amounts of coverage

* Wed Apr 25 2018 Kalev Lember <klember@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Wed Feb 28 2018 Kalev Lember <klember@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-5
- Switch to %%ldconfig_scriptlets

* Fri Sep 22 2017 Adam Jackson <ajax@redhat.com> - 1.4.3-4
- Backport some useful bits from master

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Adam Jackson <ajax@redhat.com> - 1.4.3-1
- libepoxy 1.4.3

* Thu Mar 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4.1-2
- Switch to meson
- Add license file
- Simplify spec

* Thu Mar 09 2017 Dave Airlie <airlied@redhat.com> - 1.4.1-1
- libepoxy 1.4.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Adam Jackson <ajax@redhat.com> - 1.3.1-3
- Fix detection of EGL client extensions

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 05 2015 Adam Jackson <ajax@redhat.com> 1.3.1-1
- libepoxy 1.3.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Dave Airlie <airlied@redhat.com> 1.2-3
- update GL registry files (add new EGL extension)

* Wed Mar 25 2015 Adam Jackson <ajax@redhat.com> 1.2-2
- Fix description to not talk about DRM
- Sync some small bugfixes from git

* Mon Oct 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-1
- Update to 1.2 GA
- Don't fail build on make check failure for some architectures

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.20140411git6eb075c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.3.20140411git6eb075c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Dave Airlie <airlied@redhat.com> 1.2-0.2.20140411git6eb075c
- update to latest git snapshot

* Thu Mar 27 2014 Dave Airlie <airlied@redhat.com> 1.2-0.1.20140307gitd4ad80f
- initial git snapshot

