%global fontname senamirmir-washra
%global fontconf 65-%{fontname}

%global archivename washra-fonts-%{version}

%global common_desc \
A set of high quality unicode fonts for the  Geʼez (Ethiopic) script \
published by the Senamirmir project. They can be used to write Ethiopic and \
Eritrean languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).


Name:    %{fontname}-fonts
Version: 4.1
Release: 20%{?dist}
Summary: Fonts for the Geʼez (Ethiopic) script

License: OFL
URL:     http://www.senamirmir.org/projects/typography/typeface.html
Source0: http://www.senamirmir.org/downloads/%{archivename}.zip
# Problems reported upstream
# https://www.redhat.com/archives/fedora-fonts-list/2009-June/msg00002.html
Source1: %{name}-fontconfig.conf
# We need upstream or someone who knows local Ethiopian usage to suggest a
# classification we could relay to fontconfig. In the meanwhile, only three
# font families classified
Source2: %{name}-yigezu-bisrat-goffer-fontconfig.conf
Source3: %{name}-yigezu-bisrat-gothic-fontconfig.conf
Source4: %{fontname}-bold.metainfo.xml
Source5: %{fontname}-fantuwua.metainfo.xml
Source6: %{fontname}-hiwua.metainfo.xml
Source7: %{fontname}-jiret.metainfo.xml
Source8: %{fontname}.metainfo.xml
Source9: %{fontname}-semibold.metainfo.xml
Source10: %{fontname}-tint.metainfo.xml
Source11: %{fontname}-wookianos.metainfo.xml
Source12: %{fontname}-yebse.metainfo.xml
Source13: %{fontname}-yigezu-bisrat-goffer.metainfo.xml
Source14: %{fontname}-yigezu-bisrat-gothic.metainfo.xml
Source15: %{fontname}-zelan.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc

%_font_pkg -f %{fontconf}.conf washrab.ttf washrasb.ttf
%{_datadir}/appdata/%{fontname}-semibold.metainfo.xml
%{_datadir}/appdata/%{fontname}-bold.metainfo.xml

%package common
Summary:  Common files of %{name}
Requires: fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-fantuwua-fonts
Summary:  A font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-fantuwua-fonts
%common_desc

This package consists of the “Ethiopic Fantuwua” font.

%_font_pkg -n fantuwua fantuwua.ttf
%{_datadir}/appdata/%{fontname}-fantuwua.metainfo.xml

%package -n %{fontname}-hiwua-fonts
Summary:  A font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-hiwua-fonts
%common_desc

This package consists of the “Ethiopic Hiwua” font.

%_font_pkg -n hiwua hiwua.ttf
%{_datadir}/appdata/%{fontname}-hiwua.metainfo.xml

%package -n %{fontname}-jiret-fonts
Summary:  A font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-jiret-fonts
%common_desc

This package consists of the “Ethiopia Jiret” font.

%_font_pkg -n jiret jiret.ttf
%{_datadir}/appdata/%{fontname}-jiret.metainfo.xml

%package -n %{fontname}-tint-fonts
Summary:  A font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-tint-fonts
%common_desc

This package consists of the “Ethiopic Tint” font.

%_font_pkg -n tint tint.ttf
%{_datadir}/appdata/%{fontname}-tint.metainfo.xml

%package -n %{fontname}-wookianos-fonts
Summary:  A font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-wookianos-fonts
%common_desc

This package consists of the “Ethiopic Wookianos” font.

%_font_pkg -n wookianos wookianos.ttf
%{_datadir}/appdata/%{fontname}-wookianos.metainfo.xml

%package -n %{fontname}-yebse-fonts
Summary:  A font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-yebse-fonts
%common_desc

This package consists of the “Ethiopic Yebse” font.

%_font_pkg -n yebse yebse.ttf
%{_datadir}/appdata/%{fontname}-yebse.metainfo.xml

%package -n %{fontname}-yigezu-bisrat-goffer-fonts
Summary:  A decorative font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-yigezu-bisrat-goffer-fonts
%common_desc

This package consists of the “Ethiopic Yigezu Bisrat Goffer” font, a “Gothic
Goffer” decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book
“Ye-ethiopia khine tsehifet” (Ethiopian Typography) provided the original
design that served as inspiration for this work.

%_font_pkg -n yigezu-bisrat-goffer -f %{fontconf}-yigezu-bisrat-goffer.conf goffer.ttf
%{_datadir}/appdata/%{fontname}-yigezu-bisrat-goffer.metainfo.xml

%package -n %{fontname}-yigezu-bisrat-gothic-fonts
Summary:  A decorative font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-yigezu-bisrat-gothic-fonts
%common_desc

This package consists of the “Ethiopic Yigezu Bisrat Gothic” font, a “Gothic”
decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book
“Ye-ethiopia khine tsehifet” (Ethiopian Typography) provided inspiration for
this work.

%_font_pkg -n yigezu-bisrat-gothic -f %{fontconf}-yigezu-bisrat-gothic.conf yigezubisratgothic.ttf
%{_datadir}/appdata/%{fontname}-yigezu-bisrat-gothic.metainfo.xml

%package -n %{fontname}-zelan-fonts
Summary:  A font for the Geʼez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-zelan-fonts
%common_desc

This package consists of the “Ethiopic Zelan” font.

%_font_pkg -n zelan zelan.ttf
%{_datadir}/appdata/%{fontname}-zelan.metainfo.xml

%prep
%setup -c -q
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build
#nothing to build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# No info available to classify the other fonts
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-yigezu-bisrat-goffer.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-yigezu-bisrat-gothic.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-yigezu-bisrat-goffer.conf \
             %{fontconf}-yigezu-bisrat-gothic.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-bold.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-fantuwua.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-hiwua.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-jiret.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-semibold.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tint.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-wookianos.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-yebse.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-yigezu-bisrat-goffer.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-yigezu-bisrat-gothic.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-zelan.metainfo.xml

%files common
%doc *.txt *.pdf *.doc
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Parag Nemade <pnemade AT redhat DOT com> - 4.1-12
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove buildroot which is optional now
- Remove removal of buildroot in %%install
- Remove %%defattr
- Remove group tag

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 28 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 4.1-5
— Tweak fontconfig fixing

* Sun Sep 13 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 4.1-4
— Kill camelcase WashRa capitalization too
- 4.1-3
— Fix WashRa Bold and SemiBold naming

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 4.1-2
— Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 2 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 4.1-1
— initial release
