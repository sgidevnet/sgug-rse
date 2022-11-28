Name: libmobi
Version: 0.4
Release: 4%{?dist}
Summary: Library for handling Kindle (MOBI) formats of ebook documents
License: LGPLv3+
URL: https://github.com/bfabiszewski/libmobi
Source0: https://github.com/bfabiszewski/libmobi/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: zlib-devel

%description
Features:
  * reading and parsing:
    - some older text Palmdoc formats (pdb),
    - Mobipocket files (prc, mobi),
    - newer MOBI files including KF8 format (azw, azw3),
    - Replica Print files (azw4)
  * recreating source files using indices
  * reconstructing references (links and embedded) in html files
  * reconstructing source structure that can be fed back to kindlegen
  * reconstructing dictionary markup (orth, infl tags)
  * writing back loaded documents
  * metadata editing
  * handling encrypted documents

%package tools
Summary: libmobi CLI tools
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
This is the CLI tools for libmobi package.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup

%build
autoreconf -vfi
%configure \
  --disable-static \
  --enable-encryption \
  --with-libxml2 \
  --with-zlib
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%files
%license COPYING
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*

%files tools
%{_bindir}/mobi*
%{_mandir}/man1/mobi*.1.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.4-2
- Rebuild with fixed binutils

* Fri Jul 27 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 0.4-1
- Initial import
