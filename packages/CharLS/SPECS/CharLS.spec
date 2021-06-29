Name:		CharLS
Version:	1.0
Release:	19%{?dist}
Summary:	An optimized implementation of the JPEG-LS standard
License:	BSD
URL:		https://github.com/team-charls/charls
# CharLS uses an interactive download link that asks you to accept the
# (BSD-like) license before obtaining the source code.
# You can find the download link at http://charls.codeplex.com/
Source0:	CharLS-source-1.0.zip
Patch0:		charls_add_cmake_install_target.patch
Patch1:		charls_add_sharedlib_soname.patch
Patch2:		charls_fix_tests.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake >= 2.6.0
BuildRequires:	dos2unix

%description
An optimized implementation of the JPEG-LS standard for loss less and
near loss less image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

JPEG-LS (ISO-14495-1/ITU-T.87) is a standard derived from the Hewlett Packard
LOCO algorithm. JPEG LS has low complexity (meaning fast compression) and high
compression ratios, similar to JPEG 2000. JPEG-LS is more similar to the old
loss less JPEG than to JPEG 2000, but interestingly the two different techniques
result in vastly different performance characteristics.

%prep
%setup -c -q

rm CharLS.vcproj
rm CharLS.sln

dos2unix *.h
dos2unix *.c*
dos2unix *.txt

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON\
	-Dcharls_BUILD_SHARED_LIBS:BOOL=ON\
       -DCMAKE_BUILD_TYPE:STRING="Release"\
       -DCMAKE_VERBOSE_MAKEFILE=ON\
       -DBUILD_TESTING=ON .

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
ctest .


%ldconfig_scriptlets


%files
%license License.txt
%{_libdir}/*.so.*


%package        devel
Summary:	Libraries and headers for CharLS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
CharLS Library Header Files and Link Libraries.

%files devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*
%{_libdir}/*.so

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.0-11
- Spec-file cleanups

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 3 2011 Mario Ceresa mrceresa@gmail.com CharLS 1.0-1
- Update to new version
- Applied patch to fix bug http://charls.codeplex.com/workitem/7823

* Wed Feb 17 2010 Mario Ceresa mrceresa@gmail.com CharLS 1.0-0.1.b
- Changed name schema to comply with pre-release packages

* Wed Feb 17 2010 Mario Ceresa mrceresa@gmail.com CharLS 1.0b-1
- Initial RPM Release
