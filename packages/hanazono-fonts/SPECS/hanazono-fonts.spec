%global	fontname	hanazono
%global archivename	%{fontname}-%{version}
%global	priority	66
%global fontconf	%{priority}-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	20170904
Release:	6%{?dist}
Summary:	Japanese Mincho-typeface TrueType font

License:	Copyright only or OFL
URL:		http://fonts.jp/hanazono/
Source0:	http://ija.osdn.net/projects/hanazono-font/downloads/68253/%{archivename}.zip
Source1:	%{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel libappstream-glib
Requires:	fontpackages-filesystem

%description
Hanazono Mincho typeface is a Japanese TrueType font that developed with
a support of Grant-in-Aid for Publication of Scientific Research Results from
Japan Society for the Promotion of Science and the International Research
Institute for Zen Buddhism (IRIZ), Hanazono University. also with volunteers
who work together on glyphwiki.org.

This font contains 107518 characters in ISO/IEC 10646 and Unicode Standard,
also supports character sets:
 - 6355 characters in JIS X 0208:1997
 - 5801 characters in JIS X 0212:1990
 - 3695 characters in JIS X 0213:2004
 - 6763 characters in GB 2312-80
 - 13053 characters in Big-5
 - 4888 characters in KS X 1001:1992
 - 360 characters in IBM extensions
 - 9810 characters in IICORE
 - Kanji characters in GB18030-2000
 - Kanji characters in Adobe-Japan1-6

%prep
%setup -q -T -c -a 0


%build


%install
install -dm 0755 $RPM_BUILD_ROOT%{_fontdir}
install -pm 0644 *.ttf $RPM_BUILD_ROOT%{_fontdir}
install -dm 0755 $RPM_BUILD_ROOT%{_fontconfig_templatedir} \
		 $RPM_BUILD_ROOT%{_fontconfig_confdir}
install -pm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} $RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc LICENSE.txt README.txt THANKS.txt
%{_metainfodir}/%{fontname}.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 20170904-5
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 20170904-1
- Updates to 20170904.
- Update the priority to change the default font to Noto.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 20141012-2
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove buildroot which is optional now
- Remove removal of buildroot in %%install
- Remove group tag

* Wed Oct 15 2014 Akira TAGOH <tagoh@redhat.com> - 20141012-1
- New upstream release. (#1152054)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131208-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 11 2013 Akira TAGOH <tagoh@redhat.com> - 20131208-1
- New upstream release. (#1039477)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Akira TAGOH <tagoh@redhat.com> - 20130222-1
- New upstream release. (#914077)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120421-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Akira TAGOH <tagoh@redhat.com> - 20120421-1
- New upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Akira TAGOH <tagoh@redhat.com> - 20120202-1
- New upstream release. (#786779)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110915-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Akira TAGOH <tagoh@redhat.com> - 20110915-1
- New upstream release. (#738594)
- Update License tag to make this dual license with SIL OFL since 20101013.

* Thu May 26 2011 Akira TAGOH <tagoh@redhat.com> - 20110516-1
- New upstream release. (#705302)

* Fri Apr  8 2011 Akira TAGOH <tagoh@redhat.com> - 20101013-1
- New upstream release. (#692826)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100718-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Akira TAGOH <tagoh@redhat.com> - 20100718-1
- New upstream release.
  - contains certain glyphs to cover Japanese (#586213)

* Tue May 25 2010 Akira TAGOH <tagoh@redhat.com> - 20100222-3
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100222-2
- Get rid of compare="contains".

* Fri Apr 16 2010 Akira TAGOH <tagoh@redhat.com> - 20100222-1
- Update to 20100222.
- Get rid of binding="same" from fontconfig config file. (#578019)

* Fri Nov 27 2009 Akira TAGOH <tagoh@redhat.com> - 20091003-1
- Update to 20091003.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081012-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081012-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-6
- Update the spec file to fit into new guideline. (#477395)

* Fri Nov 14 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-5
- Fix a typo in fontconfig config again.

* Thu Nov 13 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-4
- Try to test the language with the exact match in fontconfig config.

* Wed Nov 12 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-3
- Fix a typo in fontconfig config.

* Mon Nov 10 2008 Akira TAGOH <tagoh@redhat.com>
- Drop -f from fc-cache.
- Improve fontconfig config.

* Mon Nov 10 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-2
- Improve a bit in the spec file.

* Tue Oct 28 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-1
- Initial packaging.

