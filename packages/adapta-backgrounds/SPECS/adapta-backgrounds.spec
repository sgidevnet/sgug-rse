Name:           adapta-backgrounds
Version:        0.5.3.1
Release:        8%{?dist}
Summary:        Wallpaper collection for adapta-project

License:        GPLv2 and CC-BY-SA
URL:            https://github.com/adapta-project/adapta-backgrounds
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
Requires:       filesystem
Suggests:       adapta-gtk-theme
Suggests:       papirus-icon-theme

%description
%{summary}.


%prep
%autosetup -p 1


%build
%meson
%meson_build


%install
%meson_install
for f in AUTHORS COPYING LICENSE_CC_BY_SA4 README.md; do
  %{_bindir}/find %{buildroot} -type f -name "$f" -print -delete
done

# We inherit cinnamon-background-properties from Gnome in Fedora and EPEL.
%{__rm} -fr %{buildroot}%{_datadir}/cinnamon-background-properties


%files
%license AUTHORS COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/backgrounds/adapta
%{_datadir}/gnome-background-properties
%{_datadir}/mate-background-properties


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.3.1-7
- Drop unnecessary BR: fdupes

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.3.1-6
- Remove no longer needed BR: libxml-2.0
- Suggests 'adapta-gtk-theme' and 'papirus-icon-theme'

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Björn Esser <besser82@fedoraproject.org> - 0.5.3.1-1
- New upstream release (#1535449)

* Sun Jan 14 2018 Björn Esser <besser82@fedoraproject.org> - 0.5.2.3-1
- New upstream release (#1534249)

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 0.5.2.2-1
- Initial import (#1529705)

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 0.5.2.2-0.1
- Initial rpm release (#1529705)
