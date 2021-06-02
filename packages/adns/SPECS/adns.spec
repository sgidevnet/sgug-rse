Name:		adns
Version:	1.5.1
Release:	8%{?dist}

Summary:	Advanced, easy to use, asynchronous-capable DNS client library

License:	GPL+
URL:		http://www.chiark.greenend.org.uk/~ian/adns/
Source0:	http://www.chiark.greenend.org.uk/~ian/adns/ftp/%{name}-%{version}.tar.gz
BuildRequires:	autoconf, gcc

# http://debbugs.gnu.org/cgi/bugreport.cgi?bug=25757
Patch0:		adns14-rh514838.patch

%description
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
 - It is reasonably easy to use for simple programs which just want to
   translate names to addresses, look up MX records, etc.
 - It can be used in an asynchronous, non-blocking, manner. Many
   queries can be handled simultaneously.
 - Responses are decoded automatically into a natural representation
   for a C program - there is no need to deal with DNS packet formats.
 - Sanity checking (eg, name syntax checking, reverse/forward
   correspondence, CNAME pointing to CNAME) is performed automatically.
 - Time-to-live, CNAME and other similar information is returned in an
   easy-to-use form, without getting in the way.
 - There is no global state in the library; resolver state is an opaque
   data structure which the client creates explicitly. A program can have
   several instances of the resolver.
 - Errors are reported to the application in a way that distinguishes
   the various causes of failure properly.
 - Understands conventional resolv.conf, but this can overridden by
   environment variables.
 - Flexibility. For example, the application can tell adns to: ignore
   environment variables (for setuid programs), disable sanity checks eg
   to return arbitrary data, override or ignore resolv.conf in favour of
   supplied configuration, etc.
 - Believed to be correct ! For example, will correctly back off to TCP
   in case of long replies or queries, or to other nameservers if several
   are available. It has sensible handling of bad responses etc.

%package devel
Summary:	Asynchronous-capable DNS client library - development files
Requires:	%{name} = %{version}

%description devel
Asynchronous-capable DNS client library - development files.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs
Requires:	%{name} = %{version}

%description progs
DNS utility programs: adns also comes with a number of utility
programs for use from the command line and in scripts:
 - adnslogres is a much faster version of Apache's logresolv program,
 - adnsresfilter is a filter which copies its input to its output,
   replacing IP addresses by the corresponding names, without unduly
   delaying the output. For example, you can usefully pipe the output of
   netstat -n, tcpdump -ln, and the like, into it.
 - adnshost is a general-purpose DNS lookup utility which can be used
   easily in from the command line and from shell scripts to do simple
   lookups. In a more advanced mode it can be used as a general-purpose
   DNS helper program for scripting languages which can invoke and
   communicate with subprocesses.

%prep
%setup -q

%patch0 -p1 -b .rh514838

%build
%ifarch sparcv9 sparc64 s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fpic"
%endif
autoreconf -fiv
%configure --enable-dynamic
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    bindir=$RPM_BUILD_ROOT%{_bindir} \
    includedir=$RPM_BUILD_ROOT%{_includedir} \
    libdir=$RPM_BUILD_ROOT%{_libdir} \
    install

rm -f $RPM_BUILD_ROOT%{_libdir}/libadns.a

%ldconfig_scriptlets

%files
%doc README TODO changelog
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so

%files progs
%attr(755,root,root) %{_bindir}/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Tomas Hozza <thozza@redhat.com> - 1.5.1-5
- Added Build dependency on gcc and explicit dependency on main package in -progs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Tomas Hozza <thozza@redhat.com> - 1.5.1-1
- New upstream version 1.5.1 (#1369297)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Adam Tkac <atkac redhat com> - 1.4-12
- adnsresfilter: fix segfault when --brackets option is used (#761513)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 04 2010 Adam Tkac <atkac redhat com> 1.4-9
- update source URL

* Thu Aug 06 2009 Adam Tkac <atkac redhat com> 1.4-8
- rebuild

* Thu Aug 06 2009 Adam Tkac <atkac redhat com> 1.4-7
- don't crash in adns_strerror if parameter is unknown error code (#514838)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 29 2008 Dennis Gilmore <dennis@ausil.us> - 1.4-4
- some arches need -fPIC 

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-3
- Autorebuild for GCC 4.3

* Wed Dec 19 2007 Adam Tkac <atkac redhat com> 1.4-2
- don't ship static libadns.a

* Wed Dec 19 2007 Adam Tkac <atkac redhat com> 1.4-1
- updated to 1.4
- CVS cleanup
- use autoreconf
- build with -fpic instead -fPIC

* Fri Aug 31 2007 Radek Vokál <rvokal@redhat.com> 1.2-6
- rebuilt

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.2-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Radek Vokal <rvokal@redhat.com> 1.2-4
- rebuilt

* Mon May 15 2006 Mihai Ibanescu <misa[AT]redhat.com> 1.2-3
- Rebuilt in the devel branch

* Tue May  9 2006 Mihai Ibanescu <misa[AT]redhat.com> 1.2-2
- Dropped the DESTDIR patch since it was not accepted upstream.
- Added -fPIC in the compiled flags, otherwise we won't be able to link
  against this library.

* Mon May  8 2006 Mihai Ibanescu <misa[AT]redhat.com> 1.2-1
- Updated to 1.2, some of the patches were already upstream
- Removed dependency on autoconf/automake since it builds just fine without
  that

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jul 13 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 0:1.1-0.fdr.4
- Add patch2 to make adns recognize ';' in /etc/resolv.conf
  (#1626, Noa Resare).
- Add patch3 to fix bug and fix build on PPC (#1812, Colin Charles).

* Fri Apr 16 2004 Michel Salim <salimma[AT]users.sf.net> 1.1-0.fdr.3
- Builds using automake 1.5, autoconf 2.13; latest automake/autoconf combination fails on FC2

* Fri Dec 05 2003 Michel Salim <salimma[AT]users.sourceforge.net> 1.1-0.fdr.2
- adns-devel: Added epoch to Requires
- adns-progs: Removed superfluous dependency on adns
- adns-progs: Changed group to Applications/System

* Mon Oct 27 2003 Michel Salim <salimma[AT]users.sourceforge.net> 1.1-0.fdr.1
- Updated to 1.1.

* Sat Jun 07 2003 Michel Salim <salimma[AT]users.sourceforge.net> 1.0-4
- Based on PLD spec.
