%global fontname alegreya
%global fontconf 60-%{fontname}.conf
%global common_desc \
Alegreya was chosen as one of 53 "Fonts of the Decade" at the ATypI Letter2 \
competition in September 2011, and one of the top 14 text type systems. It \
was also selected in the 2nd Bienal Iberoamericana de Diseño, competition \
held in Madrid in 2010. Alegreya is a typeface originally intended for \
literature. Among its crowning characteristics, it conveys a dynamic and \
varied rhythm which facilitates the reading of long texts. Also, it \
provides freshness to the page while referring to the calligraphic letter, \
not as a literal interpretation, but rather in a contemporary typographic \
language. The italic has just as much care and attention to detail in the \
design as the roman. The bold weights are strong, and the Black weights are \
really experimental for the genre. Not only does Alegreya provide great \
performance, but also achieves a strong and harmonious text by means of \
elements designed in an atmosphere of diversity.

Name:		ht-%{fontname}-fonts
Version:	1.004
Release:	13%{?dist}
Summary:	A Serif typeface originally intended for literature
License:	OFL
URL:		http://www.huertatipografica.com.ar/tipografias/alegreya/ejemplos.html
Source0:	http://www.huertatipografica.com.ar/descargas/Alegreya.zip
Source1:	%{name}-fontconfig.conf
Source2:	ht-%{fontname}SC-fonts-fontconfig.conf
Source3:	%{fontname}.metainfo.xml
Source4:	%{fontname}SC.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
%common_desc

%package -n ht-%{fontname}-smallcaps-fonts
Summary:	SmallCaps variant of the Alegreya font family

%description -n ht-%{fontname}-smallcaps-fonts
%common_desc

This is the SmallCaps variant, in which the Capital letters are smaller.

%prep
%setup -q -c
sed -i 's/\r//' OFL.txt

%build
# Nothing to do here.

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/60-%{fontname}SC.conf

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/60-%{fontname}SC.conf \
	%{buildroot}%{_fontconfig_confdir}/60-%{fontname}SC.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}SC.metainfo.xml

%_font_pkg -f %{fontconf} Alegreya-*.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc OFL.txt

%_font_pkg -n ht-%{fontname}-smallcaps-fonts -f 60-%{fontname}SC.conf  AlegreyaSC-*.otf
%{_datadir}/appdata/%{fontname}SC.metainfo.xml
%doc OFL.txt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Richard Hughes <richard@hughsie.com> - 1.004-5
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 14 2012 Tom Callaway <spot@fedoraproject.org> - 1.004-1
- initial package
