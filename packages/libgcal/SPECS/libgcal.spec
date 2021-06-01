Name:		libgcal
Version:	0.9.6
Release:	20%{?dist}
Summary:	A library to access google calendar events and contacts

License:	BSD
URL:		http://code.google.com/p/libgcal/
Source0:	http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:	libcurl-devel
BuildRequires:	libxml2-devel
BuildRequires:	check-devel
BuildRequires:	ca-certificates
BuildRequires:	cmake

%description
This is a library to access google calendar events and contacts, its purpose is
   - provide easy access to available events/contacts
   - enable common operations: add, delete, edit
   - have few dependencies (up until now, only requires libcurl and libxml)

It implements Google Data API 2.0 and is tested on Linux and MacOSX.


%package        devel
Summary:        Development files to use libgcal
Requires:       %{name} = %{version}-%{release}

%description devel
libgcal is a library to access google calendar events and contacts: these are
the development files that can be used to link against it.


%prep
%setup -q

%build
%{cmake} .

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot}

%ldconfig_scriptlets


%files
%doc COPYING README Changelog.txt
%{_libdir}/libgcal.so.0*

%files devel
%dir %{_includedir}/libgcal
%{_includedir}/libgcal/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgcal.pc
%{_libdir}/LibGCal

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Mario Santagiuliana <fedora@marionline.it> 0.9.6-5
- Update spec file following Rex Dieter directive:
https://bugzilla.redhat.com/show_bug.cgi?id=713741#c5

* Thu Jun 16 2011 Mario Santagiuliana <fedora@marionline.it> 0.9.6-4
- Update spec file following Rex Dieter directive:
https://bugzilla.redhat.com/show_bug.cgi?id=713741#c3

* Thu Jun 16 2011 Mario Santagiuliana <mario@marionline.it> 0.9.6-3
- Update spec file
- Fix bug #659959

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.9.6-1
- update to 0.9.6

* Fri Nov 05 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.9.6-1
- update to 0.9.6

* Sat Aug 07 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.9.5-1
- update to 0.9.5

* Wed Jun 16 2010 Dennis Gilmore <dennis@ausil.us> 0.9.4-1
- update to 0.9.4

* Sun Mar 21 2010 Mario Ceresa <mrceresa@gmail.com> 0.9.3-4
- Removed INSTALL from the devel package

* Thu Mar 13 2010 Mario Ceresa <mrceresa@gmail.com> 0.9.3-3
- Patched pc_include (Thanks to Peter Lemenkov for the patch)

* Thu Jan 21 2010 Mario Ceresa <mrceresa@gmail.com> 0.9.3-2
- Fixed the comments from the reviewers

* Tue Dec 29 2009 Mario Ceresa <mrceresa@gmail.com> 0.9.3-1
- Initial RPM Release
