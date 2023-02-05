%global fontname culmus
%global fontconfd 65-%{fontname}
%global fontconf 66-%{fontname}

%global common_desc \
The culmus-fonts package contains fonts for the display of\
Hebrew from the Culmus project.


Name:           %{fontname}-fonts
Version:        0.130
Release:        15%{?dist}
Summary:        Fonts for Hebrew from Culmus project

License:        GPLv2
URL:            http://culmus.sourceforge.net
Source0:        http://downloads.sourceforge.net/culmus/%{fontname}-%{version}.tar.gz
Source1:        %{fontconf}-aharoni-clm.conf
Source2:        %{fontconf}-caladings-clm.conf
Source3:        %{fontconfd}-david-clm.conf
Source4:        %{fontconf}-drugulin-clm.conf
Source5:        %{fontconf}-ellinia-clm.conf
Source6:        %{fontconf}-frank-ruehl-clm.conf
Source7:        %{fontconf}-miriam-clm.conf
Source8:        %{fontconf}-miriam-mono-clm.conf
Source9:        %{fontconf}-nachlieli-clm.conf
Source10:        %{fontconf}-hadasim-clm.conf
Source11:        %{fontconf}-keteryg.conf
Source12:        %{fontconf}-simple-clm.conf
Source13:        %{fontconf}-stamashkenaz-clm.conf
Source14:        %{fontconf}-stamsefarad-clm.conf
Source15:        %{fontconf}-shofar.conf
Source16:        http://downloads.sourceforge.net/culmus/culmus-type1-0.121.tar.gz
Obsoletes:      culmus-fonts < 0.102-1

#for appstream metainfo
Source50:       %{fontname}-aharoni-clm.metainfo.xml
Source51:       %{fontname}-caladings-clm.metainfo.xml
Source52:       %{fontname}-david-clm.metainfo.xml
Source53:       %{fontname}-drugulin-clm.metainfo.xml
Source54:       %{fontname}-ellinia-clm.metainfo.xml
Source55:       %{fontname}-frank-ruehl-clm.metainfo.xml
Source56:       %{fontname}-hadasim-clm.metainfo.xml
Source57:       %{fontname}-keteryg.metainfo.xml
Source58:       %{fontname}-miriam-clm.metainfo.xml
Source59:       %{fontname}-miriam-mono-clm.metainfo.xml
Source60:       %{fontname}-nachlieli-clm.metainfo.xml
Source61:       %{fontname}-simple-clm.metainfo.xml
Source62:       %{fontname}-stamashkenaz-clm.metainfo.xml
Source63:       %{fontname}-stamsefarad-clm.metainfo.xml
Source64:       %{fontname}-yehuda-clm.metainfo.xml
Source65:       %{fontname}-shofar.metainfo.xml
Source66:       %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc
Meta-package of Culmus fonts which installs various families of culmus project.

%package common
Summary:        Common files of culmus-fonts
Requires:       fontpackages-filesystem
%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-aharoni-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-aharoni-clm-fonts
%common_desc

%_font_pkg -n aharoni-clm -f %{fontconf}-aharoni-clm.conf AharoniCLM-*.afm AharoniCLM-*.pfa
%{_datadir}/appdata/%{fontname}-aharoni-clm.metainfo.xml

%package -n %{fontname}-caladings-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-caladings-clm-fonts
%common_desc

%_font_pkg -n caladings-clm -f %{fontconf}-caladings-clm.conf CaladingsCLM.afm CaladingsCLM.pfa
%{_datadir}/appdata/%{fontname}-caladings-clm.metainfo.xml

%package -n %{fontname}-david-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-david-clm-fonts
%common_desc

%_font_pkg -n david-clm -f %{fontconfd}-david-clm.conf DavidCLM-*.ttf DavidCLM-*.afm DavidCLM-*.pfa
%{_datadir}/appdata/%{fontname}-david-clm.metainfo.xml

%package -n %{fontname}-drugulin-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-drugulin-clm-fonts
%common_desc

%_font_pkg -n drugulin-clm -f %{fontconf}-drugulin-clm.conf DrugulinCLM-*.afm DrugulinCLM-*.pfa
%{_datadir}/appdata/%{fontname}-drugulin-clm.metainfo.xml

%package -n %{fontname}-ellinia-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-ellinia-clm-fonts
%common_desc

%_font_pkg -n ellinia-clm -f %{fontconf}-ellinia-clm.conf ElliniaCLM-*.afm ElliniaCLM-*.pfa
%{_datadir}/appdata/%{fontname}-ellinia-clm.metainfo.xml

%package -n %{fontname}-frank-ruehl-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-frank-ruehl-clm-fonts
%common_desc

%_font_pkg -n frank-ruehl-clm -f %{fontconf}-frank-ruehl-clm.conf FrankRuehlCLM-*.ttf  FrankRuehlCLM-*.afm FrankRuehlCLM-*.pfa
%{_datadir}/appdata/%{fontname}-frank-ruehl-clm.metainfo.xml


%package -n %{fontname}-hadasim-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-hadasim-clm-fonts
%common_desc

%_font_pkg -n hadasim-clm -f %{fontconf}-hadasim-clm.conf HadasimCLM-*.ttf
%{_datadir}/appdata/%{fontname}-hadasim-clm.metainfo.xml

%package -n %{fontname}-keteryg-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-keteryg-fonts
%common_desc

%_font_pkg -n keteryg -f %{fontconf}-keteryg.conf KeterYG-*.ttf
%{_datadir}/appdata/%{fontname}-keteryg.metainfo.xml


%package -n %{fontname}-miriam-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-miriam-clm-fonts
%common_desc

%_font_pkg -n miriam-clm -f %{fontconf}-miriam-clm.conf MiriamCLM-*.ttf MiriamCLM-*.afm MiriamCLM-*.pfa
%{_datadir}/appdata/%{fontname}-miriam-clm.metainfo.xml

%package -n %{fontname}-miriam-mono-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-miriam-mono-clm-fonts
%common_desc

%_font_pkg -n miriam-mono-clm -f %{fontconf}-miriam-mono-clm.conf MiriamMonoCLM-*.ttf MiriamMonoCLM-*.afm MiriamMonoCLM-*.pfa
%{_datadir}/appdata/%{fontname}-miriam-mono-clm.metainfo.xml

%package -n %{fontname}-nachlieli-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-nachlieli-clm-fonts
%common_desc

%_font_pkg -n nachlieli-clm -f %{fontconf}-nachlieli-clm.conf NachlieliCLM-*.afm NachlieliCLM-*.pfa
%{_datadir}/appdata/%{fontname}-nachlieli-clm.metainfo.xml


%package -n %{fontname}-simple-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-simple-clm-fonts
%common_desc

%_font_pkg -n simple-clm -f %{fontconf}-simple-clm.conf SimpleCLM-*.ttf
%{_datadir}/appdata/%{fontname}-simple-clm.metainfo.xml

%package -n %{fontname}-stamashkenaz-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-stamashkenaz-clm-fonts
%common_desc

%_font_pkg -n stamashkenaz-clm -f %{fontconf}-stamashkenaz-clm.conf StamAshkenazCLM.ttf
%{_datadir}/appdata/%{fontname}-stamashkenaz-clm.metainfo.xml

%package -n %{fontname}-stamsefarad-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-stamsefarad-clm-fonts
%common_desc

%_font_pkg -n stamsefarad-clm -f %{fontconf}-stamsefarad-clm.conf StamSefaradCLM.ttf
%{_datadir}/appdata/%{fontname}-stamsefarad-clm.metainfo.xml


%package -n %{fontname}-yehuda-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-yehuda-clm-fonts
%common_desc

%_font_pkg -n yehuda-clm YehudaCLM-*.afm YehudaCLM-*.pfa
%{_datadir}/appdata/%{fontname}-yehuda-clm.metainfo.xml

%package -n %{fontname}-shofar-fonts
Summary:        Fonts for Hebrew from Culmus project
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-shofar-fonts
%common_desc

%_font_pkg -n shofar -f %{fontconf}-shofar.conf Shofar*.ttf
%{_datadir}/appdata/%{fontname}-shofar.metainfo.xml

%prep
%setup -q -n %{fontname}-%{version}
%setup -c -q -a 16
mv %{fontname}-%{version}/* .
mv %{fontname}-type1-0.121/* .

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0644 -p *.afm %{buildroot}%{_fontdir}
install -m 0644 -p *.pfa %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-aharoni-clm.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caladings-clm.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconfd}-david-clm.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-drugulin-clm.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ellinia-clm.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-frank-ruehl-clm.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-clm.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-mono-clm.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nachlieli-clm.conf
install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-hadasim-clm.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-keteryg.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-simple-clm.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stamashkenaz-clm.conf
install -m 0644 -p %{SOURCE14} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stamsefarad-clm.conf
install -m 0644 -p %{SOURCE15} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shofar.conf

for fconf in %{fontconf}-aharoni-clm.conf \
             %{fontconf}-caladings-clm.conf \
             %{fontconfd}-david-clm.conf \
             %{fontconf}-drugulin-clm.conf \
             %{fontconf}-ellinia-clm.conf \
             %{fontconf}-frank-ruehl-clm.conf \
             %{fontconf}-miriam-clm.conf \
             %{fontconf}-miriam-mono-clm.conf \
             %{fontconf}-nachlieli-clm.conf \
             %{fontconf}-hadasim-clm.conf \
             %{fontconf}-keteryg.conf \
             %{fontconf}-simple-clm.conf \
             %{fontconf}-stamashkenaz-clm.conf \
             %{fontconf}-stamsefarad-clm.conf \
             %{fontconf}-shofar.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE50} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-aharoni-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE51} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-caladings-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE52} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-david-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE53} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-drugulin-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE54} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-ellinia-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE55} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-frank-ruehl-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE56} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-hadasim-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE57} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-keteryg.metainfo.xml
install -Dm 0644 -p %{SOURCE58} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-miriam-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE59} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-miriam-mono-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE60} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-nachlieli-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE61} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-simple-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE62} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-stamashkenaz-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE63} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-stamsefarad-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE64} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-yehuda-clm.metainfo.xml
install -Dm 0644 -p %{SOURCE65} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-shofar.metainfo.xml
install -Dm 0644 -p %{SOURCE66} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


%files common
%doc CHANGES GNU-GPL LICENSE LICENSE-BITSTREAM 
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 06 2016 Pravin Satpute <psatpute@redhat.com> - 0.130-9
- Resolved #1217066 : culmus-keteryg-fonts takes over Firefox?
- Update fontconf priority of all fonts from 65 to 66, except David

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.130-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.130-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 11 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.130-6
- Add metainfo file to show this font in gnome-software
- Remove owneship of %%{_fontdir} in -common
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.130-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-4
- Resolved #1002085 :- Removed old obsoletes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.130-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-2
- Resolved #975735 :- Typo in fontconfig file

* Wed Mar 20 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-1
- Upstream release 0.130 new family Shofar
- Resolved #923153

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-4
- Spec file cleanup #878538

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-2
- Resolves bug 837533

* Mon Jan 30 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-1
- Upstream new release 0.121 with Frank Ruehl OT

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Pravin Satpute <psatpute@redhat.com> - 0.120-1
- Upstream new release.
- Added new families Hadasim CLM, Keter YG, Simple CLM, Stam Ashkenaz CLM, Stam Sefarad CLM

* Fri Sep 03 2010 Pravin Satpute <psatpute@redhat.com> - 0.105-1
- Upstream new release.
- Miriam Mono family is now OpenType and has diacritics support developed by Yoram Gnat.

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-3
- fixed bug 578018 .conf file

* Fri Feb 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-2
- updated .conf file priorities
- fixed bug 565385

* Fri Feb 12 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-1
- new upstream release

* Tue Jan 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.103-5
- fixed compat package bug 484621

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-3
- added DavidCLM afm and pfa
- bug 509694

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-1
- upstream new release 0.103

* Tue Apr 14 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-6.fc11
- Rebuild for bug #491957.

* Thu Mar 19 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-5.fc11
- Corrected Obsoletes for compat.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-3.fc11
- Modified -compat.

* Mon Feb 09 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-2.fc11
- Created -compat for subpackage for smooth upgrade.

* Wed Feb 04 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-1.fc11
- Updated version.
- Following new font packaging guidelines.

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-5.fc10
- Obsoleted dead package fonts-hebrew

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-4.fc8
- License change

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-3.fc8
- Updated according to the review

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-2.fc8
- Using common spec template for font packages

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-1.fc8
- Font directory and package name corrected and updated the version

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.100-1.fc8
- Split package from fonts-hebrew to reflect upstream project name
