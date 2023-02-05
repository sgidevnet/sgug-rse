Summary:		Generic logging layer
Name:		vanessa_logger
Version:		0.0.10
Release:		14%{?dist}
License:		LGPLv2+
URL:			http://www.vergenet.net/linux/vanessa/
Source0:		http://www.vergenet.net/linux/vanessa/download/vanessa_logger/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	automake autoconf libtool

%description
Generic logging layer that may be used to log to one or more of syslog,
an open file handle or a file name. Though due to limitations in the
implementation of syslog opening multiple syslog loggers doesn't makes
sense. Includes the ability to limit which messages will be logged based
on priorities.

# As subpackages defined -devel subpackage also must be explicit.
%package	devel
Summary:	Headers for development
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Headers required to develop against vanessa_logger.

%package	sample
Summary:	Example programme that demonstrates vanessa_logger
Requires:	%{name} = %{version}-%{release}

%description	sample
Sample programme with source that demonstrates various features of
vanessa_logger.


%prep
%setup -q

%build

# I am providing my own configure macro replacement. Hopefully this
# will result in fewer portability problems than using the one supplied
# by various vendours. I fear that I hope in vein.
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
if [ -f configure.in ]; then
	aclocal
	libtoolize --force --copy
	automake --add-missing
	autoheader
	autoconf
fi
%configure --disable-static

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_prefix}/doc
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_libdir}/*.*a

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%doc README COPYING ChangeLog

%files devel
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/vanessa-logger.pc
%doc COPYING README

%files sample
%{_bindir}/*
%{_mandir}/man1/vanessa_logger_sample.*
%doc sample/*.c sample/*.h README

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 6 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.10-1
- Update to 0.0.10

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 7 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.8-8
- Remove static libraries mention from description and summary (bz#817949).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 20 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.8-5
- New version 0.0.8

* Mon Aug 24 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-4
- Historical ./configure with huge amount parameters replaced by %%configure macro.
- Removed unnecessary requires /sbin/ldconfig
- Removed the files README,COPYING from the devel package

* Sun Aug 23 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-3
- Fix typo in condition (confgure.in instead of configure.in) (thanks to Andrew Colin Kissa)
- vanessa_logger-sample depend on vanessa_logger not on vanessa_logger-devel (thanks to Andrew Colin Kissa)
- Add --add-missing flag to automake command and put it before autoheader.

* Tue Aug 18 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-2
- Ressurect old http://hubbitus.net.ru/rpm/Fedora9/vanessa_logger/vanessa_logger-0.0.6-1.fc8.Hu.1.src.rpm.
- New version 0.0.7
- Rename spec to classic %%{name}.spec.
- Remove Hu part from release.
- Strip some old comments and unneded commands/macroses.
- Replace $RPM_BUILD_ROOT by %%{buildroot}.
- Move %%doc README COPYING ChangeLog from devel to main package.
- Old BuildPrereq tag replaced by BuildRequires.
- Make setup quiet.
- Adopt patch to new version, and name accordingly: vanessa_logger-0.0.7.error:label_at_end_of_compound_statement.patch.
- Remove *.*a files in %%install.
- License changed to LGPLv2+ from just LGPL according to README.
- Add Requires(postun):	/sbin/ldconfig, Requires(post):	/sbin/ldconfig, and %%post/%%postun ldconfig invoke.
- Move %%{_libdir}/*.so into -devel.
- Add COPYING also in %%doc of -devel, README in all packages.
- Add --disable-static in configure options (with it .la file not produced).

* Mon Dec 31 2007 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] info> - 0.0.6-1
- Replace Tag Copyright by License
- Reformat all with tabs
- Change BuildRoot:	to correct (intead of hardcoded path): %%{_tmppath}/%%{name}-%%{version}-%%{release}-%%(%%{__id_u} -n)
- Delete (Comment out) %%define prefix	/usr
- Change from Release:	1 to Release:	%%{rel}%%{?dist}.Hu.0

* Fri Dec 14 2001 Horms <horms@verge.net.au>
  Revamped configure to use %%{_libdir} and friends. This should be more
  distribution indepentant. With thanks to Scot W. Hetzel <scot@genroco.com>
* Thu Apr 26 2001 Horms <horms@verge.net.au>
  Updated to "work" with Red Hat 7
* Sat Sep 15 2000 Horms <horms@verge.net.au>
  created for version 0.0.0
