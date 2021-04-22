#
# spec file for package innoextract
#
# Copyright (c) 2012-2015 Daniel Scharrer <daniel@constexpr.org>
#               2015 Alexandre Detiste <alexandre@detiste.be>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           innoextract
Version:        1.8
Release:        3%{?dist}
License:        zlib
Summary:        Tool to extract installers created by Inno Setup
Url:            https://constexpr.org/innoextract/
Source:         %{url}/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  xz-devel

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep
%setup -q

%build
export CFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%cmake \
    -DCMAKE_INSTALL_DATAROOTDIR="%{_datadir}" \
    -DCMAKE_INSTALL_MANDIR="%{_mandir}" \
    -DCMAKE_INSTALL_BINDIR="%{_bindir}" \
    -DUSE_LDGOLD=FALSE \
    .
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG VERSION
%{_bindir}/innoextract
%{_mandir}/man1/innoextract.1*

%changelog
* Thu Apr 22 2021  HAL <notes2@gmx.de> - 1.8-3
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Sat Nov 16 2019 Alexandre Detiste <alexandre@detiste.be> - 1.8-3
- rebuild with ppc64le re-enabled

* Fri Nov 15 2019 Dan Horák <dan[at]danny.cz> - 1.8-2
- switch to ld.bfd

* Sun Sep 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8-1
- Update to 1.8
- Switch to https over http
- Disable ppc64le for now, it fails to build
# https://bugzilla.redhat.com/show_bug.cgi?id=1752252

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.7-1
- New upstream release (#1590790)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.6-12
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.6-11
- Append curdir to CMake invokation. (#1668512)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.6-8
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.6-5
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.6-4
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 1.6-2
- Rebuilt for Boost 1.63

* Fri Mar 25 2016 Alexandre Detiste- 1.6-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Alexandre Detiste <alexandre@detiste.be> - 1.5-5.fc24
- rebuilt for Boost 1.60

* Fri Jan 22 2016 Alexandre Detiste <alexandre@detiste.be> - 1.5-4.fc24
- add ?dist part to version number

* Tue Dec 29 2015 Alexandre Detiste <alexandre@detiste.be> - 1.5-3
- add blank line between changelog entries

* Thu Nov 19 2015 Alexandre Detiste <alexandre@detiste.be> - 1.5-2
- Remove "suse_version" blocks
- Drop Group: and BuildRoot: lines

* Sun Nov 08 2015 Alexandre Detiste <alexandre@detiste.be> - 1.5-1
- Initial Fedora package based on upstream spec-file for 1.5-1
