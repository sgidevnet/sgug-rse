Name:           aiksaurus
Version:        1.2.1
Release:        41%{?dist}
Summary:        An English-language thesaurus library

Epoch:          1
License:        GPLv2+
URL:            http://aiksaurus.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch0:         %{name}-1.2.1-gcc43.patch
Patch1:         %{name}-security.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils

%description
Aiksaurus is an English-language thesaurus library that can be 
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.  A basic command line 
thesaurus program is also included.

%package devel
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        Files for developing with aiksaurus
                                                                               
%description devel
Includes and definitions for developing with aiksaurus.

%package gtk
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        A GTK+ interface for aiksaurus

%description gtk
AiksaurusGTK is a GTK+ interface to the Aiksaurus library.
It provides an attractive thesaurus interface, and can be embedded
in GTK+ projects, notably AbiWord.

%package gtk-devel
Requires:       %{name}-gtk = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gtk2-devel
Summary:        Files for developing with aiksaurus-gtk
                                                                               
%description gtk-devel
gtk includes and definitions for developing with aiksaurus.

%package thesaurus
Requires:       %{name}-gtk = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        A GTK+ frontend to aiksaurus

%description thesaurus
A standalone thesaurus program base on aiksaurus-gtk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool 
make %{?_smp_mflags}

%install
%make_install

# Remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete

# Add the desktop icon.
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# Add desktop file.
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}

#%%ldconfig_scriptlets
#%%ldconfig_scriptlets gtk

%files
%doc ChangeLog README COPYING AUTHORS
%{_bindir}/%{name}
%{_bindir}/caiksaurus
%{_libdir}/*Aiksaurus-*.so*
%{_datadir}/%{name}/

%files devel
%dir %{_includedir}/Aiksaurus
%{_includedir}/Aiksaurus/Aiksaurus.h
%{_includedir}/Aiksaurus/AiksaurusC.h
%{_libdir}/*Aiksaurus.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files gtk
%{_libdir}/*GTK*.so.*

%files gtk-devel
%{_includedir}/Aiksaurus/AiksaurusGTK*.h
%{_libdir}/*GTK*.so
%{_libdir}/pkgconfig/gaiksaurus-1.0.pc

%files thesaurus
%{_bindir}/gaiksaurus
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Feb 06 2021  HAL <notes2@gmx.de> - 1:1.2.1-41
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:1.2.1-32
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1:1.2.1-31
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1:1.2.1-27
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- disable rpath

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-25
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1:1.2.1-23
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 30 2009 Matthias Clasen <mclasen@redhat.com> - 1:1.2.1-21
- Split off a thesaurus subpackage

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 10 2008 Matt Domsch <mdomsch@fedoraproject.org> - 1:1.2.1-18
- fix FTBFS #434484

* Fri Jun 13 2008 Jon Stanley <jonstanley@gmail.com> - 1:1.2.1-17
- Remove vendor tag, correct license, rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.2.1-16
- Autorebuild for GCC 4.3

* Mon Sep 11 2006 Marc Maurer <uwog@uwog.net> - 1:1.2.1-15.fc6
- Add dist to the release version

* Tue Mar 28 2006 Marc Maurer <uwog@uwog.net> - 1:1.2.1-14
- Add Red Hat, Inc. as vendor

* Fri Feb 17 2006 Marc Maurer <uwog@uwog.net> - 1:1.2.1-13
- Fix buildrequires for aiksaurus-gtk-devel too

* Fri Feb 17 2006 Marc Maurer <uwog@uwog.net> - 1:1.2.1-12
- Fix buildrequires for aiksaurus-gtk and -devel

* Tue Jan 24 2006 Brian Pepple <bdpepple@ameritech.net> - 1:1.2.1-11
- Add desktop icon.
- Remove those pesky periods from the summaries.
- Add smp_mflag.
- Correct desktop file to meet FE requirements.
- Correct ownership of datadir.
- Correct sub-packages dependencies.
- Drop PreReq (depreciated), and use requires.
- Use preferred FE build root.

* Wed Aug 17 2005 Marc Maurer <uwog@abisource.com> 1:1.2.1-10
- Rebuild against new libcairo

* Fri Jul 8 2005 Marc Maurer <uwog@abisource.com> 1:1.2.1-9
- Add URL

* Sat Jun 25 2005 Colin Charles <colin@fedoraproject.org> 1:1.2.1-8
- Fix download URL

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1:1.2.1-7
- rebuild on all arches

* Thu Mar 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.2.1-6
- add dep gtk2-devel for pkgconfig in -gtk-devel sub-package 
- include %%{_includedir}/Aiksaurus dir in -devel sub-package
- remove redundant deps "gtk2" and "aiksaurus" in -gtk sub-package

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com> 1.2.1-5
- rebuild with gcc4

* Mon Jan 24 2005 Caolan McNamara <caolanm@redhat.com> 1.2.1-4
- RH#145922# wrong location

* Mon Jan 24 2005 Caolan McNamara <caolanm@redhat.com> 1.2.1-3
- RH#145922# make a .desktop for gaiksaurus

* Wed Oct 10 2004 Caolan McNamara <caolanm@redhat.com> 1.2.1-2
- #rh134808# BuildRequires gtk2-devel

* Tue Aug 10 2004 Caolan McNamara <caolanm@redhat.com>
- initially import 1.2.1 and tweak .spec
