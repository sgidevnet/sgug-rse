%global	priority	70
%global	fontname	motoya-lcedar
%global	archivedate	20110406
%global	fontconf	%{priority}-%{fontname}.conf
%global	download_root	http://android.git.kernel.org/?p=platform/frameworks/base.git;a=blob_plain;f=data/fonts/

Name:		%{fontname}-fonts
Version:	1.00
Release:	0.21.%{archivedate}git%{?dist}
Summary:	Japanese Gothic-typeface TrueType fonts by MOTOYA Co,LTD

License:	ASL 2.0
URL:		http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
Source0:	%{download_root}MTLc3m.ttf
Source1:	%{download_root}NOTICE
Source2:	%{download_root}README.txt
Source10:	%{fontname}-fontconfig.conf
Source11:       %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel libappstream-glib
Requires:	fontpackages-filesystem

%description
Motoya font was created in 1950s, it aims beauty and readability.
"MotoyaLCedar W3 mono", Gothic-typeface font was contributed by
MOTOYA Co,LTD. for Android platform.

%prep
%setup -q -c -T
install -m 0644 -p %{SOURCE1} notice.txt
install -m 0644 -p %{SOURCE2} readme.txt


%build


%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} $RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc readme.txt
%license notice.txt
%{_metainfodir}/%{fontname}.metainfo.xml


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.21.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 1.00-0.20.20110406git
- Install metainfo files under %%{_metainfodir}.

* Fri May 17 2019 Akira TAGOH <tagoh@redhat.com> - 1.00-0.19.20110406git
- Fix a typo in conf.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.18.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.17.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.16.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 1.00-0.14.20110406git
- Update the priority to change the default font to Noto.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.14.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.13.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-0.12.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.11.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 09 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.00-0.10.20110406git
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove removal of buildroot in %%install
- Remove group tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.9.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.8.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.7.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.6.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Akira TAGOH <tagoh@redhat.com> - 1.00-0.5.20110406git
- Correct fontconfig config file. (#837530)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.4.20110406git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr  8 2011 Akira TAGOH <tagoh@redhat.com> - 1.00-0.3.20110406git
- Updates from upstream git.
  https://review.source.android.com/#change,22161

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-0.2.20100928git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Akira TAGOH <tagoh@redhat.com> - 1.00-0.1.20100928git
- Initial package.

