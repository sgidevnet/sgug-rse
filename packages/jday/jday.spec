Name:		jday
Version:        2.4
Release:        22%{?dist}
Summary:        A simple command to convert calendar dates to julian dates
License:        BSD
URL:            http://sourceforge.net/projects/jday/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

%description
A simple command to convert calendar dates to julian dates. 
Quite useful in timing situations where you need elapsed time between dates. 
Also useful for astronomy applications. 

%package devel
Summary:        Development files for jday
Requires:       %{name} = %{version}-%{release}
BuildRequires:  gcc-c++
BuildRequires:	pkgconfig

%description devel
Contains library and header files for developing applications that use jday

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc ChangeLog README AUTHORS NEWS
%{_bindir}/dbd
%{_bindir}/j2d
%{_bindir}/jday
%{_mandir}/man1/jday.1.gz
%{_libdir}/libjday.so.2.0.4
%{_libdir}/libjday.so.2

%files devel
%{_includedir}/jday.h
%{_libdir}/libjday.so
%{_libdir}/pkgconfig/jday.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 2.4-21
- Enable f30 builds by adding gcc-c++

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4-3
- Autorebuild for GCC 4.3

* Sat Jan 12 2007 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 2.4-2
- Changed the groups to correct ones

* Thu Jan 03 2007 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 2.4-1
- Changed ldconfig,URL and other things to make package compliant with 
  fedora packaging standards

* Thu Jan 03 2007 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 2.4-0
- Initial version.

