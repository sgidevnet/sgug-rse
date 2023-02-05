Name:		chocolate-doom
Version:	3.0.1
Release:	3%{?dist}
Summary:	Historically compatible Doom engine
License:	GPLv2+
URL:		http://chocolate-doom.org/
Source0:	http://www.chocolate-doom.org/downloads/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	libsamplerate-devel desktop-file-utils
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_net-devel
# Required by man/docgen
BuildRequires:	%{__python}
#Provides:	bundled(md5-plumb)
Provides:	bundled(sha1-gnupg)

%description
Chocolate Doom is a game engine that aims to accurately reproduce the experience 
of playing vanilla Doom. It is a conservative, historically accurate Doom source 
port, which is compatible with the thousands of mods and levels that were made 
before the Doom source code was released. Rather than flashy new graphics, 
Chocolate Doom's main features are its accurate reproduction of the game as it
was played in the 1990s. 

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install DESTDIR=%{buildroot} \
     iconsdir="%{_datadir}/icons/hicolor/64x64/apps" \
     docdir="%{_pkgdocdir}"
mkdir -p %{buildroot}/%{_bindir}
# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://github.com/chocolate-doom/chocolate-doom/issues/406
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">chocolate-doom.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A clone of the popular DOS game DOOM</summary>
  <description>
    <p>
      Chocolate Doom is an original source port of the popular DOOM game for the PC.
    </p>
    <p>
      It accurately reproduces the playing experience of the original DOOM game
      and is compatible with the numerous mods and levels designed for the original.
    </p>
  </description>
  <url type="homepage">http://chocolate-doom.org/</url>
  <screenshots>
    <screenshot type="default">http://www.chocolate-doom.org/wiki/images/a/a7/Chocolate-doom.png</screenshot>
  </screenshots>
</application>
EOF

desktop-file-validate %{buildroot}/%{_datadir}/applications/chocolate-heretic.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/chocolate-hexen.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/chocolate-strife.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/screensavers/chocolate-doom-screensaver.desktop

%files
%doc %{_docdir}/chocolate*
%{_datadir}/bash-completion
%{_bindir}/chocolate-doom
%{_bindir}/chocolate-server
%{_bindir}/chocolate-doom-setup
%{_bindir}/chocolate-heretic
%{_bindir}/chocolate-heretic-setup
%{_bindir}/chocolate-hexen
%{_bindir}/chocolate-hexen-setup
%{_bindir}/chocolate-strife
%{_bindir}/chocolate-strife-setup
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/chocolate-doom.desktop
%{_datadir}/applications/chocolate-setup.desktop
%{_datadir}/applications/screensavers/chocolate-doom-screensaver.desktop
%{_datadir}/applications/chocolate-heretic.desktop
%{_datadir}/applications/chocolate-hexen.desktop
%{_datadir}/applications/chocolate-strife.desktop
%{_datadir}/icons/hicolor/64x64/apps/chocolate-doom.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-setup.png
%{_mandir}/man5/chocolate-doom.cfg.5.gz
%{_mandir}/man5/chocolate-heretic.cfg.5.gz
%{_mandir}/man5/chocolate-hexen.cfg.5.gz
%{_mandir}/man5/chocolate-strife.cfg.5.gz
%{_mandir}/man5/default.cfg.5.gz
%{_mandir}/man5/heretic.cfg.5.gz
%{_mandir}/man5/hexen.cfg.5.gz
%{_mandir}/man5/strife.cfg.5.gz
%{_mandir}/man6/chocolate-doom.6.gz
%{_mandir}/man6/chocolate-server.6.gz
%{_mandir}/man6/chocolate-setup.6.gz
%{_mandir}/man6/chocolate-doom-setup.6.gz
%{_mandir}/man6/chocolate-heretic-setup.6.gz
%{_mandir}/man6/chocolate-heretic.6.gz
%{_mandir}/man6/chocolate-hexen-setup.6.gz
%{_mandir}/man6/chocolate-hexen.6.gz
%{_mandir}/man6/chocolate-strife-setup.6.gz
%{_mandir}/man6/chocolate-strife.6.gz

%changelog
* Fri Jan 13 2023 Jason Benaim <jkbenaim@gmail.com> - 3.0.1-1
- Update to new upstream release 3.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.0.0-1
- update to new upstream release 3.3.0 fixes rhbz #1543425
- spec cleanup and modernization

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.0-1
- Rebuilt for new upstream release 2.3.0 fixes rhbz #1446935
- Fix Provides replace bundled md5 for sha1 rhbz #1249213

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.2.1-1
- Update to new upstream release 2.2.1 fixes RHBZ #1307376

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Rahul Sundaram <sundaram@fedoraproject.org> - 2.2.0
- update to 2.2.0

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.6.0-10
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.0-7
- Install docs into %%pkgdocdir.
- BR: %%{__python} (Address FTBFS RHBZ #992055).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 20 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-2
- use dist tag and added provides on bundled(md5-plumb) as per review

* Tue Aug 16 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-1
- initial spec 
