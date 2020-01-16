Summary: Dans Example Autotools Program
Name: dacepsprogram
Version: 0.1.0
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/danielhams/daceps
Source: https://github.com/danielhams/daceps/releases/download/%{version}/program-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: dacepslibone-devel, dacepslibtwo-devel

Requires: dacepslibone, dacepslibtwo

%description
The is an example autotools program from daceps to demonstrate packaging
linking and dependencies.

%prep
%setup -q -n program-0.1.0

%build
%{configure}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

%files
%{_bindir}/program

%changelog
* Tue Jan 7 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
