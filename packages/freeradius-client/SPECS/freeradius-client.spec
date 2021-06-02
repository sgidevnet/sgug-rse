Summary: RADIUS protocol client library
Name: freeradius-client
Version: 1.1.7
Release: 20%{?dist}
# For a breakdown of the licensing, see PACKAGE-LICENSING 
License: BSD and MIT
URL: http://freeradius.org/freeradius-client/
Source0: ftp://ftp.freeradius.org/pub/freeradius/%{name}-%{version}.tar.gz
Source1: radiusclient.conf
Source2: PACKAGE-LICENSING
Source3: dictionary
Patch1: freeradius-client-1.1.7-size_t.patch
Patch2: freeradius-client-1.1.7-ipv6-attr-fix.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: nettle-devel >= 2.7.1

%description
FreeRADIUS Client is a library for writing RADIUS Clients.
The library lets you develop a RADIUS-aware application in less than
50 lines of C code. 

%package devel
Summary: Development files for freeradius-client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for freeradius-client.

%package utils
Summary: Utility programs for freeradius-client
Requires: %{name}%{?_isa} = %{version}-%{release}
# freeradius-client supersedes radiusclient-ng
Obsoletes: radiusclient-ng-utils

%description utils
FreeRADIUS Client is a framework and library for writing RADIUS Clients.
This package includes radius client test utilities such as,
radiusclient, radexample, radstatus, radembedded and radacct.

%prep
%setup -q
rm -f lib/md5.c
sed -i -e 's|sys_lib_dlsearch_path_spec="[^"]\+|& %{_libdir}|g' configure

%patch1 -p1 -b .size_t
%patch2 -p1 -b .attr

%build

%configure --disable-static --disable-rpath --with-nettle
make %{?_smp_mflags}

%install
cp -a %{SOURCE2} PACKAGE-LICENSING
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_sbindir}/login.radius

mkdir -p %{buildroot}%{_datadir}/radiusclient
mv %{buildroot}%{_sysconfdir}/radiusclient/dictionary.* %{buildroot}%{_datadir}/radiusclient/
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/radiusclient/
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/radiusclient/
cp %{SOURCE3} %{buildroot}%{_datadir}/radiusclient/dictionary

%ldconfig_scriptlets

%files
%doc README.rst README.radexample BUGS doc/ChangeLog
%license COPYRIGHT PACKAGE-LICENSING

%dir %{_sysconfdir}/radiusclient
%config(noreplace) %{_sysconfdir}/radiusclient/issue
%config(noreplace) %{_sysconfdir}/radiusclient/port-id-map
%config(noreplace) %{_sysconfdir}/radiusclient/radiusclient.conf
%config(noreplace) %{_sysconfdir}/radiusclient/servers
%config(noreplace) %{_sysconfdir}/radiusclient/dictionary

%{_libdir}/libfreeradius-client.so.*

%dir %{_datadir}/radiusclient/
%{_datadir}/radiusclient/dictionary.ascend
%{_datadir}/radiusclient/dictionary.compat
%{_datadir}/radiusclient/dictionary.merit
%{_datadir}/radiusclient/dictionary.sip
%{_datadir}/radiusclient/dictionary

%files devel

%{_includedir}/freeradius-client.h
%{_libdir}/libfreeradius-client.so

%files utils

%{_sbindir}/radacct
%{_sbindir}/radiusclient
%{_sbindir}/radstatus
%{_sbindir}/radlogin
%{_sbindir}/radexample
%{_sbindir}/radembedded

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.1.7-18
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.7-16
- Add gcc and make as BR (minimal buildroot change)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.1.7-14
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  8 2015 Nikos Mavrogiannopoulos - 1.1.7-8
- Ship a custom dictionary; that corrects the IPv6 dictionary types.

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.7-7
- Rebuilt for nettle soname bump

* Tue Mar 24 2015 Nikos Mavrogiannopoulos - 1.1.7-6
- when sending IPv6 attributes use the correct length (#1205156)

* Mon Feb 23 2015 Nikos Mavrogiannopoulos - 1.1.7-5
- Corrected paths of files includes in config file

* Wed Feb 11 2015 Nikos Mavrogiannopoulos - 1.1.7-4
- Added utils subpackage

* Wed Jan 28 2015 Nikos Mavrogiannopoulos - 1.1.7-3
- Line wrapped description message
- Commented out the utils subpackage

* Tue Jan 27 2015 Nikos Mavrogiannopoulos - 1.1.7-2
- Cleanup licensing
- Link to main upstream web page
- Properly obsolete radiusclient-ng-utils
- Remove dependencies on autotools

* Thu Jan 22 2015 Nikos Mavrogiannopoulos - 1.1.7-1
- New upstream release

* Mon Dec  8 2014 Nikos Mavrogiannopoulos - 1.1.6.20141208-1.gite261681
- Rebase on git repository

* Fri Dec  5 2014 Nikos Mavrogiannopoulos - 1.1.6-1
- Initial package release


