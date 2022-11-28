%global		postver	-r2
%global		postrpmver	%(echo "%postver" | sed -e 's|-|.|g' | sed -e 's|^\.||')

%global		mainver		2.2.7

%global		fedorarel	2
%global		rpmrel		%{fedorarel}%{?postver:.%postrpmver}

Name:		libtcd
Version:	%{mainver}
Release:	%{rpmrel}%{?dist}.8
Summary:	Tide Constituent Database Library
BuildRequires:	gcc

License:	Public Domain
URL:		http://www.flaterco.com/xtide/
Source0:	ftp://ftp.flaterco.com/xtide/%{name}-%{version}%{?postver}.tar.bz2


%description
libtcd provides a software API for reading and writing Tide
Constituent Database (TCD) files.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags} -k

%install
make \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	install

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc *.html

%{_includedir}/*.h
%{_libdir}/*.so

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2.r2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.7-2.rc2
- 2.2.7 respin r2

* Mon Aug 10 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.7-1
- 2.2.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-2.r2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.6-2.r2
- 2.2.6 respin r2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.6-1
- 2.2.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-5.r3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.5-5.r3
- 2.2.5 respin r3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-4.r2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-4.r2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.2.5-4.r2
- 2.2.5 respin r2

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.2.5-3
- F-17: rebuild against gcc47

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.5-1
- 2.2.5

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.4-3
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.4-2
- F-11: Mass rebuild

* Thu Aug 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.4-1
- 2.2.4

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Wed Dec 12 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.3-1
- 2.2.3

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.2-1.dist.2
- Mass rebuild (buildID or binutils issue)

* Mon Jan 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.2-1
- 2.2.2

* Mon Jan 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.1-1
- 2.2.1

* Tue Nov 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2.0.2-1
- 2.2-r2.

* Thu Nov 23 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2-1
- Formal 2.2 release.

* Mon Nov 21 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.2-0.1.dev1
- Re-split from xtide, import to Fedora Extras (see bug 211626)
