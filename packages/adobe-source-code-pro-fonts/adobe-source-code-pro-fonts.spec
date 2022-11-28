%global fontname adobe-source-code-pro
%global fontconf 61-%{fontname}.conf

%global version_roman  2.030
%global version_italic 1.050

Name:           %{fontname}-fonts
Version:        %{version_roman}.%{version_italic}
Release:        7%{?dist}
Summary:        A set of mono-spaced OpenType fonts designed for coding environments

License:        OFL
URL:            https://github.com/adobe-fonts/source-code-pro
Source0:        https://github.com/adobe-fonts/source-code-pro/archive/%{version_roman}R-ro%2f%{version_italic}R-it.tar.gz#/SourceCodePro-%{version_roman}R-ro-%{version_italic}R-it.tar.gz
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
This font was designed by Paul D. Hunt as a companion to Source Sans. It has
the same weight range as the corresponding Source Sans design.  It supports
a wide range of languages using the Latin script, and includes all the
characters in the Adobe Latin 4 glyph set.


%prep
%setup -qn source-code-pro-%{version_roman}R-ro-%{version_italic}R-it
sed -i 's/\r//' LICENSE.txt
chmod 644 LICENSE.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc README.md
%license LICENSE.txt

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.030.1.050-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.030.1.050-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.030.1.050-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.030.1.050-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.030.1.050-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.030.1.050-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Michael Kuhn <suraia@ikkoku.de> - 2.030.1.050-1
- Update to roman fonts 2.030 and italic fonts 1.050

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.010.1.030-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.010.1.030-1
- update to 2.010 (roman) and 1.030 (italic)
- update URL
- use %%license macro

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 1.017-5
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 13 2013 Matt Rose mattrose@folkwolf.net - 1.017-3
- rebuilt on fedora 19

* Mon Jan 21 2013 Tobias Florek me@ibotty.net - 1.017-2
- remove now empty clean section

* Thu Jan 17 2013 Tobias Florek me@ibotty.net - 1.017-1
- new upstream release

* Fri Dec 07 2012 Tobias Florek me@ibotty.net - 1.013-1
- new upstream release

* Sun Nov 18 2012 Tobias Florek me@ibotty.net - 1.010-2
- do not clean buildroot on install and clean

* Tue Oct  2 2012 Tobias Florek me@ibotty.net - 1.010-1
- new upstream release

* Tue Sep 25 2012 Tobias Florek me@ibotty.net - 1.009-3
- do not package ttf files

* Tue Sep 25 2012 Tobias Florek me@ibotty.net - 1.009-2
- Initial version
