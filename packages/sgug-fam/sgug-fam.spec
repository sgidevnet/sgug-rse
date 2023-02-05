Summary: SGUG File Access Monitoring Replacement Lib
Name: sgug-fam
Version: 0.1.0
Release: 1%{?dist}
License: LGPLv
URL: https://github.com/sgidevnet/sgug-fam
Source: https://github.com/sgidevnet/sgug-fam/archive/%{version}.tar.gz

BuildRequires: gcc, g++, binutils
BuildRequires: meson, ninja-build

%description
A like-for-like replacement of the standard IRIX fam library which requires
linking against the MIPSPro C++ libraries, which cannot work for GNU C++
programs.

%package devel
Summary: Header files and libraries for the sgug-fam library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
sgug-fam-devel contains the header files and libraries needed
to develop programs that use the sgug-fam library.

%prep
%autosetup -p1

%build
%meson
%meson_build

%check

%install
%meson_install

%files
%{_libdir}/libfam.so.*

%files devel
%{_libdir}/libfam.so
%{_libdir}/pkgconfig/fam*.pc
# We just use the IRIX headers, no need to double down on those.
#%%{_includedir}/libfam*


%changelog
* Sun Dec 27 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
