%define fontname kacst
%define fontdir %{_datadir}/fonts/%{fontname}
%define	fontconf	67-%{fontname}

# Common description
%define common_desc \
This package contains fonts for the display of Arabic \
from the King Abdulaziz City for Science & Technology(kacst).

Name: %{fontname}-fonts
Version: 2.0
Release: 22%{?dist}
License: GPLv2
Source: http://downloads.sourceforge.net/sourceforge/arabeyes/%{fontname}_fonts_%{version}.tar.bz2
Source1: %{fontconf}-art.conf
Source2: %{fontconf}-book.conf
Source3: %{fontconf}-decorative.conf
Source4: %{fontconf}-digital.conf
Source5: %{fontconf}-farsi.conf
Source6: %{fontconf}-letter.conf
Source7: %{fontconf}-naskh.conf
Source8: %{fontconf}-office.conf
Source9: %{fontconf}-one.conf
Source10: %{fontconf}-pen.conf
Source11: %{fontconf}-poster.conf
Source12: %{fontconf}-qurn.conf
Source13: %{fontconf}-screen.conf
Source14: %{fontconf}-title.conf
Source15: %{fontconf}-titlel.conf
Source16: %{fontname}-art.metainfo.xml
Source17: %{fontname}-book.metainfo.xml
Source18: %{fontname}-decorative.metainfo.xml
Source19: %{fontname}-digital.metainfo.xml
Source20: %{fontname}-farsi.metainfo.xml
Source21: %{fontname}-letter.metainfo.xml
Source22: %{fontname}-naskh.metainfo.xml
Source23: %{fontname}-office.metainfo.xml
Source24: %{fontname}-one.metainfo.xml
Source25: %{fontname}-pen.metainfo.xml
Source26: %{fontname}-poster.metainfo.xml
Source27: %{fontname}-qurn.metainfo.xml
Source28: %{fontname}-screen.metainfo.xml
Source29: %{fontname}-title.metainfo.xml
Source30: %{fontname}-titlel.metainfo.xml

BuildArch: noarch
BuildRequires:	dos2unix
BuildRequires:	fontpackages-devel > 1.13
Obsoletes: fonts-arabic <= 2.1-2
Summary: Fonts for arabic from arabeyes project 
URL: http://www.arabeyes.org/resources.php	
 
%description
%common_desc

%package common
Summary:  Common files for kacst-fonts
Requires: fontpackages-filesystem

%description common
%common_desc

%package -n %{fontname}-book-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-book-fonts
This package contains book type fonts for the display of Arabic 

%_font_pkg -n book -f  %{fontconf}-book* KacstBook.ttf
%{_datadir}/appdata/%{fontname}-book.metainfo.xml


%package -n %{fontname}-digital-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-digital-fonts
This package contains digital type fonts for the display of Arabic 

%_font_pkg -n digital -f %{fontconf}-digital* KacstDigital.ttf
%{_datadir}/appdata/%{fontname}-digital.metainfo.xml


%package -n %{fontname}-letter-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-letter-fonts
This package contains book kacst fonts for the display of Arabic 

%_font_pkg -n letter -f %{fontconf}-letter* KacstLetter.ttf
%{_datadir}/appdata/%{fontname}-letter.metainfo.xml

%package -n %{fontname}-office-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-office-fonts
This package contains office type fonts for the display of Arabic 

%_font_pkg -n office -f %{fontconf}-office* KacstOffice.ttf
%{_datadir}/appdata/%{fontname}-office.metainfo.xml


%package -n %{fontname}-pen-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-pen-fonts
This package contains pen type fonts for the display of Arabic 

%_font_pkg -n pen -f %{fontconf}-pen* kacstPen.ttf
%{_datadir}/appdata/%{fontname}-pen.metainfo.xml


%package -n %{fontname}-qurn-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-qurn-fonts
This package contains qurn type fonts for the display of Arabic 

%_font_pkg -n qurn -f %{fontconf}-qurn* KacstQurn.ttf
%{_datadir}/appdata/%{fontname}-qurn.metainfo.xml

%package -n %{fontname}-titlel-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-titlel-fonts
This package contains title large type fonts for the display of Arabic 

%_font_pkg -n titlel -f %{fontconf}-titlel.conf KacstTitleL.ttf
%{_datadir}/appdata/%{fontname}-titlel.metainfo.xml

%package -n %{fontname}-art-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-art-fonts
This package contains art type fonts for the display of Arabic 

%_font_pkg -n art -f %{fontconf}-art* KacstArt.ttf
%{_datadir}/appdata/%{fontname}-art.metainfo.xml

%package -n %{fontname}-decorative-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-decorative-fonts
This package contains decorative type fonts for the display of Arabic 

%_font_pkg -n decorative -f %{fontconf}-decorative* KacstDecorative.ttf
%{_datadir}/appdata/%{fontname}-decorative.metainfo.xml

%package -n %{fontname}-farsi-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-farsi-fonts
This package contains farsi type fonts for the display of Arabic 

%_font_pkg -n farsi -f %{fontconf}-farsi* KacstFarsi.ttf
%{_datadir}/appdata/%{fontname}-farsi.metainfo.xml

%package -n %{fontname}-naskh-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-naskh-fonts
This package contains naskh type fonts for the display of Arabic 

%_font_pkg -n naskh -f %{fontconf}-naskh* KacstNaskh.ttf
%{_datadir}/appdata/%{fontname}-naskh.metainfo.xml

%package -n %{fontname}-one-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-one-fonts
This package contains one type fonts for the display of Arabic 

%_font_pkg -n one -f %{fontconf}-one* KacstOne.ttf
%{_datadir}/appdata/%{fontname}-one.metainfo.xml

%package -n %{fontname}-poster-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-poster-fonts
This package contains poster type fonts for the display of Arabic 

%_font_pkg -n poster -f %{fontconf}-poster* KacstPoster.ttf
%{_datadir}/appdata/%{fontname}-poster.metainfo.xml

%package -n %{fontname}-screen-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-screen-fonts
This package contains screen type fonts for the display of Arabic 

%_font_pkg -n screen -f %{fontconf}-screen* KacstScreen.ttf
%{_datadir}/appdata/%{fontname}-screen.metainfo.xml

%package -n %{fontname}-title-fonts
Summary: Fonts for arabic from arabeyes project 
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-title-fonts
This package contains title type fonts for the display of Arabic 

%_font_pkg -n title -f %{fontconf}-title.conf KacstTitle.ttf
%{_datadir}/appdata/%{fontname}-title.metainfo.xml


%prep
%setup -q -n KacstArabicFonts-%{version}
find . -not -name \*.ttf -type f -exec dos2unix -k {} \;

%build
echo "Nothing to do in Build."

%install
rm -rf %{buildroot} 

install -m 0755 -d %{buildroot}%{fontdir}
install -m 0644 -p *.ttf %{buildroot}%{fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-art.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-decorative.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-digital.conf
install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-farsi.conf
install -m 0644 -p %{SOURCE6} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-letter.conf
install -m 0644 -p %{SOURCE7} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-naskh.conf
install -m 0644 -p %{SOURCE8} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-office.conf
install -m 0644 -p %{SOURCE9} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-one.conf
install -m 0644 -p %{SOURCE10} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf
install -m 0644 -p %{SOURCE11} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-poster.conf
install -m 0644 -p %{SOURCE12} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-qurn.conf
install -m 0644 -p %{SOURCE13} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-screen.conf
install -m 0644 -p %{SOURCE14} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-title.conf
install -m 0644 -p %{SOURCE15} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-titlel.conf

for fconf in %{fontconf}-art.conf \
		%{fontconf}-book.conf \
		%{fontconf}-decorative.conf \
		%{fontconf}-digital.conf \
		%{fontconf}-farsi.conf \
		%{fontconf}-letter.conf \
		%{fontconf}-naskh.conf \
		%{fontconf}-office.conf \
		%{fontconf}-one.conf \
		%{fontconf}-pen.conf \
		%{fontconf}-poster.conf \
		%{fontconf}-qurn.conf \
		%{fontconf}-screen.conf \
		%{fontconf}-title.conf \
		%{fontconf}-titlel.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-art.metainfo.xml
install -Dm 0644 -p %{SOURCE17} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-book.metainfo.xml
install -Dm 0644 -p %{SOURCE18} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-decorative.metainfo.xml
install -Dm 0644 -p %{SOURCE19} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-digital.metainfo.xml
install -Dm 0644 -p %{SOURCE20} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-farsi.metainfo.xml
install -Dm 0644 -p %{SOURCE21} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-letter.metainfo.xml
install -Dm 0644 -p %{SOURCE22} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-naskh.metainfo.xml
install -Dm 0644 -p %{SOURCE23} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-office.metainfo.xml
install -Dm 0644 -p %{SOURCE24} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-one.metainfo.xml
install -Dm 0644 -p %{SOURCE25} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-pen.metainfo.xml
install -Dm 0644 -p %{SOURCE26} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-poster.metainfo.xml
install -Dm 0644 -p %{SOURCE27} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-qurn.metainfo.xml
install -Dm 0644 -p %{SOURCE28} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-screen.metainfo.xml
install -Dm 0644 -p %{SOURCE29} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-title.metainfo.xml
install -Dm 0644 -p %{SOURCE30} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-titlel.metainfo.xml


%files common
%doc Copyright LICENSE README
%dir %{fontdir}

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Pravin Satpute <psatpute@redhat.com> - 2.0-14
- Added metainfo for gnome-software
- Removed buildroot and clean section

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 15 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-7
- fixed bug 578026, binding=same

* Fri Feb 26 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-6
- added .conf file for each subpackage
- resolves bug 567608

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Pravin Satpute <psatpute@redhat.com> - 2.0-4
- cleaned rpmlink

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 2.0-3
- updated spec as per new font packaging guideline

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Rahul Bhalerao <rbhalera@redhat.com> - 2.0-1.fc10
- Updated to new upstream version

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-4.fc10
- Dropping previous release

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-3.fc10
- Obsoleted dead package fonts-arabic

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-2.fc8
- Used dos2unix

* Fri Oct 12 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-1.fc8
- Initial Packaging
