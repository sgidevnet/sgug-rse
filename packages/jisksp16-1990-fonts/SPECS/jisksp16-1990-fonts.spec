%global	fontname	jisksp16-1990
%global	catalogue	%{_sysconfdir}/X11/fontpath.d

Name:		%{fontname}-fonts
Version:	0.983
Release:	19%{?dist}
Summary:	16x16 JIS X 0212:1990 Bitmap font
License:	Public Domain

URL:		http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/
Source0:	http://kanji.zinbun.kyoto-u.ac.jp/~yasuoka/ftp/fonts/jisksp16-1990.bdf.Z

BuildArch:	noarch
BuildRequires:	gzip mkfontdir xorg-x11-font-utils fontpackages-devel

Requires:	fontpackages-filesystem
Conflicts:	fonts-japanese <= 0.20061016-11.fc8
Provides:	jisksp16-1990 = 0.1-16
Obsoletes:	jisksp16-1990 <= 0.1-16

%description
This package provides 16x16 Japanese bitmap font for JIS X 0212:1990.
JIS X 0212:1990 is a character sets that contains the auxiliary kanji
characters.


%prep
%setup -c -T
gunzip -c %{SOURCE0} > jisksp16-1990.bdf

%build
%{_bindir}/bdftopcf jisksp16-1990.bdf | gzip -9c > jisksp16-1990.pcf.gz

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{catalogue}

install -m 0644 -p jisksp16-1990.pcf.gz $RPM_BUILD_ROOT%{_fontdir}/

%{_bindir}/mkfontdir $RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
ln -sf %{_fontdir} $RPM_BUILD_ROOT%{catalogue}/%{name}


%_font_pkg jisksp16-1990.pcf.gz

%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%{catalogue}/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.983-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.983-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.983-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.983-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.983-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.983-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.983-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 26 2009 Akira TAGOH <tagoh@redhat.com> - 0.983-4
- Update a spec file a bit.
- rebuild to correct autoprovides. (#491965)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 24 2007 Akira TAGOH <tagoh@redhat.com> - 0.983-2
- Use %%setup.

* Fri Aug 17 2007 Akira TAGOH <tagoh@redhat.com> - 0.983-1
- Split up from fonts-japanese.

