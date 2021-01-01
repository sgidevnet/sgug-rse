Name:		SDL_ttf
Version:	2.0.11
Release:	17%{?dist}
Summary:	Simple DirectMedia Layer TrueType Font library

License:	zlib
URL:		http://www.libsdl.org/projects/SDL_ttf/
Source0:	http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz

Patch0:		SDL_ttf.sgifixes.patch

BuildRequires:  gcc
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	zlib-devel


%description
This library allows you to use TrueType fonts to render text in SDL
applications.


%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.4


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



#%ldconfig_scriptlets


%files
%doc README CHANGES COPYING
%{_libdir}/lib*.so.*


%files devel
%{_libdir}/*.so
%{_includedir}/SDL/
%{_libdir}/pkgconfig/SDL_ttf.pc

%changelog
* Thu Dec 31 2020 Julien Maerten <julien@3dw.org> - 2.0.11-17
- Fix autoconf for building on Irix

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.11-15
- License tag fix.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.11-1
- New upstream.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 12 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.0.10-1
- update to 2.0.10
- fixes #538044

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-4
- Rebuild for gcc-4.3.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-3
- Rebuild.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-2
- Update license tag.

* Mon Jul 30 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9.
- Drop freetype-internals patch. fixed upstream.

* Thu Aug 31 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0.8-2
- Update for FC6.

* Sat Aug 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8.
- Simplify description & summary for devel package.

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.7-4
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Dec 14 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.7-3
- Add patch for Bug #171020.

* Thu Sep 29 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.7-2
- General spec formatting changes.
- Rebuild for FC4 upgrade path.

* Sun Sep 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.0.7-1
- 2.0.7, patches applied upstream.
- Require SDL-devel in -devel.
- Build with dependency tracking disabled.
- Don't ship static libs.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.0.6-5
- rebuilt

* Wed Mar 21 2004 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.4
- fix build on FC2-test (bug #1436

* Mon Nov 10 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.3
- add missing buildreq zlib-devel

* Sun Aug 24 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.2
- address issues in #631
- add full URL to source
- better description for -devel package

* Sat Aug 23 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.1
- Fedoraize
- patch to compile on RH9

* Wed Jan 19 2000 Sam Lantinga
- converted to get package information from configure
* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file

