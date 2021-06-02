%global fontname gust-antykwa-torunska
%global shortname antt
%global fontconf 69-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.08
%global versiontag %(echo %{version}|tr . _)
Release:        13%{?dist}
Summary:        Two-element typeface for typesetting of small prints
License:        LPPL
URL:            http://jmn.pl/en/antykwa-torunska/
Source0:        http://jmn.pl/pliki/AntykwaTorunska-otf-%{versiontag}.zip
Source1:        %{name}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Antykwa Toruńska (meaning just "Antiqua of Torun") is a two-element
typeface designed by Zygfryd Gardzielewski in the 50’s.

The font is mainly used for typesetting of small prints. Its
characteristic features are the widening of vertical stems at the top
and the wave-like form of some of the horizontal and diagonal lines as
well as of the serifs.

The current version contains a greatly extended character set (e.g.,
cyrillic, greek, most often used mathematical symbols and currency
symbols, additional ligatures) compared to the original, as well as
additional typefaces (light, regular, medium and bold in normal and
condensed widths).

%prep
%setup -q -n %{shortname}-otf

%build

%install
mkdir -p %{buildroot}%{_fontdir}
cp -p *.otf %{buildroot}%{_fontdir}

mkdir -p %{buildroot}%{_fontconfig_templatedir} \
         %{buildroot}%{_fontconfig_confdir}
cp -p %{SOURCE1} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
         %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.otf

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 17 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> 2.08-4
- Add fontconfig rules covering rules for each family for the packaged font

* Mon Dec 16 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> 2.08-3
- Add missing %%fontconf definition.

* Tue Oct 29 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> 2.08-2
- Update %%description, fontconfig priority.

* Mon Oct 28 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> 2.08-1
- Initial packaging.
