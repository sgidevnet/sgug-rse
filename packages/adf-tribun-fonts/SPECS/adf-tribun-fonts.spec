%global fontname adf-tribun
%global fontconf 60-%{fontname}.conf

%global archivename Tribun-Std

Name:    %{fontname}-fonts
Version: 1.13
Release: 17%{?dist}
Summary: A newsprint-like serif typeface

License:   GPLv2+ with exceptions
URL:       http://arkandis.tuxfamily.org/adffonts.html
Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/Tribun-Cat.pdf
Source2:   %{fontname}.metainfo.xml
Source11:  %{name}-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Hirwen Harendal started in 1999 the realization of a first font family, aiming
to create another “Times New Roman”… He does not consider this endeavour a huge
success. However, he transformed Tribun progessively since then to give it its
own character.

The idea was to achieve newsprint-like rendering. To this effect, the glyph
bodies, serifs, or even extenders are not normalised and use irregular strokes.
This is most visible in italics though those variations stay imperceptible at
small sizes.

Italics proved time-consuming. They are never an easy thing to draw.
Nevertheless, the designer considers them very close to those of “Times”, with
some variations.

The medium weight uses a stronger stroke. It can be used for emphasis, or for
effects in titles. That being said it has also been used for body copy. It is
also slightly expanded to complete the face offerings.

The condensed version is a bit unusual, since it stands in for both normal and
medium condensed. After several trials, Hirwen decided an intermediate weight
rendered much better both for document display and in print. Secondly, he took
great care to keep readability excellent, and this even for italics.

This font family is particularly well suited for text, display, or
presentations. It is also ideal for all Web publications. It can serve as
alternative to “Times New Roman” and other similar fonts.


%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
for txt in NOTICE */COPYING ; do
   fold -s $txt > $txt.new &&\
   sed -i 's/\r//' $txt.new &&\
   touch -r $txt $txt.new &&\
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p TTF/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc NOTICE TTF/COPYING *.pdf

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Richard Hughes <richard@hughsie.com> - 1.13-9
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov  5 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.13-2
— upstream in-place update (Tribun ADF Std Cond)

* Sat Oct 10 2009 <nicolas.mailhot at laposte.net>
- 1.13-1
— Initial release
