Name:           solar-backgrounds
Version:        0.92.0
Release:        18%{?dist}
Summary:        Solar desktop backgrounds

License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/Artwork/F10Themes/Solar
Source0:        solar-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains desktop backgrounds for the Solar theme.

%package        common
Summary:        Solar desktop backgrounds shared between GNOME and KDE

%description    common
This package includes the common files for the solar-backgrounds-extras and
solar-kde-theme packages.

%package        extras
Summary:        Solar HD desktop backgrounds

Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description    extras
This package includes more resolutions for the Solar theme desktop backgrounds.

%prep
%setup -q -n solar-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
# copy image files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/standard
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/standard.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/wide
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/wide.dual

cp -a -r $RPM_BUILD_DIR/solar-%{version}/standard \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/standard.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar 
cp -a -r $RPM_BUILD_DIR/solar-%{version}/wide \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/wide.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/normalish \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/normalish.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
# copy slideshow xml files
cp -a $RPM_BUILD_DIR/solar-%{version}/solar.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a $RPM_BUILD_DIR/solar-%{version}/solar-hd.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
# copy metadata xmls file
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/solar-%{version}/desktop-backgrounds-solar.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/solar-%{version}/desktop-backgrounds-solar-hd.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties



%files
%doc COPYING
%dir %{_datadir}/backgrounds/solar
%dir %{_datadir}/backgrounds/solar/standard
%dir %{_datadir}/backgrounds/solar/wide
%dir %{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/solar/standard/1600x1200
%{_datadir}/backgrounds/solar/wide/1680x1050
%{_datadir}/backgrounds/solar/solar.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-solar.xml

%files common
%doc COPYING
%dir %{_datadir}/backgrounds/solar/standard
%dir %{_datadir}/backgrounds/solar/wide
%dir %{_datadir}/backgrounds/solar/normalish
%dir %{_datadir}/backgrounds/solar/standard/2048x1536
%dir %{_datadir}/backgrounds/solar/wide/1920x1200
%dir %{_datadir}/backgrounds/solar/normalish/1280x1024
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-0-morn.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-0-morn.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-0-morn.png

%files extras
%doc COPYING
%{_datadir}/backgrounds/solar/standard.dual
%{_datadir}/backgrounds/solar/wide.dual
%{_datadir}/backgrounds/solar/normalish.dual
%{_datadir}/backgrounds/solar/standard/1024x768
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-1-noon.png
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-2-evening.png
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-3-night.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-1-noon.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-2-evening.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-3-night.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-1-noon.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-2-evening.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-3-night.png
%{_datadir}/backgrounds/solar/solar-hd.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-solar-hd.xml


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 01 2010 Martin Sourada <mso@fedoraproject.org> - 0.92.0-4
- Fix directory ownership (rhbz #569423)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 08 2008 Martin Sourada <mso@fedoraproject.org> - 0.92.0-1
- New releases, fixes 1680x1050 wallpapers (rhbz #469779)

* Fri Oct 31 2008 Martin Sourada <mso@fedoraproject.org> - 0.91.1-2
- Move Requires: before %%description for -extras subpackage, koji seem to omit
  those otherwise

* Thu Oct 30 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.91.1-1
- Fix 5:4 to be really 1280x1024, not 1280x1014 (add top 10px from dual version)

* Thu Oct 30 2008 Martin Sourada <mso@fedoraproject.org> - 0.91.0-2
- Bump Release for rebuild

* Thu Oct 30 2008 Martin Sourada <mso@fedoraproject.org> - 0.91.0-1
- Split into basic wallpapers with standard resolution (for Live CD Spins) and
  -extras package with more resolutions

* Tue Oct 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.90.0-2
- Split out a -common so we can symlink the wallpapers we need in the KDE theme
- without having to require all the ones we can't use.

* Wed Oct 15 2008 Martin Sourada <mso@fedoraproject.org> - 0.90.0-1
- New release, adds dual screen wallpapers

* Mon Oct 13 2008 Martin Sourada <mso@fedoraproject.org> - 0.0.2-1
- New release, adds 5:4 wallpapers

* Wed Sep 10 2008 Martin Sourada <mso@fedoraproject.org> - 0.0.1-2
- Use %%{_datadir} instead of %%{_prefix}/share

* Wed Sep 10 2008 Martin Sourada <mso@fedoraproject.org> - 0.0.1-1
- Initial RPM package
