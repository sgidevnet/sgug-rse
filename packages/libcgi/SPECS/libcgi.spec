#
# Rebuild option:
#
#   --with static            creates the -static subpckage
#

%global static  0

%{?_with_static:%global static 1}

%global libcgi_somajor 1
%global libcgi_sominor 0

Name:           libcgi
Version:        1.0
Release:        28%{?dist}
Summary:        CGI easy as C
License:        LGPLv2+
URL:            http://libcgi.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/libcgi/libcgi-%{version}.tar.gz
Patch0:         libcgi-1.0-Makefile.in.patch
Patch1:         libcgi-1.0-cgi.c-hextable.patch
Patch2:         libcgi-1.0-string.c-make_string.patch
BuildRequires:  gcc

%description
LibCGI is a library written from scratch to easily make CGI applications in C.


%package devel
Summary:        Header files and libraries for LibCGI development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libcgi-devel package contains the header files and libraries needed
to develop programs that use the LibCGI library.


%if %{static}
%package static
Summary:        LibCGI static library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libcgi-static package contains the static library needed
to develop programs that use the LibCGI library.
%endif


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
find examples/ -name "Makefile.am" -delete


%build
%configure
make SOMAJOR=%{libcgi_somajor} \
     SOMINOR=%{libcgi_sominor} \
     %{?_smp_mflags}


%install
make SOMAJOR=%{libcgi_somajor} \
     SOMINOR=%{libcgi_sominor} \
     DESTDIR=$RPM_BUILD_ROOT \
     LIBDIR=%{_libdir} \
     INCDIR=%{_includedir}/%{name} \
     install
make DESTDIR=$RPM_BUILD_ROOT install_man

%if ! %{static}
rm -f $RPM_BUILD_ROOT%{_libdir}/libcgi.a
%endif


%ldconfig_scriptlets


%files
%doc AUTHORS BUGS ChangeLog README THANKS TODO
%{_libdir}/*.so.*


%files devel
%doc doc/html/ examples/
%{_libdir}/*.so
%{_includedir}/%{name}/
%{_mandir}/man3/*.3*


%if %{static}
%files static
%{_libdir}/*.a
%endif


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.0-26
- add BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 1.0-19
- spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-8
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-7
- fix license tag

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.0-6
- Rebuild for selinux ppc32 issue.

* Tue Jun 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-5
- make install: override LIBDIR in order to support /usr/lib64.

* Tue Jun 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-4
- Install the header files in %%{_includedir}/%%{name}.

* Tue Apr 10 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-3
- Don't build the static subpackage by default.

* Sun Jan 21 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-2
- Static subpackage.

* Sun Jan  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-1
- libcgi-1.0-cgi.c-hextable.patch (sourceforge #1024122).
- libcgi-1.0-string.c-make_string.patch (sourceforge #1393115).
- libcgi-1.0-Makefile.in.patch (CFLAGS, DESTDIR, soname).

* Sat Dec 30 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-0
- Initial build.

# vim:set ai ts=4 sw=4 sts=4 et:
