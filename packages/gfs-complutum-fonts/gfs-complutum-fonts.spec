%global fontname gfs-complutum
%global fontconf 61-%{fontname}.conf

%global archivename GFS_COMPLUTUM_OT

Name:    %{fontname}-fonts
Version: 20070413
Release: 28%{?dist}
Summary: GFS Complutum Greek font

License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces16th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{name}-fontconfig.conf
Source2:   %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
The ancient Greek alphabet evolved during the millenium of the Byzantine era
from majuscule to minuscule form and gradually incorporated a wide array of
ligatures, flourishes and other decorative nuances which defined its
extravagant cursive character. Until the late 15th century, typographers who
had to deal with Greek text avoided emulating this complicated hand; instead
they would use only the twenty four letters of the alphabet separately, often
without accents and other diacritics.

A celebrated example is the type cut and cast for the typesetting of the New
Testament in the so-called Complutensian Polyglot Bible (1512), edited by the
Greek scholar, Demetrios Doukas. The type was cut by Arnaldo Guillén de Brocar
and the whole edition was a commision by cardinal Francisco Ximénez, in the
University of Alcalá (Complutum), Spain. It is one of the best and most
representative models of this early tradition in Greek typography which was
revived in the early 20th century by the eminent bibliographer of the British
Library, Richard Proctor. A font named Otter Greek was cut in 1903 and a book
was printed using the new type. The original type had no capitals so Proctor
added his own, which were rather large and ill-fitted. The early death of
Proctor, the big size of the font and the different aesthetic notions of the
time were the reasons that Otter Greek was destined to oblivion, as a
curiosity.

Greek Font Society incorporated Brocar's famous and distinctive type in the
commemorative edition of Pindar's Odes for the Athens Olympics (2004) and the
type with a new set of capitals, revived digitaly by George D. Matthiopoulos,
is now available for general use.


%prep
%setup -q -c -T
unzip -j -L -q %{SOURCE0}
chmod 0644 *.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


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

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%doc *.txt *.pdf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20070413-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 20070413-20
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070413-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070413-11
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070413-10
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070413-9
▤ Rebuild using new « rpm-fonts »

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070413-8
⌖ Fedora 10 alpha general package cleanup

* Wed Apr 30 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070413-7
⥁ Yet another prep fix®

* Mon Mar 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070413-6
⚰ RIP OSX zip metadata. You won't be missed.

* Sun Feb 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☠ 20070413-4
⌂ Update URL

* Mon Nov 26 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☠ 20070413-3
⚑ Re-size description so the paupers that can not afford a 80th column in
their terminal are not discriminated against.
(Courtesy: the 79-column-liberation-front cell that subverted the rpmlint
codebase)

* Sun Nov 25 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 20070413-2
✓ initial packaging
