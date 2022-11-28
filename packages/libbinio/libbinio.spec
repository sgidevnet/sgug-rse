# SPEC file for libbinio, primary target is the Fedora Extras
# RPM repository.

Name:		libbinio
Version:	1.4
Release:	31%{?dist}
Summary:	A software library for binary I/O classes in C++
URL:		http://libbinio.sourceforge.net/
Source:		http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		libbinio-1.4-texinfo.patch
Patch1:		libbinio-1.4-pkgconfigurl.patch
Patch2:		libbinio-1.4-includes.patch
License:	LGPLv2+
BuildRequires:	gcc-c++
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:	/sbin/install-info
%endif

%description
This binary I/O stream class library presents a platform-independent
way to access binary data streams in C++. The library is hardware 
independent in the form that it transparently converts between the 
different forms of machine-internal binary data representation.
It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

%package devel
Summary:        Development files for libbinio
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:	texinfo
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post):	/sbin/install-info
Requires(preun): /sbin/install-info
%endif

%description devel
This package contains development files for the libbinio binary
data stream class for C++.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# Remove libtool archive remnants
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# Remove doc "dir"
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir

%ldconfig_scriptlets

%if 0%{?rhel} && 0%{?rhel} <= 7
%post devel
/sbin/install-info %{_infodir}/libbinio.info.gz %{_infodir}/dir || :

%preun devel
if [ $1 = 0 ]; then
# uninstall the info reference in the dir file
/sbin/install-info --delete %{_infodir}/libbinio.info.gz %{_infodir}/dir || :
fi
%endif

%files
%{_libdir}/*.so.*
%doc AUTHORS README COPYING INSTALL INSTALL.unix NEWS TODO

%files devel
%dir %{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/*.h
%{_infodir}/*.gz

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.4-30
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4-21
- Rebuild for newest GCC 5 C++ ABI change, so deps can compile/link with this.

* Thu Feb 19 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4-20
- Drop buildroot tag, %%defattr, %%clean.
- Fix -devel group tag.
- Add %%_isa to -devel base package dep.
- Rebuild for GCC 5 C++ ABI change, so deps can compile/link with this.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Caolán McNamara <caolanm@redhat.com> - 1.4-11
- include stdio.h for EOF

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Linus Walleij <triad@df.lth.se> 1.4-9
- Rebuild for GCC 4.3.

* Fri Jan 18 2008 Linus Walleij <triad@df.lth.se> 1.4-8
- New glibc ABI wants a rebuild.

* Fri Aug 17 2007 Linus Walleij <triad@df.lth.se> 1.4-7
- License field update from LGPL to LGPLv2+

* Mon Aug 28 2006 Linus Walleij <triad@df.lth.se> 1.4-6
- Rebuild for Fedora Extras 6.

* Tue Feb 14 2006 Linus Walleij <triad@df.lth.se> 1.4-5
- Rebuild for Fedora Extras 5.

* Thu Oct 6 2005 Linus Walleij <triad@df.lth.se> 1.4-4
- BuildRequire texinfo to get makeinfo.

* Sat Oct 1 2005 Linus Walleij <triad@df.lth.se> 1.4-3
- Conforming pkg-config for FC4 and texinfo bug patch.

* Sun Sep 18 2005 Linus Walleij <triad@df.lth.se> 1.4-2
- More minor corrections.

* Sun Sep 18 2005 Linus Walleij <triad@df.lth.se> 1.4-1
- Upstream fixed header problem.

* Fri Sep 16 2005 Linus Walleij <triad@df.lth.se> 1.3-4
- Trying to resolve dispute about header subdirs.

* Thu Sep 15 2005 Linus Walleij <triad@df.lth.se> 1.3-3
- Reverted some and added some after comments from Ville Skyttä.

* Thu Sep 15 2005 Linus Walleij <triad@df.lth.se> 1.3-2
- Fixed some points raised by Ralf Corsepius.

* Wed Sep 14 2005 Linus Walleij <triad@df.lth.se> 1.3-1
- First try at a libbinio RPM.
