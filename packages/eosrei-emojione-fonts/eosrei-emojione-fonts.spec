%global fontname eosrei-emojione

Name:           %{fontname}-fonts
Version:        1.0
Release:        9%{?dist}
Summary:        A color emoji font

# Note, the link below is the last "Android" build of the EmijoOne font
# with CC-BY-4.0 assets. Do not update to a newer version.
#
# As per https://github.com/emojione/emojione/blob/master/README.md :
# EmojiOne version 2 assets (all SVG and PNG) are available in the 2.2.7
# branch, and they remain available for digital use (with attribution)
# under the Creative Commons license.
#
# This package should eventually be replaced by a build of this font:
# https://github.com/EmojiTwo/emojitwo
License:        CC-BY
URL:            https://github.com/eosrei/emojione-color-font
# From https://github.com/emojione/emojione/blob/693a9705f60efd566e40a5c9ec00ca306c9bcbd0/extras/fonts/emojione-android.ttf
Source0:        emojione-android.ttf
Source1:        https://github.com/eosrei/emojione-color-font/raw/master/LICENSE-CC-BY.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
A color and B&W emoji font built primarily from Emoji One artwork with
support for ZWJ, skin tone modifiers and country flags.

Regular B&W outline emoji are included for backwards/fallback compatibility.

It was created by Brad Erickson.

%prep
%setup -q -T -c

%build
cp -a %{SOURCE1} .

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}/

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg emojione-android.ttf
%doc LICENSE-CC-BY.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Bastien Nocera <bnocera@redhat.com> - 1.0-5
- Add appstream metadata

* Thu Aug 31 2017 Bastien Nocera <bnocera@redhat.com> - 1.0-4
- Add license file that applies to the font we're shipping
  (no code, or Power symbols in this version of the font)
- Use approved license shortname (with the version number)

* Wed Aug 30 2017 Bastien Nocera <bnocera@redhat.com> - 1.0-3
- Remove ".conf" file, the same information will be in fontconfig > 2.12.4

* Fri Jun 30 2017 Bastien Nocera <bnocera@redhat.com> - 1.0-2
- Update to latest android build of the font with the same CC-BY-4.0 license
- Add link to potential successor

* Mon Apr 11 2016 Bastien Nocera <hadess@hadess.net> - 1.0-1
- Initial package
