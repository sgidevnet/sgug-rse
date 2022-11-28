%ifarch ppc64 s390x %{arm}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           flatbuffers
Version:        1.11.0
Release:        2%{?dist}
Summary:        Memory efficient serialization library
URL:            http://google.github.io/flatbuffers

# The entire source code is ASL 2.0 except grpc/ which is BSD (3 clause)
License:        ASL 2.0 and BSD

Source0:        https://github.com/google/flatbuffers/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        flatc.1
Source2:        flatbuffers.7

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 2.8.9

# The library contains pieces of gRPC project, with some additions.
# It is not easy to identify the version, which was used to take the code,
# but it should be something after version 1.3.2. See this discussion for
# details: https://github.com/google/flatbuffers/pull/4305
Provides:       bundled(grpc)

%description
FlatBuffers is a serialization library for games and other memory constrained
apps. FlatBuffers allows you to directly access serialized data without
unpacking/parsing it first, while still having great forwards/backwards
compatibility.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep
%autosetup -p1
# cleanup distribution
rm -rf js net php python docs go java js biicode {samples/,}android
chmod -x readme.md

%cmake -DCMAKE_BUILD_TYPE=Release \
       -DFLATBUFFERS_BUILD_SHAREDLIB=ON \
       -DFLATBUFFERS_BUILD_FLATLIB=OFF \
       -DFLATBUFFERS_BUILD_FLATC=ON \
       -DFLATBUFFERS_BUILD_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
       .

%build
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man{1,7}
cp -p %SOURCE1 %{buildroot}%{_mandir}/man1/flatc.1
cp -p %SOURCE2 %{buildroot}%{_mandir}/man7/flatbuffers.7

%check
%if %{with tests}
make test
%endif

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc readme.md
%{_bindir}/flatc
%{_libdir}/libflatbuffers.so.*
%{_mandir}/man1/flatc.1*

%files devel
%{_includedir}/flatbuffers
%{_libdir}/libflatbuffers.so
%{_mandir}/man7/flatbuffers.7*
%{_libdir}/cmake/flatbuffers/*.cmake

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.11.0-1
- Update to 1.11.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.10.0-3
- Add explicit curdir on CMake invocation

* Thu Jan 10 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.10.0-2
- Fix generator (and generated tests) for gcc9 (ignore -Wclass-memaccess)

* Thu Oct 04 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.8.0-3
- Fix build errors.

* Wed Nov 22 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.8.0-2
- Update manpages for 1.8.0

* Wed Nov 22 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Thu Nov 2 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.7.1-1
- Initial version

* Mon Mar 30 2015 Daniel Vrátil <dvratil@redhat.com> - 1.0.3-1
- Initial version (abandoned at #1207208)
