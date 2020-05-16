Name:           libspng
Version:        0.5.0
Release:        1%{?dist}
Summary:        Simple, modern libpng alternative

License:        BSD
URL:            https://libspng.org/
Source0:        https://github.com/randy408/libspng/archive/v%{version}/%{name}-%{version}.tar.gz
# BigEndian problems: https://github.com/randy408/libspng/issues/29
# fix test suite on big-endian
Patch0:         0001-fix-test-suite-on-big-endian.patch
# fix reading of bKGD chunks for palleted images
Patch1:         0001-fix-reading-of-bKGD-chunks-for-palleted-images.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
Libspng is a C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security and ease of use.

Libspng is an alternative to libpng, the projects are separate and the APIs are
not compatible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -Ddev_build=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/libspng.so.0*

%files devel
%doc docs
%{_includedir}/spng.h
%{_libdir}/libspng.so
%{_libdir}/pkgconfig/spng.pc

%changelog
* Tue May 13 2020 Alexander Tafarte <notes2@gmx.de> - 0.5.0-2
  Compiles nicely on Irix 6.5 and sgug-rse gcc 9.2

* Wed Aug 21 19:17:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Initial package
