Name: udunits2
Version: 2.2.26
Release: 5%{?dist}
Summary: A library for manipulating units of physical quantities
License: UCAR
URL: http://www.unidata.ucar.edu/software/udunits/
Source0: ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-%{version}.tar.gz
BuildRequires: gcc-c++, groff, byacc, expat-devel, CUnit-devel
BuildRequires: chrpath
# workaround touching configure during build by the %%configure macro on ppc64le RHEL 7
# can go away when upstream refreshes the autoconf/libtool files
%if 0%{?rhel} == 7
%ifarch ppc64le
BuildRequires: texinfo-tex
%endif
%endif

%description
The Unidata units utility, udunits2, supports conversion of unit specifications 
between formatted and binary forms, arithmetic manipulation of unit 
specifications, and conversion of values between compatible scales of 
measurement. A unit is the amount by which a physical quantity is measured. For 
example:

                  Physical Quantity   Possible Unit
                  _________________   _____________
                        time              weeks
                      distance         centimeters
                        power             watts

This utility works interactively and has two modes. In one mode, both an input 
and output unit specification are given, causing the utility to print the 
conversion between them. In the other mode, only an input unit specification is 
given. This causes the utility to print the definition -- in standard units -- 
of the input unit.

%package devel
Summary: Headers and libraries for udunits2
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the files needed for compiling programs using
the udunits2 library.

%prep
%setup -q -n udunits-%{version}

%build
%configure --disable-static --docdir %{_docdir}/%{name}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install install-html install-pdf
# Remove rpath
chrpath -d %{buildroot}%{_bindir}/*
# Install info and doc
mkdir -p %{buildroot}%{_infodir}/
install -p -m0644 %{name}.info %{buildroot}%{_infodir}
install -p -m0644 ANNOUNCEMENT %{buildroot}%{_docdir}/%{name}/
# we get this in %%license
rm -rf %{buildroot}%{_docdir}/%{name}/COPYRIGHT

# We need to do this to avoid conflicting with udunits v1
mkdir -p %{buildroot}%{_includedir}/%{name}/
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/%{name}/
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_infodir}/dir

%check
make check

%files
%license COPYRIGHT
%{_bindir}/%{name}
%{_datadir}/udunits/
%{_infodir}/%{name}*.info*
%{_libdir}/libudunits2.so.*
%doc %{_docdir}/%{name}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libudunits2.so

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Tom Callaway <spot@fedoraproject.org> - 2.2.26-1
- update to 2.2.26

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Tom Callaway <spot@fedoraproject.org> - 2.2.25-1
- update to 2.2.25

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Orion Poplawski <orion@cora.nwra.com> - 2.2.23-1
- Update to 2.2.23

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 2.2.21-1
- Update to 2.2.21

* Tue May 17 2016 Tom Callaway <spot@fedoraproject.org> 2.2.20-4
- fix license tag
- handle license file properly

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Dan Horák <dan[at]danny.cz> - 2.2.20-2
- fix build in ppc64le EPEL-7

* Mon Oct 26 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.20-1
- Update to 2.2.20

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 2 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.19-1
- Update to 2.2.19

* Mon Feb 9 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.18-1
- Update to 2.2.18

* Fri Sep 5 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.17-1
- Update to 2.2.17

* Fri Sep 5 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.16-3
- Strip rpath from binaries

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.16-1
- Update to 2.2.16

* Mon Jun 23 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.14-1
- Update to 2.2.14

* Fri Jun 13 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.13-1
- Update to 2.2.13

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.12-2
- Move doc dir to udunits2 to avoid conflicts (bug #1104766)

* Tue Jun 3 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.12-1
- Update to 2.2.12 (fixes bug #1076802 - partial expat bundling)
- Enable tests (bug #1076799)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 9 2011 Orion Poplawski <orion@cora.nwra.com> - 2.1.24-1
- Update to 2.1.24
- Install docs via install-html/pdf

* Mon Nov 7 2011 Orion Poplawski <orion@cora.nwra.com> - 2.1.22-1
- Update to 2.1.22

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.19-1
- update to 2.1.19

* Thu Jul  1 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.17-3
- missing BuildRequires: expat-devel

* Wed Jun 30 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.17-2
- tag mistake

* Wed Jun 30 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.17-1
- update to 2.1.17
- cleanup spec file

* Sun Dec  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.11-1
- initial package for udunits2: 2.1.11
