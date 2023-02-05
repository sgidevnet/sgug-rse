%{!?ruby_vendorlibdir: %global ruby_vendorlibdir %(ruby -r rbconfig -e 'print RbConfig::CONFIG["vendorlibdir"]')}
%{!?ruby_vendorarchdir: %global ruby_vendorarchdir %(ruby -r rbconfig -e 'print RbConfig::CONFIG["vendorarchdir"]')}

%define beta beta19

Summary: Library for Colour AsCii Art, text mode graphics
Name: libcaca
Version: 0.99
Release: 0.42.%{beta}%{?dist}
License: WTFPL
URL: http://caca.zoy.org/wiki/libcaca
Source: http://caca.zoy.org/files/libcaca/libcaca-%{version}.%{beta}.tar.gz
#Patch0: libcaca-0.99.beta16-multilib.patch
BuildRequires: gcc-c++
BuildRequires: slang-devel
BuildRequires: ncurses-devel
BuildRequires: libX11-devel
#BuildRequires: glut-devel
#BuildRequires: libGLU-devel
BuildRequires: imlib2-devel
BuildRequires: pango-devel
# For the docs
#Buildrequires: doxygen
#Buildrequires: texlive-latex
#Buildrequires: texlive-dvips

%description
libcaca is the Colour AsCii Art library. It provides high level functions
for color text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.


%package devel
Summary: Development files for libcaca, the library for Colour AsCii Art
Requires: %{name} = %{version}-%{release}
Requires: slang-devel
Requires: ncurses-devel
Requires: libX11-devel
#Requires: glut-devel
#Requires: libGLU-devel
Requires: imlib2-devel
Requires: pango-devel

%description devel
libcaca is the Colour AsCii Art library. It provides high level functions
for color text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

This package contains the header files and static libraries needed to
compile applications or shared objects that use libcaca.


%package -n caca-utils
Summary: Colour AsCii Art Text mode graphics utilities based on libcaca

%description -n caca-utils
This package contains utilities and demonstration programs for libcaca, the
Colour AsCii Art library.

cacaview is a simple image viewer for the terminal. It opens most image
formats such as JPEG, PNG, GIF etc. and renders them on the terminal using
ASCII art. The user can zoom and scroll the image, set the dithering method
or enable anti-aliasing.

cacaball is a tiny graphic program that renders animated ASCII metaballs on
the screen, cacafire is a port of AALib's aafire and displays burning ASCII
art flames, and cacademo is a simple application that shows the libcaca
rendering features such as line and ellipses drawing, triangle filling and
sprite blitting.


%package -n python3-caca
Summary: Python bindings for libcaca
BuildRequires: python3-devel

%description -n python3-caca
This package contains the python bindings for using libcaca from python.


#%%package -n ruby-caca
#Summary: Ruby bindings for libcaca
#Requires: ruby(release)
#BuildRequires: ruby, ruby-devel
#Provides: ruby(caca) = %{version}-%{release}

#%%description -n ruby-caca
#This package contains the ruby bindings for using libcaca from ruby.


%prep
%setup -q -n libcaca-%{version}.%{beta}
#%%patch0 -p1 -b .multilib
for file in python/examples/*.py; do
  sed -e 's|/usr/bin/env python$|%{__python3}|g' ${file} > ${file}.tmp
  touch -r ${file} ${file}.tmp
  mv -f ${file}.tmp ${file}
done

%build
export LDFLAGS="$(pkg-config --libs gio-2.0) $LDFLAGS"

sed -i -e 's|Config::CONFIG\["sitearchdir"\]|Config::CONFIG["vendorarchdir"]|' \
       -e 's|Config::CONFIG\["sitelibdir"\]|Config::CONFIG["vendorlibdir"]|' \
       -e "s|rbconfig -e 'print Config|rbconfig -e 'print RbConfig|g" \
  configure
%configure \
  --disable-static \
  --disable-csharp \
  --disable-java
# Remove useless rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf %{buildroot} libcaca-dev-docs
make install DESTDIR=%{buildroot}
# We want to include the docs ourselves from the source directory
#mv %{buildroot}%{_docdir}/libcaca-dev libcaca-dev-docs
# Remove symlink to libcaca-dev
rm -f %{buildroot}%{_docdir}/libcucul-dev



#%%ldconfig_scriptlets


%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
#%%doc ChangeLog libcaca-dev-docs/html/
%{_bindir}/caca-config
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man1/caca-config.1*
#%%{_mandir}/man3/*

%files -n caca-utils
%doc AUTHORS COPYING* NEWS NOTES README THANKS
%{_bindir}/cacademo
%{_bindir}/cacafire
%{_bindir}/cacaclock
%{_bindir}/cacaplay
%{_bindir}/cacaserver
%{_bindir}/cacaview
%{_bindir}/img2txt
%{_datadir}/libcaca/
%{_mandir}/man1/cacademo.1*
%{_mandir}/man1/cacafire.1*
%{_mandir}/man1/cacaplay.1*
%{_mandir}/man1/cacaserver.1*
%{_mandir}/man1/cacaview.1*
%{_mandir}/man1/img2txt.1*

%files -n python3-caca
%doc python/examples
%{python3_sitelib}/caca/

#%%files -n ruby-caca
#%%doc ruby/README
#%%{ruby_vendorlibdir}/caca.rb
#%%exclude %{ruby_vendorarchdir}/caca.la
#%%{ruby_vendorarchdir}/caca.so


%changelog
* Thu Jul 28 2020  HAL <notes2@gmx.de> - 0.99-0.42.beta19
- compiles on Irix 6.5 and sgug-rse. 3 of 4 tests pass, the test that fails is for w32

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.42.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.41.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Matthias Saou <matthias@saou.eu> 0.99-0.40.beta19
- Update tetex to texlive in BR.
- Re-add python sub-package, but python3 (#1323249).

* Mon Jan 21 2019 Vít Ondruch <vondruch@redhat.com> - 0.99-0.39.beta19
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Thu Jan 10 2019 Miro Hrončok <mhroncok@redhat.com> - 0.99-0.38.beta19
- Remove Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.37.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.36.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99-0.35.beta19
- F-28: rebuild for ruby25

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.99-0.34.beta19
- Python 2 binary package renamed to python2-caca
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.33.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.32.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.31.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Vít Ondruch <vondruch@redhat.com> - 0.99-0.30.beta19
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.29.beta19
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.28.beta19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 0.99-0.27.beta19
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Mon Nov  9 2015 Matthias Saou <matthias@saou.eu> 0.99-0.26.beta19
- Update to 0.99.beta19.
- Remove upstreamed ruby patch, fixed in November 2012 (commit 36990e1).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.25.beta18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.99-0.24.beta18
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99-0.23.beta18
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.22.beta18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.21.beta18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Vít Ondruch <vondruch@redhat.com> - 0.99-0.20.beta18
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Mar 11 2014 Matthias Saou <matthias@saou.eu> 0.99-0.19.beta18
- Update to 0.99.beta18 (#1062632).
- Add python-caca sub-package with python bindings.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.18.beta17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 0.99-0.17.beta17
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.16.beta17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.15.beta17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.99-0.14.beta17
- Rebuilt and patched for Ruby 1.9.3.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.13.beta17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 11 2011 Matthias Saou <http://freshrpms.net/> 0.99-0.12.beta17
- Explicitly disable building csharp and java bindings (#671206).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.11.beta17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 28 2010 Matthias Saou <http://freshrpms.net/> 0.99-0.10.beta17
- Update to 0.99.0beta17.
- Update spec file URLs.
- Switch to using DESTDIR for install, which is the preferred method.
- Remove the static library (#556062).
- Remove no longer needed libGLU patch.
- Enable new ruby bindings.
- Leave C# and Java disabled, I hope no one will ever ask to have them enabled.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.9.beta16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Matthias Saou <http://freshrpms.net/> 0.99-0.8.beta16
- Fix build now that glut no longer links against libGLU (#502296).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Matthias Saou <http://freshrpms.net/> 0.99-0.6.beta16
- Add patch to share the same caca-config for 32 and 64bit (#341951).
- Don't include the pdf devel doc, only html (again, fixed multilib conflict).

* Mon Oct 27 2008 Matthias Saou <http://freshrpms.net/> 0.99-0.5.beta16
- Update to 0.99beta16.
- Update Source URL.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.99-0.4.beta11
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.99-0.3.beta11
- Rebuild for new BuildID feature.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 0.99-0.2.beta11
- Update License field.

* Thu Mar 29 2007 Matthias Saou <http://freshrpms.net/> 0.99-0.1.beta11
- Update to 0.99beta11.
- We now have a main libcaca package with just the shared lib (built by default
  now), so make the devel sub-package require it too. Leave static lib for now.
- Enable opengl and pango support.
- Remove useless rpath.
- Remove no longer needed man3 patch.
- Remove all configure options, they're autodetected.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.9-11
- FC6 rebuild.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.9-10
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 0.9-9
- Rebuild for new gcc/glibc.

* Mon Jan  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9-8
- Include unpackaged man page symlinks.
- Rebuild against new slang.

* Thu Nov 17 2005 Matthias Saou <http://freshrpms.net/> 0.9-7
- Change XFree86-devel requirements to libX11-devel.
- Force --x-includes= and --x-libraries=, otherwise -L gets passed empty.

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.9-6
- Include libcaca datadir.

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 0.9-5
- Bump release to provide Extras upgrade path.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 0.9-4
- Disable man3 pages, they don't build on FC3, this needs fixing.
- Fix to not get the debuginfo files go into the devel package.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9-3
- Rebuild for Fedora Core 2.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.9-2
- Fix License tag from GPL to LGPL.

* Mon Feb  9 2004 Matthias Saou <http://freshrpms.net/> 0.9-1
- Update to 0.9.
- Added cacamoir and cacaplas.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 0.7-1
- Spec file cleanup for Fedora Core 1.

* Wed Jan 7 2004 Sam Hocevar (RPM packages) <sam+rpm@zoy.org> 0.7-1
- new release

* Sun Jan 4 2004 Sam Hocevar (RPM packages) <sam+rpm@zoy.org> 0.6-2
- install documentation into {doc}/package-version instead of {doc}/package
- added tetex-dvips to the build dependencies

* Sat Jan 3 2004 Sam Hocevar (RPM packages) <sam+rpm@zoy.org> 0.6-1
- new release
- more detailed descriptions
- split the RPM into libcaca-devel and caca-utils
- packages are rpmlint clean

* Mon Dec 29 2003 Richard Zidlicky <rz@linux-m68k.org> 0.5-1
- created specfile

