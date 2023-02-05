Name:           mpfi
Version:        1.5.3
Release:        4%{?dist}
Summary:        An interval arithmetic library based on MPFR
License:        LGPLv2+
URL:            http://perso.ens-lyon.fr/nathalie.revol/software.html
Source0:        https://gforge.inria.fr/frs/download.php/file/37331/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  mpfr-devel
BuildRequires:  gmp-devel


%description
MPFI is intended to be a portable library written in C for arbitrary
precision interval arithmetic with intervals represented using MPFR
reliable floating-point numbers. It is based on the GNU MP library and
on the MPFR library and is part of the latter. The purpose of an
arbitrary precision interval arithmetic is on the one hand to get
"guaranteed" results, thanks to interval computation, and on the other
hand to obtain accurate results, thanks to multiple precision
arithmetic. The MPFI library is built upon MPFR in order to benefit
from the correct roundings provided by MPFR. Further advantages of
using MPFR are its portability and compliance with the IEEE 754
standard for floating-point arithmetic.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}, mpfr-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static library for %{name}


%description    static
The %{name}-static package contains the static %{name} library.


%prep
%autosetup


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

# Remove libtool archives
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Remove dir file in the info directory
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS TODO
%{_libdir}/libmpfi.so.*

%files devel
%{_includedir}/mpfi.h
%{_includedir}/mpfi_io.h
%{_infodir}/%{name}.info*
%{_libdir}/libmpfi.so

%files static
%{_libdir}/lib%{name}.a


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- New upstream version
- Drop upstreamed -aarch64 patch

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jerry James <loganjerry@gmail.com> - 1.5.1-4
- Add aarch64 support (bz 926172)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- New upstream version
- Drop upstreamed Debian patch

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 1.5-3
- Rebuild for GCC 4.7

* Wed Nov  2 2011 Jerry James <loganjerry@gmail.com> - 1.5-2
- Rebuild for new gmp.

* Mon Apr 25 2011 Jerry James <loganjerry@gmail.com> - 1.5-1
- New upstream version.
- Drop BuildRoot tag, clean script, and clean at start of install script.
- Drop texinfo patch, upstreamed.
- Move static library into -static subpackage.
- Add check script.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-0.8.RC3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-0.7.RC3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.6.RC3
- Add missing BR on texinfo.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-0.5.RC3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.4.RC3
- Attempt to preserve timestamps with install -p.
- Remove some useless %%docs.
- Give install-info more respect like it deserves.

* Tue Oct 14 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.4-0.3.RC3
- Use %%{_infodir} in %%preun/%%post.
- Move %%preun/%%post to *-devel.
- Remove R: from *-devel.

* Mon Oct 13 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.2.RC3
- Oops, fix the requires.
- Don't ship a base package.

* Mon Oct 13 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.1.RC3
- Fix version to follow NEVR guidelines (I don't want to bump the epoch
  since it's not even in Fedora yet).
- Install infos correctly.

* Sun Oct 12 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4RC3-1
- Initial package.
