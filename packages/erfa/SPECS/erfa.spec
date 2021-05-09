Name: erfa
Version: 1.7.1
Release: 1%{?dist}
Summary: Essential Routines for Fundamental Astronomy

License: BSD
URL: https://github.com/liberfa/erfa
Source0: https://github.com/liberfa/erfa/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc

%description
ERFA is a C library containing key algorithms for astronomy, and is 
based on the SOFA library published by the International Astronomical 
Union (IAU).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q 

%build
%configure --disable-static
make %{?_smp_mflags} 

%install
make install DESTDIR=%{buildroot}

%check
make check

%ldconfig_scriptlets

%files
%doc README.rst INFO
%license LICENSE
%{_libdir}/liberfa.so.*

%files devel
%{_libdir}/liberfa.so
%{_includedir}/erfa*.h
%{_libdir}/pkgconfig/erfa.pc
%exclude %{_libdir}/*.la

%changelog
* Sun Sep 20 2020 Sergio Pascual <sergiopr at fedoraproject.org> - 1.7.1-1
- New upstream version (1.7.1)

* Tue May 12 2020 Sergio Pascual <sergiopr at fedoraproject.org> - 1.7.0-1
- New upstream version (1.7.0)

* Tue Oct 08 2019 Sergio Pascual <sergiopr at fedoraproject.org> - 1.6.0-1
- New upstream version (1.6.0)

* Thu Aug 01 2019 Sergio Pascual <sergiopr at fedoraproject.org> - 1.5.0-1
- New upstream version (1.5.0)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.4.0-4
- BuildRequires: gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4.0-1
- New upstream version (1.4.0)
- Removed fno-caller-saves to cflags, not needed anymore

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 02 2016 Sergio Pascual <sergiopr at fedoraproject.org> - 1.3.0-1
- New upstream version (1.3.0)
- Add fno-caller-saves to cflags (https://github.com/liberfa/erfa/issues/33)

* Fri Mar 18 2016 Sergio Pascual <sergiopr at fedoraproject.org> - 1.2.0-5
- EVR bump to rebuild, disable checks for the moment

* Sun Feb 28 2016 Sergio Pascual <sergiopr at fedoraproject.org> - 1.2.0-4
- EVR bump to rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Sergio Pascual <sergiopr at fedoraproject.org> - 1.2.0-1
- New upstream version (1.2.0) (includes 2015-Jun-30 leap second)

* Wed Sep 24 2014 Sergio Pascual <sergiopr at fedoraproject.org> - 1.1.1-1
- New upstream version (1.1.1)
- Using license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Sergio Pascual <sergiopr at fedoraproject.org> - 1.1.0-1
- New usptream version (1.1.0)

* Wed Nov 13 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0.1-1
- New usptream version (1.0.1)

* Sat Oct 26 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0.0-1
- New usptream version (1.0.0)

* Mon Sep 09 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 0.0.1-3
- Updated -devel summary
- Removed explicit dependency on pkgconfig

* Mon Sep 09 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 0.0.1-2
- Updated -devel description

* Sun Sep 08 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 0.0.1-1
- Initial spec

