Name:           gtkimageview
Version:        1.6.4
Release:        21%{?dist}
Summary:        Simple image viewer widget

License:        LGPLv2+
URL:            http://trac.bjourne.webfactional.com
# To download directly, use this URL:
# Source0:        http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/gtkimageview-%{version}.tar.gz?format=raw
Source0:        gtkimageview-%{version}.tar.gz
# Fix FTBFS. https://bugzilla.redhat.com/show_bug.cgi?id=1307603
Patch0:         gtkimageview-1.6.4-no-werror.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel >= 2.8.0
BuildRequires:  gtk-doc >= 1.0
BuildRequires:  pkgconfig

%description
GtkImageView is a simple image viewer widget for GTK. It makes writing image
viewing and editing applications easy.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .no-werror


%build
%configure --disable-static
make %{?_smp_mflags}
make %{?_smp_mflags} check


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gtkimageview.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 1.6.4-18
- require gcc for building

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Nils Philippsen <nils@redhat.com> - 1.6.4-13
- don't use -Werror to fix FTBFS (#1307603)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 1.6.4-5
- rebuild for gcc 4.7

* Mon Nov 07 2011 Nils Philippsen <nils@redhat.com> - 1.6.4-4
- rebuild (libpng)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Nils Philippsen <nils@redhat.com> - 1.6.4-2
- don't require gtk-doc but own %%{_datadir}/gtk-doc (#604368, #604169)

* Wed Jun 02 2010 Nils Philippsen <nils@redhat.com> - 1.6.4-1
- version 1.6.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Nils Philippsen <nils@redhat.com> - 1.6.3-1
- version 1.6.3

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 07 2008 Nils Philippsen <nphilipp@redhat.com> - 1.6.1-2
- don't use URL for source since it doesn't download the source directly

* Fri Jul 04 2008 Nils Philippsen <nphilipp@redhat.com> - 1.6.1-1
- version 1.6.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-2
- Autorebuild for GCC 4.3

* Wed Jan 02 2008 Nils Philippsen <nphilipp@redhat.com> - 1.5.0-1
- version 1.5.0
- initial build
