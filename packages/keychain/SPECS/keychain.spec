Name:		keychain
Summary:	Agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG
Version:	2.8.5
Release:	1%{?dist}
License:	GPLv2
URL:		https://www.funtoo.org/Keychain
Source0:	https://github.com/funtoo/keychain/archive/%{version}/keychain-%{version}.tar.gz
Source1:	keychain.sh
Source2:	keychain.csh
Source3:	README.Fedora
BuildArch:	noarch

# https://bugzilla.redhat.com/show_bug.cgi?id=486025
Conflicts:	kde-settings < 4.2-3
# https://bugzilla.redhat.com/show_bug.cgi?id=314431
Conflicts:	zsh < 4.3.4-7

%description
Keychain is a manager for OpenSSH, ssh.com, Sun SSH and GnuPG agents.
It acts as a front-end to the agents, allowing you to easily have one
long-running agent process per system, rather than per login session.
This dramatically reduces the number of times you need to enter your
passphrase from once per new login session to once every time your
local machine is rebooted.

%prep
%setup -q
sed -i -e 's|/usr/ucb:||' keychain

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 755 keychain %{buildroot}%{_bindir}/keychain
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/keychain.sh
install -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/keychain.csh
install -pm 644 keychain.1 %{buildroot}%{_mandir}/man1
install -pm 644 %{SOURCE3} README.Fedora

%files
%doc COPYING.txt ChangeLog README.md README.Fedora
%config(noreplace) %{_sysconfdir}/profile.d/keychain.sh
%config(noreplace) %{_sysconfdir}/profile.d/keychain.csh
%{_bindir}/keychain
%{_mandir}/man1/keychain.1*

%changelog
* Mon Jun 01 2020 Sérgio Basto <sergio@serjux.com> - 2.8.5-1
- Update to 2.8.5 (#1226492)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 2.8.0-1
- version upgrade (rhbz#531382, rhbz#811365, rhbz#1209473)
- support for newer openssh/gnupg (rhbz#1204340)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  2 2009 Ville Skyttä <ville.skytta at iki.fi> - 2.6.8-6
- Write ~/.gpg-agent-info when launching gpg-agent for better compatibility
  with other things using it, e.g. KDE 4 (#486025).
- Drop no longer needed zsh special case which caused issues with ksh from
  profile.d script (#314431).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Ville Skyttä <ville.skytta at iki.fi> - 2.6.8-4
- Don't override/unset $HOST or $USERHOME in profile.d snippets (#463913).

* Sun Apr  6 2008 Ville Skyttä <ville.skytta at iki.fi> - 2.6.8-3
- Make profile.d sh snippet check if it has already run (skip if yes),
  and avoid polluting the shell with its internal variables.
- License: GPLv2.
- Update URLs.

* Sat Nov 04 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 2.6.8-2
- Fix #212190.

* Sat Nov 04 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 2.6.8-1
- Update to 2.6.8.

* Fri Sep 01 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 2.6.2-1
- Update to 2.6.2.

* Tue Aug 29 2006 Alexander Dalloz <alex {%} dalloz {*} de> - 2.6.1-2
- Rebuild for FC6.

* Sat Nov 26 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.6.1-1
- Update to 2.6.1.
- Invoke keychain with --noask in opt-in scripts in non-interactive shells
  to fix scp'ing to an opt-in enabled account for which keychain hasn't run.
- Make opt-in config work the same way with zsh as with other shells.
- Replace tweaks in manpage patch with more generic instructions.
- Make profile.d snippets non-executable (#35714).
- Preserve timestamps of installed files, other cosmetics.

* Tue Aug 16 2005  Alexander Dalloz <alex {%} dalloz {*} de> - 2.5.5-2
- Added test for homedir mismatch in opt-in scripts, covering
  `sudo -s' (reported by Ville Skyttä).

* Fri Aug 05 2005  Alexander Dalloz <alex {%} dalloz {*} de> - 2.5.5-1
- Updated to new upstream version
- Removed keychain.pod from %%doc.

* Wed Jul 27 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 2.5.4.1-2
- Added manpage patch and %%prep removal of non existing path
  (thanks Ville Skyttä)
- Added opt-in mechanism through profile.d scripts for all
  login shells Fedora ships.

* Sun Jul 10 2005 Alexander Dalloz <alex {%} dalloz {*} de> - 2.5.4.1-1
- Initial build, based on upstream .spec by Aron Griffis.
