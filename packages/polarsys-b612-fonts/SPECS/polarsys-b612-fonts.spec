%global forgeurl https://github.com/polarsys/b612/
Version: 1.008
%global tag %{version}
%global fontname polarsys-b612
%global fontconf 64-%{fontname}

%global common_desc \
Commissioned by Airbus and designed by Intactile Design, B612 is a \
digital font intended to be used in an aeronautical context. B612 is \
built with legibility as its core: every character is designed to be \
highly recognizable even in critical reading conditions. B612 drawing \
has been optimized for screen display, and full hinting has been added \
to all sizes of alpha numeric characters.

%forgemeta

Name:           %{fontname}-fonts
Release:        2%{?dist}
Summary:        A typeface designed for reading comfort and safety in aeroplane cockpits

# README.md explains, "This program and the accompanying materials are
# made available under the terms of the Eclipse Public License v1.0 and
# Eclipse Distribution License v1.0 and the SIL Open Font License v1.1
# which accompanies this distribution."
License:        EPL and BSD and OFL

URL:            https://www.polarsys.org/projects/polarsys.b612
Source0:        %{forgesource}
Source1:        %{fontname}-sans.conf
Source2:        %{fontname}-mono.conf
Source3:        %{fontname}-sans.metainfo.xml
Source4:        %{fontname}-mono.metainfo.xml
Source5:        https://www.eclipse.org/legal/epl-v10.html

BuildArch:      noarch
BuildRequires:  fontpackages-devel


%description
%common_desc



%package common
Summary:        Common files of B612
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%files common
%doc README.md
%doc edl-v10.html
%doc epl-v10.html
%doc OFL.txt



%package doc
Summary:        Documentation for B612

%description doc
%common_desc

This package contains a leaflet explaining the design and production of
the fonts.


%files doc
%doc docs/B612-Leaflet.pdf



%package -n %{fontname}-sans-fonts
Summary:        Sans-serif fonts designed for reading comfort and safety in aeroplane cockpits

Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This packages contains a sans serif font family.


%_font_pkg -n sans -f %{fontconf}-sans.conf B612-*.ttf
%{_datadir}/metainfo/org.polarsys.B612-sans.metainfo.xml



%package -n %{fontname}-mono-fonts
Summary:        Monospace fonts designed for reading comfort and safety in aeroplane cockpits
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-mono-fonts
%common_desc

This packages contains a monospace font family.


%_font_pkg -n mono -f %{fontconf}-mono.conf B612Mono-*.ttf
%{_datadir}/metainfo/org.polarsys.B612-mono.metainfo.xml



%prep
%forgesetup

install -m 0644 -p %{SOURCE5} .


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir} \
                   %{buildroot}%{_datadir}/metainfo

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

for fconf in %{fontconf}-sans.conf \
             %{fontconf}-mono.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/metainfo/org.polarsys.B612-sans.metainfo.xml
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/metainfo/org.polarsys.B612-mono.metainfo.xml


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Peter Oliver <rpm@mavit.org.uk> - 1.008-1
- Update to version 1.008.
- Latest source is now at GitHub rather than PolarSys's own git repository.
- Additional licence, SIL Open Font License, Version 1.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-5.20171129gitbd14fde
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov  8 2018 Peter Oliver <rpm@mavit.org.uk> - 1.003-4.20171129gitbd14fde
- Drop unneeded BuildRequires.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-3.20171129gitbd14fde
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-2.20171129gitbd14fde
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec  7 2017 Peter Oliver <rpm@mavit.org.uk> - 1.003-1.20171129gitbd14fde
- Update to version 1.003.
- Split leaflet out into a separate doc subpackage.

* Fri Nov 10 2017 Peter Oliver <rpm@mavit.org.uk> - 1.002-3.20170320gitf4ce1fd
- Remove obsolete sections.

* Fri Nov  3 2017 Peter Oliver <rpm@mavit.org.uk> - 1.002-2.20170320gitf4ce1fd
- Use auto-generated source snapshot.
- Remove obsolete sections.

* Fri Nov  3 2017 Peter Oliver <rpm@mavit.org.uk> - 1.002-1.20170320gitf4ce1fd
- Initial package.
