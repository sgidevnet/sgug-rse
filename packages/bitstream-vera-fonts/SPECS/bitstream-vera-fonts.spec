%global fontname    bitstream-vera
%global archivename ttf-bitstream-vera

%global common_desc \
The Vera fonts are high-quality Latin fonts donated by Bitstream. \
These fonts have been released under a liberal license, see the  \
licensing FAQ in COPYRIGHT.TXT or the online up-to-date version \
at %{url} for details.

Name:    %{fontname}-fonts
Version: 1.10
Release: 34%{?dist}
Summary: Bitstream Vera fonts

License:   Bitstream Vera
URL:       http://www.gnome.org/fonts/
Source:    ftp://ftp.gnome.org/pub/GNOME/sources/%{archivename}/%{version}/%{archivename}-%{version}.tar.bz2
Source1:   %{fontname}.metainfo.xml
Source2:   %{fontname}-sans.metainfo.xml
Source3:   %{fontname}-serif.metainfo.xml
Source4:   %{fontname}-sans-mono.metainfo.xml


BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc


%package common
Summary:   Common files of the Bitstream Vera font set
Requires:  fontpackages-filesystem
Obsoletes: %{name}-compat < 1.10-17

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-sans-fonts
Summary:  Variable-width sans-serif Bitstream Vera fonts
Requires: %{name}-common = %{version}-%{release}

Obsoletes: %{name}-sans < 1.10-13

%description -n %{fontname}-sans-fonts
%common_desc

This package consists of the Bitstream Vera sans-serif variable-width font
faces.

%_font_pkg -n sans Vera.ttf VeraBd.ttf VeraIt.ttf VeraBI.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml


%package -n %{fontname}-serif-fonts
Summary:  Variable-width serif Bitstream Vera fonts
Requires: %{name}-common = %{version}-%{release}

Obsoletes: %{name}-serif < 1.10-13

%description -n %{fontname}-serif-fonts
%common_desc

This package consists of the Bitstream Vera serif variable-width font faces.

%_font_pkg -n serif VeraSe*ttf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml


%package -n %{fontname}-sans-mono-fonts
Summary:  Monospace sans-serif Bitstream Vera fonts
Requires: %{name}-common = %{version}-%{release}

Obsoletes: %{name}-sans-mono < 1.10-13

%description -n %{fontname}-sans-mono-fonts
%common_desc

This package consists of the Bitstream Vera sans-serif monospace font faces.

%_font_pkg -n sans-mono VeraMo*ttf
%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml


%prep
%setup -q -n %{archivename}-%{version}

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml


%files common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc *.TXT


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Richard Hughes <richard@hughsie.com> - 1.10-26
- Fix the metainfo description...

* Fri Oct 17 2014 Richard Hughes <richard@hughsie.com> - 1.10-25
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.10-17
— remove pre-F11 compatibility metapackage


* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.10-15
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Thu Jan 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.10-14
– update for new naming guidelines
– build with new fontpackages (1.15)

* Sun Nov 23 2008 <nicolas.mailhot at laposte.net>
- 1.10-12
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 <nicolas.mailhot at laposte.net>
- 1.10-11
▤ Rebuild using new « rpm-fonts »

* Fri Aug 10 2007 Matthias Clasen <mclasen@redhat.com> - 1.10-8
- Update license field
- Shorten description line

* Fri Sep 08 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.10-7
- s/latin/Latin/ in package description (#205693)

* Fri Jul 14 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.10-6
- remove ghost file fonts.cache-1 as fontconfig uses out of tree
  cache files now.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.10-5.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Jan 08 2005 Florian La Roche <laroche@redhat.com>
- rebuilt to get rid of legacy selinux filecontexts

* Sun May 30 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- change post/postun scripts

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 10 2003 Owen Taylor <otaylor@redhat.com> 1.10-1
- Base package on spec file from Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- Cleanups from Warren Togami and Nicolas Mailhot
