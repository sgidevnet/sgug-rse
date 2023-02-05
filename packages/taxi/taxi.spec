%global appname com.github.alecaddd.%{name}

Name:           taxi
Version:        0.0.1
Release:        2%{?dist}
Summary:        The FTP Client that drives you anywhere

License:        GPLv3+
URL:            https://github.com/Alecaddd/taxi
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
Requires:       hicolor-icon-theme

%description
Taxi is a native Linux FTP client built in Vala and Gtk originally created by
Kiran John Hampal. It allows you to connect to a remote server with various
Protocols (FTP, SFT, etc.), and offers an handy double paned interface to
quickly transfer files and folders between your computer and the server.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appname}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files -f %{appname}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.appdata.xml

%changelog
* Thu Aug 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.1-2
- Initial package
