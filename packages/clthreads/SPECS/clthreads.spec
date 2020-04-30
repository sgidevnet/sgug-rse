%global libmajor 2

Summary:       POSIX threads C++ access library
Name:          clthreads
Version:       2.4.2
Release:       1%{?dist}
License:       LGPLv2+
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
BuildRequires: gcc-c++

%description
Clthreads is a C++ wrapper library around the POSIX threads API.

%package  devel
Summary:       Development files for %{name}
Requires:      %{name} = %{version}-%{release}

%description devel
Clthreads is a C++ wrapper library around the POSIX threads API. This package
contains libraries and header files for developing applications that use
%{name}.

%prep
%setup -q

# No need to call ldconfig during packaging
sed -i '\|ldconfig|d' source/Makefile

# Fix Makefile paths (patch sent upstream)
sed -i -e 's|install -d $(DESTDIR)$(PREFIX)/$(INCDIR)|install -d $(DESTDIR)$(INCDIR)|' \
 -e 's|install -d $(DESTDIR)$(PREFIX)/$(LIBDIR)|install -d $(DESTDIR)$(LIBDIR)|' source/Makefile

# Preserve timestamps
sed -i 's|/install|/install -p|' source/Makefile

# No native arch
sed -i -e '/^CXXFLAGS += -march=native/d' source/Makefile

%build
%set_build_flags
%make_build -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%make_install -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}

%files
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Mon Jul 22 2019 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.2-1
- Update to 2.4.2
- Minor spec cleanup

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.0-14
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 11 2011 Brendan Jones <brendan.jones.it@gmail.com> - 2.4.0-7
- correct URL and download link

* Fri Oct 04 2011 Brendan Jones <brendan.jones.it@gmail.com> - 2.4.0-6
- Corrected rpmlint 'undefined-non-weak-symbol /usr/lib64/libclthreads.so.2.4.0
clock_gettime' and unused-direct-shlib-dependency for libm - BZ#751466

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 04 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.0-3
- Use %%{name} macro more often
- Preserve timestamps

* Mon May 04 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.0-2
- prepare package for Fedora submission (SPEC file from PlanetCCRMA)

* Tue Apr 15 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.0-1
- updated to version 2.4.0

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.1-1
- updated to version 2.2.1

* Sun Nov 19 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.0-3
- add %%{?dist} to release tag, add %%{fedora} conditional for X build
  requirement

* Mon May 29 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.0-2
- fix library link

* Sat May 13 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.0
- update to 2.2.0

* Fri Mar 31 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- proper build dependencies for fc5

* Tue Dec 28 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanups

* Fri Dec  3 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.2-1
- updated to 1.0.2

* Fri Jul 23 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-1
- updated to 1.0.0

* Wed Jun 16 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.3-2
- DOH!, obsolete the -devel package as well...

* Mon Jun 14 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.3-1
- obsoletes classlibs
- first build

* Tue May 11 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- moved so file to main package to keep aeolus happy

* Wed May  5 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.1-2
- force apps to link with the major release name of the libraries
  (ie: ".so.0" instead of ".so")

* Tue May  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.1-1
- initial build, needed for releasing Aeolus
