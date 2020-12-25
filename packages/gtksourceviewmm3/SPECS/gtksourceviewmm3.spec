%global tarname gtksourceviewmm
%global api_ver 3.0

%global glibmm_version 2.46.1
%global gtkmm_version 3.18.0
%global gtksourceview_version 3.18.0

Name:           gtksourceviewmm3
Version:        3.18.0
Release:        9%{?dist}
Summary:        A C++ wrapper for gtksourceview3

License:        LGPLv2+
URL:            http://projects.gnome.org/gtksourceviewmm/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gtksourceviewmm/3.18/%{tarname}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= %{glibmm_version}
BuildRequires:  gtkmm30-devel >= %{gtkmm_version}
BuildRequires:  gtksourceview3-devel >= %{gtksourceview_version}
#BuildRequires:  doxygen graphviz

Requires:       glibmm24%{?_isa} >= %{glibmm_version}
Requires:       gtkmm30%{?_isa} >= %{gtkmm_version}
Requires:       gtksourceview3%{?_isa} >= %{gtksourceview_version}

%description
gtksourceviewmm is a C++ wrapper for the gtksourceview widget
library. It offers all the power of gtksourceview with an interface
familiar to c++ developers, including users of the gtkmm library


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.




#%%package        doc
#Summary:        Developer's documentation for the gtksourceviewmm3 library
#BuildArch:      noarch
#BuildRequires:  doxygen graphviz
#Requires:       gtkmm30-doc

#%%description      doc
#This package contains developer's documentation for the Gtksourceviewmm
#library. Gtksourceviewmm is the C++ API for the Gtksourceview library.

#The documentation can be viewed either through the devhelp
#documentation browser or through a web browser.


%prep
%setup -q -n %{tarname}-%{version}


%build
%configure --disable-static --without-docs
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT/usr/sgug/share/devhelp/books/gtksourceviewmm-3.0/gtksourceviewmm-3.0.devhelp2
rm -rf $RPM_BUILD_ROOT/usr/sgug/share/doc/*
#%%ldconfig_scriptlets


%files
%license COPYING
%doc README AUTHORS NEWS
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{tarname}-%{api_ver}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{tarname}-%{api_ver}.pc
%{_libdir}/%{tarname}-%{api_ver}


#%%files doc
#%%license COPYING
#%%doc %{_datadir}/devhelp/books/%{tarname}-%{api_ver}
#%%doc %{_docdir}/%{tarname}-%{api_ver}

%changelog
* Wed Nov 25 2020  HAL <notes2@gmx.de> - 3.18.0-9
- compiles on Irix 6.5 with sgug-rse gcc 9.2. 

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Set minimum version requirements
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0
- Minor spec file cleanup
- Don't ship large ChangeLog file
- Use license macro for the COPYING file

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.2.0-9
- Rebuilt for gcc5 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.2.0-5
- Rebuilt for gtksourceview3 soname bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Mar 28 2011 Krzesimir Nowak <qdlacz@gmail.com> - 2.91.9-1
- New upstream release.

* Tue Feb 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.91.5-2
- split doc into subpackage

* Fri Feb 11 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.91.5-1
- initial package

