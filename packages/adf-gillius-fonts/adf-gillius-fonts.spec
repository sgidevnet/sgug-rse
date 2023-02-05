%global fontname adf-gillius
%global fontconf 69-%{fontname}

%global common_desc \
The Gillius family from the Arkandis Digital Foundry is a set of sans-serif \
typefaces intended as an alternative to Gill Sans. Its two widths, regular and \
condensed, both feature a roman and an italic, and each includes a regular and \
bold weight.

Name:		%{fontname}-fonts
Version:	1.008
Release:	18%{?dist}
Summary:	Gillius ADF sans-serif typeface family

License:	GPLv2+ with exceptions
URL:		http://arkandis.tuxfamily.org/adffonts.html
Source0:	http://arkandis.tuxfamily.org/fonts/Gillius-Collection.zip
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}-2-fontconfig.conf
Source3:        %{fontname}.metainfo.xml
Source4:        %{fontname}-sans.metainfo.xml
Source5:        %{fontname}-sans-2.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel

Requires:	%{name}-common = %{version}-%{release}
%description
%common_desc

This is the base variant.

%_font_pkg -f %{fontconf}.conf GilliusADF-*.otf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package common
Summary:	Common files of %{fontname}
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{fontname} packages


%package -n %{fontname}-2-fonts
Summary:	Gillius ADF No2 sans-serif typeface family
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-2-fonts
%common_desc

A slightly rounder variant, which features the same set of weights,
widths, and slopes. 

%_font_pkg -n 2 -f %{fontconf}-2.conf GilliusADFNo2-*.otf
%{_datadir}/appdata/%{fontname}-sans-2.metainfo.xml

%prep
%setup -q -n Gillius-Collection
for file in NOTICE OTF/COPYING; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
			%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-2.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-2.conf \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}-2.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-2.metainfo.xml

%files common
%doc NOTICE OTF/COPYING
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.008-10
- Add metainfo file to show this font in gnome-software
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Michael J Gruber <mjg at fedoraproject.org> - 1.008-3
- split into subpackages

* Mon Nov 15 2010 Michael J Gruber <mjg at fedoraproject.org> - 1.008-2
- Add fontconfig rules for Gillius ADF No2

* Sun Nov 14 2010 Michael J Gruber <mjg at fedoraproject.org> - 1.008-1
- Initial packaging for Fedora
