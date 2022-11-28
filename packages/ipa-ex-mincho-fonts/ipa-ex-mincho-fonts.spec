%global		priority	68
%global		fontname	ipa-ex-mincho
%global		fontconf	%{priority}-%{fontname}.conf
%global		archiveversion	00401
%global		archivename	ipaexm%{archiveversion}

Name:		%{fontname}-fonts
Version:	004.01
Release:	3%{?dist}
Summary:	Japanese Mincho-typeface OpenType font by IPA

License:	IPA
URL:		http://ossipedia.ipa.go.jp/ipafont/
Source0:	https://oscdl.ipa.go.jp/IPAexfont/%{archivename}.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel libappstream-glib
Requires:	fontpackages-filesystem

%description
IPAex Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.

This package contains Mincho style font.

%prep
%setup -q -n %{archivename}

%build

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p	%{SOURCE1}	\
			$RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

install -m 0755 -d $RPM_BUILD_ROOT%{_metainfodir}
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_metainfodir}

ln -s	%{_fontconfig_templatedir}/%{fontconf}	\
	$RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf

%doc Readme_%{archivename}.txt
%license IPA_Font_License_Agreement_v1.0.txt
%{_metainfodir}/%{fontname}.metainfo.xml


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 004.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 004.01-2
- Install metainfo files under %%{_metainfodir}.

* Fri May 17 2019 Akira TAGOH <tagoh@redhat.com> - 004.01-1
- New upstream release.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 002.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 002.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 002.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 002.01-10
- Update the priority to change the default font to Noto.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 002.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 002.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 002.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 002.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Akira TAGOH <tagoh@redhat.com> - 002.01-5
- Add metainfo file.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 002.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 002.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 002.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Akira TAGOH <tagoh@redhat.com>
- the spec file cleanup

* Fri Nov  9 2012 Akira TAGOH <tagoh@redhat.com> - 002.01-1
- New upstream release.

* Fri Aug 17 2012 Akira TAGOH <tagoh@redhat.com> - 001.03-6
- Enable autohinting explicitly because it looks somewhat better.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Akira TAGOH <tagoh@redhat.com> - 001.03-4
- Correct fontconfig config file. (#837528)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Akira TAGOH <tagoh@redhat.com> - 001.03-1
- New upstream release.

* Fri May 28 2010 Akira TAGOH <tagoh@redhat.com> - 001.02-1
- New upstream release.

* Mon May 17 2010 Akira TAGOH <tagoh@redhat.com> - 001.01-2
- Get rid of binding="same" from the fontconfig config file.

* Mon Mar  1 2010 Akira TAGOH <tagoh@redhat.com> - 001.01-1
- Initial package.

