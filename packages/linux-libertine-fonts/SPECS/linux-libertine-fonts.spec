%global fontname            linux-libertine
%global prio_libertine      60
%global prio_biolinum       61
%global fontconf_libertine  %{prio_libertine}-%{fontname}-libertine.conf
%global fontconf_biolinum   %{prio_biolinum}-%{fontname}-biolinum.conf
%global fontconf_metrics    29-%{fontname}-metrics-alias.conf
%global archivename         LinLibertine
%global posttag             2012_07_02

%define common_desc                                                     \
The Linux Libertine Open Fonts are a TrueType font family for practical \
use in documents.  They were created to provide a free alternative to   \
proprietary standard fonts.

Name:           %{fontname}-fonts
Version:        5.3.0
Release:        16.%{posttag}%{?dist}
Summary:        Linux Libertine Open Fonts

License:        GPLv2+ with exceptions or OFL
URL:            http://linuxlibertine.sf.net
Source0:        http://download.sourceforge.net/sourceforge/linuxlibertine/LinLibertineOTF_%{version}_%{posttag}.tgz
Source1:        %{name}-libertine-fontconfig.conf
Source2:        %{name}-biolinum-fontconfig.conf
Source3:        %{name}-libertine-metrics-alias-fontconfig.conf
Source4:        libertine.metainfo.xml
Source5:        biolinum.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel libappstream-glib
#BuildRequires:  fontforge
Requires:       %{name}-common = %{version}-%{release}

%description
%common_desc

This package contains Serif fonts.

%package -n %{fontname}-biolinum-fonts
Summary:        Sans-serif fonts from Linux Libertine Open Fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-biolinum-fonts
%common_desc

This package contains Sans fonts.

%package common
Summary:        Common files for Linux Libertine Open Fonts
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%prep
%setup -q -c
sed -i -e 's/\r//' OFL-1.1.txt

%build
#for i in $(find -name '*.sfd'); do
#  (cd scripts;
#   ./bailly-2.sh "../$i" ttf
#  )
#done
#mv scripts/*.ttf .

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_libertine}
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_biolinum}
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_metrics}

for fconf in %{fontconf_libertine} %{fontconf_metrics} %{fontconf_biolinum}; do
    ln -s %{_fontconfig_templatedir}/$fconf \
          %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_metainfodir}/libertine.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_metainfodir}/biolinum.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files common
%license GPL.txt LICENCE.txt OFL-1.1.txt
%doc Bugs.txt ChangeLog.txt Readme-TEX.txt README

%_font_pkg -f %{fontconf_libertine} LinLibertine*.otf
%{_metainfodir}/libertine.metainfo.xml

%{_fontconfig_templatedir}/%{fontconf_metrics}
%{_fontconfig_confdir}/%{fontconf_metrics}

%_font_pkg -n biolinum -f %{fontconf_biolinum} LinBiolinum*.otf
%{_metainfodir}/biolinum.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-16.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 5.3.0-15.2012_07_02
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-14.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-13.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Akira TAGOH <tagoh@redhat.com> - 5.3.0-12.2012_07_02
- Modernize the spec file.
- Fix bogus date in the spec file.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-11.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-10.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-9.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-8.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-7.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 5.3.0-6.2012_07_02
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-5.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-4.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-3.2012_07_02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Akira TAGOH <tagoh@redhat.com> - 5.3.0-2.2012_07_02
- Use OTF version of fonts.

* Tue Jul 24 2012 Akira TAGOH <tagoh@redhat.com> - 5.3.0-1.2012_07_02
- New upstream release.
- Giving up to build fonts from the source due to lacking of the build script.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.3-3.2011_06_21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Akira TAGOH <tagoh@redhat.com> - 5.1.3-2.2011_06_21
- Fix the order for substitute of Times New Roman. (#830849)

* Thu Apr 19 2012 Akira TAGOH <tagoh@redhat.com> - 5.1.3-1.2011_06_21
- New upstream release. (#813730)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.5-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 17 2011 Akira TAGOH <tagoh@redhat.com> - 4.7.5-1.2
- Improve the spec file to meet the packaging guidelines. (#477418)
- Updates to 4.7.5-2 (#628540)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Kevin Fenzi <kevin@tummy.com> - 4.4.1-1
- Upgrade to 4.4.1
- Fix to match current font guidelines

* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net> - 4.1.8-3
— Make sure F11 font packages have been built with F11 fontforge

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Frank Arnold <frank@scirocco-5v-turbo.de> 4.1.8-1
- Updated to 4.1.8
- Modified build procedure according to GENERATING.txt

* Wed Sep 3 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
-  2.7.9-2
⚙ Rebuild with pre-F10-freeze fontforge

* Sun Feb 03 2008 Frank Arnold <frank@scirocco-5v-turbo.de> 2.7.9-1
- Updated to 2.7.9
- Drop generated PDF files to save space

* Sun Sep 16 2007 Kevin Fenzi <kevin@tummy.com> - 2.6.9-1
- Updated to 2.6.9
- Update License tag

* Sat Mar 17 2007 Frank Arnold <frank@scirocco-5v-turbo.de> 2.4.9-1
- Updated to 2.4.9
- Reenabled generation of PDF files

* Sun Oct 01 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.2.0-1
- Updated to 2.2.0
- Removed ghosted cache file as it's no longer stored in tree
- Disabled generation of PDF files because fontforge will segfault
- Added OFL to License field

* Tue Sep 19 2006 Kevin Fenzi <kevin@tummy.com> 2.1.9-2
- Upload proper 2.1.9 sources and rebuild

* Tue Sep 19 2006 Kevin Fenzi <kevin@tummy.com> 2.1.9-1
- Update to 2.1.9

* Tue Aug 29 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.1.0-1
- Updated to 2.1.0

* Tue Feb 28 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.4-2
- Named back to linux-libertine-fonts

* Mon Feb 13 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.4-1
- Updated to 2.0.4
- Removed handling of fonts.cache-2

* Wed Feb 01 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.1-3
- Nuked separate fontforge build script, now in %%build section

* Tue Jan 31 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.1-2
- Fixed the following issues addressed by Ignacio Vazquez-Abrams
- Package renaming to font-linux-libertine
- Generate fonts from sources
- Sample sheets for each font in PDF format

* Mon Jan 30 2006 Frank Arnold <frank@scirocco-5v-turbo.de> 2.0.1-1
- Initial RPM release
- Spec derived from other font packages
