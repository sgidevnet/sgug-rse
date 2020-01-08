Summary: Dans Example Autotools Library One
Name: dacepslibone
Version: 0.1.0
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/danielhams/daceps
Source: https://github.com/danielhams/daceps/releases/download/%{version}/libraryone-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

%description
The is an example autotools library from daceps to demonstrate packaging
linking and dependencies.

%package devel
Summary: Header files and libraries for the dacepslibone library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
dacepslibone-devel contains the header files and libraries needed
to develop programs that use the dacepslibone library.

%prep
%setup -q -n libraryone-0.1.0

%build
%{configure}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
rm $RPM_BUILD_ROOT/%{_libdir}/liblibraryone-0.1.la

%files
%{_libdir}/liblibraryone-0.1.so.*

%files devel
%{_libdir}/liblibraryone-0.1.a
%{_libdir}/liblibraryone-0.1.so
%{_libdir}/pkgconfig/liblibraryone-0.1.pc
%{_includedir}/libraryone-0.1


%changelog
* Tue Jan 7 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
