%global fontname kurdit-unikurd-web
%global archivename unikurdweb
%global fontconf 65-%{fontname}.conf

Name:          %{fontname}-fonts
Version:       20020502
Release:       22%{?dist}
Summary:       A widely used Kurdish font for Arabic-like scripts and Latin

License:       GPLv3
URL:           http://www.kurditgroup.org/node/1337
# Below is only working Source URL
Source0:       https://www.kurditgroup.org/sites/default/files/unikurdweb_0.zip
Source1:       65-kurdit-unikurd-web.conf
Source2:       %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
Obsoletes:     unikurd-web-font < 20020502-2

%description
A widely used Kurdish font which supports various Arabic-like scripts
(Arabic, Kurdish, Persian) and also Latin.

%prep
%autosetup -c %{archivename}

%build
#nothing to do

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

%_font_pkg -f 65-kurdit-unikurd-web.conf *.ttf
%license gpl.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20020502-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20020502-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20020502-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 20020502-19
- Update Source tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20020502-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20020502-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20020502-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20020502-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 Parag Nemade <pnemade AT redhat DOT com> - 20020502-13
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Parag <pnemade AT redhat.com> - 20020502-8
- Resolves:rh#837535 - Malformed fontconfig config file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Parag <pnemade AT redhat.com> - 20020502-5
- Resolves:rh#586259- No fontconfig config files provided

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Michal Nowak <mnowak@redhat.com> - 20020502-2
- repackage to save myself a grief

* Sun Jan 25 2009 Michal Nowak <mnowak@redhat.com> - 20020502-1
- renamed from unikurd-web-font -> kurdit-unikurd-web-fonts
- enhanced %%description field
- changes for F11 fonts rules
- add Obsoletes: unikurd-web-font <= 20020502-1

* Tue Oct 14 2008 Michal Nowak <mnowak@redhat.com> - 20020502
- version is now based on date of last issue of the font
- %%defattr(-,root,root,-) -> %%defattr(644,root,root,755)

* Mon Oct 13 2008 Michal Nowak <mnowak@redhat.com> - 1.00-2
- got rid of -web sub-package
- changed name from unikurd-fonts-web to unikurd-web-font
- minor structural changes in SPEC file

* Wed Jul 30 2008 Michal Nowak <mnowak@redhat.com> - 1.00-1
- initial packaging
- this package should be prepared for another unikurd fonts
  in sub-packages because on the KurdIT group/unikurd web there
  are plenthora of them, but probably not under suitable licenses

