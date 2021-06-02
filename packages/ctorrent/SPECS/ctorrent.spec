%define dnh dnh3.3.2

Name: ctorrent
Version: 1.3.4
Release: 32.%{dnh}%{?dist}
Summary: Command line BitTorrent client for unix-like environments
License: GPLv2+
URL: http://www.rahul.net/dholmes/ctorrent/
Source0: http://downloads.sourceforge.net/sourceforge/dtorrent/%{name}-%{dnh}.tar.gz
# http://sourceforge.net/tracker/download.php?group_id=202532&atid=981959&file_id=325065&aid=2782875
Patch0: %{name}-CVE-2009-1759.patch
BuildRequires:  gcc-c++
BuildRequires: openssl-devel
BuildRequires: gcc

%description
Enhanced CTorrent is a BitTorrent client for unix-like environments. High
performance with minimal system resources and dependencies are a priority.

%prep
%setup -q -n %{name}-%{dnh}
%patch0 -p0

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/ctorrent
%doc AUTHORS COPYING ChangeLog NEWS README README-DNH.TXT UserGuide

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-32.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-31.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-30.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.3.4-29.dnh3.3.2
- add gcc into buildrequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-28.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-27.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-26.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-25.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-24.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-23.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.4-22.dnh3.3.2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-21.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-20.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-19.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-18.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-17.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-16.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-15.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 22 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.4-14.dnh3.3.2
- rebuilt with new openssl

* Fri Aug 21 2009 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-12.dnh3.3.2
- fixed stack-based buffer overflow (CVE-2009-1759, RHBZ #501813)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-10.dnh3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 26 2009 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-9.dnh3.3.2
- update to 3.3.2 patch
- improve summary: and description

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-8.dnh3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.4-7.dnh3.2
- rebuild with new openssl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.4-6.dnh3.2
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.3.4-5
 - Rebuild for deps

* Fri Aug 17 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-4.dnh3.2
- update to latest patchlevel
- update License: tag in accordance with current guidelines
- add UserGuide to docs

* Wed Nov 01 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-3.dnh2.1
- upstream has stopped development, rebase to Enhanced CTorrent, fixes #212307
- add more docs

* Tue Oct 03 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-1
- update to 1.3.4
- mass rebuild

* Wed May 24 2006 Andrea Veri <bluekuja@ubuntu.com> 1.3.2-3
 - Added openssl-devel to BR
 - Removed libc.so.6 libc.so.6(GLIBC_2.0), libc.so.6(GLIBC_2.1) in BR
 - Description Changed
 - Fixed URL
 
* Sun Feb 1 2004 YuHong <bsdi@sina.com> 1.3.2
 - First Release


