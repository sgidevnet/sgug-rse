Summary: Murrine GTK2 engine
Name: gtk-murrine-engine
Version: 0.98.2
Release: 17%{?dist}
License: LGPLv2 or LGPLv3
URL: http://www.cimitan.com/murrine/
Source0: http://ftp.gnome.org/pub/GNOME/sources/murrine/0.98/murrine-%{version}.tar.xz
Source10: http://cimi.netsons.org/media/download_gallery/MurrinaFancyCandy.tar.bz2
Source11: http://cimi.netsons.org/media/download_gallery/MurrinaVerdeOlivo.tar.bz2
Source12: http://cimi.netsons.org/media/download_gallery/MurrinaAquaIsh.tar.bz2
Source13: http://cimi.netsons.org/media/download_gallery/MurrinaGilouche.tar.bz2
Source14: http://cimi.netsons.org/media/download_gallery/MurrinaLoveGray.tar.bz2
Source15: http://cimi.netsons.org/media/download_gallery/MurrineThemePack.tar.bz2

#rhbz 130313
Patch0: %{name}_possible-wnck-applet-crash.patch
Patch100: murrine.sgifixes.patch

BuildRequires:  gcc
BuildRequires: gtk2-devel intltool

%description
Murrine Engine is a Gtk2 theme engine, using the Cairo vector graphics
library. It comes by default with a modern glassy look, inspired by
Venetian glass artworks, and is extremely customizable.


%prep
%setup -q -n murrine-%{version}
%patch0 -p1
%patch100 -p1

%build
%configure --enable-animation --enable-animationrtl
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/themes
(cd $RPM_BUILD_ROOT/%{_datadir}/themes;
bzcat %{SOURCE10} | tar -xvf -;
bzcat %{SOURCE11} | tar -xvf -;
bzcat %{SOURCE12} | tar -xvf -;
bzcat %{SOURCE13} | tar -xvf -;
bzcat %{SOURCE14} | tar -xvf -;
bzcat %{SOURCE15} | tar -xvf -;
)
%{__sed} -i s/scrollbar_color/#\\0/ $RPM_BUILD_ROOT/%{_datadir}/themes/Murrina*/gtk-2.0/gtkrc

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true
#fix permission
find $RPM_BUILD_ROOT/%{_datadir}/themes -type f | xargs chmod 0644 || true

%files
%doc AUTHORS ChangeLog COPYING COPYING.2.1 NEWS
%{_libdir}/gtk-2.0/*/engines/*
%{_datadir}/gtk-engines
%{_datadir}/themes/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 25 2016 Martin Sourada <mso@fedoraproject.org> - 0.98.2-10
- Fix crash in wnck panel plugins (#1310313)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Martin Sourada <mso@fedoraproject.org> - 0.98.2-5
- Silence deprecation warnings (#1046757)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Martin Sourada <mso@fedoraproject.org> - 0.98.2-1
- Update to new upstream release (bugfix release)
- Fix build with newer glib

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.98.1.1-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Martin Sourada <mso@fedoraproject.org> - 0.98.1.1-1
- Update to 0.98.1.1
- License change to LGPLv2.1 and LGPLv3

* Wed Sep 29 2010 jkeating - 0.98.0-2
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Martin Sourada <mso@fedoraproject.org> - 0.98.0-1
- Update to 0.98.0

* Thu Nov 12 2009 Martin Sourada <mso@fedoraproject.org> - 0.90.3-3
- Don't own %%{_datadir}/themes

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Michel Salim <salimma@fedoraproject.org> - 0.90.3-1
- Update to 0.90.3

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.53.1-3
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.53.1-2
- Autorebuild for GCC 4.3

* Sun May 20 2007 Leo Shidai Liu <sdl.web@gmail.com> 0.53.1-1
- 0.53.1

* Thu Apr  5 2007 Leo, Shidai Liu <sdl.web@gmail.com> 0.52-1
- 0.52

* Thu Mar 15 2007 Leo, Shidai Liu <sdl.web@gmail.com> 0.51-2
- fix last change

* Thu Mar 15 2007 Leo, Shidai Liu <sdl.web@gmail.com> 0.51-1
- 0.51

* Fri Jan 12 2007 Shidai Liu, Leo <sdl.web@gmail.com> 0.41-1
- 0.41

* Wed Jan 10 2007 Shidai Liu, Leo <sdl.web@gmail.com> 0.40.1-1
- 0.40.1

* Fri Nov 24 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.31-4
- Correct changelog entries to include release number

* Tue Nov 21 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.31-3
- remove themes from gnome-look
- remove CREDITS patch
- add all themes from upstream

* Thu Nov 16 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.31-2
- 0.31

* Sun Nov 12 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.30.2-1
- Add three gtk2 themes

* Tue Sep 19 2006 Shidai Liu, Leo <sdl.web@gmail.com> 
- Initial build.

