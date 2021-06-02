%global mypaint_data_version 1.0

Name: mypaint-brushes
Version: 1.3.0
Release: 4%{?dist}
Summary: Brushes to be used with the MyPaint library

# According to Licenses.dep5 the files used for building/installing are GPLv2+
# but the shipped brush files are CC0
License: CC0
URL: https://github.com/Jehan/mypaint-brushes
Source0: https://github.com/Jehan/mypaint-brushes/archive/v%{version}.tar.gz#/mypaint-brushes-%{version}.tar.gz
Patch0: mypaint-brushes-1.3.0-automake16.patch

BuildArch: noarch

BuildRequires: autoconf
BuildRequires: automake


%package devel
Summary: Files for developing with mypaint-brushes
Requires: pkgconfig
License: GPLv2+


%description
This package contains brush files for use with MyPaint and other programs.


%description devel
This package contains a pkgconfig file which makes it easier to develop
programs using these brush files.


%prep
%autosetup


%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc AUTHORS NEWS README.md
%license COPYING Licenses.dep5 Licenses.md
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/%{mypaint_data_version}
%{_datadir}/mypaint-data/%{mypaint_data_version}/brushes


%files devel
%license COPYING Licenses.dep5 Licenses.md
%{_datadir}/pkgconfig/mypaint-brushes-%{mypaint_data_version}.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Nils Philippsen <nils@tiptoe.de> - 1.3.0-1
- initial release
