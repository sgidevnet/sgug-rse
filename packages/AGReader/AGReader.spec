Name:           AGReader
Version:        1.2
Release:        23%{?dist}
Summary:        Console reader for viewing AmigaGuide files
License:        GPL+
URL:            http://main.aminet.net/misc/unix/
Source0:        http://main.aminet.net/misc/unix/%{name}.tar.bz2
Source1:        agr.1
BuildRequires:  gcc

%description
A viewer for the UNIX console which can read and display AmigaGuide files. It
supports all of the v39 AmigaGuide specification possible and supports a large
subset of the v40 specifications.


%prep
%setup -qn %{name}


%build
make -C Sources %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1
install -m0755 Sources/agr %{buildroot}%{_bindir}



%files
%{_bindir}/agr
%{_mandir}/man1/agr.1.gz
%doc Docs/agr.guide Docs/test.guide Docs/agr.html README


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2-21
- Fix BRs.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2-5
- Autorebuild for GCC 4.3

* Sat Oct 13 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.2-4
- Added man page

* Tue Aug 21 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.2-3
- Release bump for F8 mass rebuild
- License change due to new guidelines
- A few cosmetic cleanups of the spec file

* Mon Aug 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.2-2
- Release bump for FC6 mass rebuild

* Mon Jun 05 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.2-1
- Version bump
- Dropped patches, they are no longer required
- Changed URL to use primary site, rather than a mirror

* Sun May 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-9
- Updated keys patch which fixes the keys under BOTH the console and an
  xterm, courtesy of Hans de Goede
- Added provides to offer lower case alias in preparation for probable
  policy change

* Sat May 27 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-8.iss
- Added patch to fix compilation with gcc41 courtesy of Hans de Goede
- Added patch to fix Home, End, F1, F2, F3 keys courtesy of Hans de Goede
- Added rpmoptflags to make line
- Removed compat-gcc-32 buildrequires - obsoleted by gcc41 patch.
- Use %%{?dist} for most recent changelog entry - avoids incoherent changelog
  versions if %%{?dist} macro is missing or different.

* Sat May 13 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-7.iss
- Removed gcc32 patch. It's now specified on the make command line
- Replaced %%{__rm} in clean section with rm

* Mon May 01 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-6.iss
- Altered spec file to more closely follow Fedora build guidelines

* Tue Oct 25 2004 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-5.iss
- Fixes for deprecated fields with the latest version of rpmbuild

* Thu Dec 04 2003 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-4
- Minor fixes to changelog
- Fixed permissions on documentation directory
- Changed group to Applications/Text

* Sun Oct 05 2003 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-3
- Minor fixes to prep and clean

* Fri Jul 18 2003 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-2
- Fixed few harmless bugs in SPEC file. Improved use of Macros.
