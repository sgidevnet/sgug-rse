%define fontname taipeifonts
%define common_desc Traditional Chinese Bitmap fonts

%define bmpfontdir    %{_datadir}/fonts/%{name}
%define catalogue     /etc/X11/fontpath.d

Name:       %{fontname}
Version:    1.2
Release:    26%{?dist}
Summary:    %common_desc

License:    Public Domain
URL:        http://cle.linux.org.tw/

BuildArch:        noarch
BuildRequires:    xorg-x11-font-utils

Source0:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{name}-%{version}/%{name}.alias
Source2:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{name}-%{version}/re-build.readme

%description
%common_desc

%prep
%setup -q
cp -p %SOURCE2 README

%build
bdftopcf taipei24.bdf | gzip -c > taipei24.pcf.gz
bdftopcf taipei20.bdf | gzip -c > taipei20.pcf.gz
bdftopcf taipei16.bdf | gzip -c > taipei16.pcf.gz

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei24.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei20.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei16.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 vga12x24.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{bmpfontdir}/fonts.alias

mkfontdir $RPM_BUILD_ROOT%{bmpfontdir}

# catalogue
install -d $RPM_BUILD_ROOT%{catalogue}
ln -s %{bmpfontdir} $RPM_BUILD_ROOT%{catalogue}/%{name}

%post
if [ -x %{_bindir}/fc-cache ]; then
  %{_bindir}/fc-cache %{_datadir}/fonts
fi

%postun
if [ "$1" = "0" ]; then
  if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_datadir}/fonts
  fi
fi

%files
%doc README
%dir %{bmpfontdir}
%{bmpfontdir}/*.gz
%{bmpfontdir}/fonts.alias
%verify(not md5 size mtime) %{bmpfontdir}/fonts.dir
%{catalogue}/%{name}

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 1.2-12
- rebuild to ensure F14 has higher NVR than F13

* Tue Mar 02 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2-11.fc14
- Removes inappropriate ownership of /etc/X11/fontpath.d. (rhbz#569453)

* Wed Dec 01 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.2-10.fc12
- Fixes to Mailhot's font audit.
 - Add metadata.
 - Add default attributes.

* Fri Sep 25 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.2-9.fc12
- rebuild on dist-f12

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.2-7.fc11
- Rebuilt for Fedora 11.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 15 2007 Philippe Troin <phil@fifi.org> - 1.2-5.fc9
- Resolves: rhbz#386131 (Fonts not added to the font path catalogue.)
  <<<<< Put the fonts in the font catalogue.

* Thu Sep 28 2007 Caius Chance <cchance@redhat.com> - 1.2-4
- Resolves: rhbz#253812 (Package Review: taipeifonts.)
  <<<<< Updated URL and Source tags.

* Thu Sep 27 2007 Caius Chance <cchance@redhat.com> - 1.2-3
- Resolves: rhbz#253812 (Package Review: taipeifonts.)
  <<<<< Updated BuildRoot value according to Fedora specs.

* Tue Sep 25 2007 Jens Petersen <petersen@redhat.com> - 1.2-2
- various cleanup and fixes (#253812):
- use upstream name and version
- drop requires and ghost files
- make fonts.dir at buildtime
- use standard fc-cache scriptlets

* Wed Aug 22 2007 Caius Chance <cchance@redhat.com> - 1.2-1.fc8
- package split from fonts-chinese
Resolves: rhbz#253812 (New package separated from fonts-chinese.)
