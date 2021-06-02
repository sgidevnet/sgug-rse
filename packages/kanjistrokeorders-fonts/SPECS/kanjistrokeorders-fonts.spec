%global fontname kanjistrokeorders
%global fontconf 69-%{fontname}.conf
%global archivename KanjiStrokeOrders_v%{version}

Name:    %{fontname}-fonts
Version: 3.001
Release: 10%{?dist}
Summary: Font to view stroke order diagrams for Kanji, Kana and etc
License: BSD
URL:     http://sites.google.com/site/nihilistorguk/
Source0: https://dl.dropboxusercontent.com/u/39004158/%{archivename}.zip
Source1: %{name}-fontconfig.conf
Source2: %{fontname}.metainfo.xml
BuildArch: noarch
BuildRequires: fontpackages-devel
%description
This font will assist people who are learning kanji, and will help teachers of
Japanese in the preparation of classroom material.
In the parts of your document where you want the kanji to be annotated with
stroke order numbers simply set your document's font to KanjiStrokeOrders.
You will need to set the size of the font to be large to allow the stroke
order numbers to show up: 100pt seems to be the minimum usable size.


%prep
%setup -q -c
sed -i 's#\r##g' copyright.txt
sed -i 's#\r##g' readme_en_v%{version}.utf

%build
%{nil}


%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


%files
%_font_pkg -f %{fontconf} *.ttf
%doc *.pdf *.txt *.utf
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.001-2
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove buildroot which is optional now
- Remove removal of buildroot in %%install
- Remove %%defattr
- Remove group tag

* Mon Sep 22 2014 Paul Flo Williams <paul@frixxon.co.uk> - 3.001-1
- New upstream version, with additions and improvements to about 40 characters

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Paul Flo Williams <paul@frixxon.co.uk> - 3.000-1
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 29 2011 Paul Flo Williams <paul@frixxon.co.uk> - 2.016-1
- New upstream version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct  16 2010 René Ribaud <rene.ribaud@free.fr> - 2.015-1
- New package with Kanji stroke order font 2.015 release.

* Fri May  07 2010 René Ribaud <rene.ribaud@free.fr> - 2.014-4
- Corrections after Parag AN review #1 of this new package.
- Replace dos2unix by sed to convert files.
- Remove some comments.

* Sun Mar  21 2010 René Ribaud <rene.ribaud@free.fr> - 2.014-3
- Fix changelog.

* Sun Mar  21 2010 René Ribaud <rene.ribaud@free.fr> - 2.014-2
- Correction after Fedora-Fr review.

* Sat Feb  20 2010 René Ribaud <rene.ribaud@free.fr> - 2.014-1
- Initial build.
