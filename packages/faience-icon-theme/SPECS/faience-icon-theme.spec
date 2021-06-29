%global themes Faience Faience-Azur Faience-Ocre Faience-Claire

Name:           faience-icon-theme
Version:        0.5
Release:        11%{?dist}
Summary:        Faience icon theme

License:        GPLv3
URL:            https://code.google.com/p/faience-theme
Source0:        http://raveit65.fedorapeople.org/Others/Source/%{name}_%{version}.tar.xz

# source0 is re-released and cleaned from icons with copyrighted trademarks
# Therefore we use this script to remove them before shipping it.
# runtime require faenza-icon-theme is also removed from index.theme.
# Invoke this script to generate the faience-icon-theme tarball
Source1:        faience-icon-theme-generate-tarball.sh
BuildArch:      noarch

%description
The faience icon theme include Faience, Faience-Azur,
Faience-Claire and Faience-Ocre theme.
It is cleaned from any nonfree icons.


%prep
%setup -q -n %{name}_%{version}

# unpack the icon tarballs
for theme in %{themes}
do
    tar -zxvf ${theme}.tar.gz &>/dev/null
done

# fix permissions
find . -type d -exec chmod 0755 {} \;
find . -type f -exec chmod 0644 {} \;

# delete icon-cache from source
find -type f -name "icon-theme.cache" -delete -print


%build
# nothing to build


%install
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/icons

cp -ar %{themes} $RPM_BUILD_ROOT%{_datadir}/icons


%post
for theme in %{themes}
do
    touch --no-create %{_datadir}/icons/${theme} &>/dev/null ||:
done


%postun
if [ $1 -eq 0 ] ; then
    for theme in %{themes}
    do
        touch --no-create %{_datadir}/icons/${theme} &>/dev/null
        gtk-update-icon-cache -q %{_datadir}/icons/${theme} &>/dev/null || :
    done
fi


%posttrans
for theme in %{themes}
do
    gtk-update-icon-cache %{_datadir}/icons/${theme} &>/dev/null || :
done


%files
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/icons/Faience/
%{_datadir}/icons/Faience-Azur/
%{_datadir}/icons/Faience-Claire/
%{_datadir}/icons/Faience-Ocre/


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 09 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.5-3
- remove runtime require gnome-icon-theme

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 09 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> 0.5-1
- initial build for fedora
- clean macros
- add gnome-icon-theme as runtime require
- Add time-stamp preserving flags
- remove icon-cache's from source
- add script to generate a tarball without nonfree icons
- filter source
- remove faenza-icon-theme require from index.theme
- add runtime require gnome-icon-theme
- improve install section

