Name:           sage
Version:        0.2.0
Release:        21%{?dist}
Summary:        OpenGL extensions library using SDL

License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/sage
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz
Patch0:         sage-0.1.2-noopt.patch

BuildRequires:  gcc
BuildRequires:  SDL-devel

%description
Sage is an OpenGL extensions library using SDL. It aims to simplify the use of
checking for and loading OpenGL extensions in an application.


%package devel
Summary:        Development files for sage
Requires: pkgconfig %{name} = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use sage.



%prep
%setup -q
touch -r configure.ac configure.ac.stamp
%patch0 -p0
touch -r configure.ac.stamp configure.ac
rm -f sage/glxext_sage.h
rm -f sage/wglext_sage.h


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la

%check
# There are no tests yet, but upstream tends to be good about adding 
# them.  This is a placeholder for when upstread finally adds the tests.
make %{?_smp_mflags} check



%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/lib%{name}.so.*


%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.gz


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Wart <wart at kobold.org> 0.2.0-3
- Rebuild for gcc 4.3

* Mon Aug 27 2007 Wart <wart at kobold.org> 0.2.0-2
- License tag clarification

* Wed Feb 7 2007 Wart <wart at kobold.org> 0.2.0-1
- Update to 0.2.0

* Mon Aug 28 2006 Wart <wart at kobold.org> 0.1.2-5
- Rebuild for Fedora Extras

* Wed Jul 26 2006 Wart <wart at kobold.org> 0.1.2-4
- Added 'make check' to test section.  Even though it doesn't do anything,
  it also doesn't generate an error.

* Sat Jul 15 2006 Wart <wart at kobold.org> 0.1.2-3
- Re-add --disable-static and remove the unnecessary rm of the .a file.
- Added patch to remove -O3 compiler flag so as not to conflict
  with $RPM_OPT_FLAGS

* Fri Jul 14 2006 Wart <wart at kobold.org> 0.1.2-2
- Added Requires: pkgconfig to -devel subpackage
- Remove --disable-static since libtool seems to ignore it.
- Change license to LGPL
- Use _mandir for man page locations
- Added empty %%check section

* Thu Jun 15 2006 Wart <wart at kobold.org> 0.1.2-1
- Initial spec file for Fedora Extras
