%global fontname naver-nanum
%global fontconf 65-2-%{fontname}

%global common_desc \
Nanum fonts are collection of commonly-used Myeongjo and Gothic Korean \
font families, designed by Sandoll Communication and Fontrix. The \
publisher is Naver Corporation.


Name:       %{fontname}-fonts
Version:    3.020
Release:    26.20140930%{?dist}
Summary:    Nanum family of Korean TrueType fonts

License:    OFL
URL:        http://hangeul.naver.com
# Need to convert from Windows executable to tar ball to avoid to use p7zip
#Source:    http://appdown.naver.com/naver/font/NanumFont/setup/NanumFontSetup_TTF_ALL_hangeulcamp.exe
# wget http://appdown.naver.com/naver/font/NanumFont/setup/NanumFontSetup_TTF_ALL_hangeulcamp.exe
# 7z x NanumFontSetup_TTF_ALL_hangeulcamp.exe
# tar zcvf NanumFont.tar.gz -C \$WINDIR/Fonts/ .
Source0:    NanumFont.tar.gz
Source1:    %{name}-barun-gothic-fontconfig.conf
Source2:    %{name}-barun-pen-fontconfig.conf
Source3:    %{name}-brush-fontconfig.conf
Source4:    %{name}-gothic-fontconfig.conf
Source5:    %{name}-myeongjo-fontconfig.conf
Source6:    %{name}-pen-fontconfig.conf
# License text was taken from the upstream web on May 13 2014:
# http://help.naver.com/ops/step2/faq.nhn?faqId=15879
Source7:    %{name}-license.txt
Source8:    %{fontname}-barun-gothic.metainfo.xml
Source9:    %{fontname}-barun-pen.metainfo.xml
Source10:   %{fontname}-brush.metainfo.xml
Source11:   %{fontname}-gothic.metainfo.xml
Source12:   %{fontname}.metainfo.xml
Source13:   %{fontname}-myeongjo.metainfo.xml
Source14:   %{fontname}-pen.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel libappstream-glib

Provides:   nhn-nanum-fonts = %{version}-%{release}
Obsoletes:  nhn-nanum-fonts < %{version}-%{release}

%description
%common_desc


%package common
Summary:   Common files of %{name}
Requires:  fontpackages-filesystem
Provides:  nhn-nanum-fonts-common = %{version}-%{release}
Obsoletes: nhn-nanum-fonts-common < %{version}-%{release}

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-barun-gothic-fonts
Summary:   Nanum fonts Barun Gothic font faces
Requires:  %{name}-common = %{version}-%{release}
Provides:  nhn-nanum-barun-gothic-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-barun-gothic-fonts < %{version}-%{release}

%description -n %{fontname}-barun-gothic-fonts
%common_desc

This package consists of the Nanum fonts Barun Gothic font faces.

%_font_pkg -n barun-gothic -f %{fontconf}-barun-gothic.conf NanumBarunGothic.ttf NanumBarunGothicBold.ttf NanumBarunGothicLight.ttf NanumBarunGothicUltraLight.ttf
%{_metainfodir}/%{fontname}-barun-gothic.metainfo.xml

%package -n %{fontname}-barun-pen-fonts
Summary:   Nanum fonts Barun Pen font faces
Requires:  %{name}-common = %{version}-%{release}
Provides:  nhn-nanum-barun-pen-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-barun-pen-fonts < %{version}-%{release}

%description -n %{fontname}-barun-pen-fonts
%common_desc

This package consists of the Nanum fonts Barun Pen font faces.

%_font_pkg -n barun-pen -f %{fontconf}-barun-pen.conf NanumBarunpenR.ttf NanumBarunpenB.ttf
%{_metainfodir}/%{fontname}-barun-pen.metainfo.xml

%package -n %{fontname}-brush-fonts
Summary:   Nanum fonts Brush font faces
Requires:  %{name}-common = %{version}-%{release}
Provides:  nhn-nanum-brush-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-brush-fonts < %{version}-%{release}

%description -n %{fontname}-brush-fonts
%common_desc

This package consists of the Nanum fonts Brush font faces.

%_font_pkg -n brush -f %{fontconf}-brush.conf NanumBrush.ttf
%{_metainfodir}/%{fontname}-brush.metainfo.xml

%package -n %{fontname}-gothic-fonts
Summary:   Nanum fonts Gothic font faces
Requires:  %{name}-common = %{version}-%{release}
Provides:  nhn-nanum-gothic-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-gothic-fonts < %{version}-%{release}
Provides:   nhn-nanum-gothic-light-fonts = %{version}-%{release}
Obsoletes:  nhn-nanum-gothic-light-fonts <= 1.000-9


%description -n %{fontname}-gothic-fonts
%common_desc

This package consists of the Nanum fonts Gothic font faces.

%_font_pkg -n gothic -f %{fontconf}-gothic.conf NanumGothic.ttf NanumGothicBold.ttf NanumGothicExtraBold.ttf NanumGothicLight.ttf
%{_metainfodir}/%{fontname}-gothic.metainfo.xml

%package -n %{fontname}-myeongjo-fonts
Summary:   Nanum fonts Myeongjo font faces
Requires:  %{name}-common = %{version}-%{release}
Provides:  nhn-nanum-myeongjo-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-myeongjo-fonts < %{version}-%{release}

%description -n %{fontname}-myeongjo-fonts
%common_desc

This package consists of the Nanum fonts Myeongjo font faces.

%_font_pkg -n myeongjo -f %{fontconf}-myeongjo.conf NanumMyeongjo.ttf NanumMyeongjoBold.ttf NanumMyeongjoExtraBold.ttf
%{_metainfodir}/%{fontname}-myeongjo.metainfo.xml

%package -n %{fontname}-pen-fonts
Summary:   Nanum fonts Pen font faces
Requires:  %{name}-common = %{version}-%{release}
Provides:  nhn-nanum-pen-fonts = %{version}-%{release}
Obsoletes: nhn-nanum-pen-fonts < %{version}-%{release}

%description -n %{fontname}-pen-fonts
%common_desc

This package consists of the Nanum fonts Pen font faces.

%_font_pkg -n pen -f %{fontconf}-pen.conf NanumPen.ttf
%{_metainfodir}/%{fontname}-pen.metainfo.xml

%prep
%setup -c
cp -p %{SOURCE7} COPYING


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
     %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-barun-gothic.conf
install -m 0644 -p %{SOURCE2} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-barun-pen.conf
install -m 0644 -p %{SOURCE3} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-brush.conf
install -m 0644 -p %{SOURCE4} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -m 0644 -p %{SOURCE5} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-myeongjo.conf
install -m 0644 -p %{SOURCE6} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf

for fconf in %{fontconf}-barun-gothic.conf \
    %{fontconf}-barun-pen.conf \
    %{fontconf}-brush.conf \
    %{fontconf}-gothic.conf \
    %{fontconf}-myeongjo.conf \
    %{fontconf}-pen.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
     %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_metainfodir}/%{fontname}-barun-gothic.metainfo.xml
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_metainfodir}/%{fontname}-barun-pen.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_metainfodir}/%{fontname}-brush.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_metainfodir}/%{fontname}-gothic.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_metainfodir}/%{fontname}-myeongjo.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_metainfodir}/%{fontname}-pen.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files common
%license COPYING
%{_metainfodir}/%{fontname}.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-26.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 3.020-25.20140930
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-24.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Akira TAGOH <tagoh@redhat.com> - 3.020-23.20140930
- Update the fontconfig priority again.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-22.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Peng Wu <pwu@redhat.com> - 3.020-21.20140930
- Convert from Windows executable to tar ball to avoid to use p7zip

* Tue Jan 30 2018 Akira TAGOH <tagoh@redhat.com> - 3.020-20.20140930
- Update the priority to change the default font to Noto.

* Fri Dec 22 2017 Peng Wu <pwu@redhat.com> - 3.020-19.20140930
- Obsoletes nhn-nanum-gothic-light-fonts in naver-nanum-gothic-fonts package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-18.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-17.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-16.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-15.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.020-14.20140930
- Add metainfo file to show this font in gnome-software
- Remove group tag from -common package

* Thu Oct  9 2014 Daiki Ueno <dueno@redhat.com> - 3.020-13.20140930
- new upstream release
- add -barun-pen-fonts subpackage
- add Light and UltraLight weight to -barun-gothic-fonts

* Thu Jul 17 2014 Daiki Ueno <dueno@redhat.com> - 3.020-12.20131007
- add missing Provides/Obsoletes for each subpackage (suggested by
  Jens Petersen in https://bugzilla.redhat.com/show_bug.cgi?id=1097985#c6)

* Thu Jul 10 2014 Daiki Ueno <dueno@redhat.com> - 3.020-11.20131007
- fix broken dependencies

* Tue Jun  3 2014 Daiki Ueno <dueno@redhat.com> - 3.020-10.20131007
- rename from nhn-nanum-fonts
- add fontconfig config file for NanumBarunGothic

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Daiki Ueno <dueno@redhat.com> - 3.020-7
- fix broken deps

* Thu Nov 22 2012 Daiki Ueno <dueno@redhat.com> - 3.020-6
- cleanup spec file

* Wed Nov 21 2012 Daiki Ueno <dueno@redhat.com> - 3.020-5
- include license file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 3.020-3
- simplify the last change

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 3.020-2
- fix <test> usage in fontconfig files (Closes: #837521)

* Mon Feb  6 2012 Daiki Ueno <dueno@redhat.com> - 3.020-1
- new upstream release
- update the priority
  nhn-nanum-fonts -> 65-0, un-core-fonts -> 65-1, baekmuk-ttf-fonts -> 65-2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Daiki Ueno <dueno@redhat.com> - 3.010-1
- initial packaging for Fedora

