%global fontname paratype-pt-serif
%global fontconf 57-%{fontname}

%global common_desc \
The PT Serif family was developed as a second part of the project \
“Public Types of Russian Federation”. This project aims at enabling \
The project is dedicated to the 300-year anniversary of the Russian civil \
type invented by Peter the Great from 1708 to 1710, and was realized \
with financial support from the Russian Federal Agency for Press and \
Mass Communications. \
\
PT Serif is a transitional serif face with humanistic terminals designed \
for use together with PT Sans and harmonized with PT Sans on metrics, \
proportions, weights and design. PT Serif consists of six styles: regular \
and bold weights with corresponding italics form a standard computer font \
family for basic text setting; two caption styles (regular and italic) \
are for texts of small point sizes. \
\
PT Serif was designed by Alexandra Korolkova with participation \
of Olga Umpeleva and under supervision of Vladimir Yefimov. \

Name:           %{fontname}-fonts
Version:        20141121
Release:        9%{?dist}
Summary:        A pan-Cyrillic typeface

License:        OFL
URL:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTSerifOFL.zip
Source10:       %{name}-fontconfig.conf
Source11:       %{name}-caption-fontconfig.conf
Source12:       %{fontname}.metainfo.xml
Source13:       %{fontname}-caption.metainfo.xml

BuildArch:      noarch
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel

%description
%common_desc

This package includes regular, bold and their italic styles.

%_font_pkg -f %{fontconf}.conf PTF*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%package -n %{fontname}-caption-fonts
Summary:        A pan-Cyrillic typeface (caption forms for small text)
BuildRequires:  fontpackages-devel

%description -n %{fontname}-caption-fonts
%common_desc

This package includes 2 captions styles for small text sizes.

%_font_pkg -n caption -f %{fontconf}-caption.conf PTZ*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}-caption.metainfo.xml


%prep
%setup -q -c
sed -i "s|\r||g" *.txt

%build
echo "Nothing to build"

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caption.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-caption.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-caption.metainfo.xml


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 21 2014 Rajeesh K V <rajeesh AT inflo DOT ws> - 20141121-1
- Changed version to today in YYYYMMDD format
- Fixed wrong end of line encoding in license text

* Mon Nov 17 2014 Rajeesh K V <rajeesh AT inflo DOT ws> - 20103012-1
- Initial packaging
