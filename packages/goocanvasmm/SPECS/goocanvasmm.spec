%global  api_ver 1.0

Name:           goocanvasmm
Version:        0.15.4
Release:        22%{?dist}

Summary:        C++ interface for goocanvas

License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.15/%{name}-%{version}.tar.bz2
Patch0:         goocanvasmm-0.15.4-doctooldir.patch

BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= 2.14.2
BuildRequires:  gtkmm24-devel >= 2.22.0
BuildRequires:  goocanvas-devel >= 0.15
BuildRequires:  mm-common >= 0.9.5


%description
This package provides a C++ interface for goocanvas. It is a
subpackage of the gtkmm project. The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.


%package        devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtkmm24-devel
Requires:       goocanvas-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer documentation for %{name}
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:      noarch
%endif
#BuildRequires:  doxygen graphviz
Requires:       gtkmm24-docs

%description      doc
This package contains developer's documentation for the goocanvasmm2
library. Goocanvasmm2 is the C++ API for the goocanvas graphics library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

If using a web browser the documentation is at
/usr/share/doc/%{tarname}-%{api_ver}

%prep
%setup -q
%patch0 -p1


%build
%configure --enable-shared
make %{?_smp_mflags}
# Build documentation
#(cd doc/reference; doxygen -u 2> /dev/null)


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'



#%%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*


%files devel
%{_includedir}/%{name}-%{api_ver}
%{_libdir}/%{name}-%{api_ver}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-%{api_ver}.pc

%files doc
%doc COPYING
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}
%doc %{_docdir}/%{name}-%{api_ver}


%changelog
* Wed Sep 16 2020  HAL <notes2@gmx.de> - 0.15.4-22
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.15.4-13
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.15.4-6
- Rebuild for new libpng

* Mon Jul 04 2011 Karsten Hopp <karsten@redhat.com> 0.15.4-5
- buildrequire mm-common
- fix pkg-config call to figure out doctooldir

* Mon Feb 28 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.15.4-4
- bump release

* Sun Feb 20 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.15.4-3
- add doc sub-package and fix documentation handling

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.15.4-1
- Update to upstream 0.15.4

* Sun Sep 03 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.15.3-1
- Update to upstream 0.15.3

* Mon Apr 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.15.2-1
- Update to upstream 0.15.2

* Mon Apr 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.15.1-1
- Update to upstream 0.15.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Denis <denis@poolshark.org> - 0.14.0-1
- Update to upstream 0.14.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Denis Leroy <denis@poolshark.org> - 0.13.0-1
- Update to upstream 0.13.0

* Wed Sep  3 2008 Denis Leroy <denis@poolshark.org> - 0.9.0-1
- Update to upstream 0.9.0

* Fri Jul 11 2008 Denis Leroy <denis@poolshark.org> - 0.6.0-1
- Update to upstream 0.6.0
- Updated BRs

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-3
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Denis Leroy <denis@poolshark.org> - 0.4.0-2
- Added graphviz dep, fixed doxygen warning

* Sun Nov 25 2007 Denis Leroy <denis@poolshark.org> - 0.4.0-1
- Initial version

