Name:		SDL2_ttf
Version:	2.0.15
Release:	2%{?dist}
Summary:	TrueType font rendering library for SDL2
License:	zlib
URL:		https://www.libsdl.org/projects/SDL_ttf/
Source0:	%{url}release/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:	SDL2-devel
BuildRequires:  libGL-devel
BuildRequires:	freetype-devel
BuildRequires:	zlib-devel

%description
This library allows you to use TrueType fonts to render text in SDL2
applications.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	SDL2-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
rm -rf external
# Fix end-of-line encoding
sed -i 's/\r//' README.txt CHANGES.txt COPYING.txt

%build
%configure --disable-dependency-tracking --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete -print

#%%ldconfig_scriptlets

%files
%license COPYING.txt
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL2/*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Apr 08 2021  HAL <notes2@gmx.de> - 2.0.15-2
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Tom Callaway <spot@fedoraproject.org> - 2.0.15-1
- update to 2.0.15

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.14-2
- add libGL-devel to BRs

* Tue Feb  2 2016 Tom Callaway <spot@fedoraproject.org> - 2.0.14-1
- update to 2.0.14

* Sun Jan 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.13-1
- Update to 2.0.13 (RHBZ #1296754)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 2 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.12-2
- delete external directory to drop bundles
- do not own /usr/include/SDL2
- fix unused-direct-shlib-dependency

* Mon Nov 25 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.12-1
- initial package
