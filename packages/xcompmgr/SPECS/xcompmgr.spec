Summary:	X11 composite manager
Name:		xcompmgr
Version:	1.1.7
Release:	8%{?dist}
License:	Copyright only
URL:		http://xapps.freedesktop.org
Source0:	http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:	libX11-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXrender-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libXext-devel
BuildRequires:	pkgconfig

%description
xcompmgr is a sample compositing manager for X servers supporting the XFIXES,
DAMAGE, and COMPOSITE extensions. It enables basic eye-candy effects

%prep
%setup -q 

%build
%configure
make %{?_smp_mflags}

%install
%makeinstall

%files
%doc ChangeLog COPYING README
%{_bindir}/xcompmgr
%{_mandir}/man1/xcompmgr.1.gz

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.7-1
- Rebuilt for new upstream release 1.1.7, fixes rhbz #1213038

* Sat Dec 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.6-9
- Spec clean up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Deji Akingunola <dakingun@gmail.com> - 1.1.6-1
- Update to version 1.1.6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 02 2009 Deji Akingunola <dakingun@gmail.com> - 1.1.5-1
- New release 1.1.5

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.4-1
- New release 1.1.4

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.3-8
- Rebuild for gcc43

* Wed Aug 22 2007 Deji Akingunola <dakingun@gmail.com> - 1.1.3-7
- Update License tag and Rebuild

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 1.1.3-6
- Rebuild for FC6

* Mon Jul 24 2006 Deji Akingunola <dakingun@gmail.com> 1.1.3-5
- Add pkgconfig to the BRs

* Thu Jun 29 2006 Deji Akingunola <dakingun@gmail.com> 1.1.3-4
- Use STL in the license field

* Sat Apr 22 2006 Deji Akingunola <dakingun@gmail.com> 1.1.3-3
- Fix Changelog typo
- Explicitly use MIT license as opposed to to MIT/X11

* Tue Nov 08 2005 Deji Akingunola <dakingun@gmail.com> 1.1.3-2
- Fix rpmlint error on description line
- Package the changelog file as doc

* Tue Nov 08 2005 Deji Akingunola <dakingun@gmail.com> 1.1.3-1
- Initial build.
