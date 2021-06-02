Name:           tcl-signal
Version:        1.4
Release:        18%{?dist}
Summary:        This extension adds dynamically loadable signal handling to Tcl/Tk scripts

License:        MIT
URL:            http://www.nyx.net/~mschwart/signal_ext.html
Source0:        http://www.nyx.net/~mschwart/signal_ext1.4.tar.gz
#Strip off trailing entries in TCL_PACKAGE_PATH
Patch0:         signal_ext-tclpath.patch
#Add DESTDIR support
Patch1:         signal_ext-destdir.patch
#Add lib64 support
Patch2:         signal_ext-lib64.patch
#Rename library to libtclsignal.so
Patch3:         signal_ext-libtclsignal.patch

BuildRequires:  gcc
BuildRequires:  tcl-devel


%description
This extension adds dynamically loadable signal handling to Tcl/Tk scripts.

Note that the library has been renamed to libtclsignal-%{version}.so for ease in
linking and to prevent conflicts.


%prep
%setup -q -n signal_ext%{version}
%patch0 -p1 -b .tclpath
%patch1 -p1 -b .destdir
%patch2 -p1 -b .lib64
%patch3 -p1 -b .libtclsignal


%build
export TCL_INC_DIR=%{_includedir}
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
sed -i -e s,signal.so,%{_libdir}/libtclsignal-%{version}.so, $RPM_BUILD_ROOT%{_libdir}/tcl*/signal/pkgIndex.tcl
chmod 644 $RPM_BUILD_ROOT%{_libdir}/tcl*/signal/pkgIndex.tcl


%files
%doc README sig.announce.1.4
%{_libdir}/libtclsignal-%{version}.so
%{_libdir}/tcl*/signal


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 4 2012 Orion Poplawski <orion@cora.nwra.com> 1.4-4
- Fix library name in description

* Mon Aug 27 2012 Orion Poplawski <orion@cora.nwra.com> 1.4-3
- Use spaces
- Drop BuildRoot, clean
- Add version to libtclsignal

* Thu May 5 2011 Orion Poplawski <orion@cora.nwra.com> 1.4-2
- Rename to tcl-signal
- Rename library and move to %%{_libdir}

* Wed May 4 2011 Orion Poplawski <orion@cora.nwra.com> 1.4-1
- Initial package
