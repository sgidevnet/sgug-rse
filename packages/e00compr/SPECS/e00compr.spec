Name:           e00compr
Version:        1.0.1
Release:        21%{?dist}
Summary:        Library to compress and uncompress E00 files

License:        MIT
URL:            http://avce00.maptools.org/e00compr
Source0:        http://avce00.maptools.org/dl/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
ANSI-C library to compress and uncompress Arc/Info Export (E00) files.
The package also contains a converter binary.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
Contains %{name}'s development headers and library.


%prep
%setup -q
chmod -x *.h *.c
sed -i 's/\r$//' README.TXT

# Use actual header file locations in examples and documentation
sed -i 's|#include "e00compr.h"|#include <e00compr/e00compr.h>|' ex_*.c %{name}.txt %{name}.html


%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"


%install
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}

# Header name conflict with cpl (cpl_error.h)
# http://bugzilla.maptools.org/show_bug.cgi?id=2367
install -pm 0644 *.h %{buildroot}%{_includedir}/%{name}
install -pm 0644 *.1 %{buildroot}%{_mandir}/man1
install -pm 0644 *.a %{buildroot}%{_libdir}
install -pm 0755 e00conv %{buildroot}%{_bindir}


%files
%doc HISTORY.TXT README.TXT e00compr.html
%{_bindir}/e00conv
%{_mandir}/man1/e00conv.1.*

%files devel
%doc ex_*.c README.TXT
%{_includedir}/%{name}/*.h
%{_libdir}/*.a


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Volker Fröhlich <volker27@gmx.at> - 1.0.1-19
- Add BR gcc in the wake of the removal of gcc from the builroot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Volker Fröhlich <volker27@gmx.at> - 1.0.1-6
- Solve header name conflicts with cpl
- Update header location in example files and documentation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Volker Fröhlich <volker27@gmx.at> - 1.0.1-4
- Remove isa macro from virtual provide
- Devel doesn't require the base package, and ships the license text too

* Thu Oct 30 2011 Volker Fröhlich <volker27@gmx.at> - 1.0.1-3
- Build with fPIC

* Thu Oct 27 2011 Volker Fröhlich <volker27@gmx.at> - 1.0.1-2
- Add isa macro to provide

* Mon Oct 17 2011 Volker Fröhlich <volker27@gmx.at> - 1.0.1-1
- Initial package for Fedora
