Name:           mujs
Version:        1.0.9
Release:        1%{?dist}
Summary:        An embeddable Javascript interpreter
License:        AGPLv3+
URL:            http://mujs.com/
# The mujs.com download page doesn't provide recent tarballs
# Github mirror of mujs.com repository provides releases from tags
Source0:        https://github.com/ccxvii/mujs/archiv/%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  readline-devel

%description
MuJS is a lightweight Javascript interpreter designed for embedding in
other software to extend them with scripting capabilities.

%package devel
Summary:        MuJS development files
Provides:       %{name}-static = %{version}-%{release}

%description devel
This package provides the MuJS static library.

%prep
%setup -q -n %{name}-%{version}
chmod a-x -v docs/*

%build
make debug %{?_smp_mflags} XCFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}"

%install
make install DESTDIR=%{buildroot} prefix="%{_prefix}" libdir="%{_libdir}" \
 XCFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}"

%files
%license COPYING
%doc AUTHORS README docs
%{_bindir}/%{name}

%files devel
%license COPYING
%doc AUTHORS README
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a

%changelog
* Sat Oct 31 2020 Petr Šabata <contyk@redhat.com> - 1.0.9-1
- 1.0.9 bump
- Addresses CVE-2019-11411, CVE-2019-11412 and CVE-2019-11413

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-2
- Fix build flags so debuginfo is generated
- Compile with fPIC

* Thu Sep 27 2018 Michael J Gruber <mjg@fedoraproject.org> - 1.0.4-1
* Upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20180129git25821e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20180129git25821e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Petr Šabata <contyk@redhat.com> - 0-11.20180129git25821e6
- Fix CVE-2018-5759, rhbz#1539514

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20170124git4006739
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20170124git4006739
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Petr Šabata <contyk@redhat.com> - 0-8.20170124git4006739
- Include the latest upstream Fixes
- Fixes CVE-2016-10132, CVE-2016-10133, CVE-2016-10141, CVE-2017-5627 and
  CVE-2017-5628

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20161031gita0ceaf5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Petr Šabata <contyk@redhat.com> - 0-6.20161031gita0ceaf5
- Include the latest upstream fixes
- Fixes CVE-2016-9108, CVE-2016-9109, CVE-2016-9017 and CVE-2016-9294

* Thu Sep 29 2016 Petr Šabata <contyk@redhat.com> - 0-5.20160921git5c337af
- Update to the upstream master HEAD
- Fixes CVE-2016-7563 and CVE-2016-7564

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20150929git0827611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Petr Šabata <contyk@redhat.com> - 0-1.20150929git0827611
- Update to 0827611.
- Package the docs directory

* Thu Sep 17 2015 Petr Šabata <contyk@redhat.com> - 0-4.20150202gitc1ad1ba
- Enable full RELRO

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.20150202gitc1ad1ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Petr Šabata <contyk@redhat.com> - 0-2.20150202gitc1ad1ba
- Address the reviewer's concerns

* Thu May 07 2015 Petr Šabata <contyk@redhat.com> - 0-1.20150202gitc1ad1ba
- Initial packaging
