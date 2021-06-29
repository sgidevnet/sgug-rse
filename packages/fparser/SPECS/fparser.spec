%global majorversion 4
%global minorversion 5
%global patchversion 2
Name:           fparser
Version:        %{majorversion}.%{minorversion}.%{patchversion}
Release:        11%{?dist}
Summary:        Function parser library for C++

License:        LGPLv3
URL:            http://warp.povusers.org/FunctionParser/
Source0:        http://warp.povusers.org/FunctionParser/fparser%{version}.zip
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool

# upstream doesn't provide a build system and won't include this patch
Patch0:         fparser.autotools.patch
Patch1:         fparser.includes.patch
Patch2:         fparser.config.patch

%description
This C++ library offers a class which can be used to parse and evaluate a
mathematical function from a string (which might be for example requested
from the user). The syntax of the function string is similar to
mathematical expressions written in C/C++.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
mkdir m4
autoreconf -f -i


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/*.la


%files
%doc docs/gpl.txt docs/lgpl.txt
%{_libdir}/libfparser-%{majorversion}.%{minorversion}.so

%files devel
%doc docs/fparser.html docs/style.css
%{_includedir}/*
%{_libdir}/libfparser.so
%{_libdir}/pkgconfig/fparser.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.2-1
- Update to 4.5.2 (#1229060)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.5.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-9
- Include internal headers, which are required by some external packages
- Enable multi-threading support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-7
- Remove internal headers
* Wed Mar 19 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-6
- Switch to autotools
- Change SONAME to libfparser-$major.$minor.so
* Tue Mar 18 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-5
- Fix SONAME
* Mon Mar 17 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-4
- Change library naming to libfparser-$major.$minor.so
* Tue Mar 11 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-3
- Remove mpfr-devel and gmp-devel dependencies
* Mon Feb 24 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-2
- Include cmake patches
* Mon Jan 27 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.1-1
- Update to 4.5.1
* Thu Oct 24 2013 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 4.5.0-1
- Update to 4.5.0
* Wed Apr 18 2012 Tim Niemueller <tim@niemueller.de> - 4.4.3-1
- Initial package

