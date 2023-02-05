%global fontname paratype-pt-mono
%global fontconf 57-%{fontname}

%global common_desc \
Font PT Mono™ is the last addition to the pan-Cyrillic font superfamily \
including PT Sans and PT Serif developed for the project “Public Types \
of Russian Federation”. \
\
PT Mono was developed for the special needs — for use in forms, tables, \
work sheets etc. Equal widths of characters are very helpful in setting \
complex documents, with such font you may easily calculate size of entry \
fields, column widths in tables and so on. One of the most important area \
of use is Web sites of “electronic governments” where visitors have to fill \
different request forms. PT Mono consists of Regular and Bold styles. \
\
PT Mono was designed by Alexandra Korolkova with participation of \
Isabella Chaeva and with financial support of Google.\


Name:           %{fontname}-fonts
Version:        20141121
Release:        9%{?dist}
Summary:        A pan-Cyrillic monospace typeface

License:        OFL
URL:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTMonoOFL.zip
Source10:       %{name}-fontconfig.conf
Source11:       %{fontname}.metainfo.xml

BuildArch:      noarch
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel

%description
%common_desc

This package consists of Regular and Bold styles.

%_font_pkg -f %{fontconf}.conf PTM*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


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

for fconf in %{fontconf}.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


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

* Mon Nov 17 2014 Rajeesh K V <rajeesh AT inflo DOT ws> - 20113012-1
- Initial packaging
