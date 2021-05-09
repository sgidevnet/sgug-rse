%define foundryname  ctan
%define fontpkg      cm-lgc
%define fontname     %{foundryname}-%{fontpkg}
%define fontconf     64-%{fontname}
%define ctan_date    20051007
%define texfontpath  public/%{fontpkg}


# Common description
%define common_desc The CM-LGC PostScript Type 1 fonts are converted from the METAFONT \
sources of the Computer Modern font families. CM-LGC supports the T1, T2A, \
LGR, and TS1 encodings, i.e. Latin, Cyrillic, and Greek.


Name:           ctan-cm-lgc-fonts
Version:        0.5
Release:        31%{?dist}
Summary:        CM-LGC Type1 fonts
# Font exception
License:        GPLv2+ with exceptions
URL:            http://www.ctan.org/tex-archive/fonts/ps-type1/cm-lgc
Source0:        cm-lgc-%{ctan_date}.zip
# upstream source - unversioned zip file
# http://tug.ctan.org/fonts/ps-type1/cm-lgc.zip
Source1:        %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
BuildArch:      noarch
BuildRequires:  fontpackages-devel
%description
%{common_desc}


%package common
Summary:  CM-LGC Type 1 fonts, common files (documentation…)
Requires: fontpackages-filesystem
%description common
%common_desc
This package consists of files used by other ctan-cm-lgc-fonts packages.


%define romanfonts %{fontname}-roman-fonts
%package -n %{romanfonts}
Summary:   CM-LGC Type 1 fonts, serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{romanfonts}
%common_desc
This package contains the CM-LGC serif typeface based on Computer Modern.

%_font_pkg -n roman -f %{fontconf}-roman.conf fcm*


%define sansfonts %{fontname}-sans-fonts
%package -n %{sansfonts}
Summary:   CM-LGC Type 1 fonts, sans-serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{sansfonts}
%common_desc
This package contains the CM-LGC sans-serif typeface based on Computer Modern.

%_font_pkg -n sans -f %{fontconf}-sans.conf fcs*


%define typewriterfonts %{fontname}-typewriter-fonts
%package -n %{typewriterfonts}
Summary:   CM-LGC Type 1 fonts, typewriter font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{typewriterfonts}
%common_desc
This package contains the CM-LGC serif typeface based on Computer Modern.

%_font_pkg -n typewriter -f %{fontconf}-typewriter.conf fct*


%prep
%setup -q -a1 -n %{fontpkg}


%build


%install
#install .pfb and .afm files in %{_fontdir} as per the fedora font guidelines
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/type1/%{texfontpath}/* %{buildroot}%{_fontdir}
install -m 0644 -p fonts/afm/%{texfontpath}/* %{buildroot}%{_fontdir}

# fontconfig stuff (see spectemplate-fonts-multi.spec)
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p fontconfig/%{fontname}-roman.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-roman.conf
install -m 0644 -p fontconfig/%{fontname}-sans.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p fontconfig/%{fontname}-typewriter.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-typewriter.conf

for fconf in %{fontconf}-roman.conf \
             %{fontconf}-sans.conf \
             %{fontconf}-typewriter.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%files common
%doc COPYING HISTORY README
%dir %{_fontdir}


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb  8 2013 Jens Petersen <petersen@redhat.com> - 0.5-21
- drop tex-cm-lgc subpackage since it is now provided by texlive-cm-lgc
  so no longer need to BR non-existent texlive-texmf (#907728)
- update source link to http
- clean away deprecated buildroot lines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-15
- Address comments in https://bugzilla.redhat.com/show_bug.cgi?id=480589#c2
  (thanks Nicolas Mailhot)
    - Add a buildrequires for texlive-texmf
    - Remove Requires: fontpackages-filesystem from main and add to common
      subpackage.

* Fri Jan 16 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-14
- Rename the package to ctan-cm-lgc-fonts
- Name the subpackages according to 
  http://fedoraproject.org/wiki/PackagingDrafts/Font_package_naming_(2009-01-13)
- Update to fontpackages-* >= 1.15

* Tue Jan 13 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-13
- Divide font families into subpackages (roman, sans, typewriter)

* Mon Jan 12 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-12
- Minor package description enhancement.
- Explicit vr Requires to the subpackage.

* Mon Jan 12 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-11
- Restructure spec file according to
  https://fedoraproject.org/wiki/Fonts_SIG_Fedora_11_packaging_changes
  (bug #477461)
- Split package to cm-lgc-fonts (.pfb and .afm) and tetex-font-cm-lgc 
  (TeX stuff)
- Include .afm files (forgotten in the previous versions)

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.5-10
- fix license tag

* Fri Jan  4 2008 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-9
- Drop -fonts requires.

* Tue Aug 29 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-8
- Bump release for FC6 rebuild.

* Mon Feb 20 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-6
- Rebuild for FC5.

* Sun Nov  6 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-6
- Use run-time define updmap.cfg (Michal Jaegermann, bug #172491).

* Wed Nov  2 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-5
- Use absolute path commands in post and postun.

* Wed Nov  2 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-4
- Remove explicit outputdir for updmap-sys (bug #172268)
- Readd texhash in post and postun.

* Fri Oct  7 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-3
- Require tetex-fonts.
- Drop cm-lgc-test.tex.
- Use ctan zip soure.
- Other cleanups.

* Wed Jul  6 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-2
- Run updmap-sys only when installing, not when updating

* Wed Jun 15 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.5-1
- update to 0.5 (#160464)
- make the package tetex-3 compliant (use updmap-sys instead of updmap,
  update location for .enc and .map files).

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Nov 28 2004 Michael Schwendt <mschwendt[AT]users.sf.net>
- Make tarball file name unique.

* Sun Oct 17 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.3.1-1
- Updated to 0.3.1.

* Sat Jun  5 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.3-0.fdr.1
- Updated to 0.3.

* Wed May  5 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.2.1-0.fdr.2
- Removed INSTALL file (bug 997).
- Added cm-lgc-test.tex test document (bug 997).
- Moved preun script to postun (bug 997).
- Split Requires(post,postun) into separate Require statements (bug 997).

* Sun Nov 16 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.2.1-0.fdr.1
- Initial Fedora RPM release.
