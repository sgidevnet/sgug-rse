%global _fontname google-noto
%global _fontnamevf google-noto-vf
%global _fontvfdir %{_fontbasedir}/%{_fontnamevf}
%global fontname %{_fontname}
%global fontconf %{_fontname}
%global common_desc Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported scripts. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all scripts available\
in Unicode.\
%{nil}

%global commit a5e21f60336d8b9b76a0f230d07dd59e12d6da80
%global hprio	65
%global mprio	66
%global lprio	67

Name:           %{fontname}-fonts
Version:        20181223
Release:        6%{?dist}
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
License:        OFL
URL:            https://github.com/googlei18n/noto-fonts/
# downloaded from https://github.com/googlei18n/noto-fonts/commits/a5e21f60336d8b9b76a0f230d07dd59e12d6da80 -> download [zip]
# link https://github.com/googlei18n/noto-fonts/archive/a5e21f60336d8b9b76a0f230d07dd59e12d6da80.zip
Source0:        noto-fonts-%{commit}.zip
Source3:        %{mprio}-%{fontconf}-sans-armenian.conf
Source5:        %{mprio}-%{fontconf}-sans-bengali.conf
Source6:        %{lprio}-%{fontconf}-sans-bengali-ui.conf
Source9:        %{mprio}-%{fontconf}-sans-cherokee.conf
Source10:       %{mprio}-%{fontconf}-sans-coptic.conf
Source12:       %{mprio}-%{fontconf}-sans-devanagari.conf
Source13:       %{lprio}-%{fontconf}-sans-devanagari-ui.conf
Source15:       %{mprio}-%{fontconf}-sans-ethiopic.conf
Source16:       %{mprio}-%{fontconf}-sans-georgian.conf
Source18:       %{mprio}-%{fontconf}-sans-hebrew.conf
Source21:       %{mprio}-%{fontconf}-sans-kannada.conf
Source24:       %{mprio}-%{fontconf}-sans-khmer.conf
Source25:       %{lprio}-%{fontconf}-sans-khmer-ui.conf
Source26:       %{mprio}-%{fontconf}-sans-lao.conf
Source27:       %{lprio}-%{fontconf}-sans-lao-ui.conf
Source28:       %{mprio}-%{fontconf}-sans-lisu.conf
Source31:       %{mprio}-%{fontconf}-sans-malayalam.conf
Source32:       %{lprio}-%{fontconf}-sans-malayalam-ui.conf
Source34:       %{mprio}-%{fontconf}-sans-meetei-mayek.conf
Source35:       %{mprio}-%{fontconf}-sans-nko.conf
Source40:       %{mprio}-%{fontconf}-sans-shavian.conf
Source42:       %{mprio}-%{fontconf}-sans-tagalog.conf
Source44:       %{mprio}-%{fontconf}-sans-tamil.conf
Source45:       %{lprio}-%{fontconf}-sans-tamil-ui.conf
Source46:       %{mprio}-%{fontconf}-sans-telugu.conf
Source47:       %{mprio}-%{fontconf}-sans-thai.conf
Source48:       %{lprio}-%{fontconf}-sans-thai-ui.conf
Source51:       %{mprio}-%{fontconf}-sans-vai.conf
Source52:       %{mprio}-%{fontconf}-serif-armenian.conf
Source54:       %{mprio}-%{fontconf}-serif-georgian.conf
Source55:       %{mprio}-%{fontconf}-serif-khmer.conf
Source56:       %{mprio}-%{fontconf}-serif-lao.conf
Source57:       %{mprio}-%{fontconf}-serif-thai.conf
Source58:       %{lprio}-%{fontconf}-sans-kannada-ui.conf
Source59:       %{lprio}-%{fontconf}-sans-telugu-ui.conf
Source60:       %{mprio}-%{fontconf}-sans-gujarati.conf
Source61:       %{lprio}-%{fontconf}-sans-gujarati-ui.conf
Source62:       %{mprio}-%{fontconf}-sans-hanunoo.conf
Source64:       %{mprio}-%{fontconf}-kufi-arabic.conf
Source65:       %{mprio}-%{fontconf}-naskh-arabic.conf
Source66:       %{lprio}-%{fontconf}-naskh-arabic-ui.conf
Source67:       %{mprio}-%{fontconf}-serif-balinese.conf
Source68:       %{mprio}-%{fontconf}-sans-bamum.conf
Source69:       %{mprio}-%{fontconf}-sans-batak.conf
Source70:       %{mprio}-%{fontconf}-sans-buginese.conf
Source71:       %{mprio}-%{fontconf}-sans-buhid.conf
Source72:       %{mprio}-%{fontconf}-sans-canadian-aboriginal.conf
Source73:       %{mprio}-%{fontconf}-sans-cham.conf
Source74:       %{mprio}-%{fontconf}-sans-cuneiform.conf
Source75:       %{mprio}-%{fontconf}-sans-cypriot.conf
Source76:       %{mprio}-%{fontconf}-sans-gothic.conf
Source77:       %{hprio}-0-%{fontconf}-sans-gurmukhi.conf
Source78:       %{lprio}-%{fontconf}-sans-gurmukhi-ui.conf
Source81:       %{mprio}-%{fontconf}-sans-javanese.conf
Source82:       %{mprio}-%{fontconf}-sans-lepcha.conf
Source83:       %{mprio}-%{fontconf}-sans-limbu.conf
Source85:       %{mprio}-%{fontconf}-sans-mongolian.conf
Source86:       %{mprio}-%{fontconf}-sans-myanmar.conf
Source87:       %{lprio}-%{fontconf}-sans-myanmar-ui.conf
Source88:       %{mprio}-%{fontconf}-sans-new-tai-lue.conf
Source89:       %{mprio}-%{fontconf}-sans-ogham.conf
Source90:       %{mprio}-%{fontconf}-sans-ol-chiki.conf
Source94:       %{mprio}-%{fontconf}-sans-rejang.conf
Source95:       %{mprio}-%{fontconf}-sans-runic.conf
Source97:       %{mprio}-%{fontconf}-sans-saurashtra.conf
Source98:       %{mprio}-%{fontconf}-sans-sinhala.conf
Source99:       %{mprio}-%{fontconf}-sans-sundanese.conf
Source101:      %{mprio}-%{fontconf}-sans-syriac-eastern.conf
Source102:      %{mprio}-%{fontconf}-sans-syriac-estrangela.conf
Source103:      %{mprio}-%{fontconf}-sans-syriac-western.conf
Source105:      %{mprio}-%{fontconf}-sans-tifinagh.conf
Source107:      %{mprio}-%{fontconf}-sans-tagbanwa.conf
Source108:      %{mprio}-%{fontconf}-sans-thaana.conf

Source156:      %{mprio}-%{fontconf}-sans-oriya.conf
Source157:      %{lprio}-%{fontconf}-sans-oriya-ui.conf
Source158:      %{mprio}-%{fontconf}-nastaliq-urdu.conf
Source159:      %{mprio}-%{fontconf}-sans-tibetan.conf
Source161:      %{mprio}-%{fontconf}-serif-bengali.conf
Source162:      %{mprio}-%{fontconf}-serif-devanagari.conf
Source163:      %{mprio}-%{fontconf}-serif-gujarati.conf
Source164:      %{mprio}-%{fontconf}-serif-kannada.conf
Source165:      %{mprio}-%{fontconf}-serif-malayalam.conf
Source166:      %{mprio}-%{fontconf}-serif-tamil.conf
Source167:      %{mprio}-%{fontconf}-serif-telugu.conf

# Add appstream metadata files
Source200:      %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
%common_desc


%package common
Summary:        Common files for Noto fonts

%description common
Common files for Google Noto fonts.

# notopkg [-a AltFontName] [-o old-name] Font Name
# -a overrides the FontName
# -o adds an obsoletes for an older package name
# -p overrides fontconfig .conf priority (default 66)
# -v packages a variable font
%define notopkg(c:a:o:p:v)\
%define _pname %(echo %{*} | tr "A-Z " "a-z-")\
%define pname %{_pname}%{-v:-vf}\
%{!-a:%define fname %(echo %{*} | sed -e "s/ //g")}\
%define subpkg %{_fontname}-%{pname}\
%define fconf %{-p*}%{!-p:%{-v:%{hprio}}%{!-v:%{mprio}}}-%{fontconf}-%{pname}.conf\
%package -n %{subpkg}-fonts\
Summary:        %{*}%{-v: variable} font\
Requires:       fontpackages-filesystem\
Requires:       %{name}-common = %{version}-%{release}\
%{?-o:Obsoletes:      %{_fontname}-%{-o*}-fonts < %{version}-%{release}}\
\
%description -n %{subpkg}-fonts\
%common_desc\
Noto %1 font%{?2: for %(echo %* | sed -e "s/%1 //")}.\
\
%{!-v:%_font_pkg -n %{pname} -f %{fconf} Noto%{-a*}%{!-a:%{fname}}-*.*tf} \
%{-v:%files -n %{_fontname}-%{pname}-fonts\
%dir %{_fontvfdir} \
%{_fontvfdir}/Noto%{-a*}%{!-a:%{fname}}-*VF.*tf \
%{_fontconfig_templatedir}/%{fconf} \
%config(noreplace) %{_fontconfig_confdir}/%{fconf}} \
%{_metainfodir}/%{subpkg}.metainfo.xml

%notopkg Kufi Arabic
%notopkg Music
%notopkg Naskh Arabic
%notopkg -p %{lprio} Naskh Arabic UI
%notopkg Sans
%notopkg -p %{lprio} -o sans-ui Sans Display
%notopkg Sans Adlam
%notopkg Sans Adlam Unjoined
%notopkg Sans Anatolian Hieroglyphs
%notopkg Sans Arabic
%notopkg -p %{lprio} Sans Arabic UI
%notopkg Sans Armenian
%notopkg Sans Avestan
%notopkg Sans Bamum
%notopkg Sans Bassa Vah
%notopkg Sans Batak
%notopkg Sans Bengali
%notopkg -p %{lprio} Sans Bengali UI
%notopkg Sans Bhaiksuki
%notopkg Sans Brahmi
%notopkg Sans Buginese
%notopkg Sans Buhid
%notopkg Sans Canadian Aboriginal
%notopkg Sans Caucasian Albanian
%notopkg Sans Carian
%notopkg Sans Chakma
%notopkg Sans Cham
%notopkg Sans Cherokee
%notopkg Sans Coptic
%notopkg Sans Cuneiform
%notopkg Sans Cypriot
%notopkg Sans Deseret
%notopkg Sans Devanagari
%notopkg -p %{lprio} Sans Devanagari UI
%notopkg Sans Duployan
%notopkg Sans Egyptian Hieroglyphs
%notopkg Sans Elbasan
%notopkg Sans Ethiopic
%notopkg Sans Georgian
%notopkg Sans Glagolitic
%notopkg Sans Gothic
%notopkg Sans Grantha
%notopkg Sans Gujarati
%notopkg -p %{lprio} Sans Gujarati UI
%notopkg -p %{hprio}-0 Sans Gurmukhi
%notopkg -p %{lprio} Sans Gurmukhi UI
%notopkg -o sans-hanunno Sans Hanunoo
%notopkg Sans Hatran
%notopkg Sans Hebrew
%notopkg Sans Imperial Aramaic
%notopkg Sans Inscriptional Pahlavi
%notopkg Sans Inscriptional Parthian
%notopkg Sans Javanese
%notopkg Sans Kaithi
%notopkg Sans Kannada
%notopkg -p %{lprio} Sans Kannada UI
%notopkg Sans Kayah Li
%notopkg Sans Kharoshthi
%notopkg Sans Khmer
%notopkg -p %{lprio} Sans Khmer UI
%notopkg Sans Khojki
%notopkg Sans Khudawadi
%notopkg Sans Lao
%notopkg -p %{lprio} Sans Lao UI
%notopkg Sans Lepcha
%notopkg Sans Limbu
%notopkg Sans Linear A
%notopkg -o sans-linearb Sans Linear B
%notopkg Sans Lisu
%notopkg Sans Lycian
%notopkg Sans Lydian
%notopkg Sans Mahajani
%notopkg Sans Malayalam
%notopkg -p %{lprio} Sans Malayalam UI
%notopkg Sans Mandaic
%notopkg Sans Manichaean
%notopkg Sans Marchen
%notopkg -p %{lprio} Sans Math
%notopkg -o sans-meeteimayek Sans Meetei Mayek
%notopkg Sans Mende Kikakui
%notopkg Sans Meroitic
%notopkg Sans Miao
%notopkg Sans Modi
%notopkg Sans Mongolian
%notopkg Sans Mro
%notopkg Sans Multani
%notopkg Sans Myanmar
%notopkg -p %{lprio} Sans Myanmar UI
%notopkg Sans Nabataean
%notopkg Sans New Tai Lue
%notopkg Sans Newa
%notopkg Sans NKo
%notopkg Sans Ogham
%notopkg Sans Ol Chiki
%notopkg Sans Old Hungarian
%notopkg Sans Old Italic
%notopkg Sans Old North Arabian
%notopkg Sans Old Permic
%notopkg Sans Old Persian
%notopkg Sans Old South Arabian
%notopkg Sans Old Turkic
%notopkg Sans Osage
%notopkg Sans Osmanya
%notopkg Sans Pahawh Hmong
%notopkg Sans Palmyrene
%notopkg Sans Pau Cin Hau
%notopkg Sans Phags Pa
%notopkg Sans Phoenician
%notopkg Sans Psalter Pahlavi
%notopkg Sans Rejang
%notopkg Sans Runic
%notopkg Sans Samaritan
%notopkg Sans Saurashtra
%notopkg Sans Sharada
%notopkg Sans Shavian
%notopkg -p %{mprio} Sans Sinhala
%notopkg -p %{lprio} Sans Sinhala UI
%notopkg Sans Sora Sompeng
%notopkg Sans Sundanese
%notopkg Sans Syloti Nagri
%notopkg Sans Symbols
%notopkg Sans Symbols2
%notopkg Sans Syriac
%notopkg Sans Syriac Eastern
%notopkg Sans Syriac Estrangela
%notopkg Sans Syriac Western
%notopkg Sans Tagalog
%notopkg Sans Tagbanwa
%notopkg Sans Takri
%notopkg Sans Tai Le
%notopkg Sans Tai Tham
%notopkg Sans Tai Viet
%notopkg Sans Tamil
%notopkg -p %{lprio} Sans Tamil UI
%notopkg Sans Telugu
%notopkg -p %{lprio} Sans Telugu UI
%notopkg Sans Thaana
%notopkg Sans Thai
%notopkg -p %{lprio} Sans Thai UI
%notopkg Sans Tifinagh
%notopkg Sans Tirhuta
%notopkg Sans Ugaritic
%notopkg Sans Vai
%notopkg Sans Warang Citi
%notopkg Sans Yi
%notopkg Serif
%notopkg Serif Ahom
%notopkg Serif Armenian
%notopkg -o sans-balinese Serif Balinese
%notopkg -p %{lprio} Serif Display
%notopkg Serif Ethiopic
%notopkg Serif Georgian
%notopkg Serif Hebrew
%notopkg Serif Khmer
%notopkg Serif Lao
%notopkg Serif Myanmar
%notopkg Serif Tamil Slanted
%notopkg Serif Thai
%notopkg Sans Oriya
%notopkg -p %{lprio} Sans Oriya UI
%notopkg Sans Tibetan
%notopkg Nastaliq Urdu
%notopkg -o mono Sans Mono
%notopkg Serif Bengali
%notopkg Serif Devanagari
%notopkg Serif Gujarati
%notopkg Serif Gurmukhi
%notopkg Serif Kannada
%notopkg Serif Malayalam
%notopkg Serif Sinhala
%notopkg Serif Tamil
%notopkg Serif Telugu
%notopkg Serif Tibetan

%global fontname %{_fontnamevf}
%notopkg -v Sans
%notopkg -v Sans Arabic
%notopkg -v -p %{lprio} Sans Arabic UI
%notopkg -v Sans Armenian
%notopkg -v Sans Bengali
%notopkg -v -p %{lprio} Sans Bengali UI
%notopkg -v Sans Canadian Aboriginal
%notopkg -v Sans Cham
%notopkg -v Sans Cherokee
%notopkg -v Sans Devanagari
%notopkg -v -p %{lprio} Sans Devanagari UI
%notopkg -v -p %{lprio} Sans Display
%notopkg -v Sans Ethiopic
%notopkg -v Sans Georgian
%notopkg -v Sans Hebrew
%notopkg -v Sans Kannada
%notopkg -v -p %{lprio} Sans Kannada UI
%notopkg -v Sans Khmer
%notopkg -v -p %{lprio} Sans Khmer UI
%notopkg -v Sans Lao
%notopkg -v -p %{lprio} Sans Lao UI
%notopkg -v Sans Malayalam
%notopkg -v -p %{lprio} Sans Malayalam UI
%notopkg -v Sans Mono
%notopkg -v Sans Myanmar
%notopkg -v -p %{lprio} Sans Myanmar UI
%notopkg -v -p %{hprio} Sans Sinhala
%notopkg -v Sans Symbols
%notopkg -v Sans Tamil
%notopkg -v -p %{lprio} Sans Tamil UI
%notopkg -v Sans Thaana
%notopkg -v Sans Thai
%notopkg -v -p %{lprio} Sans Thai UI
%notopkg -v Serif
%notopkg -v Serif Armenian
%notopkg -v -p %{lprio} Serif Display
%notopkg -v Serif Ethiopic
%notopkg -v Serif Georgian
%notopkg -v Serif Gujarati
%notopkg -v Serif Gurmukhi
%notopkg -v Serif Hebrew
%notopkg -v Serif Kannada
%notopkg -v Serif Khmer
%notopkg -v Serif Lao
%notopkg -v Serif Myanmar
%notopkg -v Serif Sinhala
%notopkg -v Serif Tamil
%notopkg -v Serif Tamil Slanted
%notopkg -v Serif Thai
%notopkg -v Serif Tibetan

%prep
%setup -q -n noto-fonts-%{commit}


%build

%install
%global fontname %{_fontname}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p unhinted/Noto*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p hinted/Noto*.ttf %{buildroot}%{_fontdir}
%global fontname %{_fontnamevf}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p phaseIII_only/unhinted/variable-ttf/Noto*.ttf %{buildroot}%{_fontdir}



install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add appstream metadata
install -Dm 0644 -p %{SOURCE200} \
        %{buildroot}%{_metainfodir}/%{_fontname}.metainfo.xml

%define fcconfbuild(a:g:l:p:v)\
%define _pname %(echo %{*} | tr "A-Z " "a-z-")\
%define pname %{_pname}%{-v:-vf}\
%define fconf %{-p*}%{!-p:%{-v:%{hprio}}%{!-v:%{mprio}}}-%{fontconf}-%{pname}.conf\
cat<<_EOL_>%{buildroot}%{_fontconfig_templatedir}/%{fconf}\
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
<!DOCTYPE fontconfig SYSTEM \"fonts.dtd\">\
<fontconfig>\
  %{-v:<match>\
    <test name="family">\
      <string>%{-g*}</string>\
    </test>\
    %{-l:<test name="lang">\
      <string>%{-l*}</string>\
    </test>}\
    <edit name="family" mode="prepend">\
      <string>Noto %{*}</string>\
    </edit>\
    <edit name="fonthashint" mode="append">\
      <bool>false</bool>\
    </edit>\
  </match>}\
  %{!-v:<match>\
    <test name="family">\
      <string>%{-g*}</string>\
    </test>\
    <edit name="family" mode="prepend">\
      <string>Noto %{*}</string>\
    </edit>\
    <edit name="fonthashint" mode="append">\
      <bool>true</bool>\
    </edit>\
  </match>}\
  <alias>\
    <family>Noto %{*}</family>\
    <default>\
      <family>%{-g*}</family>\
    </default>\
  </alias>\
</fontconfig>\
_EOL_

%fcconfbuild -g fantasy Music
%fcconfbuild -g sans-serif Sans Adlam
%fcconfbuild -g sans-serif Sans Adlam Unjoined
%fcconfbuild -g sans-serif Sans Anatolian Hieroglyphs
%fcconfbuild -g sans-serif Sans Arabic
%fcconfbuild -p %{lprio} -g sans-serif Sans Arabic UI
%fcconfbuild -g sans-serif Sans Avestan
%fcconfbuild -g sans-serif Sans Bassa Vah
%fcconfbuild -g sans-serif Sans Bhaiksuki
%fcconfbuild -g sans-serif Sans Brahmi
%fcconfbuild -g sans-serif Sans Carian
%fcconfbuild -g sans-serif Sans Caucasian Albanian
%fcconfbuild -g sans-serif Sans Chakma
%fcconfbuild -g sans-serif Sans Deseret
%fcconfbuild -p %{lprio} -g sans-serif Sans Display
%fcconfbuild -g sans-serif Sans Duployan
%fcconfbuild -g sans-serif Sans Egyptian Hieroglyphs
%fcconfbuild -g sans-serif Sans Elbasan
%fcconfbuild -g sans-serif Sans Glagolitic
%fcconfbuild -g sans-serif Sans Grantha
%fcconfbuild -g sans-serif Sans Hatran
%fcconfbuild -g sans-serif Sans Imperial Aramaic
%fcconfbuild -g sans-serif Sans Inscriptional Pahlavi
%fcconfbuild -g sans-serif Sans Inscriptional Parthian
%fcconfbuild -g sans-serif Sans Kaithi
%fcconfbuild -g sans-serif Sans Kayah Li
%fcconfbuild -g sans-serif Sans Kharoshthi
%fcconfbuild -g sans-serif Sans Khojki
%fcconfbuild -g sans-serif Sans Khudawadi
%fcconfbuild -g sans-serif Sans Linear A
%fcconfbuild -g sans-serif Sans Linear B
%fcconfbuild -g sans-serif Sans Lycian
%fcconfbuild -g sans-serif Sans Lydian
%fcconfbuild -g sans-serif Sans Mahajani
%fcconfbuild -g sans-serif Sans Mandaic
%fcconfbuild -g sans-serif Sans Manichaean
%fcconfbuild -g sans-serif Sans Marchen
%fcconfbuild -g sans-serif -p %{lprio} Sans Math
%fcconfbuild -g sans-serif Sans Mende Kikakui
%fcconfbuild -g sans-serif Sans Meroitic
%fcconfbuild -g sans-serif Sans Miao
%fcconfbuild -g sans-serif Sans Modi
%fcconfbuild -g monospace Sans Mono
%fcconfbuild -g sans-serif Sans Mro
%fcconfbuild -g sans-serif Sans Multani
%fcconfbuild -g sans-serif Sans Nabataean
%fcconfbuild -g sans-serif Sans Newa
%fcconfbuild -g sans-serif Sans Old Hungarian
%fcconfbuild -g sans-serif Sans Old Italic
%fcconfbuild -g sans-serif Sans Old North Arabian
%fcconfbuild -g sans-serif Sans Old Permic
%fcconfbuild -g sans-serif Sans Old Persian
%fcconfbuild -g sans-serif Sans Old South Arabian
%fcconfbuild -g sans-serif Sans Old Turkic
%fcconfbuild -g sans-serif Sans Osage
%fcconfbuild -g sans-serif Sans Osmanya
%fcconfbuild -g sans-serif Sans Pahawh Hmong
%fcconfbuild -g sans-serif Sans Palmyrene
%fcconfbuild -g sans-serif Sans Pau Cin Hau
%fcconfbuild -g sans-serif Sans Phags Pa
%fcconfbuild -g sans-serif Sans Phoenician
%fcconfbuild -g sans-serif Sans Psalter Pahlavi
%fcconfbuild -g sans-serif Sans Samaritan
%fcconfbuild -g sans-serif Sans Sharada
%fcconfbuild -p %{lprio} -g sans-serif Sans Sinhala UI
%fcconfbuild -g sans-serif Sans Sora Sompeng
%fcconfbuild -g sans-serif Sans Syloti Nagri
%fcconfbuild -g fantasy Sans Symbols
%fcconfbuild -g fantasy Sans Symbols2
%fcconfbuild -g sans-serif Sans Syriac
%fcconfbuild -g sans-serif Sans Tai Le
%fcconfbuild -g sans-serif Sans Tai Tham
%fcconfbuild -g sans-serif Sans Tai Viet
%fcconfbuild -g sans-serif Sans Takri
%fcconfbuild -g sans-serif Sans Tirhuta
%fcconfbuild -g sans-serif Sans Ugaritic
%fcconfbuild -g sans-serif Sans Warang Citi
%fcconfbuild -g sans-serif Sans Yi
%fcconfbuild -g sans-serif Sans
%fcconfbuild -g serif Serif Ahom
%fcconfbuild -p %{lprio} -g serif Serif Display
%fcconfbuild -g serif Serif Ethiopic
%fcconfbuild -g serif Serif Gurmukhi
%fcconfbuild -g serif Serif Hebrew
%fcconfbuild -g serif Serif Myanmar
%fcconfbuild -g serif Serif Sinhala
%fcconfbuild -g serif Serif Tamil Slanted
%fcconfbuild -g serif Serif Tibetan
%fcconfbuild -g serif Serif

%fcconfbuild -v -g sans-serif Sans
%fcconfbuild -v -g sans-serif -l ar Sans Arabic
%fcconfbuild -v -g sans-serif -l ar -p %{lprio} Sans Arabic UI
%fcconfbuild -v -g sans-serif -l hy Sans Armenian
%fcconfbuild -v -g sans-serif -l bn Sans Bengali
%fcconfbuild -v -g sans-serif -l bn -p %{lprio} Sans Bengali UI
%fcconfbuild -v -g sans-serif Sans Canadian Aboriginal
%fcconfbuild -v -g sans-serif Sans Cham
%fcconfbuild -v -g sans-serif -l chr Sans Cherokee
%fcconfbuild -v -g sans-serif -l hi Sans Devanagari
%fcconfbuild -v -g sans-serif -l hi -p %{lprio} Sans Devanagari UI
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Display
%fcconfbuild -v -g sans-serif Sans Ethiopic
%fcconfbuild -v -g sans-serif -l ka Sans Georgian
%fcconfbuild -v -g sans-serif -l he Sans Hebrew
%fcconfbuild -v -g sans-serif -l kn Sans Kannada
%fcconfbuild -v -g sans-serif -l kn -p %{lprio} Sans Kannada UI
%fcconfbuild -v -g sans-serif -l km Sans Khmer
%fcconfbuild -v -g sans-serif -l km -p %{lprio} Sans Khmer UI
%fcconfbuild -v -g sans-serif -l lo Sans Lao
%fcconfbuild -v -g sans-serif -l lo -p %{lprio} Sans Lao UI
%fcconfbuild -v -g sans-serif -l ml Sans Malayalam
%fcconfbuild -v -g sans-serif -l ml -p %{lprio} Sans Malayalam UI
%fcconfbuild -v -g monospace Sans Mono
%fcconfbuild -v -g sans-serif Sans Myanmar
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Myanmar UI
%fcconfbuild -v -g sans-serif -l si -p %{hprio} Sans Sinhala
%fcconfbuild -v -g fantasy Sans Symbols
%fcconfbuild -v -g sans-serif -l ta Sans Tamil
%fcconfbuild -v -g sans-serif -l ta -p %{lprio} Sans Tamil UI
%fcconfbuild -v -g sans-serif Sans Thaana
%fcconfbuild -v -g sans-serif -l th Sans Thai
%fcconfbuild -v -g sans-serif -l th -p %{lprio} Sans Thai UI
%fcconfbuild -v -g serif Serif
%fcconfbuild -v -g serif -l hy Serif Armenian
%fcconfbuild -v -g serif -p %{lprio} Serif Display
%fcconfbuild -v -g serif Serif Ethiopic
%fcconfbuild -v -g serif -l ka Serif Georgian
%fcconfbuild -v -g serif -l gu Serif Gujarati
%fcconfbuild -v -g serif -l pa Serif Gurmukhi
%fcconfbuild -v -g serif -l he Serif Hebrew
%fcconfbuild -v -g serif -l kn Serif Kannada
%fcconfbuild -v -g serif -l km Serif Khmer
%fcconfbuild -v -g serif -l lo Serif Lao
%fcconfbuild -v -g serif Serif Myanmar
%fcconfbuild -v -g serif -l si Serif Sinhala
%fcconfbuild -v -g serif -l ta Serif Tamil
%fcconfbuild -v -g serif -l ta Serif Tamil Slanted
%fcconfbuild -v -g serif -l th Serif Thai
%fcconfbuild -v -g serif -l bo Serif Tibetan

for f in \
        kufi-arabic music naskh-arabic naskh-arabic-ui \
        sans sans-adlam sans-adlam-unjoined sans-anatolian-hieroglyphs \
	sans-arabic sans-arabic-ui \
	sans-armenian sans-avestan sans-bamum sans-bassa-vah \
        sans-batak sans-bhaiksuki sans-bengali sans-bengali-ui sans-brahmi \
        sans-buginese sans-buhid sans-canadian-aboriginal sans-caucasian-albanian \
	sans-carian \
        sans-chakma sans-cham sans-cherokee sans-coptic sans-cuneiform \
        sans-cypriot sans-deseret sans-devanagari sans-devanagari-ui \
	sans-duployan \
        sans-egyptian-hieroglyphs sans-elbasan sans-ethiopic sans-georgian \
        sans-glagolitic sans-gothic sans-grantha sans-gujarati sans-gujarati-ui \
        sans-gurmukhi sans-gurmukhi-ui sans-hanunoo sans-hatran sans-hebrew \
        sans-imperial-aramaic sans-inscriptional-pahlavi \
        sans-inscriptional-parthian sans-javanese \
        sans-kaithi sans-kannada sans-kannada-ui sans-kayah-li \
        sans-kharoshthi sans-khmer sans-khmer-ui sans-khojki sans-khudawadi sans-lao \
        sans-lao-ui sans-lepcha sans-limbu sans-linear-a sans-linear-b sans-lisu \
        sans-lycian sans-lydian sans-mahajani sans-malayalam sans-malayalam-ui \
        sans-mandaic sans-manichaean sans-marchen sans-meetei-mayek sans-math \
	sans-mende-kikakui \
	sans-meroitic sans-miao sans-modi sans-mongolian sans-mro sans-multani \
	sans-myanmar \
        sans-myanmar-ui sans-nabataean sans-new-tai-lue sans-newa sans-nko sans-ogham \
        sans-ol-chiki sans-old-hungarian sans-old-italic sans-old-north-arabian \
	sans-old-permic sans-old-persian \
        sans-old-south-arabian sans-old-turkic sans-osage sans-osmanya \
        sans-pahawh-hmong sans-palmyrene sans-pau-cin-hau \
	sans-phags-pa sans-phoenician sans-psalter-pahlavi sans-rejang sans-runic \
        sans-samaritan sans-saurashtra sans-sharada sans-shavian sans-sinhala sans-sinhala-ui \
	sans-sora-sompeng \
        sans-sundanese sans-syloti-nagri sans-symbols sans-symbols2 sans-syriac sans-syriac-eastern \
        sans-syriac-estrangela sans-syriac-western sans-tagalog \
        sans-tagbanwa sans-takri sans-tai-le sans-tai-tham sans-tai-viet \
        sans-tamil sans-tamil-ui sans-telugu sans-telugu-ui \
        sans-thaana sans-thai sans-thai-ui sans-tifinagh sans-tirhuta \
        sans-ugaritic sans-display sans-vai sans-warang-citi sans-yi \
        serif serif-ahom serif-armenian serif-display serif-ethiopic serif-georgian \
	serif-gurmukhi \
	serif-hebrew serif-khmer serif-lao serif-myanmar serif-sinhala serif-thai \
        sans-oriya sans-oriya-ui sans-tibetan nastaliq-urdu sans-mono \
        serif-balinese serif-bengali serif-devanagari serif-gujarati serif-kannada \
        serif-malayalam serif-tamil serif-tamil-slanted serif-telugu serif-tibetan \
	sans-vf sans-arabic-vf sans-arabic-ui-vf sans-armenian-vf sans-bengali-vf \
	sans-bengali-ui-vf sans-canadian-aboriginal-vf sans-cham-vf sans-cherokee-vf \
	sans-devanagari-vf sans-devanagari-ui-vf sans-display-vf sans-ethiopic-vf \
	sans-georgian-vf sans-hebrew-vf sans-kannada-vf sans-kannada-ui-vf \
	sans-khmer-vf sans-khmer-ui-vf sans-lao-vf sans-lao-ui-vf sans-malayalam-vf \
	sans-malayalam-ui-vf sans-mono-vf sans-myanmar-vf sans-myanmar-ui-vf \
	sans-sinhala-vf sans-symbols-vf sans-tamil-vf sans-tamil-ui-vf \
	sans-thaana-vf sans-thai-vf sans-thai-ui-vf \
	serif-vf serif-armenian-vf serif-display-vf serif-ethiopic-vf serif-georgian-vf \
	serif-gujarati-vf serif-gurmukhi-vf serif-hebrew-vf serif-kannada-vf \
	serif-khmer-vf serif-lao-vf serif-myanmar-vf serif-sinhala-vf \
	serif-tamil-vf serif-tamil-slanted-vf serif-thai-vf serif-tibetan-vf \
        ; do
  fconf=$(basename -a %{_sourcedir}/*-%{fontconf}-$f.conf)
  ifconf=$(basename -a %{buildroot}%{_fontconfig_templatedir}/*-%{fontconf}-$f.conf)
  if [ "$(echo $fconf | wc -w)" -ne 1 -o "$(echo $ifconf | wc -w)" -ne 1 ]; then
     echo "Did not find unique \*-%{fontconf}-$f.conf file"
     exit 1
  fi
  if [ -f %{_sourcedir}/${fconf} ]; then
    install -m 0644 -p %{_sourcedir}/${fconf} \
          %{buildroot}%{_fontconfig_templatedir}/${fconf}
  else
    fconf=$ifconf
  fi
  ln -s %{_fontconfig_templatedir}/${fconf} \
        %{buildroot}%{_fontconfig_confdir}/${fconf}

  meta=%{_fontname}-$f.metainfo.xml
  echo '<?xml version="1.0" encoding="UTF-8"?>' > $meta
  echo '<!-- Copyright 2014 Parag Nemade <pnemade AT redhat DOT com> -->' >> $meta
  echo '<component type="font">' >> $meta
  echo "  <id>google-noto-$f</id>" >> $meta
  echo '  <metadata_license>CC-BY-3.0</metadata_license>' >> $meta
  echo '  <extends>google-noto</extends>' >> $meta
  echo '</component>' >> $meta

  install -Dm 0644 -p %{_fontname}-$f.metainfo.xml \
          %{buildroot}%{_metainfodir}/%{_fontname}-$f.metainfo.xml
done


%files common
%license LICENSE
%doc README.md FAQ.md
%{_metainfodir}/%{_fontname}.metainfo.xml


%changelog
* Mon Aug 12 2019 Akira TAGOH <tagoh@redhat.com> - 20181223-6
- Make variable fonts priority more than non variable fonts. (#1739976)

* Fri Jul 26 2019 Parag Nemade <pnemade AT redhat DOT com> - 20181223-5
- Resolves:rh#1554988 - google-noto-sans-gurmkukhi-fonts default for pa_IN locale

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 Akira TAGOH <tagoh@redhat.com> - 20181223-3
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Akira TAGOH <tagoh@redhat.com> - 20181223-1
- Updates to 20181223.
- Add new sub-packages for variable fonts.

* Mon Dec 17 2018 Akira TAGOH <tagoh@redhat.com> - 20181130-2
- Make Display and UI fonts lower priority.
- Add more languages to google-noto-*-devanagari.conf, google-noto-sans-ethiopic.conf,
  and google-noto-sans-hebrew.conf

* Fri Dec  7 2018 Akira TAGOH <tagoh@redhat.com> - 20181130-1
- Updates to 20181130.
- Noto Sans Balinese is now Noto Serif Balinese.
- Add new sub-packages: google-noto-music-fonts,
  google-noto-sans-bassa-vah-fonts, google-noto-sans-bhaiksuki-fonts,
  google-noto-sans-caucasian-albanian-fonts, google-noto-sans-duployan-fonts,
  google-noto-sans-elbasan-fonts, google-noto-sans-grantha-fonts,
  google-noto-sans-hatran-fonts, google-noto-sans-khojki-fonts,
  google-noto-sans-khudawadi-fonts, google-noto-sans-linear-a-fonts,
  google-noto-sans-mahajani-fonts, google-noto-sans-manichaean-fonts,
  google-noto-sans-marchen-fonts, google-noto-sans-mende-kikakui-fonts,
  google-noto-sans-meroitic-fonts, google-noto-sans-miao-fonts,
  google-noto-sans-modi-fonts, google-noto-sans-mro-fonts,
  google-noto-sans-multani-fonts, google-noto-sans-nabataean-fonts,
  google-noto-sans-newa-fonts, google-noto-sans-old-hungarian-fonts,
  google-noto-sans-old-north-arabian-fonts, google-noto-sans-old-permic-fonts,
  google-noto-sans-pahawh-hmong-fonts, google-noto-sans-palmyrene-fonts,
  google-noto-sans-pau-cin-hau-fonts, google-noto-sans-psalter-pahlavi-fonts,
  google-noto-sans-sharada-fonts, google-noto-sans-sora-sompeng-fonts,
  google-noto-sans-syriac-fonts, google-noto-sans-takri-fonts,
  google-noto-sans-tirhuta-fonts, google-noto-sans-warang-citi-fonts,
  google-noto-serif-ahom-fonts, google-noto-serif-gurmukhi-fonts,
  google-noto-serif-tamil-slanted-fonts, google-noto-serif-tibetan-fonts

* Fri Sep 21 2018 Akira TAGOH <tagoh@redhat.com> - 20180905-1
- Updates to 20180905.
- Remove Group tag.
- Don't call fc-cache in scriptlets. this isn't needed anymore.
- Drop BR: fontforge.
- Generate fontconfig config files in macro for simple one.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr  5 2018 Jens Petersen <petersen@redhat.com> - 20161022-7
- change the Sinhala fontconfig priority to 65 (#1450802)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 20161022-5
- use _font_pkg

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul  5 2017 Jens Petersen <petersen@redhat.com> - 20161022-3
- add a fontconfig priority option to the notopkg macro,
  which allows overriding the default 66 priority

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Pravin Satpute <psatpute@redhat.com> - 20161022-1
- Resolves #1321685 - Added Noto Mono font.
- License changed from ASL 2.0 to OFL. 
- New package addition: Mono, Serif Bengali, Serif Devanagari
- Serif Gujarari, Serif Malayalam, Serif Tamil and Serif Telugu.

* Wed Aug 24 2016 Pravin Satpute <psatpute@redhat.com> - 20150929-2
- Resolves #1368772 - Fixes issue with LICENSE file.

* Thu Apr 28 2016 Pravin Satpute <psatpute@redhat.com> - 20150929-1
- Resolves #1269404 - Update to new git release 20150929
- Upstream divided google-noto-fonts package into noto-cjk-font and noto-emoji
- Removed packages: google-noto-color-emoji-fonts, google-noto-sans (cjk-fonts,
- japanese-fonts, simplified-chinese-fonts and traditional-chinese-fonts)
- Replaced by google-noto-cjk-fonts and google-noto-emoji-fonts
- New subpackages - google-noto-nastaliq-urdu-fonts and google-noto-sans-tibetan-fonts

* Thu Feb 04 2016 Parag Nemade <pnemade AT redhat DOT com> - 20150417-4
- Fix for python2 fonttools

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150417-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150417-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Pravin Satpute <psatpute@redhat.com> - 20150417-1
- Updating to git snapshot d47480343178.
- Remove Thaana and Oriya from under-development list.
- Add Syriac requirements from Unicode Core Specification. 

* Fri Mar 27 2015 Pravin Satpute <psatpute@redhat.com> - 20150325-1
- Updating to git snapshot 762640379a51.
- Added 2 new packages Oriya and Oriya-UI.
- Update Hebrew, Georgian, and Ethiopic fonts.
- Fix cmap of U+06F7 to Urdu form of digit 7.

* Tue Jan 13 2015 Pravin Satpute <psatpute@redhat.com> - 20141117-6
- Resolves #1162341: Packaged Noto Color Emoji

* Mon Dec 15 2014 Jens Petersen <petersen@redhat.com> - 20141117-5
- improve generated font subpackage descriptions
- it is Hanunoo not Hanuno!
- specify font filenames more precisely

* Mon Dec 15 2014 Jens Petersen <petersen@redhat.com> - 20141117-4
- add obsoletes to cover the change of package names for Hanuno, Linear B,
  and Meetei Mayek

* Tue Dec  2 2014 Jens Petersen <petersen@redhat.com> - 20141117-3
- create the fonts subpackages with a macro

* Fri Nov 21 2014 Jens Petersen <petersen@redhat.com> - 20141117-2
- move cjk fonts fontconfig priority from 65-0 to 66
- generate the appinfo metainfo for the subpackages
- use a single for-loop to install the font config and appdata files
- move parent appinfo metainfo to common (Parag Nemade)

* Thu Nov 20 2014 Jens Petersen <petersen@redhat.com> - 20141117-1
- update to latest git (aae16d0cd626)
- package Japanese, Korean, and CJK fonts
- add Thaana font
- add common subpackage for license and doc files
- order spec subpackages lexically

* Wed Nov 19 2014 Peng Wu <pwu@redhat.com> - 20141001-5
- Rename Chinese sub-packages

* Wed Nov 12 2014 Peng Wu <pwu@redhat.com> - 20141001-4
- Add Chinese fonts

* Tue Nov 11 2014 Parag Nemade <pnemade AT redhat DOT com> - 20141001-3
- Add metainfo file to show this font in gnome-software

* Mon Nov 03 2014 Pravin Satpute <psatpute@redhat.com> - 20141001-2
- Resolves #1159562: Typo in fontconfig file

* Wed Oct 01 2014 Pravin Satpute <psatpute@redhat.com> - 20141001-1
- Google stops release tarball. Zip file derived from git Download zip.
- 45 new packages added as follows.
- kufi-arabic-fonts, naskh-arabic-fonts, naskh-arabic-ui-fonts, sans-balinese-fonts, 
- sans-bamum-fonts, sans-batak-fonts, sans-buginese-fonts, sans-buhid-fonts, 
- sans-canadian-aboriginal-fonts, sans-cham-fonts, sans-cuneiform-fonts, sans-cypriot-fonts, 
- sans-gothic-fonts, sans-gurmukhi-fonts, sans-gurmukhi-ui-fonts, 
- sans-inscriptional-pahlavi-fonts, sans-inscriptional-parthian-fonts, sans-javanese-fonts, 
- sans-lepcha-fonts, sans-limbu-fonts, sans-linearb-fonts, sans-mongolian-fonts, 
- sans-myanmar-fonts, sans-myanmar-ui-fonts, sans-new-tai-lue-fonts, sans-ogham-fonts, 
- sans-ol-chiki-fonts, sans-old-italic-fonts, sans-old-persian-fonts, sans-phags-pa-fonts, 
- sans-rejang-fonts, sans-runic-fonts, sans-samaritan-fonts, sans-saurashtra-fonts, 
- sans-sinhala-fonts, sans-sundanese-fonts, sans-syloti-nagri-fonts, sans-syriac-eastern-fonts, 
- sans-syriac-estrangela-fonts, sans-syriac-western-fonts, sans-tagbanwa-fonts, 
- sans-tai-le-fonts, sans-tifinagh-fonts, sans-yi-fonts
- Resolves #1148413

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130807-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Pravin Satpute <psatpute@redhat.com> - 20130807-1
- Upstream new release of 20130807 tarball.
- Packages Non Hinted upstream tarball.
- This pulled fonts for number of missing Unicode scripts in Fedora

* Tue Jul 16 2013 Pravin Satpute <psatpute@redhat.com> - 20130624-1
- Resolved #984459 :- Upstream new release.
- Added new package google-noto-serif-khmer-fonts

* Mon Jun 24 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-5
- Resolved #971886 :- Georgian Serif fontconfig file error  

* Mon Jun 10 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-4
- Resolved #971886 :- Georgian fontconfig file error 

* Mon May 06 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-3
- Initial import
- Updated spec file

* Fri Apr 19 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-2
- Updated package as per 3rd comment on review request #953859

* Fri Apr 19 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-1
- Initial packaging
