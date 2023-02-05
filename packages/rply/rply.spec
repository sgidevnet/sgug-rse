Name:		rply
Version:	1.1.2
Release:	13%{?dist}
Summary:	A library to read and write PLY files
License:	MIT
URL:		http://www.tecgraf.puc-rio.br/~diego/professional/rply/
Source0:	http://www.tecgraf.puc-rio.br/~diego/professional/rply/%{name}-%{version}.tar.gz
Source1:	rply_CMakeLists.txt
Source2:	RPLYConfig.cmake.in
Source3:	rply_cmake_export_cmakelists.txt

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake >= 2.6.0


%description
RPly is a library that lets applications read and write PLY files.
The PLY file format is widely used to store geometric information, such as 3D
models, but is general enough to be useful for other purposes.

RPly is easy to use, well documented, small, free, open-source, ANSI C, 
efficient, and well tested. The highlights are:

* A callback mechanism that makes PLY file input straightforward;
* Support for the full range of numeric formats;
* Binary (big and little endian) and text modes are fully supported;
* Input and output are buffered for efficiency;
* Available under the MIT license for added freedom. 

%prep
%setup -q

# Add CMakeLists.txt file
cp %{SOURCE1} CMakeLists.txt

# Add CMake detection modules
mkdir -p CMake/export
mkdir -p CMake/Modules
cp %{SOURCE2} CMake/Modules/
cp %{SOURCE3} CMake/export/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"\
       -DCMAKE_VERBOSE_MAKEFILE=ON .

make %{?_smp_mflags}

iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/rplyConfig.cmake

%ldconfig_scriptlets


%files
%doc LICENSE
%doc manual/*
%{_libdir}/*.so.*
%{_bindir}/*


%package        devel
Summary:	Libraries and headers for rply
Requires:	%{name} = %{version}-%{release}

%description devel

Rply Library Header Files and Link Libraries

%files devel
%doc LICENSE
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*
%{_libdir}/*.so
%dir %{_datadir}/%{name}/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Mario Ceresa mrceresa@gmail.com rply 1.1.2-1
- Update to latest upsteam version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Richard Hughes <rhughes@redhat.com> - 1.1.1-1
- Update to latest upstream version.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 21 2010 Mario Ceresa mrceresa@gmail.com rply 1.01-3
- Added CMake modules to detect the package

* Thu Mar 04 2010 Mario Ceresa mrceresa@gmail.com rply 1.01-2
- Fixed problems detected in https://bugzilla.redhat.com/show_bug.cgi?id=570258#c2

* Wed Mar 03 2010 Mario Ceresa mrceresa@gmail.com rply 1.01-1
- Initial RPM Release
