%global fontname dustin-dustismo
%global fontconf 63-%{fontname}

%global common_desc General purpose fonts by Dustin Norlander available in \
serif and sans-serif versions. The fonts cover all European Latin characters.

Name:          %{fontname}-fonts
Version:       20030318
Release:       21%{?dist}
Summary:       General purpose sans-serif font with bold, italic and bold-italic variations

License:       GPLv2+
URL:           http://www.dustismo.com
# Actual download URL
#URL:           http://ftp.de.debian.org/debian/pool/main/t/ttf-dustin/ttf-dustin_20030517.orig.tar.gz 
Source0:       Dustismo.zip
Source1:       %{name}-sans-fontconfig.conf
Source2:       %{name}-roman-fontconfig.conf
Source3:       %{fontname}.metainfo.xml
Source4:       %{fontname}-sans.metainfo.xml
Source5:       %{fontname}-roman.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc

%package common
Summary:       Common files for %{name}
Requires:      fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-sans-fonts
Summary:       General purpos sans-serif fonts
Requires:      %{name}-common = %{version}-%{release}
Provides:      %{name} = 20030318-3
Obsoletes:     %{name} < 20030318-3

%description -n %{fontname}-sans-fonts
%common_desc

General purpose sans-serif font with bold, italic and bold-italic variations

%_font_pkg -n sans -f %{fontconf}-sans.conf dustismo_bold_italic.ttf dustismo_bold.ttf dustismo_italic.ttf Dustismo.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package -n %{fontname}-roman-fonts
Summary:       General purpose serif font
Requires:      %{name}-common = %{version}-%{release}
Provides:      %{name}-roman = 20030318-3
Obsoletes:     %{name}-roman < 20030318-3

%description -n %{fontname}-roman-fonts
%common_desc

General purpose serif font with bold, italic and bold-italic variations

%_font_pkg -n roman -f %{fontconf}-roman.conf Dustismo_Roman_Bold.ttf Dustismo_Roman.ttf Dustismo_Roman_Italic_Bold.ttf Dustismo_Roman_Italic.ttf      
%{_datadir}/appdata/%{fontname}-roman.metainfo.xml

%prep
%setup -q -c %{name}
sed -i 's/\r//' license.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-roman.conf

for fontconf in %{fontconf}-sans.conf %{fontconf}-roman.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-roman.metainfo.xml

%files common
%doc license.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20030318-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20030318-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20030318-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20030318-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20030318-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Richard Hughes <rhughes@redhat.com> - 20030318-16
- Actually install the AppData files

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20030318-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20030318-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 20030318-12
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove buildroot which is optional now
- Remove removal of buildroot in %%install
- Remove %%defattr
- Remove group tag
- Change %%define to %%global

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20030318-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Sven Lankes <sven@lank.es> - 20030318-3
- rename according to new naming-guidelines

* Wed Jan 07 2009 Sven Lankes <sven@lank.es> - 20030318-2
- Change package-name to dustin-dustistmo-fonts

* Sun Jan 04 2009 Sven Lankes <sven@lank.es> - 20030318-1
- Use newer debian-source as source
- Convert to -multi spec

* Wed Dec 31 2008 Sven Lankes <sven@lank.es> - 20030207-1
- Initial packaging

