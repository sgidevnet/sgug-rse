%global fontname ecolier-court
%global fontconf 61-%{fontname}

%global common_desc\
Écolier court fonts were created by Jean-Marie Douteau to mimic the \
traditional cursive writing French children are taught in school. \
\
He kindly released two of them under the OFL, which are redistributed in \
this package.


Name:    %{fontname}-fonts
Version: 20070702
Release: 27%{?dist}
Summary: Schoolchildren cursive fonts

License:   OFL
URL:       http://perso.orange.fr/jm.douteau/page_ecolier.htm
# The author links to third-party licence documents not included there
Source0:   http://perso.orange.fr/jm.douteau/polices/ecl_cour.ttf
Source1:   http://perso.orange.fr/jm.douteau/polices/ec_cour.ttf
Source2:   http://perso.orange.fr/jm.douteau/polices/lisez_moi.txt
Source3:   README-Fedora.txt
Source4:   %{name}-fontconfig.conf
Source5:   %{name}-lignes-fontconfig.conf
Source6:   %{fontname}.metainfo.xml
Source7:   %{fontname}-lignes.metainfo.xml


BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      %{name}-common = %{version}-%{release}

%description
%common_desc

%_font_pkg -f %{fontconf}-lignes.conf ecl_cour.ttf
%{_datadir}/appdata/%{fontname}-lignes.metainfo.xml


%package common
Summary:  Common files of the Écolier Court font set
Requires: fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-lignes-fonts
Summary:  Schoolchildren cursive fonts with lines
Requires: %{name}-common = %{version}-%{release}

Obsoletes: %{name}-lignes < 20070702-7

%description -n %{fontname}-lignes-fonts
%common_desc

The « lignes » (lines) Écolier court font variant includes the Seyes lining
commonly used by schoolchildren notepads.

%_font_pkg -n lignes -f %{fontconf}.conf ec_cour.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml


%prep
%setup -q -c -T
iconv -f iso-8859-15 -t utf-8 %{SOURCE2} > lisez_moi.txt
touch -r %{SOURCE2} lisez_moi.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done
install -m 0644 -p %{SOURCE3} .


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{SOURCE1} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lignes.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-lignes.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-lignes.metainfo.xml


%files common
%doc *.txt


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070702-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 18 2014 Richard Hughes <richard@hughsie.com> - 20070702-19
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070702-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070702-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070702-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070702-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070702-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070702-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 28 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-12
— Tweak the fontconfig fixing

* Sun Sep 13 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-11
— Fix the font naming to something more user friendly (remove PS1 legacy
  limitations)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20070702-10
— Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20070702-9
— Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-8
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sat Jan 17 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-7
• Convert to new naming guidelines

* Wed Dec 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-5
⬊ Workaround RHEL5 rpm unicode bug to fix koji build

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-4
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-3
▤ Rebuild using new « rpm-fonts »

* Sat Jul 19 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20070702-1
⚱ Stop waitting for upstream to answer distribution change requests
♔ FESCO chickened out on UTF-8 names
♿ FESCO decision unimplementable due to bug #455119
⚙ Sync spec style with the way our font packaging guidelines have evolved
⚤ Package both fonts in a single package
  I'm going to consider they are two faces of the same font
∞ Register in new fontconfig generic families
⬢ Add upstream readme translation as asked in review

* Sun Nov 25 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 1.00-0.4.20070628
✓ sync with packaging guidelines

* Sat Sep 8 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 1.00-0.2.20070628
✓ use more accurate naming
✓ add an ASCII alias as suggested in review

* Tue Aug 28 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 1.00-0.1.20070628
✓ Initial packaging (based on DejaVu & Charis specs)
