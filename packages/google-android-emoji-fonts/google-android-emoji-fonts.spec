%global fontname google-android-emoji
%global checkout 20120228git
%global archivename %{name}-%{checkout}

Name:    %{fontname}-fonts
# No sane versionning upstream, use git clone timestamp
Version: 1.01
Release: 0.14.%{checkout}%{?dist}
Summary: Android Emoji font released by Google

License:   ASL 2.0
URL:       https://android.googlesource.com/platform/frameworks/base.git/+/jb-release/data/fonts/
Source0:   %{archivename}.tar.xz
Source1:   get-source-from-git.sh
Source2:   AndroidEmoji.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
Requires:      fontpackages-filesystem


%description
The Android Emoji typeface contains a number of pictographs and smileys,
popularly used in instant messages and chat forums.  The style of the
typeface is playful.  It is taken from Google's Android Jelly Bean
mobile phone operating system.

This font hasn’t been updated since 2012.  You may well be better served
by its replacement, google-noto-emoji-fonts.


%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p AndroidEmoji.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/metainfo


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/AndroidEmoji.metainfo.xml


%_font_pkg *.ttf
%doc README.txt NOTICE
%{_datadir}/metainfo/AndroidEmoji.metainfo.xml


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-0.14.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-0.13.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-0.12.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 27 2018 Peter Oliver <rpm@mavit.org.uk> - 1.01-0.11.20120228git
- Nudge users towards google-noto-emoji-fonts in description.

* Tue Feb 20 2018 Peter Oliver <rpm@mavit.org.uk> - 1.01-0.10.20120228git
- Validate metainfo.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-0.9.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Peter Oliver <rpm@mavit.org.uk> - 1.01-0.9.20120228git
- Improve AppData metadata.

* Thu Nov 16 2017 Peter Oliver <rpm@mavit.org.uk> - 1.01-0.8.20120228git%{?dist}
- Add a screenshot to the AppData.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-0.7.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-0.6.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-0.5.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-0.4.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Peter Oliver <rpm@mavit.org.uk> - 1.01-0.2.20120228git
- Include AppData, so that this font is included in Gnome Software.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-0.2.20120228git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan  7 2014 Peter Oliver <rpm@mavit.org.uk> - 1.01-0.1.20120228git
- New package, based on google-droid-fonts-20120715-6.
