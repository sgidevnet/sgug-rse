%if 0%{?rhel} && 0%{?rhel} < 7
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           cmark
Version:        0.28.3
Release:        6%{?dist}
Summary:        CommonMark parsing and rendering

License:        BSD and MIT
URL:            https://github.com/jgm/cmark
Source0:        https://github.com/jgm/cmark/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
`cmark` is the C reference implementation of CommonMark,
a rationalized version of Markdown syntax with a spec.

It provides a shared library (`libcmark`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark`) for parsing and rendering CommonMark
documents.


%package devel
Summary:        Development files for cmark
Requires:       cmark-lib = %{version}-%{release}

%description devel
This package provides the development files for cmark.



%package lib
Summary:        CommonMark parsing and rendering library

%description lib
This package provides the cmark library.



%prep
%setup -q


%build
mkdir build
cd build
%cmake %{?_without_tests:-DCMARK_TESTS=OFF} ..
make %{?_smp_mflags}


%install
cd build
make install DESTDIR=%{buildroot}

rm %{buildroot}%{_libdir}/libcmark.a


%check
%if %{with tests}
cd build
make test
%endif


%ldconfig_scriptlets lib


%files
%license COPYING
%{_bindir}/cmark
%{_mandir}/man1/cmark.1.gz


%files lib
%license COPYING
%{_libdir}/libcmark.so.%{version}


%files devel
%doc README.md
%{_includedir}/cmark.h
%{_includedir}/cmark_export.h
%{_includedir}/cmark_version.h
%{_libdir}/libcmark.so
%{_libdir}/pkgconfig/libcmark.pc
%{_mandir}/man3/cmark.3.gz
%{_libdir}/cmake/cmark*.cmake


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr  2 2018 Jens Petersen <petersen@redhat.com> - 0.28.3-3
- run tests on Fedora and RHEL7 (#1561473)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 0.28.3-1
- update to 0.28.3 (#1516914)
  https://github.com/commonmark/cmark/releases

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 0.27.1-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.27.1-1
- update to 0.27.1

* Tue Feb  7 2017 Jens Petersen <petersen@redhat.com> - 0.25.2-3
- drop lib64 patch

* Sun Feb  5 2017 Jens Petersen <petersen@redhat.com> - 0.25.2-2
- fix libdir in libcmark.pc for pkgconf (#1416426)
- use bcond for tests

* Fri Apr 29 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.25.2-1
- Update to 0.25.2

* Thu Feb  4 2016 Jens Petersen <petersen@redhat.com> - 0.24.1-1
- update to 0.24.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Jens Petersen <petersen@redhat.com> - 0.23.0-4
- BR c++ explicitly
- disable tests for EPEL6 since no python3

* Mon Jan 25 2016 Jens Petersen <petersen@redhat.com> - 0.23.0-3
- include license in lib (#1266429)

* Thu Jan 21 2016 Jens Petersen <petersen@redhat.com> - 0.23.0-2
- tweak the github release source url (#1266429)

* Wed Jan 20 2016 Jens Petersen <petersen@redhat.com> - 0.23.0-1
- update to 0.23.0
- cmake include GNUInstallDirs (Marco Driusso, #1266429)

* Fri Sep 25 2015 Jens Petersen <petersen@redhat.com> - 0.22.0-1
- initial packaging
- force lib64
- run tests
