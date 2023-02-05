Name:           goffice         
Version:        0.10.47
Release:        1%{?dist}
Summary:        G Office support libraries
License:        GPLv2+
URL:            http://projects.gnome.org/gnumeric/index.shtml
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.10/%{name}-%{version}.tar.xz
Patch100:       goffice.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.7
BuildRequires:  pkgconfig(lasem-0.4) >= 0.4.1
BuildRequires:  pkgconfig(libgsf-1) >= 1.14.24
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.22.0
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  perl(English)
BuildRequires:  perl(IO::Compress::Gzip)

%description
Support libraries for gnome office


%package devel
Summary:        Libraries and include files for goffice
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for goffice


%prep
%autosetup -p1

%build

%configure --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
V=1 %make_build


%install
%make_install
%find_lang goffice-%{version}
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/%{version}/plugins/*/*.la


#%%ldconfig_scriptlets


%files -f goffice-%{version}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/goffice/
%{_datadir}/goffice/

%files devel
%{_includedir}/libgoffice-0.10/
%{_libdir}/pkgconfig/libgoffice-0.10.pc
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/goffice-0.10/


%changelog
* Thu Apr 22 2021  HAL <notes2@gmx.de> - 0.10.47-1
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Mon May 11 2020 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.47-1
- Update to 0.10.47
- Add perl(English) to BuildRequires

* Wed Nov 13 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.46-1
- Update to 0.10.46

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.45-1
- Update to 0.10.45

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.44-1
- Update to 0.10.44

* Sat Aug 11 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.42-1
- Updated to 0.10.42
- Switched to %%autosetup

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.41-1
- Updated to 0.10.41

* Sun May 06 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.40-1
- Updated to 0.10.40

* Sat Mar 17 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.39-1
- Updated to 0.10.39
- Removed ldconfig scriptlets as per https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets
- Added gcc to BuildRequires as per https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequires_and_Requires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.38-1
- Updated to 0.10.38

* Tue Nov 21 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.36-1
- Updated to 0.10.36

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.35-1
- Updated to 0.10.35

* Mon Mar 27 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.34-1
- Updated to 0.10.34

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.33-1
- Updated to 0.10.33

* Sat Oct 29 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.32-2
- Added lasem support

* Sat Aug 27 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.32-1
- Updated to 0.10.32

* Mon Jun 20 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.30-1
- Updated to 0.10.30
- Spec file cleanups

* Sat May 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.29-1
- Updated to 0.10.29

* Wed Mar 23 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.28-1
- Updated to 0.10.28

* Sun Feb 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.27-1
- Updated to 0.10.27

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.25-1
- Updated to 0.10.25

* Mon Oct 26 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.24-1
- Updated to 0.10.24

* Thu Jul 30 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.23-1
- Updated to 0.10.23
- Dropped the patch included in the release

* Sat Jul 11 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.22-3
- Fixed RH bug 1240470 with a patch from upstream git

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.22-1
- Updated to 0.10.22

* Tue Apr 07 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.21-1
- Updated to 0.10.21

* Fri Feb 06 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.20-1
- Updated to 0.10.20

* Thu Jan 29 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.19-1
- Updated to 0.10.19

* Sat Sep 27 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.18-1
- Updated to 0.10.18

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.17-1
- Updated to 0.10.17

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.16-1
- Updated to 0.10.16

* Sun May 04 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.15-1
- Updated to 0.10.15

* Mon Apr 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.14-1
- Updated to 0.10.14

* Fri Mar 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.13-1
- Updated to 0.10.13

* Tue Mar 04 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.12-1
- Updated to 0.10.12
- Added libxslt-devel to BuildRequires
- Added %%{_datadir}/goffice to %%files
- Patched the bogus DESTDIR out

* Wed Feb 19 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.11-1
- Updated to 0.10.11

* Sun Feb 16 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.10-1
- Updated to 0.10.10

* Wed Jan 01 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.9-1
- Updated to 0.10.9

* Tue Oct 15 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.8-1
- Updated to 0.10.8

* Sat Sep 14 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.7-1
- Updated to 0.10.7

* Sun Aug 25 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.5-1
- Updated to 0.10.5

* Mon Aug  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.10.4-3
- Fix FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.4-1
- Updated to 0.10.4

* Sun Jun 30 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.3-1
- Updated to 0.10.3
- Corrected incorrect %%changelog dates

* Mon Apr 29 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.2-1
- Updated to 0.10.2

* Sat Mar 09 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.1-1
- Updated to 0.10.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.0-1
- Updated to 0.10.0

* Sun Nov 18 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.90-1
- Updated to 0.9.90

* Sun Sep 09 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.6-1
- Updated to 0.9.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.5-1
- Updated to 0.9.5
- Updated the License tag: goffice is now GPLv2+

* Tue Jun 26 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.4-1
- Updated to 0.9.4

* Sun Apr 22 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.3-1
- Updated to 0.9.3

* Tue Mar 13 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.2-1
- Updated to 0.9.2
- Resources are embedded now

* Sat Jan 07 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.1-1
- Updated to 0.9.1 and updated BuildRequires accordingly
- Updated the Source0 URL
- Updated the URL
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Streamlined -devel subpackage deps, rpm detects pkgconfig ones automatically

* Tue Dec  6 2011 Peter Robinson <pbrobinson@fedoraproject.org> -0.8.17-3
- add pcre-devel and pcre-tools

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.8.17-2
- Rebuild for new libpng

* Tue Aug 02 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.17-1
- Updated to 0.8.17

* Sat Jun 18 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.16-1
- Updated to 0.8.16
- Switched to .xz sources

* Sun May 22 2011 Julian Sikorski <belegdol@gmail.com> - 0.8.15-1
- Updated to 0.8.15

* Sat Mar 26 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.14-1
- Updated to 0.8.14

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.13-1
- Updated to 0.8.13

* Thu Dec 02 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.12-1
- Updated to 0.8.12

* Sat Oct 02 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.11-1
- Updated to 0.8.11

* Mon Sep 06 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.10-1
- Updated to 0.8.10

* Tue Aug 17 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.9-1
- Updated to 0.8.9

* Sat Jul 31 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.8-1
- Updated to 0.8.8

* Sun Jul 25 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.7-1
- Updated to 0.8.7

* Sat Apr 10 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.1-1
- Updated to 0.8.1

* Mon Feb 22 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.8.0-1
- New upstream

* Thu Dec 31 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.7.17-1
- New upstream version

* Tue Dec 01 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.7.16-2
- New build
- Version bump

* Wed Oct 21 2009 Robert Scheck <robert@fedoraproject.org> - 0.6.6-4
- Applied 3 patches from the 0.6 branch (#503068, #505001)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 31 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.6-1
- Updated to 0.6.6

* Mon Jan 12 2009 Caolán McNamara <caolanm@redhat.com> - 0.6.5-2
- rebuild to get provides pkgconfig(libgoffice-0.4) >= 0:0.4.0

* Sun Sep  7 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.5-1
- Updated to 0.6.5
- Development docs are now in goffice-0.6

* Wed Aug 27 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.4-1
- Updated to 0.6.4
- BuildRequires: pcre-devel only on Fedora < 9

* Sat Mar  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.2-1
- New upstream version 0.6.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.1-2
- Autorebuild for GCC 4.3

* Fri Jan 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.1-1
- Jump to upstream version 0.6.1 for new gnumeric
- Notice ABI and API changes!

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Thu Mar  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.2-1
- New upstream release 0.2.2
- Fix rpath usage on x86_64

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.1-2
- FE6 Rebuild

* Tue May  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.1-1
- new upstream version: 0.2.1

* Tue Mar 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-2
- rebuild for new libgsf

* Thu Feb 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-1
- New upstream version
- Remove .la files from plugin dirs
- Add BuildRequires: intltool gettext

* Mon Feb 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-4
- Bump release and rebuild for new gcc4.1 and glibc.
- add %%{?dist} for consistency with my other packages

* Thu Dec  8 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-3
-Switch to core version of libgsf now Core has 1.13 instead of using special
 Extras libgsf113 version.

* Mon Nov 28 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-2
-Make Source0 a full URL
-Better URL tag
-Fix not owning /usr/lib(64)/goffice and /usr/share/goffice

* Fri Nov 25 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-1
-change name to goffice as that is the upstream tarbal name.
-bump to 0.1.2 this is the minimal version supported by gnumeric-1.6
-use extras libgsf113 package since core libgsf is to old
-use locale macros
-don't ship .la files
-remove some redundant (already included in other) (Build)Requires

* Sat Nov 05 2005 Michael Wise <micwise at gmail.com> - 0.0.4-1
- Initial spec file
