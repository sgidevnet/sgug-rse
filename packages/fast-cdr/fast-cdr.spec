%global commit 649b9a0e763f8a4cfdd41238b1495c58b7ea6660
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global project Fast-CDR
%global soversion 1

Name:       fast-cdr
Version:    1.0.10
Release:    3%{?dist}
Summary:    Fast Common Data Representation (CDR) Serialization Library

License:    ASL 2.0
URL:        http://www.eprosima.com
Source0:    https://github.com/eprosima/%{project}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz    
# Fix detection of big/little endianness for ppc64le
Patch0:     %{name}-1.0.10-endian.patch
# Install CMake scripts to lib instead of share
Patch1:     %{name}-1.0.10-cmakeinstall.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
eProsima FastCDR is a C++ library that provides two serialization mechanisms.
One is the standard CDR serialization mechanism, while the other is a faster
implementation that modifies the standard.

%package devel
Summary:    Development files and libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and libraries for %{name}

%prep
%setup -q -n %{project}-%{commit} 
%patch0 -p 1 -b .endian
%patch1 -p 1 -b .cmakeinstall

%build
mkdir build
cd build
%cmake ..
make %{?_smp_mflags}

%install
%make_install -C build

%files
%license LICENSE
%doc "doc/Users Manual.odt"
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}
%{_datadir}/fastcdr

%files devel
%{_libdir}/*.so
%{_includedir}/fastcdr
%{_libdir}/fastcdr

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Rich Mattes <richmattes@gmail.com> - 1.0.10-2
- Move CMake script installation to libdir

* Tue Jul 02 2019 Rich Mattes <richmattes@gmail.com> - 1.0.10-1
- Update to release 1.0.10

* Sat Jun 09 2018 Rich Mattes <richmattes@gmail.com> - 1.0.7-0.1.git8d14897
- Update to 1.0.7 pre-release

* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-2
- Rename endian define to avoid conflicts

* Fri Jun 9 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-1
- Initial package
