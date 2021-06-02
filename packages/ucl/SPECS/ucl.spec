Name:           ucl
Version:        1.03
Release:        27%{?dist}
Summary:        Portable lossless data compression library

License:        GPLv2+
URL:            http://www.oberhumer.com/opensource/ucl/
Source0:        http://www.oberhumer.com/opensource/ucl/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
UCL is a portable lossless data compression library written in ANSI C.
UCL implements a number of compression algorithms that achieve an
excellent compression ratio while allowing *very* fast decompression.
Decompression requires no additional memory.

%package        devel
Summary:        UCL development files
Requires:       %{name} = %{version}-%{release}

%description    devel
%{summary}.


%prep
%setup -q


%build
CPPFLAGS="$RPM_OPT_FLAGS $CPPFLAGS -std=c90 -fPIC"
export CPPFLAGS
%configure --disable-dependency-tracking --enable-shared --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libucl.la



%ldconfig_scriptlets


%files
%doc COPYING NEWS README THANKS TODO
%{_libdir}/libucl.so.*

%files devel
%{_includedir}/ucl/
%{_libdir}/libucl.so


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 09 2016 Jon Ciesla <limb@jcomserv.net> - 1.03-20
- Fix FTBFS.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 1.03-8
- GCC 4.3 rebuild.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 1.03-7
- License tag correction.

* Mon Aug 28 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.03-6
- Rebuild.

* Mon Feb 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.03-5
- Rebuild.

* Wed Nov  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.03-4
- Don't ship static libraries.
- Build with dependency tracking disabled.

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.03-3
- Rebuild.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.03-2
- rebuilt

* Wed Jul 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.03-0.fdr.1
- Update to 1.03, patch applied upstream.

* Fri Apr 30 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.02-0.fdr.1
- Update to 1.02.

* Thu Oct 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.01-0.fdr.2
- Specfile cleanup.

* Fri Jul 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.01-0.fdr.1
- First build.
