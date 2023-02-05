Name:           gnome-epub-thumbnailer
Version:        1.6
Release:        1%{?dist}
Summary:        Thumbnailers for EPub and MOBI books

License:        GPLv2+
URL:            https://git.gnome.org/browse/gnome-epub-thumbnailer
Source0:        http://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
Buildrequires:  pkgconfig(libarchive)

%description
Thumbnailers for EPub and MOBI books


%prep
%setup -q
%autopatch


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install


%files
%{_bindir}/gnome-epub-thumbnailer
%{_bindir}/gnome-mobi-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gnome-epub-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-mobi-thumbnailer.thumbnailer
%doc AUTHORS COPYING NEWS README



%changelog
* Wed Oct 30 2019 Yanko Kaneti <yaneti@declera.com> - 1.6-1
- Update to 1.6
- Adds support for SVG covers in ePub 3.0 files
- Adds support for Kindle Format 8 MOBI files

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Yanko Kaneti <yaneti@declera.com> - 1.5-1
- Update to 1.5. Drop patches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Yanko Kaneti <yaneti@declera.com> - 1.4-3
- Pick couple uptream fixes. Should help avoid RHBZ 1103325

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Yanko Kaneti <yaneti@declera.com> - 1.4-1
- Update to 1.4. Drop upstream patches.

* Thu Jan 16 2014 Yanko Kaneti <yaneti@declera.com> - 1.3-4
- Yet another crash fix from upstream

* Mon Jan  6 2014 Yanko Kaneti <yaneti@declera.com> - 1.3-3
- Fix crashes on thumbnailing trash/recent files - #1046245
- Get unencrypted cover from otherwise encrypted mobi files

* Sun Oct 27 2013 Yanko Kaneti <yaneti@declera.com> - 1.3-2
- Don't crash on failure to find a cover file - #1001559

* Thu Aug  8 2013 Yanko Kaneti <yaneti@declera.com> - 1.3-1
- New upstream release fixing a number of possible crashers
  in the MOBI thumbnailer

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Yanko Kaneti <yaneti@declera.com> - 1.2-1
- New upstream release adding a MOBI thumbnailer

* Wed Jul 17 2013 Yanko Kaneti <yaneti@declera.com> - 1.1-1
- New upstream release fixing possible crashes or
  excessive warnings on failure

* Tue Jul 16 2013 Yanko Kaneti <yaneti@declera.com> - 1.0-1
- Initial packaging
