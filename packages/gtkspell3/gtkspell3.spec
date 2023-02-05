Name:           gtkspell3
Version:        3.0.10
Release:        4%{?dist}
Summary:        On-the-fly spell checking for GtkTextView widgets

License:        GPLv2+
URL:            http://gtkspell.sourceforge.net/
Source0:        http://downloads.sourceforge.net/gtkspell/gtkspell3-%{version}.tar.xz

BuildRequires:  enchant2-devel
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  vala
BuildRequires:  iso-codes-devel

Requires:       iso-codes

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use GtkSpell API version 3.0.


%prep
%autosetup


%build
%configure --disable-static --enable-vala
%make_build V=1


%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang gtkspell3


%files -f gtkspell3.lang
%doc AUTHORS README
%license COPYING
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib
%{_libdir}/libgtkspell3-3.so.*

%files devel
%doc %{_datadir}/gtk-doc/
%{_includedir}/gtkspell-3.0/
%{_libdir}/libgtkspell3-3.so
%{_libdir}/pkgconfig/gtkspell3-3.0.pc
%{_datadir}/gir-1.0/GtkSpell-3.0.gir
%{_datadir}/vala/vapi/gtkspell3-3.0.vapi
%{_datadir}/vala/vapi/gtkspell3-3.0.deps


%changelog
* Wed Nov 25 2020  HAL <notes2@gmx.de> - 3.0.10-4
- compiles on Irix 6.5 with sgug-rse gcc 9.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.0.10-3
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Sandro Mani <manisandro@gmail.com> - 3.0.10-1
- Update to 3.0.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Sandro Mani <manisandro@gmail.com> - 3.0.9-1
- Update to 3.0.9

* Sun Apr 03 2016 Sandro Mani <manisandro@gmail.com> - 3.0.8-1
- Update to 3.0.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Sandro Mani <manisandro@gmail.com> - 3.0.7-1
- Update to 3.0.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.6-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Sandro Mani <manisandro@gmail.com> - 3.0.6-1
- Update to 3.0.6

* Sat Apr 19 2014 Sandro Mani <manisandro@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Thu Sep 26 2013 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.3-2
- Add iso-codes requires and iso-codes-devel BR

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Thu Mar 07 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-2
- Merge -vala into -devel package

* Wed Mar 06 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2
- Adds vala bindings

* Sat Feb 09 2013 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Thu Nov 15 2012 Kalev Lember <kalevlember@gmail.com> - 3.0.0-1
- Initial gtkspell3 packaging, based on Fedora's gtkspell package
