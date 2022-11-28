%global fontname silkscreen
%global fontconf 60-%{fontname}

%global common_desc \
Silkscreen is a four member type family for your Web graphics created by Jason \
Kottke. Silkscreen is best used in places where extremely small graphical \
display type is needed. The primary use is for navigational items (nav bars, \
menus, etc), but it works well wherever small type is needed. In order to \
preserve the proper spacing and letterforms, Silkscreen should be used at 8pt. \
multiples (8pt., 16pt., 24pt., etc.) with anti-aliasing turned off. \

Name:		%{fontname}-fonts
Summary: 	Silkscreen four member type family
Version:	1.0
Release:	20%{?dist}
# License attribution confirmed by author and Open Font Library
# http://openfontlibrary.org/media/files/jkottke/218
License:	OFL
Source0:	http://www.kottke.org/plus/type/silkscreen/download/silkscreen.tar.gz
Source1:	%{name}-fontconfig.conf
Source2:	%{name}-expanded-fontconfig.conf
Source3:	%{fontname}.metainfo.xml
Source4:	%{fontname}-expanded.metainfo.xml
URL:		http://www.kottke.org/plus/type/silkscreen/
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}

%description
%common_desc

%package common
Summary:	Common files for Silkscreen fonts (documentation...)
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other Silkscreen packages.

%package -n %{fontname}-expanded-fonts
Summary:	Expanded Silkscreen font family
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-expanded-fonts
%common_desc

This font family has a slightly expanded spacing between the letters in 
comparison to the normal Silkscreen font family.

%_font_pkg -n expanded -f %{fontconf}-expanded.conf slkscre*.ttf
%{_datadir}/appdata/%{fontname}-expanded.metainfo.xml

%prep
%setup -q -c -n %{name}

%build

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-expanded.conf

for fontconf in %{fontconf}.conf %{fontconf}-expanded.conf ; do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-expanded.metainfo.xml

%_font_pkg -f %{fontconf}.conf slkscr.ttf slkscrb.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%files common
%doc readme.txt
%dir %{_fontdir}

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 1.0-13
- modernize spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 Richard Hughes <richard@hughsie.com> - 1.0-11
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-2
- rework package for new font guidelines

* Tue Dec 11 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-1
- Initial package for Fedora
