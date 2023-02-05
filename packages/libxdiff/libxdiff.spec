# Matches 1.0 tag.
%global commit 9c6289c5a088bf24f18f0b7bf8acaaf643aa411d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		libxdiff
Version:	1.0
Release:	15%{?dist}
Summary:	Basic functionality to create difference/patches in binary and text
License:	LGPLv2+
URL:		https://github.com/spotrh/libxdiff
Source0:	https://github.com/spotrh/libxdiff/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:		%{name}-1.0-big-endian.patch
BuildRequires:	gcc

%description
The LibXDiff library implements basic and yet complete functionalities to 
create file differences/patches to both binary and text files. The library 
uses memory files as file abstraction to achieve both performance and 
portability. For binary files, LibXDiff implements both (with some 
modification) the algorithm described in File System Support for Delta 
Compression by Joshua P. MacDonald, and the algorithm described in 
Fingerprinting By Random Polynomials by Michael O. Rabin. While for text 
files it follows directives described in An O(ND) Difference Algorithm 
and Its Variations by Eugene W. Myers.

This is a merged fork of the forks of the original libxdiff (0.23) found 
in the git and libgit2 source code, converted into a shared library.

%package devel
Summary:	Development libraries and headers for libxdiff
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for libxdiff.

%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1 -b .big-endian

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README.md NEWS ChangeLog
%{_libdir}/libxdiff.so.*

%files devel
%{_includedir}/xdiff/
%{_libdir}/libxdiff.so
%{_libdir}/pkgconfig/libxdiff.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Tom Callaway <spot@fedoraproject.org> - 1.0-13
- add BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Dan Horák <dan[at]danny.cz> - 1.0-2
- fix function on big-endian arches

* Thu May 30 2013 Tom Callaway <spot@fedoraproject.org> - 1.0-1
- initial package
