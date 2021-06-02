# FIXME: Before package was based on openSUSE package. Now it uses Debian package. Also there is git repo
# https://github.com/ganwell/dmz-cursors with high-resolution sizes. May be this is the best option?

Name:           dmz-cursor-themes
Version:        0.4.5
Release:        3%{?dist}
Summary:        Style neutral cursors themes
License:        CC-BY-SA
URL:            https://packages.debian.org/sid/gnome/dmz-cursor-theme
Source0:        http://ftp.debian.org/debian/pool/main/d/dmz-cursor-theme/dmz-cursor-theme_%{version}.tar.xz
Patch0:         dmz-cursor-themes-symbolic-links.patch
BuildArch:      noarch
BuildRequires:  xcursorgen

%description
Scalable, style-neutral cursor themes based on the Industrial cursors designed
by Jakub Steiner for the Ximian GNOME Desktop.

%prep
%autosetup -p1 -n dmz-cursor-theme-%{version}

%build
for color in White Black; do
    cd %{_builddir}/dmz-cursor-theme-%{version}/DMZ-$color/pngs
    ./make.sh
done

%install
for color in White Black; do
    install -d %{buildroot}%{_datadir}/icons/DMZ-$color/cursors
    install -m644 DMZ-$color/cursor.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/index.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/xcursors/* -t %{buildroot}%{_datadir}/icons/DMZ-$color/cursors/
done

%files
%doc debian/copyright
%{_datadir}/icons/DMZ-White/
%{_datadir}/icons/DMZ-Black/

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Ivan Romanov <drizt72@zoho.eu> - 0.4.5-2
- Fix grab pointer
- Add dmz-cursor-themes-symbolic-links.patch

* Mon May 13 2019 Ivan Romanov <drizt72@zoho.eu> - 0.4.5-1
- Update to v0.4.5 based on Debian package. Thanks to Link Dupont.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 04 2010 Benjamin Otte <otte@redhat.com> 0.4-3
- Update to new snapshot
- Change to new license CC-BY-SA

* Tue Feb 16 2010 Benjamin Otte <otte@redhat.com> 0.4-2
- Correct source download information

* Mon Feb 15 2010 Benjamin Otte <otte@redhat.com> 0.4-1
- Initial packaging
