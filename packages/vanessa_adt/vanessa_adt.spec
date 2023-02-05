Summary:		Library of Abstract Data Types 
Name:		vanessa_adt
Version:		0.0.9
Release:		10%{?dist}
License:		LGPLv2+
URL:			http://www.vergenet.net/linux/vanessa/
Source0:		http://www.vergenet.net/linux/vanessa/download/%{name}/%{version}/%{name}-%{version}.tar.gz
Requires:		vanessa_logger >= 0.0.5
BuildRequires:	automake autoconf libtool vanessa_logger-devel >= 0.0.5

%description
Library of Abstract Data Types (ADTs) that may be useful.  Includes queue,
dynamic array and key value ADT.

%package		devel
Summary:		Headers for development
Requires:		%{name} = %{version}-%{release}
Requires:		vanessa_logger-devel >= 0.0.5

%description devel
Headers required to develop against vanessa_adt.

%prep
%setup -q

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
if [ -f configure.in ]; then
	aclocal
	libtoolize --force --copy
	automake --add-missing
	autoheader
	autoconf
fi
%configure --disable-static

make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/{etc,%{prefix}/{lib,bin,doc}}
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_libdir}/*.*a

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%doc README COPYING ChangeLog

%files devel
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 17 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.9-1
- Update to version 0.0.9, prepare for epel7 (bz#1140910).
- Some spec cleanup.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 7 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-9
- Remove static libraries mention from description and summary (bz#817948).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 25 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-6
- Add %%{?_smp_mflags}
- End Fedora review.

* Mon Aug 24 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-5
- Fedora Review started. Thanks to Andrew Colin Kissa.
- Historical ./configure with huge amount parameters replaced by %%configure macro.
- Removed unnecessary requires /sbin/ldconfig
- Removed the files README,COPYING from the devel package

* Sun Aug 23 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-4
- Fix typo in condition (confgure.in instead of configure.in) (thanks to Andrew Colin Kissa)
- Add --add-missing flag to automake command and put it before autoheader.

* Tue Aug 18 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.0.7-3
- Ressurect old http://hubbitus.net.ru/rpm/Fedora9/vanessa_adt/vanessa_adt-0.0.7-2.fc8.Hu.0.src.rpm
- Rename spec to classic %%{name}.spec.
- Remove Hu part from release.
- Strip some old comments and unneded commands/macroses.
- Replace $RPM_BUILD_ROOT by %%{buildroot}.
- Move %%doc README COPYING ChangeLog from devel to main package.
- Delete unversioned explicit provides: Provides: %%{name}-%%{version}
- Old BuildPrereq tag replaced by BuildRequires.
- Make setup quiet.
- Remove *.*a files in %%install.
- Add Requires(postun): /sbin/ldconfig, Requires(post): /sbin/ldconfig, and %%post/%%postun ldconfig invoke.
- Move %%{_libdir}/*.so into -devel.
- Add COPYING also in %%doc of -devel, README in all packages.
- In devel turn "Provides: %%{name}-devel-%%{version}" to "%%{name}-devel = %%{version}-%%{release}".
- Add --disable-static in configure options (with it .la file not produced).
- Licence changed to LGPLv2+ from just LGPL.

* Mon Dec 31 2007 Pavel Alexeev <Pahan [ at ] Hubbitus [ DOT ] info> - 0.0.7-2
- Replace Tag Copyright by License
- Change license to it abbriviation LGPL (was GNU Lesser General Public Licence)
- Reformat all with tabs
- Change BuildRoot: to correct (intead of hardcoded path): %%{_tmppath}/%%{name}-%%{version}-%%{release}-%%(%%{__id_u} -n)
- Delete (Comment out) %%define prefix /usr
- Change from Release: 1 to Release: 2%%{?dist}.Hu.0

* Fri Dec 14 2001 Horms <horms@verge.net.au>
  Revamped configure to use %%{_libdir} and friends. This should be more
  distribution indepentant. With thanks to Scot W. Hetzel <scot@genroco.com>

* Sat Sep 2 2000 Horms <horms@verge.net.au>
  created for version 0.0.0
