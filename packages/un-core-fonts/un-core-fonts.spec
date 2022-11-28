%global fontname un-core
%global fontconf 67-%{fontname}

%global alphatag    080608
%global archivename un-fonts-core-%{version}-%{alphatag}

%global common_desc \
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Core set is composed of: \
\
- UnBatang: serif \
- UnDinaru: fantasy \
- UnDotum: sans-serif \
- UnGraphic: sans-serif style \
- UnGungseo: cursive, brush-stroke \
- UnPilgi: script

%global common_desc_ko \
은글꼴 시리즈는 HLaTex개발자이신 은광희님이 1998년에 개발한 폰트입니다. \
2003년에 박원규님이 FontForge를 이용하여 트루타입폰트로 변환했습니다. \
은글꼴은 가장 일반적인 글꼴들입니다. \
\
Core 모음: \
- 은바탕: serif \
- 은디나루: fantasy \
- 은돋음: sans-serif \
- 은그래픽: sans-serif style \
- 은궁서: cursive, brush-stroke \
- 은필기: script

Name:           %{fontname}-fonts
Version:        1.0.2
Release:        0.35.%{alphatag}%{?dist}
Summary:        Un Core family of Korean TrueType fonts
Summary(ko):    한글 은글꼴 Core 모음

License:        GPLv2
URL:            http://kldp.net/projects/unfonts/
Source0:        http://kldp.net/frs/download.php/4695/%{archivename}.tar.gz
Source1:        %{name}-batang-fontconfig.conf
Source2:        %{name}-dinaru-fontconfig.conf
Source3:        %{name}-dotum-fontconfig.conf
Source4:        %{name}-graphic-fontconfig.conf
Source5:        %{name}-gungseo-fontconfig.conf
Source6:        %{name}-pilgi-fontconfig.conf
Source7:        %{fontname}-batang.metainfo.xml
Source8:        %{fontname}-dinaru.metainfo.xml
Source9:        %{fontname}-dotum.metainfo.xml
Source10:       %{fontname}-graphic.metainfo.xml
Source11:       %{fontname}.metainfo.xml
Source12:       %{fontname}-gungseo.metainfo.xml
Source13:       %{fontname}-pilgi.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel libappstream-glib

%package common
Summary:        Common files of Un Core fonts
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

# un_subpkg 1:name 2:Name 3:Hangul [4:obsolete] [5:obsolete]
%global un_subpkg() \
%package -n %{fontname}-%1-fonts \
Summary:        Un Core fonts - %(echo %2) \
Summary(ko):    한글 은글꼴 Core 모음 - %(echo %3) \
Requires:       %{name}-common = %{version}-%{release} \
Obsoletes:      un-core-fonts-%1 < 1.0.2-0.9, %{?4:un-core-fonts-%{1}%{4} < 1.0.2-0.9},  %{?5:un-core-fonts-%{1}%{5} < 1.0.2-0.9} \
\
\

%un_subpkg batang UnBatang 은바탕 bold
%un_subpkg dinaru UnDinaru 은디나루 bold light
%un_subpkg dotum UnDotum 은돋음 bold
%un_subpkg graphic UnGraphic 은그래픽 bold
%un_subpkg gungseo UnGungseo 은궁서
%un_subpkg pilgi UnPilgi 은필기 bold


%description
%common_desc

%description -l ko
%common_desc_ko

%description -n %{fontname}-batang-fonts
%common_desc

This package includes UnBatang, a serif font.

%description -l ko -n %{fontname}-batang-fonts
%common_desc_ko

이 패키지에는 은바탕글꼴이 포함되어 있습니다.

%description -n %{fontname}-dinaru-fonts
%common_desc

This package includes UnDinaru, a fantasy font.

%description -l ko -n %{fontname}-dinaru-fonts
%common_desc_ko

이 패키지에는 은디나루글꼴이 포함되어 있습니다.

%description -n %{fontname}-dotum-fonts
%common_desc

This package includes UnDotum, a sans-serif font.

%description -l ko -n %{fontname}-dotum-fonts
%common_desc_ko

이 패키지에는 은돋음글꼴이 포함되어 있습니다.

%description -n %{fontname}-graphic-fonts
%common_desc

This package includes UnGraphic, a sans-serif font.

%description -l ko -n %{fontname}-graphic-fonts
%common_desc_ko

이 패키지에는 은그래픽글꼴이 포함되어 있습니다.

%description -n %{fontname}-gungseo-fonts
%common_desc

This package includes UnGungseo, a cursive font.

%description -l ko -n %{fontname}-gungseo-fonts
%common_desc_ko

이 패키지에는 은궁서글꼴이 포함되어 있습니다.

%description -n %{fontname}-pilgi-fonts
%common_desc

This package includes UnPilgi, a script font.

%description -l ko -n %{fontname}-pilgi-fonts
%common_desc_ko

이 패키지에는 은필기글꼴이 포함되어 있습니다.


%_font_pkg -n batang -f %{fontconf}-batang.conf UnBatang.ttf UnBatangBold.ttf
%{_metainfodir}/%{fontname}-batang.metainfo.xml
%_font_pkg -n dinaru -f %{fontconf}-dinaru.conf UnDinaru.ttf UnDinaruLight.ttf UnDinaruBold.ttf
%{_metainfodir}/%{fontname}-dinaru.metainfo.xml
%_font_pkg -n dotum -f %{fontconf}-dotum.conf UnDotum.ttf UnDotumBold.ttf
%{_metainfodir}/%{fontname}-dotum.metainfo.xml
%_font_pkg -n graphic -f %{fontconf}-graphic.conf UnGraphic.ttf UnGraphicBold.ttf
%{_metainfodir}/%{fontname}-graphic.metainfo.xml
%_font_pkg -n gungseo -f %{fontconf}-gungseo.conf UnGungseo.ttf
%{_metainfodir}/%{fontname}-gungseo.metainfo.xml
%_font_pkg -n pilgi -f %{fontconf}-pilgi.conf UnPilgi.ttf UnPilgiBold.ttf
%{_metainfodir}/%{fontname}-pilgi.metainfo.xml

%prep
%setup -q -n un-fonts


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-batang.conf
install -m 0644 -p %{SOURCE2}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dinaru.conf
install -m 0644 -p %{SOURCE3}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dotum.conf
install -m 0644 -p %{SOURCE4}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-graphic.conf
install -m 0644 -p %{SOURCE5}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gungseo.conf
install -m 0644 -p %{SOURCE6}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pilgi.conf

for fconf in %{fontconf}-batang.conf \
    %{fontconf}-dinaru.conf \
    %{fontconf}-dotum.conf \
    %{fontconf}-graphic.conf \
    %{fontconf}-gungseo.conf \
    %{fontconf}-pilgi.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_metainfodir}/%{fontname}-batang.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_metainfodir}/%{fontname}-dinaru.metainfo.xml
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_metainfodir}/%{fontname}-dotum.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_metainfodir}/%{fontname}-graphic.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_metainfodir}/%{fontname}-gungseo.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_metainfodir}/%{fontname}-pilgi.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files common
%doc README
%license COPYING
%{_metainfodir}/%{fontname}.metainfo.xml

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.35.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.0.2-0.34.080608
- Install metainfo files under %%{_metainfodir}.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.33.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.32.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jan 30 2018 Akira TAGOH <tagoh@redhat.com> - 1.0.2-0.31.080608
- Update the priority to change the default font to Noto.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.30.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Richard Hughes <rhughes@redhat.com> - 1.0.2-0.29.080608
- Actually install the AppData files

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.28.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.27.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.26.080608
- replace %%define uses with %%global

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.25.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-0.24.080608
- Add metainfo file to show this font in gnome-software
- Remove group tag
- Remove buildroot tag

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.23.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.22.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.21.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.20.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.19.080608%{?dist}
- fix <test> usage in fontconfig files (Closes: #837525)

* Mon Feb  6 2012 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.18.080608
- update the priority for the Korean default font change
  nhn-nanum-fonts -> 65-0, un-core-fonts -> 65-1, baekmuk-ttf-fonts -> 65-2
- drop buildroot cleanup
- drop %%defattr(0644,root,root,0755) from %%files

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.17.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.16.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 25 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.15.080608
- fix trivial typos in fontconfig config files (thanks Akira TAGOH)

* Wed May 12 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.14.080608
- add "ko" as well as "ko-kr" to the lang test of .conf files to avoid
  some glyphs to be rendered with wqy-zenhei-fonts

* Thu May  6 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.13.080608
- assign higher priority (65- -> 65-0-) to .conf files to avoid the
  effects of 65-nonlatin.conf
- remove binding="same" from .conf files

* Tue May  4 2010 Jens Petersen <petersen@redhat.com> - 1.0.2-0.12.080608
- update .conf files to be locale-specific (#586877)

* Mon Apr 26 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.11.080608
- use _font_pkg macro (#581734)
- don't install un-core-fonts-*{light,bold}-fontconfig.conf

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.10.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Jens Petersen <petersen@redhat.com> - 1.0.2-0.9.080608
- update to new fonts packaging and naming (#477474)
- moved bold (and light) weights into main subpackages (#468618)
- add obsoletes for renaming and former bold subpackages (#468618)

* Fri Jun 26 2009 Jens Petersen <petersen@redhat.com> - 1.0.2-0.8.080608
- fix filelist to only include specific font (#496795)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.7.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 14 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.6.080608
- fixed subpackage description and fontconfig.

* Wed Jul 16 2008 Jens Petersen <petersen@redhat.com> - 1.0.2-0.5.080608
- add subpackages with a macro

* Mon Jul 07 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.4.080608
- Refined .spec literal

* Sun Jul 06 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.3.080608
- Added or Changed a Summary and Description.
- Removed nil item.
- Refined versioning contents.
- Renamed from un-fonts-core.spec

* Thu Jul 03 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.2.080608
- Refined .spec literal, license, versioning contents.

* Sat Jun 28 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.1.080608
- Initial release.
