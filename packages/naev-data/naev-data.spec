Name:           naev-data
Version:        0.7.0
Release:        9%{?dist}
Summary:        Data files for NAEV
License:        GPLv3 or GPLv3+ or GPLv2+ or Public Domain or CC-BY or CC-BY-SA
URL:            http://naev.org
Source1:        http://sourceforge.net/projects/naev/files/naev-%{version}/naev-%{version}-ndata.zip
Requires:       %{name} = %{version}
BuildArch:      noarch

%description
NAEV is a 2D space trading and combat game, in a similar vein to Escape
Velocity.

NAEV is played from a top-down perspective, featuring fast-paced combat, many
ships, a large variety of equipment and a large galaxy to explore. The game is
highly open-ended, letting you proceed at your own pace.

This package contains the data files needed to play the game

%install
mkdir -p %{buildroot}%{_datadir}/naev
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/naev/ndata-%{version}.zip

%files
%{_datadir}/naev

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Jonathan Dieter <jdieter@gmail.com> - 0.7.0-6
- Remove obsolete Group tag

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Jonathan Dieter <jdieter@lesbg.com> - 0.7.0-3
- Build again because koji put 0.7.0-1 in the repository after 0.7.0-2

* Sat Jul 15 2017 Jonathan Dieter <jdieter@lesbg.com> - 0.7.0-2
- Update to new version with new missions
- Fix ndata location

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Jonathan Dieter <jdieter@lesbg.com> - 0.6.1-1
- Update to 0.6.1 with improved AI and new missions
 
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Jonathan Dieter <jdieter@lesbg.com> - 0.6.0-1
- Update to 0.6.0 which includes:
   + Greatly expanded galaxy
   + New missions
   + Hidden jumps
 
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Jonathan Dieter <jdieter@lesbg.com> - 0.5.3-8
- Attempt another rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.5.3-1
- Update to 0.5.3 - with new missions and bugfixes

* Fri Mar  2 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.5.1-1
- Update to 0.5.1 - with new missions, a new faction and other improvements 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-4
- Add dist tag

* Tue Jun 28 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-3
- Fix license
- Remove unneeded defattr

* Mon Jun 27 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-2
- Spec file cleanup

* Sun Jun  5 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-1
- Convert openSUSE Build Service RPM to Fedora RPM
- Split data into separate source rpm

* Wed Jun  9 2010 dbuck <noone@example.com> - 0.4.2-1
- initial build
