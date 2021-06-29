%global fontname source-serif-pro
%global fontconf 63-%{fontname}.conf

Name:           adobe-source-serif-pro-fonts
Version:        3.001
Release:        1%{?dist}
Summary:        A set of OpenType fonts designed to complement Source Sans Pro

License:        OFL
URL:            https://github.com/adobe-fonts/source-serif-pro
Source0:        https://github.com/adobe-fonts/source-serif-pro/archive/%{version}R.tar.gz##/%{name}-%{version}.tar.gz
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Source Serif Pro is a set of OpenType fonts to complement the Source Sans Pro
family.

%prep
%setup -q -n source-serif-pro-%{version}R
sed -i 's/\r//' LICENSE.md

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

%check
appstream-util --nonet validate-relax \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc README.md
%license LICENSE.md

%changelog
* Sat Oct 12 2019 Michael Kuhn <suraia@fedoraproject.org> - 3.001-1
- Update to 3.001

* Sat Jul 27 2019 Michael Kuhn <suraia@fedoraproject.org> - 3.000-1
- Update to 3.000

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.010.1.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Michael Kuhn <suraia@fedoraproject.org> - 2.010.1.010-1
- Update to 2.010 and 1.010

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.007.1.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Michael Kuhn <suraia@fedoraproject.org> - 2.007.1.007-1
- Update to 2.007 and 1.007

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Michael Kuhn <suraia@fedoraproject.org> - 2.000-1
- Update to 2.000

* Tue Aug 30 2016 Michael Kuhn <suraia@fedoraproject.org> - 1.017-2
- Fix AppStream metadata
- Validate AppStream metadata during check

* Tue Jan 26 2016 Michael Kuhn <suraia@fedoraproject.org> - 1.017-1
- Initial package.
