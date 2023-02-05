%global fontname google-croscore
%global fontconf62 62-%{fontname}
%global fontconf30 30-0-%{fontname}

%global common_desc \
This package contains a collections of fonts that offers improved on-screen \
readability characteristics and the pan-European WGL character set and solves \
the needs of developers looking for width-compatible fonts to address document \
portability across platforms.


Name:           %{fontname}-fonts
Version:        1.31.0
Release:        4%{?dist}
Summary:        The width-compatible fonts for improved on-screen readability

License:        ASL 2.0
#URL:            
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/croscorefonts-%{version}.tar.bz2

Source1:        62-%{fontname}-arimo-fontconfig.conf
Source2:        62-%{fontname}-cousine-fontconfig.conf
Source3:        62-%{fontname}-tinos-fontconfig.conf
Source4:        30-0-%{fontname}-arimo-fontconfig.conf
Source5:        30-0-%{fontname}-cousine-fontconfig.conf
Source6:        30-0-%{fontname}-tinos-fontconfig.conf

# Upstream has not provided license text in their tarball release
# Add ASL2.0 license text in LICENSE-2.0.txt file
Source8:        LICENSE-2.0.txt

# metainfo files for gnome-software
Source9:        %{fontname}-arimo.metainfo.xml
Source10:        %{fontname}-cousine.metainfo.xml
Source11:        %{fontname}-tinos.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc


%package common
Summary:        Common files of %{name}
Requires:       fontpackages-filesystem

# As upstream stopped distributing SymbolNeu font, let's obsolete this subpackage.
Obsoletes:      google-croscore-symbolneu-fonts < 1.31.0-1

%description common
This package consists of files used by other %{name} packages.


%package -n %{fontname}-arimo-fonts
Summary:       The croscore Arimo family fonts 
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-arimo-fonts
%common_desc
Arimo was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Arial. Arimo offers improved 
on-screen readability characteristics and the pan-European WGL character set 
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%_font_pkg -n arimo -f *-%{fontname}-arimo.conf Arimo*.ttf
%{_datadir}/appdata/%{fontname}-arimo.metainfo.xml

%package -n %{fontname}-cousine-fonts
Summary:       The croscore Cousine family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-cousine-fonts
%common_desc
Cousine was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Courier New. Cousine offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%_font_pkg -n cousine -f *-%{fontname}-cousine.conf  Cousine*.ttf
%{_datadir}/appdata/%{fontname}-cousine.metainfo.xml

%package -n %{fontname}-tinos-fonts
Summary:       The croscore Tinos family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tinos-fonts
%common_desc
Tinos was designed by Steve Matteson as an innovative, refreshing serif design
that is metrically compatible with Times New Roman. Tinos offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to
address document portability across platforms.

%_font_pkg -n tinos -f *-%{fontname}-tinos.conf Tinos*.ttf
%{_datadir}/appdata/%{fontname}-tinos.metainfo.xml

%prep
%setup -q -n croscorefonts-%{version}
cp -p %{SOURCE8} .

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-arimo.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-cousine.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-tinos.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-arimo.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-cousine.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-tinos.conf

for fconf in %{fontconf62}-arimo.conf %{fontconf30}-arimo.conf \
             %{fontconf62}-cousine.conf %{fontconf30}-cousine.conf \
             %{fontconf62}-tinos.conf %{fontconf30}-tinos.conf
do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-arimo.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-cousine.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tinos.metainfo.xml

%files common
%license LICENSE-2.0.txt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.31.0-2
- Move Obsoletes: to common subpackage

* Mon Nov 12 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.31.0-1
- Update to 1.31.0 version
- Dropped SymbolNeu subpackage as upstream stopped releasing it

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 20 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.23.0-6
- Add metainfo files to show Arimo, Cousine, Tinos fonts in gnome-software

* Wed Sep 03 2014 Parag Nemade <pnemade AT redhat DOT com>- 1.23.0-5
- Drop fontconfig for Symbol Neu font
- Fix rh#1037882 - Wrong character displayed with google-croscore-symbolneu-fonts installed 

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.23.0-1
- Update to next upstream release 1.23.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.21.0-3
- Resolves:rh#814631-Typo in 62-google-croscore-cousine-fontconfig.conf

* Tue Mar 27 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.21.0-2
- Updated fontconfig rules.

* Wed Mar 21 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.21.0-1
- Initial packaging
