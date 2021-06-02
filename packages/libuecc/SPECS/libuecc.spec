Name:           libuecc
Version:        7
Release:        8%{?dist}
Summary:        Very small Elliptic Curve Cryptography library

License:        BSD
URL:            https://git.universe-factory.net/libuecc
Source0:        https://git.universe-factory.net/libuecc/snapshot/libuecc-%{version}.zip

BuildRequires:  gcc
BuildRequires:  cmake

%description
Very small Elliptic Curve Cryptography library that is well suited for embedded
software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc CHANGELOG README
%license COPYRIGHT
%{_libdir}/%{name}.so.*

%files devel
%doc CHANGELOG README
%license COPYRIGHT
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 30 2016 Felix Kaechele <heffer@fedoraproject.org> - 7-1
- update to version 7
- added docs
- updated URLs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Felix Kaechele <heffer@fedoraproject.org> - 6-1
- update to version 6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Felix Kaechele <heffer@fedoraproject.org> - 5-2
- mark the COPYRIGHT as license, not doc

* Thu Feb 19 2015 Felix Kaechele <heffer@fedoraproject.org> - 5-1
- update to version 5

* Sat Mar 29 2014 Felix Kaechele <heffer@fedoraproject.org> - 4-1
- first package version
