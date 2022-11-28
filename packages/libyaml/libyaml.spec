%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

Name:       libyaml
Version:    0.2.2
Release:    5%{?dist}
Summary:    YAML 1.1 parser and emitter written in C

License:    MIT
URL:        http://pyyaml.org/
Source0:    http://pyyaml.org/download/libyaml/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
#BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.


%package devel
Summary:   Development files for LibYAML applications
Requires:  libyaml = %{version}-%{release}, pkgconfig


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use LibYAML.


%prep
%setup -q -n %{name}-%{version}


%build
./bootstrap
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++

export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
%if 0%{debug}
export CFLAGS="-g -O0"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -Wl,-z,relro -Wl,-z,now"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif

%configure
make all html %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install
rm -f %{buildroot}%{_libdir}/*.{la,a}

soname=$(readelf -d %{buildroot}%{_libdir}/libyaml.so | awk '$2 == "(SONAME)" {print $NF}' | tr -d '[]')
#rm -f %{buildroot}%{_libdir}/libyaml.so
#echo "INPUT($soname)" > %{buildroot}%{_libdir}/libyaml.so


%check
make check


#%%ldconfig_scriptlets


%files
%license LICENSE
%doc README
%{_libdir}/%{name}*.so.*


%files devel
#%%doc doc/html
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/yaml-0.1.pc
%{_includedir}/yaml.h


%changelog
* Tue Dec 08 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.2-5
- Correct _SGI_SOURCES (no plural)

* Sun Jul 05 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.2-4
- renable the html doc building

* Fri May 15 2020  Alexander Tafarte <notes2@gmx.de> - 0.2.2-3
- compiles on Irix 6.5 with sgug-rse gcc 9.2 , passes both tests.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 John Eckersberg <eck@redhat.com> - 0.2.2-1
- New upstream release (rhbz#1692750)

* Tue Feb  5 2019 John Eckersberg <eck@redhat.com> - 0.2.1-5
- Add patch: Revert removing of open_ended after top level plain scalar (rhbz#1672670)

* Tue Feb  5 2019 John Eckersberg <eck@redhat.com> - 0.2.1-4
- Add patch: Don't emit document-end marker at the end of stream (rhbz#1672670)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug  7 2018 Jens Petersen <petersen@redhat.com> - 0.2.1-2
- rebuild against fixed binutils to fix missing symbols (#1613350)

* Mon Jul 16 2018 John Eckersberg <eck@redhat.com> - 0.2.1-1
- New upstream release 0.2.1 (rhbz#1598611)

* Mon Jul 16 2018 John Eckersberg <eck@redhat.com> - 0.1.7-8
- Add BuildRequires for gcc
  See: https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-5
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 John Eckersberg <eck@redhat.com> - 0.1.7-1
- New upstream release 0.1.7 (RHBZ#1371154)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec  1 2014 John Eckersberg <eck@redhat.com> - 0.1.6-6
- Add patch for CVE-2014-9130 (RHBZ#1169371)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 0.1.6-4
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.6-2
- Work around ldconfig bug with libyaml.so (bz1082822)

* Wed Mar 26 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.6-1
- New upstream release 0.1.6 (bz1081492)
- Fixes CVE-2014-2525 (bz1078083)

* Tue Feb  4 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.5-1
- New upstream release 0.1.5 (bz1061087)
- Removed patches for CVE-2013-6393; they are included in 0.1.5
  upstream

* Wed Jan 29 2014 John Eckersberg <jeckersb@redhat.com> - 0.1.4-6
- Add patches for CVE-2013-6393 (bz1033990)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 John Eckersberg <jeckersb@redhat.com> - 0.1.4-1
- New upstream release 0.1.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 02 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.3-1
- New upstream release 0.1.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-4
- Minor tweaks to spec file
- Enable %%check section
- Thanks Gareth Armstrong <gareth.armstrong@hp.com>

* Tue Mar 3 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-3
- Remove static libraries

* Thu Feb 26 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-2
- Remove README and LICENSE from docs on -devel package
- Remove -static package and merge contents into the -devel package

* Wed Feb 25 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-1
- Initial packaging for Fedora
