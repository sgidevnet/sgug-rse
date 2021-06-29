%global fontname glyphicons-halflings
%global githash 728067b586d2d989c07e8a6265f06fa8631c6b1f
%global gitshort 728067b
%global date 20140211
%global checkout %{date}git%{gitshort}

Name:           %{fontname}-fonts
Epoch:          1
Version:        3.1.0
Release:        11.%{checkout}%{?dist}
Summary:        Precisely prepared monochromatic icons and symbols

License:        MIT
URL:            http://glyphicons.com/

Source0:        https://github.com/twbs/bootstrap/raw/%{githash}/fonts/glyphicons-halflings-regular.ttf
Source1:        https://github.com/twbs/bootstrap/raw/%{githash}/LICENSE
BuildArch:      noarch
BuildRequires:  fontpackages-devel 
BuildRequires:  ttembed
Requires:       fontpackages-filesystem

%description
GLYPHICONS is a library of precisely prepared monochromatic icons and symbols,
created with an emphasis on simplicity and easy orientation.

%prep
ttembed %{SOURCE0}
install -m 0644 -p %{SOURCE1} LICENSE

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}


%files
%doc LICENSE
%{_fontdir}


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-11.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-10.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-9.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-8.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-7.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-6.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-5.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.1.0-4.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.1.0-3.20140211git728067b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Pete Travis <immanetize@fedoraproject.org> 1-3.1.0-2.20140211git728067b.1
- Correcting ENVR and adding dist macro to fix packaging flub.

* Tue Feb 11 2014 Pete Travis <immanetize@fedoraproject.org> 3.1.0-20140211git728067b.1
- Use git snapshot in release, to track changes in font vs project that provides it.
- Remove unacceptable font formats.
- Set embeddable permissions on glyphicons-halflings-regular.ttf to "installable".

* Thu Jan  9 2014 Pete Travis <immanetize@fedoraproject.org> 3.0.3-1
- Initial packaging.
