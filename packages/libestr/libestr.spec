Name:           libestr
Version:        0.1.9
Release:        13%{?dist}
Summary:        String handling essentials library

License:        LGPLv2+
URL:            http://libestr.adiscon.com/
Source0:        http://libestr.adiscon.com/files/download/libestr-%{version}.tar.gz

BuildRequires:  gcc
%description
This package compiles the string handling essentials library
used by the Rsyslog daemon.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The package contains libraries and header files for
developing applications that use libestr.

%prep
%setup -q

%build
%configure --disable-static --with-pic
V=1 make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.{a,la}

#%%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README AUTHORS ChangeLog
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libestr.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libestr.pc

%changelog
* Sun Jan 10 2021  HAL <notes2@gmx.de> - 0.1.9-13
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Tom Callaway <spot@fedoraproject.org> - 0.1.9-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Tomas Heinrich <theinric@redhat.com> - 0.1.9-1
- rebase to 0.1.9
- remove patch 0; doesn't seem to be necessary anymore

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Tomas Heinrich <theinric@redhat.com> - 0.1.5-1
- rebase to 0.1.5

* Wed Dec 12 2012 Mahaveer Darade <mdarade@redhat.com> - 0.1.4-1
- upgrade to upstream version 0.1.4
- correct an impossible timestamp in an older changelog entry

* Thu Sep 20 2012 mdarade <mdarade@redhat.com> - 0.1.3-3
- Fixed broken configure script

* Mon Aug 27 2012 mdarade <mdarade@redhat.com> - 0.1.3-2
- Removed unnecessary macros in spec file.

* Tue Aug 7 2012 Mahaveer Darade <mdarade@redhat.com> - 0.1.3-1
- Initial port libestr-0.1.3
