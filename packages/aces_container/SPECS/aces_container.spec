Name:           aces_container
Version:        1.0.2
Release:        4%{?dist}
Summary:        ACES Container Reference

License:        AMPAS BSD
URL:            https://github.com/ampas/aces_container
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         Switch-to-CMAKE-default-variables.patch
Patch1:         Set-the-appropriate-SONAME-for-the-library.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
This folder contains a reference implementation for an ACES container
file writer intended to be used with the Academy Color Encoding
System (ACES). The resulting file is compliant with the ACES container
specification (SMPTE S2065-4). However, there are a few things that are
not demonstrated by this reference implementation.

    Stereo channels
    EndOfFileFiller
    Arbitrary attributes and naming validations
    half type attributes
    keycode value validations

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%autosetup -p1
chmod -x aces_writeattributes.*


%build
mkdir build ; cd build
%{cmake} \
 ..

%make_build


%install
cd build
%make_install


%ldconfig_scriptlets


%files
%doc README.md
%license LICENSE
%{_libdir}/libAcesContainer.so.*

%files devel
%dir %{_includedir}/aces/
%{_includedir}/aces/*.h
%dir %{_libdir}/cmake/AcesContainer
%{_libdir}/cmake/AcesContainer/*.cmake
%{_libdir}/libAcesContainer.so
%{_libdir}/pkgconfig/AcesContainer.pc


%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-3
- Bump patch

* Wed Jul 18 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-2
- Update patches

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Tue Dec 02 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.0-3
- Fixup includedir for cmake

* Mon Aug 25 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.0-2
- Add Requires cmake for -devel

* Sun Apr 13 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.0-1
- Initial spec file

