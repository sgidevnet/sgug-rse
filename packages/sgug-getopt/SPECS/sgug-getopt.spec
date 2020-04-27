# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary: SGUG getopt
Name: sgug-getopt
Version: 0.1.0
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/sgidevnet/sgug-getopt
Source: https://github.com/sgidevnet/sgug-getopt/releases/download/v%{version}/sgug-getopt-%{version}.tar.gz

Requires: libdicl

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: libdicl-devel

%description
An extracted version of the util-linux getopt command line tool for program argument parsing.

%prep
%setup -q

%build
export CPPFLAGS="-DLIBDICL_NEED_GETOPT=1"
%{configure}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

%files
%{_bindir}/getopt

%changelog
* Sun Apr 5 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
