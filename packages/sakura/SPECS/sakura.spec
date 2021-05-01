# Review at https://bugzilla.redhat.com/show_bug.cgi?id=496166

Name:           sakura
Version:        3.7.1
Release:        1%{?dist}
Summary:        Terminal emulator based on GTK and VTE

License:        GPLv2
URL:            https://launchpad.net/sakura
Source0:        https://launchpad.net/sakura/trunk/%{version}/+download/sakura-%{version}.tar.bz2
Patch0:         0001-Add-Keywords-field-to-desktop-file.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0) >= 2.20
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vte291-devel
BuildRequires:  cmake desktop-file-utils gettext /usr/sgug/bin/pod2man
BuildRequires:  pcre2-devel

%description
Sakura is a terminal emulator based on GTK and VTE. It's a terminal emulator 
with few dependencies, so you don't need a full GNOME desktop installed to 
have a decent terminal emulator.


%prep
%autosetup -p1


%build
find . -type f -name CMakeCache.txt -exec rm -rf {} \;
%cmake CMAKE_C_FLAGS="%{optflags}" .
%make_build


%install
%make_install
desktop-file-install \
  --delete-original \
  --remove-category=Utility \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
# location of the docs is hardcoded, so we remove them
rm -rf %{buildroot}%{_datadir}/doc/


%check
ctest .


%files -f %{name}.lang
%doc AUTHORS
%license GPL
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/terminal-tango.svg
%{_mandir}/man1/%{name}.1.*


%changelog
* Mon May 18 2020 Filipe Rosset <rosset.filipe@gmail.com> - 3.7.1-1
- Update to 3.7.1 fixes rhbz#1832482

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.7.0-1
- Update to 3.7.0 fixes rhbz#1742694 (removed upstreamed patch)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 14 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.6.0-4
- add patches from debian, fixes rhbz #1641276 and rhbz #1698150

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.6.0-2
- update to latest release 3.6.0 fixes rhbz #1574279

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.5.0-1
- update to latest release 3.5.0 fixes rhbz #1246303 #1475609 and #1409379
- spec cleanup + silent rpmlint

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Christoph Wickert <cwickert@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0 (#1173077)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.5-1
- Update to 3.1.5 (#1112288)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 18 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3 (#1034129)

* Mon Nov 25 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1 (#1034129, fixes FTBFS #993220)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Mon Feb 18 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.4-3
- Use upsteam patch instead of hack to fix #861451
- BR /usr/bin/pod2man for manpage generation
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.4-2
- Build with %%{optflags} (#861451)

* Thu Sep 27 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4 (#860958)
- Build against GTK3 and VTE3
- Change website and source URL to new location at launchpad.net

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.4.2-2
- Rebuild for new libpng

* Sat Jul 30 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.2-1
- Update tp 2.4.2
- Fixes #722686, so remove the patch

* Sun Jul 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.1-3
- Bring back the cflags patch as actually this is not fixed (#722793)

* Sat Jul 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.1-2
- Fix crash in  (#722686)
- Remove cflags patch, fixed upstream
- Remove sed hack for pod2man now that it does understand the -u option
- Remove fix for the icon in the desktop file as it's now upstream, too

* Sat Jul 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1 (fixes #713822)

* Sat Feb 12 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.8-1
- Update to 2.3.8

* Wed Apr 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.7-1
- Update to 2.3.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.3-3
- Rebuilt for libvte SONAME bump

* Sun Apr 19 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.3-2
- Add patch to honor RPM_OPT_FLAGS
- Include INSTALL in %%doc since it contains some valuable information

* Sat Apr 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Tue Nov 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Sat Nov 01 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Sun Sep 28 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sun Sep 21 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- Disable %%check again

* Fri Jun 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Enable %%check again

* Fri Jun 06 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2
- No test configuration, disable %%check temporarily 

* Mon May 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Mon May 05 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.0.2-1
- Initial Fedora RPM
