Summary: Integer point manipulation library
Name: isl
Version: 0.18
License: MIT
URL: http://isl.gforge.inria.fr/

%global libmajor 15
%global libversion %{libmajor}.3.0

#global oldversion 0.14
#global oldlibmajor 13
#global oldlibversion %{oldlibmajor}.1.0

# Please set buildid below when building a private version of this rpm to
# differentiate it from the stock rpm.
#
# % global buildid .local

Release: 9%{?buildid}%{?dist}

BuildRequires:  gcc
BuildRequires: gmp-devel
BuildRequires: pkgconfig
#Provides: isl = %{oldversion}
Provides: isl = %{version}
Provides: libisl.so.%{libmajor}

Source0: http://isl.gforge.inria.fr/isl-%{version}.tar.bz2

# Current gcc requires exactly 0.14
#Source1: http://isl.gforge.inria.fr/isl-%{oldversion}.tar.xz

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints.  Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.  It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

%package devel
Summary: Development for building integer point manipulation library
Requires: isl%{?_isa} == %{version}-%{release}
Requires: gmp-devel%{?_isa}

%description devel
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints.  Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.  It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

%prep

%global docdir isl-%{version}
#setup -a 1 -q -n isl -c
%setup -q -n isl -c

%build

#cd isl-%{oldversion}
#configure
#make %{?_smp_mflags} V=1
#cd ..

cd isl-%{version}
%configure
make %{?_smp_mflags} V=1

%install

#cd isl-%{oldversion}
#make_install INSTALL="install -p" install-libLTLIBRARIES
#cd ..

cd isl-%{version}
%make_install INSTALL="install -p"
rm -f %{buildroot}/%{_libdir}/libisl.a
rm -f %{buildroot}/%{_libdir}/libisl.la
mkdir -p %{buildroot}/%{_datadir}
%global gdbprettydir %{_datadir}/gdb/auto-load/%{_libdir}
# No python yet
#mkdir -p %{buildroot}/%{gdbprettydir}
#mv %{buildroot}/%{_libdir}/*-gdb.py* %{buildroot}/%{gdbprettydir}
rm -f %{buildroot}/%{_libdir}/*-gdb.py*

%check
#cd isl-%{oldversion}
##make check
#cd ..

cd isl-%{version}
#make check

#%ldconfig_scriptlets

%files
%{_libdir}/libisl.so.%{libmajor}
%{_libdir}/libisl.so.%{libversion}
#%{_libdir}/libisl.so.%{oldlibmajor}
#%{_libdir}/libisl.so.%{oldlibversion}
#%{gdbprettydir}/*
%license %{docdir}/LICENSE
%doc %{docdir}/AUTHORS %{docdir}/ChangeLog %{docdir}/README

%files devel
%{_includedir}/*
%{_libdir}/libisl.so
%{_libdir}/pkgconfig/isl.pc
%doc %{docdir}/doc/manual.pdf

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.1-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Troy Dawson <tdawson@redhat.com> - 0.16.1-4
- Fix %%setup options

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 02 2017 David Howells <dhowells@redhat.com> - 0.16.1-1
- Move to version 0.16.1.
- Build and install just the libraries from 0.14 so that gcc can work.

* Wed Feb 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.14-6
- Add missing %%license macro (#1418512)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 5 2015 David Howells <dhowells@redhat.com> - 0.14-3
- Initial packaging.
