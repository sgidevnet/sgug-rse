Name:       icebreaker
Version:    2.2.1
Release:    1
Summary:    An addictive action-puzzle game involving bouncing penguins
%define     isprerelease 0
%define     isdevelrelease 0
License:    GPLv2+

%if %{isprerelease}
Source:     icebreaker-%{version}-%{release}.tar.xz
%else
Source:     https://mattdm.org/icebreaker/2.1.x/icebreaker-%{version}.tar.xz
%endif

URL:        http://www.mattdm.org/icebreaker/

BuildRequires:  gcc, make
BuildRequires:  SDL-devel, SDL_mixer-devel
BuildRequires:  gawk, sed, grep
BuildRequires:  desktop-file-utils

%if %{isprerelease}
%define extradescription *** Warning *** This is a prerelease build not meant for general public use.
%elseif %{isdevelrelease}
%define extradescription NOTE: This is a development release. Bug-testers only, please.
%endif

%description
IceBreaker is an action-puzzle game in which you must capture penguins from
an Antarctic iceberg so they can be shipped to Finland, where they are
essential to a secret plot for world domination. To earn the highest Geek
Cred, trap them in the smallest space in the shortest time while losing the
fewest lives. IceBreaker was inspired by (but is far from an exact clone of)
Jezzball by Dima Pavlovsky.
%{extradescription}

%prep
%if %{isprerelease}
%setup -q -n %{name}-%{version}-%{release}
%else
%setup -q
%endif

%build
make OPTIMIZE="$RPM_OPT_FLAGS" prefix=%{_prefix}

%install
make install prefix=${RPM_BUILD_ROOT}%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications icebreaker.desktop
mkdir ${RPM_BUILD_ROOT}%{_datadir}/metainfo
cp metainfo.xml ${RPM_BUILD_ROOT}%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml

%files
%license LICENSE
%doc README README.themes TODO ChangeLog
%{_bindir}/icebreaker
%{_datadir}/applications/icebreaker.desktop
%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml
%{_datadir}/icebreaker
%{_mandir}/man6/*


%changelog
* Sun Oct  2 2021 Matthew Miller <mattdm@mattdm.org> - 2.2.1-1
- minor build improvements via PR from reinerh

* Mon Mar  1 2021 Matthew Miller <mattdm@mattdm.org> - 2.2.0-1[A
- made Windows work so I'm going to call this 2.2

* Mon Mar  1 2021 Matthew Miller <mattdm@mattdm.org> - 2.1.3-1
- fix metainfo oops

* Mon Mar  1 2021 Matthew Miller <mattdm@mattdm.org> - 2.1.2-1
- update metainfo for GNOME Software

* Tue Feb 23 2021 Matthew Miller <mattdm@mattdm.org> - 2.1.1-1
- update to 2.1.1 to fix some more buffer overflows

* Wed Sep  2 2020 Matthew Miller <mattdm@mattdm.org> - 2.1.0-1
- update to 2.1
- include metainfo

* Sun Aug 30 2020 Matthew Miller <mattdm@mattdm.org> - 2.0.2-1
- minor tweaks

* Sun Aug 30 2020 Matthew Miller <mattdm@mattdm.org> - 2.0.0-1
- high scores are going to be local to each home directory; no more setgid
- update to 2.0.0

* Thu Nov 16 2006 Matthew Miller <mattdm@mattdm.org>
- working towards 1.9.9 :)

* Fri May 31 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.6

* Mon May 27 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.5

* Thu May 23 2002 Matthew Miller <mattdm@mattdm.org>
- more complex makefile allows simpler specfile

* Tue May 21 2002 Matthew Miller <mattdm@mattdm.org>
- added themes docs

* Sun May 19 2002 Matthew Miller <mattdm@mattdm.org>
- inserted some convenience stuff to enable "make rpm" magic to work
- added "isprerelease" check. No one but me should care about this.

* Sun May 19 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.2

* Fri May 17 2002 Matthew Miller <mattdm@mattdm.org>
- REALLY add .ibt files for themes

* Mon May 13 2002 Matthew Miller <mattdm@mattdm.org>
- add .ibt files for themes

* Wed May 08 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.1

* Wed Aug 01 2001 Matthew Miller <mattdm@mattdm.org>
- 1.9.0

* Mon Jul 30 2001 Matthew Miller <mattdm@mattdm.org>
- 1.2.1

* Sat Jul 28 2001 Matthew Miller <mattdm@mattdm.org>
- 1.2

* Tue Jul 24 2001 Matthew Miller <mattdm@mattdm.org>
- move man page section 6

* Sun Jul 22 2001 Matthew Miller <mattdm@mattdm.org>
- 1.1

* Fri Jul 20 2001 Matthew Miller <mattdm@mattdm.org>
- borrowed idea of using post-script to create high score file
  from Mandrake RPM. That way, it doesn't have to be marked as a config
  file, and yet won't get zapped on upgrade.
- also, modified Makefile to cope with RPM_OPT_FLAGS, again as per
  Mandrake.

* Thu Jul 19 2001 Matthew Miller <mattdm@mattdm.org>
- added man page

* Tue Jul 18 2001 Matthew Miller <mattdm@mattdm.org>
- updated to 1.09

* Thu Oct 5 2000 Matthew Miller <mattdm@mattdm.org>
- looks good to me. one-point-oh

* Tue Oct 3 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.995 
- better make process

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.99 :)

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.98

* Fri Sep 15 2000 Matthew Miller <mattdm@mattdm.org>
- first package
