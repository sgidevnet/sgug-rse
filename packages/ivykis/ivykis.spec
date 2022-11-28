%if 0%{?rhel} > 6 || 0%{?fedora} > 16
%global librarydir %{_libdir}
%else
%global librarydir /%{_lib}
%endif

Summary:        Library for asynchronous I/O readiness notification
Name:           ivykis
Version:        0.42.4
Release:        2%{?dist}

License:        LGPLv2+
URL:            http://libivykis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/libivykis/%{version}/%{name}-%{version}.tar.gz


BuildRequires:  gcc
%description
ivykis is a library for asynchronous I/O readiness notification.
It is a thin, portable wrapper around OS-provided mechanisms such
as epoll_create(2), kqueue(2), poll(2), poll(7d) (/dev/poll) and
port_create(3C).

ivykis was mainly designed for building high-performance network
applications, but can be used in any event-driven application that
uses poll(2)able file descriptors as its event sources.

%package devel
Summary:        Development files for the ivykis package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
ivykis is a library for asynchronous I/O readiness notification.
This package contains files needed to develop applications using
ivykis.


%prep
%setup -q

%build
%configure --libdir=%{librarydir}
%{__make} %{_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{librarydir}/libivykis.{a,la}

%if "%{librarydir}" != "%{_libdir}"
  mkdir -p %{buildroot}%{_libdir}
  mv %{buildroot}%{librarydir}/pkgconfig %{buildroot}%{_libdir}/
%endif

%check
make check


%ldconfig_scriptlets


%files
%doc AUTHORS COPYING
%{librarydir}/libivykis.so.*

%files devel
%{librarydir}/libivykis.so
%{_includedir}/iv*
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*.3*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 My Karlsson <mk@acc.umu.se> - 0.42.4-1
- Update to 0.42.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 My Karlsson <mk@acc.umu.se> - 0.42.3-3
- Rebuilt

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 05 2018 My Karlsson <mk@acc.umu.se> - 0.42.3-1
- Update to 0.42.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 My Karlsson <mk@acc.umu.se> - 0.42.2-1
- Update to 0.42.2

* Sat Aug 19 2017 My Karlsson <mk@acc.umu.se> - 0.42.1-1
- Update to 0.42.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 6 2017 My Karlsson <mk@acc.umu.se> - 0.42-1
- Update to 0.42.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.41-1
- Update to 0.41.

* Fri Nov 11 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.40-3
- Patch file: ivykis-0.40-aarch64-and-ppc64.patch

* Wed Nov  2 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.40-2
- Run the test suite

* Wed Nov  2 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.40-1
- Update to 0.40.

* Sun Oct 30 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.36.3-1
- Update to 0.36.3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 17 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.36.2-1
- Update to 0.36.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.36.1-1
- Update to 0.36.1.

* Mon Dec 10 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.5-1
- Update to 0.30.5.

* Sun Oct  7 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.4-2
- Handle review issues (863719#c1)

* Sat Oct  6 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.4-1
- Initial specfile for Fedora and EPEL.

# vim:set ai ts=4 sw=4 sts=4 et:
