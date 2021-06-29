%global fontname adf-accanthis
%global fontconf 60-%{fontname}

%global archivename Accanthis-Std-20101124

%global common_desc \
A Latin typeface published by Hirwen Harendal's Arkandis Digital Foundry, \
Accanthis was inspired from the “Cloister Oldstyle” typeface found in the \
“American Specimen Book of Typefaces Suplement”. Its medium contrast is \
sufficient to be reader-friendly and deliver an elegant and refined experience.\
\
Its creator considers it as a “modernized” garaldic typeface. \
\
Accanthis is well suited to book typesetting and refined presentations.


Name:      %{fontname}-fonts
# Use the main PS version (as documented in NOTICE)
Version:   1.8
Release:   14%{?dist}
Summary:   A “modernized” garaldic serif typeface, “Galliard” alternative

License:   GPLv2+ with exceptions
URL:       http://arkandis.tuxfamily.org/adffonts.html
Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/Accanthis-Cat.pdf
Source11:  %{name}-fontconfig.conf
Source12:  %{name}-fontconfig-2.conf
Source13:  %{name}-fontconfig-3.conf
Source14:  %{fontname}.metainfo.xml
Source15:  %{fontname}-2.metainfo.xml
Source16:  %{fontname}-3.metainfo.xml


BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc

It is intended to serve as alternative to the “Galliard” typeface.

%_font_pkg -f %{fontconf}.conf AccanthisADFStd-*.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml


%package common
Summary:  Common files of %{name}
Requires: fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n adf-accanthis-2-fonts
Summary:  A “modernized” garaldic serif, “Horley old style” alternative
Requires: %{name}-common = %{version}-%{release}

%description -n adf-accanthis-2-fonts
%common_desc

This variant is closer to the “Horley old style” typeface than the original
version.

%_font_pkg -n 2 -f %{fontconf}-2.conf AccanthisADFStdNo2-*.otf
%{_datadir}/appdata/%{fontname}-2.metainfo.xml


%package -n adf-accanthis-3-fonts
Summary:  A “modernized” garaldic serif typeface
Requires: %{name}-common = %{version}-%{release}

%description -n adf-accanthis-3-fonts
%common_desc

This variant remixes a slightly modified Accanthis nº2 with elements from the
original Italic and changes to k, p, z and numbers.


%_font_pkg -n 3 -f %{fontconf}-3.conf AccanthisADFStdNo3-*.otf
%{_datadir}/appdata/%{fontname}-3.metainfo.xml


%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
for txt in NOTICE.txt OTF/COPYING ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-2.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-3.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-2.metainfo.xml
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-3.metainfo.xml

for fconf in %{fontconf}.conf \
             %{fontconf}-2.conf \
             %{fontconf}-3.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done



%files common
%doc NOTICE.txt OTF/COPYING *.pdf


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 1.8-6
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Paul Flo Williams <paul@frixxon.co.uk> - 1.8-2
- Correct some spellings

* Wed Jul 25 2012 Paul Flo Williams <paul@frixxon.co.uk> - 1.8-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 06 2009 <nicolas.mailhot at laposte.net>
- 1.6-4
— Stealth upstream update


* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
— 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 <nicolas.mailhot at laposte.net>
- 1.6-2
— Use a macro construct friendlier to pre-F12 releases

* Sun Jul 12 2009 <nicolas.mailhot at laposte.net>
- 1.6-1
– Initial packaging
