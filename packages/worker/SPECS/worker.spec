Name:		worker
Version:	4.4.0
Release:	3%{?dist}
Summary:	File Manager for the X11

License:	GPLv2+
URL:		http://boomerangsworld.de/worker
Source0:	http://boomerangsworld.de/cms/%{name}/downloads/%{name}-%{version}.tar.bz2
#Patch0:		Patch0-Fix-For-Python3.patch
Patch100:       worker.sgifixes.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	libX11-devel
BuildRequires:  avfs

%description
A X11 file-manager that features low requirements and easy to access archives.
i
%prep
%autosetup -p1

#Fix Man pages(UTF-8)
for f in ChangeLog man/fr/worker.1 man/it/worker.1; do
	iconv -f ISO-8859-1 -t UTF-8 $f > $f.new && \
	touch -r $f $f.new && \
	mv $f.new $f
done

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LDFLAGS="$RPM_LD_FLAGS -ldicl-0.1"
%configure --without-dbus
%make_build

%install
%make_install

desktop-file-install	\
--delete-original	\
--dir=%{buildroot}%{_datadir}/applications	\
--remove-category="FileManager"		\
--add-category="System;FileTools"	\
%{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS ChangeLog THANKS
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/WorkerIcon*.xpm
%{_mandir}/man1/%{name}.1*
%{_mandir}/*/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/%{name}


%changelog
* Fri Dec 24 2021 SGI User Group <> - 4.4.0-3
- added AVFS library support

* Tue Jul 07 2020  HAL <notes2@gmx.de> - 4.4.0-1
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Sun Apr 12 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.4.0-1
- Update to 4.4.0 fixes rhbz#1823214

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.3.0-1
- Update to 4.3.0 fixes rhbz#1795070

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.2.0-1
- Update to 4.2.0 fixes rhbz#1786790

* Sat Sep 21 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.1.0-1
- Update to 4.1.0 fixes rhbz#1750969

* Mon Aug 05 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.1-1
- Update to 4.0.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-1
- Rebuilt for new upstream version 4.0.0 fixes rhbz #1723206

* Sun Apr 07 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.4-1
- Rebuilt for new upstream version 3.15.4 fixes rhbz #1670216 and #1676217

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.2-1
- Rebuilt for new upstream version 3.15.2 fixes rhbz #1579346 and #1606703

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.0-3
- added gcc as BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.0-1
- Rebuilt for new upstream version 3.15.0 fixes rhbz #1491078

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 3.11.0-1
- Rebuilt for new upstream version 3.11.0 fixes rhbz #1473062

* Tue Jun 13 2017 Filipe Rosset <rosset.filipe@gmail.com> - 3.10.0-2
- Rebuilt for new upstream version 3.10.0 fixes rhbz #1460412

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Apr 22 2017 Filipe Rosset <rosset.filipe@gmail.com> - 3.9.0-1
- Rebuilt for new upstream version 3.9.0 fixes rhbz #1091751
- Fixes FTBFS in rawhide rhbz #1424545 + spec clean up

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.3.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Nathan Owe <ndowens at fedoraproject.org 3.3.3-1
 - Updated package to latest available

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 08 2012 Nathan Owe <ndowens at fedoraproject.org> 2.19.2-1
- Updated version

* Sat Feb 25 2012 Nathan Owe <ndowens at fedoraproject.org> 2.19.1-1
- Updated version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Nathan Owe <ndowens at fedoraproject.org> 2.18.1-1
- Updated to newest version

* Wed Aug 17 2011 Nathan Owe <ndowens at fedoraproject.org> 2.18.0-7
- Fixed defattr typo

* Tue Jul 26 2011 Nathan Owe <ndowens at fedoraproject.org> 2.18.0-6
- Changed email address
- Added 'BuildRoot' for EPEL compatability
- Added defattr and clean section for EPEL

* Tue Jul 19 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-5
- Convert Changelog to UTF-8

* Tue Jul 19 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-4
- Convert Man pages to UTF-8

* Mon Jul 18 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-3
- Fixed Directory Permission problem

* Mon Jul 18 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-2
- Removed Requires

* Sat Jul 16 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-1
- Inital Release
