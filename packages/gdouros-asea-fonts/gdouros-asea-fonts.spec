%global fontname gdouros-asea
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        8.01
Release:        5%{?dist}
Summary:        Asea is an etude on the dominant typeface of Greek typography
License:        Public Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Textfonts.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem
Recommends:     gdouros-textfonts-doc

%description
Asea is an etude on the dominant typeface of Greek typography. Upright Greek
letters were designed in 1805 by Firmin Didot (1764-1836) and cut by Walfard
and Vibert. The typeface, together with a complete printing house, was donated
in 1821 to the new Greek state by Didot's son, Ambroise Firmin Didot (1790-
1876).

The font covers the Windows Glyph List, IPA Extensions, Greek Extended, Ancient
Greek Numbers, Byzantine and Ancient Greek Musical Notation, various
typographic extras and several Open Type features (Case-Sensitive Forms, Small
Capitals, Subscript, Superscript, Numerators, Denominators, Fractions, Old
Style Figures, Historical Forms, Stylistic Alternates, Ligatures).

It was created by George Douros.

%prep
%setup -q -c

%build

%install
rm -f *_hint.ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/Asea*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
      %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} Asea*.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.01-1
- New version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.17-2
- Move metainfo.xml to new location

* Fri Feb 17 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.17-1
- Update to 7.17

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 11 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.31-2
- Remove documentation file and recommend Textfonts documentation subpackage

* Thu Feb 11 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.31-1
- 6.31 version bump
- Remove license info from when the site was off-line

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 3 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.00-1
- New upstream version

* Thu May 28 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.01-1
- First release

