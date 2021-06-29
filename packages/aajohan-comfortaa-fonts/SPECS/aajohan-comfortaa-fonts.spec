%global fontname aajohan-comfortaa
%global fontconf 61-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        3.001
Release:        5%{?dist}
Summary:        Modern style true type font

License:        OFL
URL:            http://aajohan.deviantart.com
Source0:        http://www.deviantart.com/download/105395949/comfortaa___font_by_aajohan-d1qr019.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:	libappstream-glib
Requires:       fontpackages-filesystem

%description
Comfortaa is a sans-serif font comfortable in every aspect with
Bold, Regular, and Thin variants.
It has very good European language coverage and decent Cyrillic coverage.  

%prep
%autosetup -n %{version}

# Fixing
# wrong-file-end-of-line-encoding issue
# Thanks to Paul Flo Williams

for file in *.txt; do
 sed 's/\r//g' "$file" | \
 fold -s > "$file.new" && \
 touch -r "$file" "$file.new" && \
 mv "$file.new" "$file"
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
%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc FONTLOG.txt OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 3.001-1
- Update to 3.001

- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.004-4
- Add metainfo file to show this font in gnome-software

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 2.004-1
- Latest upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Luya Tshimbalanga <luya@fedoraproject.org> - 2.003-1
- Upstream update (rhbz#786442)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Luya Tshimbalanga <luya@fedoraproject.org> - 2.002-5
- Upstream update (rhbz#771541)
- Spec cleaned up
- updated filename documentation

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 3 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.004-1
- Upstream update rhbz#658745

* Thu Sep 23 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-5.1
- Changed to the correct description rhbz#636987

* Tue Aug 3 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-4
- Set the right close tag inside 61 conf file

* Fri Jul 30 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-3
- Added missing documentations
- Switched to the right versioning
- Addressed wrong-file-end-of-line-encoding issue

* Thu Jul 29 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-2
- Set prefix to 61 for fontconfig.conf
- Shortened description
- Some fixes

* Tue Jul 27 2010 Luya Tshimbalanga <luya@fedoraproject.org> - 1.003-1
- Initial RPM release.
