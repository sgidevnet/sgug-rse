Name:               json-parser
Version:            1.1.0
Release:            11%{?dist}
Summary:            Very low footprint JSON parser written in portable ANSI C

License:            BSD
URL:                https://github.com/udp/json-parser
Source0:            https://github.com/udp/json-parser/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/udp/json-parser/pull/45
Patch0:             0001-improve-pkgconfig-module-close-37.patch

BuildRequires:  gcc
BuildRequires:      automake

%description
Very low footprint JSON parser written in portable ANSI C

%package devel
Summary:            Files needed to develop applications with Very low footprint JSON parser
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed to develop applications with Very low footprint JSON parser

%prep
%setup -q
%patch0 -p1 -b .pkgconfig

%build
autoreconf -vfi
%configure
make %{?_smp_mflags}

%install
make install-shared DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%doc README.md AUTHORS LICENSE
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-1
- 1.1.0 upstream release
- add pkgconfig support
- spec cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4.13ef5a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-3.13ef5a8
- Some updates in changelog
- Update with fix linking

* Wed Jul 31 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-2.df38ae7
- Move %%post[un] scripts between %%install and %%files section
- Update from upstream with LICENSE file

* Wed Jul 31 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-1.9fcf518
- Initial release
