%global fontname    un-extra
%global fontconf    66-%{fontname}

%global archivename un-fonts-extra
%global alphatag    080608

%global common_desc_en \
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Extra set is composed of: \
\
- UnPen, UnPenheulim: script \
- UnTaza: typewriter style \
- UnBom: decorative \
- UnShinmun \
- UnYetgul: old Korean printing style \
- UnJamoSora, UnJamoNovel, UnJamoDotum, UnJamoBatang \
- UnVada \
- UnPilgia: script \

%global common_desc_ko \
은글꼴 시리즈는 HLaTex개발자이신 은광희님이 1998년에 개발한 폰트입니다. \
2003년에 박원규님이 FontForge를 이용하여 트루타입폰트로 변환했습니다. \
은글꼴은 가장 일반적인 글꼴들입니다. \
\
Extra 모음 \
- 은펜, 은펜흘림: script \
- 은타자: typewriter style \
- 은봄: decorative \
- 은신문 \
- 은옛글: old Korean printing style \
- 은자모소라, 은자모노벨, 은자모돋음, 은자모바탕 \
- 은바다 \
- 은필기a: script \ 

Name:        %{fontname}-fonts
Version:     1.0.2
Release:     0.28.%{alphatag}%{?dist}
Summary:     Un Extra family of Korean TrueType fonts
Summary(ko): 한글 은글꼴 Extra 모음

License:   GPLv2
URL:       http://kldp.net/projects/unfonts/
Source0:   http://kldp.net/frs/download.php/4696/%{archivename}-%{version}-%{alphatag}.tar.gz
Source1:   %{name}-bom-fontconfig.conf
Source2:   %{name}-jamobatang-fontconfig.conf
Source3:   %{name}-jamodotum-fontconfig.conf
Source4:   %{name}-jamonovel-fontconfig.conf
Source5:   %{name}-jamosora-fontconfig.conf
Source6:   %{name}-pen-fontconfig.conf
Source7:   %{name}-penheulim-fontconfig.conf
Source8:   %{name}-pilgia-fontconfig.conf
Source9:   %{name}-shinmun-fontconfig.conf
Source10:  %{name}-taza-fontconfig.conf
Source11:  %{name}-vada-fontconfig.conf
Source12:  %{name}-yetgul-fontconfig.conf

BuildArch: noarch
BuildRequires: fontpackages-devel


%package common
Summary:     Common files for the Un Extra font set
Requires:    fontpackages-filesystem

%files common
%doc COPYING README


%global un_subpkg() \
%package -n %{fontname}-%{1}-fonts \
Summary:     Un Extra fonts - %(echo %2) \
Summary(ko): 한글 은글꼴 Extra 모음 - %(echo %3) \
Requires:    %{name}-common = %{version}-%{release} \
Obsoletes:   %{fontname}-fonts-%{1} < 1.0.2-0.10 \
\
\

%un_subpkg bom UnBom 은봄
%un_subpkg jamobatang UnJamoBatang 은자모바탕
%un_subpkg jamodotum UnJamoDotum 은자모돋음
%un_subpkg jamonovel UnJamoNovel 은자모노벨
%un_subpkg jamosora UnJamoSora 은자모소라
%un_subpkg pen UnPen 은펜
%un_subpkg penheulim UnPenheulim 은펜흘림
%un_subpkg pilgia UnPilgia 은필기a
%un_subpkg shinmun UnShinmun 은신문
%un_subpkg taza UnTaza 은타자
%un_subpkg vada UnVada 은바다
%un_subpkg yetgul UnYetgul 은옛글

%description
%common_desc_en

%description -l ko
%common_desc_ko

%description common
%common_desc_en

This package consists of files used by other %{name} packages.

%description -n %{fontname}-bom-fonts
%common_desc_en

This package includes UnBom, a decorative font.

%description -l ko -n %{fontname}-bom-fonts
%common_desc_ko

이 패키지에는 은봄글꼴이 포함되어 있습니다.

%description -n %{fontname}-jamobatang-fonts
%common_desc_en

This package includes the UnJamoBatang font.

%description -l ko -n %{fontname}-jamobatang-fonts
%common_desc_ko

이 패키지에는 은자모바탕글꼴이 포함되어 있습니다.

%description -n %{fontname}-jamodotum-fonts
%common_desc_en

This package includes the UNJamoDotum font.

%description -l ko -n %{fontname}-jamodotum-fonts
%common_desc_ko

이 패키지에는 은자모돋음글꼴이 포함되어 있습니다.

%description -n %{fontname}-jamonovel-fonts
%common_desc_en

This package includes the UNJamoNovel font.

%description -l ko -n %{fontname}-jamonovel-fonts
%common_desc_ko
 
이 패키지에는 은자모노벨글꼴이 포함되어 있습니다.

%description -n %{fontname}-jamosora-fonts
%common_desc_en

This package includes the UNJamoSora font.

%description -l ko -n %{fontname}-jamosora-fonts
%common_desc_ko

이 패키지에는 은자모소라글꼴이 포함되어 있습니다.

%description -n %{fontname}-pen-fonts
%common_desc_en

This package includes UnPen, a script font.

%description -l ko -n %{fontname}-pen-fonts
%common_desc_ko

이 패키지에는 은펜글꼴이 포함되어 있습니다.

%description -n %{fontname}-penheulim-fonts
%common_desc_en

This package includes UnPenheulim, a script font.

%description -l ko -n %{fontname}-penheulim-fonts
%common_desc_ko

이 패키지에는 은펜흘림글꼴이 포함되어 있습니다.

%description -n %{fontname}-pilgia-fonts
%common_desc_en

This package includes UnPilgia, a script font.

%description -l ko -n %{fontname}-pilgia-fonts
%common_desc_ko

이 패키지에는 은필기a글꼴이 포함되어 있습니다.

%description -n %{fontname}-shinmun-fonts
%common_desc_en

This package includes the UnShinmun font.

%description -l ko -n %{fontname}-shinmun-fonts
%common_desc_ko

이 패키지에는 은신문글꼴이 포함되어 있습니다.

%description -n %{fontname}-taza-fonts
%common_desc_en

This package includes UnTaza, a typewriter font.

%description -l ko -n %{fontname}-taza-fonts
%common_desc_ko

이 패키지에는 은타자글꼴이 포함되어 있습니다.

%description -n %{fontname}-vada-fonts
%common_desc_en

This package includes the UnVada font.

%description -l ko -n %{fontname}-vada-fonts
%common_desc_ko

이 패키지에는 은바다글꼴이 포함되어 있습니다.

%description -n %{fontname}-yetgul-fonts
%common_desc_en

This package includes UnYetgul, an old Korean printing font.

%description -l ko -n %{fontname}-yetgul-fonts
%common_desc_ko

이 패키지에는 은옛글글꼴이 포함되어 있습니다.


%_font_pkg -n bom -f %{fontconf}-bom.conf UnBom.ttf
%_font_pkg -n jamobatang -f %{fontconf}-jamobatang.conf UnJamoBatang.ttf
%_font_pkg -n jamodotum -f %{fontconf}-jamodotum.conf UnJamoDotum.ttf
%_font_pkg -n jamonovel -f %{fontconf}-jamonovel.conf UnJamoNovel.ttf
%_font_pkg -n jamosora -f %{fontconf}-jamosora.conf UnJamoSora.ttf
%_font_pkg -n pen -f %{fontconf}-pen.conf UnPen.ttf
%_font_pkg -n penheulim -f %{fontconf}-penheulim.conf UnPenheulim.ttf
%_font_pkg -n pilgia -f %{fontconf}-pilgia.conf UnPilgia.ttf
%_font_pkg -n shinmun -f %{fontconf}-shinmun.conf UnShinmun.ttf
%_font_pkg -n taza -f %{fontconf}-taza.conf UnTaza.ttf
%_font_pkg -n vada -f %{fontconf}-vada.conf UnVada.ttf
%_font_pkg -n yetgul -f %{fontconf}-yetgul.conf UnYetgul.ttf


%prep
%setup -q -n un-fonts


%build


%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bom.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamobatang.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamodotum.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamonovel.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamosora.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-penheulim.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pilgia.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shinmun.conf
install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-taza.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-vada.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-yetgul.conf

for fconf in %{fontconf}-bom.conf \
    %{fontconf}-jamobatang.conf \
    %{fontconf}-jamodotum.conf \
    %{fontconf}-jamonovel.conf \
    %{fontconf}-jamosora.conf \
    %{fontconf}-pen.conf \
    %{fontconf}-penheulim.conf \
    %{fontconf}-pilgia.conf \
    %{fontconf}-shinmun.conf \
    %{fontconf}-taza.conf \
    %{fontconf}-vada.conf \
    %{fontconf}-yetgul.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done



%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.28.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.27.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.26.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.25.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.24.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.23.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.22.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.21.080608
- replace %%define uses with %%global

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.20.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.19.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.18.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.17.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.16.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.15.080608%{?dist}
- fix <test> usage in fontconfig files (Closes: #837536)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.14.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.13.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 25 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.12.080608
- fix trivial typos in fontconfig config files

* Fri May 21 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.11.080608
- use locale-specific overrides in fontconfig.conf

* Mon Apr 26 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.10.080608
- convert to new font packaging guidelines (#477475)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.9.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.8.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.7.080608
- fixed subpackage description and fontconfig

* Sun Oct 12 2008 Nicolas Mailhot <nicolas dot mailhot at laposte dot net> - 1.0.2-0.6.080608
- complete the subpackages
- revert subpackage description macroization, it's not worth it

* Wed Oct 08 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.5.080608
- add subpackages with a macro
- add description

* Mon Jul 07 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.4.080608
- Refined .spec literal

* Sun Jul 06 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.3.080608
- Added or Changed a Summary and Description.
- Removed nil item.
- Refined versioning contents.
- Renamed from un-fonts-extra.spec

* Thu Jul 03 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.2.080608
- Refined .spec literal, license, versioning contents.

* Sat Jun 28 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.1.080608
- Initial release.
