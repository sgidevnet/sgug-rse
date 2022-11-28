%global fontname adobe-source-han-sans-tw
%global fontconf 65-2-%{fontname}.conf

%global archivename SourceHanSansTW

Name:           adobe-source-han-sans-tw-fonts
Version:        2.001
Release:        2%{?dist}
Summary:        Adobe OpenType Pan-CJK font family for Traditional Chinese

License:        OFL
URL:            https://github.com/adobe-fonts/source-han-sans/
Source0:        https://github.com/adobe-fonts/source-han-sans/raw/release/SubsetOTF/%{archivename}.zip
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

Provides:       adobe-source-han-sans-twhk-fonts = %{version}-%{release}
Obsoletes:      adobe-source-han-sans-twhk-fonts < %{version}-%{release}

%description
Source Han Sans is a sans serif Pan-CJK font family 
that is offered in seven weights—ExtraLight, Light, 
Normal, Regular, Medium, Bold, and Heavy—and 
in several OpenType/CFF-based deployment configurations
to accommodate various system requirements or limitations.

As the name suggests, Pan-CJK fonts are intended to
support the characters necessary to render or
display text in Simplified Chinese, Traditional Chinese,
Japanese, and Korean.


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
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.otf
%license LICENSE.txt


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Peng Wu <pwu@redhat.com> - 2.001-1
- Update to 2.001

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Peng Wu <pwu@redhat.com> - 2.000-1
- Update to 2.000

* Fri Jul 20 2018 Akira TAGOH <tagoh@redhat.com> - 1.004-9
- Update the fontconfig priority to ensure this as default for upgrading.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb  1 2018 Peng Wu <pwu@redhat.com> - 1.004-7
- Update the priority to change the default font to Noto

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Peng Wu <pwu@redhat.com> - 1.004-5
- Use Source Han Sans for Mono and Sans
- Use Source Han Serif for Serif

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Peng Wu <pwu@redhat.com> - 1.004-2
- Fixes Obsoletes

* Fri Aug  7 2015 Peng Wu <pwu@redhat.com> - 1.004-1
- Update to 1.004

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Peng Wu <pwu@redhat.com> - 1.002-1
- Update to 1.002

* Mon Apr 13 2015 Peng Wu <pwu@redhat.com> - 1.001-2
- Update spec according to review feedback.

* Mon Mar 30 2015 Peng Wu <pwu@redhat.com> - 1.001-1
- Renamed from adobe-source-han-sans-twhk-fonts

