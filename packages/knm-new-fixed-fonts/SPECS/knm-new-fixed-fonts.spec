%global		priority	69
%global		fontname	knm-new-fixed
%global		fontconf	%{priority}-%{fontname}.conf
%global		catalogue	%{_sysconfdir}/X11/fontpath.d

Name:		%{fontname}-fonts
Version:	1.1
Release:	28%{?dist}

Summary:	12x12 JIS X 0208 Bitmap fonts
License:	GPL+

## the following upstream URL is a dead link anymore.
#URL:		http://www.din.or.jp/~storm/fonts/
#Source0:	http://www.din.or.jp/~storm/fonts/knm_new.tar.gz
Source0:	knm_new.tar.gz
Source1:	%{name}-fontconfig.conf
BuildArch:	noarch
BuildRequires:	mkfontdir fontpackages-devel

Requires:	fontpackages-filesystem
Conflicts:	fonts-japanese <= 0.20061016-11.fc8
Obsoletes:	knm_new <= 1.1-16 knm_new-fonts < 1.1-7

%description
This package provides 12x12 Japanese bitmap fonts for JIS X 0208.
The JIS X 0208 character set contains the most often used Kanji glyphs.


%prep
%setup -q -T -c -a 0

%build

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0755 -d $RPM_BUILD_ROOT%{catalogue}

install -m 0644 -p fonts/*.pcf.gz $RPM_BUILD_ROOT%{_fontdir}/

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p	%{SOURCE1}	\
			$RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s	%{_fontconfig_templatedir}/%{fontconf}	\
	$RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

mkfontdir $RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
ln -s -f %{_fontdir} $RPM_BUILD_ROOT%{catalogue}/%{fontname}


%_font_pkg -f %{fontconf} *.pcf.gz

%lang(ja) %doc fonts/readme fonts/changes
%doc fonts/gtkrc.sample
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%{catalogue}/*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Akira TAGOH <tagoh@redhat.com> - 1.1-16
- Correct fontconfig config file. (#837537)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 25 2010 Akira TAGOH <tagoh@redhat.com> - 1.1-13
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 1.1-12
- Get rid of compare="contains".

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 1.1-11
- Get rid of binding="same" from the fontconfig config file. (#578027)

* Fri Dec  4 2009 Akira TAGOH <tagoh@redhat.com> - 1.1-10
- revert the previous change and set the priority to 69 to ensure loading
  the rule later according to the result of
  https://bugzilla.redhat.com/show_bug.cgi?id=532237#c6
  (#532237)

* Thu Oct 29 2009 Akira TAGOH <tagoh@redhat.com> - 1.1-9
- change the priority to 65 to make this the less priority.

* Tue Oct 20 2009 Akira TAGOH <tagoh@redhat.com> - 1.1-8
- Improve the spec file etc to pass the package review.

* Tue Oct 13 2009 Akira TAGOH <tagoh@redhat.com> - 1.1-7
- Renaming to satisfy the naming schema in the fontpackages policy.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 26 2009 Akira TAGOH <tagoh@redhat.com> - 1.1-5
- Clean up a spec file.
- Rebuild to correct autoprovides (#491966)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 30 2007 Akira TAGOH <tagoh@redhat.com> - 1.1-3
- Remove the upstream's dead link from the spec file. (#353941)

* Fri Sep  7 2007 Akira TAGOH <tagoh@redhat.com> - 1.1-2
- clean up

* Thu Aug 30 2007 Akira TAGOH <tagoh@redhat.com> - 1.1-1
- Split up from fonts-japanese.

