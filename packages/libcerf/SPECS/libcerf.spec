Name:		libcerf
Version:	1.13
Release:	2%{?dist}
Summary:        A library that provides complex error functions

License:        MIT
URL:            https://jugit.fz-juelich.de/mlz/libcerf
Source0:        https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  cmake
# Required to build the documentation
BuildRequires:  perl-podlators
BuildRequires:  perl-Pod-Html

%description
libcerf is a self-contained numeric library that provides an efficient
and accurate implementation of complex error functions, along with
Dawson, Faddeeva, and Voigt functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-v%{version}
# Force cmake to use the paths passed at configure time
sed -i -e 's|${destination}/lib|${LIB_INSTALL_DIR}|' lib/CMakeLists.txt
sed -i -e 's|${destination}/lib|${LIB_INSTALL_DIR}|' CMakeLists.txt
sed -i -e 's|${prefix}/lib|@LIB_INSTALL_DIR@|' libcerf.pc.in


%build
# libcerf does not build in place, that is why we create a build dir
mkdir build; cd build
%cmake ..
%make_build


%install
cd build
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Move the documentation to the devel package
mv $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}/html $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-devel


%check
cd build
make cerftest


%files
%license COPYING
%doc README
%{_libdir}/*.so.1*

%files devel
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/doc/%{name}-devel/


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 José Matos <jamatos@fedoraproject.org> - 1.13-1
- update to 1.13
- update homepage and source urls

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 José Matos <jamatos@fedoraproject.org> - 1.11-1
- update to 1.11
- adds html documentation to the devel subpackage
- adds a pkgconfig .pc file

* Fri Nov  2 2018 José Matos <jamatos@fedoraproject.org> - 1.9-3
- build for all available fedora releases

* Fri Nov  2 2018 José Matos <jamatos@fedoraproject.org> - 1.9-2
- rebuild for all the supported releases

* Fri Oct 19 2018 José Matos <jamatos@fedoraproject.org> - 1.9-1
- update to 1.9

* Mon Oct 15 2018 José Matos <jamatos@fedoraproject.org> - 1.8-2
- add tests

* Sun Oct 14 2018 José Abílio Matos <jamatos@fedoraproject.org> - 1.8-1
- initial package
