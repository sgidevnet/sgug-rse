%define _x11fontdir %{_datadir}/X11/fonts
%define catalogue /etc/X11/fontpath.d

Name:           libdockapp
Version:        0.6.2
Release:        19%{?dist}
Summary:        DockApp Development Standard Library

License:        MIT
URL:            http://solfertje.student.utwente.nl/~dalroi/libdockapp/
Source0:        http://solfertje.student.utwente.nl/~dalroi/libdockapp/files/libdockapp-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libXpm-devel libXext-devel libX11-devel

%description
LibDockApp is a library that provides a framework for developing dockapps. 
It provides functions and structures to define and display command-line 
options, create a dockable icon, handle events, etc.

The goal of the library is to provide a simple, yet clean interface and 
standardize the ways in which dockapps are developed. A dockapp developed 
using libDockApp will automatically behave well under most window 
managers, and especially well under Window Maker.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libXpm-devel
Requires:       libX11-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        fonts
Summary:        Fonts provided with %{name}

%description fonts
Bitmap X fonts provided with libdockapp.


%prep
%setup -q
find . -depth -type d -name CVS -exec rm -rf {} ';'

%build
%configure --disable-static --without-examples --disable-rpath
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT XFONTDIR=$RPM_BUILD_ROOT%{_x11fontdir} \
   INSTALL='install -p'
rm $RPM_BUILD_ROOT%{_libdir}/libdockapp.la
# fonts.alias is empty, so unusefull.
rm $RPM_BUILD_ROOT%{_x11fontdir}/dockapp/fonts.alias

rm -rf __examples_dist
cp -a examples __examples_dist
rm __examples_dist/Makefile*

mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{_x11fontdir}/dockapp $RPM_BUILD_ROOT%{catalogue}/dockapp


%ldconfig_scriptlets

%post fonts
if [ -x /usr/bin/fc-cache ]; then
  /usr/bin/fc-cache %{_datadir}/X11/fonts
fi

%postun fonts
if [ "$1" = "0" ]; then
  if [ -x /usr/bin/fc-cache ]; then
    /usr/bin/fc-cache %{_datadir}/X11/fonts
  fi
fi

%files
%doc AUTHORS BUGS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%doc __examples_dist/*
%{_includedir}/*
%{_libdir}/*.so

%files fonts
# there is no obvious package to depend on that owns %{_datadir}/X11/fonts/
%{_x11fontdir}/
#%{_x11fontdir}/dockapp/
%{catalogue}/dockapp

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May  5 2008 Patrice Dumas <pertusus@free.fr> 0.6.2-1
- update to 0.6.2

* Sat Feb  2 2008 Patrice Dumas <pertusus@free.fr> 0.6.1-6
- more portable stdincl patch

* Thu Dec 27 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-5
- minor cleanups

* Sun Sep 30 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-4
- new fontpath.d configuraton mechanism, change by ajax, Adam Jackson

* Thu May 24 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-3
- fix libtool bug on ppc64

* Wed Jan 10 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-2
- don't ship the empty fonts.alias

* Fri Jan  5 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-1
- Initial release
