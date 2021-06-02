%global fontname cdac-sakal-marathi
%global fontconf 68-%{fontname}.conf

Name:        %{fontname}-fonts
Version:     9.21
Release:     12%{?dist}
Summary:     Marathi language font from CDAC

License:     OFL
URL:         http://sakalmarathi.cdac.in/
Source0:     http://sakalmarathi.cdac.in/fr/svnapi/svndata/download/binary/Sakal_Marathi_N_Ship.TTF
#http://sakalmarathi.cdac.in/fr/licences.php
Source1:     LICENSE
Source2:     %{fontconf}
BuildArch:   noarch
BuildRequires: fontpackages-devel
Requires: fontpackages-filesystem

%description 
Open type font for Marathi language released by CDAC.

%prep
%setup -q -T -c 
cp -p %{SOURCE1} .

%build
# nothing to build here

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.TTF
%doc LICENSE



%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Pravin Satpute <psatpute@redhat.com> - 9.21-3
- Improved summary

* Thu Nov 28 2013 Pravin Satpute <psatpute@redhat.com> - 9.21-2
- Removed echo from build
- Improved summary

* Mon Nov 18 2013 Pravin Satpute <psatpute@redhat.com> - 9.21-1
- Initial build
