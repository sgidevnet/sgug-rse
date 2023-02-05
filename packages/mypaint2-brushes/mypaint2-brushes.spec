%global debug_package %{nil}

Name: mypaint2-brushes
Version: 2.0.1
Release: 1%{?dist}
Summary: Collections of brushes for MyPaint
License: CC0 and GPLv2+
URL: https://github.com/mypaint/mypaint-brushes
Source0: https://github.com/mypaint/mypaint-brushes/archive/v%{version}/mypaint-brushes-%{version}.zip
BuildArch: noarch

BuildRequires: autoconf automake

%description
Brushes used by MyPaint 2 and other software using libmypaint2.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains files needed for development with %{name}.

%prep
%autosetup -n mypaint-brushes-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%check
make check

%files
%license COPYING Licenses.dep5
%doc README.md
%{_datadir}/mypaint-data/2.0

%files devel
%{_datadir}/pkgconfig/mypaint-brushes-2.0.pc

%changelog
* Mon Oct 07 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.1-1
- Initial package
