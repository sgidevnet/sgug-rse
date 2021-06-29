%global appname com.github.cassidyjames.dippi

Name:           dippi
Summary:        Calculate display info like DPI and aspect ratio
Version:        2.7.3
Release:        3%{?dist}
License:        GPLv3

URL:            https://github.com/cassidyjames/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme


%description
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
- Find out if a display is a good choice based on its size and resolution
- Get advice about different densities
- Differentiates between laptops and desktop displays
- Stupid simple: all in a cute li'l window


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.7.3-2
- Rebuild with Meson fix for #1699099

* Sun Apr 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.7.3-1
- Update to version 2.7.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.7.1-1
- Update to version 2.7.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.7.0-1
- Update to version 2.7.0.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.3-2
- Rebuild for granite5 soname bump.

* Sat Apr 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.3-1
- Update to version 2.6.3.

* Wed Apr 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.2-1
- Update to version 2.6.2.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1-1
- Update to version 2.6.1.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.4-1
- Update to version 2.5.4.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.3-1
- Update to version 2.5.3.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1-1
- Update to version 2.5.1.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-1
- Initial package.

