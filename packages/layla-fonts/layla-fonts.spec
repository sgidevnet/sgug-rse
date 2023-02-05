%global fontname layla
%global fontconf 67-%{fontname}
Name:		%{fontname}-fonts
Version:	2.0
Release:	6%{?dist}
Summary:	A collection of traditional Arabic fonts
License:	OFL
URL:		http://sites.google.com/site/mohammedisam2000/home/projects
Source0:	http://sites.google.com/site/mohammedisam2000/home/projects/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	fontpackages-devel


%description
This package is a collection of traditional Arabic fonts (including Thuluth,
Koufi, Ruqaa..) in addition to other newly designed fonts. The aim is to 
provide all the basic fonts an Arabic user will need under X window system.
More fonts will be added regularly to the collection to make it the only font
source an Arabic user will need to install under the X window system

%package -n %{fontname}-diwani-fonts
Summary: Arabic Diwani font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-diwani-fonts
Arabic Diwani font - Part of the Layla fonts collection

%package -n %{fontname}-koufi-fonts
Summary: Arabic Koufi font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-koufi-fonts
Arabic Koufi font - Part of the Layla fonts collection

%package -n %{fontname}-thuluth-fonts
Summary: Arabic Thuluth font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-thuluth-fonts
Arabic Thuluth font - Part of the Layla fonts collection

%package -n %{fontname}-boxer-fonts
Summary: Arabic Boxer font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-boxer-fonts
Arabic Boxer font - Part of the Layla fonts collection

%package -n %{fontname}-ruqaa-fonts
Summary: Arabic Ruqaa font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-ruqaa-fonts
Arabic Ruqaa font - Part of the Layla fonts collection

%package -n %{fontname}-basic-arabic-fonts
Summary: Basic Arabic font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-basic-arabic-fonts
Basic Arabic font - Part of the Layla fonts collection

%package -n %{fontname}-arcyarc-fonts
Summary: ArcyArc font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-arcyarc-fonts
ArcyArc font - Part of the Layla fonts collection

%package -n %{fontname}-digital-fonts
Summary: Digital font - Part of the Layla fonts collection
Requires: %{name}-common = %{version}-%{release}
%description -n %{fontname}-digital-fonts
Digital font - Part of the Layla fonts collection

%package -n %{name}-common
Requires: fontpackages-filesystem
Summary: Common files for the Layla fonts package collection
%description -n %{name}-common
Common files for the Layla fonts package collection

%_font_pkg -n koufi -f %{fontconf}-Koufi.conf LaylaKoufi*.ttf
%_font_pkg -n thuluth -f %{fontconf}-Thuluth.conf LaylaThuluth*.ttf
%_font_pkg -n boxer -f %{fontconf}-Boxer.conf LaylaBoxer*.ttf
%_font_pkg -n ruqaa -f %{fontconf}-Ruqaa.conf LaylaRuqaa*.ttf
%_font_pkg -n basic-arabic -f %{fontconf}-BasicArabic.conf LaylaBasicArabic*.ttf
%_font_pkg -n diwani -f %{fontconf}-Diwani.conf LaylaDiwani*.ttf
%_font_pkg -n arcyarc -f %{fontconf}-ArcyArc.conf LaylaArcyArc*.ttf
%_font_pkg -n digital -f %{fontconf}-Digital.conf LaylaDigital*.ttf

%prep
%setup -q

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
			%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p confs/%{fontconf}-Koufi.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Koufi.conf
install -m 0644 -p confs/%{fontconf}-Thuluth.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Thuluth.conf
install -m 0644 -p confs/%{fontconf}-Boxer.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Boxer.conf
install -m 0644 -p confs/%{fontconf}-Ruqaa.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Ruqaa.conf
install -m 0644 -p confs/%{fontconf}-BasicArabic.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-BasicArabic.conf
install -m 0644 -p confs/%{fontconf}-Diwani.conf \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Diwani.conf
install -m 0644 -p confs/%{fontconf}-ArcyArc.conf \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ArcyArc.conf
install -m 0644 -p confs/%{fontconf}-Digital.conf \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Digital.conf

for fconf in %{fontconf}-Koufi.conf \
		%{fontconf}-Diwani.conf \
		%{fontconf}-ArcyArc.conf \
		%{fontconf}-Digital.conf \
		%{fontconf}-Thuluth.conf \
		%{fontconf}-Boxer.conf \
		%{fontconf}-Ruqaa.conf \
		%{fontconf}-BasicArabic.conf ; do
	ln -s %{_fontconfig_templatedir}/$fconf \
		%{buildroot}%{_fontconfig_confdir}/$fconf
done


%files common
%doc README FONTLOG.txt ChangeLog OFL.txt OFL-FAQ.txt Authors


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.0-1
- Fixed fonts. They work on MacOS now
- Changed Latin letters and numbers

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.7-1
- Fixed the font lookup tables

* Thu Nov 05 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.6-2
- Added Digital font

* Mon Nov 02 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.5-3
- Fixed ligation issue in Windows by adding missing tables

* Mon Oct 12 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.5-2
- Added ArcyArc font
- Added Diwani Font
- Increased glyph size
- Fixed gap problem with large font sizes

* Wed Oct 07 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.5-1
- Added numbers and symbol glyphs to the BasicArabic font file
- Fixed FontForge errors in the font files

* Fri Feb 06 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.4-1
- Added SIL license files & FONTLOG.txt

* Fri Feb 06 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.3-1
- Fixed spec file - removed man & info pages

* Fri Feb 06 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.2-1
- Fixed issues with spec file & missing license

* Wed Jul 16 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-1
- Updated info and manpages

* Fri Mar 21 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release
