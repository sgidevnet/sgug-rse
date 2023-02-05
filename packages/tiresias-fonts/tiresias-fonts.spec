%global fontname tiresias
%global fontconf 60-%{fontname}.conf

%global common_desc \
The Tiresias family of fonts has been designed for use in multiple environments \
to help improve legibility, especially for individuals with visual impairment. \
It includes specialized fonts for information labels, control labels (for key \
tops), large print publications, computer systems, television subtitling, and \
signs.

Name:		%{fontname}-fonts
Summary: 	Low vision fonts
Version:	1.0
Release:	24%{?dist}
# Font exception
License:	GPLv3+ with exceptions
Source0:	http://www.tiresias.org/fonts/infofont.zip
Source1:	http://www.tiresias.org/fonts/keyfont.zip
Source2:	http://www.tiresias.org/fonts/lpfont.zip
Source3:	http://www.tiresias.org/fonts/pcfont.zip
Source4:	http://www.tiresias.org/fonts/signfont.zip
Source5:	%{name}-info-fontconfig.conf
Source6:	%{name}-info-z-fontconfig.conf
Source7:	%{name}-key-v2-fontconfig.conf
Source8:	%{name}-lp-fontconfig.conf
Source9:	%{name}-pc-fontconfig.conf
Source10:	%{name}-pc-z-fontconfig.conf
Source11:	%{name}-sign-fontconfig.conf
Source12:	%{name}-sign-z-fontconfig.conf
Source19:	%{fontname}.metainfo.xml
Source20:	%{fontname}-info.metainfo.xml
Source21:	%{fontname}-info-z.metainfo.xml
Source22:	%{fontname}-key-v2.metainfo.xml
Source23:	%{fontname}-lp.metainfo.xml
Source24:	%{fontname}-pc.metainfo.xml
Source25:	%{fontname}-pc-z.metainfo.xml
Source26:	%{fontname}-sign.metainfo.xml
Source27:	%{fontname}-sign-z.metainfo.xml
URL:		http://www.tiresias.org/fonts/
BuildRequires:	fontpackages-devel
BuildArch:	noarch

%description
%common_desc

%package common
Summary:	Common files for Tiresias fonts (documentation...)
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other Tiresias packages.

%package -n %{fontname}-info-fonts
Summary:	Specialized fonts for info terminals for the visually impaired
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-info-fonts
%common_desc

The Infofont family is specialized for use in informational labels on public 
terminals such as ATMs using large characters. The only	difference between the
Infofont and the Infofont Z families is whether the zero is crossed out or not.
In the Infofont family, the zero is _not_ crossed out, which may lead to some
confusion.

%_font_pkg -n info -f %{fontconf}-infofont.conf "Tiresias*Infofont*.ttf"
%{_datadir}/appdata/%{fontname}-info.metainfo.xml

%package -n %{fontname}-info-z-fonts
Summary:	Specialized fonts for info terminals for the visually impaired
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-info-z-fonts
%common_desc

The Infofont Z family is specialized for use in informational labels on public
terminals such as ATMs using large characters. The only difference between the
Infofont Z and the Infofont families is whether the zero is crossed out or not.
In the Infofont	Z family, the zero is crossed out.

%_font_pkg -n info-z -f %{fontconf}-infofont-z.conf "TIRESIAS*INFOFONTZ*.ttf"
%{_datadir}/appdata/%{fontname}-info-z.metainfo.xml

%package -n %{fontname}-key-v2-fonts
Summary:	Specialized fonts for labeling keycaps for the visually impaired
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-key-v2-fonts
%common_desc

The Keyfont V2 family is specialized for use in labeling keycaps.

%_font_pkg -n key-v2 -f %{fontconf}-keyfont-v2.conf TIREKV__.ttf
%{_datadir}/appdata/%{fontname}-key-v2.metainfo.xml

%package -n %{fontname}-lp-fonts
Summary:	Specialized font for large print publications
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-lp-fonts
%common_desc

The LPfont family is specialized for use in large print publications.

%_font_pkg -n lp -f %{fontconf}-lpfont.conf "Tiresias*LPfont*.ttf"
%{_datadir}/appdata/%{fontname}-lp.metainfo.xml

%package -n %{fontname}-pc-fonts
Summary:	Specialized fonts for use on PCs for the visually impaired
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-pc-fonts
%common_desc

The PCfont family is specialized for people with poor vision to use on PC 
screens using large characters. The only difference between the PCfont and 
the PCfont Z families is whether the zero is crossed out or not. In the 
PCfont family, the zero is _not_ crossed out, which may lead to some
confusion.

%_font_pkg -n pc -f %{fontconf}-pcfont.conf "Tiresias*PCfont*.ttf"
%{_datadir}/appdata/%{fontname}-pc.metainfo.xml

%package -n %{fontname}-pc-z-fonts
Summary:	Specialized fonts for use on PCs for the visually impaired
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-pc-z-fonts
%common_desc

The PCfont family is specialized for people with poor vision to use on PC
screens using large characters.	The only difference between the PCfont and 
the PCfont Z families is whether the zero is crossed out or not. In the
PCfont Z family, the zero is crossed out.

%_font_pkg -n pc-z -f %{fontconf}-pcfont-z.conf "TIRESIAS*PCFONTZ*.ttf"
%{_datadir}/appdata/%{fontname}-pc-z.metainfo.xml

%package -n %{fontname}-sign-fonts
Summary:	Specialized fonts for preparing signs for the visually impaired
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-sign-fonts
%common_desc

The Signfont family is specialized for preparing signs for the visually 
impaired, using large characters. The only difference between the Signfont and 
the Signfont Z families is whether the zero is crossed out or not. In the
Signfont family, the zero is _not_ crossed out, which may lead to some
confusion.

%_font_pkg -n sign -f %{fontconf}-signfont.conf "Tiresias*Signfont*.ttf"
%{_datadir}/appdata/%{fontname}-sign.metainfo.xml

%package -n %{fontname}-sign-z-fonts
Summary:	Specialized fonts for preparing signs for the visually impaired
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-sign-z-fonts
%common_desc

The Signfont family is specialized for preparing signs for the visually 
impaired, using	large characters. The only difference between the Signfont and 
the Signfont Z families is whether the zero is crossed out or not. In the 
Signfont Z family, the zero is crossed out.

%_font_pkg -n sign-z -f %{fontconf}-signfont-z.conf "TIRESIAS*SIGNFONTZ*.ttf"
%{_datadir}/appdata/%{fontname}-sign-z.metainfo.xml

%prep
%setup -q -c -n %{name}
%{__unzip} -qqo %{SOURCE1}
%{__unzip} -qqo %{SOURCE2}
%{__unzip} -qqo %{SOURCE3}
%{__unzip} -qqo %{SOURCE4}
for f in *.TTF; do 
	newname=`echo "$f"|sed -e 's/.TTF/.ttf/'`;
	mv "$f" "$newname"; 
done;
# correct end-of-line encoding
sed -i 's/\r//' COPYING/gpl.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-infofont.conf
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-infofont-z.conf
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-keyfont-v2.conf
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lpfont.conf
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pcfont.conf
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pcfont-z.conf
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-signfont.conf
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-signfont-z.conf

for fontconf in %{fontconf}-infofont.conf %{fontconf}-infofont-z.conf %{fontconf}-keyfont-v2.conf %{fontconf}-lpfont.conf\
		%{fontconf}-pcfont.conf %{fontconf}-pcfont-z.conf %{fontconf}-signfont.conf %{fontconf}-signfont-z.conf; do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE19} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE20} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-info.metainfo.xml
install -Dm 0644 -p %{SOURCE21} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-info-z.metainfo.xml
install -Dm 0644 -p %{SOURCE22} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-key-v2.metainfo.xml
install -Dm 0644 -p %{SOURCE23} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-lp.metainfo.xml
install -Dm 0644 -p %{SOURCE24} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-pc.metainfo.xml
install -Dm 0644 -p %{SOURCE25} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-pc-z.metainfo.xml
install -Dm 0644 -p %{SOURCE26} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sign.metainfo.xml
install -Dm 0644 -p %{SOURCE27} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sign-z.metainfo.xml

%files common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc COPYING/copying.doc COPYING/gpl.txt
%dir %{_fontdir}

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 1.0-17
- modernize spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Richard Hughes <richard@hughsie.com> - 1.0-15
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul  7 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-8
- corrected license

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 25 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-6
- rebuild for font autoprovides

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-4
- fix packaging

* Thu Jan 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-3
- rework to meet new font packaging guidelines

* Wed Jan  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-2
- font versions didn't change, but sha1sums did

* Mon Nov 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-1
- Initial package for Fedora
