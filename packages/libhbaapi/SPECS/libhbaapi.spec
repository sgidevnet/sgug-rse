Name:           libhbaapi
Version:        2.2.9
Release:        15%{?dist}
Summary:        SNIA HBAAPI library
License:        SNIA
URL:            http://open-fcoe.org/
# This source was cloned from upstream git (libHBAAPI)
Source:         %{name}-%{version}.tar.gz
Patch0:         libhbaapi-2.2.9-dl-linking.patch
Patch1:         libhbaapi-2.2.9-portspeed.patch
BuildRequires:  automake libtool

%description
The SNIA HBA API library. C-level project to manage
Fibre Channel Host Bus Adapters.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup
%patch0 -p1 -b .ld-linking
%patch1 -p1 -b .portspeed

%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING
%config(noreplace) %{_sysconfdir}/hba.conf
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 07 2014 Chris Leech <cleech@redhat.com> - 2.2.9-6
- sync with upstream, adds new portspeed definitions

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Petr Šabata <contyk@redhat.com> - 2.2.9-3
- Make the devel subpackage arch-dependent

* Thu Jul 11 2013 Petr Šabata <contyk@redhat.com> - 2.2.9-2
- Link against libdl

* Tue Jun 04 2013 Petr Šabata <contyk@redhat.com> - 2.2.9-1
- 2.2.9 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 04 2012 Petr Šabata <contyk@redhat.com> - 2.2.6-1
- Migrate to the Open-FCoE.org fork

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Petr Šabata <contyk@redhat.com> - 2.2-14
- Update to hbaapi_build 2.2.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Petr Sabata <contyk@redhat.com> - 2.2-12
- Update to hbaapi_build 2.2.4
- Remove now obsolete Buildroot and defattr

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 16 2010 Jan Zeleny <jzeleny@redhat.com> - 2.2-10
- updated hbaapi_build to 2.2.2

* Wed Nov 04 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-9
- fixed linking with libdl

* Thu Jul 30 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-8
- added libtool to BuildRequires

* Thu Jul 30 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-7
- added automake to BuildRequires

* Thu Jul 30 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-6
- rebase of hbaapi_build code

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-4
- added some info to description line
- replaced unoficial build source tarball with official one

* Tue Mar 31 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-3
- minor changes in spec file - filenames change, removal of
  duplicate patch files (included in build source tarball)
  
* Thu Mar 12 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-2
- correction of patches' names to correct format

* Tue Feb 24 2009 Chris Leech <christopher.leech@intel.com> - 2.2-1
- initial packaging of hbaapi 2.2
