Name:           frotz
Version:        2.44
Release:        3%{?dist}
Summary:        Interactive fiction interpreter for Z-Machine (Infocom) games

License:        GPLv2+
URL:            https://gitlab.com/DavidGriffith/frotz/
Source0:        https://gitlab.com/DavidGriffith/frotz/-/archive/%{version}/frotz-%{version}.tar.gz

Patch0:         frotz.sgifixes.patch

BuildRequires:  gcc
#BuildRequires:  pkgconfig(ao)
#BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(ncursesw)
#BuildRequires:  pkgconfig(samplerate)
#BuildRequires:  pkgconfig(sndfile)
#BuildRequires:  pkgconfig(vorbisfile)

# For sfrotz
#BuildRequires:  pkgconfig(bzip2)
#BuildRequires:  pkgconfig(freetype2)
#BuildRequires:  pkgconfig(libpng)
#BuildRequires:  pkgconfig(libjpeg)
#BuildRequires:  pkgconfig(sdl2)
#BuildRequires:  pkgconfig(SDL2_mixer)
#BuildRequires:  pkgconfig(zlib)

%global _description\
Frotz is an interpreter for Infocom games and other Z-machine games.  It\
complies with standard 1.0 of Graham Nelson's specification.\
\
Free Z-machine game file downloads, as well as more information about\
Infocom, Z-machine games, and interactive fiction can be found at the\
Interactive Fiction Archive, http://mirror.ifarchive.org/.

%description %_description


#%package gui
#Summary: SDL GUI for frotz interactive fiction interpreter
#Requires: %{name}%{?_isa} = %{version}-%{release}
#
#%description gui
#%_description
#
#This package contains the sfrotz GUI.

%prep
%autosetup -p1

# Rewrite installation libdir
perl -pi -e "s|INSTALLDIR\)/lib|INSTALLDIR\)/%{_lib}|g" Makefile

%build
export CPPFLAGS="-I%{_includedir}"
export CC=gcc
export CXX=g++
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="-L%{_libdir} $RPM_LD_FLAGS"
export RANLIB="/bin/true"
export INSTALLDIR=%{_prefix}
#%%make_build all
make %{?_smp_mflags} curses

%install
make curses install PREFIX=%{buildroot}%{_prefix}

# Make a version of the config file with all settings commented out,
# to install in /etc
sed -Ee '/(^#|^$)/! s/^/#/' < doc/frotz.conf-big > frotz.conf
install -m0644 -D frotz.conf -t %{buildroot}%{_sysconfdir}

# Move manpages into correct place
mkdir -p $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_prefix}/man/* $RPM_BUILD_ROOT%{_mandir}/

%files
%doc AUTHORS ChangeLog DUMB HOW_TO_PLAY README TODO
%license COPYING
%doc doc/frotz.conf*
%{_bindir}/frotz
#%%{_bindir}/dfrotz
%{_mandir}/man6/frotz.6*
#%%{_mandir}/man6/dfrotz.6*
%config(noreplace) %{_sysconfdir}/frotz.conf

#%%files gui
#%%{_bindir}/sfrotz
#%%{_mandir}/man6/sfrotz.6*


%changelog
* Sub Apr 26 2020 Daniel Hams <daniel.hams@gmail.com> - 2.51-3
- Fix manpath

* Wed Feb 12 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.51-2
- Incorporate changes to upstream release

* Wed Feb 12 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.51-1
- New upstream release
- Drop upstreamed patches, adapt to changes to Makefile path handling

* Sat Feb 01 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.50-3
- Add patch to fix GCC 10 compilation failures

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.50-1
- Update to latest 2.50 release, new gitlab upstream
- Split out SDL interface into separate -gui subpackage

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.43-18
- Use '|' instead of '/' as pattern-delimiter in sed expression to filter
  CFLAGS (Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.43-7
- Autorebuild for GCC 4.3

* Wed Oct 31 2007 Chris Grau <chris@chrisgrau.com> 2.43-6
- Fixed license tag.

* Thu Sep 14 2006 Chris Grau <chris@chrisgrau.com> 2.43-5
- Rebuild for FC-6.

* Wed Mar 01 2006 Chris Grau <chris@chrisgrau.com> 2.43-4
- Rebuild for FC-5.

* Tue Jul 19 2005 Chris Grau <chris@chrisgrau.com> 2.43-3
- Changed sed command to edit Makefile in place (Michael Schwendt).
- Removed compression of the man page (Michael Schwendt).

* Tue Jul 19 2005 Chris Grau <chris@chrisgrau.com> 2.43-2
- Split up patch files.
- Added a pointer to the IF archive to the %%description.

* Thu Jul 07 2005 Chris Grau <chris@chrisgrau.com> 2.43-1
- Initial build.
