%global fontname gfs-neohellenic
%global fontconf 60-%{fontname}.conf

%global archivename GFS_NEOHELLENIC_OT

Name:    %{fontname}-fonts
Version: 20090918
Release: 16%{?dist}
Summary: A 20th century Greek typeface

License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces20th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{name}-fontconfig.conf
Source2:   %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
The design of new Greek typefaces always followed the growing needs of the
Classical Studies in the major European Universities. Furthermore, by the end
of the 19th century bibliology had become an established section of Historical
Studies, and, as John Bowman commented, the prevailing attitude was that Greek
types should adhere to a lost idealized, yet undefined, greekness of yore.
Especially in Great Britain this tendency remained unchallenged in the first
decades of the 20th century, both by Richard Proctor, curator of the incunabula
section in the British Museum Library and his successor Victor Scholderer.

In 1927, Scholderer, on behalf of the Society for the Promotion of Greek
Studies, got involved in choosing and consulting the design and production of a
Greek type called New Hellenic cut by the Lanston Monotype Corporation. He
chose the revival of a round, and almost monoline type which had first appeared
in 1492 in the edition of Macrobius, ascribable to the printing shop of
Giovanni Rosso (Joannes Rubeus) in Venice. New Hellenic was the only successful
typeface in Great Britain after the introduction of Porson Greek well over a
century before. The type, since to 1930’s, was also well received in Greece,
albeit with a different design for Ksi and Omega.

GFS digitized the typeface (1993-1994) funded by the Athens Archeological
Society with the addition of a new set of epigraphical symbols. Later (2000)
more weights were added (italic, bold and bold italic) as well as a latin
version.


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
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20090918-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20090918-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20090918-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20090918-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20090918-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20090918-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20090918-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090918-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 20090918-8
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090918-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090918-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090918-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090918-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090918-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090918-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 5 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090918-1
— upstream stealth update

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20081217-3
— Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20081217-2
— Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20081217-1
— another GFS stealth update (thanks nirik)

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-9
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-8
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-7
▤ Rebuild using new « rpm-fonts »

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-6
⌖ Fedora 10 alpha general package cleanup

* Wed Apr 30 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-5
⥁ Yet another prep fix®

* Mon Mar 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-4
⚰ RIP OSX zip metadata. You won't be missed.

* Sun Feb 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-2
⌂ Update URL

* Sun Nov 25 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 20070415-1
✓ initial packaging
