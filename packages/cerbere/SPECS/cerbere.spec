%global appname io.elementary.cerbere

Name:           cerbere
Summary:        Pantheon session watchdog
Version:        2.5.0
Release:        3%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# revert upstream commits that introduced regular SIGSEGV crashes
Patch0:         00-revert-crasher-commits.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.16

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0

Recommends:     gala
Recommends:     plank
Recommends:     wingpanel


%description
Cerbere is a sort of watchdog designed for Pantheon. It monitors a
predefined list of processes (configurable through dconf) and relaunches
them if they end. This is helpful to keep the panel, dock, and wallpaper
running, even if they crash or are killed by another process.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop


%files
%license COPYING
%doc README.md

%{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_libexecdir}/%{appname}

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml


%changelog
* Wed Sep 04 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-3
- Revert upstream commits that introduced SIGSEGV crashes.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-1
- Update to version 2.5.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.2.4-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Update to version 0.2.3.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-11
- Clean up .spec file.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-7
- Make BR on /usr/bin/pkg-config explicit.

* Fri Jan 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-6
- Clean up spec file.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-5
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-4
- Spec file cleanups.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-3
- Validate .desktop file.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-2
- Spec file cosmetics.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-1
- Update to version 0.2.2.

