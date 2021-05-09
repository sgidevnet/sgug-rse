Name: libguess
Version: 1.2
Release: 10%{?dist}

Summary: High-speed character set detection library
License: BSD
URL: http://rabbit.dereferenced.org/~nenolod/distfiles/
Source0: http://rabbit.dereferenced.org/~nenolod/distfiles/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires: pkgconfig

%description
libguess employs discrete-finite automata to deduce the character set of
the input buffer. The advantage of this is that all character sets can be
checked in parallel, and quickly. Right now, libguess passes a byte to
each DFA on the same pass, meaning that the winning character set can be
deduced as efficiently as possible.

libguess is fully reentrant, using only local stack memory for DFA
operations.


%package devel
Summary: Files needed for developing with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the files that are needed when building
software that uses %{name}.


%prep
%setup -q

sed -i '\,^.SILENT:,d' buildsys.mk.in


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p"


%check
cd src/tests/testbench
LD_LIBRARY_PATH=${RPM_BUILD_ROOT}%{_libdir} make


%ldconfig_scriptlets


%files
%doc COPYING README
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*

%files devel
%{_libdir}/%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2-1
- BR libmowgli no longer needed.
- M4 dir patch merged.
- Update URLs.
- Upgrade to 1.2 (in the API only added the no-op libguess_init).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec  2 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-7
- Add conditionals for EL builds (#1036386).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 21 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-5
- Patch configure.ac to define m4 macro dir.
- BR autoconf libtool and run autoreconf -f for aarch64 updates (#925758).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-2
- rebuild for GCC 4.7 as requested

* Sat Dec  3 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1-1
- Upgrade to 1.1 with added %%check section.

* Fri Sep 16 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0-3
- Use %%_isa in -devel package dependency.
- Drop %%defattr lines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0-1
- Use fresh 1.0 release tarball, which only adds the makerelease.sh script.
- Drop unneeded BuildRoot stuff.

* Tue Jul 13 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0-0.1.20100713
- Initial RPM packaging.
