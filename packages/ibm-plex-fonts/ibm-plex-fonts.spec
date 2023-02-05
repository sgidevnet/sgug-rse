%global fontname ibm-plex
%global fontconf 60-%{fontname}

%global common_desc \
Plex is an open-source project (OFL) and free to download and use. The Plex \
family comes in a Sans, Serif, Mono and Sans Condensed, all with roman and \
true italics. The fonts have been designed to work well in user interface \
(UI) environments as well as other mediums.

Name:           %{fontname}-fonts
Version:        4.0.2
Release:        1%{?dist}
Summary:        IBM's Plex fonts

License:        OFL
URL:            https://github.com/IBM/plex
Source0:        https://github.com/IBM/plex/releases/download/v%{version}/OpenType.zip##/%{name}-%{version}.zip
Source1:        %{name}-sans-fontconfig.conf
Source2:        %{fontname}-sans.metainfo.xml
Source3:        %{name}-serif-fontconfig.conf
Source4:        %{fontname}-serif.metainfo.xml
Source5:        %{name}-mono-fontconfig.conf
Source6:        %{fontname}-mono.metainfo.xml
Source7:        %{name}-sans-condensed-fontconfig.conf
Source8:        %{fontname}-sans-condensed.metainfo.xml
Source9:        %{name}-sans-arabic-fontconfig.conf
Source10:       %{fontname}-sans-arabic.metainfo.xml
Source11:       %{name}-sans-devanagari-fontconfig.conf
Source12:       %{fontname}-sans-devanagari.metainfo.xml
Source13:       %{name}-sans-hebrew-fontconfig.conf
Source14:       %{fontname}-sans-hebrew.metainfo.xml
Source15:       %{name}-sans-thai-looped-fontconfig.conf
Source16:       %{fontname}-sans-thai-looped.metainfo.xml
Source17:       %{name}-sans-thai-fontconfig.conf
Source18:       %{fontname}-sans-thai.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

%description
%common_desc


%package common
Summary:        Common files of IBM Plex fonts
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-sans-fonts
Summary:        IBM's Plex Sans fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This package contains the Sans version of IBM's Plex fonts.

%_font_pkg -n sans -f %{fontconf}-sans.conf *Sans-*.otf
%{_datadir}/metainfo/%{fontname}-sans.metainfo.xml

%package -n %{fontname}-serif-fonts
Summary:        IBM's Plex Serif fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

This package contains the Serif version of IBM's Plex fonts.

%_font_pkg -n serif -f %{fontconf}-serif.conf *Serif-*.otf
%{_datadir}/metainfo/%{fontname}-serif.metainfo.xml

%package -n %{fontname}-mono-fonts
Summary:        IBM's Plex Mono fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-mono-fonts
%common_desc

This package contains the Mono version of IBM's Plex fonts.

%_font_pkg -n mono -f %{fontconf}-mono.conf *Mono-*.otf
%{_datadir}/metainfo/%{fontname}-mono.metainfo.xml

%package -n %{fontname}-sans-condensed-fonts
Summary:        IBM's Plex Sans Condensed fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-condensed-fonts
%common_desc

This package contains the Sans Condensed version of IBM's Plex fonts.

%_font_pkg -n sans-condensed -f %{fontconf}-sans-condensed.conf *SansCondensed-*.otf
%{_datadir}/metainfo/%{fontname}-sans-condensed.metainfo.xml

%package -n %{fontname}-sans-arabic-fonts
Summary:        IBM's Plex Sans Arabic fonts
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{fontname}-arabic-fonts = %{version}-%{release}
Obsoletes:      %{fontname}-arabic-fonts < 2.0.0-2

%description -n %{fontname}-sans-arabic-fonts
%common_desc

This package contains the Sans Arabic version of IBM's Plex fonts.

%_font_pkg -n sans-arabic -f %{fontconf}-sans-arabic.conf *SansArabic-*.otf
%{_datadir}/metainfo/%{fontname}-sans-arabic.metainfo.xml

%package -n %{fontname}-sans-devanagari-fonts
Summary:        IBM's Plex Sans Devanagari fonts
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{fontname}-devanagari-fonts = %{version}-%{release}
Obsoletes:      %{fontname}-devanagari-fonts < 2.0.0-2

%description -n %{fontname}-sans-devanagari-fonts
%common_desc

This package contains the Sans Devanagari version of IBM's Plex fonts.

%_font_pkg -n sans-devanagari -f %{fontconf}-sans-devanagari.conf *SansDevanagari-*.otf
%{_datadir}/metainfo/%{fontname}-sans-devanagari.metainfo.xml

%package -n %{fontname}-sans-hebrew-fonts
Summary:        IBM's Plex Sans Hebrew fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-hebrew-fonts
%common_desc

This package contains the Sans Hebrew version of IBM's Plex fonts.

%_font_pkg -n sans-hebrew -f %{fontconf}-sans-hebrew.conf *SansHebrew-*.otf
%{_datadir}/metainfo/%{fontname}-sans-hebrew.metainfo.xml

%package -n %{fontname}-sans-thai-looped-fonts
Summary:        IBM's Plex Sans Thai Looped fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-thai-looped-fonts
%common_desc

This package contains the Sans Thai Looped version of IBM's Plex fonts.

%_font_pkg -n sans-thai-looped -f %{fontconf}-sans-thai-looped.conf *SansThaiLooped-*.otf
%{_datadir}/metainfo/%{fontname}-sans-thai-looped.metainfo.xml

%package -n %{fontname}-sans-thai-fonts
Summary:        IBM's Plex Sans Thai fonts
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{fontname}-thai-fonts = %{version}-%{release}
Obsoletes:      %{fontname}-thai-fonts < 2.0.0-2

%description -n %{fontname}-sans-thai-fonts
%common_desc

This package contains the Sans Thai version of IBM's Plex fonts.

%_font_pkg -n sans-thai -f %{fontconf}-sans-thai.conf *SansThai-*.otf
%{_datadir}/metainfo/%{fontname}-sans-thai.metainfo.xml

%prep
%autosetup -n OpenType


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p */*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-condensed.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-arabic.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-devanagari.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-hebrew.conf
install -m 0644 -p %{SOURCE15} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-thai-looped.conf
install -m 0644 -p %{SOURCE17} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-thai.conf

for fconf in %{fontconf}-sans.conf \
             %{fontconf}-serif.conf \
             %{fontconf}-mono.conf \
             %{fontconf}-sans-condensed.conf \
             %{fontconf}-sans-arabic.conf \
             %{fontconf}-sans-devanagari.conf \
             %{fontconf}-sans-hebrew.conf \
             %{fontconf}-sans-thai-looped.conf \
             %{fontconf}-sans-thai.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata file, Repeat for every font family
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-serif.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-condensed.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-arabic.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-devanagari.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-hebrew.metainfo.xml
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-thai-looped.metainfo.xml
install -Dm 0644 -p %{SOURCE18} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-thai.metainfo.xml

%check
# Repeat for every font family
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-serif.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-mono.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-condensed.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-arabic.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-devanagari.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-hebrew.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-thai-looped.metainfo.xml
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}-sans-thai.metainfo.xml

%files common
%license IBM-Plex-Sans/license.txt


%changelog
* Fri Dec 13 2019 Michael Kuhn <suraia@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2

* Fri Dec 06 2019 Michael Kuhn <suraia@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1

* Sun Sep 08 2019 Michael Kuhn <suraia@fedoraproject.org> - 2.0.0-1
- Initial package
