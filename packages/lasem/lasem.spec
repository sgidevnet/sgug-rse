%global apiver 0.4

Name:           lasem
Version:        0.4.3
Release:        12%{?dist}
Summary:        A library for rendering SVG and Mathml, implementing a DOM like API

License:        LGPLv2+ and GPLv2+
URL:            https://wiki.gnome.org/Projects/Lasem
Source0:        http://download.gnome.org/sources/%{name}/%{apiver}/%{name}-%{version}.tar.xz
Patch100:       lasem.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
Provides:       bundled(itex2mml) = 1.4.5

%description
Lasem is a library for rendering SVG and Mathml, implementing a DOM like API.
It's based on GObject and use Pango and Cairo for the rendering.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        render
Summary:        Simple MathML converter
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    render
Simple application, which is able to convert a Mathml, a latex math or a SVG
file to either a PNG, PDF or SVG image.


%prep
%autosetup -p1


%build
%configure --disable-static \
           --disable-silent-rules \
           --enable-gtk-doc-html=no
%make_build


%install
%make_install
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.la' -delete -print

#docs are installed using %%doc
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%find_lang %{name}-%{apiver}

#%%ldconfig_scriptlets


%files -f %{name}-%{apiver}.lang
%doc AUTHORS NEWS README
%license COPYING itex2mml/COPYING.itex2MML
%{_libdir}/girepository-1.0/Lasem-%{apiver}.typelib
%{_libdir}/lib%{name}-%{apiver}.so.*

%files devel
%{_includedir}/%{name}-%{apiver}
%{_libdir}/lib%{name}-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%{_datadir}/gir-1.0/Lasem-%{apiver}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/%{name}-%{apiver}

%files render
%{_bindir}/%{name}-render-%{apiver}
%{_mandir}/man1/%{name}-render-%{apiver}.1*

%changelog
* Wed Jan 27 2020  HAL <notes2@gmx.de> - 0.4.3-12
- initial commit, compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-9
- Removed ldconfig scriptlets as per
  https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 27 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-4
- Added itex2mml information

* Fri Jul 08 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-3
- Incorporated further review feedback

* Thu Jul 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-2
- Incorporated some of the review feedback

* Tue Jun 21 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.3-1
- Initial RPM release
