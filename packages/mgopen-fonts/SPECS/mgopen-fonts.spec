%global fontname 	mgopen
%global fontconf        61-%{fontname}
%global archivename     MgOpen
%global upstream_date   20050515

# Common description
%global common_desc The MgOpen fonts are a font family that includes Latin and Greek glyphs.\
The fonts have been released under a liberal license, similar to the\
license covering the Bitstream Vera fonts.

# Compat description
%global compat_desc \
This package only exists to help transition pre Fedora 11 MgOpen font users to\
the new package split. It will be removed after one distribution release cycle,\
please do not reference it or depend on it in any way.\
\
It can be safely uninstalled.


Name:      %{fontname}-fonts
Version:   0.%{upstream_date}
Release:   32%{?dist}
Summary:   Truetype greek fonts

License:   MgOpen
URL:       http://www.ellak.gr/fonts/mgopen/
Source0:   %{archivename}-%{upstream_date}.tar.gz
# Upstream tarball is not versioned http://www.ellak.gr/fonts/mgopen/files/%{archivename}.tar.gz
Source1:   %{archivename}-%{upstream_date}-doc.tar.gz
# Tarball of the documentation on the site http://www.ellak.gr/fonts/mgopen/
# The LICENCE file is an excerpt from the html page
Source2:   %{fontname}-fontconfig.tar.gz
# Tarball of fontconfig files for each font
Source3:   %{fontname}.metainfo.xml
Source4:   %{fontname}-canonica.metainfo.xml
Source5:   %{fontname}-cosmetica.metainfo.xml
Source6:   %{fontname}-modata.metainfo.xml
Source7:   %{fontname}-moderna.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel
%description
%common_desc


%package common
Summary:  Truetype greek fonts, common files (documentation…)
Requires: fontpackages-filesystem
%description common
%common_desc
This package consists of files used by other MgOpen packages.



%package compat
Summary:   Truetype greek fonts, compatibility package
Obsoletes: mgopen-fonts < 0.20050515-8
Requires:  %{fontname}-canonica-fonts, %{fontname}-cosmetica-fonts,
Requires:  %{fontname}-modata-fonts, %{fontname}-moderna-fonts
%description compat
%common_desc
%compat_desc



%package -n %{fontname}-canonica-fonts
Summary:   Truetype variable-stroke-width serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-canonica-fonts
%common_desc
This package contains the MgOpen Canonica serif variable-stroke-width typeface,
which is based on the design of Times Roman.

%_font_pkg -n canonica -f %{fontconf}-canonica.conf MgOpenCanonica*.ttf
%{_datadir}/appdata/%{fontname}-canonica.metainfo.xml


%package -n %{fontname}-cosmetica-fonts
Summary:   Truetype variable-stroke-width sans serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-cosmetica-fonts
%common_desc
This package contains the MgOpen Cosmetica sans serif variable-stroke-width
typeface, which is  based on the design of Optima.

%_font_pkg -n cosmetica -f %{fontconf}-cosmetica.conf MgOpenCosmetica*.ttf
%{_datadir}/appdata/%{fontname}-cosmetica.metainfo.xml


%package -n %{fontname}-modata-fonts
Summary:   Truetype fixed-stroke-width sans serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-modata-fonts
%common_desc
This package contains the MgOpen Modata sans serif fixed-stroke-width
which is based on the design of VAG rounded.

%_font_pkg -n modata -f %{fontconf}-modata.conf MgOpenModata*.ttf
%{_datadir}/appdata/%{fontname}-modata.metainfo.xml


%package -n %{fontname}-moderna-fonts
Summary:   Truetype fixed-stroke-width sans serif font faces
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-moderna-fonts
%common_desc
This package contains the MgOpen Moderna sans serif fixed-stroke-width
typeface which is based on the design of Helvetica.

%_font_pkg -n moderna -f %{fontconf}-moderna.conf MgOpenModerna*.ttf
%{_datadir}/appdata/%{fontname}-moderna.metainfo.xml


%prep
%setup -q -c -a1 -a2 -n %{archivename}-%{version}
iconv -f ISO-8859-1 -t UTF-8 LICENCE > LICENCE.tmp; mv LICENCE.tmp LICENCE

%build

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p fontconfig/%{fontname}-canonica.conf \
	 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-canonica.conf
install -m 0644 -p fontconfig/%{fontname}-cosmetica.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-cosmetica.conf
install -m 0644 -p fontconfig/%{fontname}-modata.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-modata.conf
install -m 0644 -p fontconfig/%{fontname}-moderna.conf \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-moderna.conf

for fconf in %{fontconf}-canonica.conf \
                %{fontconf}-cosmetica.conf \
                %{fontconf}-modata.conf \
                %{fontconf}-moderna.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-canonica.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-cosmetica.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-modata.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-moderna.metainfo.xml

%files common
%doc LICENCE mgopen.html _files/
%{_datadir}/appdata/%{fontname}.metainfo.xml

%files compat

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20050515-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20050515-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20050515-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.20050515-29
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20050515-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20050515-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20050515-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20050515-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.20050515-23
- Add metainfo file to show this font in gnome-software
- Change %%define to %%global
- Remove %%clean section which is optional now
- Remove buildroot which is optional now
- Remove %%defattr
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050515-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.20050515-14
- Fix fontconfig file for moderna ,i.e. 
  https://bugzilla.redhat.com/show_bug.cgi?id=477425#c7

* Wed Jan 21 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.20050515-13
- Drop provides mgopen-fonts for the -compat subpackage.

* Wed Jan 21 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.20050515-12
- Fix typo in provides: fontpackages-filesystem
- Add provides mgopen-fonts to the -compat subpackage.

* Tue Jan 20 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.20050515-11
- Fix comments from https://bugzilla.redhat.com/show_bug.cgi?id=477425#c5
  (thanks Nicolas Mailhot)
  - remove requires: fontpackages-filesystem from the main package, add it
    to the -common subpackage.
  - put space around "<" in  Obsoletes to make rpm understand it
  - provide fontconfig substitution rules for all the families (according to 
    http://www.ellak.gr/fonts/mgopen/index.en.html)

* Mon Jan 19 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.20050515-10
- Rename subpackages according to 
  http://fedoraproject.org/wiki/PackagingDrafts/Font_package_naming_(2009-01-13)
- Differentiate between macro and variable (fontconf->fconf)

* Tue Dec 30 2008 Sarantis Paskalis <paskalis@di.uoa.gr> - 0.20050515-9
- Restructure spec file according to
  https://fedoraproject.org/wiki/Fonts_SIG_Fedora_11_packaging_changes
- Provide fontconfig files for the fonts
- Provide alias for VAG rounded --> Modata (bug #472835)

* Fri Dec 19 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.20050515-8
- It was decided that the license for these fonts is sufficiently different
  from Vera to require a different license tag.

* Mon Mar  3 2008 Sarantis Paskalis <paskalis@di.uoa.gr> 0.20050515-7
- Drop ancient Conflicts < fontconfig-2.3.93
- Convert LICENCE file to UTF-8
- Fix License description to Bitstream Vera
- Spec cleanup

* Sun Feb 10 2008 Sarantis Paskalis <paskalis@di.uoa.gr> 0.20050515-6
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Tue Aug 29 2006 Sarantis Paskalis <paskalis@di.uoa.gr> 0.20050515-5
- Rebuild for FC6.

* Mon Feb 20 2006 Sarantis Paskalis <paskalis@di.uoa.gr> 0.20050515-4
- Rebuild for FC5.

* Sat Jan 28 2006 Sarantis Paskalis <paskalis@di.uoa.gr> 0.20050515-3
- remove ghosting of %%{fontdir}/fonts.cache-{1,2} for new fontconfig

* Mon Oct 31 2005 Sarantis Paskalis <paskalis@di.uoa.gr> 0.20050515-2
- add %%{fontdir}/fonts.cache-2 to %%ghost files.

* Thu Jul  6 2005 Sarantis Paskalis <paskalis@di.uoa.gr> 0.20050515-1
- Fix spelling in the description.  Import it to Fedora Extras.

* Tue Jun 14 2005 Sarantis Paskalis <paskalis@di.uoa.gr>
- Use date-versioned sources

* Wed May 25 2005 Sarantis Paskalis <paskalis@di.uoa.gr>
- Initial package spec (based on bitstream-vera-fonts)
