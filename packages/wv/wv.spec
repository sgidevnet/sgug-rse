Name:       wv
Summary:    MSWord 6/7/8/9 binary file format to HTML converter
Version:    1.2.9
Release:    20%{?dist}
License:    GPLv2+
URL:        http://www.abisource.com/downloads/wv/
Source:     http://www.abisource.com/downloads/wv/%{version}/wv-%{version}.tar.gz
Patch1:     wv-aarch64.patch
Patch2:     format-security.patch

BuildRequires:  gcc
BuildRequires: glib2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: ImageMagick-devel
BuildRequires: pkgconfig
BuildRequires: libgsf-devel >= 1.11.2
Provides:   wvware = %{version}-%{release}

%description
Wv is a program that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.


%package        devel
Summary:        MSWord format converter - development files
Requires:       %{name} = %{version}-%{release}

%description    devel
Wv is a program that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.
This package contains the development files


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%configure

%build
%configure --disable-static

make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" -exec rm -f {} \;


#%%ldconfig_scriptlets


%files
%doc COPYING README
%{_bindir}/wv*
%{_datadir}/wv
%{_mandir}/man1/*
%{_libdir}/libwv*.so.*

%files      devel
%{_includedir}/wv
%{_libdir}/libwv*.so
%{_libdir}/pkgconfig/*


%changelog
* Sat Feb 06 2021  HAL <notes2@gmx.de> - 1.2.9-20
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.2.9-11
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.9-8
- add patch to support aarch64 (rhbz#926731)
- add patch to build with format security flag (rhbz#1037388)
- use make_install macro and drop redundant defattr

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.9-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.9-1
- 1.2.8 broke binary compatibility but was never imported in Fedora. 1.2.9 fixes it
- Fix bug 10025: Segfault trying to parse certain word documents (Jean Brefort)
- Fix bug 12746: Tables not imported from MS Word documents (Martin Sevior)
- Fix Bug 11433 wvWare hangs on this seemingly blank word doc (Martin Sevior)
- Buildfix: Remove unused LINK_WIN32_DLL check (Fridrich Strba)
- Buildfix: link with -no-undefined (Fridrich Strba)

* Tue Dec 22 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.7-2
- Workaround a incorrect soname bump

* Fri Dec 11 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.7-1
- New upstream release that fixes a regression
- Resolves rhbz#546406,546406

* Sun Nov 29 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.6-1
- Changelog at rhbz#511221

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 12 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.4-5
- rebuild to get provides pkgconfig(wv-1.0) >= 0:1.2.0

* Sun Mar 30 2008 Michel Salim <michel.sylvan@gmail.com> - 1.2.4-4
- fix libdir in wv's pkgconfig entry

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4-3
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.2.4-2
- fix license tag
- rebuild for BuildID

* Sat Oct 28 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.2.4-1
- update to 1.2.4, fixes #212696 (CVE-2006-4513)

* Fri Sep 08 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.2.1-7
- rebuild (releases 1 to 7, cvs problem)

* Fri Sep 08 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.2.1-1
- version 1.2.1

* Fri Apr 14 2006 Aurelien Bompard <gauret[AT]free.fr> 1.2.0-4
- rebuild

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 1.2.0-3
- don't build the static lib

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 1.2.0-2
- rebuild for FC5

* Fri Nov 11 2005 Aurelien Bompard <gauret[AT]free.fr> 1.2.0-1
- version 1.2.0

* Fri Oct 28 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0.3-2
- split out a -devel package (#171962)

* Sun May 15 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0.3-1%{?dist}
- new version
- fix build with gcc4
- use dist tag

* Tue May 10 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.0-5
- Include printf format fix for bug 150461.

* Thu Apr 07 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Jul 28 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.0-0.fdr.3
- fix security vulnerability (CAN-2004-0645)

* Fri May 14 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.0-0.fdr.2
- add several patches
- depend on glib2 (bug 1592)

* Wed May 12 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.0-0.fdr.1
- initial RPM (from Mandrake)
