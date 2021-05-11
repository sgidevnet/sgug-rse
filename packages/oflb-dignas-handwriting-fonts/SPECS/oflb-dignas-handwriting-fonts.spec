%global fontname oflb-dignas-handwriting
%global fontconf 63-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20031109
Release:        18%{?dist}
Summary:        Handwriting font

License:        OFL
# Upstream is dead and there is no download link available
URL:            http://openfontlibrary.org/media/files/phranzysko/407
Source0:        http://openfontlibrary.org/people/phranzysko/phranzysko_-_Digna_s_Handwriting.ttf 
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Phranzysko's sister handwriting.


%prep
%setup -q -c -T
cp %{SOURCE0} .


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
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20031109-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20031109-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20031109-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Andrea Musuruane <musuruan@gmail.com> - 20031109-15
- Used new AppData directory
- Spec file clean up

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20031109-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20031109-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20031109-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20031109-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20031109-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 Richard Hughes <richard@hughsie.com> - 20031109-9
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20031109-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20031109-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20031109-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20031109-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20031109-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20031109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 09 2009 Andrea Musuruane <musuruan@gmail.com> 20031109-2
- Changed package name to comply to Font Packaging Guidelines

* Sun Nov 29 2009 Andrea Musuruane <musuruan@gmail.com> 20031109-1
- First release

