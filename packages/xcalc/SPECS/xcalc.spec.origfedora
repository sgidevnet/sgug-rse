Name:           xcalc
Version:        1.0.6
Release:        10%{?dist}
Summary:        Scientific Calculator X11 Client

License:        MIT
URL:            http://xorg.freedesktop.org
Source0:        http://xorg.freedesktop.org/releases/individual/app/xcalc-%{version}.tar.bz2
Source1:        xcalc.desktop

BuildRequires:  libXaw-devel
BuildRequires:  desktop-file-utils
BuildRequires:  xorg-x11-util-macros
BuildRequires:  libfontenc-devel
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libpng-devel
BuildRequires:  libXfixes-devel

%description
xcalc is a scientific calculator X11 client.

%prep
%setup -q
cp -p %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%if 0%{?el5}
echo 'Encoding=UTF-8' >> xcalc.desktop
%endif
install -d ${RPM_BUILD_ROOT}%{_datadir}/applications
install -p -m 644 xcalc.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/xcalc.desktop

%files
%{_bindir}/xcalc
%{_datadir}/X11/app-defaults/XCalc
%{_datadir}/X11/app-defaults/XCalc-color
%{_datadir}/applications/xcalc.desktop
%{_mandir}/man1/xcalc.1.*
%doc ChangeLog README

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Steve Traylen <steve.traylen@cern.ch> - 1.0.6-1
- New upstream 1.0.6

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Steve Traylen <steve.traylen@cern.ch> - 1.0.5-1
- New upstream 1.0.5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr 3 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0.3-5
- Forgot to add xcalc.desktop to CVS.
* Sat Apr 3 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0.3-4
- Bump release for first official Fedora release.
* Sun Mar 21 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0.3-3
- Use desktop-validate rather than desktop-install.
- Install more with -p.
* Sun Mar 21 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0.3-2
- Cosmetic line removal.
* Fri Mar 19 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0.3-1
- Initial spec for fedora extras

