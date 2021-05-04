Name:           abe
Version:        1.1
Release:        36%{?dist}

Summary:        Scrolling, platform-jumping, ancient pyramid exploring game
License:        GPL+
URL:            http://abe.sourceforge.net/
Source0:        http://downloads.sourceforge.net/abe/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar.xz
Source2:        %{name}.appdata.xml
# Enable changing the video settings.  Sent upstream 2 Apr 2006:
# https://sourceforge.net/tracker/?func=detail&aid=1463202&group_id=70141&atid=526743
Patch0:         %{name}-1.1-settings.patch
# Fix a double free() bug.  Sent upstream 15 Mar 2011:
# https://sourceforge.net/tracker/?func=detail&aid=3214269&group_id=70141&atid=526745
Patch1:         %{name}-1.1-doublefree.patch
# Fix an incorrect printf format specifier.  Sent upstream 15 Mar 2011:
# https://sourceforge.net/tracker/?func=detail&aid=3214270&group_id=70141&atid=526745
Patch2:         %{name}-1.1-format.patch
# Add support for aarch64.  Sent upstream 25 Mar 2013:
# https://sourceforge.net/tracker/?func=detail&aid=3609029&group_id=70141&atid=526743
Patch3:         %{name}-1.1-aarch64.patch
# Fix build failure with -Werror=format-security
Patch4:         %{name}-1.1-format-security.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel

Requires:       hicolor-icon-theme

%description
A scrolling, platform-jumping, key-collecting, ancient pyramid exploring game,
vaguely in the style of similar games for the Commodore+4.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4

# Fix the FSF's address
sed 's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' COPYING > COPYING.new
touch -r COPYING COPYING.new
mv -f COPYING.new COPYING

%build
%configure --with-data-dir=%{_datadir}/%{name}
sed -i "s|^CFLAGS =.*|CFLAGS = ${RPM_OPT_FLAGS} \$\(SDL_CFLAGS\)|" src/Makefile
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# make install does not copy the game data files.
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/appdata/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/
cp -p -r images maps sounds $RPM_BUILD_ROOT/%{_datadir}/%{name}
tar xJf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata/

cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Abe
Comment="Abe's Amazing Adventure"
Exec=abe
Icon=abe
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ %{name}.desktop

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-32
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Jerry James <loganjerry@gmail.com> - 1.1-28
- Add OARS data to the appdata file
- Update -aarch64 patch with newer config.{guess,sub}

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Jerry James <loganjerry@gmail.com> - 1.1-24
- Drop unused abe.png file
- Update -aarch64 patch with newer config.{guess,sub}

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 1.1-23
- Add icons of varying sizes
- Use the new license macro

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Jerry James <loganjerry@gmail.com> - 1.1-21
- Add -format-security patch

* Fri Nov  8 2013 Jerry James <loganjerry@gmail.com> - 1.1-20
- Add an AppData file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Jerry James <loganjerry@gmail.com> - 1.1-18
- Add aarch64 support (bz 924964)
- Fix the FSF's address in COPYING
- Add comments on the upstream status of each patch
- Remove deprecated "Encoding" key from desktop file

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1-17
- Remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
 
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 1.1-14
- Rebuild for GCC 4.7
- Remove bogus script Requires
- Remove unnecessary spec file elements (clean script, etc.)

* Mon Mar 14 2011 Jerry James <loganjerry@gmail.com> - 1.1-13
- Fix double free (bz 509052)
- Fix incorrectly-sized format specifier
- Don't use abe's extra optimization and debugging CFLAGS (fixes debuginfo)
- Remove filename extension from Icon field in desktop file
- Remove BuildRoot tag
- Add post/postun scripts, fix Requires for those scripts

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Wart <wart@kobold.org> - 1.1-9
- Add coreutils requirement for rpm post scripts

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.1-8
- Fix Patch0:/%%patch mismatch.

* Fri Feb 8 2008 Wart <wart@kobold.org> 1.1-7
- Rebuild for gcc 4.3

* Wed Aug 15 2007 Wart <wart@kobold.org> 1.1-6
- License tag clarification
- Simplify %%file section

* Fri Jun 1 2007 Wart <wart@kobold.org> 1.1-5
- Update desktop category for better game menu integration
- Use improved download URL.

* Thu Aug 31 2006 Wart <wart@kobold.org> 1.1-4
- Add missing BuildRequires

* Thu Aug 31 2006 Wart <wart@kobold.org> 1.1-3
- Rebuild for Fedora Extras

* Sun Apr 2 2006 Wart <wart@kobold.org> 1.1-2
- Enable changing the video settings (BZ #187589)

* Sat Mar 4 2006 Wart <wart@kobold.org> 1.1-1
- Update to 1.1

* Sat Mar 4 2006 Wart <wart@kobold.org> 1.0-6
- rebuild for FC5

* Mon Apr 11 2005 Panu Matilainen <pmatilai@welho.com> 0:1.0-5
- fix build on gcc4
- patch to fix issues in #149362

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Aug 13 2003 Panu Matilainen <pmatilai@welho.com> 0:1.0-0.fdr.3
- doh.. remember to update the icon to png in desktop file too

* Fri Aug 08 2003 Panu Matilainen <pmatilai@welho.com> 0:1.0-0.fdr.2
- fix QA issues in #555

* Sun Aug 03 2003 Panu Matilainen <pmatilai@welho.com> 0:1.0-0.fdr.1
- Initial Fedora packaging.
