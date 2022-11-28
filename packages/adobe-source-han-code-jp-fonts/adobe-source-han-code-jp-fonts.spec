%global fontname adobe-source-han-code-jp
%global fontconf 68-%{fontname}.conf
%global archivename source-han-code-jp-%{version}R

Name:		adobe-source-han-code-jp-fonts
Version:	2.011
Release:	3%{?dist}
Summary:	Adobe OpenType UI font for mixed Latin and Japanese text

License:	OFL
URL:		https://github.com/adobe-fonts/source-han-code-jp/
Source0:	https://github.com/adobe-fonts/source-han-code-jp/archive/%{version}R/%{archivename}.zip
Source1:	%{name}-fontconfig.conf

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Source Han Code JP is a derivative of Source Han Sans that replaces
its proportional Latin glyphs with fixed-width 667-unit glyphs from
Source Code Pro. The Latin glyphs are scaled to match the glyphs for
Japanese kana and kanji, and their widths are adjusted to be exactly
667 units (two-thirds of an EM). Source Han Code JP is intended to be
used as a UI font for mixed Latin and Japanese text on displays,
for programming, editing HTML/CSS, viewing text or inputing to
the command line in a terminal app, and so on.

%prep
%autosetup -n %{archivename}
chmod 0644 README.md

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s	%{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.otf

%license LICENSE.txt
%doc README.md relnotes.txt

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Akira TAGOH <tagoh@redhat.com> - 2.011-1
- Update to 2.011.

* Wed Jul 18 2018 Akira TAGOH <tagoh@redhat.com> - 2.000-6
- Update the priority to make Noto default.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Akira TAGOH <tagoh@redhat.com> - 2.000-3
- Correct fontconfig config.

* Mon Oct 30 2017 Akira TAGOH <tagoh@redhat.com> - 2.000-2
- Correct the file permission for README.md
- Correct the source URL.

* Fri Oct 27 2017 Akira TAGOH <tagoh@redhat.com> - 2.000-1
- Initial packaging.
