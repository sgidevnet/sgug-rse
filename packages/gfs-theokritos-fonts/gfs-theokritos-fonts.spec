%global fontname gfs-theokritos
%global fontconf 60-%{fontname}.conf

%global archivename GFS_THEOKRITOS_OT

Name:    %{fontname}-fonts
Version: 20070415
Release: 30%{?dist}
Summary: GFS Theokritos decorative font

License: OFL
URL:     http://www.greekfontsociety.gr/pages/en_typefaces20th.html
Source0: http://www.greekfontsociety.gr/%{archivename}.zip
Source1: %{name}-fontconfig.conf
Source2:   %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Yannis Kefallinos (1894–1958) was one of the most innovative engravers of his
generation and the first who researched methodicaly the aesthetics of book and
typographic design in Greece. He taught at the Fine Arts School of Athens and
established the first book design workshop from which many practising artists
of the 60's and 70's had graduated.

In the late 50's Kefallinos designed and published an exquisite book with
engraved illustrations of the ancient white funerary pottery in Attica in
collaboration with Varlamos, Montesanto, Damianakis. For the text of
Kefallinos' Δέκα λευκαί λήκυθοι (1956) the artist used a typeface which he
himself had designed a few years before for an unrealised edition of
Theocritos' Idyls. Its complex and heavily decorative design does point to
aesthetic codes which preoccupied his artistic expression and, although
impractical for contemporary text setting, it remains an original display
face, or it can be used as initials.

The book design workshop of the Fine Arts School of Athens has been recently
reorganised, under the direction of professor Leoni Vidali, and with her
collaboration George D. Matthiopoulos has redesigned digitaly this historical
font which is now available as GFS Theokritos.


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
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070415-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070415-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070415-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070415-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070415-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070415-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20070415-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Parag Nemade <pnemade AT redhat DOT com> - 20070415-22
- Fix metainfo parsing

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 20070415-21
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070415-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-12
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-11
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-10
▤ Rebuild using new « rpm-fonts »

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-7
⌖ Fedora 10 alpha general package cleanup

* Wed Apr 30 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-6
⥁ Yet another prep fix®

* Mon Mar 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-5
⚰ RIP OSX zip metadata. You won't be missed.

* Sun Feb 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070415-3
⌂ Update URL

* Mon Nov 26 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☠ 20070415-2
⚑ Re-size description so the paupers that can not afford a 80th column in
their terminal are not discriminated against.
(Courtesy: the 79-column-liberation-front cell that subverted the rpmlint
codebase)

* Sun Nov 25 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 20070415-1
✓ initial packaging
