%global fontconf 64-%{fontname}
%global fontname google-roboto-slab
%global commit0 90abd17b4f97671435798b6147b698aa9087612f

Name:          google-roboto-slab-fonts
Version:       1.100263
Release:       0.10.20150923git%{?dist}
Summary:       Google Roboto Slab fonts

License:       ASL 2.0
URL:           https://www.google.com/fonts/specimen/Roboto+Slab
# There are no tar archive so let's pick all the individual source files from github
Source0:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Regular.ttf
Source1:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Bold.ttf
Source2:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Light.ttf
Source3:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Thin.ttf
Source4:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/LICENSE.txt
Source5:       %{fontname}-fontconfig.conf
Source6:       %{fontname}.metainfo.xml
BuildArch:     noarch

BuildRequires: fontpackages-devel

%description
Roboto has a dual nature. It has a mechanical skeleton and the forms are
largely geometric. At the same time, the font features friendly and open
curves. While some grotesks distort their letterforms to force a rigid
rhythm, Roboto doesn't compromise, allowing letters to be settled into
their natural width. This makes for a more natural reading rhythm more
commonly found in humanist and serif types.

This is the Roboto Slab family, which can be used alongside the normal
Roboto family and the Roboto Condensed family.

%prep
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
# nothing to build here

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p RobotoSlab-*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE5} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-fontconfig.conf 

install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE6} %{buildroot}%{_datadir}/appdata

%_font_pkg -f %{fontconf}-fontconfig.conf RobotoSlab-*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%license LICENSE.txt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.10.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.9.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.8.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.7.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.6.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.5.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.4.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.3.20150923git
- Follow https://fedoraproject.org/wiki/Packaging:SourceURL#Commit_Revision

* Wed Sep 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.2.20150923
- Fix metainfo file validation by adding <p> </p>
- use %%license macro

* Wed Sep 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.1.20150923
- Initial package
