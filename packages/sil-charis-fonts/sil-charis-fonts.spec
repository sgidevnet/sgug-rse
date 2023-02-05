%global fontname sil-charis
%global fontconf 60-%{fontname}.conf

%global archivename CharisSIL

Name:    %{fontname}-fonts
Version: 5.000
Release: 9%{?dist}
Summary: A serif smart font similar to Bitstream Charter

License:   OFL
URL:       http://scripts.sil.org/CharisSILFont
# Actual download URL
# http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=%{archivename}.zip&filename=%{archivename}%{version}.zip
Source0:   %{archivename}-%{version}.zip
Source1:   %{name}-fontconfig.conf
Source2:   %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
Obsoletes:     charis-fonts < 4.104-5

%description
Charis SIL provides glyphs for a wide range of Latin and Cyrillic characters.
Charis is similar to Bitstream Charter, one of the first fonts designed
specifically for laser printers. It is highly readable and holds up well in
less-than-ideal reproduction environments. It also has a full set of styles
— regular, italic, bold, bold italic — and so is more useful in general
publishing than Doulos SIL. Charis is a serif proportionally spaced font
optimized for readability in long printed documents.


%prep
%setup -q -n %{archivename}-%{version}
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 01 2014 Kevin Fenzi <kevin@scrye.com> 5.000-1
- Update to 5.000

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 4.114-4
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.114-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Kevin Fenzi <kevin@scrye.com> 4.114-1
- Update to 4.114

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.106-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.106-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.106-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.106-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.106-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 27 2009 <nicolas.mailhot at laposte.net>
- 4.106-2
– Propose Charis SIL as substitute to Charis SIL Compact when it's not available

* Fri May 21 2009 <nicolas.mailhot at laposte.net>
- 4.106-1
– This version supports Unicode 5.1 and adds support for Small capitals

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 4.104-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 4.104-7
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Tue Jan 27 2009 <nicolas.mailhot at laposte.net>
- 4.104-6
► renamed to “sil-charis-fonts” to apply Packaging:FontsPolicy#Naming

* Sun Nov 23 2008 <nicolas.mailhot at laposte.net>
- 4.104-4
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 <nicolas.mailhot at laposte.net>
- 4.104-3
▤ Rebuild using new « rpm-fonts »

* Fri Jul 11 2008 <nicolas.mailhot at laposte.net>
- 4.104-2
⌖ Fedora 10 alpha general package cleanup

* Sun May 18 2008 <nicolas.mailhot at laposte.net>
- 4.104-1
⧉ New Unicode 5.1 compliant release, with some glyphs moved out of PUA

* Sat Nov 3 2007 <nicolas.mailhot at laposte.net>
☺ 4.100-5
✓ Sync with guidelines
✓ fix config file misplacement

* Thu Nov 1 2007 <nicolas.mailhot at laposte.net>
☺ 4.100-4
✓ Sync with guidelines
✓ new fontconfig aliasing syntax

* Tue Aug 28 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 4.100-3
✓ Sync with dejavu spec
✓ Licence++

* Thu Jun 21 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 4.100-2
✓ Fix URL (bug #245101)

* Thu May 31 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 4.100-1
✓ add fontconfig setup file
✓ make spec closer to the dejavu one to simplify maintenance

* Thu Nov 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 4.0.02-3
- Remove ghost-ed fontconfig cache files

* Tue Sep 19 2006 Kevin Fenzi <kevin@tummy.com> - 4.0.02-2
- Rebuild for fc6
- Add dist tag

* Sat Feb 18 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 4.0.02-1
- Initial packaging, based on gentium-fonts
