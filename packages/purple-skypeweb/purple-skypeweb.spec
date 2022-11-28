%global plugin_name skypeweb

%global commit0 5d29285f0f845ece94dc012371605a7f353b5d0c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20190520

Name: purple-%{plugin_name}
Version: 1.5
Release: 6.%{date}git%{shortcommit0}%{?dist}
Summary: Adds support for Skype to Pidgin

License: GPLv3
URL: https://github.com/EionRobb/skype4pidgin
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: gcc

Provides: skype4pidgin = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: skype4pidgin < %{?epoch:%{epoch}:}%{version}-%{release}

%description
Adds support for Skype to Pidgin, Adium, Finch and other libpurple 
based messengers.

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Skype protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Skype protocol implemented by libskypeweb.

%prep
%autosetup -n skype4pidgin-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," %{plugin_name}/README.md

%build
%set_build_flags
%make_build -C %{plugin_name}

%install
%make_install -C %{plugin_name}

%files
%doc %{plugin_name}/README.md
%license %{plugin_name}/gpl3.txt
%{_libdir}/purple-2/lib%{plugin_name}.so

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/skype*.png
%{_datadir}/pixmaps/pidgin/emotes/skype

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6.20190520git5d29285
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-5.20190520git5d29285
- Updated to latest snapshot.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4.20180720git2290013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-3.20180720git2290013
- Updated to latest snapshot.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2.20180525gitcf65095
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-1.20180525gitcf65095
- Updated to version 1.5.

* Wed Apr 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-9.20180315gitc395028
- Updated to latest snapshot.

* Sat Feb 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-8.20180215git9db6c43
- Updated to latest snapshot.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7.20171024gitc442007
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-6.20171024gitc442007
- Updated to latest snapshot.

* Sat Sep 09 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-5.20170907git0a276c2
- Updated to latest snapshot.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4.20170615git4ed9b14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3.20170615git4ed9b14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-2.20170615git4ed9b14
- Updated to latest snapshot.

* Sun Apr 30 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-1.20170430gita2c5b71
- Updated to version 1.4.

* Fri Apr 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-3.20170420git31222f4
- Fixed script-without-shebang rpmlint error.

* Fri Apr 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-2.20170420git31222f4
- Updated to latest snapshot.

* Thu Mar 30 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-1.20170330git35624c3
- Updated to version 1.3.

* Wed Mar 29 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-11.20170329gitfc3d6f3
- Updated to latest snapshot.

* Mon Mar 27 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-10.20170327git49cd9cf
- Updated to latest snapshot.

* Sun Mar 26 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-9.20170326gita051aa0
- Updated to latest snapshot.

* Sat Mar 11 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-8.20170226git19ba66e
- Updated to latest snapshot.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7.20161220gitfa888e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-6.20161220gitfa888e0
- Updated to latest snapshot.

* Tue Nov 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-5.20161122git92c376f
- Updated to latest snapshot.

* Thu Oct 27 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-4.20161027git3208958
- Updated to latest snapshot.

* Sun Oct 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-3.20161015gitd23eab9
- Fixed typo in changelog section. Fixed warning.

* Sun Oct 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-2.20161015gitd23eab9
- Added patch to support correct build flags.

* Sun Oct 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-1.20161015gitd23eab9
- Updated to version 1.2.2.

* Mon Aug 08 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.1-1.20160808gitf477d9e
- Updated to version 1.2.1.

* Thu Jul 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2-2.20160720git2b42d11
- Updated to latest Git snapshot.

* Thu Jul 14 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2-1.20160714git41cd230
- Updated to version 1.2.

* Tue Jun 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-11.20160620git72f0b00
- Added missing LDFLAGS to build.

* Mon Jun 20 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-10.20160620git72f0b00
- Updated to latest Git snapshot.

* Wed Jun 15 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-9.20160510giteb0b500
- Updated script generate-tarball.sh (written by Simone Caronni).

* Tue Jun 14 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-8.20160510giteb0b500
- Added script generate-tarball.sh which can be used to remove legacy sources from tarball.

* Mon Jun 13 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-7.20160510giteb0b500
- Fixed directory ownership. Removed patch.

* Sun Jun 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-6.20160510giteb0b500
- Removed empty configure script. Now obsoletes skype4pidgin package.

* Sun Jun 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-5.20160510giteb0b500
- Updated to latest Git version.

* Mon May 02 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-4.20160420gitf23913d
- Updated to latest Git version.

* Fri Mar 04 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-3.20160226git80368db
- Updated to latest Git version.

* Tue Feb 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-2.20160214git04312d8
- Updated to latest Git version. Added EPEL7 support.

* Thu Jan 07 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-1.20160107git9764e31
- Updated to version 1.1: added support of file transfers, fixed Live logins, fixed other crashes.

* Sat Jan 02 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-4.20160101git68cb5f3
- Updated to latest version: added support for receiving server-backed files. Added patch.

* Fri Dec 25 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-3.20151225gita173efa
- Updated to latest version: fixed plugin crash.

* Thu Nov 26 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-2
- Applyed Maxim Orlov's fixes.

* Sun Nov 08 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Updated to version 1.0.

* Mon Aug 24 2015 jparvela <jparvela@gmail.com> - 0.1-4
- Added missing files to spec file list.

* Mon Aug 03 2015 BOPOHA <vorona.tolik@gmail.com> - 0.1-3
- Fixed build with OBS. RPMS can be built from main tarball.

* Sat May 09 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1-2
- Separated packages. Now can be used with other libpurple-based clients without Pidgin being installed.

* Mon Mar 16 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1-1
- Created first RPM spec for Fedora/openSUSE.
