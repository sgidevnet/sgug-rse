%global _hardened_build 1

%global commit 949e85b009f65bc48746f41563ff6e9a866a47a5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    libsecp256k1
Version: 0
Release: 0.20190222git%{shortcommit}%{?dist}
Summary: Optimized C library for EC operations on curve secp256k1

License: MIT
URL:     https://github.com/bitcoin-core/secp256k1
Source0: https://github.com/bitcoin-core/secp256k1/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0: https://github.com/bitcoin-core/secp256k1/pull/558.patch

BuildRequires: gcc
BuildRequires: automake autoconf libtool

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n secp256k1-%{commit}


%build
./autogen.sh
%configure --disable-static --enable-experimental --enable-module-schnorrsig
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%check
./tests


%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.0*

%files devel
%license COPYING
%doc README.md
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190222git949e85b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20190221git949e85b
- Updated to 20190221git949e85b
- Added configure flags for schnorrsig

* Thu May 23 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20190210gita34bcaa
- Updated to 20190210gita34bcaa
- Included support for Schnorr module

* Fri Jan 11 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20181126gite34ceb3
- Inital packaging
