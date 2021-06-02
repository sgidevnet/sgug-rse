Name:           mathex
Version:        0.3b
Release:        16%{?dist}
Summary:        C++ library to parse/evaluate mathematical expressions

# Exceptions apply to static linking, see license.txt
License:        LGPLv2+ with exceptions
URL:            http://sscilib.sourceforge.net/
Source0:        http://sourceforge.net/projects/sscilib/files/%{name}/%{name}-0.3-b.zip
Source1:        CMakeLists.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
C++ library to parse/evaluate mathematical expressions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
cp %{SOURCE1} .
sed -i 's|\r||g' changelog.txt license.txt lesser.txt


%build
mkdir build
(
cd build
%cmake ..
make %{?_smp_mflags}
)


%install
%make_install -C build


%ldconfig_scriptlets


%files
%doc changelog.txt
%license license.txt lesser.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 0.3b-13
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3b-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 14 2015 Sandro Mani <manisandro@gmail.com> - 0.3b-4
- Rebuild (GCC5)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Sandro Mani <manisandro@gmail.com> - 0.3b-2
- Fix line endings

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 0.3b-1
- Initial package
