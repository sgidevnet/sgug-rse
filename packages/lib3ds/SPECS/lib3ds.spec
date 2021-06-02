Name:           lib3ds
Version:        1.3.0
Release:        30%{?dist}

Summary:        3D Studio file format library

License:        LGPLv2+
URL:            http://lib3ds.sourceforge.net
Source:         http://downloads.sourceforge.net/lib3ds/lib3ds-%{version}.zip
# Extracted from Debian's lib3ds_1.3.0-1.diff.gz
Patch0:         lib3ds-1.3.0-lib3ds-file.h.diff
# Address https://bugzilla.redhat.com/show_bug.cgi?id=633475
Patch1:         lib3ds-1.3.0-lib3ds-mesh.c.diff

Patch2:         lib3ds-1.2.0-pkgconfig.diff

Patch3:         lib3ds-1.3.0-config.patch

BuildRequires:  gcc

%description
lib3ds is a free ANSI-C library for working with the popular "3ds" 3D model
format.

Supported platforms include GNU (autoconf, automake, libtool, make, GCC) on
Unix and Cygwin, and MS Visual C++ 6.0. lib3ds loads and saves Atmosphere
settings, Background settings, Shadow map settings, Viewport setting,
Materials, Cameras, Lights, Meshes, Hierarchy, Animation keyframes. It also
contains useful matrix, vector and quaternion mathematics tools. lib3ds
usually integrates well with OpenGL. In addition, some diagnostic and
conversion tools are included.

%package        tools
Summary:        %summary

%description    tools
Some tools to process 3ds files.

%files          tools
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/3dsdump
%{_mandir}/man1/3dsdump.1*

%package        devel
Summary:        %summary
Requires:	pkgconfig
Requires:	lib3ds = %{version}-%{release}

%description    devel
Development files for lib3ds


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%configure  --disable-static

make %{?_smp_mflags}

sed -e 's,@prefix@,%{_prefix},' \
  -e 's,@exec_prefix@,%{_exec_prefix},' \
  -e 's,@libdir@,%{_libdir},' \
  -e 's,@includedir@,%{_includedir},' \
  -e 's,@VERSION@,%{version},' \
  lib3ds.pc.in > lib3ds.pc

%install
make install DESTDIR=$RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
install lib3ds.pc -m 0644 ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig

## Remove libtool archive
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*

%ldconfig_scriptlets


%files devel
%{_bindir}/lib3ds-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib3ds.pc
%{_mandir}/man1/lib3ds-config.1*
%{_includedir}/lib3ds
%{_datadir}/aclocal/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-28
- Add BR: gcc.
- Spec cleanup.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-21
- Remove %%defattr, add %%license to *-tools.

* Tue Jan 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-20
- Remove %%defattr.
- Add %%license.
- Fix bogus %%changelog entries.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-15
- Add lib3ds-1.3.0-config.patch (Allow building on aarch64; RHBZ #925660).
- Modernize spec.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.3.0-10
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-9
- Address https://bugzilla.redhat.com/show_bug.cgi?id=633475 (CVE-2010-0280).
- Adopt Debian patch to add missing decl.

* Tue May 11 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-8
- Adopt EPEL spec cleanup.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-5
- Fix silly typo in previous change.

* Wed Sep 24 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.0-4
- Work around rpmbuild having stopped supporting %%patch -P N.

* Mon Jul  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.0-3
- fix conditional comparison

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.3.0-2
- Rebuild for gcc43.

* Sat Nov 03 2007 Ralf Corsépius <rc040203@freenet.de> - 1.3.0-1
- Cleanup spec.
- Add post/postun.
- Re-add 3ds2m for fedora < 9.
- Abandon *-static for fedora >= 9.

* Fri Nov 02 2007 Xavier Lamien <lxtnow[at]gmail.com> - 1.3.0
- Updated Release.

* Sun Oct 21 2007 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-13
- Address BZ 341851:
  - Add lib3ds.pc.
  - Rework lib3ds-config to using lib3ds.pc.
  - Add lib3ds-1.2.0-pkgconfig.diff

* Sat Oct 20 2007 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-12
- Change Source: to using downloads.sourceforge.net.

* Sat Aug 18 2007 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-11
- Update license tag.

* Tue Nov 14 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-10
- Add Provides: *-static.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-9
- Mass rebuild.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-8
- Mass rebuild.

* Tue Feb 28 2006 Ralf Corsepius <rc040203@freenet.de> - 1.2.0-7
- Rebuild.

* Thu Jan 05 2006 Ralf Corsepius <rc040203@freenet.de> - 1.2.0-6
- PR 176665: Apply upstream patch.
- Add %%dist.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.2.0-5
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Aug 09 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 0:1.2.0-0.fdr.3
- Fix m4-underquoting in lib3d.m4.

* Wed Jul 14 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 0:1.2.0-0.fdr.2
- Split out tools into separate subpackage "tools".
- Fix description's formating.

* Thu Jul 08 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 0:1.2.0-0.fdr.1
- Initial RPM release.
