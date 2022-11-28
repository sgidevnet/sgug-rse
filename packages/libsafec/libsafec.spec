Name:		libsafec
Version:	3.3
Release:	5%{?dist}
Summary:	Safec fork with all C11 Annex K functions

License:	MIT
URL:		https://github.com/rurban/safeclib
Source0:	https://github.com/rurban/safeclib/releases/download/v03032018/libsafec-03032018.0-g570fa5.tar.gz
# Fixes linker failer: https://github.com/rurban/safeclib/issues/55
Patch0:		pic_flag.patch
# Fixes pkgconfig include directory path
Patch1:		pkgconfig_include.patch

BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
Safec fork with all C11 Annex K functions

%package -n libsafec-devel
Summary:	Development packages for libsafec
Requires:	libsafec%{?_isa} = %{version}-%{release}

%description -n libsafec-devel
Development files for libsafec

%package -n libsafec-check
Summary:	Finds unsafe APIs

%description -n libsafec-check
Finds unsafe APIs


%prep
%setup -qn libsafec-03032018.0-g570fa5

%patch0 -p1
%patch1 -p1

%build
autoreconf -Wall --install
%configure --disable-static --disable-doc --enable-strmax=0x8000
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete


%files -n libsafec
%license COPYING
%doc README
%{_libdir}/libsafec-3.3.so.*

%files -n libsafec-devel
%{_libdir}/libsafec-3.3.so
%{_libdir}/pkgconfig/safec-3.3.pc
%{_includedir}/libsafec

%files -n libsafec-check
%license COPYING
%{_bindir}/check_for_unsafe_apis
%{_mandir}/man1/check_for_unsafe_apis.1.*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Juston Li <juston.li@intel.com> - 3.3-3
- Fix versioning, just use simple 3.3 version
- Add comments for packages
- Capitalize summary/description
- use make_build macro
- remove ldconfig for f28
- remote defattr
- remove redundent include header files
- remote .la file

* Mon Jul 02 2018 Juston Li <juston.li@intel.com> - 03032018-2
- Add pkgconfig_include.patch to fix pkgconfig include path

* Mon Jun 25 2018 Juston Li <juston.li@intel.com> - 03032018-1
- Initial spec
