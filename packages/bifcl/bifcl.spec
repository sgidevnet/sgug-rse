Name:           bifcl
Version:        1.2
Release:        1%{?dist}
Summary:        A built-in-function (BIF) compiler/generator

License:        BSD
URL:            https://github.com/zeek/bifcl
Source0:        https://www.zeek.org/downloads/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++

%description
The bifcl program simply takes a .bif file as input and generates C++
header/source files along with a .bro script that all-together provide the 
declaration and implementation of Bro/Zeek built-in-functions (BIFs), which
can then be compiled and shipped ss part of a Bro/Zeek plugin.

A BIF allows one to write arbitrary C++ code and access it via a function
call inside a Bro script. In this way, they can also be used to access parts
of Bro/Zeek's internal C++ API that aren't already exposed via their own BIFs.

At the moment, learning the format of a .bif file is likely easiest by just
taking a look at the .bif files inside the Bro/Zeek source-tree.

%prep
%autosetup

%build
mkdir build
cd build
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    ..
%make_build

%install
%make_install

%files
%doc README CHANGES
%license COPYING
%{_bindir}/%{name}

%changelog
* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Update to latest upstream release 1.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-1
- Initial package
