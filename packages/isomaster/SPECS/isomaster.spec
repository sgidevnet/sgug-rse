Name:		isomaster
Summary:	An easy to use GUI CD image editor
Version:	1.3.13
Release:	11%{?dist}
License:	GPLv2
URL:		http://littlesvr.ca/isomaster/
#moved to .rpmmacros
#Packager:	Marcin Zajaczkowski <mszpak ATT wp DOTT pl>
Source0:	http://littlesvr.ca/isomaster/releases/isomaster-%{version}.tar.bz2
Source1:	http://timeoff.wsisiz.edu.pl/rpms/isomaster/text-editor-0.1.tar.gz
#using %%{optflags}, patch updated to work with --fuzzy=0 (has beeing used in Rawhide since October 2008)
Patch0:		isomaster-1.3.13-optflags.diff
Patch1:		isomaster-1.3.6-desktop.diff
#to call viewers for the files
Requires:	xdg-utils
BuildRequires:	gcc
#author is not sure about gtk2 version, but 2.8 should be enough
BuildRequires:	gtk2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%description
ISO Master: an easy to use graphical CD image editor. 
It allows to extract files from an ISO, add files to an ISO, 
and create bootable ISOs - all in a graphical user interface.
It can open ISO, NRG, and some MDF files but can only save as ISO.

%prep
%setup -q
%setup -q -T -D -a 1
%patch0 -p0
%patch1 -p0

%build
#PREFIX is required to specify a correct dir for icons
make %{?_smp_mflags} PREFIX=%{_prefix} OPTFLAGS="%{optflags}" DEFAULT_VIEWER=xdg-open DEFAULT_EDITOR=text-editor.sh

%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
cp text-editor.sh %{buildroot}%{_bindir}/text-editor.sh

%find_lang %{name}

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
	-vendor fedora \
%endif
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	--add-category="Audio" \
	--add-category="Video" \
	%{buildroot}%{_datadir}/applications/isomaster.desktop

%files -f %{name}.lang
%attr(0755,root,root) %{_bindir}/isomaster
%attr(0755,root,root) %{_bindir}/text-editor.sh
%{_datadir}/%{name}
%doc CHANGELOG.TXT CREDITS.TXT LICENCE.TXT README.TXT TODO.TXT
%{_datadir}/applications/*isomaster.desktop
%{_mandir}/man1/isomaster.1*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.13-9
- Add gcc to BuildRequires - https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.13-1
- updated to 1.3.13

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.9-6
- Add Audio and Video to .desktop file.
- Date fixes.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.9-4
- Remove --vendor from desktop-file-install for F19+. https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.9-1
- updated to 1.3.9
- remove already applied upstream a patch for a problem with snprintf

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.7-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 05 2010 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.7-1
- updated to 1.3.7
- patched problem with snprintf and OPTFLAGS from Fedora
- workaround for a problem with bkisofs docs in a separate directory

* Sun Oct 18 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.6-1
- updated to 1.3.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 27 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.4-2
- fixed problem with old patch

* Sat Dec 27 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.4-1
- updated to 1.3.4

* Sun Oct 5 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.3-2
- fixed problem with building when --fuzzy=0 in patch command (#465088)

* Tue Jul 1 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.3-1
- updated to 1.3.3

* Sun Jun 29 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.2-1
- updated to 1.3.2

* Mon Feb 4 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3.1-1
- updated to 1.3.1

* Sat Feb 2 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3-2
- better MimeType support - #293482 (suggested by Ignacio Vazquez-Abrams)
- better desktop file installation support (suggested by Ignacio Vazquez-Abrams)

* Tue Dec 18 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3-1
- updated to 1.3

* Sat Dec 1 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.2-2
- Utility removed from Categories in .desktop file to prevent duplication in a menu

* Sat Oct 27 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.2-1
- updated to 1.2
- removed viewer-variable patch (merged with upstream)

* Wed Aug 29 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.1-2
- added text-editor.sh to find existing GUI text editor

* Wed Aug 29 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.1-1
- updated to 1.1
- a default viewer is called by xdg-open (from xdg-utils)

* Sat Aug 25 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0-2
- specified licence type (due to a new Licensing Guidelines)

* Sun Jun 10 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0-1
- updated to 1.0

* Mon Mar 19 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.8.1-1
 - updated to 0.8.1
 - removed unused patches (merged with upstream)
 - using desktop file from upstream

* Fri Jan 26 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.7-3
 - bumped to next release to workaround problem with FC-5 tag in CVS

* Wed Jan 17 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.7-2
 - removed deprecated Application category from a .desktop file
 - man page mapping changed to more universal

* Fri Jan 12 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.7-1
 - updated to 0.7
 - added locale files
 - added a manual page
 - adjusted %%{optflags} patch to a new Makefile
 - added patch to correct wrong dependencies which broke a parallel build
 - removed redundant deletion of builddir (--clean option in rpmbuild does the same)

* Mon Jan 8 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.6-6
 - applied suggestions from Michael Schwendt
 - menu category changed to "Application;Utility;"
 - added patch to use %%{optflags}

* Sat Dec 30 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.6-5
 - description broke down into 3 lines
 - gtk+ removed from Requires, because libgdk-x11-2.0.so.0 already forces it

* Sat Dec 30 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.6-4
 - isomaster.desktop in a non gzipped form
 - corrected path in a desktop file

* Fri Dec 29 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.6-3
 - applied suggestions from Michal Bentkowski (below)
 - fixed problem with remaining %%{_datadir}/%%{name} directory
 - desktop-file-utils moved to BuildRequires
 - removed minimal required version of GTK+
 - .desktop file available as an another source

* Fri Dec 29 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.6-2
 - started adaptation to Fedora Extras requirements
 - Packager tag removed from .spec file (now only in .rpmmacros)
 - gcc-c++ removed from BuildRequires section
 - vendor changed to "fedora"
 - minimal required version of GTK+ added

* Sun Dec 10 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.6-1
 - updated to 0.6
 - changed icons names

* Sun Oct 29 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.5-1
 - updated to 0.5

* Thu Sep 28 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.4-1
 - updated to 0.4
 - removed patch for Makefile (my suggestions was included in the original release)

* Tue Sep 26 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.3-2
 - tests with new Makefile

* Sun Sep 24 2006 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.3-1
 - initial release

