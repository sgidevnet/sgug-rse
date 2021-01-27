%global tarname goocanvas
%global apiver  2.0

Name:           goocanvas2
Version:        2.0.4
Release:        5%{?dist}
Summary:        A new canvas widget for GTK+ that uses cairo for drawing

License:        LGPLv2+
URL:            http://live.gnome.org/GooCanvas
Source0:        https://download.gnome.org/sources/goocanvas/2.0/goocanvas-%{version}.tar.xz

BuildRequires:  gettext, pkgconfig
BuildRequires:  gtk3-devel >= 2.91.3
BuildRequires:  cairo-devel >= 1.4.0
BuildRequires:  gobject-introspection-devel

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n goocanvas-%{version}


%build
# python GI wrapper is not enabled yet until i figure a proper way to package it
%configure --disable-static \
           --enable-python=no 

make %{?_smp_mflags}


%install
make install DESTDIR=%buildroot
find %buildroot -name '*.la' -exec rm -f {} ';'
%find_lang %{name}


#%%ldconfig_scriptlets


%files  -f %{name}.lang
%license COPYING
%doc README ChangeLog AUTHORS NEWS TODO
%{_libdir}/*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GooCanvas-2.0.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{tarname}-%{apiver}.pc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GooCanvas-2.0.gir

%changelog
* Wed Jan 27 2021  HAL <notes2@gmx.de> - 2.0.4-5
- compiles on Irix 6.5 with sgug-rse gcc 9.2. 

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Kalev Lember <klember@redhat.com> - 2.0.4-1
- Update to 2.0.4
- Co-own gobject-introspection and gtk-doc directories

* Thu Aug 31 2017 Kalev Lember <klember@redhat.com> - 2.0.3-1
- Update to 2.0.3
- Use license macro for COPYING

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.2-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Wed Aug 07 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 2.0.1-6.8f2c63git
- backport gobject introspection fixes from GNOME git
- fix FTBFS (RHBZ #992421)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.0.1-1
- upstream 2.0.1
- remove upstreamed patch and enable GIR

* Fri Feb 11 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.90.2-1
- initial package
