Name:           tunneler
Version:        1.1.1
Release:        25%{?dist}
Summary:        Clone of legendary Tunneler game

License:        GPLv2+
URL:            http://users.jyu.fi/~tvkalvas/code/tunneler/
Source0:        http://users.jyu.fi/~tvkalvas/code/tunneler/%{name}-%{version}.tar.gz
Source1:        tunneler.svg
Source2:        tunneler.desktop
Patch0:         tunneler-1.1.1-lm.patch
Patch1:         tunneler-1.1.1-inline.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  SDL-devel
BuildRequires:  autoconf automake

%description
A clone of legendary game made by Geoffrey Silverton in 1991. In the game
two players using the same keyboard and the same screen each control an
underground tank. Goal is to find and destroy the opponent's tank. Since
only small part of the map is displayed on the split screen, you might
actually have some searching to do.


%prep
%autosetup -p1


%build
autoreconf -i
%configure
%make_build


%install
%make_install
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 -p %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install %{SOURCE2} \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rheld} < 7)
        --vendor=fedora \
%endif
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications

%files
%{_bindir}/tunneler
%{_datadir}/icons/hicolor/scalable/apps/tunneler.svg
%{_datadir}/applications/*.desktop
%doc INSTALL README
%license COPYING


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.1-24
- Fix FTBFS + spec cleanup rhbz#1606590 and rhbz#1676166

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.1.1-13
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.1-11
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.1.1-6
- Fix build

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Lubomir Rintel <lkundrak@v3.sk> 1.1.1-3
- Picking an even better menu category

* Fri Feb 13 2009 Lubomir Rintel <lkundrak@v3.sk> 1.1.1-2
- Fix the menu category

* Tue Jan 20 2009 Lubomir Rintel <lkundrak@v3.sk> 1.1.1-1
- Initial packaging
