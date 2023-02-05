Name:           dbench
Version:        4.0 
Release:        20%{?dist}
Summary:        Filesystem load benchmarking tool

License:        GPLv2+
Source0:        http://samba.org/ftp/tridge/dbench/dbench-%{version}.tar.gz 
URL:            http://samba.org/ftp/tridge/dbench/README
Patch0:         dbench-4.0-destdir.patch
Patch1:         dbench-4.0-datadir.patch
BuildRequires:  gcc
BuildRequires:  autoconf popt-devel
  
%description
Dbench is a file system benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring a
lab of Windows load generators to run. It is now considered a de facto
standard for generating load on the Linux VFS.

%prep
%setup -q
%patch0 -p1 -b .destdir 
%patch1 -p1 -b .datadir

%build
./autogen.sh 
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}/man1 INSTALLCMD='install -p'


%files
%doc README COPYING
%dir %{_datadir}/dbench
%{_datadir}/dbench/client.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 14 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 4.0-2
- Fix BR's
* Mon Apr 14 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 4.0-1
- Fix patch
* Mon Apr 14 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 4.0-0
- New upstream release 4.0
* Sat Feb 9 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 3.04-7
- Rebuild for GCC 4.3
* Tue Sep 11 2007 Rahul Sundaram<sundaram@redhat.com> - 3.04-6
- Drop redundant version macro
* Tue Sep 11 2007 Rahul Sundaram<sundaram@redhat.com> - 3.04-5
- Fix version. Dropped BR on glibc-headers
* Tue Sep 11 2007 Rahul Sundaram<sundaram@redhat.com> - 3.04-4
- Fixed docs
* Tue Sep 11 2007 Rahul Sundaram<sundaram@redhat.com> - 3.04-3
- Fixed description, man page location, timestamps, BR and license tag
* Wed Jul 11 2007 John (J5) Palmieri <johnp@redhat.com> - 3.04-2
- add patch to move client.txt to %%{_datadir}/dbench and have the app look
  there for the file
* Wed Jun 20 2007 John (J5) Palmieri <johnp@redhat.com> - 3.04-1
- add patch to respect DESTDIR
- realy make and make install dbench
- place client.txt file in a sane location
* Wed Jun 20 2007 Rahul Sundaram <sundaram@redhat.com>
- split from olpc-utils as suggested in review. Based on the spec from J5
