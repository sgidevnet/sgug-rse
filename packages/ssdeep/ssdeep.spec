# spec file for ssdeep
#
# Copyright (c) 2014-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

Name:      ssdeep
Version:   2.14.1
Release:   7%{?dist}
Summary:   Compute context triggered piecewise hashes

License:   GPLv2+
URL:       https://ssdeep-project.github.io/ssdeep/
Source0:   https://github.com/ssdeep-project/ssdeep/releases/download/release-%{version}/ssdeep-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++

Requires:  %{name}-libs%{?_isa} = %{version}-%{release}


%description
ssdeep is a program for computing context triggered piecewise hashes (CTPH).
Also called fuzzy hashes, CTPH can match inputs that have homologies.
Such inputs have sequences of identical bytes in the same order, although bytes
in between these sequences may be different in both content and length.


%package devel
Summary: Development files for libfuzzy
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains library and header files for
developing applications that use libfuzzy.


%package libs
Summary: Runtime libfuzzy library

%description libs
The %{name}-libs package contains libraries needed by applications
that use libfuzzy.


%prep
%setup -q

# avoid autotools being re-run
touch -r aclocal.m4 configure configure.ac


%build
%configure \
   --disable-auto-search \
   --disable-static

# rpath removal
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rm %{buildroot}%{_libdir}/libfuzzy.la


%files
%doc AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files devel
%doc FILEFORMAT NEWS README TODO
%{_includedir}/fuzzy.h
%{_includedir}/edit_dist.h
%{_libdir}/libfuzzy.so

%files libs
%license COPYING
%{_libdir}/libfuzzy.so.2*


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 2.14.1-4
- missing BR on C/C++ compilers

* Wed Feb 14 2018 Remi Collet <remi@remirepo.net> - 2.14.1-3
- drop ldconfig scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov  7 2017 Remi Collet <remi@fedoraproject.org> - 2.14.1-1
- update to 2.14.1

* Fri Sep 15 2017 Remi Collet <remi@fedoraproject.org> - 2.14-1
- update to 2.14
- sources from github
- fix project URL

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May  5 2015 Remi Collet <remi@fedoraproject.org> - 2.13-1
- update to 2.13

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.12-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Oct 26 2014 Remi Collet <remi@fedoraproject.org> - 2.12-1
- update to 2.12

* Mon Sep 29 2014 Remi Collet <remi@fedoraproject.org> - 2.11.1-1
- update to 2.11.1 (no change)
- fix license handling

* Fri Sep 12 2014 Remi Collet <remi@fedoraproject.org> - 2.11-1
- update to 2.11

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Remi Collet <remi@fedoraproject.org> - 2.10-2
- cleanup build path (comment from review #1056460)

* Wed Jan 22 2014 Remi Collet <remi@fedoraproject.org> - 2.10-1
- initial package
