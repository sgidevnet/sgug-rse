Name: curlpp
Version: 0.8.1
Release: 9%{?dist}
Summary: A C++ wrapper for libcURL

License: MIT
URL: http://curlpp.org/
Source0:  https://github.com/jpbarrette/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# patches for old curlpp 0.7.3, not needed for new curlpp > 0.8.1
# ARM 64
#Patch0:  curlpp-aarch64.patch
# fix FTBFS - rhbz 1106103
#Patch1:  curlpp-0.7.3-gcc49.patch

BuildRequires: boost-devel
BuildRequires: curl-devel
BuildRequires: cmake
BuildRequires: gcc-c++

%description
cURLpp is a C++ wrapper for libcURL.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: boost-devel
Requires: curl-devel
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

# Convert CRLF line endings to LF in the examples
for file in examples/*.cpp
do
	sed 's/\r//' $file > $file.new && \
	touch -r $file $file.new && \
	mv $file.new $file
done

# remove deps on global.h which in turn pulls in config.h
sed -i '28 d' include/curlpp/Types.hpp


%build
%cmake .
make %{?_smp_mflags} CPPFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot}

# Unwanted library files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a


%ldconfig_scriptlets

%check
ctest -V %{?_smp_mflags}

%files
%doc doc/AUTHORS doc/TODO
%license doc/LICENSE
%{_libdir}/libcurlpp.so.*


%files devel
%doc examples/*.cpp examples/README doc/guide.*
%{_bindir}/curlpp-config
%{_includedir}/curlpp/
%{_includedir}/utilspp/
%{_libdir}/libcurlpp.so
%{_libdir}/pkgconfig/curlpp.pc



%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.1-6
- Add g++ as BRs
- Update upstream URL

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.8.1-2
- Rebuilt for Boost 1.64

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.1-1
- Rebuilt for new upstream release 0.8.1, using cmake to build
- Fixes FTBFS rhbz#1307415 rhbz#1423319 and rhbz#1426168

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.3-29
- Spec cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.3-26
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.7.3-25
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.7.3-23
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.3-21
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.7.3-20
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.7.3-18
- Fix FTBFS with gcc-4.9 (#1106103)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.7.3-16
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.7.3-14
- Rebuild for boost 1.54.0

* Sun Mar 24 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.7.3-13
- Complete spec

* Sun Mar 24 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.7.3-12
- Add patch for ARM 64 support
- https://bugzilla.redhat.com/show_bug.cgi?id=925210

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.3-11
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.3-10
- Rebuild for Boost-1.53.0

* Mon Jul 23 2012 Veeti Paananen <veeti.paananen@rojekti.fi> - 0.7.3-9
- Fix build 

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Veeti Paananen <veeti.paananen@rojekti.fi> - 0.7.3-7
- Remove config.h

* Fri Jan 27 2012 Veeti Paananen <veeti.paananen@rojekti.fi> - 0.7.3-6
- Added missing configuration header file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Veeti Paananen <veeti.paananen@rojekti.fi> - 0.7.3-4
- Changed libcurl-devel dependency to curl-devel for EPEL5 compatibility

* Tue Jul 19 2011 Veeti Paananen <veeti.paananen@rojekti.fi> - 0.7.3-3
- Removed wildcard for selecting pkgconfig file
- Added trailing slash for directories in file listing
- Added doc/guide.pdf to development documentation

* Tue Jul 19 2011 Veeti Paananen <veeti.paananen@rojekti.fi> - 0.7.3-2
- Added boost-devel, libcurl-devel and pkgconfig as requirements to devel
  subpackage.
- Complete line-ending conversion once all steps are done
- Added default file attributes to devel subpackage
- Added verbosity to file selectors

* Mon Jul 18 2011 Veeti Paananen <veeti.paananen@rojekti.fi> - 0.7.3-1
- Initial package.
