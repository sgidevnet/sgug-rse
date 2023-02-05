# latest liblinebreak is v2.1, we obsolete anything below 2.2
%global obsEVR  2.2-1

Name:           libunibreak
Version:        4.0
Release:        4%{?dist}
Summary:        A Unicode line-breaking library

License:        zlib
URL:            http://vimgadgets.sourceforge.net/libunibreak/
Source0:        https://github.com/adah1972/libunibreak/releases/download/libunibreak_4_0/libunibreak-4.0.tar.gz
# test files
Source1:        LineBreakTest.txt
Source2:        WordBreakTest.txt
Source3:        GraphemeBreakTest.txt

# don't download test data
Patch0:         %{name}-4.0-offline_checks.patch
# update list of broken tests
Patch1:         %{name}-4.0-disable_broken_tests.patch

BuildRequires:  gcc

Provides:       liblinebreak = %{version}-%{release}
Obsoletes:      liblinebreak < %{obsEVR}

%description
Libunibreak is an implementation of the line breaking and word
breaking algorithms as described in Unicode Standard Annex 14 and
Unicode Standard Annex 29. It is designed to be used in a generic text
renderer.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       liblinebreak-devel = %{version}-%{release}
Obsoletes:      liblinebreak-devel < %{obsEVR}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p 1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} src/


%build
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
%make_build check


%ldconfig_scriptlets


%files
%doc AUTHORS NEWS README.md
%license LICENCE
%{_libdir}/*.so.*

%files devel
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.0-2
- Properly disable broken tests, run the rest

* Thu Aug 23 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.0-1
- Update to 4.0

* Sat Jun  4 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.0-1
- Initial package
