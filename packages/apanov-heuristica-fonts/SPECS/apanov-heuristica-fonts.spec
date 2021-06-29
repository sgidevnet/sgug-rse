%global fontname apanov-heuristica
%global fontconf 61-%{fontname}.conf

%global archivename heuristica-ttf-%{version}
%global googlename  evristika

Name:    %{fontname}-fonts
Version: 1.0.2
Release: 12%{?dist}
Epoch:   1
Summary: A serif latin & cyrillic font

License:   OFL
URL:       http://sourceforge.net/projects/heuristica/

#we are using binary ttf archive as source archive
#is currently missing required fontforge scripts
#to compile and generate ttf files
Source0:   http://downloads.sourceforge.net/project/heuristica/%{archivename}.tar.xz
Source1:   %{name}-fontconfig.conf
Source2:   %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: dos2unix
Requires:      fontpackages-filesystem

%description
Heuristica is a serif latin & cyrillic font, derived from the “Adobe Utopia”
font that was released to the TeX Users Group under a liberal license.


%prep
%setup -q -c
dos2unix OFL-FAQ.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *\.ttf %{buildroot}%{_fontdir}

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
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Parag Nemade <pnemade AT redhat DOT com> - 1:1.0.2-4
- Fix metainfo file for & instead of &amp;

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 1:1.0.2-3
- Add metainfo file to show this font in gnome-software

* Fri Sep 26 2014 Parag Nemade <pnemade AT redhat DOT com> - 1:1.0.2-2
- Add missing BR: dos2unix

* Fri Sep 26 2014 Parag Nemade <pnemade AT redhat DOT com> - 1:1.0.2-1
- Update to 1.0.2 release
- Move to using binary ttf as source

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:0.2.2-2
— Rebuild with new xgridfit

* Sun Jun 13 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:0.2.2-1
— Switch to new upstream hosting

* Sun Jun 6 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:0.2.1-2

* Sun Nov 22 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:0.2-5
— remove evil duplicate TTF files

* Fri Oct  9 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:0.2-4
– not smp-safe upstream makefile
- 1:0.2-3
— fonttools has been fixed ⇒ generate TTFs

* Sun Sep 13 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:0.2-2
— make Bold Italic Bold Italic not BoldItalic

* Sun Sep  6 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1:0.2-1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20090507-2
— Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090507-1

* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090125-5
— Make sure F11 font packages have been built with F11 fontforge

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20090125-4
— Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090125-3
— fix url (thanks nirik)

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090125-2
— prepare for F11 mass rebuild, new rpm and new fontpackages

*Fri Jan 30 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090125-1

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20081109-3
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Sun Nov 16 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20081109-2
▤ Rebuild using new « rpm-fonts »
- 20081109-1
↝ Fedora import

* Fri Oct 10 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20080825-1
ԇ FE-LEGAL lifted — update package in review request

* Fri Jun 20 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20080619-1
я Initial packaging
