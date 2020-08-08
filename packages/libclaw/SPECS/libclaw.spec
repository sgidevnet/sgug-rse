Name:           libclaw
Version:        1.7.4
Release:        26%{?dist}
Summary:        C++ Library of various utility functions
License:        LGPLv2
URL:            http://libclaw.sourceforge.net/
Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         libclaw-1.6.1-nostrip.patch
Patch1:         libclaw-1.7.4-libdir.patch
Patch2:         libclaw-1.7.4-gcc62.patch
# Make documentation the same on different arches
Patch3:         libclaw-1.7.4-noarch.patch
# Fix errors found by GCC 7 (and Clang)
Patch4:         libclaw-1.7.4-gcc7.patch
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake
#BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  boost-devel

%description
Claw (C++ Library Absolutely Wonderful) is a C++ library of various utility
functions. In doesn't have a particular objective but being useful to
anyone.


%package devel
Summary:        Development files for Claw library
Requires:       %{name} = %{version}-%{release}
Requires:       cmake
Requires:       boost-devel%{?_isa}
Requires:       libjpeg-devel%{?_isa}
Requires:       libpng-devel%{?_isa}

%description devel
This package contains files needed to develop and build software against
Claw (C++ Library Absolutely Wonderful).


%package doc
Summary:        Documentation for Claw library
BuildArch:      noarch

%description doc
This package contains documentation for Claw (C++ Library Absolutely
Wonderful).


%prep
%setup -q
%patch0 -p1 -b .nostrip
%patch1 -p1 -b .libdir
%patch2 -p1 -b .gcc62
%patch3 -p1 -b .noarch
%patch4 -p1 -b .gcc7


%build
%cmake .
make %{?_smp_mflags} VERBOSE=1
find examples -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done


%install
make install DESTDIR=%{buildroot} VERBOSE=1
%find_lang %{name}


#%%ldconfig_scriptlets


%files -f %{name}.lang
%license COPYING
%{_libdir}/*.so.*


%files devel
%{_bindir}/claw-config
%{_includedir}/claw
%{_libdir}/cmake/%{name}
%{_libdir}/*.so
%exclude %{_libdir}/*.a


%files doc
%license COPYING
%doc %{_datadir}/doc/libclaw1
%doc examples


%changelog
* Wed Jul 08 2020  HAL <notes2@gmx.de> - 1.7.4-26
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.4-23
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.7.4-19
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jonathan Wakely <jwakely@redhat.com> - 1.7.4-17
- Rebuilt for Boost 1.63 and patched for GCC 7

* Thu Dec 29 2016 Orion Poplawski <orion@cora.nwra.com> - 1.7.4-16
- Install cmake files in arch specific dirs
- Put documentation into separate noarch sub-package
- Require needed devel packages in -devel sub-package
- Use %%license

* Mon Nov 28 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.7.4-15
- Fix FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.7.4-13
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.7.4-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.7.4-10
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.4-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.4-7
- Rebuilt for GCC 5 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.7.4-6
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.7.4-3
- Rebuild for boost 1.55.0

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.7.4-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sun Aug 18 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.7.4-1
- Rebase
- Fix FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.7.0-9
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.7.0-7
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-5
- Rebuilt for c++ ABI breakage

* Sun Feb  5 2012 Tom Callaway <spot@fedoraproject.org> - 1.7.0-4
- fix png.hpp to include zlib.h

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7.0-2
- Rebuild for new libpng

* Thu Aug 25 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.0-1
- update to 1.7.0

* Mon Apr 18 2011 Tom Callaway <spot@fedoraproject.org> - 1.6.1-1
- update to 1.6.1

* Fri Feb 11 2011 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-7
- Fix Rawhide build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.5.4-5
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.4-4
- Fix wrong return type of 'claw::log_system::operator<<'
- Fix incorrect return type in basic_socket.

* Fri Oct 23 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-3
- Really fix the examples encoding

* Fri Oct 02 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-2
- Merge in changes from Xavier Bachelot's package:
- More sensible Group name
- Fix libdir name for 64bit archs
- Add examples to documentation
- Fix examples encoding
- Let -devel require cmake

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5.4-1
- Initial packaging
