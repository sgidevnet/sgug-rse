Summary:		Simplify TCP/IP socket operations
Name:		vanessa_socket
Version:		0.0.12
Release:		15%{?dist}
License:		LGPLv2+
URL:			http://www.vergenet.net/linux/vanessa/
Source0:		http://www.vergenet.net/linux/vanessa/download/%{name}/%{version}/%{name}-%{version}.tar.bz2
Requires:		vanessa_logger >= 0.0.8
BuildRequires:	automake autoconf libtool vanessa_logger-devel >= 0.0.8

%description
Library to simplify TCP/IP socket operations. Includes code to
open a socket to a server as a client, to listen on socket for
clients as a server and to pipe information between sockets.

%package		devel
Summary:		Headers and static libraries for development
Requires:		%{name} = %{version}-%{release}
Requires:		vanessa_logger-devel >= 0.0.8

%description devel
Headers and static libraries required to develop against libvanessa_socket.

%package		pipe
Summary:		Trivial TCP/IP pipe build using libvanessa_adt
License:		GPLv2+
Requires:		%{name} = %{version}-%{release}
# Epel5 have not popt-devel package
%if 0%{?fedora}%{?rhel} > 5
BuildRequires:	popt-devel
%endif

%description pipe
A TCP/IP pipe is a user space programme that listens for TCP/IP connections on
port on the local host and when a client connects makes a connection to a
TCP/IP port, possibly on another host. Once both connections are established
data sent on one connection is relayed to the other, hence forming a
bi-directional pipe.

Uses include enabling connections to specific ports on hosts behind a
packet filter.

This code is intended primarily as an example of how many of the
features of libvanessa_socket work.

%prep
%setup -q

%build
%configure --disable-static

# Disable Rpath for x86_64
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_libdir}/*.*a


%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%doc README COPYING ChangeLog

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files pipe
%{_bindir}/vanessa_socket_pipe
%{_mandir}/man1/vanessa_socket_pipe.*
%doc README vanessa_socket_pipe/COPYING

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 1 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.12-1
- Update to 0.0.12 version.

* Mon Jan 25 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.10-8
- Change License back to LGPLv2+, as clarified by Simon Horman - http://hg.vergenet.net/vanessa/vanessa_socket/rev/1e82bd57c239

* Mon Jan 25 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.10-7
- libvanessa_socket/vanessa_socket_daemon.c is GPLv2+, so all package License change to GPLv2+ from LGPLv2+ (Garrett Holmstrom)
- Cut off strange issue vith rpath appeared only in x86_64 (thanks to Garrett Holmstrom, Joshua Roys)
- Fix forgot version of vanessa_logger-devel >= 0.0.8 (thanks Michael Schwendt).

* Tue Jan 5 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.10-6
- Add %%{?_smp_mflags} for parallel build.
- Remove hand  invoking autotuls, build with existing configure (thanks to Joshua Roys).
- Requires: vanessa_logger updated to version 0.0.8

* Sun Dec 20 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.10-5
- Update to 0.0.10 version.
- BR up to vanessa_logger-devel >= 0.0.8
- Add new files %%{_mandir}/man1/vanessa_gethostbyname.1.gz, %%{_bindir}/vanessa_gethostbyname

* Mon Aug 24 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-4
- Historical ./configure with huge amount parameters replaced by %%configure macro.
- Removed unnecessary requires /sbin/ldconfig
- Removed the files README,COPYING from the devel package

* Sun Aug 23 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-3
- Fix typo in condition (confgure.in instead of configure.in) (thanks to Andrew Colin Kissa)
- In -pipe sabpackage Requires: %%{name}-%%{version} replaced by more precise: %%{name} = %%{version}-%%{release}
- Add --add-missing flag to automake command and put it before autoheader.

* Tue Aug 18 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-2
- Ressurect old http://hubbitus.net.ru/rpm/Fedora9/vanessa_socket/vanessa_socket-0.0.7-1.fc8.Hu.1.src.rpm.
- Rename spec to classic %%{name}.spec.
- Remove Hu part from release.
- Strip some old comments and unneded commands/macroses.
- Replace $RPM_BUILD_ROOT by %%{buildroot}.
- Move %%doc README COPYING ChangeLog from devel to main package.
- Old BuildPrereq tag replaced by BuildRequires.
- Make setup quiet.
- Remove *.*a files in %%install.
- Move %%{_libdir}/*.so into -devel.
- Add Requires(postun):	/sbin/ldconfig, Requires(post):	/sbin/ldconfig, and %%post/%%postun ldconfig invoke.
- Add COPYING also in %%doc of -devel, README in all packages.
- Add --disable-static in configure options (with it .la file not produced).
- License changed to LGPLv2+ for main package and to GPLv2+.

* Mon Dec 31 2007 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] info> - 0.0.7-1
- Replace Tag Copyright by License
- Change BuildRoot:	to correct (intead of hardcoded path): %%{_tmppath}/%%{name}-%%{version}-%%{release}-%%(%%{__id_u} -n)
- Reformat all with tabs
- Delete (Comment out) %%define prefix	/usr
- Change from Release:	1 to Release:	%%{rel}%%{?dist}.Hu.0
- For package pipe Change BuildRequires: popt to BuildRequires: popt-devel

* Fri Dec 14 2001 Horms <horms@verge.net.au>
  Revamped configure to use %%{_libdir} and friends. This should be more
  distribution indepentant. With thanks to Scot W. Hetzel <scot@genroco.com>
* Fri Dec 14 2001 Horms <horms@verge.net.au>
  Use %%configure and %%{_libdir} and friends. This should be more
  distribution indepentant. With thanks to Scot W. Hetzel <scot@genroco.com>
* Mon Feb 12 2001 Horms <horms@verge.net.au>
  Added manual page for vanessa_socket_pipe
* Sat Sep 2 2000 Horms <horms@verge.net.au>
  created for version 0.0.0
