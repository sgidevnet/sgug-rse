%global fontname astigmatic-grand-hotel
%global fontconf 61-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	1.000
Release:	9%{?dist}
Summary:	Script retro style fonts

License:	OFL
URL:		http://www.astigmatic.com/
Source0:	https://www.fontsquirrel.com/fonts/download/grand-hotel/grand-hotel.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
%if 0%{?fedora} >= 21
BuildRequires:	libappstream-glib
%endif
Requires:	fontpackages-filesystem

%description
Grand Hotel finds its inspiration from the title screen of the 1937 film “Cafe 
Metropole” starring Tyrone Power. This condensed upright connecting script has 
a classic vibe to it.

It has a wonderful weight to it that feels subtly tied to Holiday and Bakery 
themed designs, even though it can work outside that genre.

%prep
%autosetup -c


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%if 0%{?fedora} >= 21
install -Dm 0644 -p %{SOURCE2} \
		%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%_font_pkg -f %{fontconf} *.otf

%license "SIL Open Font License.txt"
%if 0%{?fedora} >= 21
%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-3
- Fix appdata file

* Sat Aug 20 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-2
- Remove legacy install code line "rm -fr %%{buildroot}"

* Fri Aug 19 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-1
- Initial build
