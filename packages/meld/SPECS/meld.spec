Name:		meld
Version:	3.20.1
Release:	3%{?dist}
Summary:	Visual diff and merge tool

License:	GPLv2+
URL:		http://meldmerge.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.20/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	python3-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libappstream-glib

Requires:	glib2 >= 2.34.0
Requires:	gtk3 >= 3.6.0

Requires:	gtksourceview3 >= 3.6.0
Requires:	patch
Requires:	python3-cairo
%if 0%{?rhel}
Requires:   pygobject3
%else
Requires:	python3-gobject
%endif

Requires:	gsettings-desktop-schemas

BuildArch:	noarch

Provides:	mergetool
Provides:	difftool


%description
Meld is a visual diff and merge tool targeted at developers. It helps you
compare files, directories, and version controlled projects. It provides two-
and three-way comparison of both files and directories, and the tabbed interface
allows you to open many diffs at once.
Meld has has support for many popular version control systems including Git,
Mercurial, Bazaar, SVN and CVS. The diff viewer lets you edit files in place
(diffs update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy navigation.


%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
%{__python3} setup.py --no-update-icon-cache --no-compile-schemas install --root $RPM_BUILD_ROOT

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 6)
  --vendor fedora \
%endif
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  --delete-original \
  --add-category="GTK" \
  --remove-category="Application" \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/*%{name}.desktop \

mv ${RPM_BUILD_ROOT}/%{_datadir}/doc/%{name}-%{version} ${RPM_BUILD_ROOT}/%{_datadir}/doc/%{name}

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/*meld.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/meld/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/meld/b.png

%find_lang %{name} --with-gnome


%pre
# Remove duplicated doc directories (RHBZ#1261341)
if [ $1 -ge 1 ] ; then
  rm -rf %{_datadir}/doc/%{name}*
fi


%files -f %{name}.lang
%doc COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/mime/packages/*%{name}.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/metainfo/*%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/icons/HighContrast/*/apps/*%{name}.*
%{python3_sitelib}/*
%{_datadir}/glib-2.0/schemas/org.gnome.meld.gschema.xml
%{_mandir}/man1/meld.1*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Kalev Lember <klember@redhat.com> - 3.20.1-2
- Drop obsolete python3-dbus and dbus-x11 requires

* Sun Mar 31 2019 Dominic Hopf <dmaphy@fedoraproject.org> 3.20.1-1
- New upstream release: Meld 3.20.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Dominic Hopf <dmaphy@fedoraproject.org> 3.20.0-1
- New upstream release: Meld 3.20.0

* Tue Dec 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.19.1-1
- 3.19.1.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.19.0-2
- Rebuilt for Python 3.7

* Mon Apr 02 2018 Dominic Hopf <dmaphy@fedoraproject.org> 3.19.0-1
- New upstream release: Meld 3.19.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.18.0-2
- Remove obsolete scriptlets

* Sun Sep 10 2017 Dominic Hopf <dmaphy@fedoraproject.org> 3.18.0-1
- New upstream release: Meld 3.18.0

* Wed Aug 16 2017 Dominic Hopf <dmaphy@fedoraproject.org> 3.17.4-1
- New upstream release: Meld 3.17.4

* Sun Aug 13 2017 Dominic Hopf <dmaphy@fedoraproject.org> 3.17.3-1
- New upstream release: Meld 3.17.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Dominic Hopf <dmaphy@fedoraproject.org> 3.17.2-1
- New upstream release: Meld 3.17.2

* Sun Mar 19 2017 Dominic Hopf <dmaphy@fedoraproject.org> 3.17.1-4
- Remove duplicated doc directories (RHBZ#1261341)
- Ensure old versioned directories in /usr/share/doc are removed
- Specify the documentation files as documentation

* Mon Mar 13 2017 Dominic Hopf <dmaphy@fedoraproject.org> 3.17.1-1
- New upstream release: Meld 3.17.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 3.17.0-4
- Rebuild for Python 3.6

* Tue Dec 20 2016 Dominic Hopf <dmaphy@fedoraproject.org> 3.17.0-3
- Try to make dependencies to Python3 better (RHBZ#1406346)

* Mon Dec 19 2016 Dominic Hopf <dmaphy@fedoraproject.org> 3.17.0-2
- Update to 3.17.0 and Python3 (RHBZ#1405732)
- Remove duplicated doc directories (RHBZ#1261341)

* Sun Oct 09 2016 Thorsten Leemhuis <thl@fedoraproject.org> 3.16.3-2
- mention COPYING and NEWS only once in file section
- Conditionalize the dep on python-gobject to make spec file work on
  rhel and fedora

* Thu Sep 29 2016 Dominic Hopf <dmaphy@fedoraproject.org> 3.16.3-1
- Update to 3.16.3 (RHBZ#1380050)

* Sun Jul 31 2016 Dominic Hopf <dmaphy@fedoraproject.org> 3.16.2-1
- Update to 3.16.2 (RHBZ#1361780)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 20 2016 Dominic Hopf <dmaphy@fedoraproject.org> 3.16.1-1
- Update to 3.16.1 (RHBZ#1347968)

* Sun May 01 2016 Dominic Hopf <dmaphy@fedoraproject.org> 3.16.0-1
- Update to 3.16.0 (RHBZ#1321567)

* Tue Mar 29 2016 Dominic Hopf <dmaphy@fedoraproject.org> 3.15.2-1
- Update to 3.15.2 (RHBZ#1321567)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Dominic Hopf <dmaphy@fedoraproject.org> 3.15.1-1
- Update to 3.15.1 (RHBZ#1291664)

* Mon Oct 05 2015 Dominic Hopf <dmaphy@fedoraproject.org> 3.15.0-1
- Update to 3.15.0 (RHBZ#1268659)

* Mon Sep 28 2015 Dominic Hopf <dmaphy@fedoraproject.org> 3.14.0-2
- add dependency to python-gobject (RHBZ#1266389)

* Mon Jul 27 2015 Dominic Hopf <dmaphy@fedoraproject.org> 3.14.0-1
- Update to 3.14.0 (RHBZ#1246475)

* Mon Jul 13 2015 Dominic Hopf <dmaphy@fedoraproject.org> 3.13.3-1
- Update to 3.13.3 (RHBZ#1242225)

* Sun Jul 05 2015 Dominic Hopf <dmaphy@fedoraproject.org> 3.13.2-1
- Update to 3.13.1 (RHBZ#1239300)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Dominic Hopf <dmaphy@fedoraproject.org> 3.13.1-1
- Update to 3.13.1 (RHBZ#1214727)

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.13.0-3
- Use better AppData screenshots

* Fri Feb 20 2015 Lubomir Rintel <lkundrak@v3.sk> - 3.13.0-2
- Add missing dependencies (Pavel Alexeev, #1192623)

* Wed Jan 07 2015 Richard Hughes <rhughes@redhat.com> - 3.13.0-1
- Update to 3.13.0

* Thu Dec 18 2014 Richard Hughes <rhughes@redhat.com> - 3.12.2-1
- Update to 3.12.2

* Thu Nov 06 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 3.12.1-1
- Update to 3.12.1
- Fix SVN breaking on non-root directories.
- Fix GtkSource view parameters not being honored.

* Sat Oct 04 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 3.12.0-1
- Update to 3.12.0

* Fri Sep 19 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 3.11.4-1
- Update to 3.11.4

* Fri Sep 12 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 3.11.3-1
- Update to 3.11.3

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> - 3.11.2-2
- update mime scriptlet
- drop added dep for icon scriptlets, see https://fedoraproject.org/wiki/Packaging:ScriptletSnippets?rd=Packaging/ScriptletSnippets#Icon_Cache

* Sat Jul 12 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 3.11.2-1
- Update to 3.11.2

* Wed Jun 11 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 3.11.1-2
- Require gtk2 for gtk-update-icon-cache

* Sun Jun 08 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 3.11.1-1
- Update to 3.11.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Richard Hughes <rhughes@redhat.com> - 3.11.0-1
- Update to 3.11.0

* Thu Jan 02 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 1.8.3-2
- add virtual Provides for mergetool (RHBZ#990449)

* Wed Jan 01 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 1.8.3-1
- New upstream release: Meld 1.8.3

* Fri Oct 18 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.8.2-1
- New upstream release: Meld 1.8.2

* Sun Sep 22 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.8.1-1
- New upstream release: Meld 1.8.1

* Sun Sep 15 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.8.0-1
- New upstream release: Meld 1.8.0

* Sun Sep 01 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.7.5-1
- New upstream release: Meld 1.7.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.7.3-1
- New upstream release: Meld 1.7.3

* Sat Mar 30 2013 Kalev Lember <kalevlember@gmail.com> - 1.7.1-3
- More rpm scriptlet fixes
- Use find_lang --with-gnome for the help documentation

* Sat Mar 30 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.7.1-2
- Fix mime installation
- Fix some changelog entries

* Sat Mar 30 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.7.1-1
- New upstream release: Meld 1.7.1

* Tue Feb 19 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.7.0-6
- Require dbus-python and dbus-x11 (#912580)
- Require pygtksourceview (#888717)
- No longer require pygtk-libglade (#887527)
- Update description and fix URL (#887527)

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7.0-5
- Conditionalize the --vendor removal so the spec can be used on other releases

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7.0-4
- remove the --vendor switch to desktop-file-install

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.7.0-2
- Remove version from Requires (RHBZ#873198)

* Wed Nov 21 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.7.0-1
- New upstream release: Meld 1.7.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 05 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.6.0-1
- New upstream release: Meld 1.6.0

* Sat Apr 07 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.5.4-1
- New upstream release: Meld 1.5.4

* Sat Feb 04 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.5.3-1
- New upstream release: Meld 1.5.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 1.5.2-1
- New upstream release: Meld 1.5.2

* Mon Apr 04 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.5.1-2
- Add NEWS to %%doc

* Sun Apr 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1
- Run gtk-update-icon-cache after (un)install

* Sun Mar 13 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 1.5.0-2
- remove the scrollkeeper patch
- add requirement for patch (fixes rhbz#651815)

* Sun Mar 13 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 1.5.0-1
- New upstream release: Meld 1.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Brian Pepple <bpepple@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0.
- Update source url.

* Mon Sep  6 2010 Brian Pepple <bpepple@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2.

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.1-3
- recompiling .py files against Python 2.7 (rhbz#623335)

* Sun Apr 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 1.3.1-2
- Remove clean section. No longer needed.

* Wed Jan  6 2010 Brian Pepple <bpepple@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1.
- Remove scrollkeeper scriptlets since they are no longer needed.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Brian Pepple <bpepple@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0.
- Drop gnome-python2-* requires, since they shouldn't be needed anymore.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.1-2
- Rebuild for Python 2.6

* Sun Nov 23 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.
- Drop desktop file patch.  Fixed upstream.

* Tue Aug 26 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2-2
- Change require to gnome-python2-gnome. (#460010)

* Sun Aug  3 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2-1
- Update to 1.2.
- Drop git patch.  fixed upstream.
- Update scrollkeeper patch.

* Tue Jun  3 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-5
- Backport git support (#449250).

* Wed Nov 14 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-4
- Add Requires on gnome-python2-gtksourceview to enable syntax coloring. (#382041)

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-3
- Update license tag.

* Sun Jun 10 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-2
- Drop requires on yelp.

* Sat Jun  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5.
- Drop gettext patch.  fixed upstream.

* Sat Jun  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-7
- Add requires on yelp.

* Sat Dec  9 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-6
- Drop X-Fedora category from desktop file.
- Add patch to fix rejects from new version of gettext.

* Fri Dec  8 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-5
- Rebuild against new python.

* Wed Sep  6 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-4
- Don't ghost *.pyo files.
- Add BR for intltool and perl(XML::Parser).
- Rebuild for FC6.

* Sun Jun 11 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.4-3
- Update to 1.1.4.

* Thu Feb 16 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.3-4
- Remove unnecessary BR (intltool).

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.3-3
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb  5 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.3-2
- Update to 1.1.3.
- Update scrollkeeper scriptlet.
- Update versions required for pygtk2 & gnome-python2.
- Add patch to disable scrollkeeper in Makefile.
- Ghost the *.pyo.

* Sun Nov 13 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.1.2-1
- Update to 1.1.2.

* Mon Jul 25 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.0-1
- Update to 1.0.0.
- Include fix for upstream bug #309408.

* Wed Jun  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.6-1
- Remove unused meld shell script from src.rpm.
- Add scriptlets for scrollkeeper-update.
- Use %%find_lang macro.
- Simplify %%install (let included Makefile do the installation).
- Update to 0.9.6 (fixes manual).
- BR scrollkeeper (#156235).

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.5-2
- rebuilt

* Sun Feb 06 2005 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.9.5-1
- 0.9.5.

* Thu Nov 11 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.9.4.1-0.fdr.3
- Clean up spec/Bump release.

* Sat Jul 31 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.4.1-0.fdr.2
- Group now Development/Tools.

* Wed Jul 21 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.4.1-0.fdr.1
- Updated to 0.9.4.1.

* Fri May 28 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.3-0.fdr.1
- Updated to 0.9.3.

* Wed Apr 07 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.2.1-0.fdr.2
- BuildReqs intltool & gettext (#1459).

* Tue Apr 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.2.1-0.fdr.1
- Updated to 0.9.2.1.

* Thu Dec 04 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.1-0.fdr.2
- Include translations.

* Sat Nov 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.1-0.fdr.1
- Updated to 0.9.1.

* Thu Oct 23 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.0-0.fdr.2
- Reuire pygtk2 >= 0:1.99.15.

* Sun Oct 12 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.0-0.fdr.1
- Updated to 0.9.0.

* Mon Sep 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.5-0.fdr.1
- Updated to 0.8.5.

* Wed Aug 13 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.4-0.fdr.3
- dropped tidyxml.py.

* Mon Aug 11 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.4-0.fdr.2
- Moved manual so the help feature will work.

* Thu Jul 31 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.4-0.fdr.1
- Updated to 0.8.4.
- now install files under %%{_datadir} rather than %%{_libdir}.

* Wed May 28 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.1-0.fdr.3
- Package now contains verifiable source.

* Tue May 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.1-0.fdr.2
- Cleaned out libdir/meld.
- fixed file permissions.

* Sun May 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.1-0.fdr.1
- Updated to 0.8.1.
- buildroot -> RPM_BUILD_ROOT.

* Wed Apr 16 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.7.1-0.fdr.1
- Updated to 0.7.1.

* Wed Apr 09 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.7.0-0.fdr.3
- Updated Requires.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.7.0-0.fdr.2
- Changed category to X-Fedora-Extra.
- Added desktop-file-utils to BuildRequires.
- Added missing Requires fields.
- Added Epoch:0.

* Thu Mar 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.7.0-0.fdr.1
- Initial RPM release.
