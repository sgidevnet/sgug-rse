%global fontname kanotf
%global fontconf 65-%{fontname}.conf
%global _subdir /fonts

Name:           %{fontname}-fonts
Version:        20050515
Release:        14%{?dist}
Summary:        OpenType Kannada fonts
License:        GPLv2
URL:            http://sourceforge.net/projects/brahmi/
Source0:        http://sourceforge.net/projects/brahmi/files/Brahmi%20OpenType%20Fonts/OpenType%20font%20for%20Kannada%20-%20Kedgae%20and%20Mallige%20Ver%201.0/kanotf.zip
Source1:        %{name}-fontconfig.conf
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Consists of two Kannada open-type fonts named "Kedage" and "Mallige". 

%define debug_package %{nil}

%prep
%setup -q -n %{fontname}%{_subdir}
sed -i 's/\r//' ../readme.txt
%build

%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.TTF %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}



%_font_pkg -f %{fontconf} *.TTF



%doc ../readme.txt ../gpl.txt

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20050515-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20050515-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20050515-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20050515-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050515-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050515-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20050515-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050515-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050515-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050515-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050515-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050515-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Feb 27 2011 Susmit Shannigrahi <susmit at fedoraproject.org> - 20050515-1%{?dist}
- Changing version format. Upstream does not provide consistent version number.
- Corrected wrong-file-end-of-line-encoding.
* Thu Nov 12 2010 Susmit Shannigrahi <susmit at fedoraproject.org> - 1.0-1
- Initial Packaging

