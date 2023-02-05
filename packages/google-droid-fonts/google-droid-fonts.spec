%global fontname google-droid
%global archivename %{name}-%{version}

%global common_desc \
The Droid typeface family was designed in the fall of 2006 by Ascender's \
Steve Matteson, as a commission from Google to create a set of system fonts \
for its Android platform. The goal was to provide optimal quality and comfort \
on a mobile handset when rendered in application menus, web browsers and for \
other screen text. \
The family was later extended in collaboration with other designers such as \
Pascal Zoghbi of 29ArabicLetters.

Name:    %{fontname}-fonts
# No sane versionning upstream, use git clone timestamp
Version: 20120715
Release: 16%{?dist}
Summary: General-purpose fonts released by Google as part of Android

License:   ASL 2.0
URL:       https://android.googlesource.com/
Source0:   %{archivename}.tar.xz
#Brutal script used to pull sources from upstream git
Source1:   getdroid.sh
Source10:  %{name}-sans-fontconfig.conf
Source11:  %{name}-sans-mono-fontconfig.conf
Source12:  %{name}-serif-fontconfig.conf
Source13:  %{name}-kufi-fontconfig.conf
Source14:  %{fontname}-sans.metainfo.xml
Source15:  %{fontname}-sans-mono.metainfo.xml
Source16:  %{fontname}-serif.metainfo.xml
Source17:  %{fontname}-kufi.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc


%package -n %{fontname}-sans-fonts
Summary:   A humanist sans serif typeface
Requires:  fontpackages-filesystem
Obsoletes: %{name}-common <= 20090906-5.fc12

%description -n %{fontname}-sans-fonts
%common_desc

Droid Sans is a humanist sans serif typeface designed for user interfaces and
electronic communication.

%_font_pkg -n sans -f ??-%{fontname}-sans.conf DroidSans*ttf
%exclude %{_fontdir}/DroidSansMono*ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package -n %{fontname}-sans-mono-fonts
Summary:  A humanist monospace sans serif typeface
Requires: fontpackages-filesystem

%description -n %{fontname}-sans-mono-fonts
%common_desc

Droid Sans Mono is a humanist monospace sans serif typeface designed for user
interfaces and electronic communication.

%_font_pkg -n sans-mono -f ??-%{fontname}-sans-mono.conf DroidSansMono.ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml

%package -n %{fontname}-serif-fonts
Summary:  A contemporary serif typeface
Requires: fontpackages-filesystem
Provides: %{fontname}-naskh-fonts = %{version}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.
The Arabic block was designed by Pascal Zoghbi of 29ArabicLetters under the
Droid Naskh name.

%_font_pkg -n serif -f ??-%{fontname}-serif.conf DroidSerif*ttf DroidNaskh*ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%package -n %{fontname}-kufi-fonts
Summary:  A kufi Arabic titling typeface designed to complement Droid Sans
Requires: fontpackages-filesystem
Requires: %{fontname}-kufi-fonts

%description -n %{fontname}-kufi-fonts
%common_desc

Droid Kufi is a stylized display font suitable for titles and short runs of
text, and designed to complement Droid Sans. It was initialy designed by
Steve Matteson of Ascender with consulting by Pascal Zoghbi of 29ArabicLetters
to finalize the font family.

%_font_pkg -n kufi -f ??-%{fontname}-kufi.conf DroidKufi*ttf
%{_datadir}/appdata/%{fontname}-kufi.metainfo.xml

%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p $(ls *ttf | grep -v DroidSansFallbackFull\
                             | grep -v DroidSansFallbackLegacy\
                             | grep -v DroidNaskh-Regular-SystemUI) \
                    %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-sans.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/60-%{fontname}-sans-mono.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-serif.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-kufi.conf

for fontconf in 65-%{fontname}-sans.conf \
                60-%{fontname}-sans-mono.conf \
                65-%{fontname}-serif.conf \
                65-%{fontname}-kufi.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
install -Dm 0644 -p %{SOURCE17} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-kufi.metainfo.xml

%changelog
* Wed Jan 27 2020  HAL <notes2@gmx.de> - 20120715-16
- initial commit of the font collection

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120715-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120715-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120715-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120715-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120715-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120715-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20120715-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120715-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 08 2014 Parag Nemade <pnemade AT redhat DOT com> - 20120715-8
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove removal of buildroot in %%install
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120715-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120715-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120715-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120715-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20120715-3
— Split Kufi in a separate subpackage and resurect DroidSansArabic for Sans

* Sun Jul 15 2012 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20120715-1
— Switch to new upstream git source (marginally less hopeless than the Google
  Font Directory)
— Remove Arabic, add Armenian, Devanagari, Ethiopic, Georgian, Tamil, Kufi to Sans
– Add Naskh to Serif
– Try to adapt fontconfig rules to new upstream rules and new fonts

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20100409-3
– Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 20100409-2
– Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20100409-1
— Update to upstream's latest data dump
— Add Arabic, Hebrew, Thai coverage to Sans

* Mon Sep 28 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-5
— Tweak the fontconfig fixing

* Sun Sep 13 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-4
— follow the fontpackages template more closely
- 20090906-3
— more Behdad-suggested fontconfig tweaks

* Mon Sep  7 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-2
— first-level CJK fixes (as suggested by Behdad in bug #517789, complete fix
   needs the rpm changes traced in bug #521697)

* Sun Sep  6 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-1
— upstream stealth update

* Sat Jul 25 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090320-3
— try to fit Japanese in

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 1.0.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.112-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-5
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sat Jan 31 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-4
⬨ fix-up fontconfig installation for sans and mono

* Fri Jan 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-3
⁉ Workaround RHEL5 rpmbuild UTF-8 handling bug
- 1.0.112-2
⁍ Convert to new naming guidelines
⁍ Do strange stuff with Sans Fallback (CJK users please check)

* Tue Dec  9 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-1
փ Licensing bit clarified in bug #472635
շ Fedora submission

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.107-1
Ϫ Initial built using “fontpackages”

