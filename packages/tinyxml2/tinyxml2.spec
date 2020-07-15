Name:           tinyxml2
Version:        7.0.1
Release:        3%{?dist}
Summary:        Simple, small and efficient C++ XML parser

License:        zlib
URL:            https://github.com/leethomason/tinyxml2
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 2.6
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrated into other programs. It uses a Document Object Model
(DOM), meaning the XML data is parsed into a C++ objects that can be
browsed and manipulated, and then written to disk or another output stream.

TinyXML-2 doesn't parse or use DTDs (Document Type Definitions) nor XSLs
(eXtensible Stylesheet Language).

TinyXML-2 uses a similar API to TinyXML-1, But the implementation of the
parser was completely re-written to make it more appropriate for use in a
game. It uses less memory, is faster, and uses far fewer memory allocations.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with the %{name} library.

%prep
%autosetup
chmod -c -x *.cpp *.h

%build
%cmake . -B%{_vpath_builddir} -DBUILD_STATIC_LIBS=OFF
%make_build -C %{_vpath_builddir}

# Library tests were disabled in 3.0.0
#%check
#cd objdir
#make test
#export LD_LIBRARY_PATH=`pwd`
#./test

# and partially re-enabled in 6.0.0
%check
%make_build test -C %{_vpath_builddir}

%install
%make_install -C %{_vpath_builddir}

#%%ldconfig_scriptlets

%files
%doc readme.md
%{_libdir}/lib%{name}.so.7*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
* Sun Jun 07 2020  Alexander Tafarte <notes2@gmx.de> - 7.0.1-4 
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.1-1
- Update to 7.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.0.0-2
- Switch to %%ldconfig_scriptlets

* Mon Jan 22 2018 François Cami <fcami@fedoraproject.org> - 6.0.0-1
- Update to latest upstream (rhbz#1357711)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 21 2016 Rich Mattes <richmattes@gmail.com> - 3.0.0-1
- Update to release 3.0.0 (rhbz#1202166)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4.20140914git5321a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3.20140914git5321a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-2.20140914git5321a0e
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 05 2015 François Cami <fcami@fedoraproject.org> - 2.2.0-1.20140914git5321a0e
- Update to 2.2.0.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4.20140406git6ee53e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3.20140406git6ee53e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 François Cami <fcami@fedoraproject.org> - 2.1.0-2.20140406git6ee53e7
- Bump release and make it build (switch GNUInstallDirs.cmake from sources to git).

* Sat May 17 2014 François Cami <fcami@fedoraproject.org> - 2.1.0-1.20140406git6ee53e7
- Update to 2.1.0.

* Mon Oct 14 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.11-4.20130805git0323851
- Patch to build in EPEL branches.

* Mon Aug 12 2013 François Cami <fcami@fedoraproject.org> - 1.0.11-3.20130805git0323851
- Fixes by Susi Lehtola: build in a separate directory and don't build anything static.

* Mon Aug 12 2013 François Cami <fcami@fedoraproject.org> - 1.0.11-2.20130805git0323851
- Fixes suggested by Ville Skyttä: drop -static, add check, etc.

* Sat Aug 10 2013 François Cami <fcami@fedoraproject.org> - 1.0.11-1.20130805git0323851
- Initial package.

