Name:           azove
Version:        2.0
Release:        17%{?dist}
Summary:        Another Zero-One Vertex Enumeration tool

License:        GPLv2+
URL:            http://www.mpi-inf.mpg.de/~behle/azove.html
Source0:        http://www.mpi-inf.mpg.de/~behle/%{name}-%{version}.tar.gz
# Man page written by Jerry James from text found in the sources.  Therefore,
# the copyright and license of the man page is the same as the sources.
Source1:        %{name}2.1
# Sent upstream 2 Mar 2012: add an include that used to be implicit.
Patch0:         %{name}-include.patch

BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

%description
Azove is a tool designed for counting (without explicit enumeration) and
enumeration of 0/1 vertices.  Given a polytope by a linear relaxation or
facet description P = {x | Ax <= b}, all 0/1 points lying in P can be
counted or enumerated.  This is done by intersecting the polytope P with
the unit-hypercube [0,1] d.  The integral vertices (no fractional ones)
of this intersection will be enumerated.  If P is a 0/1 polytope, azove
solves the vertex enumeration problem.  In fact it can also solve the
0/1 knapsack problem and the 0/1 subset sum problem.

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags} COMPILER_FLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 -p %{name}2 $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc INSTALL README
%license COPYING
%{_bindir}/%{name}2
%{_mandir}/man1/%{name}2.1*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 2.0-7
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug  3 2012 Jerry James <loganjerry@gmail.com> - 2.0-2
- Fix permissions on installed files

* Fri Mar  2 2012 Jerry James <loganjerry@gmail.com> - 2.0-1
- Initial RPM
