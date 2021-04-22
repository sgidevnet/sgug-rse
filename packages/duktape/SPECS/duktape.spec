Name:           duktape
Version:        2.2.0
Release:        5%{?dist}
Summary:        Embeddable Javascript engine
License:        MIT
Url:            http://duktape.org/
Source0:        http://duktape.org/%{name}-%{version}.tar.xz
Source1:        duktape.pc.in
BuildRequires:  gcc
BuildRequires:  pkgconfig

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
Embeddable Javascript engine.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%setup -q

sed -e's|@prefix@|%{_prefix}|' \
    -e's|@libdir@|%{_lib}|' \
    -e's|@PACKAGE_VERSION@|%{version}|' \
    < %{SOURCE1} > %{name}.pc.in

%build
sed -e '/^INSTALL_PREFIX/s|[^=]*$|%{_prefix}|' \
    -e '/install\:/a\\tinstall -d $(DESTDIR)$(INSTALL_PREFIX)/%{_lib}\n\tinstall -d $(DESTDIR)$(INSTALL_PREFIX)/include' \
    -e 's/\(\$.INSTALL_PREFIX.\)/$(DESTDIR)\1/g' \
    -e 's/\/lib\b/\/%{_lib}/g' \
     < Makefile.sharedlibrary > Makefile
%make_build

%install
%make_install

install -Dm0644 %{name}.pc.in %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

#%%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc AUTHORS.rst
%{_libdir}/libduktape.so.*
%{_libdir}/libduktaped.so.*

%files devel
%doc examples/ README.rst
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc

%changelog
* Thu Apr 22 2021  HAL <notes2@gmx.de> - 2.2.0-5
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.2.0-2
- Macro corrections, dist tag.

* Fri Apr 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.2.0-1
- Adapt to modern packaging guidelines.

* Mon Mar 19 2018 jk@lutty.net
- Initial package for fedora derived from Suse
