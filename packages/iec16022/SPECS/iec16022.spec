# TODO: shared lib calls exit

Name:           iec16022
Version:        0.2.4
Release:        23%{?dist}
Summary:        Generate ISO/IEC 16022 2D barcodes

License:        GPLv2+
URL:            http://www.datenfreihafen.org/projects/iec16022.html
Source0:        http://www.datenfreihafen.org/~stefan/iec16022/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-test-suite-fix.patch

## For ARM64 support.
BuildRequires:  gcc
BuildRequires:  autoconf >= 2.69
BuildRequires:  popt-devel zlib-devel


%description
iec16022 is a program for producing ISO/IEC 16022 2D barcodes, also
known as Data Matrix.  These barcodes are defined in the ISO/IEC 16022
standard.

%package        libs
Summary:        ISO/IEC 16022 libraries

%description    libs
%{summary}.

%package        devel
Summary:        ISO/IEC 16022 development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
%{summary}.


%prep
%setup -q
%patch0 -p1 -b .orig


%build
autoconf
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libiec16022.la


%check
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
make -C test check


%ldconfig_scriptlets libs


%files
%{_bindir}/iec16022
%{_mandir}/man1/iec16022.1*

%files libs
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/libiec16022.so.*

%files devel
%{_includedir}/iec16022/
%{_libdir}/libiec16022.so
%{_libdir}/pkgconfig/libiec16022.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Peter Gordon <peter@thecodergeek.com> - 0.2.4-12
- Update spec file in accordance with newer packaging guidelines:
  - Remove unnecessary BuildRoot references;
  - Remove %%defattr lines in %%files listings.
- Rerun autoconf in %%build to update for ARM64 arch support.
- Fixes bug #925577 (iec16022: Does not support aarch64 in f19 and rawhide)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 02 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-6
- Rearranging sed positions.

* Wed Jun 02 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-5
- Fixed test-suite(wasn't correctly fixed) and devel dependencies.

* Thu May 27 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-4
- Fixed test-suite and devel dependencies.

* Fri May 21 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-3
- Modify the spec according to Fedora Package Guidelines.

* Sat Mar 6 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.2.4-2
- Avoid rpath in executable.

* Sun Oct 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.2.4-1
- 0.2.4.

* Tue Jul 22 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.2.3-1
- 0.2.3.

* Sun Dec 30 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.2.2-1
- 0.2.2.

* Sat Nov 10 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.2.1-2
- BuildRequire popt-devel.
- License: GPLv2+

* Wed Nov 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.2.1-1
- 0.2.1.

* Sat Sep 30 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.2-2
- Rebuild.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.2-1
- First build.
