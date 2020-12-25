Name:           libspectrum
Version:        1.4.4
Release:        1%{?dist}
Summary:        A library for reading spectrum emulator file formats
License:        GPLv2+
URL:            http://fuse-emulator.sourceforge.net/libspectrum.php
Source0:        http://downloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
BuildRequires:  audiofile-devel >= 0.2.3
BuildRequires:  bzip2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  zlib-devel
#required by generate.pl
BuildRequires:  perl

%description
A library for reading various spectrum emulator file formats.


%package devel
Summary:    Development files for libspectrum
Requires:   %{name} = %{version}-%{release}
Requires:   libgcrypt-devel

%description devel
Development files for libspectrum.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"


#%%ldconfig_scriptlets



%files
%{_libdir}/libspectrum.so.*
%{_mandir}/man3/libspectrum.3*
%doc README ChangeLog THANKS AUTHORS COPYING


%files devel
%exclude %{_libdir}/libspectrum.la
%{_libdir}/libspectrum.so
%{_includedir}/libspectrum.h
%{_libdir}/pkgconfig/libspectrum.pc
%doc doc/libspectrum.txt


%changelog
* Tue Aug 18 2020  HAL <notes2@gmx.de> - 
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Aug 09 2019 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.4-1
- update to latest upstream ver

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.3-2
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.1-1
- new upstream release

* Thu Sep 28 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.0-1
- new upstream release

* Tue Aug 22 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.6-2
- update BR

* Mon Aug 21 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.6-1
- new upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.5-1
- new upstream release

* Sun May 14 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.3-2
- missing sources

* Sun May 14 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.3-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.2-2
- forgot sources file

* Sat Dec 10 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.2-1
- new upstream release

* Tue Nov 15 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.1-2
- catch with updated sources file

* Tue Nov 15 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.1-1
- new upstream release

* Tue Oct 04 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.0-2
- new upstream release

* Thu Sep 01 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.2-1
- new upstream release

* Wed Jul 20 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.1-1
- new upstream release

* Sat Jun 11 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.0-2
- bump version to catch with fuse-emulator builds

* Tue Jun 07 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.0-1
- update to latest upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Tomas Mraz <tmraz@redhat.com> - 1.1.1-3
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Lucian Langa <cooly@gnome.eu.org> - 1.1.1-1
- new upstream release

* Tue May 21 2013 Lucian Langa <cooly@gnome.eu.org> - 1.1.0-1
- new upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 Lucian Langa <cooly@gnome.eu.org> - 1.0.0-5
- rebuilt with newer libaudiofile

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Lucian Langa <cooly@gnome.eu.org> - 1.0.0-1
- new upstream release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Lucian Langa <cooly@gnome.eu.org> - 0.5.0-1
- new upstream 0.5.0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-2
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.0-1
- Upgrade to 0.4.0

* Tue Aug 21 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.3.0.1-3
- Release bump for F8 mass rebuild
- License change due to new guidelines

* Sat Jun 30 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.3.0.1-2
- Release bump

* Sat Jun 30 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.3.0.1-1
- Upgrade to 0.3.0.1
- Changes to spec due to new guidelines

* Fri Nov 11 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.2.2-4
- Renamed spec file

* Fri Nov 11 2005 Paul Howarth <paul@city-fan.org> 0.2.2-3
- Remove Packager: tag
- Use full URL for source
- Use standard Fedora Extras buildroot
- Add buildreqs bzip2-devel, libgcrypt-devel, glib2-devel
- Add libgcrypt-devel req for -devel subpackage
- Unpack tarball quietly
- Don't build or include static library
- Use DESTDIR with make instead of %%makeinstall
- Honour %%{?_smp_mflags}
- Move manpage to -devel subpackage

* Mon Oct 17 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0-2.2-2.3
- Multiple fixes to the spec file to bring it into line with FC rules

* Mon Jul 11 2005 Paul Johnson <paul@all-the-johnsons.co.uk> - 0.2.2-2.iss
- Rebuild for Fedora Core 4
- Slight alteration to SPEC file for it to work with the Fedora RPM tools

* Mon Feb 28 2005 Ian Chapman <packages[AT]amiga-hardware.com> - 0.2.2-2.iss
- Change log duplicated in spec file, fixed.

* Mon Jul 19 2004 Ian Chapman <packages[AT]amiga-hardware.com> - 0.2.2-1.iss
- Upgraded to version 0.2.2
- RPM built for Fedora Core 2

* Fri Dec 05 2003 Ian Chapman <packages[AT]amiga-hardware.com> - 0.2.0.1-2
- Minor changes to changelog
- Improved use of macros
- Moved appropriate files to devel package

* Mon Dec 01 2003 Ian Chapman <packages[AT]amiga-hardware.com> - 0.2.0.1-1
- Initial Release
