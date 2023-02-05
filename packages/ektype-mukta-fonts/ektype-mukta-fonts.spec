%global fontname ektype-mukta
%global fontconf 67-%{fontname}
%global common_desc \
Mukta is a typeface available in \
seven weights, supporting Devanagari, Gujarati, Tamil and Latin scripts.

Name:			%{fontname}-fonts
Version:			2.538
Release:			5%{?dist}
Summary:		Free Indian truetype/open type fonts
License:			OFL
URL:			https://github.com/EkType/Mukta
Source0:		https://github.com/EkType/Mukta/releases/download/%{version}/Mukta.Font.Family.%{version}.zip
Source1:		%{name}-devanagari-fontconfig.conf
Source2:		%{name}-vaani-fontconfig.conf
Source3:		%{name}-mahee-fontconfig.conf
Source4:		%{name}-malar-fontconfig.conf
Source5:		%{fontname}.devanagari.metainfo.xml
Source6:		%{fontname}.vaani.metainfo.xml
Source7:		%{fontname}.mahee.metainfo.xml
Source8:		%{fontname}.malar.metainfo.xml
BuildArch:		noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Requires:		fontpackages-filesystem

%description
%common_desc

%package common
Summary:		Common files of %{name}
Requires:		fontpackages-filesystem

%description common
%common_desc

%package -n %{fontname}-devanagari-fonts
Summary:		Free Devanagari font
Requires:		%{name}-common = %{version}-%{release}
Obsoletes:		ekmukta-fonts < 1.2.2-9
Provides:		ekmukta-fonts = %{version}-%{release}

%description -n %{fontname}-devanagari-fonts
%common_desc
This package provides a free devanagari truetype/open type font.
%_font_pkg -n devanagari -f %{fontconf}-devanagari.conf Mukta-*.ttf
%{_datadir}/metainfo/%{fontname}.devanagari.metainfo.xml

%package -n %{fontname}-vaani-fonts
Summary:		Free Gujarati font
Requires:		%{name}-common = %{version}-%{release}

%description -n %{fontname}-vaani-fonts
%common_desc
This package provides a free Gujarati truetype/open type font.
%_font_pkg -n vaani -f %{fontconf}-vaani.conf MuktaVaani-*.ttf
%{_datadir}/metainfo/%{fontname}.vaani.metainfo.xml

%package -n %{fontname}-mahee-fonts
Summary:		Free Gurmukhi font
Requires:		%{name}-common = %{version}-%{release}

%description -n %{fontname}-mahee-fonts
%common_desc
This package provides a free Gurmukhi truetype/open type font.
%_font_pkg -n mahee -f %{fontconf}-mahee.conf MuktaMahee-*.ttf
%{_datadir}/metainfo/%{fontname}.mahee.metainfo.xml

%package -n %{fontname}-malar-fonts
Summary:		Free Tamil font
Requires:		%{name}-common = %{version}-%{release}

%description -n %{fontname}-malar-fonts
%common_desc
This package provides a free Tamil truetype/open type font.
%_font_pkg -n malar -f %{fontconf}-malar.conf MuktaMalar-*.ttf
%{_datadir}/metainfo/%{fontname}.malar.metainfo.xml

%prep
%autosetup -c  
sed -i 's/\r$//' *.txt README.md

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p */*.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-devanagari.conf
install -m 0644 -p %{SOURCE2} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-vaani.conf
install -m 0644 -p %{SOURCE3} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mahee.conf
install -m 0644 -p %{SOURCE4} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-malar.conf

install -Dm 0644 -p %{SOURCE5} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.devanagari.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.vaani.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.mahee.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.malar.metainfo.xml

for fconf in %{fontconf}-devanagari.conf \
		%{fontconf}-vaani.conf \
		%{fontconf}-mahee.conf \
		%{fontconf}-malar.conf; do
	ln -s %{_fontconfig_templatedir}/$fconf \
		%{buildroot}%{_fontconfig_confdir}/$fconf
done

%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.*.metainfo.xml

%files common
%doc AUTHORS.txt README.md CONTRIBUTORS.txt
%license OFL.txt Copyright.txt 

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.538-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 2.538-4
- Font CI test added 

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.538-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 2.538-2
- updated obsoletes and provides values for ektype-mukta-devanagari-fonts subpackage

* Mon Sep 17 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 2.538-1
- first release of ektype-mukta fonts
