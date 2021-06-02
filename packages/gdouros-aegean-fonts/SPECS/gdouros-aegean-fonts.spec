%global fontname gdouros-aegean
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        9.81
Release:        5%{?dist}
Summary:        A font for ancient scripts in the greater Aegean vicinity
License:        Public Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Aegean.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Aegean covers the following scripts and symbols: Basic Latin, Greek and Coptic,
Greek Extended, some Punctuation and other Symbols, Linear B Syllabary, Linear
B Ideograms, Aegean Numbers, Ancient Greek Numbers, Ancient Symbols, Phaistos
Disc, Lycian, Carian, Old Italic, Ugaritic, Old Persian, Cypriot Syllabary,
Phoenician, Lydian, Archaic Greek Musical Notation, Cretan Hieroglyphs,
Cypro-Minoan, Linear A, the Arkalochori Axe, Ancient Greek and Old Italic
variant alphabets. Those of the above that are not supported by the Unicode
Standard 8.0, they are allocated in the Supplementary Private Use Plane 15.

It was created by George Douros.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Aegean.ttf %{buildroot}%{_fontdir}

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
      %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} Aegean.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Aegean.pdf Aegean.odt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 12 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.81-1
- New version

* Sat Dec 23 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.78-1
- New version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.17-2
- Move metainfo.xml to new location

* Fri Feb 17 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.17-1
- 9.17 update

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 01 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.00-2
- Fix date in spec file

* Sat Oct 01 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.00-1
- 9.00 update

* Mon Apr 04 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.91-1
- 8.91 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.01-1
- New upstream version
- Remove license comment, since the site is back on line

* Sat Oct 24 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-4
- Updated documentation
- Fix a couple of typos in the spec file

* Fri Oct 02 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-3
- New upstream version

* Fri Jul 17 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-2
- Add license text
- Add appstream validation check

* Fri Jun 19 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-1
- 8.00 bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.45-0.3.20150430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.45-0.2.20150430
- Change naming scheme to cope with upstream's silent updates and internal versions

* Tue Apr 14 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.45-2
- Merge the documentation back into the font package
- Fix some typos

* Wed Apr 01 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.45-1
- 7.45 bump
- Add separate source package for documentation
- Add metainfo file to show this font in gnome-software
- Change license to Public Domain

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Robin Sonefors <ozamosi@flukkost.nu> - 3.02-1
- New upstream version

* Mon Oct 19 2009 Robin Sonefors <ozamosi@flukkost.nu> - 3.01-2
- Fix description, License string

* Thu Oct 15 2009 Robin Sonefors <ozamosi@flukkost.nu> - 3.01-1
- Initial packaging
