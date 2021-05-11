%global fontname apa-new-athena-unicode
%global fontconf 64-%{fontname}.conf


Name:		%{fontname}-fonts
Version:	3.4
Release:	18%{?dist}
Summary:	New Athena Unicode is a libre/open multilingual font

License:	OFL
URL:		http://apagreekkeys.org/NAUdownload.html
Source0:	http://apagreekkeys.org/fonts/NAU3_4ttf.zip
Source1:	%{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
New Athena Unicode is an libre/open multilingual font distributed by
the American Philological Association. It follows the latest version
of the Unicode standard and includes characters for English and
Western European languages, polytonic Greek, Coptic, Old Italic, 
and Demotic Egyptian transliteration, as well as metrical symbols
and other characters used by classical scholars.

%prep
%setup -q -n NAU3_4ttf

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
%doc *.pdf *.rtf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.4-10
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 15 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.4-2
- Made changes according to bug #511336
- changed fontconf priority to 64
- changed description 
* Tue Jul 14 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.4-1
- initial rpm build

