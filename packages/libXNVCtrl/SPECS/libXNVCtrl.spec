Name:           libXNVCtrl
Version:        435.17
Release:        1%{?dist}
Summary:        Library providing the NV-CONTROL API
License:        GPLv2+
URL:            https://download.nvidia.com/XFree86/nvidia-settings/
Source0:        %{url}/nvidia-settings-%{version}.tar.bz2
Patch0:         libxnvctrl_so_0.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: libXext-devel
# BuildRequires: hostname

# Obsoletes older package provided in the NVIDIA CUDA repository
Obsoletes: nvidia-%{name} < 3:%{version}-100
Provides: nvidia-%{name} = 3:%{version}-100

%description
This packages contains the libXNVCtrl library from the nvidia-settings
application. This library provides the NV-CONTROL API for communicating with
the proprietary NVidia xorg driver. This package does not contain the
nvidia-settings tool itself as that is included with the proprietary drivers
themselves. 


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n nvidia-settings-%{version}


%build
%{set_build_flags}
%make_build \
   CC="gcc" \
   NV_VERBOSE=1 \
   DO_STRIP=0 \
   STRIP_CMD=/dev/true \
   -C src/%{name} \
   libXNVCtrl.so


%install
_wd=$PWD
cd src/%{name}
install -m 0755 -d $RPM_BUILD_ROOT%{_libdir}/
install -p -m 0755 libXNVCtrl.so.0.0.0    $RPM_BUILD_ROOT%{_libdir}/
ln -s libXNVCtrl.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libXNVCtrl.so.0
ln -s libXNVCtrl.so.0 $RPM_BUILD_ROOT%{_libdir}/libXNVCtrl.so
install -m 0755 -d $RPM_BUILD_ROOT%{_includedir}/NVCtrl/
install -p -m 0644 {nv_control,NVCtrl,NVCtrlLib}.h $RPM_BUILD_ROOT%{_includedir}/NVCtrl/
cd $_wd


#%%ldconfig_post

#%%ldconfig_postun


%files
%license COPYING
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/NV-CONTROL-API.txt doc/FRAMELOCK.txt
%{_includedir}/NVCtrl
%{_libdir}/%{name}.so


%changelog
* Mon Aug 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 435.17-1
- Update to 435.17
- Obsoletes older nvidia-libXNVCtrl from cuda repo
- Switch URL to https

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 352.21-9
- Use ldconfig scriptlet macros

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 352.21-8
- Use LDFLAGS from redhat-rpm-config
- Add "BuildRequires: gcc"
- Remove "Group:"

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 352.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 352.21-2
- fix build flags

* Thu Jul 09 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 352.21-1
- update to latest 352.21 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 169.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 08 2008 Dennis Gilmore <dennis@ausil.us> 169.12-2
- make sure libdir is set right on sparc64

* Wed Mar  5 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 169.12-1
- Update to new upstream 169.12 release (talking about version inflation)

* Tue Feb 19 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-7
- Rebase to latest upstream, which is still called 1.0 (GRRRR)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-6
- Autorebuild for GCC 4.3

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-5
- Update License tag for new Licensing Guidelines compliance

* Fri Jul 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-4
- Add missing libXext-devel BuildRequires

* Fri Jul 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-3
- Link the lib against libX11 and libXext to avoid undefined non weak symbols
  (through updated libXNVCtrl-imake.patch)

* Sun Jul 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-2
- Honor optflags
- Preserve timestamps of headers when installing them

* Sun Jul 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-1
- Initial Fedora Extras version
