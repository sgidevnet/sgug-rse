%global fontname sil-scheherazade
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.100
Release:        9%{?dist}
Summary:        An Arabic script unicode font

License:        OFL
URL:            https://software.sil.org/scheherazade/
Source0:        https://software.sil.org/downloads/r/scheherazade/Scheherazade-%{version}.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Scheherazade, named after the heroine of the classic Arabian Nights tale, is
designed in a similar style to traditional typefaces such as Monotype Naskh,
extended to cover the full Unicode Arabic repertoire.

%prep
%setup -q -n Scheherazade-%{version}


%build
for docfile in *.txt; do
    fold -s $docfile > $docfile.new && \
    sed -i "s|\r||g" $docfile.new && \
    touch -r $docfile $docfile.new && \
    mv $docfile.new $docfile
done

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
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%license OFL.txt
%doc FONTLOG.txt README.txt OFL-FAQ.txt documentation/*
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Akira TAGOH <tagoh@redhat.com> - 2.100-7
- Update URL.
- Modernize the spec file.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 10 2015 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.100-1
- Update to upstream version 2.100

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.020-3
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.020-1
- Update to 2.020 upstream release with bug fixes

* Mon Sep 16 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.010-1
- Update to upstream bugfix release 010

* Sun Aug 18 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.000-1
- Update to version 2.000

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 16 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.005-3
- Fix fontconfig test tag to use 'compare' rather than 'mode' which is the
  correct keyword

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.005-1
- Updated to 1.005 upstream version
- Removed some deprecated entries (like cleaning buildroot)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 01 2010 Hedayat Vatankhah <hedayat@grad.com> - 1.001-3
- Scaled the font (1.2 times bigger) to make it more like other fonts

* Sat Oct 03 2009 Hedayat Vatankhah <hedayat@grad.com> - 1.001-2
- Fixed summary to not include font name
- Removed some parts of the description
- Added fontconfig rules

* Mon Sep 28 2009 Hedayat Vatankhah <hedayat@grad.com> - 1.001-1
- Initial version

