%global fontname fontsquirrel-crete-round
%global fontconf 63-%{fontname}.conf

Name:          %{fontname}-fonts
Version:       0
Release:       0.6.20111222%{?dist}
Summary:       General purpose warm slab serif font
License:       OFL
URL:           https://www.fontsquirrel.com/fonts/crete-round
Source0:       https://www.fontsquirrel.com/fonts/download/crete-round#/crete-round.zip
Source1:       %{name}.conf
BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Crete Round is a warm slab serif providing a hint of softness to texts. It
started as a tailored version of the original Crete fonts -
www.type-together.com/Crete - created specially to serve as corporate typeface
for the type design competition Letter2 - www.letter2.org. Crete Round is more
independent from the original with modified terminals and serifs to create two
new fonts that deliver a more contemporary and functional appearance. The tall
x-height, low contrast and sturdy slabs prove to be surprisingly efficient for
web use. This font supports 128 languages and has 416 glyphs.

%prep
%setup -qc

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p CreteRound-{Italic,Regular}.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} CreteRound-{Italic,Regular}.otf

%license *.txt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20111222
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20111222
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20111222
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20111222
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20111222
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Nov 23 2016 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.20111222
- initial build
