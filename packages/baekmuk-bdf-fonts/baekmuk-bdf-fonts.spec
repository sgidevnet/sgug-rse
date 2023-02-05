%global fontname   baekmuk-bdf

%global fontdir      %{_datadir}/fonts/%{fontname}
%global catalogue    %{_sysconfdir}/X11/fontpath.d

Name:           %{fontname}-fonts
Version:        2.2
Release:        25%{?dist}
Summary:        Korean bitmap fonts

License:        Baekmuk
URL:            http://kldp.net/projects/baekmuk/
Source:  http://kldp.net/frs/download.php/1428/%{fontname}-%{version}.tar.gz
Patch0:	 baekmuk-bdf-fonts-fix-fonts-alias.patch
BuildArch:      noarch
BuildRequires:  xorg-x11-font-utils
Conflicts:      fonts-korean < 2.2-5

%description
This package provides the Korean Baekmuk bitmap fonts.


%prep
%setup -q -n %{fontname}-%{version}
%patch0 -p1 -b .fix-fonts-alias

%build
for file in bdf/*.bdf; do
    bdftopcf $file | gzip -9 > ${file%.bdf}.pcf.gz
done

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{fontdir}

# for bmp font
install -m 0644 bdf/*.pcf.gz $RPM_BUILD_ROOT%{fontdir}/
install -m 0444 bdf/fonts.alias $RPM_BUILD_ROOT%{fontdir}/

# for catalogue
install -d $RPM_BUILD_ROOT%{catalogue}
ln -sf ../../..%{fontdir} $RPM_BUILD_ROOT%{catalogue}/%{name}

mkfontdir $RPM_BUILD_ROOT%{fontdir} 

# convert Korean copyright file to utf8
iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko

%post
if [ -x %{_bindir}/fc-cache ]; then
  %{_bindir}/fc-cache %{fontdir}
fi

%postun
if [ "$1" = "0" ]; then
  if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{fontdir}
  fi
fi

%files
%doc COPYRIGHT COPYRIGHT.ko README
%dir %{fontdir}
%{fontdir}/*.gz
%{fontdir}/fonts.alias
%verify(not md5 size mtime) %{fontdir}/fonts.dir
%{catalogue}/%{name}

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Daiki Ueno <dueno@redhat.com> - 2.2-18
- replace %%define uses with %%global

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Daiki Ueno <dueno@redhat.com> - 2.2-15
- Don't run fc-cache with /usr/share/fonts (Closes: #1021754)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Daiki Ueno <dueno@redhat.com> - 2.2-10
- add baekmuk-bdf-fonts-fix-fonts-alias.patch (#733105)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Caius 'kaio' Chance <cchance@redhat.com> - 2.2-7.fc11
- Rebuilt for Fedora 11.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 14 2007 Jens Petersen <petersen@redhat.com> - 2.2-5
- better url
- use fontname macro

* Tue Sep 25 2007 Jens Petersen <petersen@redhat.com> - 2.2-4
- fix name of fonts.alias file

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-3
- conflict with fonts-korean < 2.2-5

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-2
- convert Korean copyright file to utf8 (Mamoru Tasaka, #302451)

* Tue Sep 11 2007 Jens Petersen <petersen@redhat.com> - 2.2-1
- initial packaging separated from fonts-korean (#253155)
