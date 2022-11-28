%global svnrev 316

Name:           libg15render
Version:        1.3.0
Release:        0.2.svn%{svnrev}%{?dist}
Summary:        Library for rendering bitmaps for the Logitech G15 keyboard LCD
License:        GPLv2+
URL:            https://sourceforge.net/projects/g15tools/
# Upstream is dead and never did a proper release of 1.3.0, use a svn snapshot
# as Debian and other distros are doing
Source0:        ftp://ftp.nluug.nl/pub/os/Linux/distr/debian/pool/main/libg/libg15render/libg15render_%{version}~svn%{svnrev}.orig.tar.gz
BuildRequires:  gcc libtool freetype-devel

%description
libg15render is a library for rendering bitmaps in the format expected
by the LCD screen on the Logitech G15 (and similar) keyboards.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}.svn%{svnrev}
autoreconf -ivf


%build
%configure --disable-static --enable-ttf
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Nuke docs installed in wrong location
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-1.3


%files
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.1*
%{_datadir}/g15tools

%files devel
%{_bindir}/g15fontconvert
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/libg15render.3*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.2.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Hans de Goede <hdegoede@redhat.com> - 1.3.0-0.1.svn316
- Initial libg15render Fedora package
