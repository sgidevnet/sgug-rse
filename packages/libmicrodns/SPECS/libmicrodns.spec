Name:           libmicrodns
Version:        0.0.10
Release:        4%{?dist}
Summary:        Minimal mDNS resolver library

License:        LGPLv2+
URL:            https://github.com/videolabs/libmicrodns
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libtool


%description
Minimal mDNS resolver (and announcer) library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup
./bootstrap


%build
%configure \
  --disable-static \
  --disable-assert

%make_build V=1


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS
%{_docdir}/microdns/README.md
%{_libdir}/libmicrodns.so.0*

%files devel
%{_includedir}/microdns
%{_libdir}/libmicrodns.so
%{_libdir}/pkgconfig/microdns.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.0.10-1
- Update to 0.0.10

* Wed Feb 14 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.0.8-1
- Initial spec file
