Name: wcstools
Version: 3.9.6
Release: 1%{?dist}
Summary: Software utilities to display and manipulate the WCS of a FITS image
License: GPLv2+
URL: http://tdc-www.harvard.edu/wcstools
Source0: http://tdc-www.harvard.edu/software/wcstools/%{name}-%{version}.tar.gz

BuildRequires:  gcc

# Patch from Debian to create shared lib and rename it to avoid
# conflicts with Mark Calabretta's wcslib package.
Patch0: wcstools-3.9.6-rename-shlib.patch

%description
Wcstools is a set of software utilities, written in C, which create,
display and manipulate the world coordinate system of a FITS or IRAF
image, using specific keywords in the image header which relate pixel
position within the image to position on the sky.  Auxiliary programs
search star catalogs and manipulate images.


%package libs
Summary: Wcstools shared library 
License: LGPLv2+

%description libs
Shared library necessary to run wcstools and programs based on libwcs.


%package devel
Summary: Libraries, includes, etc. used to develop an application with wcstools
License: LGPLv2+
Requires: %{name}-libs%{_isa} = %{version}-%{release}
%description devel
This are the files needed to develop an application using wcstools.

%prep
%setup -q
%patch0 -p1

# Fix wrong FSF address in source headers
# asked upstream by mail to fix this
grep -rl '59 Temple Place, Suite 330, Boston, MA  02111-1307  USA' --include=*.{c,h} | xargs -i@ sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA./g' @


%build
CFLAGS="$RPM_OPT_FLAGS"
CPPFLAGS="$RPM_OPT_FLAGS"
export CFLAGS
export CPPFLAGS

# Parallel build fails
make

%install
%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_includedir}/wcs
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -p bin/* %{buildroot}%{_bindir}

# Rename conflicting binary bug #1450190
# Mailed upstream, no response
# Debian uses the same rename
mv %{buildroot}%{_bindir}/remap %{buildroot}%{_bindir}/wcsremap

%{__cp} -a libwcs/*.so* %{buildroot}%{_libdir}
%{__install} -p -m 644 libwcs/*.h %{buildroot}%{_includedir}/wcs
%{__install} -p -m 644 man/man1/* %{buildroot}%{_mandir}/man1



%files
%license COPYING
%doc NEWS Readme Programs
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%license libwcs/COPYING
%{_libdir}/*.so.1*

%files devel
%doc libwcs/NEWS
%{_libdir}/*.so
%{_includedir}/wcs


%changelog
* Sat Jun 27 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.9.6-1
- Update to 3.9.6

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Mattia Verga <mattia.verga@yandex.com> - 3.9.5-7
- Remove ldconfig scriptlets

* Mon Feb 19 2018 Mattia Verga <mattia.verga@email.it> - 3.9.5-6
- Add gcc to BuildRequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 20 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.9.5-2
- Rename remap to wcsremap. See #1450190

* Fri Apr 14 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.9.5-1
- Update to 3.9.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.9.4-1
- Update to 3.9.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 03 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.8.1-1
- New upstream source
- Patch to fix bz #559863 from upstream

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-6
- Reverting soname change

* Sat Feb 14 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-5
- Libray and headers renamed as wcstools

* Wed Oct 01 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-4
- Fails to build from source bz#465061

* Wed Oct 01 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-3
- Fails to build from source bz#465061

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.7.0-2
- Autorebuild for GCC 4.3

* Wed Sep 05 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 3.7.0-1
- New upstream source 3.7.0

* Mon Aug 27 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 3.6.8-2.1
- Rebuild for Fedora 8 to get the build-id

* Tue Mar 20 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.8-2
- Fix for bug #232413

* Mon Mar 19 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.8-1
- New upstream source 3.6.8
- Added pacthes to remove warnings during the compilation

* Mon Feb 26 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.7-1
- New upstream source 3.6.7

* Wed Nov 15 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.6-1
- New upstream source 3.6.6

* Tue Oct 10 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.6-0.1.beta
- New upstream source 3.6.6beta

* Mon Sep 4 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.5-3
- Rebuild.

* Wed Aug 30 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.5-2
- Corrected bug in edhead (patch2) (bug #204642).

* Wed Jun 21 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.5-1
- New upstream source 3.6.5

* Tue Jun 13 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.4-3
- Patched overflows in catutil.c and getdate.c
- Patched incompatible pointer in binread.c

* Mon Jun 12 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.4-2
- Patched edhead.
- libwcs provides libwcs.so.3
- libwcs into System Environment/Libraries group
- Makefile uses ${RPM_OPT_FLAGS} and $(CC)

* Fri Jun 09 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.4-1
- Removed not needed ldconfig in wcstools and libwcs-devel.

* Wed Mar 08 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.3-1
- Initial RPM file.
