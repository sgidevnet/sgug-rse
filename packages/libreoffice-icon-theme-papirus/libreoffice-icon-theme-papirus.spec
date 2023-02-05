%global upstream_name   papirus-libreoffice-theme

Name:           libreoffice-icon-theme-papirus
Version:        20170228
Release:        3%{?dist}
Summary:        Papirus theme for LibreOffice

License:        GPLv3
URL:            https://github.com/PapirusDevelopmentTeam/papirus-libreoffice-theme
Source0:        %url/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Papirus theme for LibreOffice.

It is available in three variants:

 - ePapirus
 - Papirus
 - Papirus Dark


%prep
%autosetup -n %{upstream_name}-%{version}


%build
# Nothing to build


%install
%make_install PREFIX=%{_libdir}


%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_libdir}/libreoffice
%dir %{_libdir}/libreoffice/share
%dir %{_libdir}/libreoffice/share/config
%{_libdir}/libreoffice/share/config/images_*.zip


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170228-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170228-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 20170228-1
- Initial release
