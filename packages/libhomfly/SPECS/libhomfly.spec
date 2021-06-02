Name:           libhomfly
Version:        1.02r6
Release:        3%{?dist}
Summary:        Library to compute the homfly polynomial of a link

License:        Unlicense
URL:            https://github.com/miguelmarco/%{name}
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gc-devel
BuildRequires:  gcc

%description
This is a conversion of the program written by Robert J Jenkins Jr into
a shared library.  It accepts as entry a character string, formatted in
the same way as the input files that the original code used (see the
documentation).  The returned value is the string that the original
program would print on screen.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install

# We do not want the libtool files
rm %{buildroot}%{_libdir}/*.la

%check
make check

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*

%files devel
%{_includedir}/homfly.h
%{_libdir}/%{name}.so

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02r6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02r6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 1.02r6-1
- New upstream version

* Wed Oct 24 2018 Jerry James <loganjerry@gmail.com> - 1.02r5-1
- Initial RPM
