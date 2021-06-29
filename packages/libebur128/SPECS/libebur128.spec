Name:           libebur128
Version:        1.2.4
Release:        2%{?dist}
Summary:        A library that implements the EBU R 128 standard for loudness normalization
License:        MIT
URL:            https://github.com/jiixyj/%{name}

Source0:        https://github.com/jiixyj/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake >= 2.8.11

%description
A library that implements the EBU R 128 standard for loudness normalization.

It implements M, S and I modes, loudness range measurement (EBU - TECH 3342),
true peak scanning and all sample-rates by recalculation of the filter
coefficients.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
# EPEL has CMake 2.8.11 but project requires 2.8.12
sed -i -e 's/2.8.12/2.8.11/g' CMakeLists.txt

%build
%cmake %{?_cmake_skip_rpath}
%make_build

%check
pushd test
make

%install
%make_install
find %{buildroot} -name '*.a' -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 1.2.4-1
- Update to 1.2.4.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Simone Caronni <negativo17@gmail.com> - 1.2.3-1
- Update to 1.2.3.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Simone Caronni <negativo17@gmail.com> - 1.2.2-1
- Update to 1.2.2.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-1
- First build.
