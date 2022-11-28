%global fontname iso8859-2

%global __mkfontdir umask 133;mkfontdir
%global catalogue  %{_sysconfdir}/X11/fontpath.d

Name:           %{fontname}-fonts
Version:        1.0
Release:        39%{?dist}
Summary:        Central European language fonts for the X Window System
License:        MIT
# Upstream url http://www.biz.net.pl/images/ISO8859-2-bdf.tar.gz is dead now.
Source:         ISO8859-2-bdf.tar.gz

Patch0:         XFree86-ISO8859-2-1.0-redhat.patch
BuildArch:      noarch
Buildrequires:  xorg-x11-font-utils
BuildRequires:  fontpackages-devel
Requires:       mkfontdir
 
%description
If you use the X Window System and you want to display Central
European fonts, you should install this package.


%package common
Summary:        Common files of %{name}
Requires:       fontpackages-filesystem

%description common
Common files of %{name}.


%package -n %{fontname}-misc-fonts
Summary:        A set of misc Central European language fonts for X
Obsoletes:      fonts-ISO8859-2 < 1.0-23
Provides:       fonts-ISO8859-2 = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       mkfontdir

%description -n %{fontname}-misc-fonts
This package contains a set of Central European fonts, in
compliance with the ISO8859-2 standard.


%package -n %{fontname}-75dpi-fonts
Summary:        A set of 75dpi Central European language fonts for X
Obsoletes:      fonts-ISO8859-2-75dpi < 1.0-23
Provides:       fonts-ISO8859-2-75dpi = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       mkfontdir

%description -n %{fontname}-75dpi-fonts
This package contains a set of Central European language fonts in 75 dpi
resolution for the X Window System. 


%package -n %{fontname}-100dpi-fonts
Summary:        A set of 100dpi Central European language fonts for X
Obsoletes:      fonts-ISO8859-2-100dpi < 1.0-23
Provides:       fonts-ISO8859-2-100dpi = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       mkfontdir

%description -n %{fontname}-100dpi-fonts
This package includes Central European (ISO8859-2) fonts, in 100 dpi
resolution, for the X Window System.


%prep
%setup -c -q
chmod 644 RELEASE_NOTES.TXT
sed -i "/\--0/d" 100dpi/fonts.alias
sed -i "/\--0/d" 75dpi/fonts.alias

%patch0 -p1 -b .redhat

%build
make all

%install
make install PREFIX=$RPM_BUILD_ROOT \
           FONTDIR=$RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{_fontdir}/misc $RPM_BUILD_ROOT%{catalogue}/%{fontname}-misc-fonts
ln -sf %{_fontdir}/75dpi $RPM_BUILD_ROOT%{catalogue}/%{fontname}-75dpi-fonts
ln -sf %{_fontdir}/100dpi $RPM_BUILD_ROOT%{catalogue}/%{fontname}-100dpi-fonts

%post -n %{fontname}-misc-fonts
{
    %__mkfontdir %{_fontdir}/misc
} &> /dev/null || :

%post -n %{fontname}-75dpi-fonts
{
    %__mkfontdir %{_fontdir}/75dpi
} &> /dev/null || :

%post -n %{fontname}-100dpi-fonts
{
    %__mkfontdir %{_fontdir}/100dpi
} &> /dev/null || :


%files -n %{fontname}-misc-fonts
%doc
%dir %{_fontdir}/misc
%{_fontdir}/misc/*.gz
%verify(not md5 size mtime) %{_fontdir}/misc/fonts.alias
%verify(not md5 size mtime) %{_fontdir}/misc/fonts.dir
%{catalogue}/%{fontname}-misc-fonts

%files -n %{fontname}-75dpi-fonts
%doc
%dir %{_fontdir}/75dpi
%{_fontdir}/75dpi/*.gz
%verify(not md5 size mtime) %{_fontdir}/75dpi/fonts.alias
%verify(not md5 size mtime) %{_fontdir}/75dpi/fonts.dir
%{catalogue}/%{fontname}-75dpi-fonts

%files -n %{fontname}-100dpi-fonts
%doc
%dir %{_fontdir}/100dpi
%{_fontdir}/100dpi/*.gz
%verify(not md5 size mtime) %{_fontdir}/100dpi/fonts.alias
%verify(not md5 size mtime) %{_fontdir}/100dpi/fonts.dir
%{catalogue}/%{fontname}-100dpi-fonts

%files common
%doc *.TXT
%dir %{_fontdir}

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Parag Nemade <pnemade AT redhat DOT com> 1.0-36
- fonts.alias wrongly claims the fonts are scalable (rh#1551221)
- Follow current packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 17 2010 Parag <pnemade AT redhat.com> 1.0-24
- Repackaged according to current Fonts packaging guidelines.
- Added -common subpackage

* Tue Mar 02 2010 Parag <pnemade AT redhat.com> 1.0-23
- Resolves:rh#569428 - Wrong directory ownership of %%{catalogue}

* Tue Aug 11 2009 Parag <pnemade@redhat.com> - 1.0-22
- Fixed for Source Audit 2009-08-10

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-19
- fix license tag

* Tue Aug 21 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-18.fc8
- Dropping chkfontpath dependency (bug #251026, by Matthias Clasen)
- Spec cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0-17.1
- rebuild

* Tue Feb 21 2006 Karsten Hopp <karsten@redhat.de> 1.0-17
- BuildRequire xorg-x11-font-utils

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov  7 2005 Caolan McNamara <caolanm@redhat.com> - 1.0-16
- modular X

* Fri Oct 28 2005 Caolan McNamara <caolanm@redhat.com> - 1.0-15
- package description mentions old package name

* Thu Mar  3 2005 Mike A. Harris <mharris@redhat.com> - 1.0-14
- *cough* Rebuild for FC4 with gcc 4 *cough*

* Wed Sep 22 2004 Owen Taylor <otaylor@redhat.com> - 1.0-13
- Require xorg-x11-font-utils (#125031, Maxim Dzumanenko)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Oct  7 2002 Mike A. Harris <mharris@redhat.com> 1.0-10
- All-arch rebuild
-
* Fri Jun 21 2002 Mike A. Harris <mharris@redhat.com> 1.0-9
- Totally non-automated rebuild done manually without assistance of
  any fancy pants scripts or other automation utilities  ;o)
- Added :unscaled FPE attributes to all bitmap font rpm scripts

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun  4 2002 Mike A. Harris <mharris@redhat.com> 1.0-7
- Removed ulT1mo fonts

* Thu May 23 2002 Tim Powers <timp@redhat.com> 1.0-4
- automated rebuild

* Mon Apr 15 2002 Mike A. Harris <mharris@redhat.com> 1.0-3
- Made Type1 subpackage to own the afm/pfm directories
- removed fonts.* glob from all subpackages, and manually listed each of the
  various fonts.{alias,dir,scale} files individually with the proper
  ghost/config/verify flags (MF #61694)
- Cleaned up post/postun scripts to match the XFree86 packaging style, and
  made the fonts.dir files generated at install time like they should be
  instead of included with the packaging which is broken and evil.

* Mon Apr  8 2002 Mike A. Harris <mharris@redhat.com> 1.0-2
- Added proper prereqs for chkfontpath, mkfontdir for bug (#62741)

* Thu Feb 28 2002 Mike A. Harris <mharris@redhat.com> 1.0-1
- Moved ulT1mo fonts from XFree86 packaging back out into their own happy
  rpm package.  Renamed it to fonts-foo to remove XFree86 reference since
  it is not an XFree86 package.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 17 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment

* Sat May 27 2000 Ngo Than <than@redhat.de>
- rebuild for 7.0

* Thu Aug 19 1999 Preston Brown <pbrown@redhat.com>
- fonts.* are now config files

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- fixed typos

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb 16 1999 Preston Brown <pbrown@redhat.com>
- chkfontpath compliant.

* Sat Feb 06 1999 Preston Brown <pbrown@redhat.com>
- fonts moved to %%{_fontbasedir}ISO8859-2 under new font scheme.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- packaged for RH 5.2
- made a noarch package

