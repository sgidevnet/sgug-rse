Summary: Lightweight pthread related functions (consumed mainly by X11 applications)
Name: libpthread-stubs
Version: 0.4
Release: 1wip%{?dist}
License: GPLv3+
URL: https://github.com/freedesktop/xcb-pthread-stubs
Source: https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz

# Just some standard bits
BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

# Here's where you add parents you need in place
#Requires: parentproject

%description
A lightweight library containing mainly mutex related pthread functions.

%prep
# You can omit the "-n example-wip-%{version}" here as it's the default
# this is just to show how you'd specific a particular extracted package dir
%setup -q -n %{name}-%{version}

%build
%{configure}
make %{?_smp_mflags}

%check
# Do the tests by hand
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

# Here you add removes for stuff you don't want included
# example to remove doc
# rm -rf $RPM_BUILD_ROOT%{_prefix}/BLAH

%files
# If you have programs
#%{_bindir}/*
# If you have libraries
%{_libdir}/pkgconfig/*
# other stuff, add the relative paths here

%changelog
* Mon Apr 13 2020 Daniel Hams <daniel.hams@gmail.com> - 0.4
- First import into wip.
