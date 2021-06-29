%global fontname pcaro-hermit
%global fontconf 69-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.21
Release:        12%{?dist}
Summary:        Hermit monospace fonts

License:        OFL
URL:            https://pcaro.es/p/hermit
Source0:        https://pcaro.es/d/otf-hermit-%{version}.tar.gz
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem


%description
Hermit is a monospace font designed to be clear, pragmatic and very readable.
Its creation has been focused on programming. Every glyph was carefully planned
and calculated, according to defined principles and rules. For this reason,
Hermit is coherent and regular.


%prep
%setup -cq


%build


%install
sed -i "s|\r||g" LICENSE # remove windows encoding of LICENSE file

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.otf


%doc LICENSE


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 31 2014 Ryan Brown <sb@ryansb.com> - 1.21-4
- Respond to Parag An's review bz#1124070
- Change the way DOS line endings are removed

* Thu Jul 31 2014 Ryan Brown <sb@ryansb.com> - 1.21-3
- Respond to Parag An's review bz#1124070
- Add empty %%build section to satisfy rpmlint
- Remove optional Group tag

* Mon Jul 28 2014 Ryan Brown <sb@ryansb.com> - 1.21-2
- Fix rpmlint encoding and spelling errors

* Mon Jul 28 2014 Ryan Brown <sb@ryansb.com> - 1.21-1
- Created package
- Pulled 1.21 source from upstream
