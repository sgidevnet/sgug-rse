Name:		spread-sheet-widget
Version:	0.3
Release:	3%{?dist}
Summary:	A library for Gtk+ which provides a spread sheet widget
License:	GPLv3+
URL:		https://www.gnu.org/software/ssw/
Source0:	https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz
Source1:	https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz.sig
Patch1:		spread-sheet-widget-0001-Install-the-pc-file-without-executable-permission.patch
Patch2:		spread-sheet-widget-0002-No-need-to-specify-gtk3-lib-in-pc-file.patch
Patch3:		spread-sheet-widget-0003-Generate-pc-file-in-a-standard-way.patch
Patch4:		spread-sheet-widget-0004-Link-library-against-GTK3-and-GLIB2-libs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	pkgconfig(glib-2.0) >= 2.44
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.18.0


%description
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2 dimensional tabular data in a manner similar to many
popular spread sheet programs.

The design follows the model-view-controller paradigm and is of complexity O(1)
in both time and space. This means that it is efficient and fast even for very
large data.

Features commonly found in graphical user interfaces such as cut and paste,
drag and drop and row/column labelling are also included.


%package devel
Summary: The development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
Additional header files for development with %{name}.


%prep
%autosetup -p1
autoreconf -ivf


%build
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
rm -f %{buildroot}%{_infodir}/dir


%check
make check


%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*


%files devel
%{_includedir}/ssw-axis-model.h
%{_includedir}/ssw-sheet-axis.h
%{_includedir}/ssw-sheet.h
%{_infodir}/%{name}.info*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.3-2
- Fix pc-file

* Wed Feb 06 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.3-1
- Initial build
