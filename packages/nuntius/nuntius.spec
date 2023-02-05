Name:           nuntius
Version:        0.2.0
Release:        11%{?dist}
Summary:        Get notifications from the phone or tablet

License:        GPLv2+
URL:            https://github.com/holylobster/nuntius-linux
Source0:        https://github.com/holylobster/nuntius-linux/releases/download/v%{version}/nuntius-%{version}.tar.xz
Patch0:         0001-Fix-a-syntax-error-in-desktop-file-keywords-German-t.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  vala-devel

%description
Nuntius is a daemon that connects to another Nuntius app running on a phone or
a tablet and proxies the notifications using Bluetooth.

%prep
%setup -q
%patch0 -p1
rm data/org.holylobster.nuntius.desktop

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%find_lang nuntius

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.holylobster.nuntius.desktop

%files -f nuntius.lang
%license COPYING
%{_sysconfdir}/xdg/autostart/org.holylobster.nuntius.desktop
%{_bindir}/nuntius
%{_datadir}/appdata/org.holylobster.nuntius.appdata.xml
%{_datadir}/applications/org.holylobster.nuntius.desktop
%{_datadir}/dbus-1/services/org.holylobster.nuntius.service
%{_datadir}/icons/hicolor/*/apps/nuntius.png

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Tue Mar 10 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.0-1
- Update to 0.1.0

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.1-2
- Capitalize names in the description (#1197756)

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.1-1
- Initial Fedora packaging
