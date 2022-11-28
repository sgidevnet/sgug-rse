Name:           klavaro
Version:        3.11
Release:        1%{?dist}
Summary:        Typing tutor

License:        GPLv3+
URL:            http://klavaro.sourceforge.net/en/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-docutils
BuildRequires:  libcurl-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
Klavaro  is a touch typing tutor that is very flexible and supports 
customizable keyboard layouts. Users can edit and save new or unknown
keyboard layouts, as the basic course provided by the program was
designed to not depend on specific layouts.

%prep
%autosetup


%build
%configure --disable-rpath --enable-static=no
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|$(DATADIRNAME)|share|' data/Makefile.in

%make_build

%install
%make_install

# Adding folder for scores saving
mkdir -p %{buildroot}%{_localstatedir}/games/%{name}
%find_lang %{name}

rm %{buildroot}%{_libdir}/libgtkdataboks.la


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%attr(0755, root, games) %{_localstatedir}/games/%{name}
%{_mandir}/man*/*.*
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_libdir}/libgtkdataboks.*

%changelog
* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.11-1
- Update to 3.11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.10-1
- Update to 3.10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.09-2
- Switch to python3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.09-1
- Update to 3.09

* Mon Jun 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.08-1
- Update to 3.08

* Mon Jun 03 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.07-1
- Update to 3.07

* Fri Mar 22 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.05-3
- Fix segfault

* Tue Mar 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.05-2
- Correct databox library handling

* Sun Mar 17 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.05-1
- Update to 3.05

* Mon Feb 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.04-1
- Update to 3.04
- Clean spec and correct paths

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.03-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Vasiliy N. Glazov <vascom2@gmail.com> 3.03-5
- Update to 3.03

* Thu Jun 29 2017 Vasiliy N. Glazov <vascom2@gmail.com> 3.02-5
- Fix BR python naming

* Wed May 31 2017 Vasiliy N. Glazov <vascom2@gmail.com> 3.02-4
- Fix build (rhbz#1423817)

* Mon Apr 03 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.02-3
- Fix FTBFS (rhbz#1252792)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 3.02-1
- Update to latest upstream release 3.02

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Kalev Lember <klember@redhat.com> - 3.01-1
- Update to final 3.01 release
- Use license macro

* Sat Sep 19 2015 Kalev Lember <klember@redhat.com> - 3.01-0.pre1.1.2
- Fix linkage for internal libraries

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-0.pre1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 09 2014 Richard Hughes <richard@hughsie.com> - 3.01-0.pre1.1
- Update to a pre-release which includes an AppData file.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.00-1
- Updated to new upstream release 2.00

* Wed Sep 04 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.9-1
- Patch removed
- Updated to new upstream release 1.9.9

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.7-2
- Rebuilt (gtkdatabox)

* Sun Feb 24 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.7-1
- Updated to new upstream release 1.9.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 16 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.6-1
- Updated to new upstream release 1.9.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.5-1
- Updated to new upstream release 1.9.5

* Tue Feb 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.4-2
- Linking patch added

* Sat Feb 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.4-1
- Updated to new upstream release 1.9.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.3-1
- Updated to new upstream release 1.9.3

* Sat Apr 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Sun Mar 06 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.8.1-2
- Updated BR

* Sun Mar 06 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.8.1-1
- Updated to new upstream version 1.8.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 14 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.3-1
- Updated to new upstream version 1.7.3

* Sun Aug 29 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Updated to new upstream version 1.7.0

* Fri Aug 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Updated to new upstream version 1.6.0

* Sat Mar 06 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Removed DSO linking fix
- Updated to new upstream version 1.5.0

* Thu Feb 11 2010 Mathieu Bridon <bochecha@fedoraproject.org> - 1.4.1-2
- Rebuild against new gtkdatabox version
- Fix DSO-linking failure

* Tue Jan 05 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Updated to new upstream version 1.4.1

* Fri Dec 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- BR libsexy-devel removed
- Updated to new upstream version 1.4.0

* Mon Nov 16 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.6-1
- Updated to new upstream version 1.3.6

* Sun Oct 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.4-1
- Updated to new upstream version 1.3.4

* Mon Oct 05 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.3-1
- Updated to new upstream version 1.3.3

* Sun Aug 23 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Sun Aug 23 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-3
- Fixed license tag

* Mon Jul 13 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-2
- https://sourceforge.net/tracker/?func=detail&aid=2819484&group_id=135657&atid=733522
- Removed the changing of the permission of /usr/bin/klavaro_helper

* Fri Jul 10 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Updated BR
- .desktop file and icon are now in the source
- Updated to new upstream version 1.2.1

* Sat Apr 11 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.9-1
- Initial package for Fedora
