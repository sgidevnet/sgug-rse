%global fontname gdouros-symbola
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        10.24
Release:        5%{?dist}
Summary:        A symbol font

# https://web.archive.org/web/20150625020428/http://users.teilar.gr/~g1951d/
# "in lieu of a licence:
# Fonts and documents in this site are not pieces of property or merchandise
# items; they carry no trademark, copyright, license or other market tags;
# they are free for any use. George Douros"
License:        Public Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Symbola.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Symbola was created with Mathematics and other technical documents in mind. It
covers many scripts and symbols supported by Unicode.

These include those in Basic Latin, Latin-1 Supplement, Latin Extended-A, IPA
Extensions, Spacing Modifier Letters, Greek and Coptic, Cyrillic, Cyrillic
Supplementary, General Punctuation, Superscripts and Subscripts, and many
others.

It was created by George Douros.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Symbola.ttf %{buildroot}%{_fontdir}

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


%_font_pkg -f %{fontconf} Symbola.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Symbola.pdf Symbola.odt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 10.24-1
- New version

* Sat Dec 23 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 10.23-1
- New version, includes bugfixes and glyph additions

* Tue Oct 10 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 10.03-1
- Minor bugfixes
- Upstream now provides a changelog in the documentation

* Fri Oct 06 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 10.00-3
- And another silent update

* Thu Oct 05 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 10.00-2
- Another silent update
- Fix version number

* Mon Oct 02 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 10.0-1
- New version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Mike FABIAN <mfabian@redhat.com> - 9.17-1
- New upstream version with Unicode 10.0.0 support

* Mon May 22 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.00-3
- Move metainfo.xml to new location

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 07 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 9.00-1
- New upstream version with Unicode 9.0 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 03 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-4
- New upstream version

* Sun Jul 19 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-3
- Add license text
- Add appstream validation check

* Fri Jun 19 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-2
- Add new sources to the lookaside cache system

* Fri Jun 19 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 8.00-1
- 8.00 bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.21-0.4.20150430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.21-0.3.20150430
- Change naming scheme to cope with upstream's silent updates and internal versions

* Tue Apr 14 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.21-3
- Merge the documentation back into the font package

* Fri Mar 13 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.21-2
- Rebuilt for 20150308 internal update
- Remove font with hinting as discussed on fedora-devel mailing list
- Change license to Public Domain

* Thu Mar 05 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.21-1
- 7.21 bump

* Sun Mar 01 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 7.19-1
- 7.19 bump
- Add Symbola with hinting
- Add source package for documentation

* Sat Oct 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 6.13-6
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Petr Pisar <ppisar@redhat.com> - 6.13-1
- 6.13 bump
- Remove obsolete code from spec file
- Put heavy documentation into sub-package

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Robin Sonefors <ozamosi@flukkost.nu> - 2.54-1
- New upstream version
- Simplified description

* Thu Oct 22 2009 Robin Sonefors <ozamosi@flukkost.nu> - 2.52-1
- Initial package
