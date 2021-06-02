%global fontname adobe-source-han-mono
%global fontconf 68-%{fontname}.conf
%global archivename source-han-mono-%{version}R

Name:		adobe-source-han-mono-fonts
Version:	1.002
Release:	4%{?dist}
Summary:	Adobe OpenType monospaced font for mixed Latin and CJK text

License:	OFL
URL:		https://github.com/adobe-fonts/source-han-mono/
Source0:	https://github.com/adobe-fonts/source-han-mono/releases/download/%{version}/SourceHanMono.ttc
Source1:	https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/LICENSE.md
Source2:	https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/README.md
Source10:	%{name}-fontconfig.conf
Source11:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel libappstream-glib
Requires:	fontpackages-filesystem

%description
Source Han Mono, which is derived from Source Han Sans and Source Code Pro,
is an OpenType/CFF Collection (OTC) that includes 70 font instances—consisting
of seven weights, five languages, and two styles—and is a Pan-CJK version
of Source Han Code JP.

%prep
%autosetup -c -T
cp -a %{SOURCE0} .
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_metainfodir}
install -m 0644 -p %{SOURCE11} %{buildroot}%{_metainfodir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s	%{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%_font_pkg -f %{fontconf} *.ttc

%license LICENSE.md
%doc README.md
%{_metainfodir}/%{fontname}.metainfo.xml

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.002-3
- Update sources.

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.002-2
- Use tagged url for sources.

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.002-1
- New upstream release.

* Tue Jun  4 2019 Akira TAGOH <tagoh@redhat.com> - 1.001-3
- Add BR: libappstream-glib.

* Mon Jun  3 2019 Akira TAGOH <tagoh@redhat.com> - 1.001-2
- Install appdata.xml file into %%{_metainfodir}.
- Run validator for appdata in %%check.

* Fri May 31 2019 Akira TAGOH <tagoh@redhat.com> - 1.001-1
- New upstream release.
- Add metainfo file.

* Thu May 30 2019 Akira TAGOH <tagoh@redhat.com> - 1.000-1
- Initial packaging.
