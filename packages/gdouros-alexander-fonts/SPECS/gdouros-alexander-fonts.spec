%global fontname gdouros-alexander
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        8.01
Release:        5%{?dist}
Summary:        A Greek typeface inspired by Alexander Wilson
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
A text typeface using the Greek letters designed by Alexander Wilson
(1714-1786), a Scottish doctor, astronomer, and type founder, who established a
type foundry in Glasgow in 1744. The type was especially designed for an
edition of Homer’s epics, published in 1756-8 by Andrew and Robert Foulis,
printers to the University of Glasgow. A modern revival, Wilson Greek, was
designed by Matthew Carter in 1995. Peter S. Baker is also using Wilson’s Greek
type in his Junicode font for medieval scholars (2007).

Latin and Cyrillic are based on a Garamond typeface. The font covers the
Windows Glyph List, IPA Extensions, Greek Extended, Ancient Greek Numbers,
Byzantine and Ancient Greek Musical Notation, various typographic extras and
several Open Type features (Case-Sensitive Forms, Small Capitals, Subscript,
Superscript, Numerators, Denominators, Fractions, Old Style Figures, Historical
Forms, Stylistic Alternates, Ligatures).

It was created by George Douros.

%package -n gdouros-textfonts-doc
Summary:        Documentation for all Textfonts by G. Douros
%description -n gdouros-textfonts-doc
This package contains documentation regarding the Textfonts family of fonts by
G. Douros, i.e. Aroania, Anaktoria, Alexander, Avdira and Asea. The origin of
each font is presented, as well as sample texts along with a character overview
and opentype features supported by the fonts.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/Alexander.ttf %{buildroot}%{_fontdir}

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


%_font_pkg -f %{fontconf} Alexander.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%files -n gdouros-textfonts-doc
%doc Textfonts.pdf Textfonts.odt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.01-1
- New version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.17-3
- Move metainfo.xml to new location

* Sun Feb 19 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.17-2
- Update documentation

* Fri Feb 17 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.17-1
- Update to 7.17

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 11 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.31-2
- Update documentation
- Create documentation subpackage for all Textfonts

* Thu Feb 11 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.31-1
- 6.31 version bump
- Remove license info from when the site was off-line

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 17 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.00-2
- Add license text
- Add appstream validation check

* Fri Jun 19 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.00-1
- 6.00 bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.01-0.3.20150430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.01-0.2.20150430
- Change naming scheme to cope with upstream's silent updates and internal versions

* Tue Apr 14 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.01-2
- Merge the documentation back into the font package

* Fri Apr 03 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.01-1
- 5.01 bump
- Add separate source package for documentation
- Add metainfo file to show this font in gnome-software
- Change license to Public Domain

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.01-7
- Honor %%{_docdir_fmt}.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 18 2009 Robin Sonefors <ozamosi@flukkost.nu> - 3.01-2
- Fix fontconfig priority and categorization
- Add sample document

* Thu Oct 22 2009 Robin Sonefors <ozamosi@flukkost.nu> - 3.01-1
- Initial packaging
