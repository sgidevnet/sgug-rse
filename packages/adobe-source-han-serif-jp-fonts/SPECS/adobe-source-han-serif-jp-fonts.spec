%global fontname adobe-source-han-serif-jp
%global fontconf 68-%{fontname}.conf
%global archivename SourceHanSerifJP

Name:		adobe-source-han-serif-jp-fonts
Version:	1.001
Release:	6%{?dist}
Summary:	Adobe OpenType Pan-CJK font family for Japanese

License:	OFL
URL:		https://github.com/adobe-fonts/source-han-serif/
Source0:	https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/%{archivename}.zip
Source1:	%{name}-fontconfig.conf

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Source Han Serif is a set of OpenType/CFF Pan-CJK fonts.

%prep
%autosetup -n %{archivename}

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s	%{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.otf

%license LICENSE.txt

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Akira TAGOH <tagoh@redhat.com> - 1.001-4
- Update the fontconfig priority to make Noto default.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Akira TAGOH <tagoh@redhat.com> - 1.001-1
- Initial packaging.
