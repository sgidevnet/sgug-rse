Name:           treecc
Version:        0.3.8
Release:        25%{?dist}

Summary:        Tree Compiler Compiler

License:        GPLv2+
URL:            http://www.southern-storm.com.au/treecc.html
Source0:        http://www.southern-storm.com.au/download/treecc-0.3.8.tar.gz
Patch0:         treecc-0.3.8-texinfo5.patch

BuildRequires:  bison >= 1.28
BuildRequires:  flex >= 2.5.4
BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  texinfo

# ExcludeArch s390x to allow build on rawhide
ExcludeArch:    s390x

%description
The treecc program is designed to assist in the development of compilers
and other language-based tools.  It manages the generation of code to handle
abstract syntax trees and operations upon the trees.


%prep
%autosetup -p1


%build
%configure
%make_build

%check
make check

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -f $RPM_BUILD_ROOT/%{_libdir}/libtreecc.a

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*


%changelog
* Mon Jul 29 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.8-25
- Fix FTBFS on rawhide + spec cleanup and modernization

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3.8-14
- Fix FTBFS (#1107463)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0.3.8-5
- Rebuilt for gcc43

* Thu Aug 23 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.3.8-4
- new license tag
- rebuild for buildid

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.3.8-3
- FE6 rebuild

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.3.8-2
- Rebuild for Fedora Extras 5

* Thu Jan 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.3.8-1
- same spec for all arches hence add dist
- upgrade to new version

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.3.4-4
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Feb 20 2005 David Woodhouse <dwmw2@infradead.org> 0.3.4-2
- Don't package %%{_infodir}/dir

* Fri Nov 26 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.3.4-1
- 0.3.4.

* Sat Nov 13 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.3.2-0.fdr.2
- Clean up spec/Bump release.

* Sun Aug 08 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.3.2-0.fdr.1
- Update to 0.3.2.

* Mon Mar 15 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.3.0-0.fdr.1
- Update to 0.3.0.
- Add make check.

* Sat Nov 15 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.2.6-0.fdr.4
- BuildReq m4.

* Sun Sep 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.2.6-0.fdr.3
- removed aesthetic comments.
- brought spec more in line with current template.

* Thu Jul 24 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.2.6-0.fdr.2
- BuildReq texinfo.
- Req(post,preun) info.
- Changed URL.

* Fri Jul 18 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.2.6-0.fdr.1
- Updated to 0.2.6.
- Removed INSTALL from doc.
- buildroot -> RPM_BUILD_ROOT.
- Correctd Group.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.2.4-0.fdr.2
- Added Epoch:0.
- Removed ldconfig from post and postun.

* Sat Mar 29 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.2.4-0.fdr.1
- Updated to 0.2.4.

* Mon Mar 24 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.2.2-0.fdr.2
- Cleaned up for Fedora.

* Sat Mar 08 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.2.2-0.fdr.1
- Spec cleanup.

* Thu Feb 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.2.2-1.fedora.2
- Spec cleanup.

* Fri Feb 07 2003  Phillip Compton
- Initial build.
