Name:           libGL
Version:        1.2
Release:        1%{?dist}
Summary:        Irix OpenGL library
License:	Proprietary

Source0: gl.pc

Provides: libGL.so
Provides: libGLcore.so

%description
Irix system OpenGL libraries and headers

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:	libGL-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
# nothinbg to do

%build
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
cp %{SOURCE0} %{buildroot}/%{_libdir}/pkgconfig/gl.pc

%install
# nothing to do

%clean
# nohting to do

%files
# nothing

%files devel
%{_libdir}/pkgconfig/gl.pc

%changelog
* Fri Jan 1 2021 Julien Maerten <julien@3dw.org> - 1.2-1
- Initial packaging for libGL
