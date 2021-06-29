%global commit0 722c52e819e98ed8b88a26f9891d4b6b0983bcb7
%global date0   20160804

Name:           apx
Version:        0.1
Release:        22.%{date0}git%{?dist}
Summary:        QIX clone, cut into and claim the square area

License:        MIT
URL:            https://github.com/tstriker/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel python3-setuptools
BuildRequires:  fontpackages-devel
BuildRequires:  desktop-file-utils libappstream-glib

Requires:       python3

Requires:       hicolor-icon-theme

# need introspection for cairo
Requires:       python3-gobject
Requires:       python3-cairo

Requires:       %{name}-fonts = %{version}-%{release}

%description
APX is a QIX clone with minor differences in game-play from the original.
Read about the original: http://en.wikipedia.org/wiki/Qix

Use arrow keys to move around the perimeter of square, hold down Space or Shift
to cut into the area. Connect back to perimeter to claim the area.

Your objective is to claim 75 percent or more to proceed to the next level.

Claiming with Shift key will be slower but give you double the points.

For every claimed full percent over 75 percent you get extra 1000 points.


%package fonts
Summary:       Fonts for the game %{name}
License:       CC-BY
URL:           http://www.04.jp.org/
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description fonts
Fonts for the game %{name}.
Redistribution from: http://www.04.jp.org


%prep
%autosetup -p1 -n%{name}-%{commit0}
sed -i s,Games,Game, data/*.desktop
# add right shebang
sed -i '1d;2i#!%{__python3}' bin/%{name}
find %{name} -name \*.py |xargs sed -i '/^#!\//, 1d'
# do not try to install the font again and again
sed -i /utils.install_font.*/d bin/%{name}
sed -i -r 's,(fonts/)04b03,\1%{name},' setup.py

%build
sed -i '/"install":/d' setup.py
%py3_build

%install
%py3_install
# avoid misplaced license file
find %{buildroot} -name '*LICENSE' -print -delete

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.sqlite
%{_datadir}/icons/hicolor/scalable/*.svg
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml

%_font_pkg *.ttf
%license data/*_LICENSE


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22.20160804git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Raphael Groner <projects.rg@smart.ms> - 0.1-21.20160804git
- fix build for python 3.8
- condense upstreamed patches

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-18
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1-16
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-13
- Rebuild for Python 3.6

* Sun Jul 31 2016 Raphael Groner <projects.rg@smart.ms> - 0.1-12
- add another patch for python3

* Fri Jul 29 2016 Raphael Groner <projects.rg@smart.ms> - 0.1-11
- add patch: Difficult to see with some desktop themes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 10 2016 Raphael Groner <projects.rg@smart.ms> - 0.1-9
- note new upstream URL

* Sat Jul 09 2016 Raphael Groner <projects.rg@smart.ms> - 0.1-8
- fix crash with python3, rhbz#1347738

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 27 2015 Raphael Groner <projects.rg@smart.ms> - 0.1-6
- fix Requires again

* Sat Dec 26 2015 Raphael Groner <projects.rg@smart.ms> - 0.1-5
- fix b0rken dependencies to cairo
- apply acceptance of upstream 2to3
- apply upstream patch to revert removal of R: hicolor-icon-theme
- comply to fonts packaging policy

* Fri Dec 25 2015 Raphael Groner <projects.rg@smart.ms> - 0.1-4
- apply latest upstream patches
- port to python3
- enable appdata validation
- remove R: hicolor-icons-theme

* Sat Sep 26 2015 Raphael Groner <projects.rg@smart.ms> - 0.1-3
- avoid duplicated but misplaced license file from doc folder

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.7.20150118gite978d95
- first official upstream release v0.1

* Wed Jan 28 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.8.20150118gite978d95
- introduce license macro

* Sun Jan 18 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.7.20150118gite978d95
- new upstream snapshot
- remove obsolete tweaks
- legal fonts subpackage

* Mon Jan 12 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.6.20141101gite7766f1
- R: pycairo without -devel

* Fri Dec 19 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.5.20141102gite7766f1
- require cairo
- honor AUTHORS
- use date of last commit (instead of export/clone)

* Mon Nov 03 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.4.20141102gite7766f1
- proper usage of macro python2_sitelib
- comment about strange location for redistributed font

* Sun Nov 02 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.3.20141102gite7766f1
- new snapshot: license change for font

* Wed Oct 29 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.2.20141010git853fdd0
- fix Requires
- fix description
- preserve timestamps

* Sat Oct 11 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.1.20141010git853fdd0
- initial
