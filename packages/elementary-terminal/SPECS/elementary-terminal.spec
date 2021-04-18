%global srcname terminal
%global appname io.elementary.terminal

Name:           elementary-terminal
Summary:        The terminal of the 21st century
Version:        5.5.2
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# drop upstream tests, which only validate .desktop and appdata files
Patch0:         00-drop-upstream-tests.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.40.0

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
#BuildRequires:  pkgconfig(vte-2.91)

Obsoletes:      pantheon-terminal < 0.4.3-9
Provides:       pantheon-terminal = %{version}-%{release}


%description
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.


%package        fish
Summary:        The terminal of the 21st century (fish support)

BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       fish

Supplements:    (%{name} and fish)

%description    fish
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.

This package contains the files needed to support "process completed"
notifications when using the fish shell.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson -Dubuntu-bionic-patched-vte=false
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/open-pantheon-terminal-here.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml

%files fish
%{_datadir}/fish/vendor_conf.d/pantheon_terminal_process_completion_notifications.fish


%changelog
* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 5.5.2-1
- Update to version 5.5.2.

* Fri Jan 17 2020 Fabio Valentini <decathorpe@gmail.com> - 5.5.1-1
- Update to version 5.5.1.

* Mon Jan 06 2020 Fabio Valentini <decathorpe@gmail.com> - 5.5.0-1
- Update to version 5.5.0.

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.0-1
- Update to version 5.4.0.

* Fri Nov 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6-3
- Drop superfluous dependency on appstream by dropping upstream tests.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.6-1
- Update to version 5.3.6.

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.5-1
- Update to versiojn 5.3.5.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 5.3.4-2
- Rebuild with Meson fix for #1699099

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 5.3.4-1
- Update to version 5.3.4.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.3-1
- Update to version 5.3.3.

* Wed Oct 31 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.2-1
- Update to version 5.3.2.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 5.3.1-1
- Update to version 5.3.1.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-1
- Update to version 0.5.3.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.2-1
- Update to version 0.5.2.
- Fix FTBFS issue with vala 0.42.

* Tue Jul 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.1-1
- Update to version 0.5.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5-1
- Initial package renamed from pantheon-terminal.

