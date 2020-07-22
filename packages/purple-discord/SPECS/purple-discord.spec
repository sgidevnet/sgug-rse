%global plugin_name discord

%global commit0 11744587f65fc7afb679cc7c0c06b116a40fca5c
%global shortcommit0 %(c=%{commit0}; echo $c |cut -c 1-7)
%global date 20200512

Name: purple-%{plugin_name}
Version: 0
Release: 28.%{date}git%{shortcommit0}.1%{?dist}
Summary: Discord plugin for libpurple

License: GPLv3+
URL: https://github.com/EionRobb/%{name}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# For now can be found in the 0.0.6prerelease area
Source1: %{name}-images.tar.gz

Patch100: purple-discord.irixfixes.patch

BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: gettext-devel
# We don't use imagemagick to generate the pngs, they are in a tarball.
#BuildRequires: ImageMagick
BuildRequires: zlib-devel
BuildRequires: gcc

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Discord protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Discord to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Discord protocol implemented by
purple-discord.

%prep
%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
%set_build_flags
%make_build
tar xf %{SOURCE1}

%install
%make_install
%find_lang %{name}

# Push in the PNG files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/pidgin/protocols/16
cp discord16.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/pidgin/protocols/16/discord.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/pidgin/protocols/22
cp discord22.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/pidgin/protocols/22/discord.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/pidgin/protocols/48
cp discord48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/pidgin/protocols/48/discord.png

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_libdir}/purple-2/lib%{plugin_name}.so

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Wed Jul 22 2020 Daniel Hams <daniel.hams@gmail.com> - 0-28.20200512git1174458.1
- Include images by tarball

* Tue Jul 21 2020 Eric Dodd <eric.e.dodd@gmail.com> - 0-28.20200512git1174458
- sgug 0.0.6 prerelease.

* Wed May 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-28.20200512git1174458
- Updated to latest snapshot.

* Tue Apr 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-27.20200405gitdb7dc79
- Updated to latest snapshot.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20190805git250a8a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-25.20190805git250a8a0
- Updated to latest snapshot.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.20190505git8623ec7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-23.20190505git8623ec7
- Updated to latest snapshot.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.20181108gita5dd44f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-21.20181108gita5dd44f
- Updated to latest snapshot.

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-20.20180628git84fe764
- Updated to latest snapshot.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20180515gitb895521
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-18.20180515gitb895521
- Updated to latest snapshot.

* Wed Apr 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-17.20180401git4bea5d7
- Updated to latest snapshot.

* Wed Jan 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-15.20171227git9b7c3ad
- Updated to latest snapshot.

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-14.20171124gita5a41bb
- Updated to latest snapshot.

* Wed Nov 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-13.20171010git2ca7b3c
- Updated to latest snapshot.

* Sat Sep 09 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-12.20170904gitcb53020
- Updated to latest snapshot.

* Tue Aug 29 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-11.20170829git9115bd2
- Updated to latest snapshot.

* Mon Aug 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-10.20170823git4397461
- Updated to latest snapshot.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20170608git5263aff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20170608git5263aff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-7.20170608git5263aff
- Updated to latest snapshot.

* Thu May 25 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-6.20170525gitec1292a
- Updated to latest snapshot.

* Thu May 25 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-5.20170521gitfe92ea6
- Updated to latest snapshot.

* Sat May 06 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20170501git28b1aa4
- Updated to latest snapshot.

* Thu Apr 27 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20170427gitd879f18
- Updated to latest snapshot.

* Wed Apr 26 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20170426gitcca7860
- Updated to latest snapshot.

* Thu Apr 20 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170420git5c2b3ee
- First SPEC release.
