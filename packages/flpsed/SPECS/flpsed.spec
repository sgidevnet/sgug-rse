Name:          flpsed
Version:       0.7.3
Release:       11%{?dist}
Summary:       WYSIWYG pseudo PostScript editor

License:       GPL+
URL:           http://flpsed.org/flpsed.html
Source0:       http://flpsed.org/%{name}-%{version}.tar.gz
Source1:       flpsed.desktop

BuildRequires:  gcc-c++
BuildRequires: fltk-devel
BuildRequires: desktop-file-utils
Requires:      ghostscript

%description
Flpsed is a WYSIWYG pseudo PostScript editor. "Pseudo", because you can't
remove or modify existing elements of a document. Flpsed lets you add
arbitrary text lines to existing PostScript 1 documents. Added lines can later
be reedited with flpsed. Using pdftops, which is part of xpdf, one can convert
PDF documents to PostScript and also add text to them. flpsed is useful for
filling in forms, adding notes etc.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files

%doc AUTHORS NEWS README ChangeLog INSTALL
%license COPYING 
%{_bindir}/*
%{_datadir}/applications/*
%{_mandir}/man1/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Luis Bazán <lbazan@fedoraproject.org> - 0.7.3-3
- fix COPYING file to correct path

* Sun Aug 16 2015 Luis Bazán <lbazan@fedoraproject.org> - 0.7.3-2
- fix bug #1247059

* Mon Jul 27 2015 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.3-1
- Rebuilt for new upstream version 0.7.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.7.2-5
- rebuild (fltk)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.2-2
- Rebuilt to fix FBTFS in rawhide, spec cleanup, fixes rhbz #1037065

* Thu Feb 06 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.7.2-1
- new upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-5
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Luis Bazan <bazanluis20@gmail.com> -0.7.0-1
- New Upstream

* Wed Jun 15 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5.2-3
- Rebuild for fltk-1.3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 29 2009 Stepan Kasal <skasal@redhat.com> - 0.5.2-1
- new upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Nicholas Boyle <nsboyle@gmail.com> - 0.5.0-4
-Rebuild for GCC 4.3

* Wed Sep 05 2007 Nicholas Boyle <nsboyle@gmail.com> - 0.5.0-3
-Corrected license version to match source
-Added dependency for ghostscript
-Built files are now globbed, rather than specified explicitly by name

* Mon Aug 20 2007 Nicholas Boyle <nsboyle@gmail.com> - 0.5.0-2
- Added flpsed.desktop
- Specified GPL license version
- Changed buildroot to be more Fedora compliant
- Removed generic INSTALL from installed docs list

* Sat Aug 11 2007 Nicholas Boyle <nsboyle@gmail.com> - 0.5.0-1
- Initial Fedora packaging
