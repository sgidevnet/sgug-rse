#%%global prever rc3

Name: log4cplus
Version: 1.2.0
Release: 10%{?prever:.%{prever}}%{?dist}
Summary: Logging Framework for C++

License: ASL 2.0
URL: http://sourceforge.net/projects/log4cplus
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}%{?prever:-%{prever}}.tar.xz

%description
log4cplus is a simple to use C++ logging API providing thread-safe, flexible,
and arbitrarily granular control over log management and configuration. It is
modeled after the Java log4j API.

%package devel
Summary: Development files for log4cplus C++ logging framework
Requires: %{name} = %{version}-%{release}
BuildRequires: gcc-c++

%description devel
This package contains headers and libraries needed to develop applications
using log4cplus logging framework.

%prep
%setup -q %{?prever:-n %{name}-%{version}-%{prever}}

%build
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++11"
%configure
make %{?_smp_mflags}


%install
%make_install

rm -f $RPM_BUILD_ROOT/%{_libdir}/liblog4cplus.{a,la}

%ldconfig_scriptlets

%files
%doc LICENSE README.md ChangeLog
%{_libdir}/liblog4cplus*.so.5*

%files devel
%dir %{_includedir}/log4cplus
%dir %{_includedir}/log4cplus/boost
%dir %{_includedir}/log4cplus/config
%dir %{_includedir}/log4cplus/helpers
%dir %{_includedir}/log4cplus/internal
%dir %{_includedir}/log4cplus/spi
%dir %{_includedir}/log4cplus/thread
%dir %{_includedir}/log4cplus/thread/impl
%{_libdir}/lib*.so
%{_includedir}/log4cplus/*.h*
%{_includedir}/log4cplus/boost/*.h*
%{_includedir}/log4cplus/config/*.h*
%{_includedir}/log4cplus/helpers/*.h*
%{_includedir}/log4cplus/internal/*.h*
%{_includedir}/log4cplus/spi/*.h*
%{_includedir}/log4cplus/thread/*.h*
%{_includedir}/log4cplus/thread/impl/*.h*
%{_libdir}/pkgconfig/log4cplus.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Tomas Hozza <thozza@redhat.com> - 1.2.0-7
- Added gcc-c++ as an explicit BuildRequires

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 23 2016 Zdenek Dohnal zdohnal@redhat.com - 1.2.0-2
- Replacing hard names with macros, returning and commenting macro prever in
  specfile

* Fri Mar 18 2016 zdohnal <zdohnal@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.5.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Tomas Hozza <thozza@redhat.com> - 1.1.3-0.4.rc3
- Fixed typo so that log4cplus is compiled with C++11 support (#1297906)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-0.3.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.3-0.2.rc3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Dec 16 2014 Tomas Hozza <thozza@redhat.com> - 1.1.3-0.1.rc3
- update to 1.1.3rc3
- build the library with c++11 support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Tomas Hozza <thozza@redhat.com> - 1.1.2-1
- update to 1.1.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Tomas Hozza <thozza@redhat.com> 1.1.1-1
- update to 1.1.1

* Mon Feb 18 2013 Adam Tkac <atkac redhat com> - 1.1.0-1
- update to 1.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.3.rc10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 21 2012 Adam Tkac <atkac redhat com> - 1.1.0-0.2.rc10
- some fixes related to pkg review

* Thu Sep 20 2012 Adam Tkac <atkac redhat com> - 1.1.0-0.1.rc10
- initial package
