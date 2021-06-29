%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary: Cross platform C library for parsing GNU style command line arguments
Name: argtable
Version: 2.13
Release: 17%{?dist}
License: LGPLv2+
Url: http://argtable.sourceforge.net/
Source: http://prdownloads.sourceforge.net/argtable/%{name}2-13.tar.gz
BuildRequires:  gcc
BuildRequires: pkgconfig

%description
Argtable is an ANSI C library for parsing GNU style command line
arguments. It enables a program's command line syntax to be defined in
the source code as an array of argtable structs. The command line is
then parsed according to that specification and the resulting values
are returned in those same structs where they are accessible to the main
program. Both tagged (-v, --verbose, --foo=bar) and untagged arguments
are supported, as are multiple instances of each argument.
Syntax error handling is automatic.

%package devel
Summary: Development package that includes the argtable header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header and development files for using argtable

%prep
%setup -q -n %{name}2-13

%build
%configure --disable-static --docdir=%{_pkgdocdir}
make %{?_smp_mflags} 

%install
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.la
install -pm 644 AUTHORS ChangeLog COPYING README ${RPM_BUILD_ROOT}%{_pkgdocdir}

%files
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/COPYING
%{_pkgdocdir}/README
%{_libdir}/libargtable2.so.*

%files devel
%{_libdir}/libargtable2.so
%{_includedir}/argtable2.h
%{_libdir}/pkgconfig/argtable2.pc

%doc %{_mandir}/man3/*
%{_pkgdocdir}/*
%exclude %{_pkgdocdir}/AUTHORS
%exclude %{_pkgdocdir}/ChangeLog
%exclude %{_pkgdocdir}/COPYING
%exclude %{_pkgdocdir}/README

%ldconfig_scriptlets

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Mukundan Ragavan <nonamedotc@gmail.com> - 2.13-7
- Rebuilt for F22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.13-5
- Install doc to %%{_pkgdocdir} where available (#993671).
- Don't duplicate docs in main and -devel.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 27 2012 Paul Wouters <pwouters@redhat.com> - 2.13-2
- Removed el5 specific spec options

* Sat Oct 27 2012 Paul Wouters <pwouters@redhat.com> - 2.13-1
- Initial package
- Notified upstream of incorrect-fsf-address
