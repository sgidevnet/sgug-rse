%global	fontname jomolhari
%global fontconf 65-0-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	0.003
Release:	27%{?dist}
Summary:	Jomolhari a Bhutanese style font for Tibetan and Dzongkha

License:	OFL
# Looks like currently following URL is gone now. Maybe temporary issue
#URL:		http://chris.fynn.googlepages.com/jomolhari
# Try following URL for this package
#URL:           https://sites.google.com/site/chrisfynn2/home/fonts/jomolhari
Source0:	http://chris.fynn.googlepages.com/jomolhari-alpha003c.zip
Source1:        %{name}-fontconfig.conf 
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Jomolhari is an TrueType OpenType Bhutanese style font for Dzongkha and
Tibetan text. It is based on Bhutanese manuscript examples, supports the
Unicode and the Chinese encoding for Tibetan.
The font supports the standard combinations used in most texts.

%prep
%setup -q -c

%build
# Empty build section

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

for i in FONTLOG.txt OFL-FAQ.txt OFL.txt
do
	tr -d '\r' < $i > ${i}.tmp
	mv -f ${i}.tmp $i
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f 65-0-%{fontname}.conf *.ttf
%doc FONTLOG.txt OFL-FAQ.txt OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.003-19
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Parag <pnemade AT redhat DOT com> - 0.003-15
- Resolves:rh#879544: upstream source url not active

* Thu Aug 16 2012 Parag <pnemade AT redhat DOT com> - 0.003-14
- Resolves:rh#847627 - Malformed fontconfig config file

* Tue Aug 14 2012 Parag <pnemade AT redhat DOT com> - 0.003-13
- Resolves:rh#847621 - better enabling autohinting by default
- Resolves:rh#847623 - fontconfig file isn't shipped in rpm
- Resolves:rh#847627 - Malformed fontconfig config file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Parag <pnemade AT redhat.com> - 0.003-9
- Resolves:rh#586241  - No fontconfig config files provided

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Marcin Garski <mgarski[AT]post.pl> 0.003-7
- Update to new fonts guidelines, thanks to Rajeesh K Nambiar (#477403)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 29 2008 Marcin Garski <mgarski[AT]post.pl> 0.003-5
- Update URL

* Fri Aug 31 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-4
- Fix license tag

* Fri Apr 06 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-3
- Update to 0.003c
- Change license from GPL to OFL

* Fri Mar 23 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-2
- Extend description section

* Mon Mar 12 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-1
- Initial specfile
