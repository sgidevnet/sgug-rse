%define debug_package %{nil}
# $Revision: 1.4 $, $Date: 2017/03/27 17:07:55 $
Summary:	Character set conversion library
Name:		libiconv
Version:	1.16
Release:	1%{?dist}
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libiconv/%{name}-%{version}.tar.gz
URL:		http://www.haible.de/bruno/packages-libcharset.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:  gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch x86_64
Provides:	libiconv.so.2()(64bit)
Provides:	libcharset.so.1()(64bit)
%else
Provides:	libiconv.so.2
Provides:	libcharset.so.1
%endif

%description
This library provides an iconv() implementation, for use on systems
which don't have one, or whose implementation cannot convert from/to
Unicode.

# Here's a terminator

%package devel
Summary:	libiconv header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains libiconv header files.

%package static
Summary:	libiconv static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libiconv library.

%package utils
Summary:	iconv utility
License:	GPL v3+
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description utils
iconv utility.

%prep
%setup -q
#%patch1 -p1
#%if 0%{?fedora} >= 20 || 0%{?centos} >= 7
#%patch2 -p1
#%endif

rm -f po/stamp-po

%build
#cp `which libtool` libtool
#cp -f %{_prefix}/usr/share/automake*/config.sub build-aux
#cp -f /usr/share/automake*/config.sub libcharset/build-aux
#%{__aclocal} -I m4 -I srcm4
#%{__autoconf}
aclocal -I m4 -I srcm4
autoconf
export CPPFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS $CPPFLAGS"
%configure --enable-static --enable-dynamic
#%{__make}
%make_build

%install
rm -rf $RPM_BUILD_ROOT

#%{__make} install DESTDIR=$RPM_BUILD_ROOT
%make_install DESTDIR=$RPM_BUILD_ROOT
#if [ -d $RPM_BUILD_ROOT%{_prefix}/%{_lib} ]; then ln -s %{_lib} $RPM_BUILD_ROOT%{_prefix}/%{_lib}; fi

#mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
#echo "%{_libdir}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf


%find_lang %{name}

%clean
#rm -rf $RPM_BUILD_ROOT

#%post	-p /sbin/ldconfig
#%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING COPYING.LIB DEPENDENCIES DESIGN HACKING INSTALL.generic NEWS NOTES README THANKS
%attr(755,root,root) %{_libdir}/libcharset.so.*.*.*
%{_libdir}/libcharset.so.1
%attr(755,root,root) %{_libdir}/libiconv.so.*.*.*
%{_libdir}/libiconv.so.2
##%attr(755,root,root) %{_libdir}/preloadable_libiconv.so
##%attr(644,root,root) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
##%ifarch x86_64
##%attr(755,root,root) %{_prefix}/lib
##%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcharset.so
%{_libdir}/libiconv.so
%{_libdir}/libcharset.la
%{_libdir}/libiconv.la
%{_includedir}/iconv.h
%{_includedir}/libcharset.h
%{_includedir}/localcharset.h
%{_mandir}/man3/iconv*.3*
%{_docdir}/iconv*.html

%files static
%defattr(644,root,root,755)
%{_libdir}/libcharset.a
%{_libdir}/libiconv.a
#{_libdir}/charset.alias

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iconv
%{_mandir}/man1/iconv.1*

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* Mon Mar 27 2017 Lawrence R. Rogers <lrr@cert.org> 1.14-3
	New in 1.15:
	* The UTF-8 converter now rejects surrogates and out-of-range code points.
	* Added ISO-2022-JP-MS converter.
	* Updated the CP1255 converter to map one more character.
	* The functions now support strings longer than 2 GB.

* Fri Feb 1 2013 Lawrence R. Rogers <lrr@cert.org> 1.14-3
- only packages /usr/libiconv/lib for x86_64 architectures.
  This packaging error caused duplication of files in the libiconv and libiconv-devel packages

* Fri Nov 30 2012 Lawrence R. Rogers <lrr@cert.org> 1.14-2
* Release 1.14-2
	Now creates the needed /etc/ld.so.conf.d/libiconv-%arch.conf file
	Also creates a link from lib to lib64 on x86_64 architectures

	Revision 1.14  2008/04/08 08:24:53  glen
	- unify ftp.gnu.org urls

	Revision 1.13  2007-11-30 21:14:54  qboosh
	- libiconv is on LGPL v2+, but iconv utility is GPL v3+ now

	Revision 1.12  2007-11-30 20:26:16  qboosh
	- up to 1.12
	- updated pl.po-update patch

	Revision 1.11  2007-02-13 06:46:51  glen
	- tabs in preamble

	Revision 1.10  2007/02/12 00:49:02  baggins
	- converted to UTF-8

	Revision 1.9  2006/07/22 07:46:57  qboosh
	- updated to 1.11, updated pl.po-update patch

	Revision 1.8  2005/08/15 00:00:52  qboosh
	- updated to 1.10, added pl.po-update patch

	Revision 1.7  2004/09/01 16:11:10  adamg
	- kill pld.org.pl leftovers

	Revision 1.6  2004/03/14 23:12:48  qboosh
	- added iconv.h to -devel (yes, C: glibc-devel - but it doesn't make sense with glibc)
	- strict internal deps

	Revision 1.5  2004/02/14 21:47:01  undefine
	- copy config.sub. mayby it help on amd64.. mayby not... who know?
	- release 2

	Revision 1.4  2004/01/27 21:01:50  qboosh
	- 1.9.2

	Revision 1.3  2003/10/08 21:41:20  qboosh
	- 1.9.1, added pl description, removed obsolete DESTDIR patch

	Revision 1.2  2003/09/10 16:30:49  gotar
	- md5

	Revision 1.1  2003/09/10 16:26:07  gotar
	- just in case
