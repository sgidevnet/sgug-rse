%global fontname gdouros-aegyptus
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        6.17
Release:        7%{?dist}
Summary:        A font for Egyptian hieroglyphs

# https://web.archive.org/web/20150625020428/http://users.teilar.gr/~g1951d/
# "in lieu of a licence:
# Fonts and documents in this site are not pieces of property or merchandise
# items; they carry no trademark, copyright, license or other market tags;
# they are free for any use. George Douros"
License:        Public Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Aegyptus.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Aegyptus contains an Extended List of 7062 Egyptian Hieroglyphs, in regular and
bold font weights.

There is no standard for Egyptian Hieroglyphs or Meroitic, so they are
allocated in the Supplementary Private Use Plane 15. The fonts also cover Basic
Latin and some Punctuation and other Symbols.

They were created by George Douros, mainly based on the book Hieroglyphica,
PIREI I², 2000 and the work of Alan Gardiner.

%prep
%setup -q -c

%build

%install
rm -f *_hint.ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Aegyptus*.ttf %{buildroot}%{_fontdir}

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


%_font_pkg -f %{fontconf} Aegyptus*.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc *.pdf

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.17-2
- Move metainfo.xml to new location

* Fri Feb 17 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 6.17-1
- 6.17 update
- Fix bogus date in changelog

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.03-0.9.20151024
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.03-0.8.20151024
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 24 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.03-0.7.20151024
- Updated documentation

* Sat Oct 03 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.03-0.6.20151001
- Aegyptus bold was modified upstream

* Fri Jul 17 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.03-0.5.20150618
- Add license text
- Add appstream validation check

* Fri Jun 19 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.03-0.4.20150618
- Rebuilt for 20150618 silent upstream update

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.03-0.3.20150430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.03-0.2.20150430
- Change naming scheme to cope with upstream's silent updates and internal versions
- Drop Gardiner and Nilus fonts

* Thu Apr 02 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.03-2
- Merge the documentation back into the font package
- Update Nilus font to 5.11

* Thu Apr 02 2015 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.03-1
- 5.03 bump
- Upstream has split the font into three parts; they are all included now
- Add metainfo file to show this font in gnome-software
- Add separate source packages for documentation
- Change license to Public Domain

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Robin Sonefors <ozamosi@flukkost.nu> 3.11-1
- New upstream version

* Thu Jan 14 2010 Robin Sonefors <ozamosi@flukkost.nu> 3.10-1
- New upstream version

* Wed Oct 21 2009 Robin Sonefors <ozamosi@flukkost.nu> 2.52-1
- Initial package
