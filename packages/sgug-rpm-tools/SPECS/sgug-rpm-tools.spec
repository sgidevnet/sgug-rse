Summary: SGUG RPM Tools
Name: sgug-rpm-tools
Version: 0.1.0
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/sgidevnet/sgug-rpm-tools
Source: https://github.com/sgidevnet/sgug-rpm-tools/releases/download/v%{version}/sgug-rpm-tools-%{version}.tar.gz

BuildRequires: g++
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: rpm-build, rpm-devel

Requires: rpm, rpm-build

%description
Some utility programs to help with release / dependency management.

%prep
%setup -q

%build
%{configure}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

%files
%{_bindir}/sgug_minimal_computer
%{_bindir}/sgug_world_builder

%changelog
* Sun Mar 8 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
