Summary:	C library for parsing command line parameters
Name:		popt
Version:	1.16
Release:	18%{?dist}
License:	MIT
URL:		http://www.rpm5.org/
Source:		http://www.rpm5.org/files/%{name}/%{name}-%{version}.tar.gz
Patch0:		popt-1.16-pkgconfig.patch
Patch1:		popt-1.16-execfail.patch
Patch2:		popt-1.16-man-page.patch
Patch3:		popt-1.16-help.patch
Patch4:		popt-1.16-nextarg-memleak.patch
Patch5:		popt-1.16-glob-error.patch
BuildRequires:	gcc gettext
BuildRequires:  libdicl-devel
Requires:       libdicl

%description
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but
it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%package devel
Summary:	Development files for the popt library
Requires:	%{name}%{?_isa} = %{version}-%{release}, pkgconfig
Requires:       libdicl-devel

%description devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library. It contains the
API documentation of the popt library, too.

%package static
Summary:	Static library for parsing command line parameters
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
The popt-static package includes static libraries of the popt library.
Install it if you need to link statically with libpopt.

%prep
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LIBS="-ldicl-0.1"
%autosetup

%build
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LIBS="-ldicl-0.1"
%configure
%make_build

%install
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LIBS="-ldicl-0.1"
%make_install

rm -f $RPM_BUILD_ROOT/%{_libdir}/libpopt.la

# Multiple popt configurations are possible
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/popt.d

%find_lang %{name}

%check
make check

#%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc CHANGES
%{_sysconfdir}/popt.d
%{_libdir}/libpopt.so.*

%files devel
%doc README
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/popt.h
%{_mandir}/man3/popt.3*

%files static
%{_libdir}/libpopt.a

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Panu Matilainen <pmatilai@redhat.com> - 1.16-16
- Use modern build helper macros
- Drop support for pre-usrmove versions (Fedora < 17 and RHEL < 7)
- Erm, dont nuke build-root at beginning of %%install

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16-13
- Switch to %%ldconfig_scriptlets

* Thu Oct 12 2017 Robert Scheck <robert@fedoraproject.org> 1.16-12
- Added upstream patch to handle glob(3) error returns (#1051685)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Peter Jones <pjones@redhat.com> - 1.16-10
- Make it use %%autosetup -S git
- Fix a memory leak

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Panu Matilainen <pmatilai@redhat.com> - 1.16-4
- Mark license as such, not documentation

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 08 2014 Robert Scheck <robert@fedoraproject.org> 1.16-2
- Added patch to have --help and --usage translatable (#734434)

* Sun Nov 24 2013 Robert Scheck <robert@fedoraproject.org> 1.16-1
- Upgrade to 1.16 (#448286, #999377)
- Tight run-time dependencies between sub-packages via %%{?_isa}
- Added patch for spelling mistakes in popt man page (#675567)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Panu Matilainen <pmatilai@redhat.com> - 1.13-13
- Remove useless doxygen docs to eliminate multilib conflicts (#533829)

* Thu Aug 02 2012 Panu Matilainen <pmatilai@redhat.com> - 1.13-12
- Hack poptBadOption() to return something semi-meaningful on exec alias
  failures (#697435, #710267)
- Run internal test-suite on build, minimal as it might be

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 14 2011 Panu Matilainen <pmatilai@redhat.com>
- Backport upstream patch to fix --opt=<arg> syntax for aliases (#293531)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Robert Scheck <robert@fedoraproject.org> 1.13-7
- Solved multilib problems at doxygen generated files (#517509)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.13-5
- Rebuilt against gcc 4.4 and rpm 4.6

* Sun May 25 2008 Robert Scheck <robert@fedoraproject.org> 1.13-4
- Solved multilib problems at doxygen generated files (#342921)

* Wed Feb 20 2008 Robert Scheck <robert@fedoraproject.org> 1.13-3
- Revert the broken bind_textdomain_codeset() patch (#433324)

* Thu Feb 14 2008 Robert Scheck <robert@fedoraproject.org> 1.13-2
- Added patch to work around missing bind_textdomain_codeset()

* Sun Dec 30 2007 Robert Scheck <robert@fedoraproject.org> 1.13-1
- Upgrade to 1.13 (#290531, #332201, #425803)
- Solved multilib problems at doxygen generated files (#342921)

* Thu Aug 23 2007 Robert Scheck <robert@fedoraproject.org> 1.12-3
- Added buildrequirement to graphviz (#249352)
- Backported bugfixes from CVS (#102254, #135428 and #178413)

* Sun Aug 12 2007 Robert Scheck <robert@fedoraproject.org> 1.12-2
- Move libpopt to /lib[64] (#249814)
- Generate API documentation, added buildrequirement to doxygen

* Mon Jul 23 2007 Robert Scheck <robert@fedoraproject.org> 1.12-1
- Changes to match with Fedora Packaging Guidelines (#249352)

* Tue Jul 10 2007 Jeff Johnson <jbj@rpm5.org>
- release popt-1.12 through rpm5.org.

* Sat Jun  9 2007 Jeff Johnson <jbj@rpm5.org>
- release popt-1.11 through rpm5.org.

* Thu Dec 10 1998 Michael Johnson <johnsonm@redhat.com>
- released 1.2.2; see CHANGES

* Tue Nov 17 1998 Michael K. Johnson <johnsonm@redhat.com>
- added man page to default install

* Thu Oct 22 1998 Erik Troan <ewt@redhat.com>
- see CHANGES file for 1.2

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- added ./configure step to spec file
