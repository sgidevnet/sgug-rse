Name:           pcllib
Version:        1.12
Release:        13%{?dist}
Summary:        Portable Coroutine Library (PCL)

License:        GPLv2+
URL:            http://xmailserver.org/libpcl.html
Source0:        http://xmailserver.org/pcl-1.12.tar.gz

%description
The Portable Co-routine Library (PCL) implements the low level 
functionality for co-routines in C. Co-routines are a very simple 
cooperative multitasking environment where the switch from one task
to another is done explicitly by a function call. Co-routines are a 
lot faster and require much less OS resources than processes or 
threads.

%package devel
Summary:        Development headers and libraries for pcllib
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:	gcc

%description devel
Development headers and libraries for Portable Co-routine Library (PCL).


%prep
%setup -q -n pcl-%{version}


# Note that --disable static is not given because make check requires the static libs
%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a

%check
make check %{?_smp_mflags}

%ldconfig_scriptlets

%files
%{_libdir}/libpcl.so.*
%doc AUTHORS COPYING


%files devel
%{_includedir}/*
%{_libdir}/libpcl.so
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.12-11
- Added gcc build requires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 10 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.12-1
- Initial version of the package
