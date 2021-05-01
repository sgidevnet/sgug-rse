Summary: Shared memory allocation library
Name: mm
Version: 1.4.2
Release: 23%{?dist}
License: BSD with advertising
Source0: ftp://ftp.ossp.org/pkg/lib/mm/mm-%{version}.tar.gz
URL: http://www.ossp.org/pkg/lib/mm/

BuildRequires:  gcc
%description
OSSP mm is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes
under Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level
malloc(3)-style API for a convenient and well known way to work with
data structures inside those shared memory segments.


%package devel
Summary: Header files and libraries for %{name} development
Requires: %{name} = %{version}


%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.


%prep
%setup -q


%build
%configure --enable-debug
%{__make} %{?_smp_mflags}


%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name "*.la" -exec rm -f {} \;
find %{buildroot} -name "*.a" -exec rm -f {} \;

# Fix permissions, so that find-debuginfo.sh picks up the libraries
find %{buildroot} -name *.so.* -type f -exec chmod 755 {} \;

# Fix the installed mm-config script to remove unnecessary flags and
# prevent a multilib conflict
sed -i -e 's#^mm_libdir=.*#mm_libdir=#; s# -L$mm_libdir##; s# -m[36][24]##' %{buildroot}%{_bindir}/mm-config



#%%ldconfig_scriptlets


%files
%doc LICENSE THANKS README
%{_libdir}/*.so.*


%files devel
%doc ChangeLog
%defattr(-, root, root)
%{_bindir}/mm-config
%{_libdir}/*.so
%{_includedir}/mm.h
%{_mandir}/man1/mm-config.1*
%{_mandir}/man3/mm.3*


%changelog
* Wed Sep 16 2020  HAL <notes2@gmx.de> - 1.4.2-23
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-8
- Rebuilt for glibc bug#747377

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Andreas Thienemann <andreas@bawue.net> - 1.4.2-5
- Updated mm-config file to remove multilib conflict.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.2-4
- Autorebuild for GCC 4.3

* Mon Feb 18 2008 Andreas Thienemann <andreas@bawue.net> - 1.4.2-3
- Rebuilt against gcc43

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 1.4.2-2
- FE6 Rebuild

* Thu Aug 17 2006 Andreas Thienemann <andreas@bawue.net> 1.4.2-1
- Updated to 1.4.2

* Thu Mar 02 2006 Andreas Thienemann <andreas@bawue.net> 1.4.0-3
- --enable-debug to finally fix the debuginfo package.

* Tue Feb 21 2006 Andreas Thienemann <andreas@bawue.net> 1.4.0-2
- Fix the debuginfo package.

* Sat Sep 13 2005 Andreas Thienemann <andreas@bawue.net> 1.4.0-1
- Initial spec.
